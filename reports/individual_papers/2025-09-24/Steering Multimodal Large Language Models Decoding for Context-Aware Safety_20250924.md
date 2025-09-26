<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:15:13.866612",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Safety-aware Contrastive Decoding",
    "Vision-Language Model",
    "Scene-level reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Safety-aware Contrastive Decoding": 0.79,
    "Vision-Language Model": 0.8,
    "Scene-level reasoning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of integrating multiple modalities, a key aspect of the paper's focus on safety in language models.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Safety-aware Contrastive Decoding",
        "canonical": "Safety-aware Contrastive Decoding",
        "aliases": [
          "SafeCoDe"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method specifically designed for improving safety in multimodal models, central to the paper's contribution.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Connects to the emerging field of models that process both visual and textual data, relevant to the paper's context.",
        "novelty_score": 0.54,
        "connectivity_score": 0.87,
        "specificity_score": 0.81,
        "link_intent_score": 0.8
      },
      {
        "surface": "Scene-level reasoning",
        "canonical": "Scene-level reasoning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Highlights a specific reasoning approach used in the paper to enhance safety decisions, offering a unique technical angle.",
        "novelty_score": 0.71,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "oversensitivity",
      "undersensitivity",
      "general safety evaluations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Safety-aware Contrastive Decoding",
      "resolved_canonical": "Safety-aware Contrastive Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.54,
        "connectivity": 0.87,
        "specificity": 0.81,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Scene-level reasoning",
      "resolved_canonical": "Scene-level reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.71,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Steering Multimodal Large Language Models Decoding for Context-Aware Safety

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19212.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19212](https://arxiv.org/abs/2509.19212)

## 🔗 유사한 논문
- [[2025-09-23/Automating Steering for Safe Multimodal Large Language Models_20250923|Automating Steering for Safe Multimodal Large Language Models]] (89.2% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (87.3% similar)
- [[2025-09-24/Safe-SAIL_ Towards a Fine-grained Safety Landscape of Large Language Models via Sparse Autoencoder Interpretation Framework_20250924|Safe-SAIL: Towards a Fine-grained Safety Landscape of Large Language Models via Sparse Autoencoder Interpretation Framework]] (86.8% similar)
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (85.8% similar)
- [[2025-09-23/Reasoning-to-Defend_ Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking_20250923|Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking]] (85.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Safety-aware Contrastive Decoding|Safety-aware Contrastive Decoding]], [[keywords/Scene-level reasoning|Scene-level reasoning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19212v1 Announce Type: cross 
Abstract: Multimodal Large Language Models (MLLMs) are increasingly deployed in real-world applications, yet their ability to make context-aware safety decisions remains limited. Existing methods often fail to balance oversensitivity (unjustified refusals of benign queries) and undersensitivity (missed detection of visually grounded risks), leaving a persistent gap in safety alignment. To address this issue, we introduce Safety-aware Contrastive Decoding (SafeCoDe), a lightweight and model-agnostic decoding framework that dynamically adjusts token generation based on multimodal context. SafeCoDe operates in two stages: (1) a contrastive decoding mechanism that highlights tokens sensitive to visual context by contrasting real and Gaussian-noised images, and (2) a global-aware token modulation strategy that integrates scene-level reasoning with token-level adjustment to adapt refusals according to the predicted safety verdict. Extensive experiments across diverse MLLM architectures and safety benchmarks, covering undersensitivity, oversensitivity, and general safety evaluations, show that SafeCoDe consistently improves context-sensitive refusal behaviors while preserving model helpfulness.

## 📝 요약

다중모달 대형 언어 모델(MLLM)의 안전성 문제를 해결하기 위해 제안된 연구입니다. 기존 방법들은 안전성 조정에서 과도한 민감성과 부족한 민감성을 균형 있게 처리하지 못했습니다. 이를 해결하기 위해, 본 연구에서는 SafeCoDe라는 경량의 모델 비종속적 디코딩 프레임워크를 소개합니다. SafeCoDe는 두 단계로 작동하며, 첫째로 실제 이미지와 가우시안 노이즈 이미지를 대비시켜 시각적 맥락에 민감한 토큰을 강조하는 대조 디코딩 메커니즘을 사용합니다. 둘째로, 장면 수준의 추론과 토큰 수준의 조정을 통합하여 예측된 안전 판결에 따라 거부를 조정하는 글로벌 인식 토큰 조정 전략을 채택합니다. 다양한 MLLM 아키텍처와 안전성 벤치마크를 통해 수행된 실험 결과, SafeCoDe는 문맥에 민감한 거부 행동을 개선하면서 모델의 유용성을 유지하는 데 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 다중모달 대형 언어 모델(MLLMs)은 실제 응용에서 점점 더 많이 사용되지만, 맥락 인식 안전 결정 능력은 제한적이다.
- 2. 기존 방법은 과민성(정당하지 않은 거절)과 저민성(시각적으로 기반한 위험의 탐지 실패) 간의 균형을 맞추지 못한다.
- 3. SafeCoDe는 다중모달 맥락에 따라 동적으로 토큰 생성을 조정하는 경량의 모델 비종속적 디코딩 프레임워크이다.
- 4. SafeCoDe는 대조 디코딩 메커니즘과 전역 인식 토큰 조정 전략을 통해 시각적 맥락에 민감한 토큰을 강조하고, 예측된 안전 판결에 따라 거절을 조정한다.
- 5. 다양한 MLLM 아키텍처와 안전 벤치마크를 통한 실험에서 SafeCoDe는 맥락에 민감한 거절 행동을 개선하면서 모델의 유용성을 유지한다.


---

*Generated on 2025-09-24 14:15:13*