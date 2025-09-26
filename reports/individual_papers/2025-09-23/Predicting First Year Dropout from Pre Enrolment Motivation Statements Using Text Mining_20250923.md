---
keywords:
  - Natural Language Processing
  - Student Motivation Analysis
  - Machine Learning
  - TF-IDF
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16224
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:03:26.615208",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Natural Language Processing",
    "Student Motivation Analysis",
    "Machine Learning",
    "TF-IDF"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Natural Language Processing": 0.8,
    "Student Motivation Analysis": 0.72,
    "Machine Learning": 0.75,
    "TF-IDF": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "text mining",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP",
          "text analysis"
        ],
        "category": "broad_technical",
        "rationale": "Text mining is a key application of Natural Language Processing, which is a fundamental area in machine learning and AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "motivation statements",
        "canonical": "Student Motivation Analysis",
        "aliases": [
          "motivation letters",
          "personal statements"
        ],
        "category": "unique_technical",
        "rationale": "Analyzing motivation statements is a unique approach to predicting student dropout, offering new insights into educational data mining.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Support Vector Machines",
        "canonical": "Machine Learning",
        "aliases": [
          "SVM"
        ],
        "category": "broad_technical",
        "rationale": "Support Vector Machines are a classic machine learning technique used for classification tasks, relevant to the study's methodology.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "TFiDF",
        "canonical": "TF-IDF",
        "aliases": [
          "Term Frequency-Inverse Document Frequency"
        ],
        "category": "specific_connectable",
        "rationale": "TF-IDF is a common technique in text analysis, linking to broader applications in information retrieval and NLP.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "dropout",
      "student characteristics",
      "university"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "text mining",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "motivation statements",
      "resolved_canonical": "Student Motivation Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Support Vector Machines",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "TFiDF",
      "resolved_canonical": "TF-IDF",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Predicting First Year Dropout from Pre Enrolment Motivation Statements Using Text Mining

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16224.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16224](https://arxiv.org/abs/2509.16224)

## 🔗 유사한 논문
- [[2025-09-23/Quantifying Student Success with Generative AI_ A Monte Carlo Simulation Informed by Systematic Review_20250923|Quantifying Student Success with Generative AI: A Monte Carlo Simulation Informed by Systematic Review]] (78.4% similar)
- [[2025-09-22/Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom_20250922|Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom]] (76.6% similar)
- [[2025-09-22/KatFishNet_ Detecting LLM-Generated Korean Text through Linguistic Feature Analysis_20250922|KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis]] (75.7% similar)
- [[2025-09-23/Rethinking the Role of Text Complexity in Language Model Pretraining_20250923|Rethinking the Role of Text Complexity in Language Model Pretraining]] (75.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]], [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/TF-IDF|TF-IDF]]
**⚡ Unique Technical**: [[keywords/Student Motivation Analysis|Student Motivation Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16224v1 Announce Type: cross 
Abstract: Preventing student dropout is a major challenge in higher education and it is difficult to predict prior to enrolment which students are likely to drop out and which students are likely to succeed. High School GPA is a strong predictor of dropout, but much variance in dropout remains to be explained. This study focused on predicting university dropout by using text mining techniques with the aim of exhuming information contained in motivation statements written by students. By combining text data with classic predictors of dropout in the form of student characteristics, we attempt to enhance the available set of predictive student characteristics. Our dataset consisted of 7,060 motivation statements of students enrolling in a non-selective bachelor at a Dutch university in 2014 and 2015. Support Vector Machines were trained on 75 percent of the data and several models were estimated on the test data. We used various combinations of student characteristics and text, such as TFiDF, topic modelling, LIWC dictionary. Results showed that, although the combination of text and student characteristics did not improve the prediction of dropout, text analysis alone predicted dropout similarly well as a set of student characteristics. Suggestions for future research are provided.

## 📝 요약

이 연구는 대학 중퇴 예측을 위해 학생들이 작성한 동기부여서를 텍스트 마이닝 기법으로 분석했습니다. 기존의 중퇴 예측 요소인 학생 특성과 텍스트 데이터를 결합하여 예측력을 높이고자 했습니다. 네덜란드 대학의 비선별적 학사 과정에 등록한 학생 7,060명의 동기부여서를 대상으로 하여, 75%의 데이터를 학습시킨 후 다양한 모델을 테스트했습니다. 텍스트 분석 기법으로는 TFiDF, 주제 모델링, LIWC 사전을 사용했습니다. 연구 결과, 텍스트와 학생 특성의 결합이 중퇴 예측을 향상시키지는 않았지만, 텍스트 분석만으로도 학생 특성 세트와 유사한 수준의 예측력을 보였습니다. 향후 연구 방향에 대한 제언도 포함되어 있습니다.

## 🎯 주요 포인트

- 1. 고등학교 GPA는 대학 중퇴를 예측하는 강력한 지표이지만, 중퇴의 많은 변동성을 설명하지 못한다.
- 2. 본 연구는 학생들이 작성한 동기 부여 진술서의 정보를 활용하여 텍스트 마이닝 기법으로 대학 중퇴를 예측하고자 했다.
- 3. 텍스트 데이터와 학생 특성이라는 고전적 중퇴 예측 지표를 결합하여 예측력을 향상시키려는 시도를 했다.
- 4. 텍스트 분석만으로도 학생 특성을 이용한 예측과 유사한 수준으로 중퇴를 예측할 수 있었다.
- 5. 텍스트와 학생 특성의 결합이 중퇴 예측을 향상시키지는 못했지만, 향후 연구에 대한 제안을 제공했다.


---

*Generated on 2025-09-24 02:03:26*