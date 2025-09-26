<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:12:13.796981",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Functional Object Canonicalization",
    "Vision-Language Model",
    "Action Chunks",
    "Sim2Real Deployment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Functional Object Canonicalization": 0.88,
    "Vision-Language Model": 0.82,
    "Action Chunks": 0.8,
    "Sim2Real Deployment": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Functional Object Canonicalization",
        "canonical": "Functional Object Canonicalization",
        "aliases": [
          "Object Canonicalization",
          "Canonicalization"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's method for improving generalization in robotic manipulation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Models",
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "These models are crucial for mapping objects into shared functional frames, enhancing the paper's approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Action Chunks",
        "canonical": "Action Chunks",
        "aliases": [
          "Action Segments",
          "Action Units"
        ],
        "category": "unique_technical",
        "rationale": "Action chunks are a key element in the framework for breaking down tasks, aiding in policy learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Sim2Real Deployment",
        "canonical": "Sim2Real Deployment",
        "aliases": [
          "Simulation to Reality",
          "Sim-to-Real"
        ],
        "category": "specific_connectable",
        "rationale": "This is a significant challenge in robotics that the paper addresses, making it a strong link candidate.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "General-purpose",
      "Task-specific",
      "Policy Learning",
      "Benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Functional Object Canonicalization",
      "resolved_canonical": "Functional Object Canonicalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Action Chunks",
      "resolved_canonical": "Action Chunks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Sim2Real Deployment",
      "resolved_canonical": "Sim2Real Deployment",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# FUNCanon: Learning Pose-Aware Action Primitives via Functional Object Canonicalization for Generalizable Robotic Manipulation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19102.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19102](https://arxiv.org/abs/2509.19102)

## 🔗 유사한 논문
- [[2025-09-19/A Novel Task-Driven Diffusion-Based Policy with Affordance Learning for Generalizable Manipulation of Articulated Objects_20250919|A Novel Task-Driven Diffusion-Based Policy with Affordance Learning for Generalizable Manipulation of Articulated Objects]] (81.5% similar)
- [[2025-09-22/Compose by Focus_ Scene Graph-based Atomic Skills_20250922|Compose by Focus: Scene Graph-based Atomic Skills]] (81.2% similar)
- [[2025-09-23/MaskedManipulator_ Versatile Whole-Body Manipulation_20250923|MaskedManipulator: Versatile Whole-Body Manipulation]] (81.1% similar)
- [[2025-09-24/MV-UMI_ A Scalable Multi-View Interface for Cross-Embodiment Learning_20250924|MV-UMI: A Scalable Multi-View Interface for Cross-Embodiment Learning]] (80.6% similar)
- [[2025-09-24/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training_20250924|Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sim2Real Deployment|Sim2Real Deployment]]
**⚡ Unique Technical**: [[keywords/Functional Object Canonicalization|Functional Object Canonicalization]], [[keywords/Action Chunks|Action Chunks]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19102v1 Announce Type: cross 
Abstract: General-purpose robotic skills from end-to-end demonstrations often leads to task-specific policies that fail to generalize beyond the training distribution. Therefore, we introduce FunCanon, a framework that converts long-horizon manipulation tasks into sequences of action chunks, each defined by an actor, verb, and object. These chunks focus policy learning on the actions themselves, rather than isolated tasks, enabling compositionality and reuse. To make policies pose-aware and category-general, we perform functional object canonicalization for functional alignment and automatic manipulation trajectory transfer, mapping objects into shared functional frames using affordance cues from large vision language models. An object centric and action centric diffusion policy FuncDiffuser trained on this aligned data naturally respects object affordances and poses, simplifying learning and improving generalization ability. Experiments on simulated and real-world benchmarks demonstrate category-level generalization, cross-task behavior reuse, and robust sim2real deployment, showing that functional canonicalization provides a strong inductive bias for scalable imitation learning in complex manipulation domains. Details of the demo and supplemental material are available on our project website https://sites.google.com/view/funcanon.

## 📝 요약

FunCanon은 일반적인 로봇 기술을 향상시키기 위해 긴 작업을 행위 조각으로 나누는 프레임워크입니다. 각 조각은 행위자, 동사, 객체로 정의되어, 개별 작업이 아닌 행동 자체에 초점을 맞추어 정책 학습을 가능하게 합니다. 이 과정에서 대형 비전 언어 모델의 어포던스 단서를 활용하여 객체를 공통 기능 프레임으로 매핑하는 기능적 객체 정규화를 수행합니다. 이를 통해 정책이 객체의 어포던스와 자세를 자연스럽게 반영하며 학습이 간소화되고 일반화 능력이 향상됩니다. 실험 결과, FunCanon은 범주 수준의 일반화, 작업 간 행동 재사용, 강력한 시뮬레이션-현실 전환을 보여주며, 복잡한 조작 영역에서 모방 학습을 확장할 수 있는 강력한 유도 편향을 제공합니다.

## 🎯 주요 포인트

- 1. FunCanon 프레임워크는 긴 조작 작업을 배우기 쉽게 액션 청크로 변환하여 학습의 재사용성과 조합성을 높입니다.
- 2. 기능적 객체 정규화를 통해 객체를 공유 기능 프레임에 매핑하여 정책이 포즈를 인식하고 범주 일반화를 가능하게 합니다.
- 3. FuncDiffuser는 객체의 기능적 정렬 데이터를 기반으로 학습하여 객체의 기능성과 포즈를 자연스럽게 존중하며 학습을 단순화하고 일반화 능력을 향상시킵니다.
- 4. 실험 결과, FunCanon은 범주 수준의 일반화, 작업 간 행동 재사용, 강력한 시뮬레이션에서 실제 환경으로의 전환을 보여줍니다.
- 5. 기능적 정규화는 복잡한 조작 도메인에서 확장 가능한 모방 학습을 위한 강력한 귀납적 편향을 제공합니다.


---

*Generated on 2025-09-24 14:12:13*