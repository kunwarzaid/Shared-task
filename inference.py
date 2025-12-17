

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

Ground Truth
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

Qwen-2.5-7B-Instruct-zero-shot
The patient is a 4-month-old male infant presenting with chronic cough and poor weight gain since birth. The parents report that the child has had intermittent loose stools, which have become more frequent. The child was diagnosed with Cystic Fibrosis (CF) through autosomal recessive inheritance. The parents are seeking information about CF and its management. They are unsure if the child's condition has worsened recently. CF can lead to respiratory complications, including meconium ileus. The child had no bowel movements shortly after birth, and currently, the child is breathing normally with routine oxygen supplementation. There is no fever, and the child is not traveling to the city for a sweat test at AIIMS, Pune, due to financial constraints. The parents are unaware of the procedure for the sweat test and seek guidance on how to prepare for it. 

The management plan includes regular monitoring of weight, height, diet, and respiratory status. The parents should prepare for the sweat test by collecting a small sample of sweat from the arm. They should also track the child’s weight daily and maintain a balanced diet to promote healthy growth. If travel to the city is necessary, they may apply for government subsidies or assistance programs. The parents should gather all required documents such as Aadhar card, ration card, village address, mobile number, and health insurance documents. They should also consider seeking help from the primary healthcare center in their village. Regular follow-ups are recommended every two months to monitor the child’s progress and adjust the treatment plan based on the sweat test results. If the sweat test is negative, the likelihood of CF decreases, but other causes should be considered. If positive, a multidisciplinary team involving pulmonologists, nutritionists, and physiotherapists will be involved in the management plan. The cost of treatment can be managed through government schemes and subsidies. The parents should prepare for the sweat test by measuring the child’s weight in the morning, avoiding heavy meals, and following the doctor’s instructions. If the sweat test is negative, further steps include genetic counseling. If positive, the management plan will focus on nutrition, respiratory care, infection control, and genetic counseling. 

The parents are advised to keep the child hydrated and maintain a balanced diet. They should also be aware of signs of worsening condition such as shortness of breath, weight loss, or changes in bowel habits. They should contact the doctor immediately if any of these symptoms occur. The weather being hot, they should ensure the child stays well-hydrated and plan accordingly

