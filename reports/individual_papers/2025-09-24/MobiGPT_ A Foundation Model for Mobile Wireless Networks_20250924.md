<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:48:39.058544",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MobiGPT",
    "soft-prompt learning",
    "Zero-Shot Learning",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MobiGPT": 0.85,
    "soft-prompt learning": 0.78,
    "Zero-Shot Learning": 0.82,
    "Few-Shot Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MobiGPT",
        "canonical": "MobiGPT",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "MobiGPT is a novel foundation model specifically designed for mobile data forecasting, offering a unique contribution to the field.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "soft-prompt learning",
        "canonical": "soft-prompt learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific learning method introduced in the paper, enhancing model adaptability across different data types.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "ZSL"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a trending topic that connects well with the model's ability to generalize in unseen scenarios.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Few-Shot Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "FSL"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is relevant to the model's performance in limited-data scenarios, enhancing its connectivity.",
        "novelty_score": 0.45,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "mobile networks",
      "forecasting accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MobiGPT",
      "resolved_canonical": "MobiGPT",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "soft-prompt learning",
      "resolved_canonical": "soft-prompt learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Few-Shot Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MobiGPT: A Foundation Model for Mobile Wireless Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18166.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18166](https://arxiv.org/abs/2509.18166)

## 🔗 유사한 논문
- [[2025-09-24/Accurate and Efficient Prediction of Wi-Fi Link Quality Based on Machine Learning_20250924|Accurate and Efficient Prediction of Wi-Fi Link Quality Based on Machine Learning]] (81.7% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (81.0% similar)
- [[2025-09-24/MobileRL_ Online Agentic Reinforcement Learning for Mobile GUI Agents_20250924|MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents]] (81.0% similar)
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (80.8% similar)
- [[2025-09-23/TSGym_ Design Choices for Deep Multivariate Time-Series Forecasting_20250923|TSGym: Design Choices for Deep Multivariate Time-Series Forecasting]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/MobiGPT|MobiGPT]], [[keywords/soft-prompt learning|soft-prompt learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18166v1 Announce Type: new 
Abstract: With the rapid development of mobile communication technologies, future mobile networks will offer vast services and resources for commuting, production, daily life, and entertainment. Accurate and efficient forecasting of mobile data (e.g., cell traffic, user behavior, channel quality) helps operators monitor network state changes, orchestrate wireless resources, and schedule infrastructure and users, thereby improving supply efficiency and service quality. However, current forecasting paradigms rely on customized designs with tailored models for exclusive data types. Such approaches increase complexity and deployment costs under large-scale, heterogeneous networks involving base stations, users, and channels. In this paper, we design a foundation model for mobile data forecasting, MobiGPT, with a unified structure capable of forecasting three data types: base station traffic, user app usage, and channel quality. We propose a soft-prompt learning method to help the model understand features of different data types, and introduce a temporal masking mechanism to guide the model through three forecasting tasks: short-term prediction, long-term prediction, and distribution generation, supporting diverse optimization scenarios. Evaluations on real-world datasets with over 100,000 samples show that MobiGPT achieves accurate multi-type forecasting. Compared to existing models, it improves forecasting accuracy by 27.37%, 20.08%, and 7.27%, reflecting strong generalization. Moreover, MobiGPT exhibits superior zero/few-shot performance in unseen scenarios, with over 21.51% improvement, validating its strong transferability as a foundation model.

## 📝 요약

이 논문에서는 모바일 데이터 예측을 위한 통합 모델인 MobiGPT를 제안합니다. 기존 예측 모델은 특정 데이터 유형에 맞춘 설계로 복잡성과 비용이 증가하는 문제를 해결하기 위해, MobiGPT는 기지국 트래픽, 사용자 앱 사용량, 채널 품질 등 세 가지 데이터 유형을 예측할 수 있는 통합 구조를 갖추고 있습니다. 소프트 프롬프트 학습 방법과 시간 마스킹 메커니즘을 도입하여 단기 및 장기 예측, 분포 생성 등 다양한 최적화 시나리오를 지원합니다. 실제 데이터셋 평가 결과, MobiGPT는 기존 모델 대비 예측 정확도를 최대 27.37% 향상시켰으며, 새로운 상황에서도 뛰어난 전이 학습 성능을 보여주었습니다.

## 🎯 주요 포인트

- 1. MobiGPT는 기지국 트래픽, 사용자 앱 사용량, 채널 품질을 예측할 수 있는 통합 구조를 가진 모바일 데이터 예측 모델입니다.
- 2. 소프트 프롬프트 학습 방법과 시간 마스킹 메커니즘을 도입하여 다양한 최적화 시나리오를 지원합니다.
- 3. 실제 데이터셋 평가 결과, MobiGPT는 기존 모델 대비 예측 정확도를 최대 27.37%까지 향상시켰습니다.
- 4. MobiGPT는 새로운 시나리오에서 21.51% 이상의 성능 향상을 보여 강력한 전이 학습 능력을 입증했습니다.


---

*Generated on 2025-09-24 14:48:39*