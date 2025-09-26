---
keywords:
  - Large Language Model
  - Entropy-Enhanced Multi-Turn Preference Optimization
  - Test-Time Scaling
  - Preference Optimization
  - SWE-bench
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.12434
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:34:18.069032",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Entropy-Enhanced Multi-Turn Preference Optimization",
    "Test-Time Scaling",
    "Preference Optimization",
    "SWE-bench"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Entropy-Enhanced Multi-Turn Preference Optimization": 0.8,
    "Test-Time Scaling": 0.78,
    "Preference Optimization": 0.82,
    "SWE-bench": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion on coding agents and preference optimization.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Entropy-Enhanced Multi-Turn Preference Optimization",
        "canonical": "Entropy-Enhanced Multi-Turn Preference Optimization",
        "aliases": [
          "EntroPO"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel framework introduced in the paper, crucial for understanding the proposed methodology.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Test-Time Scaling",
        "canonical": "Test-Time Scaling",
        "aliases": [
          "TTS"
        ],
        "category": "unique_technical",
        "rationale": "Test-Time Scaling is a key concept discussed for enhancing model performance, relevant for linking optimization strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Preference Optimization",
        "canonical": "Preference Optimization",
        "aliases": [
          "Direct Preference Optimization",
          "DPO",
          "Kahneman-Tversky Optimization",
          "KTO"
        ],
        "category": "specific_connectable",
        "rationale": "Preference Optimization is a central theme, with multiple methods discussed, making it a strong linking candidate.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "SWE-bench",
        "canonical": "SWE-bench",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "SWE-bench is a benchmark used to evaluate the effectiveness of the proposed methods, essential for performance context.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "tool use",
      "real-world issues",
      "model outputs",
      "interactive coding agents"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Entropy-Enhanced Multi-Turn Preference Optimization",
      "resolved_canonical": "Entropy-Enhanced Multi-Turn Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Test-Time Scaling",
      "resolved_canonical": "Test-Time Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Preference Optimization",
      "resolved_canonical": "Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "SWE-bench",
      "resolved_canonical": "SWE-bench",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12434.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.12434](https://arxiv.org/abs/2509.12434)

## 🔗 유사한 논문
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (84.9% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (84.4% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (84.2% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (84.1% similar)
- [[2025-09-22/Creative Preference Optimization_20250922|Creative Preference Optimization]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Preference Optimization|Preference Optimization]]
**⚡ Unique Technical**: [[keywords/Entropy-Enhanced Multi-Turn Preference Optimization|Entropy-Enhanced Multi-Turn Preference Optimization]], [[keywords/Test-Time Scaling|Test-Time Scaling]], [[keywords/SWE-bench|SWE-bench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12434v2 Announce Type: replace 
Abstract: Software engineering presents complex, multi-step challenges for Large Language Models (LLMs), requiring reasoning over large codebases and coordinated tool use. The difficulty of these tasks is exemplified by benchmarks like SWE-bench, where current LLMs still struggle to resolve real-world issues.
  A promising approach to enhance performance is test-time scaling (TTS), but its gains are heavily dependent on the diversity of model outputs.
  While standard alignment methods such as Direct Preference Optimization (DPO) and Kahneman-Tversky Optimization (KTO) are effective at aligning model outputs with human preferences, this process can come at the cost of reduced diversity, limiting the effectiveness of TTS.
  Additionally, existing preference optimization algorithms are typically designed for single-turn tasks and do not fully address the complexities of multi-turn reasoning and tool integration required for interactive coding agents.
  To bridge this gap, we introduce EntroPO, an entropy-enhanced framework that adapts existing preference optimization algorithms to the multi-turn, tool-assisted setting.
  EntroPO augments the preference objective to explicitly preserve policy entropy and generalizes learning to optimize over multi-turn interactions rather than single-turn responses.
  We validate EntroPO by fine-tuning a diverse suite of models from different families and sizes (up to 106B parameters).
  To maximize performance gains from TTS, we further propose a hybrid best-trajectory selection scheme combining a learned verifier model with model free approaches.
  On the \swebench leaderboard, our approach establishes new state-of-the-art results among open-weight models. A 30B parameter model trained with EntroPO ranks 1st on \lite and 4th on \verified on the open-weight leaderboard, surpassed only by models with over 10x more parameters(\eg$>$350B).

## 📝 요약

소프트웨어 엔지니어링에서 대형 언어 모델(LLM)은 복잡한 문제 해결을 요구하며, 이는 SWE-bench와 같은 벤치마크에서 드러납니다. 기존의 정렬 방법인 DPO와 KTO는 모델 출력을 인간의 선호에 맞추지만, 다양성을 감소시켜 테스트 시 스케일링(TTS)의 효과를 제한합니다. 이를 해결하기 위해, 우리는 기존의 선호 최적화 알고리즘을 다중 턴 및 도구 보조 설정에 적응시키는 엔트로피 강화 프레임워크인 EntroPO를 제안합니다. EntroPO는 정책 엔트로피를 보존하고 다중 턴 상호작용을 최적화합니다. 다양한 모델을 미세 조정하여 EntroPO를 검증하였고, TTS 성능을 극대화하기 위해 학습된 검증 모델과 모델 프리 접근을 결합한 하이브리드 최적 경로 선택 방식을 제안합니다. 이 접근법은 \swebench 리더보드에서 새로운 최고 성과를 기록했으며, 30B 파라미터 모델이 \lite에서 1위, \verified에서 4위를 차지했습니다.

## 🎯 주요 포인트

- 1. 소프트웨어 엔지니어링에서 대형 언어 모델(LLM)은 복잡한 문제 해결을 위해 대규모 코드베이스와 도구 사용을 조정해야 합니다.
- 2. 테스트 시 스케일링(TTS)은 성능 향상의 유망한 방법이지만, 모델 출력의 다양성에 크게 의존합니다.
- 3. 기존의 선호 최적화 알고리즘은 단일 턴 작업에 초점을 맞추고 있어, 다중 턴 추론과 도구 통합의 복잡성을 충분히 해결하지 못합니다.
- 4. EntroPO는 기존 선호 최적화 알고리즘을 다중 턴, 도구 지원 환경에 맞게 조정하여 정책 엔트로피를 보존하는 프레임워크입니다.
- 5. EntroPO로 훈련된 30B 파라미터 모델은 \swebench 오픈 가중치 리더보드에서 \lite 부문 1위, \verified 부문 4위를 기록했습니다.


---

*Generated on 2025-09-24 00:34:18*