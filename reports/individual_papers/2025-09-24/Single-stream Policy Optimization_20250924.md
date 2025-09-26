<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:42:12.561837",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Single-stream Policy Optimization",
    "Large Language Model",
    "KL-adaptive value tracker",
    "Advantage Normalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Single-stream Policy Optimization": 0.8,
    "Large Language Model": 0.85,
    "KL-adaptive value tracker": 0.78,
    "Advantage Normalization": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Single-stream Policy Optimization",
        "canonical": "Single-stream Policy Optimization",
        "aliases": [
          "SPO"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to policy optimization that addresses key limitations in existing methods, offering a unique contribution to the field.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in the paper, connecting to a broad range of research in natural language processing and machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "KL-adaptive value tracker",
        "canonical": "KL-adaptive value tracker",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific mechanism introduced in the paper that provides a stable learning signal, crucial for understanding the proposed optimization method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "advantage normalization",
        "canonical": "Advantage Normalization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A technique that is central to the paper's methodology, offering potential links to other works on optimization techniques in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "baseline estimation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Single-stream Policy Optimization",
      "resolved_canonical": "Single-stream Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "KL-adaptive value tracker",
      "resolved_canonical": "KL-adaptive value tracker",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "advantage normalization",
      "resolved_canonical": "Advantage Normalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Single-stream Policy Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13232.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.13232](https://arxiv.org/abs/2509.13232)

## 🔗 유사한 논문
- [[2025-09-24/NGRPO_ Negative-enhanced Group Relative Policy Optimization_20250924|NGRPO: Negative-enhanced Group Relative Policy Optimization]] (88.3% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (86.6% similar)
- [[2025-09-23/Advancing Speech Understanding in Speech-Aware Language Models with GRPO_20250923|Advancing Speech Understanding in Speech-Aware Language Models with GRPO]] (86.1% similar)
- [[2025-09-24/MAPO_ Mixed Advantage Policy Optimization_20250924|MAPO: Mixed Advantage Policy Optimization]] (85.4% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (85.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Advantage Normalization|Advantage Normalization]]
**⚡ Unique Technical**: [[keywords/Single-stream Policy Optimization|Single-stream Policy Optimization]], [[keywords/KL-adaptive value tracker|KL-adaptive value tracker]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13232v2 Announce Type: replace-cross 
Abstract: We revisit policy-gradient optimization for Large Language Models (LLMs) from a single-stream perspective. Prevailing group-based methods like GRPO reduce variance with on-the-fly baselines but suffer from critical flaws: frequent degenerate groups erase learning signals, and synchronization barriers hinder scalability. We introduce Single-stream Policy Optimization (SPO), which eliminates these issues by design. SPO replaces per-group baselines with a persistent, KL-adaptive value tracker and normalizes advantages globally across the batch, providing a stable, low-variance learning signal for every sample. Being group-free, SPO enables higher throughput and scales effectively in long-horizon or tool-integrated settings where generation times vary. Furthermore, the persistent value tracker naturally enables an adaptive curriculum via prioritized sampling. Experiments using Qwen3-8B show that SPO converges more smoothly and attains higher accuracy than GRPO, while eliminating computation wasted on degenerate groups. Ablation studies confirm that SPO's gains stem from its principled approach to baseline estimation and advantage normalization, offering a more robust and efficient path for LLM reasoning. Across five hard math benchmarks with Qwen3 8B, SPO improves the average maj@32 by +3.4 percentage points (pp) over GRPO, driven by substantial absolute point gains on challenging datasets, including +7.3 pp on BRUMO 25, +4.4 pp on AIME 25, +3.3 pp on HMMT 25, and achieves consistent relative gain in pass@$k$ across the evaluated $k$ values. SPO's success challenges the prevailing trend of adding incidental complexity to RL algorithms, highlighting a path where fundamental principles, not architectural workarounds, drive the next wave of progress in LLM reasoning.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 정책 경사 최적화를 단일 스트림 관점에서 재검토합니다. 기존의 그룹 기반 방법인 GRPO는 변동성을 줄이기 위해 실시간 기준선을 사용하지만, 학습 신호 소멸과 동기화 문제로 인해 확장성에 한계가 있습니다. 이를 해결하기 위해 단일 스트림 정책 최적화(SPO)를 제안합니다. SPO는 그룹 기준선을 KL-적응형 가치 추적기로 대체하고, 배치 전반에 걸쳐 이점을 정규화하여 안정적이고 낮은 변동성의 학습 신호를 제공합니다. SPO는 그룹 없이도 높은 처리량을 가능하게 하며, 긴 시간대나 도구 통합 환경에서도 효과적으로 확장됩니다. 실험 결과, SPO는 GRPO보다 더 매끄럽게 수렴하고 높은 정확도를 달성하며, 불필요한 계산을 제거합니다. SPO는 기본 원칙에 기반한 접근 방식으로, LLM 추론의 새로운 발전 경로를 제시합니다. Qwen3-8B를 사용한 실험에서 SPO는 GRPO 대비 평균 정확도를 3.4%포인트 향상시켰습니다.

## 🎯 주요 포인트

- 1. SPO는 그룹 기반 방법의 단점을 해결하여 안정적이고 낮은 분산의 학습 신호를 제공하는 단일 스트림 정책 최적화 방법입니다.
- 2. SPO는 지속적인 KL-적응형 가치 추적기를 사용하여 그룹별 기준선을 대체하고, 전역적으로 이점을 정규화하여 학습 효율성을 높입니다.
- 3. SPO는 그룹이 없어 높은 처리량을 가능하게 하며, 다양한 생성 시간의 긴 수평선 또는 도구 통합 설정에서 효과적으로 확장됩니다.
- 4. 실험 결과, SPO는 GRPO보다 더 부드럽게 수렴하고 높은 정확도를 달성하며, 퇴화된 그룹에 낭비되는 계산을 제거합니다.
- 5. SPO는 복잡성을 추가하는 대신 기본 원칙에 기반하여 LLM 추론의 다음 발전을 이끄는 경로를 제시합니다.


---

*Generated on 2025-09-24 14:42:12*