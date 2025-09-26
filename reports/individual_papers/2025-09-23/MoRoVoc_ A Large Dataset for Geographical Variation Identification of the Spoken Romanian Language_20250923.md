---
keywords:
  - MoRoVoc Dataset
  - Adversarial Training
  - Wav2Vec2
  - Meta-Learning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16781
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:18:51.901678",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MoRoVoc Dataset",
    "Adversarial Training",
    "Wav2Vec2",
    "Meta-Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MoRoVoc Dataset": 0.8,
    "Adversarial Training": 0.85,
    "Wav2Vec2": 0.78,
    "Meta-Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MoRoVoc",
        "canonical": "MoRoVoc Dataset",
        "aliases": [
          "MoRoVoc"
        ],
        "category": "unique_technical",
        "rationale": "A unique dataset for Romanian language variation, crucial for linking regional linguistic studies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-target adversarial training",
        "canonical": "Adversarial Training",
        "aliases": [
          "multi-target adversarial training"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to adversarial methods in machine learning, enhancing model robustness.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Wav2Vec2-Base",
        "canonical": "Wav2Vec2",
        "aliases": [
          "Wav2Vec2-Base",
          "Wav2Vec2-Large"
        ],
        "category": "specific_connectable",
        "rationale": "Links to self-supervised learning models for speech processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "meta-learning",
        "canonical": "Meta-Learning",
        "aliases": [
          "meta-learning"
        ],
        "category": "specific_connectable",
        "rationale": "Facilitates connections to learning paradigms that optimize model adaptation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "audio samples",
      "demographic attributes"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MoRoVoc",
      "resolved_canonical": "MoRoVoc Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-target adversarial training",
      "resolved_canonical": "Adversarial Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Wav2Vec2-Base",
      "resolved_canonical": "Wav2Vec2",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "meta-learning",
      "resolved_canonical": "Meta-Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MoRoVoc: A Large Dataset for Geographical Variation Identification of the Spoken Romanian Language

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16781.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16781](https://arxiv.org/abs/2509.16781)

## 🔗 유사한 논문
- [[2025-09-22/Evaluating Multimodal Large Language Models on Spoken Sarcasm Understanding_20250922|Evaluating Multimodal Large Language Models on Spoken Sarcasm Understanding]] (78.6% similar)
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (78.5% similar)
- [[2025-09-17/Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications_20250917|Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications]] (78.2% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (78.1% similar)
- [[2025-09-23/CAARMA_ Class Augmentation with Adversarial Mixup Regularization_20250923|CAARMA: Class Augmentation with Adversarial Mixup Regularization]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Adversarial Training|Adversarial Training]], [[keywords/Wav2Vec2|Wav2Vec2]], [[keywords/Meta-Learning|Meta-Learning]]
**⚡ Unique Technical**: [[keywords/MoRoVoc Dataset|MoRoVoc Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16781v1 Announce Type: new 
Abstract: This paper introduces MoRoVoc, the largest dataset for analyzing the regional variation of spoken Romanian. It has more than 93 hours of audio and 88,192 audio samples, balanced between the Romanian language spoken in Romania and the Republic of Moldova. We further propose a multi-target adversarial training framework for speech models that incorporates demographic attributes (i.e., age and gender of the speakers) as adversarial targets, making models discriminative for primary tasks while remaining invariant to secondary attributes. The adversarial coefficients are dynamically adjusted via meta-learning to optimize performance. Our approach yields notable gains: Wav2Vec2-Base achieves 78.21% accuracy for the variation identification of spoken Romanian using gender as an adversarial target, while Wav2Vec2-Large reaches 93.08% accuracy for gender classification when employing both dialect and age as adversarial objectives.

## 📝 요약

이 논문은 루마니아어의 지역적 변이를 분석하기 위한 최대 규모의 데이터셋인 MoRoVoc를 소개합니다. 이 데이터셋은 루마니아와 몰도바에서 사용되는 루마니아어를 균형 있게 포함하며, 93시간 이상의 오디오와 88,192개의 오디오 샘플로 구성되어 있습니다. 연구에서는 연령과 성별 같은 인구통계적 속성을 대립적 목표로 삼아 음성 모델을 훈련하는 다중 목표 대립 학습 프레임워크를 제안합니다. 메타 학습을 통해 대립 계수를 동적으로 조정하여 성능을 최적화합니다. 이 접근법은 성별을 대립 목표로 사용할 때 Wav2Vec2-Base 모델이 78.21%의 변이 식별 정확도를, 방언과 연령을 대립 목표로 사용할 때 Wav2Vec2-Large 모델이 93.08%의 성별 분류 정확도를 달성하는 등 주목할 만한 성과를 보였습니다.

## 🎯 주요 포인트

- 1. MoRoVoc는 루마니아어의 지역 변이를 분석하기 위한 가장 큰 데이터셋으로, 루마니아와 몰도바에서 사용되는 루마니아어를 균형 있게 포함하고 있습니다.
- 2. 제안된 다중 목표 적대적 학습 프레임워크는 연령과 성별 같은 인구통계학적 속성을 적대적 목표로 사용하여 모델이 주요 작업에 대해 차별성을 가지면서도 부차적 속성에 대해 불변성을 유지하도록 합니다.
- 3. 적대적 계수는 메타 학습을 통해 동적으로 조정되어 성능을 최적화합니다.
- 4. Wav2Vec2-Base 모델은 성별을 적대적 목표로 사용하여 루마니아어 변이 식별에서 78.21%의 정확도를 달성하였고, Wav2Vec2-Large 모델은 방언과 연령을 적대적 목표로 사용하여 성별 분류에서 93.08%의 정확도를 기록했습니다.


---

*Generated on 2025-09-24 03:18:51*