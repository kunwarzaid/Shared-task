

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

Ground Truth
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

Qwen-2.5-7B-Instruct-zero-shot
Dr. Ahare is following up with Rajesh Patel, a 52-year-old male from Mumbai who has completed chemotherapy and radiotherapy and is in the recovery phase. Rajesh reports feeling fatigued, difficulty swallowing, and weight loss. The follow-up involves a trimeal follow-up, where an MDT (Multidisciplinary Team) makes decisions based on physical examination, lab tests, and imaging to formulate a plan.

Rajesh mentions experiencing fatigue more than usual, difficulty eating, and some difficulty speaking. To reduce fatigue, he needs to consume energy-rich food, engage in light exercise, and undergo swallowing therapy. Speech therapy starts as needed, and home-based exercises are provided for the affected muscles. The speech therapist initiates speech therapy when ready and provides guidance on daily activities like speaking and eating.

Rajesh is considering tube feeding if oral intake remains low for an extended period. He should maintain a soft, high-protein, high-calorie diet, consuming small meals every two to three hours. He should drink at least 2-3 liters of water daily to aid weight gain. For protein supplementation, he can consider protein shakes if needed. Regular meal timings are important.

Rajesh's family is involved in his care, and Dr. Ahare emphasizes the importance of family support. They discuss household arrangements, including managing cooking, travel, and cleanliness. They recommend quitting smoking and alcohol completely and provide resources for support groups and nicotine replacement therapy.

For home-based care, they suggest a structured meal plan including protein-rich foods, soft foods, fruits, and adequate hydration. If any discomfort occurs, Rajesh should contact the clinic immediately. MDT meetings occur every three months to review reports online and provide further care plans.

To improve swallowing issues at home, they advise drinking small amounts of water, eating soft foods, and performing gentle exercises. For dry mouth, they recommend using mouth moisturizers and sipping water regularly. They will provide necessary medications as per the doctor's advice.

They also discuss maintaining a routine and being prepared for any discomfort. They will assist with travel if needed and ensure clear understanding of the care plan. They will prepare a detailed care plan for the next visit, which will be online and clear. If any questions arise, they can be answered via tele-consultation or phone.

The follow-up will continue for the long term, ensuring Rajesh's safety and well-being through regular check-ups. The next visit is scheduled in three months, and they will review online reports and clarify any doubts
