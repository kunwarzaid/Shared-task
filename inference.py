

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

Ground Truth
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

Qwen-2.5-7B-Instruct-zero-shot
The patient, Rajesh Patel, 45 years old, from Mumbai, reports symptoms of weight loss, hoarseness, difficulty swallowing, and reduced appetite for several months. He has a history of long-term tobacco use (tobacco chewing and pan masala), occasional alcohol consumption, and no known Human Papillomavirus (HPV) infection. The patient is scheduled for a biopsy, followed by CT/MRI within 2-3 days. Family members will accompany him to all medical appointments.

The patient's primary concerns include understanding the process and preparing for the biopsy. He mentions experiencing pain during the procedure, which would be managed with local anesthesia. The patient also discusses potential nutritional support due to weight loss and difficulty eating. He inquires about quitting smoking and the role of family support in this process.

The patient is concerned about the staging of his condition and the implications for treatment decisions. He asks about the role of HPV testing and its impact on tumor staging and treatment options. The doctor explains that while HPV status can influence treatment decisions, the final decision is based on multiple factors including imaging results and biopsy findings.

The patient is scheduled for baseline tests over the next two weeks, after which an MDT (Multidisciplinary Team) meeting will review the results and determine the stage of the tumor. Based on the stage, surgical intervention, radiotherapy, or combination therapy may be recommended. The patient is advised to maintain a high-protein diet, stay hydrated, and consume high-calorie snacks to aid in weight gain and recovery.

Nutritional support is emphasized, and the patient is referred to a nutritionist for personalized dietary advice. The patient inquires about the logistics of participating in clinical trials through the Ayushman Bharat program and the necessary documentation required for such trials.

MDT meetings are scheduled for the following month, and the patient is encouraged to prepare all necessary documents in advance. The patient expresses gratitude for the clear communication and requests further clarification on medical terms and procedures. The doctor provides a list of clinical terms and diagrams to assist in understanding.

The patient is advised to follow up with the MDT team regarding the biopsy results, which are expected within 2-5 days. The patient is reassured that the MDT will provide updates and guidance throughout the process. The patient is reminded to ask any questions at any time and to refer to checklists, forms, and MDT notes for further information.
