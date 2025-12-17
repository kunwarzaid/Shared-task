

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

Ground Truth
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

Qwen-2.5-7B-Instruct-zero-shot
The patient is a 4-month-old male named Ajay who has had poor weight gain since birth, intermittent fever, and a history of malnutrition. The parents suspect cystic fibrosis (CF) and have brought him for evaluation. Ajay has gained some weight recently but still appears underweight. He does not have night sweats or significant fever. The parents report that he has had intermittent sweating since birth. Given the suspicion of CF, a sweat test is recommended as the diagnostic test of choice. The parents can visit a nearby CF center to arrange for the sweat test. The cost of the sweat test and travel expenses will be covered by a subsidy program. The parents should bring necessary documents such as Aadhaar card, ration card, village address, mobile number, and medical history to the CF team. They should prepare for the trip and contact the CF center for the sweat test date. 

Baseline measurements including weight, height, oxygen saturation, and temperature should be taken before the trip. The parents should maintain a diary of weight, height, diet, and bowel movements every 2-3 weeks. They should increase calorie intake, drink more water, and take pancreatic enzymes as prescribed. If there is no sweating, stool fat studies may be needed to adjust diet and enzyme dosage. Chest physiotherapy (CPT) is recommended twice a day; parents should perform it gently and involve the child in activities like singing or storytelling. They should ensure the equipment is clean and find a suitable time for CPT at home. Follow-up is scheduled two months after the sweat test results are available.

The parents should ensure proper hydration, maintain a balanced diet, and consider travel plans if needed. The CF team will provide guidance on travel arrangements and accommodations. If there are any changes in hydration status, they should contact the CF center. The sweat test results will determine if CF is confirmed or if other causes need to be investigated. The parents should keep the appointment for the sweat test and follow the plan accordingly. They should continue to monitor weight, diet, and bowel movements and update the doctor every 2-3 weeks. The next visit will include additional follow-up based on baseline data. The parents are advised to stay calm and the doctor is available for further consultation if needed.
