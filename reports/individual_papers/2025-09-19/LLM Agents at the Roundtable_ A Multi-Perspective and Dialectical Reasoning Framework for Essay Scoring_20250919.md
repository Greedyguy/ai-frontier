---
keywords:
  - Large Language Models
  - Zero-Shot Learning
  - Automated Essay Scoring
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14834
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:39:06.178488",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Zero-Shot Learning",
    "Automated Essay Scoring"
  ],
  "rejected_keywords": [
    "Natural Language Processing",
    "Dialectical Reasoning"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Zero-Shot Learning": 0.77,
    "Automated Essay Scoring": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring

**Korean Title:** 원탁의 LLM 에이전트: 에세이 채점에 대한 다중 관점 및 변증법적 추론 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Setting]]
**⚡ Unique Technical**: [[keywords/Automated Essay Scoring|Automated Essay Scoring]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (84.3% similar)
- [[CLEAR A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models]] (82.9% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (82.8% similar)
- [[Judging with Many Minds Do More Perspectives Mean Less Prejudice On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge]] (82.8% similar)
- [[LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (82.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14834v1 Announce Type: new 
Abstract: The emergence of large language models (LLMs) has brought a new paradigm to automated essay scoring (AES), a long-standing and practical application of natural language processing in education. However, achieving human-level multi-perspective understanding and judgment remains a challenge. In this work, we propose Roundtable Essay Scoring (RES), a multi-agent evaluation framework designed to perform precise and human-aligned scoring under a zero-shot setting. RES constructs evaluator agents based on LLMs, each tailored to a specific prompt and topic context. Each agent independently generates a trait-based rubric and conducts a multi-perspective evaluation. Then, by simulating a roundtable-style discussion, RES consolidates individual evaluations through a dialectical reasoning process to produce a final holistic score that more closely aligns with human evaluation. By enabling collaboration and consensus among agents with diverse evaluation perspectives, RES outperforms prior zero-shot AES approaches. Experiments on the ASAP dataset using ChatGPT and Claude show that RES achieves up to a 34.86% improvement in average QWK over straightforward prompting (Vanilla) methods.

## 🔍 Abstract (한글 번역)

arXiv:2509.14834v1 발표 유형: 신규  
초록: 대형 언어 모델(LLM)의 등장은 교육 분야 자연어 처리의 오랜 실용적 응용인 자동 에세이 채점(AES)에 새로운 패러다임을 가져왔습니다. 그러나 인간 수준의 다각적 이해와 판단을 달성하는 것은 여전히 도전 과제로 남아 있습니다. 본 연구에서는 정확하고 인간에 맞춘 채점을 수행하기 위해 설계된 다중 에이전트 평가 프레임워크인 Roundtable Essay Scoring (RES)을 제안합니다. RES는 LLM을 기반으로 평가 에이전트를 구성하며, 각 에이전트는 특정 프롬프트와 주제 맥락에 맞춰져 있습니다. 각 에이전트는 독립적으로 특성 기반 루브릭을 생성하고 다각적 평가를 수행합니다. 그런 다음, 원탁 회의 스타일의 토론을 시뮬레이션하여 RES는 변증법적 추론 과정을 통해 개별 평가를 통합하여 인간 평가와 더 가깝게 일치하는 최종 종합 점수를 산출합니다. 다양한 평가 관점을 가진 에이전트 간의 협력과 합의를 가능하게 함으로써, RES는 이전의 제로샷 AES 접근법을 능가합니다. ChatGPT와 Claude를 사용한 ASAP 데이터셋 실험에서 RES는 단순한 프롬프트(Vanilla) 방법에 비해 평균 QWK에서 최대 34.86%의 개선을 달성했습니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용한 자동 에세이 채점(AES)의 새로운 접근법인 Roundtable Essay Scoring (RES)을 제안합니다. RES는 여러 평가 에이전트를 사용하여 다양한 관점에서 에세이를 평가하고, 이를 통해 인간과 유사한 수준의 평가를 목표로 합니다. 각 에이전트는 특정 주제와 맥락에 맞춰 독립적으로 평가 기준을 생성하고, 이를 바탕으로 다각적인 평가를 수행합니다. 이후, 원탁회의 방식의 토론을 통해 개별 평가를 통합하여 최종 점수를 도출합니다. 실험 결과, RES는 ChatGPT와 Claude를 사용한 ASAP 데이터셋에서 기존의 단순 프롬프트 방법에 비해 평균 QWK에서 최대 34.86% 향상된 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 등장으로 자동 에세이 채점(AES)에 새로운 패러다임이 형성되었습니다.

- 2. Roundtable Essay Scoring(RES)은 다중 에이전트 평가 프레임워크로, 인간과 유사한 정밀한 채점을 목표로 합니다.

- 3. RES는 LLM을 기반으로 한 평가 에이전트를 구성하여 각 에이전트가 독립적으로 다각적 평가를 수행합니다.

- 4. RES는 원탁 토론 스타일의 논증적 추론 과정을 통해 최종 점수를 산출하여 인간 평가와의 일치를 높입니다.

- 5. ChatGPT와 Claude를 사용한 실험에서 RES는 기존의 방법에 비해 평균 QWK에서 최대 34.86% 향상된 성과를 보였습니다.

---

*Generated on 2025-09-19 15:52:36*