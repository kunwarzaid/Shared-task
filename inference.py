

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

Ground Truth
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

Qwen-2.5-7B-Instruct-zero-shot
The patient is a 3-month-old male infant who has been underweight since birth, with poor weight gain, excessive sweating, and persistent cough. The mother reports that he sweats more in cooler temperatures and at night. The child has a stevie (a type of cystic fibrosis-related lung infection). The mother has started a CF (Cystic Fibrosis) diary to track respiratory symptoms, hydration, and weight/stool changes over three days. 

The doctor recommends completing the short-form diary for three days, noting times of coughing, temperature, and respiration. A sweat test is planned to confirm CF, as it is an important diagnostic tool. The nearest facility for this test is CMC Vellore, with other options being AIIMS and PGI Chandigarh. Follow-ups are scheduled every four weeks, with the next one in two weeks.

The family will explore travel subsidies for the trip. The doctor advises on travel safety and COVID protocols. The child's weight was 5400g, and today's weight will be measured again. Stool consistency remains oily, though slightly less than before. ORS (Oral Rehydration Solution) is given three times daily, along with adequate fluids and calories.

Genetic counseling is discussed to understand the benefits and risks of carrier testing for parents. If the child is diagnosed with CF, parents can be screened to make future decisions. The family will visit CMC Vellore for the sweat test, and the doctor will provide necessary information for booking. Travel logistics and safety measures are discussed.

The next follow-up will assess weight, hydration, and stool status, with the sweat test completed. The family will finalize travel plans and book the sweat test. The doctor emphasizes the importance of raising awareness about CF in the community. The next clinic visit will evaluate the child's condition based on the diary entries and sweat test results.

In conclusion, the child shows signs consistent with CF, and further diagnostic steps are being taken. The family is advised to continue the CF diary and prepare for travel. The doctor will monitor the child's progress and adjust the management plan accordingly.
