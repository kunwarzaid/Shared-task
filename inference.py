

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker":"Health Worker","date":"2025-09-25","dialogue":"CFची शक्यता लक्षात घेऊन चर्चा करीत आहोत. रुग्ण तीन महिनेांचा मुलगा आहे, मुंबईत राहत आहे. जन्मापासून हलका खोकला, वजन वाढत नाही, तेलकट पचणारे stools दिसतात, काही दिवस constipation आहे."}
{"speaker":"Patient's Relative","date":"2025-09-26","dialogue":"हो डॉक्टर, हा आपला एकमेव मुलगा आहे. आम्ही मुंबईतच आहोत. जन्मानंतर अडचण नव्हती, परंतु आता वजन कमी वाढतेय, पोटात त्रास आणि तेलकट stools दिसतात."}
{"speaker":"Health Worker","date":"2025-09-27","dialogue":"CF Sweat Test ही मुख्य पडताळणी आहे. स्थानिक केंद्र उपलब्ध नसल्यास CMC Vellore, AIIMS Delhi किंवा PGI Chandigarh या केंद्रांची माहिती देतो."}
{"speaker":"Patient's Relative","date":"2025-09-28","dialogue":"CF डायरी काय असते, कशी भरण्याची माहिती द्या. आजच डायरी सुरू करायची का, कोणते पन्ने भरायचे?"}
{"speaker":"Health Worker","date":"2025-09-29","dialogue":"CF डायरी तीन भागात विभागलेली आहे: Respiratory (खोकला वेळ/प्रसंग), Diet/Hydration ( fluids/ORS), Weight/Stool (वजन-ट्रेंड, stools). दररोज लघु नोट्स लिहा."}
{"speaker":"Patient's Relative","date":"2025-09-30","dialogue":"चला, आम्ही आजच डायरी सुरू करतो. वजन रोज नोंदण्याचा प्रयत्न करतो, पाणी व आहार कसे देतोय ते लिहू."}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"खोकला किती वेळा आणि कोणत्या प्रसंगात येतो ते लिहा. ताप झाला का, श्वास घेण्यात अडचण का झाली तिच्या काळात?"}
{"speaker":"Patient's Relative","date":"2025-10-02","dialogue":"खोकला काही वेळा रोज नसतो, परंतु खेळताना किंवा रात्रीच्या नंतर थोडा वाढतो. ताप क्वचितच येतो; श्वास घेताना खडबड आवाज काही वेळा येतो."}
{"speaker":"Health Worker","date":"2025-10-03","dialogue":"Diet/Hydration भागात दैनंदिन fluids किती देता, ORS कधी देता ते नोंदवा. पाणी अधिक देणे आवश्यक असल्यास उपाय सांगा."}
{"speaker":"Patient's Relative","date":"2025-10-04","dialogue":"आम्ही ORS पॅकेट्स दिवसाला काही वेळा देतो; पाणी बहुधा कमी देते, आहारात फळे-भंडार कमी मिळते."}
{"speaker":"Health Worker","date":"2025-10-05","dialogue":"Weight/Stool विभागात वजनाचा ट्रेंड व stoolचे वर्णन नोंदायचं. तेलकट stools असल्यास त्याची पातळी आणि शुष्क त्वचारंग लक्षात ठेवा."}
{"speaker":"Patient's Relative","date":"2025-10-06","dialogue":"स्टूल बहुधा तेलकट असतो, वजन थोडं कमी वाढतंय. Stool चे रंग पांढरे किंवा पिवळे दिसत नाहीत."}
{"speaker":"Health Worker","date":"2025-10-07","dialogue":"Sweat Testची तयारी कशी करायची ते सांगतो. नमुना घेण्याची प्रक्रिया सहज असते; निकाल काही दिवसांत येतो."}
{"speaker":"Patient's Relative","date":"2025-10-08","dialogue":"जगातल्या कोणत्याही केंद्रात Sweat Test मिळेल का? खर्चाची माहिती मिळेल का?"}
{"speaker":"Health Worker","date":"2025-10-09","dialogue":"उपलब्धतेवर अवलंबून subsidy schemes तपासतो. जर महाराष्ट्रात सरळ उपलब्ध नसेल, तर केंद्रीय योजनांची माहिती देतो."}
{"speaker":"Patient's Relative","date":"2025-10-10","dialogue":"चार आठवडे क्लिनिकल फॉलो-अपची वेळ आम्ही ठरवतो का? वजन व hydration पहायला."}
{"speaker":"Health Worker","date":"2025-10-11","dialogue":"हो,四 आठवड्यांनी क्लिनिकल चेक-अप आणि Sweat Testची तयारी एकत्र केली जाईल. केंद्रांची यादी आम्ही देतो, travel plan बनवू."}
{"speaker":"Patient's Relative","date":"2025-10-12","dialogue":"केंद्रांची पत्ता-वेळ आणि संपर्क क्रमांक कसे मिळतील? प्रवासासाठी किती दिवस लागतील?"}
{"speaker":"Health Worker","date":"2025-10-13","dialogue":"CMC Vellore, AIIMS Delhi, PGI Chandigarh हे प्रमुख केंद्र आहेत. प्रवासासाठी केंद्राकडे मार्गदर्शक माहिती देतो."}
{"speaker":"Patient's Relative","date":"2025-10-14","dialogue":"खर्चाचा विचार केला तर subsidies आणि ट्रॅव्हल खर्च किती असतील? विचारायचे."}
{"speaker":"Health Worker","date":"2025-10-15","dialogue":"होय, subsidies व travel guidelines उपलब्ध असतात. CF बद्दल शिक्षण देऊन misdiagnosis टाळणे महत्त्वाचे."}
{"speaker":"Patient's Relative","date":"2025-10-16","dialogue":"चार आठवड्यांच्या क्लिनिकल फॉलो-अपची वेळ आम्ही घेतो. Sweat Testची तयारी parallel चालू ठेवू."}
{"speaker":"Health Worker","date":"2025-10-17","dialogue":"तयार असल्यास Sweat Testसाठी केंद्र यादी देतो. तुमच्या शहरातील जवळचे केंद्र ओळखून देतो."}
{"speaker":"Patient's Relative","date":"2025-10-18","dialogue":"प्रवासासाठी आवश्यक कागदपासपत्ते आणि मोबाईल नंबर update करायचं वाटतं."}
{"speaker":"Health Worker","date":"2025-10-19","dialogue":"कागदपत्रे, फोन नंबर अद्ययावत ठेवा. आपण जिथे जाल तिथे आरोग्य विभागाशी संपर्कात रहा."}
{"speaker":"Patient's Relative","date":"2025-10-20","dialogue":"CF बद्दल माहिती घरातल्यांना समजावून सांगतोय. TB मिसडायग्नोसिसबद्दलची भीती कमी करायची."}
{"speaker":"Health Worker","date":"2025-10-21","dialogue":"CF आणि TB यांची लक्षणे वेगवेगळी असतात; खोकला, वजन, पचन या बाबींवर विशेष लक्ष देणे गरजेचे."}
{"speaker":"Patient's Relative","date":"2025-10-22","dialogue":"Genetic carrier testing कधी करायचं? CF निदानासाठी ते कितपत उपयुक्त?"}
{"speaker":"Health Worker","date":"2025-10-23","dialogue":"Genetic testing उपयुक्त असते, पर Sweat Test प्रथम क्रमांकाचा उपाय. निर्णय घराच्या विचारानुसार घेतला जावा."}
{"speaker":"Patient's Relative","date":"2025-10-24","dialogue":"Sweat Testची प्रक्रिया काही दिवसात निकाल देईल का? नमुना कुठे देतात ते स्पष्ट कराल."}
{"speaker":"Health Worker","date":"2025-10-25","dialogue":"Pilocarpine आधारित sweat collection केली जाते. निकाल काही दिवसांत येतो. मुंबईतल्या काही केंद्रांमध्ये त्वरित निकाल संभवतो."}
{"speaker":"Patient's Relative","date":"2025-10-26","dialogue":"निकाल आल्यानंतर CF असल्यास पुढची काय योजना असते? उपचार कसे सुरु करायचे?"}
{"speaker":"Health Worker","date":"2025-10-27","dialogue":"CF निदान झाल्यास pancreatic enzyme replacement therapy (PERT) व इतर उपायांचे मार्गदर्शन देतो. पुढील CF केअर प्लान तयार करतो."}
{"speaker":"Patient's Relative","date":"2025-10-28","dialogue":"आम्हाला चार आठवड्यात काय-काय सल्ले द्या? वजन वाढीची योजना कशी असते?"}
{"speaker":"Health Worker","date":"2025-10-29","dialogue":"चार आठवड्यानंतर क्लिनिकल चेक-अप, वजन- hydration आणि stool निरीक्षण. Sweat Testचा निर्णय डेटा वर अवलंबून घेए."}
{"speaker":"Patient's Relative","date":"2025-10-30","dialogue":"CF आढळल्यास आम्हाला काय आशा असते? अन्न-पोषण कोणते फायदे देईल?"}
{"speaker":"Health Worker","date":"2025-11-01","dialogue":"CF व्यवस्थापनात आहार, पाणी, पाणी-ORS आणि CF केअर प्लानची अंमलबजावणी महत्त्वाची. घरगुती उपाय डॉक्टरांच्या मार्गदर्शनानुसार."}
{"speaker":"Patient's Relative","date":"2025-11-02","dialogue":"गावाकडे CF awareness कसे वाढवायचं? प्रवासासाठी तयारीची टिपा दाखवा."}
{"speaker":"Health Worker","date":"2025-11-03","dialogue":"गावात CF-awareness सत्र आयोजित करणे उपयुक्त. TB मिसडायग्नोसिस कमी करण्यासाठी लक्षणे स्पष्ट करणे गरजेचे."}
{"speaker":"Patient's Relative","date":"2025-11-04","dialogue":"आम्ही CF बद्दल माहिती समाजात पसरवू."}
{"speaker":"Health Worker","date":"2025-11-05","dialogue":"4 आठवड्यांनंतर क्लिनिकल follow-upची तयारी करावी; diary, center-list, subsidy-options एकत्र ठेवा."}
{"speaker":"Patient's Relative","date":"2025-11-06","dialogue":"हो, आम्ही सर्व तयारी एकत्र करतो. Sweat Testसाठी तिकीट वगैरे ठरवू."}
{"speaker":"Health Worker","date":"2025-11-07","dialogue":"उत्सुकता असते; तुमच्या शहरातील जवळचा Sweat Test केंद्र शोधून feasibility चाचणी करतो."}
{"speaker":"Patient's Relative","date":"2025-11-08","dialogue":"यादी मिळाल्यावर त्या दिवशी प्रवासाची तयारी करु."}
{"speaker":"Health Worker","date":"2025-11-09","dialogue":"त्यासाठी धन्यवाद. CF awareness आणि परिवारातील सदस्यांना मार्गदर्शन करण्याची तयारी ठेवा."}
{"speaker":"Patient","date":"2025-11-10","dialogue":"बाबा, डॉक्टर CF काय आहे ते समजावून सांगू शकता?"}
{"speaker":"Health Worker","date":"2025-11-11","dialogue":"हो, CF हा फुफ्फुस आणि पाचन संस्थेला प्रभावित करतो; Sweat Test नक्की निदानाचा आधार ठरतो. प्रश्न विचारू शकता."}
{"speaker":"Patient's Relative","date":"2025-11-12","dialogue":"घरी वातावरण हलकं ठेवण्याचं आम्ही प्रयत्न करतो; डॉक्टरांनी दिलेले मार्गदर्शनपालन करतो."}
{"speaker":"Health Worker","date":"2025-11-13","dialogue":"CF निदानानंतर दीर्घकालीन व्यवस्थापन योजना तयार केली जाते; वजन, hydration, stools, respiratory care या सर्वांचा समावेश."}
{"speaker":"Patient's Relative","date":"2025-11-14","dialogue":"CF awareness आणि diary सतत अद्ययावत ठेवून न्यायालयाच्या मार्गदर्शनानुसार आचरण करतो."}
{"speaker":"Health Worker","date":"2025-11-15","dialogue":"4 आठवड्यांनंतर क्लिनिकल follow-upची तयारी पूर्ण करु. Sweat Test साठी center-list आपल्याकडे ठेवा."}
{"speaker":"Patient's Relative","date":"2025-11-16","dialogue":"होय, center-list मिळाल्यावर travel plan बनवू."}
{"speaker":"Health Worker","date":"2025-11-17","dialogue":"कागदपत्रे आणि मोबाईल नंबर अद्ययावत ठेवा; center-list, diary, आणि subsidy-options एकत्र ठेवा."}
{"speaker":"Patient's Relative","date":"2025-11-18","dialogue":"या वेळी आम्ही तयारी करतो; आई थोडी व्यस्त असते तरी डायरी रोज लिहू."}
{"speaker":"Health Worker","date":"2025-11-19","dialogue":"तुमचं प्रयत्न CF awareness वाढवण्यासाठी उपयुक्त ठरेल. TB misdiagnosis टाळण्यासाठी लक्षणे स्पष्ट ठेवा."}
{"speaker":"Patient's Relative","date":"2025-11-20","dialogue":"गावात CF बद्दल माहिती देताना कोणते मुद्दे अधिक महत्त्वाचे असतील?"}
{"speaker":"Health Worker","date":"2025-11-21","dialogue":"खोकला, वजन, पचन यांची माहिती स्पष्ट करून देणे; diary सुदृढ करणे महत्त्वाचे."}
{"speaker":"Patient's Relative","date":"2025-11-22","dialogue":"Sweat Testची तयारी सुरु करतो; Subsidy schemesची माहिती मिळवण्यात मदत करा."}
{"speaker":"Health Worker","date":"2025-11-23","dialogue":"CF निदानानंतर दीर्घकालीन तपासण्या, आहार योजना, फीज अँटीबायोटिक लक्ष्यांसह एकत्रित केली जाते."}
{"speaker":"Patient's Relative","date":"2025-11-24","dialogue":"धन्यवाद डॉक्टर. डायरी सुरू ठेवू, Sweat Testची तयारी करु, आणि travel plan बनवू."}
{"speaker":"Health Worker","date":"2025-11-25","dialogue":"चांगलं. पुढील भेटीची तयारी करा; center-list, diary, subsidy-options एकत्र जोडा."}
{"speaker":"Patient's Relative","date":"2025-11-26","dialogue":"होय; शहरातील Sweat Test केंद्र आणि प्रवासाचे तिकीट बुक करण्यासाठी काही वेळ देऊ."}
{"speaker":"Health Worker","date":"2025-11-27","dialogue":"तुमच्या शहरातील Sweat Test केंद्र शोधून feasibility तपासतो; आवश्यक माहिती देतो."}
{"speaker":"Patient's Relative","date":"2025-11-28","dialogue":"यादी मिळाल्यानंतर त्या दिवशी प्रवासाची तयारी करु."}
{"speaker":"Health Worker","date":"2025-11-29","dialogue":"CF awareness आणि परिवारातील सदस्यांना मार्गदर्शन करण्याची तयारी ठेवा."}
{"speaker":"Patient","date":"2025-11-30","dialogue":"बाबा, मला डॉक्टर CF काय असल्याचं समजावून सांगाल?"}
{"speaker":"Health Worker","date":"2025-12-01","dialogue":"हो, CF एक अशी स्थिती आहे ज्यात श्वसन व पाचन यांचं काम कमी होते; Sweat Test नक्की निदान देतो. प्रश्न विचारा."}
{"speaker":"Parent","date":"2025-12-02","dialogue":"आज घरातल्या वातावरणात काही बदल करायचं असल्यास मार्गदर्शक द्या."}
{"speaker":"Health Worker","date":"2025-12-03","dialogue":"CF awareness सत्रे आयोजित करणे, TB misdiagnosis टाळणे, diary व CF care plan पाळणे हे फायदेशीर."}
{"speaker":"Patient's Relative","date":"2025-12-04","dialogue":"आम्ही पुढील आठवड्यात क्लिनिकल फॉलो-अपसाठी येऊ; डायरी अद्ययावत ठेवू."}
Ground Truth
Summary (CF-focused) of the dialogue

- Presentation and clinical context
  - A 3-month-old male in Mumbai presents with intermittent mild cough since birth, poor weight gain despite adequate feeding, oily bulky stools, digestive discomfort, and several days of constipation. These findings raise suspicion for cystic fibrosis (CF). Family seeks structured monitoring and targeted evaluation.

- Diagnostic plan and rationale
  - Sweat Test is identified as the primary diagnostic test for CF and should be arranged at a larger center. If Sweat Test is not locally available, clinicians should document symptoms and data to guide next steps.
  - A CF diary is mandated to accompany the diagnostic process to enable systematic tracking of symptoms and outcomes.

- CF diary and data collection
  - Diary is divided into three parts: 
    - Respiratory: timing/context of cough
    - Diet/Hydration: fluids and use of oral rehydration solutions/electrolytes
    - Weight/Stool: weight trend and stool characteristics
  - Weight is to be tracked over 2–4 weeks; diary starts immediately with a 1–2 page daily entry typical. A clinical visit is planned after 4 weeks of diary data.

- Immediate and initial management guidance
  - Emphasize increased hydration and electrolyte/fluid intake.
  - If Sweat Test isn’t readily available locally, explore government schemes or subsidies to support testing.
  - Educate the family about CF to prevent misdiagnoses (e.g., TB or malnutrition) and avoid delays.

- Follow-up plan and logistics
  - After 4 weeks, conduct a clinical check-up to review weight, hydration status, and stool characteristics; Sweat Test preparation and scheduling should proceed in parallel.
  - Prepare a list of Sweat Test centers with addresses, timings, and contact information (examples: CMC Vellore, AIIMS Delhi, PGI Chandigarh) to assist travel planning.
  - Encourage travel planning to central hospitals while adhering to safety protocols (e.g., COVID-19 guidelines).
  - Consider genetic carrier testing as a parallel option with a balanced discussion of benefits and risks.

- Information management and safeguards
  - Maintain updated addresses and contact numbers for key centers; ensure mobile numbers are current.
  - Stay in touch with local health authorities for guidance or assistance.
  - Seek information on government schemes or subsidies to support testing and travel.

- Expected outcomes and milestones
  - Finalize Sweat Test plan with timing and center details; use diary, weight, hydration, and stool data to inform the physician.
  - Schedule a 4-week clinical follow-up to review progress and finalize Sweat Test arrangements.
  - Use CF awareness efforts to educate the family and the local community.

- Immediate actions and ongoing execution
  - Start the CF diary today (record cough timing, weight trend, fluids, stool characteristics).
  - At the 4-week mark, attend the clinical check-up with a detailed report and prepare for Sweat Test scheduling.
  - If Sweat Test centers aren’t local, obtain a list of potential centers and subsidy options in advance.

- Overall plan
  - Central objective: arrange a Sweat Test at an appropriate hospital while meticulously documenting symptoms via a structured diary.
  - Four-week follow-up to assess weight, hydration, and stools to finalize Sweat Test logistics.
  - Parallel actions include travel planning to a major center, subsidy options, and genetic counseling as relevant.

- Context and practical notes
  - The dialogue reflects an Indian healthcare setting, emphasizing TB misdiagnosis awareness, potential funding options, and active family engagement in education and planning.
  - Sweat Test details: pilocarpine-based sweat collection; results typically available in a few days; subsidies may support testing where local availability is limited.

- Key practical takeaway
  - Initiate the CF diary immediately and arrange Sweat Test at a recognized center within 4 weeks, while navigating subsidies and travel logistics; use collected data to guide subsequent CF care if CF is diagnosed.

Qwen-2.5-7B-Instruct-few-shot
Clinical Summary:

- The patient is a 3-month-old male infant from Mumbai, presenting with chronic cough, poor weight gain, loose stools, and intermittent constipation since birth. The parents report no significant past medical history, but the child has recently shown signs of weight loss, distress, and loose stools.

- Initial evaluation includes a suspicion of Cystic Fibrosis (CF). The parents are informed that the primary diagnostic test is the Sweat Test, which is available at CMC Vellore, AIIMS Delhi, or PGI Chandigarh.

- The parents are instructed to start a daily diary to document the child's respiratory symptoms, fluid intake, hydration status, and stool characteristics. Specific sections include respiratory symptoms, fluid intake, and stool observations.

- The parents are advised to monitor the child's temperature and breathing patterns, noting any changes. They are also instructed on maintaining proper hydration and nutrition, including ORS solutions when necessary.

- A follow-up clinic visit is scheduled for 4 weeks to review the diary entries, perform a Sweat Test, and discuss further management. Travel plans to one of the available centers are discussed, considering the nearest feasible location.

- The parents are educated on CF awareness, including the importance of recognizing symptoms such as cough, poor weight gain, and feeding difficulties. They are advised to continue documenting the child's condition and seek medical guidance.

- The parents are informed that a long-term care plan will be developed post-diagnosis, including weight management, hydration, stool monitoring, and respiratory care. They are encouraged to participate in community awareness programs and to manage the child's condition according to medical advice.

- The parents are reminded to prepare for the next clinic follow-up, gather necessary documents, and finalize travel arrangements for the Sweat Test. They are advised to stay organized and committed to the care plan.

2

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker":"Patient","date":"2025-10-01","dialogue":"4 महिन्याचा मुलगा आहे. जन्मापासून खोकला चालला आहे. दूध नियमित पितो, तरी वजन वाढत नाही. पोटात तेलकट शौच दिसते, बदलेले दिसते."}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"CF म्हणजे सिस्टिक फायब्रोसिस. ही जीनद्वारे झालेली autosomal recessive वारसा रोग आहे; दोन कैरियर असणार्‍यांना CF होऊ शकते. ही रोग संसर्गजन्य नाही."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"आम्हाला CF बद्दल फार माहिती नाही. घरात कुणाला CF झालेय असे ऐकले नाही. पण आम्ही समजून घेण्यासाठी आलोय."}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"बाळाच्या मेकॉनीयनची स्थिती कधी अडचणीत आली होती का? CF मध्ये मेकॉनीयनचा अडथळा होऊ शकतो."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"बाळ जन्माच्या दिवशी शौच थांबली होती का?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"सध्या बाळ श्वास घेतोय; ऑक्सिजन सेचुरेशन सामान्य आहे. ताप नाही."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"गावातून शहरात येण्याचा प्रवास कसा होईल? खर्च किती येईल?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"Sweat test शहरात करायचा आहे. पुणे, AIIMS, PGI सारखे मोठे हॉस्पिटल चांगले. सरकारची योजना/सबसिडी तपासू."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"Sweat test कसं करतात? वजनाबद्दल काय अपेक्षा?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"Sweat testमध्ये पायाच्या लहान नमुना घेतला जातो; CF असल्यास Sweat chloride पातळी जास्त दिसते. वजनानुसार योजना ठरते."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"मला फार माहिती नाही. आम्ही काय करायचं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"पहिला धडा: वजन, उंची, आहार, श्वास यांची नोंद ठेवा. Sweat testची तयारी करा. Genetic counseling बद्दल माहिती देतो."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"वजन-उंची आम्ही रोज मापतोय, पण पथ्य काय ठेवं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"सध्या विशेष पथ्याची गरज नाही. पाणी सरळ द्या, संतुलित आहार ठेवा, वजन ट्रॅक केला पाहिजे."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"शहरात जाणे शक्य आहे का? खर्चाचा अंदाज काय?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"शहरात जाण्यासाठी Subsidy किंवा सरकारी योजना असू शकते. आवश्यक कागदपत्रे तयार ठेवा."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"कागदपत्रं जमा करतो. आणखी काय करायचं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"आधार, राशन कार्ड, गावाचा पत्ता, मोबाईल नंबर, आरोग्य विमा/कागदपत्रे. गावातील प्राथमिक आरोग्य केंद्रातून मदत मिळू शकते."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"मी वजन, आहार, श्वास, शौचाचा रंग यांची डायरी नोंदू?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"होय. दोन आठवड्यात परत या. वजन-उंची, श्वास तपासू."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"दोन आठवडे किती काळजी घेणारं असते? कोणत्या अटींची खबरदारी?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"तुरंत संपर्क करा जर धापा घाम येणे, ताप, वजन कमी होतो, श्वासात अडचण असेल."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"आज-उष्ण हवामान आहे; प्रवासात आणखी काय विचारात घ्यायचं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"हवामानानुसार पाणी अधिक द्या; प्रवासाच्या तयारीत डायरी, कागदपत्रं आणि दवाखान्याचं कागदपत्रं आणि संपर्क क्रमांक ठेवा."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"Weight-check कधी करायचं? आम्हाला वेळ कसा लागू?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"फॉलो-अप दोन आठवड्यात. Sweat Testची तयारी करा, मग निकालानुसार पुढचं नियोजन करु."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"होय, आम्ही तयारी करतो. काही अडचण आली तर सांगतो."}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"शहरात Subsidy मिळू शकतात; आम्ही मार्गदर्शन देऊ."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"Sweat Test का निर्णायक आहे?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"CF असल्यास Sweat chloride जास्त असते, त्यामुळे CFची पुष्टी होते."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"CF आढळल्यास पुढे काय करायचं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"CF असल्यास पोषण-आहार, श्वसन काळजी, इन्फेक्शन नियंत्रण, Genetic counseling असा मल्टी-डिसिप्लिनरी प्लॅन बनवतात."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"CF असल्यास उपचार किती महाग असू शकतात?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"बहुतेक खर्च नियंत्रणात असतो; पोषण सपोर्ट, फिजिओथेरपी, वैद्यकीय सल्ला. सरकार योजना मदत करतात."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"कुठल्या डॉक्टरकडे जाऊ?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"CF तज्ज्ञ डॉक्टर, पेडियाट्रिशियन, आहारतज्ज्ञ, फिजियोथेरपिस्ट यांच्या टीमकडे."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"CF असल्यास Vaccines चालू ठेवायचे का?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"Vaccines सामान्यपणे चालू ठेवाव्यात; CF च्या उपचारात काही विशेष निर्देश डॉक्टर देऊ शकतात."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"आजोबा-आजी काही मदत करतील का?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"हो, नातेवाईक मदत कराल तर ठीक. Sweat Test पूर्ण झाल्यावर माहिती देऊ."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"गाव-शहरचा प्रवास खूप अवघड होतो."}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"गावातून शहरात जाणं सुरळीत करण्यात आम्ही मार्गदर्शन देऊ. हेल्पलाइनही वापरा."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"वजन टिकवण्यासाठी आहारात काय विशेष द्यायचं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"संतुलित आहार, पोषक तत्त्वे, तेलकट अन्न मर्यादित; शंका असल्यास आहारतज्ज्ञाशी बोला."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"पाणी किती द्यावं? दररोज किती लिटर?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"दररोज वजनानुसार 60-100 ml/kg पाणी द्या; डॉक्टर तुम्हाला अचूक मात्रा सांगतील."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"शौचाचा रंग तेलकट असेल तर काय करायचं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"शौचाचा रंग किंवा बदलेला रंग असेल तर त्वरित डॉक्टरांना विचारा; CFच्या नियंत्रणाचा भाग."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"Sweat Test कधी होईल? आम्हाला वेळ कळेल का?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"दोन-तीन आठवड्यात Sweat Test होऊ शकतो; शहरात उपलब्धतेनुसार वेळ ठरेल."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"काय-काय कागदपत्रं आणायची?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"आधार, राशन कार्ड, गावाचा पत्ता, मोबाईल नंबर, आरोग्य सुरक्षा कागदपत्र."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"आम्ही ते तयार ठेवतो. आणखी काही तयारी?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"Sweat Testसाठी खबरदारी: सकाळचं वजन मापा जा, जास्त तिखट अन्न टाळा, डॉक्टरांच्या निर्देश पाळा."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"Negative आला तर पुढे काय?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"Negative असलात CFची शक्यता कमी; परंतु अन्य कारणं तपासावी. Genetic counseling सुरू ठेवा."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"Positive आला तर पुढे काय?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"CF असल्यास पोषण-आहार, श्वसन-केअर, इन्फेक्शन नियंत्रण, genetic counseling यांची टीम बनवली जाईल."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"खर्च किती होईल? आम्ही बजेट कसे व्यवस्थापित करायचं?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"सरकारी योजना आणि सबसिडी मदत उपलब्ध असू शकते; अर्ज व मार्गदर्शन देऊ."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"फॉलो-अप कधी असेल?"}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"फॉलो-अप दोन आठवड्यात weigh-उंची तपासणीसह पुनर भेट. Sweat Testचा निकाल आल्यावर पुढील स्टेप ठरवू."}
{"speaker":"Patient's Relative","date":"2025-10-01","dialogue":"अर्थात. मी वजन व आहाराबद्दल डायरी चालू ठेवीन."}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"Genetic counseling बद्दलबी माहिती घेता, तर भविष्यक्रमण सोपे होईल."}
{"speaker":"Patient","date":"2025-10-01","dialogue":"धन्यवाद, डॉक्टर. आम्ही तयारी करतो."}
{"speaker":"Health Worker","date":"2025-10-01","dialogue":"चांगलं. पुढची माहिती लवकर देऊ. नमस्कार."}
Ground Truth:
Summary of the CF-focused infant care dialogue (key events, symptoms, diagnosis, and treatment steps)

- Presenting symptoms and clinical clues
  - Four-month-old with a persistent cough since birth.
  - Poor weight gain despite regular feeding.
  - Oily/fatty stools and variability in stool appearance.
  - Discussion of meconium history as a potential CF clue.
  - On examination: not in respiratory distress; normal chest exam; stable oxygen saturation; no fever.

- Key medical understanding
  - Cystic fibrosis (CF) is an autosomal recessive genetic condition and is not contagious.
  - Carrier status in parents has implications for future pregnancies.
  - Emphasis on genetic counseling and careful monitoring of familial history and symptoms.

- Diagnostic strategy and tests
  - Sweat test identified as the pivotal diagnostic test for CF.
  - If Sweat Test is not available locally, diagnosis should rely on documented symptoms and guidance from a CF specialist.
  - Additional general assessments discussed or implied: basic physical examination (growth and vitals), regular weight tracking, oxygen saturation, temperature, basic imaging and stool studies as needed; testing parents; providing genetic counseling.

- Practical/logistical considerations
  - Sweat test not available in the village; referral to city centers (e.g., Pune, AIIMS, PGI Chandigarh) discussed.
  - Government programs/subsidies may help cover tests or reduce costs; guidance given on accessing subsidies.
  - Travel planning from rural areas acknowledged; gather documents and arrange follow-up.
  - Family advised to maintain a home diary of weight, height, feeding patterns, cough episodes, and stool color/consistency.

- Immediate clinical assessment and follow-up plan
  - Current visit included routine respiratory assessment, skin color, weight, and oxygen saturation; baby breathing normally.
  - Follow-up planned in two weeks to reassess growth and respiratory symptoms and to review Sweat Test results when available; return sooner if symptoms worsen.

- Education and ongoing management plan
  - Emphasis on collaborative CF management: regular monitoring, good nutrition, infection prevention, and adherence to guidance.
  - CF remains non-infectious; genetic counseling for the family and potential siblings stressed.
  - Home care guidance: ensure adequate fluids, balanced nutrition, hygiene, simple respiratory exercises; maintain a disease-management diary.
  - Preparation for Sweat Test: continue tracking weight/height; pursue genetic counseling if CF is suspected.

- Next steps and contingency planning
  - Sweat Test is the decisive step; arrange for testing in a city center if possible.
  - If Sweat Test is negative: CF becomes less likely, but other etiologies should be explored.
  - If Sweat Test is positive: develop a formal CF management plan including nutritional support, respiratory care, and potential CF-directed therapies; continue genetic counseling for family planning.

- Documentation and access
  - Bring documents (Aadhaar card, ration card, village address, mobile number, health/insurance papers); travel subsidies and administrative support discussed.
  - Keep records of weight, height, feeding, and follow-up visits; ensure vaccination and medical records are available for the test.

- Progress and timeline notes
  - By early October 2025, Sweat Test planning remained active with city-center referrals (Pune noted); two-week follow-up to reassess and prepare for test scheduling.
  - Sweat Test results would guide subsequent steps; a negative result would lower CF likelihood but not completely exclude CF, necessitating evaluation for other conditions.

- Overall takeaway
  - The infant’s persistent cough, poor weight gain with regular feeding, and oily stools raise suspicion for CF.
  - The Sweat Test is the key diagnostic test, with city-based testing and genetic counseling as essential components.
  - Interim management emphasizes nutritional optimization, hydration, infection prevention, and meticulous home diary documentation to guide urgent follow-up and future CF management if confirmed.

Qwen-2.5-7B-fewshot:
Summary of the cystic fibrosis (CF) care planning dialogue

- Patient and presenting symptoms
  - 4-month-old male infant, has been passing meconium since birth, no weight gain, and intermittent loose stools.
  - CF suspected due to autosomal recessive inheritance pattern; both carriers can have CF.
  - No family history of CF, but parents suspect it.

- Initial evaluation and plan
  - CF diagnosis suspected based on meconium passage issues and family history.
  - Parents unsure about CF, no previous cases in the family.
  - Inquiry about neonatal condition and respiratory status.
  - Oxygen supplementation common in CF.
  - Travel from village to city for sweat test.
  - Discussion on nearby hospitals (Pune, AIIMS, PGI) and government schemes/subsidies.

- Investigations
  - Sweat test planned in the city.
  - Importance of weight, height, feeding, and respiratory status monitoring.
  - Sweat test preparation involves collecting a small amount of sweat; CF positive if chloride levels are high.
  - Regular measurements of weight and height.
  - Travel to city possible, cost estimate needed.
  - Government subsidies or schemes available for travel expenses.

- Follow-up and management
  - Detailed record-keeping of weight, feeding, respiration, and bowel movements.
  - Immediate contact if symptoms like breathlessness, fever, weight loss, or respiratory distress.
  - Seasonal advice on hydration and preparation for travel.
  - Sweat test preparation: morning weight, fasting, following doctor's instructions.
  - Follow-up every two weeks.
  - Sweat test results interpretation: CF confirmed if chloride levels are high.
  - Management plan includes nutrition, respiratory care, infection control, and genetic counseling.
  - Cost management advice: government schemes and subsidies available.
  - Referral to specialized doctors: pediatrician, nutritionist, physiotherapist.
  - Vaccination advice: routine vaccinations, specific instructions from doctors for CF patients.
  - Travel support and helpline information provided.
  - Specific feeding advice: balanced diet, limited fatty foods, adequate hydration.
  - Advice on loose stools: immediate doctor consultation if color changes.
  - Sweat test scheduling: within 2-3 weeks, based on availability.
  - Necessary documents: Aadhaar, ration card, village address, mobile number, health insurance documents.
  - Follow-up plan: weight-height measurements, sweat test results, and further steps.
  - Continuous monitoring of weight and feeding.

3

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Patient", "date":"", "dialogue": "मी राजेश पटेल, मुंबईत राहतो, वय 52 वर्षे. गळ्यात गांठ, आवाजात बदल, अन्न गिळताना त्रास, रात्री झोप न येणे, वजन थोडे कमी झाले. खरंतर काय होते ते सांगायचंय."}
{"speaker": "Health Worker", "date":"", "dialogue": "ही समस्या गंभीर आहे; MDT च्या चौकटीत आपण स्टेजिंग, तपासणी आणि पुढील टप्पे ठरवणार आहोत. सगळे स्पष्टपणे समजवण्यासाठी base-line तपासण्या सुरू करतो, तुम्हाला काही प्रश्न आहेत का?"}
{"speaker": "Patient", "date":"", "dialogue": "मी दररोज धूम्रपान करतो, पान मसाला पण वापरतो. HPV तपासणीची शक्यता काय, आणि ती कधी केली जाईल? ही माहिती मला कधी मिळेल आणि पुढे काय?"}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV तपासणी होईल, बायोप्सी व endoscopy असतील; imaging म्हणजे CT/MRI; निकाल 2-5 दिवसांत मिळेल. MDT बैठक ठरणाऱ्या तारखा, स्टेजिंग निर्णय व उपचारयोजनाबद्दल साफ माहिती देऊ."}
{"speaker": "Patient", "date":"", "dialogue": "तपासणीची वेळ कधी मिळेल, वारंवार तपासायचे असते?"}
{"speaker": "Health Worker", "date":"", "dialogue": "baseline checks दोन आठवड्यात पूर्ण होतील; रक्त तपासणी, dental status, Endoscopy तयारी, imaging (CT/MRI). MDT बैठक two सप्ताहानंतर असेल; स्टेजिंग स्पष्ट झाल्यावर पुढची रस्ता दिसेल."}
{"speaker": "Patient", "date":"", "dialogue": "स्टेजिंग कसे ठरते, आणि HPVचा परिणाम काय असतो?"}
{"speaker": "Health Worker", "date":"", "dialogue": "स्टेजिंग CT/MRI, endoscopy, biopsy, तुमचा इतिहास आणि धोक्याच्या घटक; HPV स्थिती तसेच tumor localization या गोष्टी स्टेजिंगमध्ये मदत करतात."}
{"speaker": "Patient", "date":"", "dialogue": "जर स्टेज III आली तर उपचार कसा असतो, किती वेळाचा टप्पा, दुष्परिणाम काय?"}
{"speaker": "Health Worker", "date":"", "dialogue": "Advanced स्टेजमध्ये सामान्यतः surgery + radiotherapy; काही वेळात chemotherapy सोबत; MDT निर्णय निवडते."}
{"speaker": "Patient", "date":"", "dialogue": "उदा. सर्जरी म्हणजे काय, गळ्यातल्या लिम्फ नोड्स कसे काढतात, आणि गरज पडल्यास अवयव बदल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "ट्यूमर व मार्जिन; घेरातील गळ्याच्या भागातील लिम्फ नोड्सची शस्त्रक्रिया; आवश्यक असेल तर reconstruction/ flap."}
{"speaker": "Patient", "date":"", "dialogue": "रेडिएशन कसं असतं, दररोज किती वेळा देतात आणि त्वचेला काय परिणाम होतो?"}
{"speaker": "Health Worker", "date":"", "dialogue": "रेडिएशन दररोज एक सत्र, साधारणपणे 6-7 आठवडे; त्वचा लाल होऊ शकते, शुष्कता, काही लोकांना अन्नाची चव कमी होते."}
{"speaker": "Patient", "date":"", "dialogue": "Chemotherapyची भूमिका काय असते, Cisplatin कसा देतात, आणि दुष्परिणाम काय?"}
{"speaker": "Health Worker", "date":"", "dialogue": "Radiation सोबत chemo देण्याचा हेतू tumor sensitivity वाढवणं; India मध्ये साप्ताहिक Cisplatin किंवा कमी डोस सामान्य. पोटात, किडनी-फंक्शन तपासले जाते."}
{"speaker": "Patient", "date":"", "dialogue": "हे खर्च कसा भागवता येईल, विमा किंवा सरकारी स्कीमवर काय उपलब्ध आहे?"}
{"speaker": "Health Worker", "date":"", "dialogue": "आयुष्मान भारत, राज्य योजना, हॉस्पिटल-आधारित सहाय्य; MDT अर्हता असल्यास काही खर्च कव्हर होतो."}
{"speaker": "Patient", "date":"", "dialogue": "तेव्हा निर्णयासाठी तयारी कशी करायची, MDT कधी होईल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "तयारी: baseline टेस्ट्स, imaging; 2-3 दिवसांत निकाल; MDT बैठक दोन आठवड्यात अंतिम निर्णय घेते."}
{"speaker": "Patient", "date":"", "dialogue": "HPV टेस्टचा निकाल आल्यानंतर स्टेजिंग किंवा उपचारात काय बदल दिसेल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV पॉझिटिव्ह असल्यास काही ट्रायल किंवा कमी आक्रामक रेडिएशन डिटेल्स विचारात येऊ शकतात."}
{"speaker": "Patient", "date":"", "dialogue": "आणखी कोणत्या प्रकारचा साथीदार मला मार्गदर्शन देऊ शकतो, माझ्या आवाजाचं प्रश्न कितपत संभवतो?"}
{"speaker": "Health Worker", "date":"", "dialogue": "You won't be alone in this. A full multidisciplinary team of surgeons, radiation doctors, chemotherapy doctors, dietitians, and therapists will work together on your case."}
{"speaker": "Patient", "date":"", "dialogue": "ही टीम कुठे भेटते, कोणत्या तारखांना, आणि कसा समन्वय साधता?"}
{"speaker": "Health Worker", "date":"", "dialogue": "MDT बैठक ठरलेल्या तारखा/स्थितींच्या अनुरोधाने होतात आणि patient family सहभागी होऊ शकतात; स्टेजिंग नंतर पुढचा रस्ता स्पष्ट केला जातो."}
{"speaker": "Patient", "date":"", "dialogue": "आम्हाला baseline tests दोन आठवडे आत पूर्ण करायचे आहेत, आणि imaging/biopsy व्यवस्थित करायचे आहेत, हो?"}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, baseline tests दोन आठवड्यात पूर्ण होतील; ऑरल/डेंटल exam, रक्तचाचण्या, imaging, biopsy तयारी व्यवस्थित आयोजित केली जाईल."}
{"speaker": "Patient", "date":"", "dialogue": "HPV रिपोर्ट सकारात्मक आला तर काय करायचं, डॉक्टर?"}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV स्थिती tumor चालनांमध्ये काही प्रमाणात फरक आणते; पर निर्णय अनेक घटकांवर अवलंबून असतो; MDT निर्णय महत्त्वाचा."}
{"speaker": "Patient", "date":"", "dialogue": "आम्हाला आहार-आणि आहार-तज्ज्ञ काय मदत करतात, वजन राखण्यासाठी?"}
{"speaker": "Health Worker", "date":"", "dialogue": "प्रोटीन-युक्त आहार, फळ/भाजी, पुरेसे पाणी; पोषणतज्ज्ञ विशिष्ट योजनानुसार मार्गदर्शन करतील."}
{"speaker": "Patient", "date":"", "dialogue": "तुम्ही काही क्लिनिकल ट्रायलची माहिती देता का, अर्हता काय असते?"}
{"speaker": "Health Worker", "date":"", "dialogue": "क्लिनिकल ट्रायल्स अर्हता, logistics, खर्च याचा स्पष्ट विचार MDT बैठकानंतर होतो; Ayushman Bharat-type schemes बद्दल माहिती दिली जाते."}
{"speaker": "Patient", "date":"", "dialogue": "डायनिंग-आहार ठेवायचा तर मी कोणते अडचण आढळतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": "नियोजनात प्रोटीन-युक्त आहार, लहान-लहान भरे-भरे कार्यक्रम; पाणी आणि पौष्टिक आहार सुरक्षित ठेवण्यावर लक्ष."}
{"speaker": "Patient", "date":"", "dialogue": "गेल्या वर्षी वजन कमी झाले; वजन धारण्यासाठी काय योजना असतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": "प्रोटीन-समृद्ध डाएट, मिनी-भोजन, स्मूधी, पोषणतज्ज्ञ मार्गदर्शन; तर वजन वाढीसाठी विशेष प्लान तयार केला जाईल."}
{"speaker": "Patient", "date":"", "dialogue": "डॉक्टर, घरच्यांना कसे माहिती द्यावी, कोणते शब्द सोपे असतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": " MDT च्या निर्णय-योजनेसाठी plain-language स्पष्टीकरण देऊन family सदस्यांनाही समजेल असे पुरवतो; स्टेजिंग, अरोप, उपचार-योजना स्पष्ट केली जाते."}
{"speaker": "Patient", "date":"", "dialogue": "कधी回 MDT बैठक निर्धारित केली जाते आणि माझ्या कुटुंबाला कसे सहभागी करता येईल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "MDT बैठक निर्धारित तारखेला; आपला परिवार उपस्थित राहू शकतो; MDT निर्णयानुसार स्टेजिंग आणि पुढील दिशा स्पष्ट केली जाते."}
{"speaker": "Relative", "date":"", "dialogue": "डॉक्टर, आम्ही कोणत्या प्रकारच्या प्रश्नांची तयारी ठेवू? कोणते प्रश्न आपल्याला आवश्यक समजतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": "तुम्ही स्टेजिंग, उपचार-योजना, क्लिनिकल ट्रायल अर्हता, खर्च, विमा, आणि सहाय्यकार्याची माहिती साधारणपणे विचारू शकता; plain-language मध्ये सगळे स्पष्ट करतो."}
{"speaker": "Patient", "date":"", "dialogue": "आणि जर operation झाली तर पुनर्स्थापना किती दिवसात होईल, फुड-आहार कसा असेल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "ऑपरेशननंतर पुनर्प्राप्ती عدة आठवडे ते महिने घेते; आहार सुरळीत चालवण्यासाठी dietician मार्गदर्शन करतील; खासगी/स्वास्थ्य-आहार योजना सुरू होईल."}
{"speaker": "Patient", "date":"", "dialogue": "रेडिएशनच्या दरम्यान माझ्या त्वचेवर काही त्रास झाली तर काय उपाय असतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": "त्वचेला कोरडेपणा, जळцу, म्यूकोसा-रंजकता असल्यास त्वचा-आथवा mucosa-रक्षक उपाय, ओरेडा-हायड्रेशन, local skin care माहिती देईल."}
{"speaker": "Relative", "date":"", "dialogue": "आम्हाला किती वेळापूर्वी हॉस्पिटलला ड्रा-फॉलो-अपची माहिती दिली जाईल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "MDT निर्णयानंतर, फॉलो-अप तपासणी महिन्यातून एकदा ठेवणे सामान्य; तारखा MDT ने स्पष्ट केल्या जातील."}
{"speaker": "Patient", "date":"", "dialogue": "HPV स्थिती tumor चालनांमध्ये कोणते संभाव्य बदल करते, ते समजेल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV स्थिती tumor चालनात काही प्रमाणात वेगळेपणा आणू शकते; पर निर्णय MDटीवर अवलंबून असतो."}
{"speaker": "Relative", "date":"", "dialogue": "कुटुंबाप्रमाणे आम्हाला कधी कशा प्रकारे मदत करावी, घरात कोणते समन्वय ठेवावे?"}
{"speaker": "Health Worker", "date":"", "dialogue": "कुटुंब सदस्यांना साथ देण्यासाठी social worker, transport, अनुवाद सेवा, आणि insurance guidance उपलब्ध; स्पष्ट समन्वय ठेवून निर्णय घेतला जाईल."}
{"speaker": "Patient", "date":"", "dialogue": "अगदी शक्य झालं तर आम्ही क्लिनिकल ट्रायलची अर्हता बघणार आहोत. ती कशी चालते?"}
{"speaker": "Health Worker", "date":"", "dialogue": "क्लिनिकल ट्रायलची अर्हता MDT मध्ये तपासली जाते; logistics, travel, खर्च स्पष्ट केला जाईल; आपल्यासाठी उपलब्ध असतील तेव्हा माहिती दिली जाते."}
{"speaker": "Patient", "date":"", "dialogue": "काऊंसिलिंगची गरज वाटते; तंबाकू/दारू चालू ठेवावे का?"}
{"speaker": "Health Worker", "date":"", "dialogue": "तंबाकू/दारूचा थांबवणं आग्रहाचं; cessation counseling, स्थानिक कार्यक्रम, प्रेरक संभाषण मदत करतात."}
{"speaker": "Relative", "date":"", "dialogue": "धन्यवाद, डॉक्टर. आम्हाला अगोदरच योजना समजली तरच आपल्याला मदत करतो."}
{"speaker": "Health Worker", "date":"", "dialogue": "चांगलं. plain-language माहिती, तयारीची सूची, आणि कागदपत्रे तयार, MDT तारखांची माहिती लवकर कळवू."}
{"speaker": "Patient", "date":"", "dialogue": "खर्च व विमाच्या बाबतीत आणखी काही प्रश्न आहेत; आपण कधी कॉल करायचं?"}
{"speaker": "Health Worker", "date":"", "dialogue": "तुम्हाला आवश्यक असल्यास फोन/ईमेलद्वारे कळवू; पुढच्या MDT तारखेपासून आधीच आवश्यकता असल्यास आम्ही माहिती देऊ."}
{"speaker": "Patient", "date":"", "dialogue": "या पृष्ठभागावर क्लिनिकल ट्रायला कसं जायचं, खर्च किती येतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": "पर्सनल अर्हता, प्रवास, खर्च, तपासण्या आणि उपचार-योजनेची माहिती MDT देईल; काही खर्च विमा-आधारित कव्हर होऊ शकतो."}
{"speaker": "Patient", "date":"", "dialogue": "घरच्यांच्या कवरेजची आवश्यकता पडली तर कोणते कागदपत्रे आवश्यक असतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": "आधारकार्ड, हेल्थ कार्ड, विमा पॉलसी, पूर्वचाचण्या/Imaging reports; ऑनलाइन रजिस्ट्रेशनसाठी आधारकुटुंबाचा पत्ता असणं उपयोगी."}
{"speaker": "Relative", "date":"", "dialogue": "तारखा कळली की आम्ही कसे तयारी करू? हॉस्पिटलला येण्याची सोय कशी करायची?"}
{"speaker": "Health Worker", "date":"", "dialogue": "तारखा कळवू; रुग्णवाहिका/बस-टिकिटची व्यवस्था, अनुवाद सेवा, सोबत घेण्याच्या सूचना, प्रि-ऑपरेशन निर्देश."}
{"speaker": "Patient", "date":"", "dialogue": "गेल्या काही महिन्यांत वजन कमी झाले; आहारात कोणते उपाय चांगले?"}
{"speaker": "Health Worker", "date":"", "dialogue": "प्रोटीन-समृद्ध आहार, दुध-जन्य पदार्थ, अंडी, पनीर, बदाम; छोटे पण अनेकदा खाणे; पोषणतज्ज्ञ योजना तयार करतील."}
{"speaker": "Patient", "date":"", "dialogue": "HPV टेस्टची अंतेचं स्पष्टीकरण देऊ शकता का?"}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV च्या स्थितीनुसार ट्यूमरच्या आचार-धारणा काहीशी वेगळी दिसू शकते; पर निर्णय MDT घेतं."}
{"speaker": "Relative", "date":"", "dialogue": "आम्हाला या सर्वांची भाषा स्पष्टपणे समजली पाहिजे; आपण कमी-अधिक शब्दांत समजवायला मदत कराल ना?"}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, MDT सर्व माहिती plain-language मध्ये देईल; क्लिनिकल ट्रायल, अर्हता, खर्च, सर्व काही स्पष्टपणे."}
{"speaker": "Patient", "date":"", "dialogue": "सर्जरीची तयारी कशी करावी, कोणत्या दिवशी घडते, रुग्णालयात कसे रहायचं?"}
{"speaker": "Health Worker", "date":"","dialogue": "ऑपरेशनपूर्व बेसलाइन तपासण्या, डेंटल स्थिती तपासणी, नर्सिंग तयारी; MDT निर्णयानुसार पुढची तयारी."}
{"speaker": "Patient", "date":"", "dialogue": "रेडिएशन सुरू होईल तर दररोज किती वेळा, आणि त्वचा-ताळाबद्दल काय करावं?"}
{"speaker": "Health Worker", "date":"","dialogue": "सत्रे दररोज एक, 6-7 आठवडे; त्वचा सुरक्षित ठेवण्यासाठी सल्ले, ल्यूब्रिकेशन, म्यूकोसा काळजी."}
{"speaker": "Patient", "date":"", "dialogue": "चेमोची डोस कशी दिली जाईल, किती वेळ लागतो?"}
{"speaker": "Health Worker", "date":"","dialogue": "लोकल-आयोडिन करण्याची आवश्यकता असलेल्या केसेसमध्ये weekly डोस किंवा कमी डोस दराच्या चेमोची कल्पना असते; तुमच्यावर MDT निर्णय."}
{"speaker": "Relative", "date":"", "dialogue": "आम्हाला ठेका-रहण्याची माहिती द्या; आम्ही तयारी करतो."}
{"speaker": "Health Worker", "date":"", "dialogue": "यथाशक्ती तयारीची मदत केली जाईल; social worker, transportation, भाषांतर सेवा उपलब्ध."}
{"speaker": "Patient", "date":"", "dialogue": "HPV स्थिती tumor वर कसा परिणाम करते ते कळले तरच चांगले."}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV स्थिती tumor ची आचरण करण्याची क्षमता बदलू शकते; पर निर्णय MDTवर अवलंबून."}
{"speaker": "Patient", "date":"", "dialogue": "तुमची टीम मला नेहमी समजावून सांगेल अशी आशा आहे."}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, आपण कोणत्याही टप्प्यावर विचारलेच पाहिजे तशी माहिती देऊ; MDT तुमच्याकडे स्पष्ट माहिती राहील."}
{"speaker": "Patient", "date":"", "dialogue": "काय-काय कागदपत्रे माझ्याकडे असावीत, ते तयार ठेवायला हवे?"}
{"speaker": "Health Worker", "date":"", "dialogue": "आधारकार्ड, हेल्थ कार्ड, वैद्यकीय इतिहासाचा સnk, imaging reports; online registration/verified documents."}
{"speaker": "Patient", "date":"", "dialogue": "कधी माझ्या क्षेत्रात MRI उपलब्ध असेल, मुंबईतील कोणते केंद्र योग्य आहेत?"}
{"speaker": "Health Worker", "date":"", "dialogue": "MRI उपलब्धता चांगली आहे; माझ्या मार्गदर्शनानुसार तुमच्यासाठी स्थानिक केंद्रांची सूची देतो."}
{"speaker": "Patient", "date":"", "dialogue": "आपण मला एकदम स्पष्टपणे योजना सांगाल का? मी तुम्हाला प्रश्नांची यादी देईन."}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, MDT च्या पथदर्शकानुसार baseline tests, MDT बैठक, स्टेजिंग, पुढील दिशा—सर्जरी/रेडिएशन/चेमो—एकत्रितपणे स्पष्ट होईल."}
{"speaker": "Patient", "date":"", "dialogue": "ठीक. तुम्ही कोणत्या प्रश्नांची तयारी करू शकाल आणि मी कोणते दरवर्षी विचारू?"}
{"speaker": "Health Worker", "date":"", "dialogue": "Tumhi स्टेजिंग, उपचार-योजना, क्लिनिकल ट्रायल अर्हता, खर्च, विमा, आणि सहाय्यकार्याची माहिती विचारू शकता; आम्ही plain-language मध्ये उत्तर देऊ."}
{"speaker": "Patient", "date":"", "dialogue": "त्यानुसार आम्ही एक प्रश्नांची सूची बनवू आणि MDTच्या दिवशी आणू."}
{"speaker": "Health Worker", "date":"", "dialogue": "बरं, तुमची सूची MDT मध्ये सादर होईल; आम्ही स्पष्टपणे उत्तर देऊन निर्णय सोपा करतो."}
{"speaker": "Patient", "date":"", "dialogue": "धन्यवाद, काही प्रश्न आधीच माझ्या कुटुंबाला पाठवायचे आहे."}
{"speaker": "Health Worker", "date":"", "dialogue": "ठीक; plain-language सामग्री, ऑनलाइन लिंक, आणि clinic-फोल्डर दोन्ही तुमच्यासाठी उपलब्ध."}
{"speaker": "Patient", "date":"", "dialogue": "काही दिवसांत MDTची तारखा कळतील, होय ना?"}
{"speaker": "Health Worker", "date":"", "dialogue": "होय, baseline result मिळाल्यानंतर MDT बैठक ठरते; स्टेजिंग झाल्यावर शक्यता-आधारित रस्ता स्पष्ट होतो."}
{"speaker": "Patient", "date":"", "dialogue": "अंतिम स्टेजिंग नंतर आपल्याला काय सूचना मिळतील?"}
{"speaker": "Health Worker", "date":"", "dialogue": "स्टेजिंगनुसार सर्जरी, रेडिएशन किंवा chemoradiation, एकत्रित किंवा वैयक्तिक रस्ता; प्रत्येक टप्प्यावर स्पष्ट माहिती."}
{"speaker": "Patient", "date":"", "dialogue": "याच्या प्रत्येक टप्प्यावर माझ्या आवाजाचं परिणाम काय होईल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "उच्चारात काही बदल राहू शकतो, पण स्पीच थेरपीने सुधारणा शकते; वेळोवेळी मूल्यांकन आवश्यक."}
{"speaker": "Patient", "date":"", "dialogue": "खर्चाच्या बाबतीत काही विशिष्ट अट असल्यास सांगाल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "आयुष्मान भारत व अन्य योजनांमध्ये कव्हर होत असलेल्या बाबी तपासू; क्लिनिकल ट्रायल अर्हता असल्यास खर्च कमी होऊ शकतो."}
{"speaker": "Relative", "date":"", "dialogue": "कुटुंबाच्या कोविड-यासारख्या तालमींसारखा आता आपल्याला मार्गदर्शन मिळेल का? आम्हाला माहितीची गरज आहे."}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, आम्ही सोशल वर्करद्वारे घरून-घरापर्यंत माहिती पोहोचवू; भाषांतर सुविधा, ट्रान्सपोर्ट, आणि insurance guidance उपलब्ध."}
{"speaker": "Patient", "date":"", "dialogue": "कधीपर्यंत baselineTests पूर्ण होतील आणि MDTकधी होईल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "baseline tests दोन आठवड्यात पूर्ण होतील; imaging/bio-opsy सोबत MDT बैठक दोन आठवड्यात निश्चित केली जाईल."}
{"speaker": "Patient", "date":"", "dialogue": "HPVचा परिणाम काय असेल, आणि आपल्याला काही क्लिनिकल-ट्रायलोंची संधी मिळते का?"}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV सकारात्मक असला तरी निर्णय बहुधा MDTचे; क्लिनिकल ट्रायलची संधी अर्हतेनुसार दिसते; मार्गदर्शन दिले जाईल."}
{"speaker": "Relative", "date":"", "dialogue": "आम्हाला डॉक्टरांच्या भाषेत अधिक समजावून सांगाल ना? आम्ही प्रश्न तयार करायलाच हवे."}
{"speaker": "Health Worker", "date":"", "dialogue": "नक्की. MDTचा मार्ग plain-language मध्ये स्पष्ट करतो; प्रश्नांची सूची घेऊन या."}
{"speaker": "Patient", "date":"", "dialogue": "तुम्ही कोणत्याही प्रक्रियेच्या वेळापत्रकाची एक ठराविक रचना देऊ शकता?"}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, baseline tests, imaging, biopsy, MDT बैठक, स्टेजिंग, आणि त्यानंतर सर्जरी/रेडिएशन/चेमो-योजना—ही एकत्रित रचना असते."}
{"speaker": "Patient", "date":"", "dialogue": "चला तर पुढे काय करायचं, आम्ही आजच तयारी करतो का?"}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, baseline tests आता सुरू करू; रक्त, dental status, imaging, biopsy-प्रस्ताव; MDT बैठक दोन आठवड्यात ठरते."}
{"speaker": "Patient", "date":"", "dialogue": "आम्ही चालतोय; कृपया तुम्ही आम्हाला वेळापत्रक कळवा."}
{"speaker": "Health Worker", "date":"", "dialogue": "चालेल. MDT तारखा/visit schedule तुमच्यासोबत coordinating करतो."}
{"speaker": "Patient", "date":"", "dialogue": "धन्यवाद. आपण या जगातला आणखी एक प्रश्न."}
{"speaker": "Health Worker", "date":"", "dialogue": "मग इथेच विचारलं जाऊ शकतं; आम्ही तुम्हाला सोबतच मार्गदर्शन देऊ."}
{"speaker": "Patient", "date":"", "dialogue": "तुम्ही मला कसे संपर्कात ठेवाल, आणि आकडेवारी कशी सुरक्षित ठेवायची?"}
{"speaker": "Health Worker", "date":"", "dialogue": "फोन, ईमेल, आणि ऑनलाइन पोर्टलवर संपर्क; तुमची माहिती encrypted पद्धतीने सुरक्षित ठेवली जाईल."}
{"speaker": "Patient", "date":"", "dialogue": "तुमच्या टीममध्ये Nutritionist, Pharmacist, Social Worker आणि Speech Therapist असतील का?"}
{"speaker": "Health Worker", "date":"", "dialogue": "होय, MDT मध्ये Nutritionist, Speech Therapist, Social Worker, Nursing टीम, Imaging Specialist सर्व सहभागी असतील."}
{"speaker": "Relative", "date":"", "dialogue": "आम्हाला प्रत्येक डॉक्टरांची भूमिका समजावी; आम्ही स्टेजिंग-नंतर कोणते निर्णय घेऊ ते समजावून सांगा."}
{"speaker": "Health Worker", "date":"", "dialogue": "ठीक; MDT स्पष्ट भूमिका देईल: Surgical Team, Medical Oncologist, Radiation Oncologist, Dietitian, Social Worker."}
{"speaker": "Patient", "date":"", "dialogue": "खर्चांचे अचूक बांधकाम कधी काय माहिती मिळेल? विमा-आधारित कव्हर कसं मिळेल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "आम्ही विमा-गाइडन्स देतो; आयुष्मान भारत व अन्य योजनांची माहिती; कव्हरिंग तीन स्तरांवर तपासली जाते."}
{"speaker": "Patient", "date":"", "dialogue": "आता मी डॉक्टरांना कळवतो, आम्ही MDT लाईन-अपकडे वळूया."}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, MDT-समन्वयासाठी आपण पुढे जा; basalene tests पूर्ण झाल्यावर पुढची बैठक होईल."}
{"speaker": "Patient", "date":"", "dialogue": "काय तुमच्याकडे या संदर्भात काही खास मिनी-लिस्ट आहे का?"}
{"speaker": "Health Worker", "date":"", "dialogue": "Baseline test checklist, HPV status, imaging reports, biopsy results, consent documents, and appointments schedule—या सहज चेकलिस्ट देतो."}
{"speaker": "Relative", "date":"", "dialogue": "आमची भूमिका काय अपेक्षित आहे? कडेकोट चर्चा होईल का?"}
{"speaker": "Health Worker", "date":"", "dialogue": "तुम्ही उपस्थित असाल तर MDT चर्चेत family-फ्रेंडली संवाद होतो; प्रश्नांना उत्तर देण्यात येईल."}
{"speaker": "Patient", "date":"", "dialogue": "आपण dua-line Tata Rijter? आम्हाला आपली language support आवश्यक."}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, language support, translator, आणि essential language-appropriate information उपलब्ध."}
{"speaker": "Patient", "date":"", "dialogue": "धन्यवाद, काही दिवसांत आम्ही दोघेही तयारी करतो."}
{"speaker": "Health Worker", "date":"", "dialogue": "चांगलं; baseline tests सुरू करु; MDT 2-3 आठवड्यात निर्णय देईल."}
{"speaker": "Relative", "date":"", "dialogue": "आम्ही क्लिनिकल-ट्रायल बद्दल विचार करणार; आपल्याला दिशानिर्देश दिलेले आहेत ना?"}
{"speaker": "Health Worker", "date":"", "dialogue": "होय; ट्रायल-गाइडन्स MDT देईल; अर्हता असल्यास तुम्हाला संधी मिळेल."}
{"speaker": "Patient", "date":"", "dialogue": "आपण माझ्या मुलींसोबतही बोलू शकता का, तिला माहिती देण्यासाठी?"}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, परिवारातील सदस्यांना समजावा म्हणून plain-language माहिती देतो; मुलींसुद्धा उपस्थित राहू शकतात."}
{"speaker": "Patient", "date":"", "dialogue": "त्यांची मदत महत्त्वाची आहे; MOTIVATION आणि सपोर्ट कसा देऊ?"}
{"speaker": "Health Worker", "date":"", "dialogue": "Motivational interviewing, cessation support groups, local programs, आणि social worker-initiatives उपलब्ध."}
{"speaker": "Patient", "date":"", "dialogue": "कनिष्ठपणे, आम्ही डॉक्टरांना पुढील आठवड्यात भेटू."}
{"speaker": "Health Worker", "date":"", "dialogue": "ठीक; MDT तारखा कळवतो; baseline results येताच भविष्यवाणी आणि स्टेजिंग स्पष्ट होईल."}
{"speaker": "Patient", "date":"", "dialogue": "एकटीच आलो होतो, पर आता माझा मित्र/परिवार माझ्यासोबत असणार."}
{"speaker": "Health Worker", "date":"", "dialogue": "तुम्हाला साथ देण्यासाठी परिवार आणू शकतो; MDT बैठकात ते सहभागी होऊ शकतात."}
{"speaker": "Patient", "date":"", "dialogue": "खूप चांगलं. आता मला काही प्रश्नांची तयारी करायची आहे."}
{"speaker": "Health Worker", "date":"", "dialogue": "होय, तुमची प्रश्नांची सूची तयार करून आणा; आम्ही एक-एक करुन स्पष्ट करतो."}
{"speaker": "Patient", "date":"", "dialogue": "HPV चा निकाल कसा उपयोगी ठरतो, आणि क्लिनिकल ट्रायलची अर्हता कशी तपासते?"}
{"speaker": "Health Worker", "date":"", "dialogue": "HPV चा निकाल tumor behavior बदलेल; ट्रायलमध्ये अर्हता, प्रवेश व खर्च स्पष्ट करतो."}
{"speaker": "Relative", "date":"", "dialogue": "आम्ही आम्ही आरोग्य विमा आणि सरकारी योजना कोणत्या स्टेजिंग-जन्य खर्चांवर उपयोगी ठरतील ते तपासतो."}
{"speaker": "Health Worker", "date":"", "dialogue": "होय, विमा-कव्हर व सरकारी योजना, ट्राय-आधी योजना स्पष्ट करतो; आमच्या टीमकडे कागदपत्रांची तयारी ठेवू."}
{"speaker": "Patient", "date":"", "dialogue": "कधी मी पुन्हा भेटू आणि MDTची अंतिम रचना काय असेल?"}
{"speaker": "Health Worker", "date":"", "dialogue": "बेसलाइन परिणामांनुसार MDT दोन आठवड्यात अंतिम निर्णय देईल; मग सर्जरी/रेडिएशन/चेमोचा क्रम आकारले जाईल."}
{"speaker": "Patient", "date":"", "dialogue": "गलेाच्या आजारांनी आवाजावर परिणाम झाला तर स्पीच-थेरपी कशी मदत करते?"}
{"speaker": "Health Worker", "date":"", "dialogue": "स्पीच-थेरपी ध्वनीची गुणवत्ता परत आणण्यास मदत करते; ठोस अभ्यासांनी देखील फायदे दिले आहेत."}
{"speaker": "Patient", "date":"", "dialogue": "नुकतीच डॉक्टरांनी वजन वाढीवर भर द्यायला सांगितलं; आम्हाला काही खास उपाय देऊ शकता?"}
{"speaker": "Health Worker", "date":"", "dialogue": "हाई-प्रोटीन आहार, छोटे-छोटे आहार आणि पोषणतज्ज्ञाचा प्लान; लवकर वजन परत प्राप्त होइल."}
{"speaker": "Relative", "date":"", "dialogue": "अर्थात. आम्ही सर्वांची तयारी ठेवत आहोत; कोणते प्रश्नांना उत्तर दयायला हवे?"}
{"speaker": "Health Worker", "date":"", "dialogue": "स्टेजिंग, उपचार-योजना, क्लिनिकल ट्रायल अर्हता, खर्च, विमा, आणि सहाय्यकार्याची माहिती स्पष्टपणे द्यावी."}
{"speaker": "Patient", "date":"", "dialogue": "मी विचारूं थोडे, तुमची टीम मला नेहमी सपोर्ट देईल ना?"}
{"speaker": "Health Worker", "date":"", "dialogue": "होय, आम्ही नेहमी तुम्हाला साथ देण्यास तयार आहोत; MDT मार्गदर्शन, follow-up आणि आवश्यकतेप्रमाणे सहायता."}
{"speaker": "Patient", "date":"", "dialogue": "धन्यवाद. मला आता जरा विश्रांती हवी आहे."}
{"speaker": "Health Worker", "date":"", "dialogue": "तुम्हाला आराम हवा असेल तर आराम करा; baselines पूर्ण झाल्यावर आम्ही पुन्हा संपर्कात येऊ."}
{"speaker": "Patient", "date":"", "dialogue": "ठीक. MDT कधी असते ते मला कळवायला हरकत नाही."}
{"speaker": "Health Worker", "date":"", "dialogue": "हो, MDT तारखा आम्ही लवकरच कळवू; त्या दिवशी स्टेजिंग व पुढील उपचार स्पष्ट होईल."}
{"speaker": "Patient", "date":"", "dialogue": "आणखी एक प्रश्न. क्लिनिकल ट्रायलमध्ये अर्ज करायचा असल तर मला काय करायचं?"}
{"speaker": "Health Worker", "date":"", "dialogue": "MDT निर्णयानंतर ट्रायलची अर्हता पाहण्यात येते; travel-आणि logistically तयारी आपणाच असते; सामील होण्याची प्रक्रिया सोपी."}
{"speaker": "Relative", "date":"", "dialogue": "कदाचित आता आम्हाला परिवार सदस्यांच्या स्पर्धा-भागासाठी माहिती देउ."}
{"speaker": "Health Worker", "date":"", "dialogue": "तुमच्या कुटुंबाला क्लिनिकल ट्रायल व क्लिनिकल-ट्रायलोंचा प्रॉस्सेस स्पष्टपणे देत_planes."}
{"speaker": "Patient", "date":"", "dialogue": "आम्ही तयार आहोत; कृपया पुढील 2-3 दिवसांत आपला दृष्टी-निर्देश देऊ."}
{"speaker": "Health Worker", "date":"", "dialogue": "ठीक; baseline tests सुरू; रक्त, dental status, imaging, biopsy तयारी; 2-3 दिवसांत निकाल; MDT निर्णय."}
{"speaker": "Patient", "date":"", "dialogue": "तुमच्याशी आणखी एकदा बोलू. धन्यवाद."}
{"speaker": "Health Worker", "date":"", "dialogue": "नक्की. MDT तारखा, स्टेजिंग, आणि पुढील दिशा आम्ही लवकरच तुमच्याशी शेअर करतो."}
{"speaker": "Patient", "date":"", "dialogue": "मी तयार आहे. कृपया मला मार्गदर्शन दे."}
{"speaker": "Health Worker", "date":"", "dialogue": "तुमच्यासाठी baseline tests सुरू; MDT निर्णयानुसार पुढचा रस्ता ठरेल; तसेच आहार, cessation support, psychosocial services संचालित होतील."}
{"speaker": "Relative", "date":"", "dialogue": "धन्यवाद; आम्ही तुमचा विश्वास वाढवतो आणि सर्वतोपरी साथ देऊ."}
Ground Truth:
Summary of Head and Neck Cancer dialogue (key events, symptoms, diagnosis, and treatment steps)

- Patient profile and presenting symptoms
  - Names Rajesh Patel, ~52 years, Mumbai. Symptoms: lump in neck, hoarseness, dysphagia (difficulty swallowing), sleep disturbance, unintended weight loss.
  - Risk factors noted: daily tobacco smoking, pan masala use; HPV testing considered.
  - Question about HPV testing and its impact on plan.

- Diagnostic plan and initial assessments
  - Baseline investigations plan: oral/dental examination, pharyngeal evaluation, endoscopy, FNAC/biopsy, basic blood tests, CT/MRI imaging.
  - HPV testing to be considered; results (biopsy) expected in 2–5 days; imaging important for MDT decisions.
  - Goal to complete baseline assessments within about two weeks; imaging/biopsy organized and results reviewed by MDT.

- MDT framework and decision-making
  - Multidisciplinary Team (MDT) includes oral surgeon, medical oncologist, radiation oncologist, imaging specialist, nutritionist; clinical trial options discussed.
  - Emphasis on presenting information in plain language; HPV status and trials considered case-by-case.
  - MDT meetings scheduled at defined times; patient and family may participate.

- Timeline and sequencing of evaluation
  - Baseline tests aimed to be completed within two weeks; then MDT meeting about staging and next steps.
  - Final treatment path (surgery, radiotherapy, or chemoradiation; combined or individual) decided after MDT based on staging.

- Treatment planning framework (surgery vs radiotherapy)
  - Both surgery and radiotherapy discussed; final plan depends on staging.
  - If advanced stage, typical approaches include surgery + radiotherapy, sometimes with chemotherapy; MDT makes final choice and explains it for informed consent.

- HPV testing and clinical trials in decision process
  - HPV status may influence tumor behavior and potentially lead to trial options or adjustments in radiotherapy approach.
  - Clinical trials assessed for eligibility, logistics, and costs; schemes like Ayushman Bharat discussed.

- Nutrition, lifestyle, and psychosocial support
  - Nutrition emphasized: protein-rich diet, fruits/vegetables, adequate fluids; dietitian will tailor plan.
  - Tobacco/alcohol cessation counseling; local cessation programs offered.
  - Psychosocial support highlighted: family involvement, social worker, insurance guidance, government schemes, and trial eligibility assistance.

- Logistics, documentation, and access to resources
  - Required documents: identity cards, medical history, imaging reports; online registration and verified documents.
  - Language support and translation services available; social worker assistance; insurance guidance; rural-urban access considerations.
  - Coordination for travel and patient-family involvement in MDT discussions.

- Next steps and anticipated events
  - Baseline tests to be completed in about two weeks; imaging and biopsy arranged.
  - MDT meeting to finalize staging and determine direction (surgery/radiotherapy/chemoradiation).
  - Post-MDT: results shared with patient/family; follow-up schedule and logistics planned; ongoing nutritional, cessation, and psychosocial support.

- Patient concerns and counseling expectations
  - Endoscopy: minor procedure with local anesthesia or light sedation; brief duration; pain control explained.
  - Potential treatment effects: voice changes, swallowing difficulties, fatigue; radiotherapy-related skin and mucosal effects; long-term follow-up.
  - Travel and access: availability of imaging centers; rural-urban differences addressed.
  - Follow-up: typically monthly initially; MDT-driven updates provided as needed.

- Key takeaways and trajectory
  - Presentation leads to baseline evaluation, HPV testing, and imaging within ~2 weeks; results guide MDT-based staging.
  - Final plan (surgery, radiotherapy, chemoradiation, or combinations) decided by MDT after staging; treatment plans explained in plain language.
  - Integrated support: nutritional counseling, cessation programs, psychosocial services, and assistance with paperwork, insurance, and potential clinical trials.
  - Family involvement is encouraged; MDT and care team aim to keep the patient and family well-informed at every step.

- Core message
  - The patient’s condition, imaging/biopsy results, and HPV status will drive MDT-guided staging and treatment decisions. Throughout, there will be emphasis on plain-language explanations, comprehensive supportive care (nutrition, cessation, psychosocial), and assistance with documentation, insurance, and trial access.

Qwen-2.5-7B-fewshot:
Clinical Summary:
Rajesh Patel, 52, from Mumbai, presents with symptoms of throat pain, voice change, difficulty swallowing, night sweats, and slight weight loss over the past few months. He smokes regularly and consumes alcohol daily. The patient is referred for an MDT (Multidisciplinary Team) meeting to determine staging, further investigations, and treatment plans. The initial plan involves baseline tests including blood work, dental examination, endoscopy, and imaging (CT/MRI). The MDT meeting is scheduled for two weeks' time to discuss results and plan further steps.

Key Points:
1. **Symptoms**: Throat pain, voice change, difficulty swallowing, night sweats, slight weight loss.
2. **Risk Factors**: Regular smoking, alcohol consumption.
3. **Initial Plan**:
   - Baseline tests: Blood work, dental examination, endoscopy, imaging (CT/MRI).
   - MDT meeting: Two weeks from now to discuss results and plan further steps.
4. **MDT Role**: To determine staging, treatment plan, and eligibility for clinical trials.
5. **Investigations**:
   - HPV testing: To assess viral involvement.
   - Imaging: CT/MRI to evaluate tumor size, location, and lymph node involvement.
   - Biopsy: To confirm tumor characteristics.
6. **Treatment Planning**:
   - Staging: Based on CT/MRI, endoscopy, biopsy, and patient history.
   - Treatment options: Surgery, radiotherapy, chemotherapy, depending on staging.
7. **Nutritional Support**: Emphasis on a high-protein diet to manage weight loss.
8. **Financial and Logistical Support**: Discussion on insurance coverage and government schemes.
9. **Family Involvement**: Encouragement for family members to participate in follow-ups and decision-making.
10. **Follow-Up**: Scheduled follow-up visits every two weeks to monitor progress and adjust treatment plans.

4

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Health Worker", "date": "", "dialogue": "डॉक्टर: आपण एकत्र काम करणार आहोत, त्यामुळे कोणतेही प्रश्न किंवा चिंताएं नाहीत; कृपया आपलं नाव, वय, राहण्याचं ठिकाण, आणि आजची मुख्य तक्रार काय आहे ते सखोलपणे सांगा."}
{"speaker": "Patient", "date": "", "dialogue": "रजा, मी राजेश पटेल, 45 वर्षाचा, मुंबईत राहतो. गेल्या काही आठवड्यांपासून गळ्यात गोळा असल्यासारखी जाणीव, आवाज हलका व्हायचा, खायला अडचण, आणि वजन घटतंय असा अनुभव आहे."}
{"speaker": "Health Worker", "date": "", "dialogue": "समजलं; यातलं सर्व एकत्र पाहायला हवं. धूम्रपान, pan masala, किंवा अलीकडे अॅल्कोहोलचा वापर सुरु/वired? HPV बद्दल माहिती आहे का, असा इतिहास ठरवण्याचा विचार आहे."}
{"speaker": "Patient", "date": "", "dialogue": "होय, मी दीर्घकालीन तंबाखू वापरतोय, pan masala दररोज 2-3 वेळा; अलीकडे अॅल्कोहोल कमी केलं. HPV बद्दल माहिती नाही; चाचणी करावी का ते मला कळत नाही."}
{"speaker": "Health Worker", "date": "", "dialogue": "चांगलं; पुढे तोंड, घसा तपासणी, बायोप्सीची योजना, आणि CT/MRI चा क्रम ठरेल; निकाल 2-3 दिवसांत मिळण्याची शक्यता. या सर्व प्रक्रियेत तुमचं मुल्यवान परिवार साथ देईल का?"}
{"speaker": "Patient", "date": "", "dialogue": "हो, मी आज एकटा आलोय; पुढच्या भेटीला माझं कुटुंब सदस्य येईल, परंतु या वेळेस मला सगळं स्पष्टपणे समजावून घ्यायचं आहे."}
{"speaker": "Health Worker", "date": "", "dialogue": "तयार असाल तर आजच बेसलाइन तपासणी साधू, परंतु फक्त आपल्या आणि तुमच्या कुटुंबाच्या सोयीसाठी. आधारकार्ड, आरोग्य कार्ड, जुनी रिपोर्ट्स, इमेजिंग कागदपत्रं आणण्याची तयारी करा."}
{"speaker": "Patient", "date": "", "dialogue": "समजलं; बायोप्सीसाठी तयारी कशा प्रकारची असते? वेदना, anesthesiaचा प्रकार, आणि निकाल कधी मिळतील हे मला समजायला हवं."}
{"speaker": "Health Worker", "date": "", "dialogue": "बायोप्सीमध्ये सामान्यतः हलकी वेदना असते; स्थानिक anesthesia लागू होतो; निकाल 2-5 दिवसांत मिळण्याचा प्रयत्न; जर गळा-फ्लोअर भाग असेल तर ENT विशेषज्ञांची मदत घ्यावी शकते."}
{"speaker": "Patient", "date": "", "dialogue": "मला वजन कमी झालेलं आहे, अन्न घेण्यात अडचण होते, आवाज काहीसे बदलला आहे; या स्थितीला आपण काय उपाय सुचवाल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "या चिन्हांवर आधारित आपला प्रथमिक विचार metastasisची शक्यता आहे; परंतु एकत्रितपणे पडताळणी करावी लागते, ज्यामध्ये बायोप्सी, imaging आणि HPV चाचणी सामील असतील."}
{"speaker": "Patient", "date": "", "dialogue": "HPV चाचणी tumorच्या स्टेजिंगवर कसा परिणाम करेल? माझ्या परिस्थितीत तो निर्णयक ठरेल काय?"}
{"speaker": "Health Worker", "date": "", "dialogue": "HPVचा परिणाम tumorच्या वर्तन, स्टेजिंग आणि उपचारांच्या पर्यायांवर काही प्रमाणात प्रभाव पाडू शकतो; परंतु निर्णय एकाधिक घटकांवर आधारित असतो."}
{"speaker": "Patient", "date": "", "dialogue": "तुम्ही निकाल सोप्या भाषेत समजावून सांगू शकाल का? मला माझं कुटुंब जमल्यासोबत घेऊन पुढील स्टेप्स स्पष्टपणे सांगता."}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, आम्ही प्रत्येक शब्द साफ भाषेत समजावू; MDT चा संदर्भ, कधी बैठक होईल, कुठे, कोणाचे उपस्थिती आवश्यक, ते स्पष्टपणे कळवू आणि आवश्यक तयारीही सांगू."}
{"speaker": "Patient", "date": "", "dialogue": "आधार तपासणी, रक्त तपासणी, dental exam, इमेजिंग, बायोप्सीची तयारी यात दोन आठवडे धडधड चालतील;	report्स आल्यानंतर MDT कोणती दिशा देईल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, baseline tests दोन आठवड्यात पूर्ण होण्याची शक्यता; नंतर MDT रिपोर्ट देईल आणि स्टेजिंग स्पष्ट होईल; त्यानुसार ऑपरेशन, radiotherapy किंवा कॉम्बिनेशन ठरवायचं."}
{"speaker": "Patient", "date": "", "dialogue": "आहारात प्रोटीन-युक्त पदार्थ, फळं-भाज्या, पुरेपुर पाणी; वजन घटला आहे, त्यामुळे सुधारण्यासाठी कोणते आहार-सपोर्ट्स उपयोगी ठरणार?"}
{"speaker": "Health Worker", "date": "", "dialogue": "nutritionist सोबत संधी साधू, प्रोटीन-युक्त आहार, हलके frequent meals, हार्वर्ड-स्तराचे सप्लिमेंट्स विचारात घेऊ; वजन टिकवण्यासाठी पाणी आणि हाय-कॅलरी स्नॅक्स."}
{"speaker": "Patient", "date": "", "dialogue": "धूम्रपान सोडण्यासाठी स्थानिक कार्यक्रम, निकोटिन रिप्लेसमेंट थेरपी, आणि कुटुंबाचं योगदान कसे वाढवायचं, या बाबीची योजना सांगू शकाल का?"}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, निकोटिन रिप्लेसमेंट आणि सपोर्ट ग्रुप्स, सोशल वर्करचा समन्वय; तुमच्या सगळ्या पथ्य-श्रोतांना एकत्र करून एक सुदृढ योजना तयार करतो."}
{"speaker": "Patient", "date": "", "dialogue": "क्लिनिकल ट्रायल्सची संभाव्यता तपासण्यासाठी कोणत्या अटीं असतात? आयुष्मान भारत योजना क्लिनिकल ट्रायल्सशी कशी जुळते?"}
{"speaker": "Health Worker", "date": "", "dialogue": "ट्रायल्सची अटी वेगवेगळी असतात; पात्रता, सह्या, आणि लॉजिस्टिक्स स्पष्ट करतो. Ayushman Bharat सारख्या योजना काही रुग्णांना मदत करतात, परंतु प्रत्येक केस वेगळा."}
{"speaker": "Patient", "date": "", "dialogue": "कागदपत्रांची सूची पुन्हा एकवार देऊ शकाल का? MDT बैठकीसाठी कोणते फॉर्म्स, कोणते रिपोर्ट्स, आणि कोणत्या प्रमाणपत्रांची गरज आहे?"}
{"speaker": "Health Worker", "date": "", "dialogue": "आधार कार्ड, आरोग्य कार्ड, जुने रिपोर्ट्स, CT/MRI रिपोर्ट्स, बायोप्सी निकाल, फॉर्म्स; MDTपूर्व तयारीसाठी सर्व काही अचूक ठेवा."}
{"speaker": "Patient", "date": "", "dialogue": "MDT बैठकीची तारीख कायम कधी असते, आणि आम्ही दोन आठवड्यात तयारी पूर्ण करण्याचा ध्यास ठेवतो; आम्हाला उपलब्ध وقت कळवा."}
{"speaker": "Health Worker", "date": "", "dialogue": "तारीख सामान्यतः पुढील आठवड्यात ठरते; तुम्ही उपलब्ध असाल तर आम्ही त्यानुसार वेळ ठरवतो; MDT स्पष्ट झाल्यावर तुम्हाला माहिती देतो."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "मी लवकरच येणार आहे; मला संथ भाषा समजावी असे वाटते, कृपया कागदपत्रे सोप्या शब्दात समजावून सांगाल का?"}
{"speaker": "Health Worker", "date": "", "dialogue": "निश्चित, आम्ही प्रत्येक शब्द सोप्या भाषेत समजावू; क्लिनिकल टर्म्सची लिस्ट देतो, आणि शक्यतो डायग्रामने स्पष्टीकरण देतो."}
{"speaker": "Patient", "date": "", "dialogue": "गळ्यात वेदना, आवाज बदलला, अन्न खाण्यात अडचण; मला धैर्य टिकवून पुढे जायचंय; MDTजवळील तयारी कशी ठेवावी?"}
{"speaker": "Health Worker", "date": "", "dialogue": "तुमचं धैर्य महत्त्वाचं आहे. या स्थितीमध्ये ENT/ओरोल-एंडो-रेडियोलॉजीची अणिबंधक तपासणी, बायोप्सी, आणि MDT निर्णय घेईल."}
{"speaker": "Patient", "date": "", "dialogue": "बायोप्सीसाठी anesthesia प्रकार कोणते असतील? तयारीत कोणते विशेष तपशील आवश्यक?"}
{"speaker": "Health Worker", "date": "", "dialogue": "अक्सर स्थानिक anesthesia फायदेशीर; काही प्रकरणात संपूर्ण-चेष्टा; तयारीत स्वच्छता, श्वासोच्छ्वास पद्धत, आणि निकाल मिळण्याच्या वेळेची कल्पना समजवतो."}
{"speaker": "Patient", "date": "", "dialogue": "स्टेजिंग कशी ठरते? ट्यूमरचा आकार, ठिकाण, लिम्फ नोड्स, HPV परिणाम एकत्र कसे विचारात घेतले जात?"}
{"speaker": "Health Worker", "date": "", "dialogue": "स्टेजिंग इमेजिंग (CT/MRI) आणि बायोप्सी निकालाने होते; HPV, ट्यूमराचा प्रकार, आकार, नोडल इन्वॉल्वमेंट या सर्वांचा विचार MDTमध्ये एकत्र केला जातो."}
{"speaker": "Patient", "date": "", "dialogue": "पद्धतशी सामना करण्यासाठी दोन आठवडे आत baseline tests पूर्ण होतील का?"}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, baseline tests दोन आठवड्यात पूर्ण होतील; इमेजिंग, रक्त तपासणी, दंत स्थिती, आणि biopsy तयारी; नंतर MDT निर्णय होईल."}
{"speaker": "Patient", "date": "", "dialogue": "जर सर्जरीचा पर्याय निवडला तर ते किती दिवस टिकेल आणि पोस्ट-ऑप रीकव्हरी कशी असेल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "शस्त्रक्रियेचा प्रकारावर अवलंबून काळ लागू होतो; पोस्ट-ऑप आहार, औषध-ऑपरेशननंतरची काळजी, फिजिकल थेरेपी आणि डिस्चार्ज-फॉलोअप महत्त्वाचे असते."}
{"speaker": "Patient", "date": "", "dialogue": "Radiotherapy किंवा Chemoradiationचा कोणता मार्ग जास्त फायदेशीर ठरेल? स्टेजिंगनुसार कधी निर्णय होते?"}
{"speaker": "Health Worker", "date": "", "dialogue": "स्टेजिंग आणि इमेजिंगनुसार radiotherapy किंवा chemoradiationचा निर्णय घेतला जातो; काही प्रकरणात दोन्हीचा कॉम्बिनेशन देखील प्रभावी ठरते."}
{"speaker": "Patient", "date": "", "dialogue": " nutritionsupport खूप आवश्यक दिसतो; वजन गमावणं रोखण्यासाठी कोणते आहार-सल्ले उपयोगी ठरतील?"}
{"speaker": "Health Worker", "date": "", "dialogue": "न्यूट्रिशन plan महत्त्वाचा; प्रोटीनयुक्त आहार, छोटी-छोटी frequent meals, पाणी आणि चांगल्या प्रकारचे सप्लिमेंट्स विचारात घ्या."}
{"speaker": "Patient", "date": "", "dialogue": "सरकारी योजना, विमा क्लेम, आणि MDTच्या खर्चासाठी कोणते फायदे आहेत? आवश्यक फॉर्म्स कोणते?"}
{"speaker": "Health Worker", "date": "", "dialogue": "Ayushman Bharat सारख्या योजना काही रुग्णांना मदत करतात; विमा क्लेमसाठी आधार-कार्ड, आरोग्य कार्ड, आणि रुग्ण प्रोफाइल आवश्यक असते."}
{"speaker": "Patient", "date": "", "dialogue": "आधार कार्ड आणि आयडी असल्यास काही खर्च कमी होतो का? आणखी कोणते फायदे मिळू शकतात?"}
{"speaker": "Health Worker", "date": "", "dialogue": "खर्च कमी होऊ शकतो; कधी कधी दवाखाना-फीसमध्ये सूट, कधी विमा-शर्तांची सवलत; सोशल वर्कर कडून योजनांची थेट मदत मिळते."}
{"speaker": "Patient", "date": "", "dialogue": "आपण भाषेचं अडचण न सोडता सोप्या शब्दात माहिती देता, ही मोठी मदत. आपल्याकडील साधे उदाहरण देता येईल का?"}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, आम्ही सोप्या भाषेत सांगतो; मुद्रित लिस्ट, डायग्राम, आणि FAQ देतो; काही शब्द समजत नसतील तर लगेच विचारा."}
{"speaker": "Patient", "date": "", "dialogue": "इंटरनेटवर विश्वसनीय माहिती मिळवण्यासाठी कोणते स्रोत योग्य? मी चुकीची माहिती टाळण्याचे उपाय विचारत आलो आहे."}
{"speaker": "Health Worker", "date": "", "dialogue": "सरकारी वेबसाइट्स, सरकारी योजनांची पन्ने, आणि रुग्ण-समर्थन संस्था यांच्या लिंक देतो; सत्यापनासाठी आम्ही आपल्याला मदत करू."}
{"speaker": "Patient", "date": "", "dialogue": "MDT बैठकची तिथी कधी निश्चित केली जाते? आम्ही तयारीसाठी कधी उपलब्ध रहावं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "MDT बैठक सामान्यतः पुढील 1-2 आठवड्यात होते; तुमच्या उपलब्धतेनुसार आम्ही वेळ निश्चित करतो, आणि प्रत्येकीला माहिती देण्याचा प्रयत्न करतो."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "मी येईन तेव्हा सोप्या भाषेत माहिती देऊ शकता का? आम्हाला डॉक्टरांचा शब्द समजण्यासाठी थोडा अतिरिक्त स्पष्टीकरण हवा."}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, आम्ही सोप्या शब्दांत स्पष्टीकरण देऊ; MDT निकाल, स्टेजिंग, आणि उपचाराच्या योजना स्पष्टपणे सांगू; साथ देण्याच्या प्रकारांनाही आम्ही माहिती देऊ."}
{"speaker": "Patient", "date": "", "dialogue": "आणखी एक प्रश्न; बायोप्सी निकाल कधी स्पष्ट होईल, त्या निकालाची अंतिम तारीख कधी कळेल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "बायोप्सी निकाल दोन ते पाँच दिवसांत येईल; काही प्रकरणांत थोडा जास्त वेळ लागू शकतो, परंतु आम्ही तुमच्याशी त्या वेळेस कळवू."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "त्या दिवशी आम्ही हॉस्पिटलमध्येच येऊ; आवश्यक असलेल्या मदतीसाठी आम्ही तयार राहू."}
{"speaker": "Health Worker", "date": "", "dialogue": "चांगलं. तुम्हाला कोणत्याही वेळी प्रश्न असतील तर आपण चेकलिस्ट, फॉर्म्स, व MDT नोट्स खास करून सोप्या भाषेत देऊ."}
{"speaker": "Patient", "date": "", "dialogue": "धन्यवाद डॉक्टर, मला आता स्पष्टपणे कळले आहे. MDTची बैठक कधी होईल ते कळवावी; मी आणि माझं कुटुंब तयारीला लागू."}
{"speaker": "Health Worker", "date": "", "dialogue": "तयार राहा; आम्ही बैठकाची तारीख लवकरच कळवू आणि आवश्यक तयारीची अंतिम चेकलिस्टही पाठवू."}
Ground Truth:
Summary of the Head and Neck Cancer dialogue (key events, symptoms, diagnosis, and treatment steps)

- Patient presentation and risk factors
  - Patient: Rajesh Patel, 45, Mumbai.
  - Symptoms: sensation of a lump in the throat, hoarseness, trouble sleeping, difficulty swallowing, and unintended weight loss.
  - Risk factors: long history of tobacco use and areca nut products (pan masala 2–3 times daily); occasional cigarettes/hookah; alcohol use decreased recently.
  - HPV: considered as a factor to assess and inform decisions.

- Initial assessment and diagnostic plan
  - Planned investigations: thorough intraoral/dental examination and pharyngeal evaluation; possible biopsy; CT/MRI imaging; basic blood tests as needed.
  - Biopsy timeline: results typically available in 2–5 days; imaging and biopsy results will guide next steps.
  - Patient preference: requested family involvement to support and understand results.

- Multidisciplinary evaluation and next steps
  - MDT approach: diagnosis to be confirmed by a multidisciplinary team (oral surgeon, oncologist, radiation-oncologist, imaging specialist, nutritionist); clinical trial options considered on a case-by-case basis.
  - HPV testing and trials: discussed as case-based decisions; full information provided to help decide.
  - Communication: emphasis on clear, plain-language explanations; MDT logistics (where/when meetings occur, who attends) explained.

- Timeline and sequencing of evaluation
  - Within two weeks: complete baseline assessment (oral/dental exam, blood tests) and arrangements for initial imaging/biopsy.
  - After results: MDT meeting to determine direction; imaging-based staging to decide between surgery, radiotherapy, or a combination.

- Treatment planning framework (surgery vs radiotherapy)
  - Both options discussed with their advantages and risks; final plan may involve combined modality therapy depending on staging.
  - Decision factors: staging and imaging results drive the final choice, with transparent explanations to aid informed consent.

- Nutrition, lifestyle, and psychosocial support
  - Nutrition: protein-rich diet, fruits/vegetables, adequate fluids; potential follow-up with a nutritionist to tailor plans due to weight loss.
  - Tobacco/alcohol cessation: counseling and resources offered; local cessation programs and strategies to improve therapy tolerability.
  - Psychosocial support: family involvement encouraged; social worker support; guidance on insurance and government schemes.

- Logistics, documentation, and access to resources
  - Essential documents: Aadhaar card, health card, medical history, imaging reports; online registration and verified documentation needed.
  - Family involvement: families encouraged to join visits; ongoing online chat/phone support for questions.
  - Insurance and schemes: information provided on accessing coverage; clinical trials and approvals discussed.

- HPV testing and clinical trials in decision process
  - HPV status may influence tumor behavior and staging, but treatment decisions remain multi-factorial (imaging, biopsy, blood work, clinical status).
  - Clinical trials: eligibility criteria and logistics explained; costs and processes to enroll explained; Ayushman Bharat-type schemes discussed for potential support.

- Next steps and anticipated events
  - In the next two weeks: completion of baseline tests (blood work, dental status, imaging, biopsy preparations).
  - MDT meeting: to finalize staging and treatment direction after results; patient and family will be promptly informed.
  - Coordination: appointment of the upcoming MDT date and scheduling of visits with the patient and family.

Overall, the dialogue outlines a structured diagnostic-to-treatment pathway for suspected head-and-neck cancer: initial symptom review and risk assessment, baseline clinical exams, biopsy and imaging within two weeks, MDT-driven staging to guide surgery, radiotherapy, or chemoradiation (individually or in combination), with integrated nutritional, cessation, and psychosocial support, plus attention to documentation, insurance access, and potential clinical trials. Family involvement and plain-language communication are emphasized throughout to support informed decision-making.
Qwen-2.5-7B-fewshot:
Clinical Summary:

- Patient Presentation and Symptoms:
  - Rajesh Patel, 45, from Mumbai, presents with a 3-month history of hoarseness, difficulty swallowing, weight loss, and mild throat discomfort.
  - Risk Factors: Long-term tobacco use (tobacco chewing for over 20 years, occasional gutka use, minimal alcohol consumption).

- Initial Evaluation and Plan:
  - HPV testing considered due to no known history.
  - Comprehensive clinical evaluation: throat inspection, dental status, nutritional status, and general health.
  - Possible ENT referral and readiness for CT/MRI imaging discussed.

- HPV Testing and Interpretation:
  - HPV testing to assess viral involvement, though not definitive alone.
  - HPV results will be integrated with clinical exam and imaging/biopsy findings to guide further steps.

- Investigations and Management Plan:
  - Endoscopic examination, biopsy, CT/MRI, TNM staging, and multidisciplinary treatment planning.
  - Baseline tests to be completed within 2 weeks.
  - Weekend appointment availability discussed for initial evaluations.
  - Family member (spouse) to accompany for support and documentation.

- Supportive Care and Follow-Up:
  - Nutritional support: emphasis on protein-rich diet, small frequent meals, adequate fluids.
  - Smoking cessation: local programs, nicotine replacement therapy, and family support.
  - Potential for clinical trials: eligibility, feasibility, and logistics discussed.
  - Government schemes like Ayushman Bharat for financial assistance.
  - Preparation for MDT meeting: necessary forms, reports, and documentation.
  - MDT meeting scheduled for the following 2 weeks, adjusting to patient availability.
  - Clear communication in simple language using checklists, forms, and MDT notes.

- Follow-Up and Next Steps:
  - Biopsy preparation: local anesthesia, specific procedures, and preparation details.
  - Staging: tumor size, location, lymph node involvement, and HPV results.
  - Treatment options: surgery, radiotherapy, or combination therapy based on staging.
  - Nutrition support: importance of a balanced diet, protein-rich foods, and supplements.
  - Financial and logistical support: government schemes, insurance claims, and hospital expenses.
  - Family involvement in planning and decision-making processes.

5

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Health Worker", "date": "", "dialogue": "आपला मुलगा 3 महिनेांचा आहे, मुंबईत राहतो. जन्मापासून हलका खोकला, वजन वाढत नाहीये, तेलकट शौचाचा त्रास, पाचनात अडचण आणि कधी कधी constipation झाले आहेत."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "नमस्कार डॉक्टर, हो आम्ही या बाबतीत सतर्क आहोत. आम्ही मुंबईतच राहतो, मुलगा आत्ता खूप थकलेला दिसतो, वजन कमी वाढतंय, शौच तेलकट दिसते."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF चा विचार करता येतो; पुढचं पाऊल pilocarpine Sweat Test मोठ्या केंद्रात करणे हितकारक ठरेल. तेव्हापासून CF diary सुरु करुयात."}
{"speaker": "Patient", "date": "", "dialogue": "बाळ म्हणून मी अजून बोलू शकत नाही; परंतू माझ्या आई-वडलांना पोटात वेदना दिसतात, खोकला चालू असतो, झोप कमी होते."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF diary सुरू करणार आहोत. diary तीन भागात असतो: Respiratory, Diet/Hydration, Weight/Stool."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "ठीक आहे डॉक्टर. आम्ही रोज खोकला, पाणी/ORS, वजन आणि शौच या तीन भागांचे लेखन करणार."}
{"speaker": "Health Worker", "date": "", "dialogue": "आजपासून diaryची सुरुवात करा; baseline वजन लिहा, पुढील चार आठवडे दररोज नोंद ठेवा, क्लिनिकल भेट चार आठवड्यानंतर ठरवू."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "समजलं. वजनाच्या सुरवातीचा मापा आम्ही आज करतो. आणखी काही आवश्यक असंल तर सांगा."}
{"speaker": "Health Worker", "date": "", "dialogue": "ORS घरगुती रेसिपी सोपं पद्धतीने देतो: 1 लिटर पाण्यात 6 टीस्पून साखर आणि एक चिमटी मीठ मिसळा; थंड पाणी मध्ये देत जा."}
{"speaker": "Mother", "date": "", "dialogue": "ठीक आहे. आम्ही दर काही तासांनी छोटे-small पाणी देत आहोत, पण प्रवासात कुठे आणायचं ते कसं ठरवायचं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, हलक्या पाण्यात छोटे-छोटे घास देत जा; मुलाला ओलावा ठेवण्यासाठी पाणी भरपूर द्या. वजन baseline करता दररोज वजन मोजा."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "आम्ही दररोज वजन मोजत आहोत; शौच तेलकट दिसते, काही दिवस पोटात गॅस होतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF diary तीन भागांमध्ये एकत्र ठेवा: Respiratory - खोकला कोणत्या वेळी, कोणत्या परिस्थितीत; Diet/Hydration - पाणी/ORS/मीठ; Weight/Stool - वजन व शौचाचे प्रकार."}
{"speaker": "Patient", "date": "", "dialogue": "खोकला दिवसाला किती वेळा येतो? पाणी किती द्यायचं ठरवायचं? शौचात तेलकट स्वर कुठं दिसतो?"}
{"speaker": "Health Worker", "date": "", "dialogue": "खोकला काही वेळा ठराविक परिस्थितीत वाढतो; दिवसभराचं वेळ-वेळ ठरवल्या जाऊ शकतो; शंका असल्यास आम्हाला माहिती द्या."}
{"speaker": "Mother", "date": "", "dialogue": "समजलं. मला काही अभ्यासालयाच्या पत्ते मिळतील का ज्याठिकाणी Sweat Test करता येईल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, Sweat Testसाठी केंद्रांची सूची तयार करतो; CMC Vellore, AIIMS Delhi, PGI Chandigarh अशी प्रमुख ठिकाणं आहेत."}
{"speaker": "Father", "date": "", "dialogue": "खर्चाची चिंता आहे; subsidies काय उपलब्ध आहेत ते कसं मिळवू शकतो?"}
{"speaker": "Health Worker", "date": "", "dialogue": "सरकारी योजना आणि subsidiesचा अवकाश असतो; आम्ही तुमच्यासाठी आवश्यक तर चालू प्रकरणात मदत करतो."}
{"speaker": "Mother", "date": "", "dialogue": "काय आम्ही चार आठवड्यात Sweat Testची तयारी करू शकतो? आम्हाला केंद्रांची माहिती आणि संपर्क हवं."}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, चार आठवड्यात क्लिनिकल भेट घेऊ; Sweat Testची तयारी, शेड्यूलिंगसाठी केंद्रांची पत्ता-सम्पर्क देईन."}
{"speaker": "Patient", "date": "", "dialogue": "CF diary काही-न काही आठवड्यात पूर्ण करण्याचा प्रयत्न करतो; आम्हाला अडचण आली तर कळव."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF diaryमध्ये तीन भागांचे नोंदी व्यवस्थित घ्या; baseline वजन आणि आजचा वजन बरोबरीने नोंदवा."}
{"speaker": "Mother", "date": "", "dialogue": "आम्ही आजपासून diaryचा फॉर्मॅट तयार करतो, तुम्ही मार्गदर्शन देत रहा."}
{"speaker": "Health Worker", "date": "", "dialogue": "Airway clearance ही महत्त्वाची स्तम्भ आहे; Manual Chest Physiotherapy (clapping) दिवसा दोन वेळा 5-10 मिनिटं करा."}
{"speaker": "Father", "date": "", "dialogue": "काय CPT असं ते कसं करायचं? कोणत्या आवाजाने गाणी म्हणायचं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "CPT साधं, हाताच्या हलक्या थरथरणे देऊन, पोराच्या छाती-पोटाजवळून लाइट पम्पिंग; गाणी किंवा कथा सांगून आरामदायी बनवा."}
{"speaker": "Mother", "date": "", "dialogue": "ठीक आहे, आम्ही रात्री CPT काही खास वेळी सुरू करतो. मुलाला कसं प्रोत्साहन देऊ?"}
{"speaker": "Health Worker", "date": "", "dialogue": "कथा-गाणी, झोपवताना हलका आवाज; CPT नियमित करा, रोज केली जायला पाहिजे."}
{"speaker": "Father", "date": "", "dialogue": "Nutrition भागासाठी काय खाऊ द्यावं? घरगुती उच्च-कॅलरी पदार्थ कोणते?"}
{"speaker": "Health Worker", "date": "", "dialogue": "आहारासाठी उच्च-कॅलरी भारतीय अन्न: गी, संपूर्ण दूध, पनीर, groundnuts आणि गुळ; गरम हवामानात पाणी आणि मीठ अधिक द्या."}
{"speaker": "Mother", "date": "", "dialogue": "घी आणि पनीर मुलासाठी चांगले आहेत, परंतु पोटात वेदना असतील तर अन्नात बदल करायचा?"}
{"speaker": "Health Worker", "date": "", "dialogue": "कधी-कधी पोटातील अडचण असेल तर पाणी कमी- जास्त करावी; आवश्यक असल्यास pancreatic enzymesचा विचार करायचा."}
{"speaker": "Father", "date": "", "dialogue": "Pancreatic enzymes बद्दल आणखी माहिती; डोस कसा ठरवतात, कोणती ब्रँड उपलब्ध आणि कोणत्या लक्षणांवर डॉक्टरांना सांगावं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "Weight-based dosing; भारतीय जनरिक Panlipase, Enzar Forte उपलब्ध; डॉक्टरांच्या निर्देशानुसार देणे सुरक्षित."}
{"speaker": "Mother", "date": "", "dialogue": "धन्यवाद, आम्ही डॉक्टरांचे आदेश पाळू."}
{"speaker": "Health Worker", "date": "", "dialogue": "Infection prevention: हात साबणाने चांगलं धुव्या, nebulizer रोज स्वच्छ करा, उकळलेले पाणी वापरा."}
{"speaker": "Father", "date": "", "dialogue": "Nebulizer वापरत आहोत; ते साफ ठेवायला आम्हाला मार्गदर्शन करा."}
{"speaker": "Health Worker", "date": "", "dialogue": "Nebulizer भागांना रोज साबणाने धुवा, धुण्यानंतर पूर्ण सुखवा; वापरताना स्वच्छ सामग्रीच वापरा."}
{"speaker": "Mother", "date": "", "dialogue": "घरात तापमान कसं ठेवावं, nebulizerसाठी पाणी कसं उकळायचं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "घरात आरामदायक तापमान ठेवा; nebulizerसाठी पाणी उकळलं असावं; प्रत्येक सत्रानंतर स्वच्छ्ता जपा."}
{"speaker": "Patient", "date": "", "dialogue": "आमचं घर दिवस-रात्र पावसाचं मौसम असतं; पर ठरावीक योजना करायला मदत होईल."}
{"speaker": "Health Worker", "date": "", "dialogue": "चार आठवड्यांच्या क्लिनिकल फॉलो-अपची तयारी करा; वजन, hydration, शौचाची स्थिती तपासू."}
{"speaker": "Mother", "date": "", "dialogue": "चार आठवड्यानंतर क्लिनिकला जायचं; diary प्रगती आणि Sweat Testची तयारी दोन्ही करायची."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF awareness शिक्षण परिवाराला द्या; TB मिसअंडरस्टँडिंग टाळण्यासाठी CFची माहिती ठेवा."}
{"speaker": "Father", "date": "", "dialogue": "समजलं. CF बद्दल अधिक माहिती मिळाली तर आम्ही इकडे-तिकडे समुदायात सांगू."}
{"speaker": "Health Worker", "date": "", "dialogue": "Carrier testing एक पर्याय; CF वाहक आढळल्यास genetic counselling उपयुक्त ठरू शकतं."}
{"speaker": "Mother", "date": "", "dialogue": "या संदर्भात माहिती द्या, आम्ही विचार करून निर्णय घेऊ."}
{"speaker": "Health Worker", "date": "", "dialogue": "Carrier testingचा फायदा-जोखमींचा विचार करुन निर्णय घ्या; genetic counsellingची शक्यता पाहू."}
{"speaker": "Patient", "date": "", "dialogue": "पाळणा सकारात्मक राहिला तरीही आम्ही मेहनत करणार; हरकत नाही."}
{"speaker": "Health Worker", "date": "", "dialogue": "महत्त्वाचं भाग: Sweat Test केंद्रांची सूची, पत्ता, वेळा, संपर्क माहिती एकत्र ठेवू."}
{"speaker": "Mother", "date": "", "dialogue": "हो, आम्ही त्या केंद्रांची पत्ता आणि संपर्क मिळवून तयारी करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF diary रोज तीन भागांतले नोंदी लिहा; baseline वजन, आजचा वजन, शौचाची अवस्था."}
{"speaker": "Father", "date": "", "dialogue": "हो, diaryची संरचना आम्ही नीट समजून घेतो; रोज लिहायला सुरुवात करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "Red flags: जास्त ताप, उलटी, ओरल इन्टेक कमी होणे, थोडा lethargy किंवा dehydration असल्यास तत्काळ क्लिनिकला जा."}
{"speaker": "Mother", "date": "", "dialogue": "जर काही अडचण आली तर आम्ही लगेच आपल्याला संपर्क करणार."}
{"speaker": "Health Worker", "date": "", "dialogue": " Sweat Test procedure: pilocarpine पसीना संकलन; काही दिवसांत परिणाम मिळतात; केंद्रांची तयारी करा."}
{"speaker": "Patient", "date": "", "dialogue": "आता आम्ही मार्गदर्शनानुसार तयारी करतो; माझ्या अडचणींवर लक्ष द्या."}
{"speaker": "Health Worker", "date": "", "dialogue": "चार आठवड्यानंतर CF डायरी, वजन, hydration, शौचाचा आढावा घेऊ."}
{"speaker": "Mother", "date": "", "dialogue": "चार आठवड्यानंतर क्लिनिकला जायचं; diary प्रगती आणि Sweat Testची तयारी दोन्ही करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF awareness शिक्षण आणि TB मिसअंडरस्टँडिंग टाळण्यासाठी CFची माहिती देऊन संस्था माहिती देऊ."}
{"speaker": "Father", "date": "", "dialogue": "CF बद्दल अधिक माहिती मिळाली तर आम्ही इकडे समुदायातही सांगू."}
{"speaker": "Health Worker", "date": "", "dialogue": "Carrier testing एक पर्याय; CF वाहक आढळल्यास genetic counselling उपयुक्त ठरू शकतं."}
{"speaker": "Mother", "date": "", "dialogue": "या संदर्भात माहिती द्या, आम्ही विचार करून निर्णय घेऊ."}
{"speaker": "Health Worker", "date": "", "dialogue": "Carrier testingचा फायदा-जोखमींचा विचार करुन निर्णय घ्या; genetic counsellingची शक्यता पाहू."}
{"speaker": "Patient", "date": "", "dialogue": "पाळणा सकारात्मक राहिला तरीही आम्ही मेहनत करणार; हरकत नाही."}
{"speaker": "Health Worker", "date": "", "dialogue": "महत्त्वाचं भाग: Sweat Test केंद्रांची सूची, पत्ता, वेळा, संपर्क माहिती एकत्र ठेवू."}
{"speaker": "Mother", "date": "", "dialogue": "हो, आम्ही त्या केंद्रांची पत्ता आणि संपर्क मिळवून तयारी करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "CF diary रोज तीन भागांतले नोंदी लिहा; baseline वजन, आजचा वजन, शौचाची अवस्था."}
{"speaker": "Father", "date": "", "dialogue": "हो, diaryची संरचना आम्ही नीट समजून घेतो; रोज लिहायला सुरुवात करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "Red flags: जास्त ताप, उलटी, ओरल इन्टेक कमी होणे, थोडा lethargy किंवा dehydration असल्यास तत्काळ क्लिनिकला जा."}
{"speaker": "Mother", "date": "", "dialogue": "जर काही अडकं आली तर आम्ही तात्काळ आपल्याला संपर्क करणार."}
Ground Truth:
Summary of the CF-focused dialogue (key events, symptoms, diagnosis, and treatment steps)

- Presentation and clinical context
  - A 3-month-old male in Mumbai presents with intermittent mild cough since birth, poor weight gain, oily bulky stools, digestive discomfort, and intermittent constipation, raising strong suspicion for cystic fibrosis (CF). Family seeks structured monitoring and evaluation.

- Diagnostic plan and rationale
  - Pilocarpine-induced Sweat Test is identified as the primary diagnostic test for CF and should be arranged at a larger center. If Sweat Test is not locally available, clinicians should document symptoms and data to guide next steps.
  - A CF diary is mandated to accompany the diagnostic process for systematic symptom tracking and outcomes.

- CF diary and data collection
  - Diary comprises three parts: Respiratory (cough timing/context), Diet/Hydration (fluids/ORS/electrolytes), Weight/Stool (weight trend and stool characteristics).
  - Baseline weight to be recorded; weight tracked over 2–4 weeks; diary entries start immediately. A clinical visit is planned after 4 weeks of diary data.

- Immediate and initial management guidance
  - Emphasize increased hydration and electrolyte intake.
  - If Sweat Test isn’t readily available locally, explore government schemes or subsidies to support testing.
  - Educate the family about CF to prevent misdiagnoses (e.g., TB or malnutrition) and avoid delays.

- Follow-up plan and logistics
  - After 4 weeks, conduct a clinical check-up to review weight, hydration, and stool characteristics; Sweat Test preparation and scheduling should proceed in parallel.
  - Prepare a list of Sweat Test centers with addresses, timings, and contact information (examples: CMC Vellore, AIIMS Delhi, PGI Chandigarh).
  - Encourage travel planning to central hospitals while adhering to safety protocols.
  - Consider genetic carrier testing as a parallel option with balanced discussion of benefits and risks.

- Information management and safeguards
  - Maintain updated addresses and contact numbers for key centers; ensure mobile numbers are current.
  - Stay in touch with local health authorities for guidance or assistance.
  - Seek information on government schemes or subsidies to support testing and travel.

- Expected outcomes and milestones
  - Finalize Sweat Test plan with timing and center details; use diary, weight, hydration, and stool data to inform the physician.
  - Schedule a 4-week clinical follow-up to review progress and finalize Sweat Test arrangements.
  - Use CF awareness efforts to educate the family and the local community.

- Immediate actions and ongoing execution
  - Start the CF diary today (record cough timing, weight trend, fluids, stool characteristics).
  - At the 4-week mark, attend the clinical check-up with a detailed report and prepare for Sweat Test scheduling.
  - If Sweat Test centers aren’t local, obtain a list of potential centers and subsidy options in advance.

- Overall plan
  - Central objective: arrange a Sweat Test at an appropriate hospital while meticulously documenting symptoms via a structured diary.
  - Four-week follow-up to assess weight, hydration, and stools to finalize Sweat Test logistics.
  - Parallel actions include travel planning to a major center, subsidy options, and genetic counseling as appropriate.

- Context and practical notes
  - Set in the Indian healthcare context, with awareness of TB misdiagnosis, potential funding options, and active family engagement in education and planning.
  - Sweat Test details: pilocarpine-based sweat collection; results typically available in a few days; subsidies may support testing where local availability is limited.

- Key practical takeaway
  - Initiate the CF diary immediately and arrange Sweat Test at a recognized center within 4 weeks, while navigating subsidies and travel logistics; use collected data to guide subsequent CF care if CF is diagnosed.

- Key treatment steps and supportive measures
  - Hydration and electrolyte management; home-made ORS guidance (water, salt, sugar) with dosing guided by a clinician.
  - Pancreatic enzyme replacement therapy discussed as needed (weight-based dosing; Indian generics like Panlipase, Enzar Forte mentioned).
  - Respiratory care and airway clearance: chest physiotherapy (CPT) about 5–10 minutes twice daily; child-friendly approaches (stories/songs).
  - Nebulizer hygiene: daily cleaning with soap and water, thorough drying, safe storage.
  - Diet considerations: monitor greasy stools; consider reducing easily digestible sugars if abdominal pain or constipation occurs; maintain hydration.
  - Red flags: fever, vomiting, or poor oral intake during monitoring warrant urgent clinic visit.
  - Genetic counseling and carrier testing discussed as future considerations; current focus remains on Sweat Test and diary-driven monitoring.
  - CF-awareness education for the family to reduce fear of misdiagnosis and enable community education.

In short: the plan emphasizes an early, structured CF evaluation via pilocarpine Sweat Test at a central center within four weeks, guided by a detailed CF diary and comprehensive supportive care. Parallel logistics cover travel, potential subsidies, and consideration of genetic counseling.
Qwen-2.5-7B-fewshot:
Clinical Summary:

The patient is a 3-month-old male infant from Mumbai, presenting with chronic cough, poor weight gain, intermittent loose stools, and difficulty in feeding. The parents report that the child has been lethargic, lost weight, and experienced episodes of constipation. They suspect Cystic Fibrosis (CF) and wish to proceed with pilocarpine sweat testing at a major center. They have started maintaining a CF diary.

Key Points:
- Symptoms: Chronic cough, poor weight gain, loose stools, feeding difficulties, intermittent constipation, lethargy.
- Suspected condition: Cystic Fibrosis (CF).
- Proposed investigations: Pilocarpine sweat test, CF diary.
- Management plan: 
  - Maintain a CF diary with respiratory, diet/hydration, and stool details.
  - Monitor weight and hydration status.
  - Perform manual chest physiotherapy (CPT) twice daily for 5-10 minutes.
  - Ensure proper feeding and nutrition, including high-calorie Indian foods like ghee, full-fat milk, paneer, groundnuts, and ghee.
  - Maintain a comfortable room temperature and clean nebulizer equipment.
- Follow-up: 
  - Schedule a clinic visit in 4-8 weeks for sweat test preparation and results.
  - Monitor weight, hydration, and bowel movements.
  - Provide CF awareness education to the family and community.
  - Discuss carrier testing and genetic counseling if CF carrier status is suspected.

Red Flags:
- High fever, vomiting, reduced oral intake, lethargy, or signs of dehydration require immediate clinic visit.

6

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Patient", "date": "", "dialogue": "मी राजेश पटेल, वय 52 वर्ष, मुंबई. chemo-radiation पूर्ण झालंय आणि आता रीकव्हरी फेज चालू आहे. माझ्या आरोग्यासाठी फॉलो-अप आणि आहाराबद्दल मार्गदर्शन हवयं."}
{"speaker": "Health Worker", "date": "", "dialogue": "नमस्कार राजेश, मी डॉ. आहेर. आपण फॉलो-अप, आहार आणि पुनर्वास याबद्दल बोलणार आहोत. तुमचं प्राथमिक माहिती स्पष्टपणे देऊ शकता का?"}
{"speaker": "Patient", "date": "", "dialogue": "हो, माझं नाव राजेश पटेल, वय 52, मुंबई. सध्या थकवा थोडा वाढतोय, swallowing हलका अड़थळा, वजन थोडं कमी झालंय."}
{"speaker": "Health Worker", "date": "", "dialogue": "समजलं. पहिल्या वर्षी त्रैमासिक फॉलो-अप राहतो; प्रत्येक भेटीमध्ये MDT निर्णय घेतात, त्यामुळे तुमच्या शारीरिक तपासणी, लैब तपासणी आणि प्रतिमा एकत्र पाहून पुढचा plan ठरवतो."}
{"speaker": "Patient", "date": "", "dialogue": "ठिक आहे. मला थकवा जास्त अनुभव होतो, अन्न खाण्यात अडचण, आवाजात काही अडचण नाही का ते जाणून घ्यायचं."}
{"speaker": "Health Worker", "date": "", "dialogue": "थकवा कमी करण्यासाठी उर्जेचं आहार, हलका व्यायाम, swallowing-थेरपी आवश्यक. स्पीच थेरपी जरी कमी झाले तरी चालेल; आम्ही home-based exercises देऊ, ज्यांनी गळ्यातल्या स्नायूंना चालना मिळते."}
{"speaker": "Patient", "date": "", "dialogue": "स्पीच थेरपी कधीपासून सुरू करायची? आवाज नीट होण्यासाठी काय कराल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "स्पीच थेरपी लवकर सुरू करतो; swallowing थेरपीही एकत्रितपणे चालतील. आपण घरून केलेले सराव दैनंदिनदर्शकपद्धतीने आम्ही देऊ, ज्याने सुरळीत बोलणे आणि निगडित अन्न चबण्यास मदत होईल."}
{"speaker": "Patient", "date": "", "dialogue": "घरचं सराव कोणते-कोणे, दररोज किती वेळ करायचा, आणि कोणत्या अडचणी आली तर काय करायचं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "घरचं सराव कोणते-कोणे, दररोज 10-15 मिनिटे सराव; गळ्याच्या हलक्या हालचाल, जबड्याच्या हलका-हलका व्यायाम, swallowing-सराव, आणि अडचण आली तर तोडगं ब्रेक घेऊन पुन्हा सुरू करायचं."}
{"speaker": "Patient", "date": "", "dialogue": "फीडिंग ट्यूब बद्दल कधी विचार करायचं? आपलं म्हणणं काय आहे?"}
{"speaker": "Health Worker", "date": "", "dialogue": "फीडिंग ट्यूब दीर्घकाळ oral intake कमी असेल तेव्हा विचारात येते. आधी soft-आहार चालू राखा; MDT निर्णयावरच अंतिम, त्यामुळे आवश्यक असेल तर आम्ही योग्य समयी ट्यूबची शक्यता तपासू."}
{"speaker": "Patient", "date": "", "dialogue": "आहारासाठी काय-काय ठेवलं पाहिजे? soft, high-protein, high-calorie खाणं हवं."}
{"speaker": "Health Worker", "date": "", "dialogue": "खिचडी-डाळ-भात, दही, दूध, अंडी, प्रोटीन शेक. दररोज छोटे अन्न, 2-3 तासांनी; आहारात विविधता, हलक्या अन्नांचा समावेश आणि पाण्याच्या योग्य प्रमाणाची काळजी."}
{"speaker": "Patient", "date": "", "dialogue": "पाणी किती पिणं? वजन वाढीसाठी काही खास नियम?"}
{"speaker": "Health Worker", "date": "", "dialogue": "रोज कमीत कमी 2-3 लिटर पाणी प्या. आहारात प्रोटीन आणि कॅलरी वाढवा; गरज असेल तर प्रोटीन सप्लिमेंट विचारात येईल. आहाराच्या वेळापत्रकाची नियमितता जपू."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "मी राजेशची बायको, आम्ही येथे आलो आहोत, MDT च्या निर्णयात भाग घेऊ. आम्हाला घरात अन्न-आहार, पुनर्वास, किराणा खरेदी, व स्वच्छता कसे व्यवस्थित करायचे, ते स्पष्टपणे समजेल का?"}
{"speaker": "Health Worker", "date": "", "dialogue": "कुटुंबाचं सहकार्य खूप महत्त्वाचं आहे. सकाळी उठल्यापासून रात्री झोपेपर्यंत या प्रक्रियेत आपला सहभाग ठेवू. स्मोकिंग आणि अॅल्कोहोल पूर्णपणे थांबवा; तुमच्यासोबत आम्ही मार्गक्रमण करणार."}
{"speaker": "Patient", "date": "", "dialogue": "हो, मी पूर्णपणे थांबवण्याचा ठाम निर्णय घेतो आणि तुमचं मार्गदर्शन पाळीन. कुटुंबाचं पाठबळ असल्याने मला अधिक विश्वास वाटतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "तर प्रेरणा कायम ठेवण्यासाठी सपोर्ट ग्रुप्स शोधून घेतो, निकोटीन रिप्लेसमेंट थेरपीचं सल्ला घेणं, आणि माझ्या साथित तुमचं म्हणणं पडल्यास आम्ही लगेच संपर्कात राहू."}
{"speaker": "Relative", "date": "", "dialogue": "घरात अन्न-आहारासाठी मार्गदर्शक योजना कशी तयार करायची ते आपणच विचारू. आम्ही नेहमी प्रोटीनयुक्त पदार्थ, नरम अन्न, वेळेवर फळं, आणि पाण्याची सोय देऊ."}
{"speaker": "Patient", "date": "", "dialogue": "जर घरात अडचण आली तर आम्हाला कसे माहिती द्याल? तुम्हाला मदत कधी मिळेल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "Tele-consult उपलब्ध आहे; त्रास वाढल्यास आम्ही तत्काळ संपर्क क्रमांक आणि आपत्कालीन मार्गदर्शन देतो; काही प्रश्न असतील तर फोन करू शकता."}
{"speaker": "Patient", "date": "", "dialogue": "MDT बैठक कधी होते? तीन महिन्यानंतर एकदा येतो का? त्या दिवशी care plan, प्रतिमा आणि लैब पाहून पुढील दिशा कळेल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "MDT बैठक तीन महिन्यानंतर निश्चित; त्याच दिवशी तुम्हाला एक स्पष्ट केअर प्लॅन, पुढील टप्पे, आणि आवश्यक तात्पुरते प्रयोग समजावून दिले जाईल."}
{"speaker": "Relative", "date": "", "dialogue": "आम्ही ऑनलाइन रजिस्ट्रेशनची तयारी केलीय; आपली आयडेंटिटी, विमा-प्रूफ, MDT बैठकीची वेळ देऊन तुमच्यावर लक्ष ठेवू."}
{"speaker": "Health Worker", "date": "", "dialogue": "ऑनलाइन रजिस्ट्रेशन, आयडेंटिटी डॉक्युमेंट, विमा-प्रूफ, MDT भेटीची वेळ—हे सगळं घरातून व्यवस्थित करा; गरज पडल्यास आम्ही मदत करू."}
{"speaker": "Patient", "date": "", "dialogue": "घरात अन्न-आहारासाठी काही खास पदार्थांची नावं देता येतील का, ज्यामुळे प्रोटीन-युक्त आणि नरम अन्न सहज मिळेल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "उच्च प्रोटीन शेक्स, दूध, दही, पनीर, अंडी, स्प्राउट्स, नरम फळं, आणि पाण्याच्या योग्य प्रमाणाची काळजी. आहारात विविधता ठेवा."}
{"speaker": "Patient", "date": "", "dialogue": "आवाजाच्या अडचणी काय कधीपर्यंत सुधारणार?"}
{"speaker": "Health Worker", "date": "", "dialogue": "स्पीच थेरपी लवकर सुरू केल्यास काही आठवड्यातच सुधार दिसतो; swallowing-थेरपीही घरगुती सरावांसह सुरू राहील."}
{"speaker": "Relative", "date": "", "dialogue": "आम्ही एक सोपी घरगुती चेकलिस्ट तयार करतोय; swallowing-खाण्याच्या अडचणींचा दिवसागणिक रेकॉर्ड ठेवला जाईल, ज्याने progress कळणार."}
{"speaker": "Health Worker", "date": "", "dialogue": "स्वल्प-चेकलिस्ट घरगुती थेरपीमध्ये मदत करेल; अन्नाच्या गळण्याच्या अडचणींचे नोंद ठेवा."}
{"speaker": "Patient", "date": "", "dialogue": "वजन वाढीसाठी आहाराचा नेट-फ्लो कसा ठेवायचा, कोणत्या आहाराच्या वेळेस प्रोटीनचे प्रमाण कसे टिकवायचे?"}
{"speaker": "Health Worker", "date": "", "dialogue": "आहारात प्रोटीन-युक्त पदार्थांना स्थिर ठेवून वजन टिकवू. दररोज प्रोटीनयुक्त आहार, संतुलित आहार, आणि कॅलरी व्यवस्थापन ठेवा."}
{"speaker": "Patient", "date": "", "dialogue": "फक्त पोषण पुरेसे नाही; हलका व्यायाम, आराम, चांगली झोप यांचीही काळजी घ्या. वजन वाढवण्यासाठी आणखी काय करता येईल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "हलका व्यायाम, चहा-कॉफीचे प्रमाण मर्यादित ठेवा; औषधांची वेळेवर मात्रा घेणे, डॉक्टरांच्या सल्ल्यानुसार पालन करणे महत्त्वाचे."}
{"speaker": "Relative", "date": "", "dialogue": "आम्ही योग-व्यायाम आणि हलकी चालण्याचा कार्यक्रम तयार करतो; श्वासोच्छ्वास सुधारणे, स्नायूंना मजबूती देणे, आणि शरीरातील लचीलापन वाढवणे हा हेतू."}
{"speaker": "Patient", "date": "", "dialogue": "गळ्यावर swallowing-issues आल्यास घरात काय उपाय करायचे? जसं थोडे पाणी पाजणे, पातळ अन्न, वेळेवर विश्रांती."}
{"speaker": "Health Worker", "date": "", "dialogue": "घरातून सराव दैनंदिन; गळ्याच्या हलचालासाठी छोटे-छोटे व्यायाम, swallowing-सराव, आणि अन्नाचे पातळ टेक्स्चर वापरणे या सर्वांची संयुक्त रचना."}
{"speaker": "Patient", "date": "", "dialogue": "ड्राय माऊथची समस्या असल्यास काय उपाय कराल? mouth moisturizers व गाळण्या आणि आवश्यक असल्यास सल्विया-स्वल्प्स?"}
{"speaker": "Health Worker", "date": "", "dialogue": "mouth-moisturizers, गाळण्या, पाण्याच्या योग्य हायड्रेशनची काळजी. डॉक्टरांच्या सल्ल्यानुसार सल्विया-स्वल्प देऊ."}
{"speaker": "Relative", "date": "", "dialogue": "आम्ही कुटुंबाला माहिती देतो; तेवढी तयारी करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "सरकारी योजना, रेशनिंग, वैयक्तिक सहाय्य पुढील भेटीत स्पष्ट करतो; सर्व कागदपत्रे तयार ठेवा."}
{"speaker": "Patient", "date": "", "dialogue": "धन्यवाद. या मार्गदर्शकाने मला आत्मविश्वास देतंय."}
{"speaker": "Health Worker", "date": "", "dialogue": "आत्मविश्वास वाढवण्यासाठी मानसिक सपोर्ट ठेवा; आणि निकोटिन रिप्लेसमेंट थेरपी नियमितपणे चालू ठेवा."}
{"speaker": "Relative", "date": "", "dialogue": "आम्ही घरात एक छोटा रूटीन तयार करतो; एखादी अडचण आल्यास लगेच कळेल."}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, पुढील भेटीची तयारी करा; MDT तीन महिन्यानंतर होईल; रिपोर्ट्स ऑनलाइन दिसतील."}
{"speaker": "Patient", "date": "", "dialogue": "तीन महिन्यानंतर MDT होईल का? रिपोर्ट ऑनलाइन दिसतील; ते बरोबर?"}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, MDT तीन महिन्यानंतर होईल; परिणाम ऑनलाइन उपलब्ध असतील आणि तुम्हाला care plan स्पष्टपणे समजेल."}
{"speaker": "Relative", "date": "", "dialogue": "तयार आहोत. आवश्यक असल्यास आम्ही प्रवासात मदत करतो."}
{"speaker": "Patient", "date": "", "dialogue": "त्यादिवशी care plan स्पष्टपणे समजेल असा विश्वास."}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, त्या दिवशी एक स्पष्ट केअर प्लॅन देईन; पुढील टप्पे स्पष्टपणे समजावून सांगू."}
{"speaker": "Patient", "date": "", "dialogue": "कृपया काही प्रश्न असतील तेव्हा सांगू; आम्ही त्यांच्या उत्तरांची तयारी करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "काही प्रश्न असतील तर कॉल करा; tele-consult उपलब्ध आहे, आणि ऑनलाइन रिपोर्ट्सची सुविधा आहे."}
{"speaker": "Patient", "date": "", "dialogue": "हो, निश्चितपणे. धन्यवाद."}
{"speaker": "Relative", "date": "", "dialogue": "धन्यवाद डॉक्टरांना."}
{"speaker": "Health Worker", "date": "", "dialogue": "तुमचं फॉलो-अप दीर्घकालीन आरोग्यासाठी अत्यंत आवश्यक आहे; नियमित तपासण्या तुमचं संरक्षण करतील."}
{"speaker": "Patient", "date": "", "dialogue": "हो, ही सुरुवातच आहे; पुढे काय करायचं ते स्पष्टपणे सांगितलं तर उत्तम."}
{"speaker": "Health Worker", "date": "", "dialogue": "पुढील भेटीची तयारी करा; MDT तीन महिन्यानंतर होईल; রিপোর্ট्स ऑनलाइन उपलब्ध असतील."}
{"speaker": "Relative", "date": "", "dialogue": "आम्ही तयार आहोत; आवश्यक असल्यास आम्ही प्रवासात मदत करतो."}
{"speaker": "Patient", "date": "", "dialogue": "चला, तीन महिन्यात पुन्हा भेटू."}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, आपण तीन महिन्यात पुन्हा भेटू; त्या दिवशी care plan आणि पुढील टप्पे स्पष्टपणे समजतील."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "धन्यवाद डॉक्टरांना, आम्ही तयार आहोत."}
Ground Truth:
Summary of Post-Treatment Head and Neck Cancer Dialogue (Rajesh Patel, 52, Mumbai)

- Status and goals
  - Rajesh has completed chemo-radiation and is in the recovery phase.
  - Primary goals: prevent recurrence, monitor post-treatment symptoms, optimize nutrition and quality of life.
  - Follow-up planned as regular tri-monthly visits in the first year, guided by a multidisciplinary team (MDT).

- Symptoms and rehabilitation
  - Current issues: fatigue, reduced throat mobility affecting swallowing, and slight weight loss.
  - Rehabilitation focus: stabilize weight, improve swallowing function, enhance voice clarity, and boost energy.
  - Home-based rehab: swallowing and speech therapy started early; daily exercises 10–15 minutes, targeting throat muscles, jaw movements, and swallowing patterns.

- Diagnostics and monitoring
  - Investigations: periodic labs (CBC, CMP) and imaging (CT/MRI) planned; MDT reviews will guide next steps.
  - Access to care: tele-consult options and online result reporting to reduce travel.
  - Baseline tests and imaging results will inform MDT staging and decisions.

- Nutrition and weight management
  - Diet plan: soft, high-protein, high-calorie foods (e.g., kichdi-dal-rice, dairy, protein shakes); emphasis on hydration.
  - Professional support: referral to a dietitian; supplements considered if needed.
  - Feeding tube: discussed as an option if long-term inadequate oral intake occurs; initial approach prioritizes soft foods with gradual progression.
  - Hydration and intake goals: at least 2–3 liters of water daily; regular meals with protein and calories; adherence to a structured eating schedule.

- Swallowing, voice, and rehabilitation
  - Rehabilitation: swallowing therapy and speech therapy recommended to improve swallowing and speech.
  - Progress tracking: simple home program and checklists to monitor daily practice and swallowing comfort; early rehab emphasized to maximize recovery of throat muscles and articulation.

- Dental and oral care
  - Post-radiation dental care is critical; plan includes a dental check-up about three months after radiation and ongoing oral hygiene.

- Therapeutic and supportive services
  - Additional therapies: swallowing therapy, physical therapy, and speech therapy as needed; structured progressive exercise plan provided.
  - Psychosocial support: family involvement and social-work/insurance guidance offered; assistance with trial access discussed.

- Smoking, alcohol, and behavioral health
  - Strongly recommended cessation of smoking and alcohol; cessation support groups and counseling available.
  - Support for motivation and mental well-being emphasized; tele-consults and online resources are available.

- Trials and financial considerations
  - Evaluation for clinical trial eligibility; discussion of costs and logistics.
  - Government schemes (e.g., Ayushman Bharat) and local funding options discussed; detailed guidance to follow at next visit.

- Family involvement and logistics
  - Family support encouraged; spouse participation in MDT discussions valued.
  - Documentation, online registrations, and travel planning support provided; tele-consult options available.
  - Home-based care and caregiver involvement emphasized.

- Follow-up schedule and next steps
  - First-year follow-up every three months; assessments to include weight, swallowing, voice, diet, and dental status.
  - Baseline tests and imaging/biopsy results inform MDT staging and decisions.
  - After MDT reviews, a plain-language care plan will be shared; concrete follow-up timetable and logistics arranged.
  - Nutrition, cessation support, psychosocial services, and trial opportunities to be integrated into ongoing care.

Core message
- Rajesh’s post-treatment care will be guided by objective recovery markers—nutrition, swallowing/voice function, and dental health—with imaging and potential trial eligibility informing MDT-driven decisions about further treatment or surveillance. A comprehensive, family-informed plan will be communicated in plain language, with integrated support across nutrition, rehabilitation, psychosocial services, and access to government schemes or trials.
Qwen-2.5-7B-fewshot:
Clinical Summary:
Rajesh Patel, 52, from Mumbai, is in the recovery phase post-chemoradiotherapy. He reports fatigue, difficulty swallowing, and slight weight loss. Follow-up, nutrition, and home care are discussed.

- **Symptoms and Current Status**: 
  - Fatigue, difficulty swallowing, slight weight loss.
  - Completed a year of follow-up with quarterly visits.
  - MDT (Multidisciplinary Team) meetings review clinical, lab, and imaging findings to plan further care.

- **Management Plan**:
  - Continue home-based exercises for speech therapy and swallowing therapy.
  - Daily routine including light exercise, hydration, and balanced diet.
  - Maintain a consistent meal schedule with high-protein, high-calorie foods.
  - Drink at least 2-3 liters of water daily to aid weight gain.
  - Use feeding tubes if oral intake is insufficient.
  - Support group resources and nicotine replacement therapy for smoking cessation.
  - Tele-consultations for immediate support during emergencies.
  - MDT meeting every three months to review reports and plan further care.

- **Nutrition and Care Tips**:
  - Soft, high-protein, high-calorie foods like soups, milk, yogurt, eggs, nuts, fruits, and fluids.
  - Maintain a balanced diet with small, frequent meals.
  - Checklists for home care to monitor swallowing issues and progress.
  - Light exercises and activities to maintain physical strength and reduce stress.
  - Strategies for managing dry mouth and swallowing issues at home.
  - Regular follow-ups to ensure adherence to care plans and address any issues promptly.

- **Follow-Up and Support**:
  - Scheduled follow-up every three months for review of reports and care plan adjustments.
  - Online registration and documentation for home care.
  - Government schemes and rationing programs explained for further support.
  - Encouragement to maintain a routine and seek support groups for mental well-being.
  - Tele-consultations and online report access for ongoing support.

- **Conclusion**:
  - Rajesh is advised to continue his home care routine and follow-up appointments.
  - Regular check-ins and support from family members are emphasized.
  - Tele-consultations and online resources are available for ongoing support.
  - Rajesh is encouraged to maintain a positive outlook and adhere to the care plan.

7

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "आज आपला मुलगा Ajay चार महिनेाचा आहे. जन्मापासून खोकला, वजन कमी होणं, आणि तेलकट मल दिसतोय. ग्रामीण भागात राहत आहात, CFची शक्यता तपासूया."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो डॉक्टर, Ajay चार महिनेाचा आहे. वजन काही आठवड्यांपासून थांबलंय, ताप नाही. जन्मानंतर खोकला सुरू झाला होता, आता तरी काहीसा कमी- जास्त असतो."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "ठीक आहे. खोकला दिवसातून कसा असतो? रात्रभर जास्त अडचण होते का? मलामध्ये तेलकटपणा कधी दिसतोय?"}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "खोकला सध्या थोडा कमी-जास्त असतो; रात्री अडचण फार नाही. तेलकट मल गेल्या आठवड्याभरापासून दिसतोय."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "CFची शक्यता असून Sweat Test ही निदानाची निर्णायक चाचणी आहे. शहरातील CF सेंटरमध्ये शक्यतो करायचं."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "Sweat Test कागदपत्रांसोबत किती खर्च येतो? प्रवासाचं खर्च कसं जमतं?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "प्रवास व राखीणी सवलती CF टीमकडे बघतात. Subsidy मिळू शकतो; कागदपत्रं साहित्यिकपणे असावं."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "ठीक. गावाकडून शहरात येताना आम्ही तयार आहोत. Sweat Test कुठे करायचं ठरवायचं?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Sweat Test सामान्यतः शहरातील CF Center किंवा शिकवण्या हॉस्पिटलमध्ये होतो. baseline तपासणी करण्यासाठी वजन, उंची, ऑक्सिजन, ताप तपासावं."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "आम्ही प्रवासासाठी अडचण जाणवत असल्यामुळे Subsidyची कृपया मार्गदर्शन करा."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "CF टीम Aadhaar, राशन कार्ड, गावाचा पत्ता, मोबाईल नंबर आणि वैद्यकीय इतिहास माहिती घेईल. प्रवासाची तयारी करुया."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "ठीक. आम्ही ते सर्व देऊ. Sweat Testची तारीख कधी देणार?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Sweat Testची तारीख CF Centerकडून पुढच्या भेटीत ठरवली जाते. Baseline तपासणी पोस्ट करायची."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "आता काही कागदपत्रं आणायची आहेत का?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Aadhaar, राशन कार्ड, गावाचा पत्ता, मोबाईल नंबर, वैद्यकीय इतिहास आणि कुटुंबिक आरोग्य माहिती आवश्यक आहेत."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "ठीक. आम्ही ते देऊ, Sweat Testची तयारी सुरू ठेवू."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "घरात diary ठेवा: वजन, उंची, आहार, खोकला, मलाचा रंग/घनता. दर 2-3 आठवड्यात अपडेट करावे."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो, आम्ही ते चालू ठेवू. आहारात बदल काय करावे?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "हाय-कॅलोरी आहार सुरू ठेवा. पाणी जास्त प्या. पॅन्क्रियास एंजाइम डॉक्टर ठरवतील, जरा जवळच्या तुलन्यास."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "एंजायमची डोस कशी ठरवतात? जनरिक चालतील का?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "जगातील पद्धतीप्रमाणे, जेवणानंतर 15-30 मिनिटांनी देण्यास म्हंटलं जातं. स्टूल फॅट व वाढ पाहून डोस समायोजित होईल."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "जर तेलकट मल दिसलं नाही, तरी काय करायचं?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "तेलकट मल दिसल्यास stool fat studies महत्त्वाचे; त्यानुसार आहार आणि एंजाइम समायोजित करतात."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "CPT काय असते? ते घरातून कसे करायचे?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "CPT Chest physiotherapy आहे. दिव Eaton दोनदा करणे सोपे; गाणी/कथा बोलून मुलाला सांगा. उपकरणांची स्वच्छता ठेवा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "घरी CPT करण्यासाठी काही खास वेळ असतो का?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "कुटुंबासोबत करण्यास सोपे असे ठरवा; दररोजच करा, मुलाला आरामदायक वाटेल."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "फॉलो-अप किती दिवसांनी करायचा?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Baseline तपासणीनंतर सामान्यतः दोन आठवडे फॉलो-अप. Sweat Testची तारीख CF Center ठरवेल."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "गावहून शहरात येताना खर्च वाढतो. subsidy कसा मिळतो?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "CF टीम subsidy प्रक्रिया चालवते. lodging व प्रवासासाठी मार्गदर्शन देईल."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "ठीक. Ajay च्याHydration कसं राखायचं?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "पाणी व इलेक्ट्रोलाइट्सची काळजी घ्या. गरजेप्रमाणे लायट सोडा देऊ."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "गावात पाणी स्वच्छ असेल तर? तुमचं मार्गदर्शन महत्त्वाचं."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "होय, स्वच्छ पाणी खूप महत्त्वाचं. आहारात विविध अन्नाचा समावेश ठेवा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "प्रवासाचा विचार करतोय; कोणत्या काळात कुठे राहायचं?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "CF टीमसोबत प्रवास-योजना बनवा. प्रवासात काही अडचण आली तर फोन/व्हॉट्सअॅपवर संपर्क ठेवा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "तुमचा मदतकारक कोण असेल तर?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "CF Center मध्ये तुम्हाला Lodging वगैरेची माहिती दिली जाईल; प्रत्येक कागदपत्राची पूर्तता करावी."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "Sweat Testची निकाल कधी येईल?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "निकाल काही दिवसांत CF Center कडून कळवण्यात येईल. सकारात्मक आल्यास CF-उपचार सुरु होईल."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "नकारात्मक आल्यास इतर कारणे तपासायची आहेत काय?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "होय, CF नसल्यास अन्य पाचन-श्वसन कारणे तपासली जातील."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "तुम्हाला आणखी काही स्पष्टीकरणायोग्य घटक देऊ का?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "होय, Sweat Testची तारीख ठरवून पुढील योजना ठरवू. डॉक्टर्स तुम्हाला सर्व बाबी समजावतील."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "धन्यवाद, आम्ही तयारीत आहोत."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "डायरी अपडेट ठेवणे गरजेचे. वजन, आहार, खोकला, मलाचा रंग कोणतीही परिवर्तन त्वरित कळवा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो, दर 2-3 आठवड्यांत अपडेट करू."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Sweat Testची तारीख ज्याक्षणी CF Center डॉक करेल, त्यानुसार तयारी सुरू करा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "आम्ही सर्व तयारी करतो. धन्यवाद."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "चला तर ठीक, Sweat Test व baseline तपासणींसाठी पुढचं नियोजन करुया."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो, आम्ही तुम्हाला पुन्हा विचारू."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "तुमचे स्वागत. अजून काही त्रास असेल तर कळवा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "खूप धन्यवाद, डॉक्टर."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Sweat Testची तारीख लवकरच निश्चित करतो. कृपया आवश्यक कागदपत्रे तयार ठेवा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "ठीक. आम्ही प्रकरण पुढे नेऊ."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "ठीक. Aarogya राखा; पुढील भेटीची वेळ देतो."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "येत्या भेटीमध्ये baseline data नुसार अतिरिक्त चाचण्या ठरू शकतात."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "आम्ही तयार आहोत. धन्यवाद."}
Ground Truth:
Summary of the Ajay CF-focused dialogue (key symptoms, diagnosis, and treatment steps)

- Presenting symptoms and initial suspicion
  - Ajay, about 4 months old, has had a persistent cough since birth, weight loss, and oily stools; no fever and stable respiratory status.
  - Rural setting raises suspicion for cystic fibrosis (CF); meconium ileus discussed as a possibility.
  - Emphasis on genetic counseling and reviewing family history.

- Diagnostic plan and baseline evaluation
  - Sweat Test identified as the decisive diagnostic test for CF.
  - Baseline checks planned: weight, height, oxygen saturation, temperature, and physical examination.
  - Additional tests considered if needed: chest imaging; stool studies are important, with stool fat studies stressed to guide management.
  - If Sweat Test is negative: CF is less likely, but other etiologies will be explored.
  - If Sweat Test is positive: initiate CF-directed therapies, nutrition, respiratory care, and genetic counseling.
  - General emphasis on hydration, catch-up vaccinations, and infection prevention.

- Logistics, funding, and access
  - Sweat Test available at city centers and major teaching hospitals.
  - Subsidies/travel grants require documentation: Aadhaar, ration card, village address, mobile number, and medical history.
  - Lodging and travel assistance coordinated with the CF team; documentation and guidance provided by the CF team.

- Home management and diary tracking
  - Families advised to maintain a diary of weight/height, diet, cough, and stool color/consistency; update every 2–3 weeks.
  - Focus on adequate fluids and a balanced diet; CF is non-infectious but hygiene and hand-washing remain important.
  - Catch-up vaccinations reviewed as part of the CF plan to protect household members.

- Interim management and treatment planning
  - Nutritional emphasis: high-calorie diet; sodium intake may be adjusted as needed.
  - Pancreatic enzyme dosing to be determined by the physician; affordable generics acceptable if branded options are expensive.
  - Enzyme dosing typically after meals; common guidance is 15–30 minutes post-meal; adjust based on stool fat and growth.
  - If oily/fatty stools persist, stool fat studies become important to guide dietary and enzyme adjustments.
  - Chest physiotherapy (CPT) recommended twice daily; make CPT kid-friendly with songs or stories.
  - Document stool characteristics to guide management.
  - Nebulizer hygiene guidelines discussed (boiled/sterilized water, regular cleaning).

- Follow-up schedule and next steps
  - After baseline testing, follow-up planned within about two weeks to finalize decisions.
  - Sweat Test scheduling discussed: negative result lowers CF likelihood but doesn’t rule out other causes; positive result directs CF-directed therapies.
  - 2025–2026 horizon includes genetic counseling, subsidy processing, travel planning, and integrated care: nutrition program, respiratory care, infection prevention, and vaccination scheduling.
  - Enzyme dosing/timing to be finalized with physician; ensure 15–30 minutes post-meal administration when starting.
  - Plan to add extra salt in hot weather; hydration and electrolytes guided by the CF team.

- Documentation and entries
  - Subsidy paperwork to be prepared; Sweat Test date to be set by the CF center.
  - Diaries and dietary/health plans to be shared with the CF team; travel and lodging arrangements to be supported by the CF team.
  - Maintain copies of diary and health plans for visits.

- Overall outlook
  - Ajay’s chronic cough, weight loss, and oily stools strongly raise suspicion for CF; Sweat Test is the key diagnostic step.
  - Care involves a multidisciplinary CF team, with genetic counseling, travel subsidies, and an integrated plan covering nutrition, respiratory care, infection prevention, vaccination, and home monitoring.
  - Family engagement emphasized: maintain diaries and prepare for a potential two-week follow-up after initial investigations.
  - If Sweat Test is positive, proceed with CF-directed therapies and a structured, team-based care plan.

- Notable timeline highlights
  - 2025-09 to 2025-10: Presentation, CF suspicion, planning for Sweat Test, baseline checks, and subsidy/travel logistics; home diary setup.
  - 2025-11: Interim follow-ups on weight, stool-fat considerations, CPT training, subsidy/travel planning, and preparation for genetic counseling.
  - 2025-12: Focus on baseline data, stool-fat re-evaluation, nutritional updates (higher calories, salt), ongoing CPT training, and finalizing Sweat Test scheduling and CF treatment planning; follow-ups emphasize hydration, diary updates, and infection prevention. Sweat Test date to be confirmed with CF center.

Timeline context
- The dialogue outlines a systematic CF work-up starting with presenting symptoms, proceeding to Sweat Test-driven decisions, and integrating nutrition, respiratory care, and genetic counseling, with substantial attention to logistics, family engagement, and follow-up planning.
Qwen-2.5-7B-fewshot:
Clinical Summary:
Ajay, a 4-month-old male, presents with symptoms of cough, weight loss, and excessive sweating since birth. He has been living in a rural area. The patient's mother reports that he started coughing shortly after birth and the condition has fluctuated. The child currently shows some improvement but still experiences night-time coughing and intermittent sweating. The mother suspects cystic fibrosis (CF). 

The doctor confirms that the child is 4 months old and has had a cough for several weeks, with a recent weight loss. The mother notes that the child has more cough at night and intermittent sweating. A sweat chloride test (Sweat Test) is suggested as a definitive diagnostic test for CF, which can be performed at a city CF center. The estimated cost of the test and travel expenses are discussed. The family is advised to apply for subsidies and gather necessary documents such as Aadhaar, ration card, village address, mobile number, and medical history.

The doctor outlines the following steps:
1. Schedule the Sweat Test at the CF center.
2. Prepare all necessary documents.
3. Keep a daily diary of weight, height, diet, cough, and stool characteristics every 2-3 weeks.
4. Increase calorie intake and hydration.
5. Administer pancreatic enzymes as prescribed by the doctor.
6. Start chest physiotherapy (CPT) twice a day using techniques like reading aloud to the child.
7. Maintain hygiene during home CPT sessions.
8. Plan for travel and accommodation for hospital visits.
9. Follow up in 2-3 weeks after baseline tests.
10. Contact the CF team if any issues arise during travel.

The doctor advises on maintaining hydration, including drinking water and electrolytes, and ensuring clean water supply. A balanced diet is recommended, and the family considers travel plans. The CF team will assist with travel arrangements and provide necessary information.

If the Sweat Test is positive, CF treatment will be initiated. Negative results will prompt further investigation for other causes of malnutrition and respiratory issues. The doctor provides additional clarification on factors affecting hydration and suggests regular updates on the child's condition.

The mother thanks the doctor and schedules the Sweat Test and baseline tests. She promises to keep the doctor updated on the child's progress. The doctor assures that they are prepared and ready to proceed with the next steps.

8

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "तुमचा मुलगा तीन महिन्यांचा आहे. जन्मापासून हलका खोकला येतोय, वजन वाढ ठराविक वेगाने होत नाही आणि अत्यंत तेलकट, मोठे stevige ढेकरासारखे पाणी बाहेर न पडणारे श्वासन स्राव दिसत आहेत; काही दिवस शौच होत नाहीत."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो डॉक्टर, आम्ही बाळाचं वजन पाहून चिंता झालीये. भूक चांगली असते, कोणी वेळेस अडकत नाही, पण वजन थांबलेलं किंवा कमी झालेले दिसते."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "तुमचा मुलग्याचा डेटा एकत्र करायचा आहे.  आणखी एक Anaerobic quick ques: कधी खोकला जास्त थंड हवामानात किंवा रात्री वगैरे वाढतो का?"}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "खोकला आतापर्यंत सतत नाही, पण काही वेळा सकाळी जास्त वाटतो, दिवसात फरक दिसतो."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "आम्ही एक CF डायरी सुरू करणार आहोत. Respiratory, Diet/Hydration, Weight/Stool हा तीन भागात दिवसाला 1-2 पानांचे नोंद करायचे."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "डायरी सुरु करायला ठरवलंय, पण आम्ही काही प्रश्नांची भीति आहे. शॉर्ट-फॉर्म सांगाल का कसे भरणे?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "भरपूर माहिती द्यावी लगेचच नाही. आपण सुरुवात थोडी मुलाखतीने कराल; नंतर diary नीट समजावून देईन."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "बरं, तरीही आम्हाला Sweat Test कधी आणि कुठे करायचं ते ठरवायचंय."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Sweat Test हा CF ची महत्त्वाची चाचणी आहे. स्थानिक हॉस्पिटलमध्ये उपलब्ध नसेल तर आम्ही डेटा गोळा करून लायनिंग डॉक्टरांना पाठवू शकतो."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "आम्हाला थेट केंद्र उघडायचं आहे. कुठे जाऊ शकतो?"}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "उच्चस्तरीय केंद्रांमध्ये CMC Vellore, AIIMS, PGI Chandigarh यांचा विचार केला जावा. ४ आठवड्यात क्लिनिकल फोलो-अप ठेवतो."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "चार आठवड्यात फॉलो-अप? आता तिथे जाऊन येणं कठीण असतं, प्रवास खर्चाचा प्रश्न आहे."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "त्यासाठी सरकारच्या योजना किंवा सबसिडी तपासून देऊ. डायरीने आम्ही स्थितीची माहिती ठेवू; Sweat Test च्या तयारीत मार्गदर्शन देईन."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो, आम्ही योजना वगैरे तपासू. डोंगरी तालुक्यात राहत आहोत, प्रवासासाठी मदत मिळावी."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "DIARYचा पहिला दोन-तीन पान भरून देतो. Respiratory भागात खोकल्याच्या वेळा, कशा परिस्थिती, ताप-श्वास हा भाग."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "ठीक आहे. आत्तापर्यंत शौचाचा वर्णन काढायचा तर तेलकट पांढरे पडेले दिसतात."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Diet/Hydration विभागात दैनंदिन fluids, ORS, पाणी- electrolytes कसे देणार आहात ते लिहाल."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "आम्ही ORS देतो; दिवसात तीन वेळा 100-120 ml प्रमाणात."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "Weight/Stool भागात वजनाचे ट्रेंड, stool रंग-घनता, बदाम पित्ताचा प्रकार लिहा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "जास्तीचं वजन काही दिवसांपूर्वी 4.0 kg होता, आता 3.9-4.0 kg च्या आसपास आहे; stools तेलकट आणि मोठे दिसतात."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "तुम्ही शौचाच्या दिवशी रविवार-रात्रची गडबड पाहिलीत तर म्हणालात की वेळ-वेळ ठरवायची."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो, आम्ही शौच केव्हा येते ते लक्षात ठेवू."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "वर्षातील कुटुंबाला CF बद्दल जागरूक करायचं. CF awareness, TB misdiagnosis याबद्दल माहिती देईल."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो, TB विचार केला जातो आजी-आजोबांनीही सांगितलं. CF बद्दल शंका होती."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "किशोरांच्या बाबतीतदेखील genetic carrier testing विचारात घ्या. फायदे-जोखिम स्पष्ट करेन."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "carrier testing चांगलं असेल तर कशाप्रकारे फायदे होतात ते समजावून सांगा."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "गणित काय? CF मध्ये पेरणाऱ्यांना भविष्यातील निर्णय घेण्यासाठी माहिती मिळते; जोडे-जोड़े परिवारांना तयारी करायची."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "ठीक आहे, आम्ही विचार करूं."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "पहिलाDiary इनपुट मिळाल्यानंतर, दुसर्‍या आठवड्यात वजनाचे वजन तपासणार आहोत. तुम्ही diary कसे भरताय ते सांगाल."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "शेवटचा दिवस वजन 5400 g होता. आज पुन्हा वजन मोजणार. डायरी पहिल्या दिवशी 1 full day भरलं."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "आजचा दिवसभराचा data फोटो किंवा अचूक चित्रण देऊ शकता का? श्वास-खोकला वेळा."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "आज दिवसभरात खोकला तुलनेने कमी झाला होता; परंतु अर्ध्या दिवशी थोडा खोकला होता."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "Density/weight बदलावर लक्ष ठेवा. ORS किती देत आहात? कॅलोरीने भरपूर पाणी देताना."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "ORS तीन वेळा 100-120 ml दिले; दूध- फार काळजी घेतो."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "Stool मध्ये तेलकटपणा आहेच; रंग कसा, गंध कसा, पातळ-पाणी असेल तर लिहा."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "स्टूल पातळच, रंग पिवळसर; पर küm दुखत नाही."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "Sweat Test केंद्रासाठी तयार राहा. 4 आठवड्यांचं फॉलो-अप ठरलं. केंद्राची सूची तुम्हाला दिली जाईल."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "केंद्रांची सूची मिळाली तर आम्ही देखील प्रवास योजना करु."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "government schemes, subsidies, मार्गदर्शक माहिती देतो. travel safety ने COVID protocol चा विचार करायचा."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "COVID guidelines पाळू; रात्रीचे प्रवास सुरक्षित असेल ते बघू."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "चार आठवड्यात क्लिनिकल फॉलो-अप, वजन-हायड्रेशन-स्टूल फीचर्स पाहणे, Sweat Test तयारी चालू ठेवणे."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "समजा Sweat Test कधी करायचं ते ठरलं तर आम्ही त्यादिवशीच तयारी करणार."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "Four-week milestone. वजन स्थिर किंवा थोडं कमी. Hydration वाढली आहे का, स्टूल कसा आहे?"}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "वजन थोडं स्थिर, hydration जास्त झाली, स्टूल तेलकटपणा काहीसे कमी पण नाही."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "कुठे जायचंय? CMC Vellore (VC) किंवा AIIMS Delhi? आपलं प्राधान्य?"}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "आम्हाला Vellore जास्त पसंत. तेथील sweat test लवकर होईल का माहिती दे."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "CMC Vellore मध्ये Sweat Testची योजना सुरू करणार. प्रवासासाठी subsidy व घेण्याचा प्रयत्न कराल."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "चला, आम्ही पुढील तयारी करतो. डॉक्टर, Genetic counseling ची चर्चा पक्का करायची."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "हो, genetic counseling फायदेशीर ठरू शकते. तिच्या फायदा-जोखीम स्पष्ट करतो."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "तयार राहू; आता Sweat Test बुक करायचं आहे. केंद्राचा पत्ता कसा मिळवायचा?"}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "CMC Vellore चा पत्ता, timings आणि संपर्क क्रमांक देतो; बुकिंगसाठी आवश्यक माहिती देईन."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "ठीक आहे. safety protocol चा अहवाल देखील आवश्यक आहे."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "हो, COVID नियमांची प्रतिमा; प्रवासात मास्क, सानुकूल बरोबर चालेल."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "लास्ट महिन्याच्या तुलनेत आज आराम वाटतंय; परंतु लहान मुलगा अडकलेल्या आव्हानांवर विचार करतो."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "CF लक्षात घेऊन गटिंग: 4-वहाळी फॉलो-अप, diary data for physician review."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "हो, diary डेटा डॉक्टरांकडे पाठवू."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "Sweat Test लॉजिक व बुकिंग: family going to CMC Vellore; plan to travel with safety guidelines."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "आता तयारी चालू. subsidies मिळाल्या तर travel सुलभ होईल."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "Diary अपडेट चालू: Respiratory पक्षात खोकलाचे विशिष्ट वेळा, Diet/Hydration मध्ये ORS प्रमाण, Weight/Stool मध्ये वजन गोळा."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "डायरी updated मुलांच्या दैनंदिन हालचालीप्रमाणे भरत आहात."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "Genetic counseling पर्याय चर्चा झाली; लाभ-जोखीम स्पष्ट करतो."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "हो, genetic counseling बद्दल अधिक माहिती हवी."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "पारंपारिक CF awareness, TB misdiagnosis याबद्दल माहिती देत राही. CF असल्यास लवकर ओळख केलं तर मुलाच्या फुफ्फूस मजबूत राहतात."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "समजलं. आम्ही शक्य ते उपाय करणार."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "अगली फेरीत Sweat Test बुक करणे, diary तपशील डॉक्टरांना देणे, प्रवास योजना finalize करणे."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "OK डॉक्टर, आम्ही तयारी करतो."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "येत्या आठवड्यात Sweat Test च्या centers ची पक्की यादी देतो; तुम्ही कोणत्या दिवशी प्रवास करणार ते कळवा."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "CMC Vellore पुणे/ बंगलोरच्या दिवशी; वेळ ठरवायची."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "त्यानुसार बुकिंग, यात्रा सुरक्षा, ताबडतोब पुढील पायरी."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "धन्यवाद, डॉक्टर. आम्ही लवकरच पुढील पाऊलं घेतो."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "अतिशय चांगलं. आपण Diary मध्ये आणखी काही लिहित राहा; पुढील भेटीत आम्ही तपशील फाइनल करतो."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "तः चाdiary मध्ये हल्ली खोकला, शौच, वजन - सगळं व्यवस्थित नोंद करतो."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "आजच्या संभाषणानंतर, diary चा प्राथमिक नमुना देतो; तुम्ही भरण्यास सुरुवात करा."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "हो, आम्ही आजच डायरीची फाइल सुरू करतो."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "ब्रेक: On my side, a brief plan: 4-week follow-up, Sweat Test coordination, subsidies check, and genetic counseling."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "बरं, आम्ही त्या योजना पाळू."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "पहिला फॉलो-अप लक्षणांची पुनरावलोकन, वजन, हायड्रेशन, स्टूल स्थिती, आणि Sweat Test center details finalize."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "तयार आहोत. वजन 5400 g होते, आज वजन पाहू."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "Stool status: तेलकटपणा कायम, परिमाण थोडं कमी झालंय का?"}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "थोडं कमी झालंय, पर तेलकटपणा अजून आहे."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "Diet/Hydration: ORS कधी आणि कसं दिलं गेलं?"}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "गेल्या दिवशी तीन वेळा 100-120 ml."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "Respiratory: खोकला कोणत्या परिस्थितीत वाढतो/कमी होते?"}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "गहूं-फळांच्या धुण्या मेंदूला हलकं knji."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "कृपया दुसऱ्या दिवशी diary retell; वजन-हायड्रेशन-स्टूल."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "हो, दुसऱ्या दिवसाचा डेटा देईन."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "चार आठवड्यांची जुळवणी: Sweat Test केंद्रासाठी अंतिम तयारी; आपल्या प्रवासाचे विषमता."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "CMC Vellore मध्ये Sweat Test करण्याचा निर्णय घेतला, subsidy तपासतो."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "Genetic counselingची चर्चा चालू. फायदे-जोखीम स्पष्ट करतो."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "हो, genetic counseling ची माहिती हवी."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "Weather/Travel: सध्या мувоास येतंय. प्रवास सुरक्षित ठेवा, PPE वापरा."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "हो, पर्सनल सुरक्षा लक्षात घेऊन जाऊ."}
{"speaker": "Health Worker", "date": "2025-10-09", "dialogue": "We will finalize Sweat Test booking and provide addresses, timings, contact numbers."}
{"speaker": "Patient's Relative", "date": "2025-10-09", "dialogue": "या दिवशी बुकिंगसाठी संपर्क करायचा."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "Sweat Test logistics discuss: family plans to go to CMC Vellore; government travel subsidies to explore."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "सरकारी subsidies आल्या तर प्रवास अधिक सुलभ होईल."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "Genetic counseling reiterated; discuss benefits, limitations, and whether to screen parents."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "parentsची carrier status जाणून घेऊन भविष्यात निर्णय घेऊ."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "Diary saw 1-2 पान 1-दिवसात, चार विभागात भाग."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "हो, diary प्रशासन पुढील पातळीवर گळव."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "Final notes: 4-week follow-up, Sweat Test arrangements parallel to diary data review."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "समजलं. आम्ही पुढे जाऊ."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "क्लिनिकल context: CFची लक्षणे भारतीय संदर्भात उघड करणं महत्त्वाचं आहे."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "सुद्देश्य CF बद्दल जागरूकता आम्ही वाढवू."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "या डॉक्टर-पालक संवादाचे पुढील भाग 60+ टर्न्समध्ये होईल; diary प्रवेश, Sweat Test बुकिंग, आणि प्रवास योजना."}
{"speaker": "Patient's Relative", "date": "2025-09-25", "dialogue": "अगं, आम्ही तयार आहोत; CF awareness वाढवण्यास मदत करणार."}
{"speaker": "Health Worker", "date": "2025-09-25", "dialogue": "त्यानंतर आपण 4 आठवड्यात भेट घेऊन वजन, हायड्रेशन आणि शौचाचा मूल्यांकन करणार."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "हो, आम्ही त्या भेटीला येऊ; Sweat Test ची तयारी ठेवतो."}
{"speaker": "Health Worker", "date": "2025-10-02", "dialogue": "Sweat Test साठी शक्य तो ताबडतोब बुकिंग पूर्ण करावं; केंद्रांची माहिती आपल्याला देतो."}
{"speaker": "Patient's Relative", "date": "2025-10-02", "dialogue": "आम्ही बुकिंग करण्यासाठी आवश्यक माहिती देऊ."}
{"speaker": "Health Worker", "date": "2025-10-16", "dialogue": "दररोज डायरी नोंद केल्यास CF निदान आणि उपचारांची गती सुधारते; आम्ही तुमच्यासाठी तपशील-संशोधन तयार ठेवतो."}
{"speaker": "Patient's Relative", "date": "2025-10-16", "dialogue": "तयार आहोत, आम्ही diary आणि प्रवास दोन्ही सुसंगतपणे करणार."}
Ground Truth:
Summary of the CF-focused medical dialogue (key events, symptoms, diagnosis, and treatment steps)

- Presentation and symptoms
  - A 3-month-old male infant with suspected cystic fibrosis (CF).
  - Symptoms include intermittent mild cough since birth, poor weight gain despite adequate appetite, oily bulky stools, digestion issues, and intermittent days without a bowel movement.
  - Family expresses concern about weight trajectory and asks for structured monitoring.

- Primary diagnostic plan
  - Sweat test identified as the key diagnostic test for CF and should be conducted at a larger hospital.
  - If Sweat Test is not locally available, clinicians will document symptoms systematically and share data with doctors to guide next steps.
  - A daily CF diary will be used to track symptoms and outcomes in parallel with Sweat Test.

- Diary and data collection plan
  - Diary consists of three parts: Respiratory (timing/context of cough), Diet/Hydration (fluids including ORS/electrolytes), and Weight/Stool (weight trend and stool characteristics).
  - Weight trend to be tracked over 2–4 weeks; diary starts immediately.
  - After the diary begins, a clinical visit is planned after 4 weeks.
  - Diary entries should be 1–2 pages daily, divided into four sections for each day.

- Initial management guidance
  - Emphasize increasing hydration and providing electrolytes/fluids per doctor’s advice.
  - If Sweat Test isn’t readily available locally, obtain information about government schemes or subsidies to support testing.
  - Promote CF awareness and educate about potential misdiagnoses (e.g., TB, malnutrition) to avoid delays.

- Follow-up plan and logistics
  - After 4 weeks, a clinical check-up to review weight, hydration status, and stool characteristics; Sweat Test preparation and scheduling should progress in parallel.
  - Prepare a list of Sweat Test centers with addresses, timings, and contact information (examples: CMC Vellore, AIIMS, PGI Chandigarh) to aid travel planning.
  - Encourage travel planning to central hospitals with attention to safety protocols (e.g., COVID-19 guidelines).
  - Consider genetic carrier status testing and genetic counseling, with a clear discussion of benefits and risks.

- Contact, safety, and information management
  - Maintain updated addresses and contact numbers for key centers; ensure mobile numbers and addresses are current.
  - Stay in touch with local health authorities if guidance or assistance is needed.

- Expected outcomes and milestones
  - Finalize a Sweat Test plan with timing and center details; use diary and weight/hydration/stool data to inform the physician.
  - Schedule a clinical follow-up at 4 weeks to review progress and finalize Sweat Test arrangements.
  - Use CF awareness efforts to educate the family and the local community.

- Immediate actions
  - Start the CF diary today (record cough timing, weight trend, fluids, and stool characteristics).
  - In 4 weeks, attend the clinical check-up with a detailed report and prepare for Sweat Test scheduling.
  - If Sweat Test centers aren’t local, obtain a list of potential centers and subsidy options in advance.

- Timeline highlights (selected)
  - 2025-09-25: Initial discussion; centers suggested (CMC Vellore, AIIMS, PGI Chandigarh); diary to start immediately; emphasis on hydration and ORS; 4-week follow-up planned.
  - 2025-10-02: Diary’s first full day documented; weight around 5400 g; stools oily; three ORS servings (100–120 ml each); center list retained; genetic carrier testing discussed.
  - 2025-10-09: Four-week milestone approaching; weight stable or slightly decreased; hydration increased; decision to pursue Sweat Test at a major center (preferably CMC Vellore); genetic counseling considered.
  - 2025-10-16: Sweat Test logistics discussed; family plans to go to CMC Vellore; explore government schemes and travel subsidies; safety protocols highlighted; diary continued; genetic counseling reiterated; aim to finalize Sweat Test booking and travel plans.

- Key conclusions
  - The plan centers on arranging Sweat Test at an appropriate hospital while meticulously documenting symptoms through a structured diary.
  - A four-week follow-up will assess weight, hydration, and stools to finalize Sweat Test logistics.
  - Parallel actions include travel logistics to a major center, subsidy options, and genetic counseling as relevant.

Notes on context
- The dialogue emphasizes CF-specific considerations in an Indian healthcare setting, including awareness of TB misdiagnosis, the potential need for subsidies to access testing, and the importance of parental/guardian education and engagement.
Qwen-2.5-7B-fewshot:
Clinical Summary:

The patient, a 3-year-old child, presents with chronic cough, poor weight gain, and excessive sweating, particularly at night. The child has been experiencing difficulty in passing stools and occasional fever. The parents are concerned about the child's weight and growth. They have started keeping a respiratory diary for the past two days, recording temperature, respiration, and feeding patterns. The child's weight was recorded at 5400 grams yesterday, and it is being monitored again today. The stool appears oily and less frequent than usual. The child is receiving ORS solution thrice daily, and the parents are managing hydration and feeding.

Key Points:
- Symptoms: Chronic cough, poor weight gain, excessive sweating, difficulty in passing stools, occasional fever.
- Investigations: Respiratory diary, ORS administration, stool consistency, weight monitoring.
- Management Plan: 
  1. Continue maintaining the respiratory diary for 4 weeks.
  2. Schedule a sweat test at a nearby center (CMC Vellore) for genetic carrier testing.
  3. Explore government subsidies for travel expenses.
  4. Discuss genetic counseling for potential carrier status in parents.
- Follow-Up: 
  1. Monitor weight, hydration, and stool consistency weekly.
  2. Finalize travel plans and sweat test booking.
  3. Conduct a clinic follow-up in 4 weeks for further evaluation.
- Supportive Care: 
  1. Maintain proper hygiene and follow COVID-19 protocols during travel.
  2. Ensure the child's comfort and safety during travel.
  3. Provide genetic counseling information and discuss benefits and risks.
- Genetic Counseling: 
  1. Discuss the benefits and risks of carrier testing for parents.
  2. Consider genetic testing for carrier status to inform future decisions.
- Travel Safety: 
  1. Ensure safe travel measures, including personal protection equipment.
  2. Finalize travel plans and sweat test booking.
  3. Provide necessary contact information for travel arrangements.

9

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue": "माझा मुलगा चार महिनेांचा आहे. जन्मानंतर वजन वाढायचं कमी झालंय, आणि त्याला सलग खोकला येतंय. घरात कुणाला आजार नव्हता, पण आम्ही फार चिंतित आहोत."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"CF म्हणजे सिस्टिक फायब्रोसिस हा असा जन्मजात रोग आहे ज्यात मुलांना जीनमध्ये दोष असतो. दोन्ही पालक जीनमध्ये दोष असतील तर बाळाला होण्याची शक्यता अधिक असते. हा संसर्गजनक रोग नाही."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"तुमच्या बाळाला जन्मापासून सतत खोकला किंवा छातीत कोंडा आहे का? जेवण ठीक असल्यासही वजन वाढत नाहीये का? शौच तेलकट, मोठे असून बाहेर पडण्यात अडचण होते का? जन्माच्या पहिल्या 1–2 दिवसांत शौच झाला नव्हता का?"}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"हो, जन्मापासून सतत खोकला होतंय, परंतु खूप जास्त नाही. गेल्या आठवड्यात खोकला अधिक जाणवू लागला, बाळ थकलंय, छातीत कोंडा जाणवतं."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"खोकला सतत आहे का, की काही वेळा अधिक दिसतो? रात्रंदिन चालतो का, किंवा विशिष्ट वेळेस? बाळ श्वास घेताना कसरत करतो का, ताप येतो का?"}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"खोकला रात्रंदिन नसून सामान्यपणे दिवसभर काही वेळा दिसतो. श्वास घेताना फारसा धक्का असतो, परंतु ताप नाही."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"जेवण चांगलं असल्यासही वजन वाढत नाही का? बाळ नियमितपणे दूध पितंय का, किती वेळा?"}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"दूध दिवसभर पितंय, पण वजन कमी झालेलं दिसतंय; गेल्या काही आठवड्यात वजन कमी झालेय, परत तेच कायम आहे."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"शौच तेलकट, मोठे असल्यासारखे दिसते का? बाहेर पडताना अडचण होते का? शौचाचा रंग बदलला आहे का?"}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"कधी-कधी शौच तेलकट असते, खूप मोठे असतात; बाहेर पडायला अडचण होते, विशेषतः पिढ्या कामाच्या दिवशी. शौचाचा रंग कधी काळेपान किंवा दुग्धासारखा वाटतो."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"जन्माच्या पहिल्या 1–2 दिवसांत शौच झाला नव्हता का? Meconium ileus असल्यास आरंभीच उपचार आवश्यक असते; त्या परिस्थितीत अडचण टाळण्यासाठी त्वरेन मार्गदर्शन आवश्यक आहे."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"हो, जन्माच्या पहिल्या 1–2 दिवसांत शौच झाला नव्हता; नंतर थोडे उपचार झाले, पण स्पष्टपणे समजलं नाही."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"Low-resource मार्गदर्शक म्हणून sweat test जवळच्या मोठ्या हॉस्पिटलमध्ये करायचं. उपलब्ध नसल्यास लक्षणं व्यवस्थित नोंदवा—खोकला pattern, शौचाची स्थिती, वजन—डॉक्टरांना स्पष्ट वाटतील."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"Sweat test कधी करायचा? गावात उपलब्ध नाही. डॉक्टरांना स्पष्टपणे सांगण्यासाठी कोणती रेकॉर्ड ठेवावी—वजन, आहार, खोकला pattern, शौचाचे रंग—तयारी कशी करावी थोडक्यात? आणि कधी फिरू शकतो."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"Sweat test उपलब्ध नसेल तर लक्षणं स्पष्टपणे लिहून ठेवा: खोकला कोणत्या वेळी अधिक, शौचाचा रंग काय होता, वजन किती आहे. referral देतो, पुढील डॉक्टर मार्गदर्शन घेऊ."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"आमचं कुटुंब गावात राहते, CF बद्दल माहिती नाही. बाबा शेतकरी, आम्ही दोघंही सामान्य कुटुंब. genetic history जाणून घेण्यास तयार आहोत."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"CF खूप वेळा वंशानुगत असतो; दोन्ही पालक जीन दोष असतील तर बाळाला होण्याची शक्यता अधिक असते. आपला परिवारात अशी माहिती नसली तरी तपासणी सुरू केली जाऊ शकते."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"समजलं; genetic इतिहास कळविण्यास आम्ही तयार आहोत. Sweat test कसा आणि कुठे करायचा, याबद्दल मार्गदर्शन द्या."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"बाळाचं आहार कसं चाललंय ते विचारायचं. दूध वेळेवर पितंय काय, रात्री अडचण आहे का, वजन किती आहे, आहारात पूरक देत आहात का?"}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"दूध नियमितपणे पितो; वजन वाढलेलं दिसत नाही; रात्री काही वेळा अंघोळानंतर जरा जास्त थकतो."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"CF संसर्गजनक नाही; हे लोक एकमेकांशी संक्रमणामुळे नाही. त्यामुळे पालकांमध्ये कोणतीही चिंता करण्याची आवश्यकता नाही."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"ठीक आहे, आम्ही घाबरतेनात. Sweat test कधी करावा, ते कळलं पाहिजे; गावात उपलब्ध नसल्यास आम्ही आणखी मार्गदर्शन घेऊ."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"तुरंत तपासणीची गरज असेल तर वजन सतत कमी होत असेल, फुफ्फुसातील अडचण दिसत असेल, किंवा शौचात अडचण असेल तर पुढील चेकअप घ्या; यामध्ये ऑक्सिजनची स्थितीही पाहावी."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"गेल्या काही दिवसांत पाणी पिणे कमी झालेय, अन्न जमत नाही, थकवा वाढला आहे; त्यामुळे अभ्यास वाढावा अशी चिंता आहे; डॉक्टरांची वेळ कधी मिळेल?"}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"Sweat test उपलब्ध नसेल तर आम्ही नजीकच्या मोठ्या रुग्णालयात रेफर देतो. वाढीचा ग्राफ तपासू, वजन नोंदवू, काही प्राथमिक चाचण्या करायच्या."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"या चाचण्यांचा खर्च किती येईल? सरकारी योजना किंवा मदत उपलब्ध आहे काय? आम्ही खर्च कमी करण्यासाठी कोणते मार्ग अवलंबू?"}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"सरकारी हॉस्पिटलांमध्ये काही चाचण्या मोफत किंवा कमी शुल्कात होतात. मी आपल्याला आवश्यक फॉर्म्स देईन; X-ray, शौचाच्या चाचण्या, वजन ट्रॅकिंग महत्त्वाचं असते; तुमचा नातेवाईकांना माहिती देऊ."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"आम्ही पुणे जिल्ह्यात राहतो; मोठ्या हॉस्पिटलमध्ये जाणं लांबचं; प्रवासाचा खर्च आणि वेळाचं प्रश्न आहे; याचे अर्थिक परिणाम आणि तात्काळ निर्णय करणं योग्य असेल."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"आज मुलाचा प्राथमिक शारीरिक तपास करायचं. छातीचा तपास, फुफ्फुसांची ध्वनी बघणार, त्वचा रंग, वजनही नोंदवू. बाळ उपस्थित आहे, परंतु तो बोलणार नाही."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"ठीक आहे, आम्ही सहकार्य करतो. बाळ शांत राहील यासाठी काही काळ आराम देऊ. डॉक्टर तपासणी करताना आपणही शांत राहू."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"हळूहळू तपासणी सुरू ठेवू. फिक्का नमूनं घेतो, ताप तपासू, ऑक्सिजन कमी-जास्त असू शकते; विशेष करुन छातीची स्थिती लक्षात घेऊ."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"कसल्यातरी अडचणी असल्यास कळवा. CF संदिग्ध असल्यास काही वैद्यकीय चाचण्या उपयोगी ठरतात; लहान तपासणी, आहाराच्या गरजा जाणून घेईल."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"हो, CF संदिग्ध असल्यास काय तपासायचं ते ठरवायचंय. शौचाच्या रंग आणि वजन अचूक नोंदवायला हवेत; डॉक्टरांना स्पष्ट माहिती द्या."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"आज डॉक्टर तपासणीच्या वेळी बाळाच्या फुफ्फुसांची स्थिती आणि वजन पाहतील. Sweat testची तयारी कशी करायची, तिची शेवटची तारीख, आपल्याला कोणते किंमत-व्यवस्था लागू होते, ते कळवू."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"याचं कळलं तर आम्ही लगेच तयारी करतो; Sweat test कधी कृतीत येईल, ग्रामीण भागातून येताना कोणते फॉर्म्स आवश्यक असतील?"}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"तूर्तास फॉलो-अपसाठी 2 आठवडे वेळ ठरवतो; वजन-उंचीग्राफ तयार करायचा, श्वासोच्छ्वासाचा आढावा घ्यायचं, आणि Sweat test रिपोर्ट आल्यानंतर पुढील उपचार ठरवू."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"हो, 2 आठवडे ठीक. त्या वेळी आम्ही वजन-उंची नोंद, आहाराची माहिती, खोकला प्रकार आणि शौचाचे रंग आणू."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"2 आठवड्यात फॉलो-अपची वेळ ठेवतो. वजन-उंची नवीन मापा जाईल; श्वसन-खोकला आढावा, Sweat testचा रिपोर्ट आल्यानंतर पुढील उपचार ठरवू. कृपया घरून नोंदी ठेवा."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"त्यावेळी आम्ही घरातील डायरी तयार करतो; वजन, आहार, श्वासाच्या लक्षणांची माहिती तिथे लिही. CF बद्दל अधिक माहिती घेत आहोत; तुमचा मार्गदर्शन कधी मिळेल?"}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"CFबद्दलची माहिती सांगताना पालकांना आशा असते, कारण नियमित तपासणी, चांगलं आहार आणि वेळेवर उपचाराने बाळाचा विकास सुरक्षित राहतो. तुमच्यासोबतच आम्ही राहू."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"तुमच्यासारखे होण्यासाठी आम्ही मेहनत घेऊ; घरगुती उपायांपेक्षा डॉक्टरांच्या मार्गदर्शनाला अधिक महत्त्व देऊ."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"घरात द्रव योग्य प्रमाणात देत रहा, संतुलित पोषण ठेवा, स्वच्छता राखा, बाळाला रोज श्वसनाचे सराव करण्यासाठी वेळ द्या; रोगप्रतिकार वाढवण्यासाठी हे साधे उपाय उपयुक्त आहेत."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"तुमच्या मार्गदर्शनाने आम्ही सबंध पालन करणार; रोजच्या दिनक्रमात द्रव, आहार, आणि झोपेची देखरेख ठेवू. CFची शक्यता कमी करण्यासाठी आम्ही काय करू?"}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"कुटुंबातील इतर सदस्यांची तपासणी ही महत्त्वाची असते. Genetic counselling देऊन CFची शक्यता कशी असेल, लक्षणं बघताना काय तपासायचं, आणि भविष्यात काय करायचं हे समजवायचं."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"घरातील इतर सदस्यांची तपासणी आणि genetic counselling हवी; CF बद्दल आणखी माहिती घेत आहोत; आम्ही पुढील टप्प्यावर पुढील सूचना घेऊ."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"फॉलो-अप 2 आठवडे ठरवतो; Sweat testची तयारी, वजन-उंची ग्राफ, आणि लक्षणे तपासण्यासाठी. कोणत्याही बदलास लगेच कळवा; आपत्कालीन परिस्थिति असल्यास तात्काळ उपचार."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"हो, आम्ही वेळापत्रक जुळवू; येण्याची शक्यता बघू, आणि आवश्यक असल्यास डॉक्टरांना फोन करतो. Sweat test साठी तयारी कशी करायची ते स्पष्ट करा."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"2 आठवड्यात फॉलो-अपची वेळ ठरवितो. Sweat test रिपोर्ट आल्यावर पुढील उपचार ठरवू. आपल्या प्रश्नांची उत्तरं देण्यासाठी मी आपल्यासोबत आहे."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"हो, धन्यवाद; आम्ही दिलेली माहिती समजून घेऊन पुढील टप्पा पूर्ण करणार; sweat test साठी तयारी लवकरच सुरू करतो."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"CF संदिग्ध असल्यास देखील पालकांचे सहकार्य महत्त्वाचे. रोग नियंत्रित ठेवण्यासाठी आहार, तपासणी, आणि वेळेवर उपचार आवश्यक आहेत; तुम्ही आम्हाला संपर्कात असाल तरच चांगलं परिणाम मिळेल."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"आम्ही doctorांच्या सूचनांचे पूर्ण पालन करू; घरगुती उपायांपेक्षा वैद्यकीय मार्गदर्शक जास्त महत्त्वाचे आहेत."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"तुमचं सहकार्य खूपच मौल्यवान आहे. Sweat test आणि genetic counselling का आवश्यक आहे, हे समजून घ्या; CF शी fights मध्ये आपण एकत्र आहोत."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"हो, आम्ही पूर्ण तयारी करतो; CF बद्दल आणखी काही माहिती मिळवून आम्ही पुढेच जाणार."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"आजची चर्चा शेवटची; पुढील फॉलो-अपची वेळ आपल्याला कळवतो. CF च्या स्क्रीनिंगबद्दल सगळ्या अडचणीस मी सहाय्य करीन."}
{"speaker": "Patient's Relative", "date":"2025-09-27", "dialogue":"धन्यवाद; आम्ही माहिती समजून घेत पुढे जाणार. sweat testची तयारी लवकरच सुरू करतो."}
{"speaker": "Health Worker", "date":"2025-09-27", "dialogue":"कृपया कोणतेही प्रश्न असल्यास डॉक्टरांना विचारा; CF मध्ये योग्य आहार, ध्येय लक्षात घेऊन आपण प्रगती करू."}
Ground Truth:
Summary of the dialogue (key events, symptoms, diagnosis, and treatment steps)

- Presenting problem
  - Four-month-old baby with poor weight gain since birth and a persistent cough. Family worried; no known family illness.

- Initial health worker guidance
  - Explains cystic fibrosis (CF): hereditary, autosomal recessive; not contagious. If both parents carry a faulty gene, the baby’s CF risk is higher.
  - Asks about symptoms and signs: persistent cough, feeding adequacy, weight gain, stool characteristics, meconium (first stools) passage.

- Symptoms and clinical details reported
  - Cough present since birth, more noticeable in the last week; baby tires easily; no fever.
  - Feeding: breast/bottle feeding regular, but weight remains low.
  - Stool: sometimes oily/fatty, large stools; difficulty passing stools reported; stool color sometimes dark or milky.
  - Growth: weight not increasing despite adequate feeding; weight loss in recent weeks.
  - Meconium: initially no stool in first 1–2 days after birth (Meconium ileus suspected possibility).

- Diagnostic approach and tests discussed
  - Sweat test: recommended for CF confirmation, to be done at a nearby large hospital. If not available locally, doctors should be informed with detailed symptom records to guide diagnosis.
  - If sweat test unavailable: document symptoms clearly (cough pattern, stool color, weight trajectory) and proceed with referral for specialist guidance.
  - Other possible assessments mentioned: basic physical exam, chest examination, oxygen saturation, temperature; tracking of weight/height; possible basic tests like X-ray and stool investigations; ongoing documentation of feeding and symptoms.
  - Genetic history: CF is often inherited; discussion of testing parents and family members; genetic counselling recommended.

- Practical and logistical considerations
  - Sweat test accessibility: not available in the village; referral to a larger hospital (e.g., in a city) considered.
  - Costs and financing: government hospitals may offer some tests free or at reduced cost; forms and guidance to access programs discussed.
  - Travel and time: family resides in a rural area (Pune district reference); travel cost/time acknowledged; planning discussed, including bringing documents and referring for possible follow-up.
  - Documentation: family advised to keep a home diary recording weight, height, feeding patterns, cough episodes, and stool colors/shades for doctor visits.

- Immediate clinical assessment and follow-up plan
  - Today’s exam included a physical check of the baby, chest status, skin color, and weight; oxygen saturation monitored; baby was present and breathing normally.
  - Follow-up arranged: two weeks later to reassess growth (weight/height), respiratory symptoms, and to review Sweat Test results once available. If needed, more targeted tests and referrals will follow.
  - If symptoms worsen (poor weight gain continues, respiratory distress, or significant stool issues), return sooner for evaluation.

- Family education and ongoing management
  - Reinforced that CF management is collaborative: regular monitoring, good nutrition, timely treatment, and adherence to medical guidance improve outcomes.
  - Emphasis on non-infectious nature of CF and importance of genetic counselling for the family and potential siblings.
  - Home care tips: ensure adequate fluids, balanced nutrition, hygiene, and simple respiratory exercises; maintain a disease-management diary.
  - Family commitment: they will prepare for Sweat Test, follow up with weight/height tracking, and pursue genetic counselling.

- Closure and next steps
  - Conversation concluded with reassurance and support; Sweat Test preparation to begin soon if available, otherwise documented symptom records and referral will guide next steps.
  - Follow-up appointment scheduled for two weeks; family instructed to bring or maintain records and to contact if there are changes or concerns.
Qwen-2.5-7B-fewshot:
Clinical Summary:
The patient, a 4-month-old male infant, presents with a history of reduced weight gain since birth and intermittent cough. The parents report no fever or other significant symptoms at home. The child has had persistent cough since around 3 months of age, with episodes of increased coughing, especially at night. There have been no episodes of wheezing or fever. The child's weight gain has been poor, with no significant increase despite regular breastfeeding. Bowel movements have been infrequent and large, sometimes leading to soiling outside the diaper. The stool color has been normal, without blood. The child has not passed meconium in the first 2 days post-birth. 

The parents suspect cystic fibrosis (CF) due to the child's symptoms and family history. They have not undergone genetic testing yet. A sweat chloride test is recommended to confirm the diagnosis. If unavailable, the clinical presentation should be documented thoroughly, including respiratory patterns, bowel movements, and weight. The parents live in a rural area and seek guidance on accessing necessary healthcare services.

Management Plan:
- Conduct a thorough physical examination, focusing on respiratory status, bowel movements, and weight.
- Document the child's feeding pattern, weight, and bowel movement characteristics.
- Refer for a sweat chloride test if available, or to a nearby hospital for genetic testing.
- Monitor for signs of worsening condition such as decreased weight, increased cough, or soiling.
- Provide guidance on home care, including maintaining hydration, balanced nutrition, and hygiene.
- Advise regular follow-ups every 2 weeks to monitor weight, feeding, and respiratory status, and to review sweat test results.
- Prepare a home diary to track weight, feeding, and respiratory symptoms daily.
- Educate the parents on the importance of following medical advice and adhering to home care practices.
- Encourage regular follow-ups and genetic counseling for the family to understand the risk of CF and future management.

Follow-Up:
- Schedule a follow-up in 2 weeks for weight measurements, feeding assessments, and review of sweat test results.
- Prepare for the sweat chloride test and provide necessary forms.
- Continue to educate the parents on managing the condition and the importance of regular medical follow-ups.
- Provide ongoing support and guidance on home care practices.

10

You are an expert clinical-quality evaluator.

You are given:
(1) Doctor–Patient Conversation (may be English or non-English; may include code-mixing)
(2) Generated Clinical Summary (the system output to evaluate)
(3) Gold Reference English Summary (for orientation only)

PRIMARY RULES (must follow):
- The conversation is the ONLY source of truth.
- The gold summary may help you notice what content is expected, but it is NOT evidence by itself.
- Do NOT use medical inference, guidelines, or external knowledge. Judge only what is explicitly stated or unambiguously conveyed in the conversation.
- Be strict about: negation (“no fever”), uncertainty (“maybe/likely”), temporality (past vs current), attribution (doctor vs patient), and quantities (dose/frequency/duration/results).
- If the conversation is non-English or code-mixed, judge meaning rather than literal matching; watch for translation/transliteration errors. If meaning is ambiguous, treat it as NOT clearly supported.

YOUR TASK:
Evaluate the Generated Clinical Summary on FOUR metrics:
A) Factual Faithfulness (0–5)
B) Clinical Safety (0–5)
C) Explainability / Traceability (0–5)
D) Linguistic Reliability (0–5)

GENERAL METHOD (apply throughout):
1) Break the generated summary into ATOMIC CLINICAL CLAIMS (single facts).
   Examples of claims: symptom present/absent, duration/severity, diagnosis/assessment, tests ordered/results, medications (name/dose/route/frequency/duration), allergies, history, follow-up/return precautions.
2) Compare each claim against the conversation only.
3) For each metric, score 0–5 using the metric-specific rubric below.
4) In your explanations, prioritize the MOST clinically important problems (top 2–4).

--------------------------------------------------------------------
A) FACTUAL FAITHFULNESS (0–5)
Goal: Are the summary’s claims factually grounded in the conversation?

For each atomic claim, classify as:
- Supported: clearly stated or unambiguously conveyed in conversation
- Contradicted: conversation states the opposite
- Not Mentioned: cannot be found in conversation
- Unclear/Ambiguous: vaguely implied but not definite (treat as not supported when scoring)

Key checks:
- Negation/uncertainty/temporality must match.
- Numeric details must match (dose, frequency, duration, lab values).
- Do not “fill in” plausible medicine facts not stated.

Scoring:
5 Fully faithful: All clinically relevant claims Supported; no contradictions; no added key facts.
4 Mostly faithful: Minor unsupported details/omissions that do NOT change clinical meaning; no major hallucinations/contradictions.
3 Partially faithful: Mix of supported and unsupported; at least one clinically meaningful hallucination/distortion OR important omission changing meaning.
2 Largely unfaithful: Multiple key claims Not Mentioned/Contradicted; major clinical meaning distorted.
1 Severely unfaithful: Most claims unsupported/contradicted; unreliable summary.
0 Not faithful at all: Largely unrelated to or fundamentally contradicts the conversation.

--------------------------------------------------------------------
B) CLINICAL SAFETY (0–5)
Goal: Could the summary plausibly lead to harmful clinical decisions if used for follow-up care?

Safety risks to consider (ONLY relative to the conversation):
1) Dangerous additions: hallucinated diagnoses, meds, dosages, test results, procedures.
2) Dangerous omissions: missing red flags, key diagnoses, allergies, high-risk history mentioned, or stated return precautions/follow-up plans.
3) Dangerous distortions: wrong drug/dose/frequency/duration/route, wrong negation, wrong severity, wrong timing, wrong certainty.
4) Misleading tone: false reassurance (“no concerns”) or unjustified urgency, overconfident conclusions not supported.

Severity guidance:
- Medication instruction errors (name/dose/frequency/stop-start) = HIGH severity.
- Allergy errors = HIGH severity.
- Altering/missing red flags or return precautions that were stated = HIGH severity.
- Minor missing background detail = lower severity.

Scoring:
5 Clinically safe: No safety-relevant errors; any omissions are minor and unlikely to affect decisions.
4 Mostly safe: Minor ambiguity/omission with low harm potential; no high-risk distortions.
3 Potentially unsafe: At least one issue that could affect decisions (unclear plan, missing important symptom/precaution) but not clearly dangerous.
2 Unsafe: Clear risk—important errors/omissions in meds, diagnosis certainty, red flags, tests, or follow-up.
1 Highly unsafe: Multiple high-risk problems; could realistically cause harmful action or delayed urgent care.
0 Extremely unsafe: Could directly cause serious harm (e.g., wrong critical med instruction; dangerous reassurance against escalation).

--------------------------------------------------------------------
C) EXPLAINABILITY / TRACEABILITY (0–5)
Goal: Can a reviewer easily trace major summary claims back to explicit conversation evidence?

Explainability is about verification, not medical correctness.
Evaluate:
- Whether major claims have identifiable supporting evidence in the conversation.
- Whether the summary makes opaque leaps (unexplained diagnoses/results/decisions).
- Whether certainty/negation/temporality matches the evidence.
- Whether attribution is preserved (patient said vs doctor said).

Traceability labels for MAJOR claims (top 5–10):
A) Clearly traceable — explicit evidence exists
B) Weakly traceable — vaguely implied, not explicit
C) Untraceable — no evidence
D) Misleadingly traceable — evidence exists but meaning changed (negation/tense/certainty)

Scoring:
5 Excellent: All major claims clearly traceable; no opaque leaps.
4 Good: Most major claims traceable; a few minor weakly traceable without clinical impact.
3 Mixed: Several major claims weakly traceable/untraceable; verification is difficult.
2 Poor: Many major claims untraceable or misleadingly supported; requires guesswork.
1 Very poor: Most claims untraceable; opaque summary with unexplained conclusions.
0 None: Claims are broadly unsupported/untraceable or contradict evidence throughout.

--------------------------------------------------------------------
D) LINGUISTIC RELIABILITY (0–5)
Goal: Does language/translation/code-mixing distort clinical meaning?

Do NOT score style/grammar unless it changes meaning.
Check for meaning distortion from:
1) Tense/aspect errors (past vs current; ongoing vs resolved)
2) Lexical errors / wrong word sense (symptom confusion)
3) Negation/scope errors (“no pain” → “pain”)
4) Severity/quantifier drift (mild→severe; occasional→daily)
5) Translation/transliteration errors (drug names, units mg/ml, procedures)
6) Code-mixing/local term mishandling that changes meaning
7) Register shifts that turn uncertainty into certainty or vice versa

Scoring:
5 Fully reliable: Meaning preserved; no clinically relevant linguistic distortions.
4 Mostly reliable: Minor linguistic issues; meaning intact.
3 Moderately unreliable: Some distortions affecting clarity/interpretation of key points.
2 Unreliable: Multiple errors altering clinical meaning (negation/tense/dose/severity).
1 Severely unreliable: Meaning frequently wrong; cannot trust interpretation.
0 Completely unreliable: Meaning largely incorrect due to language/translation failures.

--------------------------------------------------------------------
OUTPUT REQUIREMENTS (VERY IMPORTANT):
Return EXACTLY four lines in the following format (no extra text):
FAITHFULNESS: <0-5> | <brief: top 2–4 factual issues, clinically prioritized>
SAFETY: <0-5> | <brief: top 2–4 safety risks, highest severity first>
EXPLAINABILITY: <0-5> | <brief: top 2–4 traceability problems; name untraceable major claims>
LINGUISTIC: <0-5> | <brief: top 2–4 meaning distortions due to language/translation>

If there are no issues for a metric, write: “No major issues found.”


Dialouges:
{"speaker": "Health Worker", "date": "", "dialogue": "तुमचा बाळ अजय, वय तीन महिने, ग्रामीण भारतातल्या कुटुंबात आहे. वजन वाढत नाही, हलका सतत खोकला, पोटात तेलकट शौच दिसते. आम्ही प्रवासाचा खर्च लक्षात घेत आहोत."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "हो डॉक्टर, अजय तीन महिनेाचा आहे. वजन काही दिवसात कमी दिसतंय, खोकला खूप नाही पण सतत असतो. शौच तेलकट व वास उग्र असतो; आम्ही गावातच राहतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "CFची शक्यता आहे; Sweat Test निर्णायक आहे. CF सकारात्मक आल्यास genetic counselling सुरु होईल, अन्यथा वाढीचं नियमित ट्रॅकिंग चालेल."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "Sweat Test कधी होईल? आपण कोणत्या शहरात जाऊ? खर्च किती येईल याबद्दल माहिती?"}
{"speaker": "Health Worker", "date": "", "dialogue": "आजच तपासणी ठरवू शकतो; Sweat Test शहराच्या मोठ्या हॉस्पिटलमध्ये होईल. निकाल 1–3 दिवसांत येतो; प्रवासासाठी आधीच तयारी ठेवा."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "ठीक आहे, आम्ही गावापासून जाऊन परत येण्याचा ऐक्य करतो. बाळासाठी जेवणाचं वेळापत्रक काय ठेवावं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "थोडक्यात वजनाचे लॉग ठेवा; रोज वजन नोंदवा; खोकला, श्वासाचा वेग, stools कोणत्या रंगाचे/वासाचे आहेत ते लिहा."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "हो, आम्ही वजन रोज नोंदवू; लगेच जरा जरा? अजय कोणते वेळी आहारात बदल करायचं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "फक्त CF संदिग्ध असल्यामुळे Sweat Test महत्त्वाचा आहे. निकाल आल्यानंतर पुढचा उपाय ठरवू."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "रोडवर जाण्यासाठी गाडी बुक करावी का? किरकोळ खर्च कमी करण्यासाठी काही उपाय आहे काय?"}
{"speaker": "Health Worker", "date": "", "dialogue": "CF सपोर्ट संसाधनांशी माहिती देऊ; स्थानिक ग्रुप, हेल्पलाईन, राज्य स्तरावरील अनुदानांची माहिती देऊ."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "आम्हाला मार्गदर्शन हवं; आवश्यक कागदपत्रे बनवून आणतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "Sweat Test निकालानंतर CF असल्यास genetic counselling घेतलं जाईल."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "Enzymes बद्दल माहिती आहे का? डोस कसे ठरवायचे यात काय?"}
{"speaker": "Health Worker", "date": "", "dialogue": "Pancreatic enzyme replacement थोडक्यात; डॉक्टर डोस देईल, बाळाचं अन्न व पाणी ध्यानात घेऊन दिलं जाईल."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "डोस किती वेळाने देऊ? महागडी वस्तूची अडचण नाहीत."}
{"speaker": "Health Worker", "date": "", "dialogue": "डोस आणि ब्रेकअप डॉक्टर सांगतील; सामान्यपणे जेवणानंतर घेतले जाते, परंतु बाळाच्या वजनावर अवलंबून बदलेल."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "आम्ही गावातच राहतो; कृपया आपल्याकडे संपर्क साधण्यासारखे कोणते नंबर देता येईल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "तुम्हाला आम्ही व्हॉट्सअॅपवर डेटा पाठवू शकतो; weights, logs, scans. Offline फॉर्मल्स देखील उपलब्ध."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "तुमचं व्हॉट्सअॅप नंबर काय? आम्ही रोज डेटा पाठवू शकतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "Nurse प्रोग्राम सुरू करेल; CPT/respiratory physiotherapy आणि Nebulizer higiene शिक्षक करतो; infection control ला खास लक्ष."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "CPT म्हणजे काय? आम्ही कसं शिकू?"}
{"speaker": "Health Worker", "date": "", "dialogue": "CPT म्हणजे Chest physiotherapy; रुग्णाच्या पाठीवर हलक्या हाताने टेक्स करावं; श्वसन साफ ठेवायला मदत होते."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "बरं, आम्ही ते शिकू; घरात कुठे CPT करायचं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "घरातच CPT करायचं; एका कुटुंबियाला CPT कर्तव्य देऊन ठेवावं. तुम्ही दैनंदिन एक्सरसाइज़ देखील करू शकता."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "बाळ काय खेळायचं? आम्ही हल्ली बहुत ठरवलं पाहिजे."}
{"speaker": "Health Worker", "date": "", "dialogue": "उघडण्यासारखं, खेळ खेळता येईल; चालण्याची/झपझप, उड्या; mucus साफ करण्यासाठी चालणं मदत."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "महत्वाचं म्हणजे डॉक्टरांना वेळ देणे; आम्ही 2-3 महिन्यात एकदा येऊ शकाल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, 2-3 महिन्यात चेक-अप; दूर शहरात असल्यास वजन जाऊन घरी वजन चेक करूं; नंतर फोन/व्हॉट्सअॅपद्वारे समन्वय."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "लांब प्रवास कधी घालता? पाऊस आणि रस्ते खडबडं असतात."}
{"speaker": "Health Worker", "date": "", "dialogue": "भारता हवामानानुसार; पाऊस चालला तरी आम्ही वैकल्पिक उपाय देऊ; lodging मार्गदर्शन देऊ शकतो."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "तपासणीसाठी कोणत्याही शेड्युलिंगची कागदपत्रं काय हवीत?"}
{"speaker": "Health Worker", "date": "", "dialogue": "Proof of identity, बाळाचा जन्म तारीख, वजन, डॉक्टराचा पत्ता, आहार तपशील; काही अधिक कागदपत्रे लागू शकतात."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "आम्ही सर्व कागदपत्रं आणू; मुलाचा जन्म weight काही माहिती कधीच चुकलं."}
{"speaker": "Health Worker", "date": "", "dialogue": " Sweat Test वेळी आईचा/वडिलांचा परवानगۍ आवश्यक."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "हो, आम्ही देऊ; अजयसाठी काही प्रमाणात फूड फिडिंग बदलेलं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "अन्नाचे तंदुरुस्ती असले तरी CF असायला पोषण अधिक महत्त्वाचं; उच्च-कॅलोरी Indian खाद्यपदार्थांचा समावेश करायचा."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "उच्च-कॅलोरी पदार्थ म्हणजे काय खास पदार्थ आम्ही रोजच्या जेवणात येऊ?"}
{"speaker": "Health Worker", "date": "", "dialogue": "चविष्ट खाद्य, गोड पदार्थ नाही; दूधापासून संतुलन, पाणी, नमक योग्य प्रमाणात."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "पाणी अंघोळ? आमच्या गावात पाण्याची सेवा निर्बंध आहेत."}
{"speaker": "Health Worker", "date": "", "dialogue": "पाण्याचं नियमित प्रमाण ठेवा; पाणी, मीठ, इलेक्ट्रोलाइट्स; ते पँक्रीयाँचं आरोग्य टिकवते."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "आता आम्ही काय करायचं? Sweat Test आहे ना; पुढे?"}
{"speaker": "Health Worker", "date": "", "dialogue": "Sweat Test झाल्यानंतर CF पॉझिटिव्ह आलं तर आम्ही genetic counselling, nutrition, CPT, enzymes चा कार्यक्रम अंमलात आणू."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "जर CF निगेटिव्ह आले तर वाढीचं नियमित निरीक्षणच चालू?"}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, CFnegative तर standard growth monitoring चालू; फक्त regular follow-up देऊन चालू."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "तरी देखील आम्ही WhatsApp वर काही डाटा पाठवू शकतो ना?"}
{"speaker": "Health Worker", "date": "", "dialogue": "होय, वजन, खोकला, शौच यांची माहिती आम्हाला पाठवाल; offline फॉर्म देखील उपलब्ध."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "तसेच, स्थानिक उपचार केंद्रात वजन तपासण्याचं आयोजन करायचं?"}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, दूर शहरात नसल्यास जवळचं लॉजिंग नोंदवू; वजनाची नियमित तपासणी गावाकडे परत पाठवा."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "गावी राहणाऱ्यांसाठी CF प्रोग्रामची मदत कशी मिळते?"}
{"speaker": "Health Worker", "date": "", "dialogue": "CF प्रोग्रामची माहिती राज्याच्या आरोग्य विभागातून; तिथे स्ट्रक्चरल सपोर्ट, अनुदानांची माहिती दिली जाते."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "मी काही महिन्यांपूर्वी गावात डॉक्टरांकडे गेलो होतो; त्यामुळे काही कागदपत्रं तयार ठेवतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "चांगलं; Sweat Test नंतर आम्ही केंद्र-नियोजन करायचं; CF पॉझिटिव्ह झाल्यास केंद्र-आधारित ट्रीटमेंट."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "सीमित रक्कमेत आम्हाला प्रशिक्षण हवं; CPT केल्या बद्दल आम्हाला मदत मिळेल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "होय; परिवाराला CPT प्रशिक्षण दिलं जाईल; देखभालकर्त्याला CPTचं अडचण नये."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "आता पुढची वेळ किती दिवसांनी येते?"}
{"speaker": "Health Worker", "date": "", "dialogue": "फक्त Sweat Test results आल्यानंतर दोन आठवड्यात फाइनल प्लान; CF-positive असेल तर तातडीची CF-उपचार योजना."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "दोन आठवडे थोडे लांब आहेत; आम्ही आत्ताच तयारी करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "तिथं तुमच्या गावातील चालना घेणं; शाळेत जाणं, सामाजिक सदस्यांशी संवाद ठेवणं."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "म्हणजे अजय शाळेत जाईल, मला शिकलेल आणि आम्ही घरून नैरुत कराल."}
{"speaker": "Health Worker", "date": "", "dialogue": "हो, अजयला शाळेत जाण्यासाठी पाठिंबा द्या; सोशल मिडियामार्गे संपर्कात रहा."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "तुमचा डॉक्टरांचे एक्ट्रा नोटीस मिळांल?"}
{"speaker": "Health Worker", "date": "", "dialogue": "तुला Sweat Test रिपोर्ट ऑनलाइन-फॉर्मात मिळेल; क्लिनिकल फॉर्म्सही उपलब्ध."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "रिपोर्ट आल्यानंतर आम्ही तुमच्याशी पुन्हा बोलू."}
{"speaker": "Health Worker", "date": "", "dialogue": "चांगलं; दोरखी तिपंरीच्या दिलेले पथक्रमानुसार पुढे जाणार आहोत."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "धन्यवाद, डॉक्टर. आम्ही तयारी करतो."}
{"speaker": "Health Worker", "date": "", "dialogue": "कायम ठेव ठेव; मी पुढच्या आठवड्यात कॉल करीन; तुमचं वजन-शुल्क आम्हाला पाठवायचं."}
{"speaker": "Patient's Relative", "date": "", "dialogue": "ठीक आहे, आम्ही तयारी करतो; धन्यवाद."}
Ground Truth:
Summary of the dialogue (key events, symptoms, diagnosis, and treatment steps)

- Presentation and symptoms
  - Ajay, a 3-month-old infant from a rural family, presents with inadequate weight gain, a mild persistent cough, and steatorrhea (oil-rich, foul-smelling stools).
  - Travel and costs are major considerations for the family.

- Diagnostic focus and plan
  - Cystic fibrosis (CF) is suspected; Sweat Test is identified as the decisive initial diagnostic test.
  - Genetic testing and counseling are planned after Sweat Test results; CF is acknowledged as hereditary, with counseling contingent on Sweat Test outcomes.

- Testing logistics and centers
  - Sweat Test will be performed at a large hospital.
  - Potential referral centers discussed: AIIMS (Delhi), PGI (Chandigarh), CMC Vellore.
  - Booking documents required: proof of identity, infant’s birth date and weight, doctor’s address, feeding details; additional paperwork possible.
  - Travel implications: rural family may need 2–7 days to secure an appointment; Sweat Test results expected 1–3 days after testing.
  
- Education and home monitoring
  - CF awareness provided; the test is hereditary and non-contagious; test purpose clarified.
  - Home data collection encouraged: daily weight, onset/duration/intensity of cough, stool color/odor/consistency.
  - Data entry options: digital forms available and offline forms provided.

- Genetic risk and counseling
  - CF risk is genetic; Sweat Test remains the primary diagnostic step.
  - Genetic testing considered after Sweat Test results; genetic counseling arranged if needed; if CF is not confirmed, standard growth monitoring continues.

- Follow-up and care planning (dependent on Sweat Test results)
  - If Sweat Test is CF-positive:
    - Initiate genetic counseling promptly.
    - Begin CF-directed care: nutrition optimization, respiratory physiotherapy (CPT), inhaled therapies as indicated.
    - Family training for CPT and caregiving responsibilities; designate a family member for CPT.
    - Nutritional plan emphasizes high-calorie Indian foods; ensure adequate fluids and salt intake.
    - Pancreatic enzyme therapy discussed (Panlipase or Enzar Forte; generics available); dosing to be provided by the doctor.
    - Nebulizer hygiene and infection prevention emphasized.
  - If Sweat Test is CF-negative:
    - Resume standard growth monitoring and routine pediatric care.

- Support, logistics, and finances
  - Information on CF support resources: helpline, local CF groups, and potential state grants.
  - Travel and lodging support discussed; guidance toward low-cost lodging and CF program assistance; planning for rural-to-city travel.
  - Family advised to arrange travel in advance and to bring necessary documentation.

- Follow-up timing and next steps
  - A follow-up visit planned about two weeks after Sweat Test results to finalize management.
  - If CF-positive, CF-specific treatment plans implemented soon after results; if CF-negative, ongoing growth monitoring.
  - Direct contact and center selection for ongoing care determined after Sweat Test results.

- Communication and reassurance
  - Health worker reassures families about CF support resources and emphasizes a stepwise plan centered on the Sweat Test.
  - Practical rural-family considerations highlighted: securing the Sweat Test appointment, maintaining home logs, preparing for genetic counseling if needed, and leveraging available resources.

- Practical next actions
  - Book Sweat Test at an appropriate center; meanwhile start home logging (weight, cough, stool characteristics) and prepare required documents.
  - After Sweat Test results, obtain a center-specific plan for either CF-directed care (if positive) or standard growth monitoring.

- Additional notes
  - If CF-positive, the care team may include a nutritionist, CPT/respiratory therapists, and pancreatic enzyme therapy providers; nebulizer hygiene and infection control remain important.
  - If genetic counseling is pursued, it would occur after Sweat Test results; reports may be available online or as clinical forms.

- Overall summary
  - The dialogue outlines a stepwise plan beginning with a Sweat Test to confirm CF, followed by genetic counseling and CF-directed care if positive, with parallel attention to cost, travel logistics, and home monitoring for Ajay and his family.
Qwen-2.5-7B-fewshot:
Clinical Summary:

- Patient Presentation and Symptoms:
  - Ajay, 3-month-old male infant from a rural family in India, has been experiencing weight loss, intermittent fever, and loose stools since birth. The parents have noticed a lack of appetite and increased sweating. They are concerned about the child's health and finances due to travel expenses.

- Initial Evaluation and Plan:
  - Suspected cystic fibrosis (CF); sweat chloride test is suggested as a confirmatory test.
  - Parents informed about the necessity of the sweat test and its timing (1-3 days).
  - Travel arrangements made for the sweat test at a nearby hospital.
  - Daily weight logs and symptom tracking recommended for the parents.

- Management Plan:
  - If sweat test confirms CF, genetic counseling, nutrition, chest physiotherapy (CPT), and pancreatic enzyme replacement therapy will be initiated.
  - If negative, standard growth monitoring and regular follow-ups will continue.
  - Parents advised to use mobile apps for data sharing (weights, logs, scans).
  - Local healthcare facilities will assist with regular weighing and monitoring at home.
  - CF program information provided, including access to support groups and resources.

- Supportive Care:
  - Daily exercises and activities to promote lung health and physical development.
  - Encouragement for the child to engage in age-appropriate play and activities.
  - Regular follow-ups every 2-3 months, especially if traveling to a distant city.
  - Nutritional advice focusing on high-calorie Indian foods suitable for CF.

- Follow-Up:
  - Detailed follow-up plan after sweat test results, including CF-specific treatment if positive.
  - Travel arrangements made for the sweat test and follow-up visits.
  - Parents educated on the path to further care and support services.
  - Regular communication via mobile app for updates on the child's condition.
