---
keywords:
  - Large Language Model
  - Fair Machine Learning
  - Demographic Parity
  - Equal Opportunity
  - KL-divergence
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15759
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:12:31.613368",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Fair Machine Learning",
    "Demographic Parity",
    "Equal Opportunity",
    "KL-divergence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Fair Machine Learning": 0.78,
    "Demographic Parity": 0.8,
    "Equal Opportunity": 0.77,
    "KL-divergence": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on steering representations to achieve fairness.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Fair Machine Learning",
        "canonical": "Fair Machine Learning",
        "aliases": [
          "Fair ML"
        ],
        "category": "unique_technical",
        "rationale": "Focus of the paper is on achieving fairness in machine learning models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Demographic Parity",
        "canonical": "Demographic Parity",
        "aliases": [
          "Demographic Fairness"
        ],
        "category": "specific_connectable",
        "rationale": "A key fairness criterion discussed in the context of the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Equal Opportunity",
        "canonical": "Equal Opportunity",
        "aliases": [
          "Equalized Odds"
        ],
        "category": "specific_connectable",
        "rationale": "Another fairness criterion that is crucial for the paper's objectives.",
        "novelty_score": 0.58,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "KL-divergence",
        "canonical": "KL-divergence",
        "aliases": [
          "Kullback-Leibler Divergence"
        ],
        "category": "specific_connectable",
        "rationale": "Used in the optimization process for steering distributions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "bias",
      "utility",
      "optimization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Fair Machine Learning",
      "resolved_canonical": "Fair Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Demographic Parity",
      "resolved_canonical": "Demographic Parity",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Equal Opportunity",
      "resolved_canonical": "Equal Opportunity",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "KL-divergence",
      "resolved_canonical": "KL-divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# On Optimal Steering to Achieve Exact Fairness

**Korean Title:** 정확한 공정성을 달성하기 위한 최적 조정에 관하여

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15759.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15759](https://arxiv.org/abs/2509.15759)

## 🔗 유사한 논문
- [[2025-09-22/Beyond Linear Steering_ Unified Multi-Attribute Control for Language Models_20250922|Beyond Linear Steering: Unified Multi-Attribute Control for Language Models]] (85.2% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (84.2% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (83.7% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (83.7% similar)
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Demographic Parity|Demographic Parity]], [[keywords/Equal Opportunity|Equal Opportunity]], [[keywords/KL-divergence|KL-divergence]]
**⚡ Unique Technical**: [[keywords/Fair Machine Learning|Fair Machine Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15759v1 Announce Type: cross 
Abstract: To fix the 'bias in, bias out' problem in fair machine learning, it is important to steer feature distributions of data or internal representations of Large Language Models (LLMs) to ideal ones that guarantee group-fair outcomes. Previous work on fair generative models and representation steering could greatly benefit from provable fairness guarantees on the model output. We define a distribution as ideal if the minimizer of any cost-sensitive risk on it is guaranteed to have exact group-fair outcomes (e.g., demographic parity, equal opportunity)-in other words, it has no fairness-utility trade-off. We formulate an optimization program for optimal steering by finding the nearest ideal distribution in KL-divergence, and provide efficient algorithms for it when the underlying distributions come from well-known parametric families (e.g., normal, log-normal). Empirically, our optimal steering techniques on both synthetic and real-world datasets improve fairness without diminishing utility (and sometimes even improve utility). We demonstrate affine steering of LLM representations to reduce bias in multi-class classification, e.g., occupation prediction from a short biography in Bios dataset (De-Arteaga et al.). Furthermore, we steer internal representations of LLMs towards desired outputs so that it works equally well across different groups.

## 🔍 Abstract (한글 번역)

arXiv:2509.15759v1 발표 유형: 교차  
초록: 공정한 기계 학습에서 '편향 입력, 편향 출력' 문제를 해결하기 위해서는 데이터의 특성 분포나 대형 언어 모델(LLM)의 내부 표현을 그룹 공정한 결과를 보장하는 이상적인 분포로 조정하는 것이 중요합니다. 공정 생성 모델과 표현 조정에 관한 이전 연구는 모델 출력에 대한 증명 가능한 공정성 보장을 통해 크게 이익을 얻을 수 있습니다. 우리는 비용 민감 위험의 최소화가 정확한 그룹 공정 결과(예: 인구 통계적 동등성, 기회 균등)를 보장하는 경우, 분포를 이상적이라고 정의합니다. 즉, 공정성과 유용성 간의 상충 관계가 없습니다. 우리는 KL-발산에서 가장 가까운 이상적인 분포를 찾아 최적의 조정을 위한 최적화 프로그램을 수립하고, 기본 분포가 잘 알려진 모수적 가족(예: 정규 분포, 로그 정규 분포)에서 나올 때 이를 위한 효율적인 알고리즘을 제공합니다. 경험적으로, 합성 및 실제 데이터셋에 대한 우리의 최적 조정 기술은 유용성을 저하시키지 않으면서 공정성을 향상시키며, 때로는 유용성을 향상시키기도 합니다. 우리는 LLM 표현의 아핀 조정을 통해 다중 클래스 분류에서의 편향을 줄이는 것을 시연합니다. 예를 들어, Bios 데이터셋(De-Arteaga et al.)에서 짧은 전기를 통한 직업 예측에서의 편향을 줄입니다. 또한, 우리는 LLM의 내부 표현을 원하는 출력으로 조정하여 서로 다른 그룹에서 동일하게 잘 작동하도록 합니다.

## 📝 요약

이 논문은 공정한 기계 학습에서 '편향된 입력은 편향된 출력으로 이어진다'는 문제를 해결하기 위해, 데이터의 특징 분포나 대형 언어 모델(LLM)의 내부 표현을 이상적인 분포로 조정하는 방법을 제안합니다. 이상적인 분포란 비용 민감 위험의 최소화가 정확한 그룹 공정성을 보장하는 분포로 정의됩니다. 저자들은 KL-발산을 이용해 최적의 분포 조정을 위한 최적화 프로그램을 수립하고, 잘 알려진 매개변수 분포에서 효율적인 알고리즘을 제공합니다. 실험 결과, 제안된 방법은 합성 및 실제 데이터셋에서 공정성을 개선하면서도 유용성을 저하시키지 않으며, 때로는 유용성을 향상시키기도 합니다. 특히, LLM의 표현을 조정하여 직업 예측과 같은 다중 클래스 분류에서 편향을 줄이는 방법을 입증하였습니다.

## 🎯 주요 포인트

- 1. 공정한 머신러닝에서 'bias in, bias out' 문제를 해결하기 위해 데이터의 특징 분포나 대형 언어 모델(LLM)의 내부 표현을 그룹 공정한 결과를 보장하는 이상적인 분포로 조정하는 것이 중요합니다.
- 2. 이상적인 분포는 비용 민감 위험의 최소화가 정확한 그룹 공정 결과를 보장하는 분포로, 공정성과 유틸리티 간의 트레이드오프가 없습니다.
- 3. KL-발산에서 가장 가까운 이상적인 분포를 찾는 최적화 프로그램을 공식화하고, 잘 알려진 파라메트릭 분포군(예: 정규 분포, 로그 정규 분포)에서 효율적인 알고리즘을 제공합니다.
- 4. 합성 및 실제 데이터셋에서 최적의 조정 기술을 사용하여 공정성을 개선하면서 유틸리티를 감소시키지 않으며, 때로는 유틸리티를 향상시키기도 합니다.
- 5. LLM의 내부 표현을 원하는 출력으로 조정하여 다양한 그룹에서 동일하게 잘 작동하도록 하고, 예를 들어 Bios 데이터셋의 직업 예측에서 편향을 줄이기 위한 LLM 표현의 아핀 조정을 시연합니다.


---

*Generated on 2025-09-23 09:12:31*