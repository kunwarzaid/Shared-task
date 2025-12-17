

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
Ground Truth
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

Qwen-2.5-7B-Instruct-zero-shot
Mr. Rajesh Patel, 52 years old from Mumbai, presents with throat pain, voice change, difficulty swallowing, night sweats, and weight loss. He is a known smoker and uses tobacco and spices. The patient seeks evaluation for possible head and neck cancer. An HPV test is recommended to assess risk. The baseline tests include blood work, dental examination, imaging (CT/MRI), and endoscopy preparation. The MDT (Multidisciplinary Team) meeting is scheduled for two weeks later to discuss staging, treatment options, and further steps based on initial test results. 

The patient asks about the timing of HPV testing and further investigations. The baseline tests are completed within two weeks, including blood work, dental status, imaging, and endoscopy preparation. The MDT meeting is set for two weeks after baseline results to determine staging and next steps. The patient inquires about the impact of HPV status on staging and prognosis. HPV positivity may influence treatment decisions, but final staging is determined by the MDT considering multiple factors.

The patient asks about the role of chemotherapy and radiation in advanced stages. Surgery, followed by radiation, is common for advanced cases, with chemotherapy added in some cases. The MDT will decide on the exact treatment plan. The patient inquires about the specifics of surgery, including lymph node removal and reconstruction. Radiation involves daily sessions over 6-7 weeks, with potential side effects like skin irritation and reduced appetite. Chemotherapy dosage and side effects are discussed, with local iodine application considered in certain cases.

The patient asks about financial assistance and insurance coverage. Government schemes like Ayushman Bharat and state programs may cover costs. The MDT team coordinates follow-up visits and provides plain-language explanations to the patient and family. The patient inquires about the availability of MRI scans and suitable centers in Mumbai. The MDT provides a list of local facilities.

The patient asks about the MDT's role in decision-making and coordination. The MDT team includes surgeons, oncologists, dietitians, and therapists who work together on the patient's case. The patient inquires about the MDT's communication and coordination methods. The MDT team uses plain-language to explain complex medical concepts to the patient and family.

The patient asks about the MDT's decision-making process and timeline. The MDT meeting is scheduled based on baseline results, with family members potentially involved. The patient inquires about the MDT's role in decision-making and coordination. The MDT team coordinates follow-up visits and provides plain
