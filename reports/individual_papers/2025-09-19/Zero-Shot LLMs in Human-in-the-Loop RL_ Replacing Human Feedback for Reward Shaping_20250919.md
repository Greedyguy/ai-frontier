---
keywords:
  - Reinforcement Learning
  - Large Language Models
  - Reward Shaping
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2503.22723
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:16:53.088019",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Large Language Models",
    "Reward Shaping"
  ],
  "rejected_keywords": [
    "Human-in-the-Loop",
    "Bias Correction"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Large Language Models": 0.8,
    "Reward Shaping": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping

**Korean Title:** 제로샷 대형 언어 모델(LLM)에서의 인간 참여 강화 학습(RL): 보상 형성을 위한 인간 피드백 대체

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Reward Shaping|Reward Shaping]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[FlowRL Matching Reward Distributions for LLM Reasoning]] (84.7% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (84.0% similar)
- [[SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (82.9% similar)
- [[Do LLMs Align Human Values Regarding Social Biases_ Judging and Explaining Social Biases with LLMs_20250918|Do LLMs Align Human Values Regarding Social Biases Judging and Explaining Social Biases with LLMs]] (82.8% similar)
- [[Judging with Many Minds Do More Perspectives Mean Less Prejudice On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge]] (82.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.22723v2 Announce Type: replace-cross 
Abstract: Reinforcement learning (RL) often struggles with reward misalignment, where agents optimize given rewards but fail to exhibit the desired behaviors. This arises when the reward function incentivizes proxy behaviors misaligned with the true objective. While human-in-the-loop (HITL) methods can mitigate this issue, they also introduce biases, leading to inconsistent and subjective feedback that complicates learning. To address these challenges, we propose two key contributions. First, we extend the use of zero-shot, off-the-shelf large language models (LLMs) for reward shaping beyond natural language processing (NLP) to continuous control tasks. Using LLMs as direct feedback providers eliminates the need for surrogate models trained on human feedback, which often inherit biases from training data. Second, we introduce a hybrid framework (LLM-HFBF) that enables LLMs to identify and correct biases in human feedback while incorporating this feedback into the reward shaping process. The LLM-HFBF framework creates a more balanced and reliable system by addressing both the limitations of LLMs (e.g., lack of domain-specific knowledge) and human supervision (e.g., inherent biases). By enabling human feedback bias flagging and correction, our approach improves reinforcement learning performance and reduces reliance on potentially biased human feedback. Empirical experiments show that biased human feedback significantly reduces performance, with Average Episodic Reward dropping by nearly 94% compared to unbiased approaches. In contrast, LLM-based methods sustain performance at a similar level to unbiased feedback, even in challenging edge-case scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2503.22723v2 발표 유형: 교차 교체  
초록: 강화 학습(RL)은 종종 보상 불일치로 어려움을 겪는데, 이는 에이전트가 주어진 보상을 최적화하지만 원하는 행동을 보이지 못하는 경우입니다. 이는 보상 함수가 실제 목표와 일치하지 않는 대리 행동을 장려할 때 발생합니다. 인간이 개입하는 루프(HITL) 방법은 이 문제를 완화할 수 있지만, 편향을 도입하여 학습을 복잡하게 만드는 일관성 없는 주관적 피드백을 초래합니다. 이러한 문제를 해결하기 위해 우리는 두 가지 주요 기여를 제안합니다. 첫째, 자연어 처리(NLP)를 넘어 연속 제어 작업에 대한 보상 형성을 위해 제로샷, 기성품 대형 언어 모델(LLM)의 사용을 확장합니다. LLM을 직접 피드백 제공자로 사용하면 종종 훈련 데이터에서 편향을 상속받는 인간 피드백으로 훈련된 대리 모델의 필요성이 사라집니다. 둘째, LLM이 인간 피드백의 편향을 식별하고 수정하면서 이 피드백을 보상 형성 과정에 통합할 수 있는 하이브리드 프레임워크(LLM-HFBF)를 소개합니다. LLM-HFBF 프레임워크는 LLM의 한계(예: 도메인별 지식 부족)와 인간 감독(예: 고유한 편향)을 모두 해결하여 보다 균형 잡히고 신뢰할 수 있는 시스템을 만듭니다. 인간 피드백의 편향 플래그 지정 및 수정을 가능하게 함으로써, 우리의 접근 방식은 강화 학습 성능을 향상시키고 잠재적으로 편향된 인간 피드백에 대한 의존도를 줄입니다. 실험 결과, 편향된 인간 피드백은 성능을 크게 저하시켜 평균 에피소드 보상이 편향되지 않은 접근법에 비해 거의 94% 감소하는 것으로 나타났습니다. 반면, LLM 기반 방법은 까다로운 엣지 케이스 시나리오에서도 편향되지 않은 피드백과 유사한 수준의 성능을 유지합니다.

## 📝 요약

강화 학습(RL)은 보상 불일치 문제로 인해 원하는 행동을 잘 수행하지 못하는 경우가 많습니다. 이는 보상 함수가 실제 목표와 일치하지 않는 대리 행동을 유도할 때 발생합니다. 인간 참여(HITL) 방법은 이를 완화할 수 있지만, 주관적 피드백으로 인해 학습이 복잡해집니다. 이를 해결하기 위해 두 가지 주요 기여를 제안합니다. 첫째, 대형 언어 모델(LLM)을 자연어 처리(NLP) 외의 연속 제어 작업에서도 보상 형성에 활용합니다. 둘째, LLM이 인간 피드백의 편향을 식별하고 수정할 수 있는 하이브리드 프레임워크(LLM-HFBF)를 도입합니다. 이 프레임워크는 LLM과 인간 감독의 한계를 보완하여 강화 학습 성능을 향상시키고 편향된 인간 피드백 의존도를 줄입니다. 실험 결과, 편향된 인간 피드백은 성능을 크게 감소시키지만, LLM 기반 방법은 성능을 유지합니다.

## 🎯 주요 포인트

- 1. 강화 학습(RL)은 보상 불일치 문제로 인해 원하는 행동을 보여주지 못할 때가 많습니다.

- 2. 인간 참여 방법(HITL)은 보상 불일치 문제를 완화할 수 있지만, 주관적 피드백으로 인해 학습이 복잡해집니다.

- 3. 제안된 방법은 대형 언어 모델(LLM)을 보상 형성에 활용하여 인간 피드백의 편향성을 줄입니다.

- 4. LLM-HFBF 프레임워크는 인간 피드백의 편향을 식별하고 수정하여 강화 학습 성능을 향상시킵니다.

- 5. 실험 결과, 편향된 인간 피드백은 성능을 크게 저하시켰지만, LLM 기반 방법은 성능을 유지했습니다.

---

*Generated on 2025-09-19 15:13:45*