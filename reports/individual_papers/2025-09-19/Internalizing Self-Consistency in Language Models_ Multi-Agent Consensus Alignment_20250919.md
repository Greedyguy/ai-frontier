---
keywords:
  - Large Language Models
  - Multi-Agent Consensus Alignment
  - Reinforcement Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15172
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:39:48.704673",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Multi-Agent Consensus Alignment",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [
    "Self-Consistency"
  ],
  "similarity_scores": {
    "Large Language Models": 0.88,
    "Multi-Agent Consensus Alignment": 0.8,
    "Reinforcement Learning": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment

**Korean Title:** 언어 모델에서 자기 일관성 내재화: 다중 에이전트 합의 정렬

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Large Language Models|Language Models]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Multi-Agent Consensus Alignment|Multi-Agent Consensus Alignment]]

## 🔗 유사한 논문
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (84.8% similar)
- [[Enhancing Multi-Agent Debate System Performance via Confidence Expression]] (84.0% similar)
- [[Language Models Identify Ambiguities and Exploit Loopholes]] (83.7% similar)
- [[A_Knowledge-driven_Adaptive_Collaboration_of_LLMs_for_Enhancing_Medical_Decision-making_20250919|A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making]] (83.6% similar)
- [[AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (83.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15172v1 Announce Type: new 
Abstract: Language Models (LMs) are inconsistent reasoners, often generating contradictory responses to identical prompts. While inference-time methods can mitigate these inconsistencies, they fail to address the core problem: LMs struggle to reliably select reasoning pathways leading to consistent outcomes under exploratory sampling. To address this, we formalize self-consistency as an intrinsic property of well-aligned reasoning models and introduce Multi-Agent Consensus Alignment (MACA), a reinforcement learning framework that post-trains models to favor reasoning trajectories aligned with their internal consensus using majority/minority outcomes from multi-agent debate. These trajectories emerge from deliberative exchanges where agents ground reasoning in peer arguments, not just aggregation of independent attempts, creating richer consensus signals than single-round majority voting. MACA enables agents to teach themselves to be more decisive and concise, and better leverage peer insights in multi-agent settings without external supervision, driving substantial improvements across self-consistency (+27.6% on GSM8K), single-agent reasoning (+23.7% on MATH), sampling-based inference (+22.4% Pass@20 on MATH), and multi-agent ensemble decision-making (+42.7% on MathQA). These findings, coupled with strong generalization to unseen benchmarks (+16.3% on GPQA, +11.6% on CommonsenseQA), demonstrate robust self-alignment that more reliably unlocks latent reasoning potential of language models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15172v1 발표 유형: 신규  
초록: 언어 모델(LM)은 일관성이 없는 추론을 하며, 동일한 프롬프트에 대해 모순된 응답을 생성하는 경우가 많습니다. 추론 시간 방법은 이러한 불일치를 완화할 수 있지만, 핵심 문제를 해결하지는 못합니다. 즉, LM은 탐색적 샘플링 하에서 일관된 결과를 이끌어내는 추론 경로를 신뢰성 있게 선택하는 데 어려움을 겪습니다. 이를 해결하기 위해, 우리는 자기 일관성을 잘 정렬된 추론 모델의 내재적 특성으로 공식화하고, 다중 에이전트 합의 정렬(Multi-Agent Consensus Alignment, MACA)을 도입합니다. 이는 다중 에이전트 토론에서 다수/소수 결과를 사용하여 내부 합의에 맞는 추론 경로를 선호하도록 모델을 사후 학습시키는 강화 학습 프레임워크입니다. 이러한 경로는 독립적인 시도의 집계가 아닌, 에이전트가 동료의 주장을 기반으로 추론을 정립하는 심의적 교환에서 발생하여 단일 라운드 다수 투표보다 더 풍부한 합의 신호를 생성합니다. MACA는 에이전트가 외부 감독 없이 다중 에이전트 환경에서 동료의 통찰력을 더 잘 활용하고, 더 결단력 있고 간결하게 스스로를 가르칠 수 있도록 하여 자기 일관성(+27.6% GSM8K), 단일 에이전트 추론(+23.7% MATH), 샘플링 기반 추론(+22.4% Pass@20 MATH), 다중 에이전트 앙상블 의사 결정(+42.7% MathQA) 전반에 걸쳐 상당한 개선을 이끌어냅니다. 이러한 발견은 미지의 벤치마크에 대한 강력한 일반화(+16.3% GPQA, +11.6% CommonsenseQA)와 결합하여 언어 모델의 잠재적 추론 능력을 더 신뢰성 있게 발휘할 수 있는 견고한 자기 정렬을 입증합니다.

## 📝 요약

이 논문은 언어 모델(LM)의 일관성 문제를 해결하기 위해 다중 에이전트 합의 정렬(MACA)이라는 강화 학습 프레임워크를 제안합니다. MACA는 다중 에이전트 토론을 통해 모델이 내부 합의에 맞는 추론 경로를 선호하도록 훈련시킵니다. 이 방법은 독립적인 시도들의 단순한 집계가 아닌, 에이전트 간의 심층적인 논의를 통해 풍부한 합의 신호를 생성합니다. MACA는 외부 감독 없이 에이전트가 스스로 더 결정적이고 간결하게 학습하도록 하며, 동료의 통찰을 더 잘 활용할 수 있게 합니다. 그 결과, 자기 일관성, 단일 에이전트 추론, 샘플링 기반 추론, 다중 에이전트 의사 결정에서 상당한 개선을 이루었습니다. 또한, 새로운 벤치마크에 대한 강력한 일반화 능력을 보여 언어 모델의 잠재적 추론 능력을 더 안정적으로 발휘할 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. 언어 모델(LMs)은 동일한 프롬프트에 대해 모순된 응답을 생성하는 비일관적인 추론을 보인다.

- 2. Multi-Agent Consensus Alignment(MACA)는 다중 에이전트 토론의 다수/소수 결과를 활용하여 모델을 자기 일관성에 맞게 후훈련시키는 강화 학습 프레임워크이다.

- 3. MACA는 에이전트가 동료의 주장을 기반으로 추론을 진행하여 더 풍부한 합의 신호를 생성하고, 외부 감독 없이도 더 결정적이고 간결하게 학습할 수 있게 한다.

- 4. MACA는 자기 일관성, 단일 에이전트 추론, 샘플링 기반 추론, 다중 에이전트 의사결정에서 상당한 개선을 이끌어낸다.

- 5. 새로운 벤치마크에 대한 강력한 일반화 능력을 통해 언어 모델의 잠재적 추론 능력을 더 신뢰성 있게 발휘할 수 있음을 보여준다.

---

*Generated on 2025-09-19 14:49:41*