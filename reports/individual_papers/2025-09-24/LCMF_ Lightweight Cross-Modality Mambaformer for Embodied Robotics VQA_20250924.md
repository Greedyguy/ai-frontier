<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:55:31.123036",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Multimodal Learning",
    "Human-Robot Interaction",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.85,
    "Multimodal Learning": 0.89,
    "Human-Robot Interaction": 0.78,
    "Large Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cross-Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Cross Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Cross-Attention is a specific form of the Attention Mechanism, crucial for linking multimodal data.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multimodal semantic learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal semantic"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is key for integrating data from different modalities, enhancing connectivity.",
        "novelty_score": 0.55,
        "connectivity_score": 0.92,
        "specificity_score": 0.82,
        "link_intent_score": 0.89
      },
      {
        "surface": "Human-Robot Interaction",
        "canonical": "Human-Robot Interaction",
        "aliases": [
          "HRI"
        ],
        "category": "unique_technical",
        "rationale": "Human-Robot Interaction is a unique technical domain that benefits from specific multimodal applications.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Model Agents",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM Agents"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are a broad technical category relevant for understanding language-based tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.87,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Mambaformer",
      "LCMF",
      "EQA video tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cross-Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multimodal semantic learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.92,
        "specificity": 0.82,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Human-Robot Interaction",
      "resolved_canonical": "Human-Robot Interaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Model Agents",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.87,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18576.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18576](https://arxiv.org/abs/2509.18576)

## 🔗 유사한 논문
- [[2025-09-23/Surgical-MambaLLM_ Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery_20250923|Surgical-MambaLLM: Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery]] (85.7% similar)
- [[2025-09-24/VLA-LPAF_ Lightweight Perspective-Adaptive Fusion for Vision-Language-Action to Enable More Unconstrained Robotic Manipulation_20250924|VLA-LPAF: Lightweight Perspective-Adaptive Fusion for Vision-Language-Action to Enable More Unconstrained Robotic Manipulation]] (84.9% similar)
- [[2025-09-23/Open Vision Reasoner_ Transferring Linguistic Cognitive Behavior for Visual Reasoning_20250923|Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning]] (84.6% similar)
- [[2025-09-23/LEO-MINI_ An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts_20250923|LEO-MINI: An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts]] (84.4% similar)
- [[2025-09-23/MCP_ A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models_20250923|MCP: A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Human-Robot Interaction|Human-Robot Interaction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18576v1 Announce Type: cross 
Abstract: Multimodal semantic learning plays a critical role in embodied intelligence, especially when robots perceive their surroundings, understand human instructions, and make intelligent decisions. However, the field faces technical challenges such as effective fusion of heterogeneous data and computational efficiency in resource-constrained environments. To address these challenges, this study proposes the lightweight LCMF cascaded attention framework, introducing a multi-level cross-modal parameter sharing mechanism into the Mamba module. By integrating the advantages of Cross-Attention and Selective parameter-sharing State Space Models (SSMs), the framework achieves efficient fusion of heterogeneous modalities and semantic complementary alignment. Experimental results show that LCMF surpasses existing multimodal baselines with an accuracy of 74.29% in VQA tasks and achieves competitive mid-tier performance within the distribution cluster of Large Language Model Agents (LLM Agents) in EQA video tasks. Its lightweight design achieves a 4.35-fold reduction in FLOPs relative to the average of comparable baselines while using only 166.51M parameters (image-text) and 219M parameters (video-text), providing an efficient solution for Human-Robot Interaction (HRI) applications in resource-constrained scenarios with strong multimodal decision generalization capabilities.

## 📝 요약

이 연구는 로봇의 지능적 의사결정에 중요한 다중 모달 의미 학습의 기술적 과제를 해결하기 위해 LCMF 경량화 연속 주의 프레임워크를 제안합니다. Cross-Attention과 선택적 매개변수 공유 상태 공간 모델(SSM)의 장점을 결합하여 이질적 데이터의 효율적 융합과 의미 보완 정렬을 달성합니다. 실험 결과, LCMF는 VQA 작업에서 74.29%의 정확도로 기존 다중 모달 기준을 능가하며, EQA 비디오 작업에서 경쟁력 있는 성능을 보입니다. 또한, 평균 대비 4.35배의 FLOPs 감소와 적은 매개변수 사용으로 자원 제한 환경에서 효율적인 인간-로봇 상호작용(HRI) 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 이종 데이터의 효과적인 융합과 자원 제약 환경에서의 계산 효율성을 해결하기 위해 경량 LCMF 계단식 주의 메커니즘을 제안합니다.
- 2. LCMF 프레임워크는 Cross-Attention과 선택적 파라미터 공유 상태 공간 모델(SSMs)의 장점을 통합하여 이종 모달리티의 효율적인 융합과 의미적 보완 정렬을 달성합니다.
- 3. 실험 결과, LCMF는 VQA 작업에서 74.29%의 정확도로 기존 멀티모달 기준선을 능가하며, EQA 비디오 작업에서 LLM 에이전트 분포 클러스터 내에서 경쟁력 있는 중간 성능을 보여줍니다.
- 4. LCMF의 경량 설계는 비교 가능한 기준선의 평균 대비 FLOPs를 4.35배 감소시키며, 이미지-텍스트 166.51M 파라미터와 비디오-텍스트 219M 파라미터만을 사용하여 자원 제약 시나리오에서 효율적인 인간-로봇 상호작용(HRI) 응용 솔루션을 제공합니다.


---

*Generated on 2025-09-24 13:55:31*