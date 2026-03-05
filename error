
import os
import json
import time
import re
from typing import List, Dict, Any, Tuple, Optional

import pandas as pd
import fitz  # PyMuPDF for PDF text extraction
from fpdf import FPDF

from openai import OpenAI



TRACE_LOG: List[str] = []
DEBUG_MODE_ENABLED: bool = True
TRACE_LOG_MAX_LINES: int = 200


def log_trace(message: Any, level: str = "INFO") -> None:
    
    global TRACE_LOG

    if not DEBUG_MODE_ENABLED and level == "DEBUG":
        return

    timestamp = time.strftime("%H:%M:%S")
    full_message = f"[{timestamp}][{level}] {str(message)}"
    TRACE_LOG.append(full_message)

    if len(TRACE_LOG) > TRACE_LOG_MAX_LINES:
        TRACE_LOG.pop(0)

    
    if level in ("ERROR", "WARN"):
        print(full_message)


def get_trace_log() -> List[str]:
    """Return a copy of the current trace log."""
    return list(TRACE_LOG)


# ============================================================
#  PDF UTILITIES
# ============================================================

def create_pdf(text_content: str, filename: str = "output.pdf") -> bytes:
    """
    Create a simple PDF (bytes) from text_content.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    page_width = pdf.w - 2 * pdf.l_margin
    for line in text_content.split("\n"):
        words = line.split(" ")
        current_line = ""
        for word in words:
            if pdf.get_string_width(current_line + " " + word) < page_width:
                current_line += " " + word if current_line else word
            else:
                pdf.cell(0, 5, current_line, ln=True)
                current_line = word
        if current_line:
            pdf.cell(0, 5, current_line, ln=True)
        pdf.ln(2)

    return pdf.output(dest="S").encode("latin-1")


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    
    text_chunks = []
    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text_chunks.append(page.get_text())
    except Exception as ex:
        log_trace(f"Error extracting PDF text: {type(ex).__name__} - {ex}", "ERROR")
        return ""
    return "\n".join(text_chunks)


# ============================================================
#  OPENAI CLIENT + LLM WRAPPER
# ============================================================

_openai_client: Optional[OpenAI] = None
DEFAULT_GPT_MODEL = "gpt-4.1-mini"  


def _init_openai_client_if_needed() -> None:
    global _openai_client
    if _openai_client is None:
        
        _openai_client = OpenAI()
        log_trace("OpenAI client initialized.", "DEBUG")


def query_model(
    model: str,
    user_prompt: str,
    system_prompt: Optional[str] = None,
    image_bytes: Optional[bytes] = None,
    image_mime_type: Optional[str] = None,
    pdf_text: Optional[str] = None,
    tries: int = 2,
    timeout_val_for_retry: float = 2.0,
) -> str:

    _init_openai_client_if_needed()

    last_exception = None

    
    combined_prompt = ""
    if pdf_text:
        combined_prompt += f"[PDF_CONTENT_START]\n{pdf_text}\n[PDF_CONTENT_END]\n\n"
    combined_prompt += user_prompt

    for attempt in range(tries):
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": combined_prompt})

            resp = _openai_client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.1,
                max_completion_tokens=2048,
            )
            ans = resp.choices[0].message.content or ""
            log_trace(
                f"OpenAI model '{model}' answered, len={len(ans)}.", "DEBUG"
            )
            return ans.strip()

        except Exception as ex:
            last_exception = ex
            log_trace(
                f"Error in query_model (attempt {attempt+1}/{tries}) for '{model}': "
                f"{type(ex).__name__} - {ex}",
                "ERROR",
            )
            if attempt < tries - 1:
                time.sleep(timeout_val_for_retry)

    return f"ERROR: LLM query failed after {tries} attempts. Last error: {last_exception}"


# ============================================================
#  THINKING PROCESS PARSER
# ============================================================

def parse_llm_response_with_thinking(
    response_text: str, agent_name: str = "UnknownAgent"
) -> Tuple[str, str]:
    """
    Extract <thinking_process>...</thinking_process> from an LLM response.
    Returns (thinking_process, actionable_text_without_tags).
    """
    if not response_text:
        return "", ""

    pattern = re.compile(
        r"<thinking_process>(.*?)</thinking_process>", re.DOTALL | re.IGNORECASE
    )
    match = pattern.search(response_text)

    if not match:
        log_trace(
            f"No <thinking_process> tags found for {agent_name}. Using full text as actionable.",
            "DEBUG",
        )
        return "", response_text.strip()

    thinking = match.group(1).strip()
    actionable_text = (
        response_text[: match.start()] + response_text[match.end() :]
    ).strip()

    log_trace(
        f"Parsed thinking for {agent_name}, length={len(thinking)}, "
        f"actionable length={len(actionable_text)}",
        "DEBUG",
    )
    return thinking, actionable_text


# ============================================================
#  PATIENT SUMMARY & INTENT DETECTION
# ============================================================

def get_patient_summary_and_missing_fields(
    conversation_history: List[Dict[str, Any]],
    patient_profile: Optional[Dict[str, Optional[str]]] = None,
) -> Tuple[str, List[str]]:
    """
    Build a concise clinical summary from conversation history + patient profile,
    and compute which key fields are missing.
    """
    known_facts = {
        "age": None,
        "gender": None,
        "weight": None,
        "height": None,
        "medications": [],
        "allergies": [],
        "major_dx": [],
        "key_symptoms": [],
    }

    if patient_profile:
        known_facts["age"] = patient_profile.get("age") or known_facts["age"]
        known_facts["gender"] = patient_profile.get("gender") or known_facts["gender"]
        known_facts["weight"] = patient_profile.get("weight") or known_facts["weight"]
        known_facts["height"] = patient_profile.get("height") or known_facts["height"]

    for turn in conversation_history:
        role = turn.get("role", "")
        content = (turn.get("content") or "").strip()
        if not content:
            continue

        lower = content.lower()

        # Age
        age_match = re.search(r"\b(\d{1,2})\s*years?\s*old\b", lower)
        if not known_facts["age"] and age_match:
            known_facts["age"] = age_match.group(1)

        # Gender
        if not known_facts["gender"]:
            if "i am male" in lower or "i'm male" in lower:
                known_facts["gender"] = "Male"
            elif "i am female" in lower or "i'm female" in lower:
                known_facts["gender"] = "Female"

        # Medications
        if "medication" in lower or "medicine" in lower or "pill" in lower:
            known_facts["medications"].append(content)

        # Allergies
        if "allergic" in lower or "allergy" in lower:
            known_facts["allergies"].append(content)

        # Major diagnoses
        if "diagnosed with" in lower or "history of" in lower:
            known_facts["major_dx"].append(content)

        # Key symptoms 
        if role == "user":
            if any(
                term in lower
                for term in [
                    "pain",
                    "fever",
                    "cough",
                    "headache",
                    "nausea",
                    "vomit",
                    "dizzy",
                    "rash",
                    "swelling",
                    "infection",
                ]
            ):
                known_facts["key_symptoms"].append(content)

    lines = []
    lines.append(f"Age: {known_facts['age'] or 'Unknown'}")
    lines.append(f"Gender: {known_facts['gender'] or 'Unknown'}")
    lines.append(f"Weight: {known_facts['weight'] or 'Unknown'}")
    lines.append(f"Height: {known_facts['height'] or 'Unknown'}")

    lines.append(
        "Key Symptoms: "
        + (
            "; ".join(known_facts["key_symptoms"])
            if known_facts["key_symptoms"]
            else "Not clearly specified yet."
        )
    )
    lines.append(
        "Medications (mentioned in conversation): "
        + (
            "; ".join(known_facts["medications"])
            if known_facts["medications"]
            else "None explicitly mentioned."
        )
    )
    lines.append(
        "Allergies (mentioned in conversation): "
        + (
            "; ".join(known_facts["allergies"])
            if known_facts["allergies"]
            else "None explicitly mentioned."
        )
    )
    lines.append(
        "Past diagnoses / major conditions: "
        + (
            "; ".join(known_facts["major_dx"])
            if known_facts["major_dx"]
            else "None clearly stated."
        )
    )

    summary_text = "\n".join(lines)

    missing_fields: List[str] = []
    if not known_facts["age"]:
        missing_fields.append("Age")
    if not known_facts["gender"]:
        missing_fields.append("Gender")
    if not known_facts["medications"]:
        missing_fields.append("Current Medications")
    if not known_facts["allergies"]:
        missing_fields.append("Allergies")

    return summary_text, missing_fields


def detect_intent(user_input: str) -> str:
    """
    Rough intent classifier used by the doctor agent.
    """
    user_input_lower = user_input.lower().strip()

    non_human_terms = [
        "dog",
        "cat",
        "pet",
        "puppy",
        "kitten",
        "animal",
        "bird",
        "hamster",
        "fish",
        "vet",
    ]
    human_context_terms = [
        "i'm",
        "my",
        "i feel",
        "me",
        "myself",
        "patient",
        "human",
        "person",
    ]
    is_non_human = any(term in user_input_lower for term in non_human_terms)
    is_human_context = any(term in user_input_lower for term in human_context_terms)
    if is_non_human and not is_human_context:
        return "non_human"

    emotional_terms = [
        "love",
        "relationship",
        "crush",
        "heartbreak",
        "feeling down",
        "sad",
        "anxious",
        "depressed",
        "lonely",
        "stress",
        "overwhelmed",
        "dating",
        "partner",
        "boyfriend",
        "girlfriend",
        "wife",
        "husband",
        "break up",
        "feelings",
        "advice on my",
        "need advice",
        "trouble with",
    ]
    if any(term in user_input_lower for term in emotional_terms) and not any(
        phys in user_input_lower
        for phys in ["heart", "chest", "panic attack", "heart rate"]
    ):
        return "emotional_support"

    no_concern_terms = [
        "no health concern",
        "don't have any concern",
        "im fine",
        "i'm fine",
        "nothing wrong",
        "no issues",
        "just looking",
        "exploring",
        "no medical problem",
        "not applicable",
        "no complaints",
        "no medical issues",
    ]
    if any(term in user_input_lower for term in no_concern_terms):
        return "no_concern"

    physical_terms = [
        "pain",
        "fever",
        "cough",
        "headache",
        "stomach",
        "nausea",
        "vomit",
        "dizzy",
        "rash",
        "injury",
        "bleed",
        "blood",
        "swelling",
        "infection",
        "test results",
        "symptom",
        "medical",
        "health",
        "doctor",
        "illness",
        "condition",
        "unwell",
        "sick",
        "prescription",
        "medication",
        "treatment",
        "diagnosis",
        "pills",
        "appointment",
    ]
    if any(term in user_input_lower for term in physical_terms):
        return "physical_health"

    return "unknown_or_general"


# ============================================================
#  AGENTS
# ============================================================

class DoctorAgent:
    def __init__(self, model: str, max_infs: int = 25, bias_present: Optional[str] = None):
        self.infs = 0
        self.MAX_INFS = max_infs
        self.model = model
        self.bias_present = None if str(bias_present).lower() == "none" else bias_present
        self.diff_cad = ""

    def generate_bias(self) -> str:
        return {
            "confirmation": "\nBias:Seek disconfirming evidence.\n",
            "recency": "\nBias:Recent case.Focus on current pt.\n",
        }.get(self.bias_present, "")

    def _get_img_request_instruction_text(self) -> str:
        return (
            " If an image is crucial, state CLEARLY ON A NEW LINE: "
            "'REQUEST IMAGE UPLOAD: [image description, e.g. Chest X-ray]'."
        )

    def _get_pdf_request_instruction_text(self) -> str:
        return (
            " If a PDF document is crucial, state CLEARLY ON A NEW LINE: "
            "'REQUEST PDF DOCUMENT: [document description, e.g., Lab Results]'."
        )

    def system_prompt_template(
        self,
        state_for_medical_flow: str,
        patient_summary: str,
        image_content_provided_this_turn: bool = False,
        pdf_content_provided_this_turn: bool = False,
    ) -> str:
        bias = self.generate_bias()
        img_instr = self._get_img_request_instruction_text()
        pdf_instr = self._get_pdf_request_instruction_text()

        img_ctx_instr = (
            "\nIMPORTANT: An interpretation/description of an image was provided by the system. "
            "Consider this information carefully."
            if image_content_provided_this_turn
            else ""
        )
        pdf_ctx_instr = (
            "\nIMPORTANT: Content from a PDF document was provided by the system. Review it carefully."
            if pdf_content_provided_this_turn
            else ""
        )

        thinking_instr = (
            "\n\nBefore your main response/action, first provide your detailed step-by-step reasoning "
            "and plan within <thinking_process> and </thinking_process> tags. After this block, provide "
            "your actual conversational response or structured output."
        )

        meta_prompt_self_correction = (
            "\n\n**CRITICAL SELF-CORRECTION & CONTEXT INSTRUCTION:**\n"
            "1. **USE THE SUMMARY & HISTORY:** Review the clinical summary and conversation history on every turn. "
            "Do not ask for information already provided.\n"
            "2. **STOP AND ACT:** If a patient cannot provide a requested test result, do not loop. "
            "Acknowledge the lack of data and proceed to a provisional diagnosis and management plan.\n"
            "3. **HANDLE PATIENT REFUSAL:** If the patient refuses a critical test, respect it but still propose a "
            "provisional diagnosis and symptomatic management and conclude with `DIAGNOSIS READY: [Diagnosis] (provisional)`.\n"
            "4. **PIVOT AFTER NEGATIVE WORKUP:** If major tests are normal but symptoms are significant, acknowledge that "
            "serious pathology is likely ruled out and provide a diagnosis of exclusion and robust symptom management.\n"
            "5. **PROVIDE ROBUST PLANS:** For significant symptoms (e.g., pain > 6/10), give specific actions and follow-up.\n"
            "6. **CONCLUDE CONFIDENTLY:** Once a plan is agreed, conclude with a short summary and "
            "`DIAGNOSIS READY: [Final Diagnosis]`.\n"
        )

        general_prefix = (
            "You are an AI doctor in a simulated consultation, talking directly to the patient.\n"
            "You must think clinically, systematically, and clearly.\n"
            "Your tone must be empathetic, professional, and conversational."
            f" {bias} {meta_prompt_self_correction}\n"
            f"**Your Primary Goal is to reach a plausible diagnosis.**\n\n"
            f"--- CLINICAL SUMMARY OF KNOWN FACTS ---\n{patient_summary}\n------------------------------------"
        )

        scope_guard_medical = (
            "\nIMPORTANT: If the patient's latest query is clearly NOT about a human health concern for themselves "
            "(e.g., about a pet or vehicle), you MUST politely state your limitation to human medical topics and ask "
            "if they have a human health issue to discuss."
        )

        prompts_medical = {
            "greeting_and_symptom_exploration": (
                "Goal: Greet the patient warmly and briefly, then ask an open-ended question about their symptoms."
                f" {thinking_instr} {img_instr}{pdf_instr}"
            ),
            "diagnostic_process": (
                f"Goal: Continue the diagnostic process. {img_ctx_instr}{pdf_ctx_instr}{thinking_instr} "
                "Based on the conversation and the clinical summary, you can:\n"
                "1. Ask clarifying questions.\n"
                "2. Ask for relevant history not yet provided.\n"
                "3. Propose a differential diagnosis list ('CANDIDATE_DISEASES_START...END').\n"
                "4. Request a test or imaging procedure ('REQUEST TEST: [Test Name]' or 'REQUEST IMAGE UPLOAD: [Image Name]').\n"
                "5. Propose a provisional prescription for severe symptoms ('PROPOSE PROVISIONAL TREATMENT: [Medication and purpose]').\n"
                "6. State a final diagnosis ('DIAGNOSIS READY: [Diagnosis]')."
                f"{img_instr}{pdf_instr}"
            ),
        }

        specific_state_prompt = prompts_medical.get(
            state_for_medical_flow, prompts_medical["diagnostic_process"]
        )
        return general_prefix + scope_guard_medical + specific_state_prompt

    def _compile_history_for_prompt(
        self, hist_sess: List[Dict[str, Any]], max_turns_to_include: int = 8
    ) -> str:
        s_lines = []
        idx = max(0, len(hist_sess) - max_turns_to_include)
        rel_hist = hist_sess[idx:]

        for t in rel_hist:
            r = t.get("role", "")
            c = t.get("content", "")

            if r.startswith("system_"):
                c_summary = f"[{r.replace('_', ' ').title()} provided]"
            else:
                c_summary = c

            r_disp = (
                r.replace("_", " ")
                .title()
                .replace("User", "Patient")
                .replace("Assistant", "Doctor")
                .replace("System Ddx", "DrNotes(DDx)")
                .replace("System File Info", "Sys(File)")
                .replace("System Test Result", "Sys(TestRslt)")
                .replace("System Test Safety", "Sys(TestSafe)")
                .replace("System Provisional Rx", "Sys(ProvRx)")
            )

            s_lines.append(f'{r_disp}: "{c_summary}"')

        return "\n\n".join(s_lines).strip()

    def inference_doctor(
        self,
        last_input_from_patient_or_system: str,
        conversation_history_from_session: List[Dict[str, Any]],
        patient_summary: str,
        intent_override: str = "physical_health",
        is_initial_turn: bool = False,
        image_content_provided_this_turn: bool = False,
        pdf_content_provided_this_turn: bool = False,
    ) -> Dict[str, Any]:
        """
        Main doctor agent call. Returns:
          {
            "text": str,
            "is_ddx_turn": bool,
            "ddx_list_text": Optional[str],
            "thinking_process": Optional[str],
          }
        """
        log_trace(f"--- Dr Turn {self.infs + 1} ---", "INFO")

        action_output = {
            "text": "",
            "is_ddx_turn": False,
            "ddx_list_text": None,
            "thinking_process": None,
        }

        if self.infs >= self.MAX_INFS:
            action_output["text"] = (
                "We have reached the maximum number of doctor turns "
                "for this simulated consultation."
            )
            return action_output

        # Intent guardrails
        if intent_override == "non_human":
            action_output["text"] = (
                "I'm designed to discuss human medical issues. It sounds like your "
                "question may be about a non-human. Please consult a veterinarian or "
                "let me know if you have a human health concern."
            )
            return action_output

        if intent_override == "emotional_support":
            action_output["text"] = (
                "I understand you're going through something emotionally difficult. "
                "While I'm focused on medical topics here, it may help to speak with a "
                "mental health professional or a trusted person. If you ever feel in crisis, "
                "please seek urgent help immediately."
            )
            return action_output

        if intent_override == "no_concern":
            action_output["text"] = (
                "Thanks for letting me know you don't have a current health concern. "
                "If anything changes, I'm here to help you think through symptoms and next steps."
            )
            return action_output

        state_for_med_flow = (
            "greeting_and_symptom_exploration" if is_initial_turn else "diagnostic_process"
        )

        sys_prompt = self.system_prompt_template(
            state_for_medical_flow=state_for_med_flow,
            patient_summary=patient_summary,
            image_content_provided_this_turn=image_content_provided_this_turn,
            pdf_content_provided_this_turn=pdf_content_provided_this_turn,
        )

        hist_str = self._compile_history_for_prompt(conversation_history_from_session)
        usr_prompt = (
            f"--- Conversation History (Recent) ---\n{hist_str}\n\n"
            f"--- Latest Input (from patient or system) ---\n{last_input_from_patient_or_system}"
        )

        full_response = query_model(self.model, usr_prompt, sys_prompt)
        thinking_process, actionable_text = parse_llm_response_with_thinking(
            full_response, "DoctorAgent"
        )

        # Extract candidate diseases list if present
        ddx_pattern = re.compile(
            r"CANDIDATE_DISEASES_START(.*?)CANDIDATE_DISEASES_END",
            re.DOTALL | re.IGNORECASE,
        )
        ddx_match = ddx_pattern.search(actionable_text)
        ddx_list_text = None
        is_ddx_turn = False

        if ddx_match:
            ddx_list_text = ddx_match.group(1).strip()
            is_ddx_turn = True

        action_output["text"] = actionable_text.strip()
        action_output["is_ddx_turn"] = is_ddx_turn
        action_output["ddx_list_text"] = ddx_list_text
        action_output["thinking_process"] = thinking_process

        self.infs += 1
        return action_output


class MeasurementAgent:
    def __init__(self, model: str):
        self.model = model

    def inference_measurement(self, requested_test_name: str, user_entered_results: str) -> str:
        log_trace(
            f"MeasureAgent for:{requested_test_name}, Res:{user_entered_results[:50]}..",
            "INFO",
        )
        sys_prompt = (
            "AI assistant for medical simulation. "
            "Doctor requested: '[Test Name]'. User provided: '[User-Entered Test Results Text]'. "
            "First provide reasoning within <thinking_process>...</thinking_process>. "
            "Then, provide a clear formatted result. ALWAYS start the final output with:\n"
            f"'RESULTS FOR {requested_test_name.upper()}: '"
        )

        usr_prompt = (
            f'Test:"{requested_test_name}"\n'
            f'Results:"{user_entered_results}"\n'
            "Task: Provide thinking process, then the formatted results line as specified."
        )

        full_ans = query_model(self.model, usr_prompt, sys_prompt)
        thinking_process, actionable_ans = parse_llm_response_with_thinking(
            full_ans, "MeasurementAgent"
        )

        kwd = f"RESULTS FOR {requested_test_name.upper()}:"
        if not actionable_ans.upper().startswith(kwd):
            final_ans = f"{kwd} {actionable_ans}"
        else:
            final_ans = actionable_ans

        log_trace(f"FmtdMeasure:{final_ans[:100]}..", "DEBUG")
        return final_ans


class DDIDatabase:
    def __init__(self, csv_fp: str = "db_drug_interactions.csv"):
        self.p: Dict[Tuple[str, str], str] = {}
        self.e: Optional[str] = None

        try:
            df = pd.read_csv(csv_fp)
            if len(df.columns) < 3:
                self.e = f"DDI CSV '{csv_fp}' has <3 cols."
                log_trace(self.e, "ERROR")
                return

            df.iloc[:, 0] = (
                df.iloc[:, 0].fillna("").astype(str).str.lower().str.strip()
            )
            df.iloc[:, 1] = (
                df.iloc[:, 1].fillna("").astype(str).str.lower().str.strip()
            )
            interaction_col_idx = 2
            for _, r in df.iterrows():
                drug1, drug2, interaction_desc = (
                    r.iloc[0],
                    r.iloc[1],
                    r.iloc[interaction_col_idx],
                )
                if drug1 and drug2:
                    self.p[tuple(sorted((drug1, drug2)))] = str(interaction_desc)
        except FileNotFoundError:
            self.e = f"DDI CSV '{csv_fp}' missing."
            log_trace(self.e, "ERROR")
        except Exception as ex:
            self.e = f"Err DDI CSV '{csv_fp}':{type(ex).__name__}-{ex}"
            log_trace(self.e, "ERROR")

    def check_interaction(self, d1: str, d2: str) -> Optional[str]:
        if not self.p:
            return None
        return self.p.get(tuple(sorted((d1.lower().strip(), d2.lower().strip()))))


class PrescriptionWriterAgent:


    def __init__(self, model: str):
        self.model = model

    def get_system_prompt(self, purpose: str, summary: str) -> str:
        return (
            "You are an AI simulating a prescription writer. FOR SIMULATION ONLY. "
            "First, provide your step-by-step thinking process within <thinking_process> and </thinking_process> tags. "
            f"This should include how you select medications based on the purpose ('{purpose}') and patient context, "
            "considering potential contraindications or interactions mentioned in the patient summary. Then, generate "
            "the sample prescription. State SIMULATION ONLY. Use placeholder patient details.\n"
            f"PATIENT CONTEXT:\n{summary}\n\n"
            "Your final prescription must clearly separate medications, dosing, frequency, and warnings.\n"
            "Wrap the final prescription in a block that starts with 'SIMULATED PRESCRIPTION' and ends with "
            "'--- END PRESCRIPTION FORMAT ---'."
        )

    def write_prescription(self, purpose: str, summary: str) -> str:
        sys_prompt = self.get_system_prompt(purpose, summary)
        usr_prompt = (
            "Task: Generate a simulated prescription for the above purpose & patient context. "
            "Follow the instructions strictly."
        )

        full_response = query_model(self.model, usr_prompt, sys_prompt)
        thinking_process, actionable_rx_text = parse_llm_response_with_thinking(
            full_response, "PrescriptionWriterAgent"
        )

        s_tag = "SIMULATED PRESCRIPTION"
        e_tag = "--- END PRESCRIPTION FORMAT ---"
        s_idx = actionable_rx_text.upper().find(s_tag)
        parsed_rx_content = actionable_rx_text

        if s_idx != -1:
            parsed_rx_content = actionable_rx_text[s_idx:]
            e_idx_relative = parsed_rx_content.upper().find(e_tag)
            if e_idx_relative != -1:
                parsed_rx_content = parsed_rx_content[
                    : e_idx_relative + len(e_tag)
                ].strip()
        else:
            log_trace(
                f"RxWriter could not find start tag '{s_tag}' in: {actionable_rx_text[:200]}.",
                "WARN",
            )

        log_trace(
            f"RxWriter Final Parsed Rx (start):{parsed_rx_content[:200]}.", "DEBUG"
        )
        return parsed_rx_content.strip()


class SafetyAgent:


    def __init__(self, ddi_db: DDIDatabase, model: str):
        self.ddi_db = ddi_db
        self.model = model

    def _parse_medications_from_prescription(
        self, prescription_text: str
    ) -> List[str]:
        medications = set()
        patterns = [
            r"^\s*\d+\.\s*Medication Name:\s*\[?([^;(\[]+)\]?",
            r"^\s*Medication Name:\s*\[?([^;(\[]+)\]?",
            r"^\s*Rx:\s*\[?([^;(\[]+)\]?",
            r"^\s*\d+\.\s*([A-Za-z0-9\s-]+?)\s*(?:\d|\(|\[|$)",
        ]
        excluded_terms = {
            "secondary medication",
            "primary medication",
            "medication name",
            "suggest plausible primary medication",
            "medication",
            "name",
            "rx",
            "dosage",
            "form",
            "route",
            "frequency",
            "duration",
            "quantity",
            "refills",
            "sig",
            "instructions",
            "additional instructions",
            "patient",
            "date",
            "prescribing doctor",
            "license",
            "signature",
            "simulated prescription",
            "educational purposes only",
            "consult healthcare professional",
            "dr. agent",
        }
        for line in prescription_text.splitlines():
            if not line.strip():
                continue
            for pattern_str in patterns:
                match = re.search(pattern_str, line.strip(), re.IGNORECASE)
                if match and match.group(1):
                    candidate = match.group(1).strip()
                    candidate = re.sub(
                        r"\s+\d+(\.\d+)?\s*(mg|ml|mcg|g|iu|units?|puff[s]?|application[s]?)\b.*",
                        "",
                        candidate,
                        flags=re.I,
                    ).strip()
                    candidate = re.sub(
                        r"\s+(tablet|capsule|oral|topical|inhaler|injection|solution|cream|ointment|syrup|suspension|sublingual|intravenous|intramuscular|subcutaneous|transdermal|otic|ophthalmic)\b.*",
                        "",
                        candidate,
                        flags=re.I,
                    ).strip()
                    candidate = re.sub(
                        r"\s+(QD|BID|TID|QID|QHS|Q\d+H|PRN)\b.*",
                        "",
                        candidate,
                        flags=re.I,
                    ).strip()
                    candidate = candidate.strip(".,[]()-:")
                    if (
                        candidate
                        and len(candidate) > 2
                        and candidate.lower() not in excluded_terms
                        and not candidate.lower().startswith("e.g.,")
                    ):
                        medications.add(candidate.lower())
                        break
        return [med.capitalize() for med in medications]

    def perform_safety_check(self, rx_txt: str, summary: str) -> str:
        log_trace("SafetyAgent check Rx. Initiating safety check.", "SYSTEM_EVENT")

        meds = self._parse_medications_from_prescription(rx_txt)
        dd_interactions = []

        if self.ddi_db and meds:
            for i in range(len(meds)):
                for j in range(i + 1, len(meds)):
                    d1, d2 = meds[i], meds[j]
                    interaction = self.ddi_db.check_interaction(d1, d2)
                    if interaction:
                        dd_interactions.append((d1, d2, interaction))

        sys_prompt = (
            "You are a safety-focused clinical reasoning agent. You will review a simulated prescription and "
            "a clinical summary. Identify potential safety issues (DDIs, contraindications, dosing concerns, allergies, etc.).\n\n"
            "First, provide detailed reasoning within <thinking_process>...</thinking_process>.\n"
            "Then, provide a concise safety assessment. Do NOT provide a new prescription."
        )
        usr_prompt = (
            f"--- CLINICAL SUMMARY ---\n{summary}\n\n"
            f"--- SIMULATED PRESCRIPTION ---\n{rx_txt}\n\n"
            f"--- Structured DDI Database Findings ---\n{json.dumps(dd_interactions, indent=2)}\n\n"
            "Task: Analyze overall safety, referencing DDI findings where relevant.\n"
        )

        full_response = query_model(self.model, usr_prompt, sys_prompt)
        thinking_process, actionable_text = parse_llm_response_with_thinking(
            full_response, "SafetyAgent"
        )
        return actionable_text.strip()


class TestSafetyAgent:
    def __init__(self, model: str):
        self.model = model

    def assess_test_safety(self, procedure_name: str, summary: str) -> str:
        log_trace(f"TestSafetyAgent analyzing procedure '{procedure_name}'.", "INFO")
        sys_prompt = (
            "You are a test/procedure safety-checking assistant in a medical simulation.\n"
            "You will receive a procedure or test name and a clinical summary.\n"
            "First, provide reasoning in <thinking_process>...</thinking_process>.\n"
            "Then, give a concise risk-benefit assessment in plain language:\n"
            "- Is the test/procedure appropriate?\n"
            "- Important contraindications/precautions?\n"
            "- Pre-test requirements?\n"
        )
        usr_prompt = (
            f"Procedure/Test Name: {procedure_name}\n\n"
            f"Clinical Summary:\n{summary}\n\n"
            "Task: Provide a safety and appropriateness assessment."
        )
        full_response = query_model(self.model, usr_prompt, sys_prompt)
        thinking_process, actionable_text = parse_llm_response_with_thinking(
            full_response, "TestSafetyAgent"
        )
        return actionable_text.strip()


class DietaryAdvisorAgent:
    def __init__(self, model: str):
        self.model = model

    def generate_dietary_advice(self, final_dx: str, summary: str) -> str:
        log_trace(f"DietaryAdvisorAgent generating advice for dx='{final_dx}'.", "INFO")

        sys_prompt = (
            "You are a clinical dietary advisor in a medical simulation. You will receive a final diagnosis and "
            "a concise clinical summary. Generate medically reasonable, food-based guidance.\n\n"
            "First, provide reasoning in <thinking_process>...</thinking_process>.\n"
            "Then, outside those tags, provide a structured dietary plan:\n"
            "- Foods to emphasize\n"
            "- Foods to limit/avoid\n"
            "- Practical meal examples\n"
            "- Hydration and lifestyle notes\n"
        )

        usr_prompt = (
            f"Final Diagnosis: {final_dx}\n\n"
            f"Clinical Summary:\n{summary}\n\n"
            "Task: Provide clinically sensible dietary guidance."
        )

        full_ans = query_model(self.model, usr_prompt, sys_prompt)
        thinking_process, actionable_text = parse_llm_response_with_thinking(
            full_ans, "DietaryAdvisorAgent"
        )
        return actionable_text.strip()


# ============================================================
# BACKEND WRAPPER 
# ============================================================

class MedGuardBackend:


    def __init__(
        self,
        dr_model: str = DEFAULT_GPT_MODEL,
        measure_model: Optional[str] = None,
        test_safety_model: Optional[str] = None,
        dietary_model: Optional[str] = None,
        max_doctor_turns: int = 25,
        doctor_bias: Optional[str] = None,
        ddi_csv_path: str = "db_drug_interactions.csv",
        enable_test_safety: bool = True,
    ):
        self.dr_model = dr_model
        self.measure_model = measure_model or dr_model
        self.test_safety_model = test_safety_model or dr_model
        self.dietary_model = dietary_model or dr_model
        self.enable_test_safety = enable_test_safety

        # Internal state
        self.conversation: List[Dict[str, Any]] = []
        self.patient_profile: Dict[str, Optional[str]] = {
            "age": None,
            "gender": None,
            "weight": None,
            "height": None,
        }
        self.current_intent: str = "unknown_or_general"
        self.dx_made: bool = False
        self.final_diagnosis_text: Optional[str] = None

        # Agents
        self.doctor_agent = DoctorAgent(
            model=self.dr_model,
            max_infs=max_doctor_turns,
            bias_present=doctor_bias,
        )
        self.measure_agent = MeasurementAgent(self.measure_model)
        self.dietary_agent = DietaryAdvisorAgent(self.dietary_model)
        self.ddi_db = DDIDatabase(csv_fp=ddi_csv_path)

        self.test_safety_agent = (
            TestSafetyAgent(self.test_safety_model) if enable_test_safety else None
        )

        

    # ----------------- State Helpers -----------------

    def reset(self) -> None:
        self.conversation = []
        self.patient_profile = {
            "age": None,
            "gender": None,
            "weight": None,
            "height": None,
        }
        self.current_intent = "unknown_or_general"
        self.dx_made = False
        self.final_diagnosis_text = None
        self.doctor_agent.infs = 0

    def set_patient_profile(
        self,
        age: Optional[str] = None,
        gender: Optional[str] = None,
        weight: Optional[str] = None,
        height: Optional[str] = None,
    ) -> None:
        if age is not None:
            self.patient_profile["age"] = str(age)
        if gender is not None:
            self.patient_profile["gender"] = str(gender)
        if weight is not None:
            self.patient_profile["weight"] = str(weight)
        if height is not None:
            self.patient_profile["height"] = str(height)

    def get_patient_summary(self) -> Tuple[str, List[str]]:
        return get_patient_summary_and_missing_fields(
            self.conversation, self.patient_profile
        )

    

    def patient_turn(
        self,
        user_text: str,
        *,
        test_results_text: Optional[str] = None,
        procedure_name_for_safety: Optional[str] = None,
        image_bytes: Optional[bytes] = None,
        image_mime_type: Optional[str] = None,
        pdf_bytes: Optional[bytes] = None,
    ) -> Dict[str, Any]:
        """
        Main entry point: patient says something, backend responds as doctor.

        user_text: what the patient says this turn.
        test_results_text: optional raw test results to feed via MeasurementAgent.
        procedure_name_for_safety: optional name of a procedure; if provided and
            enable_test_safety=True, TestSafetyAgent will run.
        image_bytes / image_mime_type / pdf_bytes: optional attachments this turn.

        Returns a dict with keys:
            - "doctor_reply"
            - "doctor_thinking"
            - "intent"
            - "clinical_summary"
            - "missing_fields"
            - "ddx_list"
            - "is_ddx_turn"
            - "dx_ready"
            - "final_diagnosis"
            - "procedure_safety_report"
        """
        # Append patient message
        self.conversation.append({"role": "user", "content": user_text})

        # Detect intent
        self.current_intent = detect_intent(user_text)

        # Test results -> MeasurementAgent -> system_test_result
        if test_results_text:
            fmt_res = self.measure_agent.inference_measurement(
                requested_test_name="(User-specified test)",
                user_entered_results=test_results_text,
            )
            self.conversation.append(
                {"role": "system_test_result", "content": fmt_res}
            )

        # Procedure safety
        procedure_safety_report = None
        if procedure_name_for_safety and self.enable_test_safety and self.test_safety_agent:
            summary_for_safety, _ = self.get_patient_summary()
            procedure_safety_report = self.test_safety_agent.assess_test_safety(
                procedure_name_for_safety, summary_for_safety
            )
            self.conversation.append(
                {
                    "role": "system_test_safety",
                    "content": f"Safety report for '{procedure_name_for_safety}':\n{procedure_safety_report}",
                }
            )

        # PDF attachment
        image_content_provided = False
        pdf_content_provided = False
        pdf_text_for_llm = None

        if pdf_bytes is not None:
            pdf_text_for_llm = extract_text_from_pdf(pdf_bytes)
            max_pdf = 4000
            trunc_pdf = (
                pdf_text_for_llm[:max_pdf] + ". (PDF trunc)"
                if len(pdf_text_for_llm) > max_pdf
                else pdf_text_for_llm
            )
            self.conversation.append(
                {
                    "role": "system_file_info",
                    "content": f"PDF content attached. Starts:\n{trunc_pdf[:150]}...",
                }
            )
            pdf_content_provided = True

        # Image attachment 
        if image_bytes is not None and image_mime_type:
            self.conversation.append(
                {
                    "role": "system_file_info",
                    "content": "An image was attached this turn (not auto-interpreted).",
                }
            )
            image_content_provided = True

        # Build clinical summary
        summary, missing_fields = self.get_patient_summary()

        # Is this the first assistant turn?
        is_initial_turn = (
            len([t for t in self.conversation if t["role"] == "assistant"]) == 0
        )

        # Let doctor agent respond
        dr_out = self.doctor_agent.inference_doctor(
            last_input_from_patient_or_system=user_text,
            conversation_history_from_session=self.conversation,
            patient_summary=summary,
            intent_override=self.current_intent,
            is_initial_turn=is_initial_turn,
            image_content_provided_this_turn=image_content_provided,
            pdf_content_provided_this_turn=pdf_content_provided,
        )

        dr_txt = dr_out["text"]
        dr_thinking = dr_out.get("thinking_process")
        ddx_list_text = dr_out.get("ddx_list_text")
        is_ddx_turn = dr_out.get("is_ddx_turn", False)

        # Append doctor's message
        self.conversation.append(
            {
                "role": "assistant",
                "content": dr_txt,
                "thinking": dr_thinking,
            }
        )

        # Detect if diagnosis is ready
        diag_ready_match = re.search(
            r"DIAGNOSIS READY:\s*(.*)", dr_txt, re.IGNORECASE
        )
        dx_ready = False
        if diag_ready_match:
            self.dx_made = True
            dx_ready = True
            self.final_diagnosis_text = diag_ready_match.group(1).strip()

        result = {
            "doctor_reply": dr_txt,
            "doctor_thinking": dr_thinking,
            "intent": self.current_intent,
            "clinical_summary": summary,
            "missing_fields": missing_fields,
            "ddx_list": ddx_list_text,
            "is_ddx_turn": is_ddx_turn,
            "dx_ready": dx_ready,
            "final_diagnosis": self.final_diagnosis_text,
            "procedure_safety_report": procedure_safety_report,
        }

        return result

    
    def _compile_hist_for_report(self) -> str:
        lines = []
        for t in self.conversation:
            role = t.get("role", "")
            if role == "assistant":
                who = "Doctor"
            elif role == "user":
                who = "Patient"
            else:
                who = role
            content = t.get("content", "")
            lines.append(f"{who}: {content}")
        return "\n".join(lines)

    def generate_final_doctor_report(self) -> str:
        summary, _ = self.get_patient_summary()
        sys_prompt = (
            "You are summarizing a completed clinical consultation. "
            "You will get a concise clinical summary and a transcript. "
            "Provide a clear, structured doctor's report including:\n"
            "- Chief complaint\n"
            "- History of present illness\n"
            "- Relevant positives/negatives\n"
            "- Investigations & results (if any)\n"
            "- Assessment / Diagnosis\n"
            "- Plan / Advice\n"
        )
        hist_str = self._compile_hist_for_report()
        usr_prompt = (
            f"--- Clinical Summary ---\n{summary}\n\n--- Transcript ---\n{hist_str}\n\n"
            "Task: Write the report as described."
        )
        full_ans = query_model(self.dr_model, usr_prompt, sys_prompt)
        _, report_content = parse_llm_response_with_thinking(
            full_ans, "DoctorReportAgent"
        )
        return report_content.strip()


if __name__ == "__main__":
    print("MedGuardBackend (OpenAI) demo. Set OPENAI_API_KEY before running.")
    backend = MedGuardBackend(dr_model=DEFAULT_GPT_MODEL)
    backend.set_patient_profile(age="40", gender="Male")
    print("Type 'exit' to quit.\n")

    while True:
        user_in = input("You (patient): ").strip()
        if not user_in:
            continue
        if user_in.lower() in {"exit", "quit"}:
            break

        out = backend.patient_turn(user_in)
        print("\nDoctor:", out["doctor_reply"], "\n")
        if out["dx_ready"]:
            print("Diagnosis flagged as ready:", out["final_diagnosis"])
            break

































