<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:56:12.983743",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Vision-Language Model",
    "Neurosymbolic Planning",
    "Scene Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.85,
    "Vision-Language Model": 0.89,
    "Neurosymbolic Planning": 0.78,
    "Scene Graph": 0.81
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot Transfer",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Transfer",
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is crucial for linking to related works on learning without prior exposure to specific tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language Navigation",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Navigation",
          "VLN"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are a rapidly evolving area, connecting to multimodal learning and integration.",
        "novelty_score": 0.65,
        "connectivity_score": 0.9,
        "specificity_score": 0.82,
        "link_intent_score": 0.89
      },
      {
        "surface": "Neurosymbolic Planning",
        "canonical": "Neurosymbolic Planning",
        "aliases": [
          "Neurosymbolic Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Neurosymbolic Planning is a novel approach combining symbolic reasoning with neural networks, relevant for advanced AI systems.",
        "novelty_score": 0.72,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Scene Graph",
        "canonical": "Scene Graph",
        "aliases": [
          "Symbolic Scene Graph"
        ],
        "category": "specific_connectable",
        "rationale": "Scene Graphs are essential for linking to works on structured visual representations and symbolic reasoning.",
        "novelty_score": 0.58,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.81
      }
    ],
    "ban_list_suggestions": [
      "Rapid Exploration",
      "Cache-Enabled Execution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-Shot Transfer",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language Navigation",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.9,
        "specificity": 0.82,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Neurosymbolic Planning",
      "resolved_canonical": "Neurosymbolic Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Scene Graph",
      "resolved_canonical": "Scene Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.81
      }
    }
  ]
}
-->

# VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18592.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18592](https://arxiv.org/abs/2509.18592)

## 🔗 유사한 논문
- [[2025-09-19/Handle Object Navigation as Weighted Traveling Repairman Problem_20250919|Handle Object Navigation as Weighted Traveling Repairman Problem]] (85.8% similar)
- [[2025-09-18/FSR-VLN_ Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph_20250918|FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (85.1% similar)
- [[2025-09-22/Walk and Read Less_ Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning_20250922|Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation via Tuning-Free Multimodal Token Pruning]] (84.6% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (84.0% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Scene Graph|Scene Graph]]
**⚡ Unique Technical**: [[keywords/Neurosymbolic Planning|Neurosymbolic Planning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18592v1 Announce Type: cross 
Abstract: Rapid adaptation in unseen environments is essential for scalable real-world autonomy, yet existing approaches rely on exhaustive exploration or rigid navigation policies that fail to generalize. We present VLN-Zero, a two-phase vision-language navigation framework that leverages vision-language models to efficiently construct symbolic scene graphs and enable zero-shot neurosymbolic navigation. In the exploration phase, structured prompts guide VLM-based search toward informative and diverse trajectories, yielding compact scene graph representations. In the deployment phase, a neurosymbolic planner reasons over the scene graph and environmental observations to generate executable plans, while a cache-enabled execution module accelerates adaptation by reusing previously computed task-location trajectories. By combining rapid exploration, symbolic reasoning, and cache-enabled execution, the proposed framework overcomes the computational inefficiency and poor generalization of prior vision-language navigation methods, enabling robust and scalable decision-making in unseen environments. VLN-Zero achieves 2x higher success rate compared to state-of-the-art zero-shot models, outperforms most fine-tuned baselines, and reaches goal locations in half the time with 55% fewer VLM calls on average compared to state-of-the-art models across diverse environments. Codebase, datasets, and videos for VLN-Zero are available at: https://vln-zero.github.io/.

## 📝 요약

VLN-Zero는 새로운 환경에서의 빠른 적응을 목표로 하는 비전-언어 내비게이션 프레임워크로, 두 단계로 구성됩니다. 탐색 단계에서는 비전-언어 모델을 활용해 상징적 장면 그래프를 효율적으로 구축하고, 다양한 경로를 탐색합니다. 배치 단계에서는 신경-상징적 계획자가 장면 그래프와 환경 관찰을 바탕으로 실행 가능한 계획을 생성하며, 캐시 기능을 통해 이전에 계산된 경로를 재사용하여 적응 속도를 높입니다. 이 프레임워크는 기존 방법의 일반화 문제와 계산 비효율성을 극복하여, 새로운 환경에서의 견고하고 확장 가능한 의사결정을 가능하게 합니다. VLN-Zero는 최신 모델 대비 성공률이 두 배 높고, 목표 도달 시간이 절반으로 단축되며, 평균적으로 55% 적은 VLM 호출을 필요로 합니다.

## 🎯 주요 포인트

- 1. VLN-Zero는 비전-언어 모델을 활용하여 상징적 장면 그래프를 효율적으로 구축하고 제로샷 신경상징적 내비게이션을 가능하게 하는 두 단계의 비전-언어 내비게이션 프레임워크입니다.
- 2. 탐색 단계에서는 구조화된 프롬프트가 VLM 기반 검색을 정보가 풍부하고 다양한 경로로 안내하여 간결한 장면 그래프 표현을 생성합니다.
- 3. 배포 단계에서는 신경상징적 계획자가 장면 그래프와 환경 관찰을 바탕으로 실행 가능한 계획을 생성하며, 캐시 지원 실행 모듈이 이전에 계산된 작업-위치 경로를 재사용하여 적응을 가속화합니다.
- 4. VLN-Zero는 빠른 탐색, 상징적 추론, 캐시 지원 실행을 결합하여 기존 비전-언어 내비게이션 방법의 계산 비효율성과 일반화 부족 문제를 극복합니다.
- 5. VLN-Zero는 최신 제로샷 모델 대비 2배 높은 성공률을 기록하며, 대부분의 미세 조정된 기준 모델을 능가하고, 다양한 환경에서 목표 위치에 도달하는 데 걸리는 시간을 절반으로 줄이고 평균적으로 55% 적은 VLM 호출을 사용합니다.


---

*Generated on 2025-09-24 13:56:12*