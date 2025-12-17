

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
Ground Truth
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
Qwen-2.5-7B-Instruct-zero-shot
The patient is a 3-month-old male child, Ajay, from a rural family in India. He has been experiencing poor weight gain, intermittent diarrhea, and greasy stools. The parents suspect cystic fibrosis (CF) and have undergone a sweat test, which was positive. Genetic counseling has been initiated, and regular monitoring of growth will be conducted. The sweat test was performed at a nearby hospital and took 1-3 days to complete. The parents plan to travel to the city for further treatment and have arranged for a road trip. They will keep a log of the child's weight, feeding, and stool characteristics daily. 

Management includes pancreatic enzyme replacement therapy as needed based on the child's feeding and weight. The parents will perform chest physiotherapy (CPT) at home, with guidance from a nurse program. They are advised to engage in daily exercises and activities suitable for the child's age, such as walking and playing, to help clear mucus. Regular follow-ups are planned every 2-3 months, either in person or via phone/WhatsApp, depending on the distance. For long-distance travel, alternative arrangements like accommodation assistance may be provided if needed.

For travel documentation, proof of identity, birth certificate, weight, doctor's contact information, and dietary habits are required. The parents will provide all necessary documents, including the child's weight history. The sweat test result will require a signed consent form. The diet should include high-calorie Indian foods to support growth. Specific high-calorie foods include chawal (rice), ghee (clarified butter), and balanced with milk, water, and salt. The parents will continue to monitor the child's weight and feeding habits regularly.

If the sweat test confirms CF, a specialized CF treatment plan will be implemented. If negative, standard growth monitoring will continue with regular follow-ups. The parents can share data via WhatsApp, including weight, feeding, and bowel movements. Local health centers can arrange weight checks for the child when they visit the city. The CF program can provide support and resources, including structural support and financial aid, through the state health department. The parents will prepare necessary documents before traveling to the clinic.

The final plan will be finalized after the sweat test results, which will take about 2 weeks. The parents will continue to prepare for the journey and adapt to the new environment, including school and social interactions. The child will attend school and learn while the parents adjust to their new surroundings. The parents will receive further instructions based on the sweat test
