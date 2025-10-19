In this work, we present MedGuard-X, an enhanced and trustworthy evolution of the original MedGuard framework, designed for safe, transparent, and explainable clinical reasoning with large language models (LLMs). Unlike most LLM-driven diagnostic agents that only record final outcomes, MedGuard-X introduces complete event-level logging across all agents — doctor, patient, safety, and measurement. Every interaction, reasoning step, and model call is stored in a structured audit trail with precise timestamps and semantic labels (e.g., “REQUEST TEST”, “DIAGNOSIS READY”, “SAFETY FLAGGED”).

This continuous, multi-agent logging architecture transforms the system from a black box into a traceable reasoning graph, enabling both real-time interpretability and post-hoc forensic explainability. Evaluators and clinicians can replay diagnostic reasoning, inspect disagreements between agents, and understand why each decision was taken. Through this design, MedGuard-X advances explainability from a model-centric concept (interpreting attention maps or weights) to a system-centric paradigm where every reasoning step is recorded, interpretable, and auditable.

In summary, our contributions are threefold:
	1.	A trustworthy multi-agent diagnostic framework with explicit reasoning and safety modules.
	2.	A comprehensive logging and transparency pipeline that records every decision for explainability, accountability, and safety auditing.
	3.	A comparative experimental evaluation showing how safety and explainability mechanisms alter diagnostic accuracy, test safety compliance, and prescription reliability across 20 diverse medical cases.

⸻

🧩 New Section — 3.2.3 Logging, Traceability, and Explainability

Explainability in MedGuard-X is achieved through a unified logging infrastructure that captures every agent’s reasoning process and actions in real time. Each event — including internal model reasoning (“thinking traces”), prompts, responses, and decisions — is automatically tagged with:
	•	Actor type: (Doctor, Patient, Safety, or Measurement agent)
	•	Event label: (e.g., “REQUEST TEST”, “DIAGNOSIS READY”, “LLM FALLBACK TRIGGERED”)
	•	Timestamp and sequence index
	•	Underlying model configuration and parameters

This structured data forms a chronological reasoning graph, mapping the diagnostic trajectory from initial hypothesis generation to final prescription. The system allows replaying any simulation turn by turn, making it possible to analyze how evidence accumulated and why certain diagnostic paths were chosen or abandoned.

Logging thus serves three interrelated functions:
	1.	Transparency: Exposes decision provenance — how model inputs translate into actions.
	2.	Explainability: Provides interpretable reasoning traces beyond black-box outputs.
	3.	Accountability: Enables clinical auditing and post-hoc investigation of unsafe or incorrect outputs.

Moreover, MedGuard-X’s logging supports quantitative trust metrics, including:
	•	frequency of LLM disagreement (consensus divergence),
	•	safe vs. unsafe prescription ratio,
	•	time-to-diagnosis distribution, and
	•	correlation between reasoning depth and accuracy.

Such metrics can be computed automatically from the logs, linking transparency directly to measurable trustworthiness.

Figure 3 illustrates a representative explainability trace, showing how doctor reasoning, test results, and safety agent feedback are connected in the audit log to form an interpretable reasoning chain.

⸻

📊 Figure 3 caption (for Methods section):

Figure 3. Visualization of MedGuard-X’s logging architecture. Each node represents an agent event (Doctor, Patient, Safety, or Measurement), and edges indicate temporal and causal relationships. This audit trail supports post-hoc reasoning analysis, transparency, and system-level explainability.

⸻

💬 Add to Discussion (Explainability and Trustworthiness Analysis)

The full-scope logging design in MedGuard-X bridges the gap between algorithmic transparency and clinical accountability. In traditional LLM pipelines, outputs are ephemeral and difficult to attribute, making safety validation nearly impossible. By contrast, our event-based logging creates a causal record of every diagnostic step, allowing experts to inspect when and why unsafe or inconsistent reasoning occurred.

This aligns with the WHO (2021) and IEEE P7001 (2021) frameworks on AI transparency, which emphasize the need for auditable decision trails in safety-critical domains. Beyond compliance, the logs provide a cognitive mirror of the model’s reasoning — allowing researchers to quantify “explainability gaps” (e.g., number of opaque actions, missing evidence, or unexplained conclusions).

We observe that the logging mechanism also assists in identifying hallucination cascades, where initial misinterpretations propagate through subsequent turns. By capturing intermediate reasoning, MedGuard-X enables forensic AI safety analysis, a critical feature for trust in clinical settings.

In future iterations, we plan to extend this feature into an interactive explainability dashboard, where clinicians can visualize reasoning paths and intervene when unsafe or logically inconsistent actions arise.
