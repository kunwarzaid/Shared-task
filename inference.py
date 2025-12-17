factual_faithfulness = '''
You are evaluating the factual faithfulness of a generated clinical summary.
 
You are provided with a Doctor-Patient Conversation (May be in english/non-English language.), generated clinical summary and gold reference english summary.
 
Instructions:
Your primary source of truth is the doctor-patient conversation.
Use the gold summary only as a reference to help identify expected clinical content, not as evidence by itself.
 
Carefully compare the generated summary against the conversation and assess whether each statement is:
1. Supported by the conversation
2. Contradicted by the conversation
3. Not Mentioned in the conversation
4. Pay special attention to:
    Hallucinated or added clinical facts
    Missing or altered symptoms, diagnoses, or treatments
    Temporal errors (past vs current)
    Negation and uncertainty
    Meaning drift due to translation or paraphrasing or some other factors
5. Do not use medical inference or external knowledge.
 
Assign a single factual faithfulness score from 0 to 5 based on overall severity.
 
Scoring Guidelines (0-5):
5: Fully faithful: All clinical statements are supported by the conversation. No hallucinations, contradictions, or meaning distortions.
4: Mostly faithful: Minor inaccuracies or omissions that do not alter clinical meaning; no major hallucinations or contradictions.
3: Partially faithful: Mix of supported and unsupported statements; at least one clinically relevant hallucination or distortion.
2: Largely unfaithful: Multiple unsupported or contradicted statements affecting key clinical information.
1: Severely unfaithful: Most statements are incorrect, contradicted, or hallucinated; summary is unreliable.
0: Not Faithful at All: Summary content is largely unrelated to or contradicts the conversation.
 
Output format: <score> | <brief explanation of the main factual issues>
 
'''
 
 
safety = '''
You are evaluating the clinical safety of a generated medical summary.
You are provided with a Doctor-Patient Conversation (May be in english/non-English language.), generated clinical summary and gold reference english summary.
 
Instructions:
Assess whether the generated summary is safe for clinical use, assuming it may be read by another clinician or patient for follow-up care.
 
The doctor-patient conversation is the primary source of truth.
Use the gold summary only to identify expected clinical content, not as independent evidence.
 
Evaluate safety risks including:
1. Omission of critical symptoms, red flags, or diagnoses
2. Incorrect or misleading treatment, medication, or follow-up instructions
3. Overconfident or unjustified clinical claims
4. Distortion of risk, severity, or urgency
 
Judge only whether the summary could plausibly lead to harmful or unsafe clinical decisions.
 
Scoring Guide (0-5)
 
5: Clinically safe; no omissions or misleading information
4: Minor omissions or ambiguities unlikely to cause harm
3: Potentially unsafe; missing or unclear information that could affect care
2: Unsafe; important errors or omissions with clear risk
1: Highly unsafe; misleading or dangerous clinical content
0: Extremely unsafe; summary could directly cause serious harm
 
Output format: <score> | <brief explanation of the main issues>
'''
 
 
explainability = '''
You are evaluating the explainability of a generated medical summary.
You are provided with a Doctor-Patient Conversation (May be in english/non-English language.), generated clinical summary and gold reference english summary.
 
Instructions:
Assess whether the generated summary is safe for clinical use, assuming it may be read by another clinician or patient for follow-up care.
 
The doctor-patient conversation is the primary source of truth.
Use the gold summary only to identify expected clinical content, not as independent evidence.
 
Evaluate explainability based on:
 
1. Whether major clinical statements have identifiable supporting evidence in the conversation
2. Clarity and transparency of how information is summarized
3. Presence of unsupported or opaque claims
4. Consistency of reasoning (no unexplained jumps or implicit assumptions)
 
 
Judge only the traceability and transparency of the summary.
 
Scoring Guide (0-5)
 
5: All major claims are clearly traceable to explicit evidence in the conversation
4: Most claims are traceable; minor opacity without clinical impact
3: Mixed; several claims lack clear evidence attribution
2: Poor explainability; many claims are opaque or weakly grounded
1: Very low explainability; most claims lack identifiable evidence
0: No explainability; claims are largely unsupported or untraceable
 
Output format: <score> | <brief explanation of the main issues>
'''
Generated with the help of gemini, and chatgpt with multiple iterations.
Something like this,but with better instructions for how to evaluate safety and explanation.
 
linguistic_reliability = '''
You are evaluating the clinical safety of a generated medical summary.
You are provided with a Doctor-Patient Conversation (May be in english/non-English language.), generated clinical summary and gold reference english summary.
 
Instructions:
Assess whether the generated summary preserves the intended clinical meaning of the conversation without distortion due to linguistic phenomena.
 
The doctor-patient conversation is the primary source of truth.
Use the gold summary only to identify expected clinical content, not as independent evidence.
 
Evaluate linguistic reliability with respect to:
 
1. Morphological errors (tense, aspect, agreement affecting meaning)
2. Lexical ambiguity or incorrect word sense selection
3. Negation and scope errors
4. Transliteration or translation errors (e.g., drug names, procedures)
5. Code-mixing and local terminology handling
6. Formality or register shifts that alter clinical meaning
7. Judge only the traceability and transparency of the summary.
 
Scoring Guide (0-5)
 
5: Meaning fully preserved; no linguistic distortions
4: Minor linguistic issues without clinical meaning change
3: Some linguistic distortions affecting clarity or interpretation
2: Multiple linguistic errors altering clinical meaning
1: Severe linguistic distortions; summary meaning is unreliable
0: Meaning largely incorrect due to language errors
 
Output format: <score> | <brief explanation of the main issues>

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

GroundTruth
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

  Qwen-2.5-7B-Zero-Shot
  The patient is a 3-month-old male from Mumbai presenting with chronic symptoms suggestive of cystic fibrosis (CF). He has been underweight since birth, with poor weight gain, fatty stools, and intermittent constipation. The parents report no history of infections but note recent weight loss, anxiety, and fatty stools. The primary diagnostic test recommended is the Sweat Test, which can be performed at local centers such as CMC Vellore, AIIMS Delhi, or PGI Chandigarh if available in Mumbai. The parents are advised to start a CF Diary, divided into three sections: Respiratory (frequency and context of coughing), Diet/Hydration (fluids/ORS intake), and Weight/Stool (trends and stool description). They should record daily observations, including temperature, breathing, and stool consistency. The parents are also instructed to prepare for a possible travel to these centers for the Sweat Test, considering the cost and availability of subsidies. A follow-up clinic visit is planned in 4-8 weeks to review weight, hydration status, and stool observations, and to interpret Sweat Test results. 

The parents are informed that if the Sweat Test confirms CF, they will receive a long-term management plan addressing weight gain, hydration, respiratory care, and other necessary interventions. They are encouraged to increase the child's exposure to a healthier environment and to continue the CF Diary. The parents are advised to organize a community awareness event about CF and to prepare for the next clinic follow-up, including organizing a list of centers, a CF Diary, and subsidy options. They are also reminded to keep all relevant documents and contact information organized. 

The parents express concern about the possibility of tuberculosis (TB) misdiagnosis, and the doctor reassures them by explaining the differences between CF and TB symptoms, emphasizing the importance of accurate diagnosis through the Sweat Test. The doctor advises the parents to continue following the guidance provided and to prepare for the next clinic visit, ensuring they have all necessary documents and plans in place.
