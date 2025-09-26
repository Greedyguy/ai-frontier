---
keywords:
  - Machine Learning
  - Universal Sentence Encoder
  - Support Vector Machine
  - Temporal Analysis
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16014
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:40:12.909843",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Universal Sentence Encoder",
    "Support Vector Machine",
    "Temporal Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Universal Sentence Encoder": 0.78,
    "Support Vector Machine": 0.8,
    "Temporal Analysis": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Central to the system's classification and analysis capabilities.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Universal Sentence Encoder",
        "canonical": "Universal Sentence Encoder",
        "aliases": [
          "USE"
        ],
        "category": "unique_technical",
        "rationale": "Key component for feature extraction in the proposed system.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Support Vector Machine",
        "canonical": "Support Vector Machine",
        "aliases": [
          "SVM"
        ],
        "category": "specific_connectable",
        "rationale": "Used for classification in the system, linking to machine learning methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Temporal Analysis",
        "canonical": "Temporal Analysis",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Essential for understanding trends and changes in attitudes over time.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "extremism",
      "terrorism",
      "dataset",
      "tracking"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Universal Sentence Encoder",
      "resolved_canonical": "Universal Sentence Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Support Vector Machine",
      "resolved_canonical": "Support Vector Machine",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Temporal Analysis",
      "resolved_canonical": "Temporal Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Predicting the descent into extremism and terrorism

**Korean Title:** 극단주의와 테러리즘으로의 추락 예측

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16014.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16014](https://arxiv.org/abs/2509.16014)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (79.2% similar)
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (79.0% similar)
- [[2025-09-18/BERTector_ An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (79.0% similar)
- [[2025-09-22/A Weak Supervision Approach for Monitoring Recreational Drug Use Effects in Social Media_20250922|A Weak Supervision Approach for Monitoring Recreational Drug Use Effects in Social Media]] (78.9% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Support Vector Machine|Support Vector Machine]]
**⚡ Unique Technical**: [[keywords/Universal Sentence Encoder|Universal Sentence Encoder]], [[keywords/Temporal Analysis|Temporal Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16014v1 Announce Type: new 
Abstract: This paper proposes an approach for automatically analysing and tracking statements in material gathered online and detecting whether the authors of the statements are likely to be involved in extremism or terrorism. The proposed system comprises: online collation of statements that are then encoded in a form amenable to machine learning (ML), an ML component to classify the encoded text, a tracker, and a visualisation system for analysis of results. The detection and tracking concept has been tested using quotes made by terrorists, extremists, campaigners, and politicians, obtained from wikiquote.org. A set of features was extracted for each quote using the state-of-the-art Universal Sentence Encoder (Cer et al. 2018), which produces 512-dimensional vectors. The data were used to train and test a support vector machine (SVM) classifier using 10-fold cross-validation. The system was able to correctly detect intentions and attitudes associated with extremism 81% of the time and terrorism 97% of the time, using a dataset of 839 quotes. This accuracy was higher than that which was achieved for a simple baseline system based on n-gram text features. Tracking techniques were also used to perform a temporal analysis of the data, with each quote considered to be a noisy measurement of a person's state of mind. It was demonstrated that the tracking algorithms were able to detect both trends over time and sharp changes in attitude that could be attributed to major events.

## 🔍 Abstract (한글 번역)

arXiv:2509.16014v1 발표 유형: 신규  
초록: 본 논문은 온라인에서 수집된 자료의 진술을 자동으로 분석하고 추적하여, 진술의 작성자가 극단주의나 테러리즘에 관여할 가능성이 있는지를 탐지하는 접근법을 제안한다. 제안된 시스템은 다음을 포함한다: 온라인에서 수집된 진술을 기계 학습(ML)에 적합한 형태로 인코딩, 인코딩된 텍스트를 분류하는 ML 구성 요소, 추적기, 그리고 결과 분석을 위한 시각화 시스템. 탐지 및 추적 개념은 wikiquote.org에서 얻은 테러리스트, 극단주의자, 운동가, 정치인의 인용문을 사용하여 테스트되었다. 각 인용문에 대해 최첨단의 Universal Sentence Encoder(Cer et al. 2018)를 사용하여 512차원 벡터로 특징을 추출하였다. 이 데이터는 10겹 교차 검증을 사용하여 서포트 벡터 머신(SVM) 분류기를 훈련하고 테스트하는 데 사용되었다. 이 시스템은 839개의 인용문 데이터셋을 사용하여 극단주의와 관련된 의도와 태도를 81%의 정확도로, 테러리즘과 관련된 의도와 태도를 97%의 정확도로 올바르게 탐지할 수 있었다. 이 정확도는 n-그램 텍스트 특징에 기반한 단순한 기준 시스템보다 높은 것이었다. 또한, 추적 기술을 사용하여 데이터를 시간적으로 분석하였으며, 각 인용문은 개인의 정신 상태에 대한 잡음이 있는 측정값으로 간주되었다. 추적 알고리즘이 시간이 지남에 따라 나타나는 경향과 주요 사건에 기인할 수 있는 급격한 태도 변화를 모두 탐지할 수 있음을 입증하였다.

## 📝 요약

이 논문은 온라인에서 수집된 자료를 자동으로 분석하고 추적하여 작성자가 극단주의나 테러에 연루될 가능성을 감지하는 시스템을 제안합니다. 시스템은 온라인에서 문장을 수집하고, 이를 기계 학습에 적합한 형태로 인코딩한 후, 기계 학습을 통해 분류합니다. 또한, 추적 및 시각화 시스템을 통해 결과를 분석합니다. wikiquote.org에서 수집한 테러리스트, 극단주의자, 운동가, 정치인의 인용문을 사용하여 테스트했으며, Universal Sentence Encoder를 활용해 512차원 벡터로 특징을 추출했습니다. 839개의 인용문을 사용하여 SVM 분류기를 10겹 교차 검증으로 훈련하고 테스트한 결과, 극단주의 관련 의도를 81%, 테러 관련 의도를 97% 정확도로 감지했습니다. 이는 n-gram 기반의 단순한 시스템보다 높은 정확도입니다. 또한, 추적 기법을 통해 시간에 따른 데이터의 경향성과 주요 사건에 따른 급격한 태도 변화를 감지할 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. 본 논문은 온라인에서 수집된 자료의 발언을 자동으로 분석하고 추적하여, 발언자가 극단주의나 테러에 연루될 가능성을 탐지하는 시스템을 제안합니다.
- 2. 제안된 시스템은 발언을 기계 학습에 적합한 형태로 인코딩하고, 이를 분류하는 ML 컴포넌트, 추적기, 결과 분석을 위한 시각화 시스템으로 구성됩니다.
- 3. Universal Sentence Encoder를 사용하여 각 인용문에서 특징을 추출하고, SVM 분류기를 통해 10겹 교차 검증으로 극단주의와 테러 관련 의도를 각각 81%, 97%의 정확도로 탐지했습니다.
- 4. 추적 기법을 통해 시간에 따른 데이터의 경향성과 주요 사건에 기인한 급격한 태도 변화를 감지할 수 있음을 입증했습니다.


---

*Generated on 2025-09-23 10:40:12*