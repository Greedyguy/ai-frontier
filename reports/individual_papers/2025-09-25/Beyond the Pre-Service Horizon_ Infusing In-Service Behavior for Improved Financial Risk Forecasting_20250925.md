---
keywords:
  - Multi-Granularity Knowledge Distillation
  - Knowledge Distillation
  - Re-weighting Strategy
  - Behavioral Patterns
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.06385
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:34:27.492947",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Granularity Knowledge Distillation",
    "Knowledge Distillation",
    "Re-weighting Strategy",
    "Behavioral Patterns"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Granularity Knowledge Distillation": 0.8,
    "Knowledge Distillation": 0.85,
    "Re-weighting Strategy": 0.7,
    "Behavioral Patterns": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Granularity Knowledge Distillation",
        "canonical": "Multi-Granularity Knowledge Distillation",
        "aliases": [
          "MGKD"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper that integrates in-service behavior for risk prediction, offering a unique approach to financial risk forecasting.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Knowledge Distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Knowledge Distillation is a key technique used in the framework, connecting it to broader machine learning practices.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Re-weighting Strategy",
        "canonical": "Re-weighting Strategy",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This strategy is crucial for addressing model bias, making it a unique contribution to the methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Behavioral Patterns",
        "canonical": "Behavioral Patterns",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding and transferring behavioral patterns is central to the proposed framework, linking it to user behavior analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "financial risk management",
      "default detection",
      "risk prediction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Granularity Knowledge Distillation",
      "resolved_canonical": "Multi-Granularity Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Knowledge Distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Re-weighting Strategy",
      "resolved_canonical": "Re-weighting Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Behavioral Patterns",
      "resolved_canonical": "Behavioral Patterns",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Beyond the Pre-Service Horizon: Infusing In-Service Behavior for Improved Financial Risk Forecasting

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.06385.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.06385](https://arxiv.org/abs/2509.06385)

## 🔗 유사한 논문
- [[2025-09-19/Evaluating Supervised Learning Models for Fraud Detection_ A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data_20250919|Evaluating Supervised Learning Models for Fraud Detection: A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data]] (81.5% similar)
- [[2025-09-22/RMT-KD_ Random Matrix Theoretic Causal Knowledge Distillation_20250922|RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation]] (81.3% similar)
- [[2025-09-17/Synthesizing Behaviorally-Grounded Reasoning Chains_ A Data-Generation Framework for Personal Finance LLMs_20250917|Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation Framework for Personal Finance LLMs]] (81.1% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (81.1% similar)
- [[2025-09-24/LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection_20250924|LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Knowledge Distillation|Knowledge Distillation]], [[keywords/Behavioral Patterns|Behavioral Patterns]]
**⚡ Unique Technical**: [[keywords/Multi-Granularity Knowledge Distillation|Multi-Granularity Knowledge Distillation]], [[keywords/Re-weighting Strategy|Re-weighting Strategy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06385v3 Announce Type: replace-cross 
Abstract: Typical financial risk management involves distinct phases for pre-service risk assessment and in-service default detection, often modeled separately. This paper proposes a novel framework, Multi-Granularity Knowledge Distillation (abbreviated as MGKD), aimed at improving pre-service risk prediction through the integration of in-service user behavior data. MGKD follows the idea of knowledge distillation, where the teacher model, trained on historical in-service data, guides the student model, which is trained on pre-service data. By using soft labels derived from in-service data, the teacher model helps the student model improve its risk prediction prior to service activation. Meanwhile, a multi-granularity distillation strategy is introduced, including coarse-grained, fine-grained, and self-distillation, to align the representations and predictions of the teacher and student models. This approach not only reinforces the representation of default cases but also enables the transfer of key behavioral patterns associated with defaulters from the teacher to the student model, thereby improving the overall performance of pre-service risk assessment. Moreover, we adopt a re-weighting strategy to mitigate the model's bias towards the minority class. Experimental results on large-scale real-world datasets from Tencent Mobile Payment demonstrate the effectiveness of our proposed approach in both offline and online scenarios.

## 📝 요약

이 논문은 금융 리스크 관리에서 사전 리스크 평가와 서비스 중 디폴트 감지를 통합하는 새로운 프레임워크인 다중-그레인 지식 증류(MGKD)를 제안합니다. MGKD는 서비스 중 사용자 행동 데이터를 활용하여 사전 리스크 예측을 향상시키는 방법론입니다. 역사적 서비스 중 데이터로 학습된 교사 모델이 사전 데이터로 학습된 학생 모델을 지도하며, 다중-그레인 증류 전략을 통해 두 모델 간의 표현과 예측을 정렬합니다. 이 접근법은 디폴트 사례의 표현을 강화하고, 디폴트 관련 행동 패턴을 학생 모델로 전이시켜 사전 리스크 평가 성능을 개선합니다. 또한, 소수 클래스에 대한 모델 편향을 완화하기 위해 재가중치 전략을 채택했습니다. Tencent 모바일 결제의 대규모 실제 데이터셋을 활용한 실험 결과, 제안된 방법이 오프라인 및 온라인 시나리오에서 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 서비스 전 위험 예측을 개선하기 위해 서비스 중 사용자 행동 데이터를 통합하는 새로운 프레임워크인 MGKD를 제안합니다.
- 2. MGKD는 역사적인 서비스 중 데이터를 기반으로 훈련된 교사 모델이 서비스 전 데이터를 기반으로 훈련된 학생 모델을 지도하는 지식 증류 아이디어를 따릅니다.
- 3. 다중-그레인 증류 전략을 도입하여 교사와 학생 모델의 표현과 예측을 정렬하고, 디폴트 사례의 표현을 강화합니다.
- 4. 소수 클래스에 대한 모델 편향을 완화하기 위해 재가중치 전략을 채택합니다.
- 5. Tencent 모바일 결제의 대규모 실제 데이터셋에 대한 실험 결과, 제안된 접근 방식의 오프라인 및 온라인 시나리오에서의 효과가 입증되었습니다.


---

*Generated on 2025-09-25 16:34:27*