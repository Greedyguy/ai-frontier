# Empathy-R1: A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support

**Korean Title:** 공감-R1: 장기 정신 건강 지원을 위한 공감 사슬 및 강화 학습 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Xianrong Yao|Xianrong Yao]] [[authors/Dong She|Dong She]] [[authors/Chenxu Zhang|Chenxu Zhang]] [[authors/Yimeng Zhang|Yimeng Zhang]] [[authors/Yueru Sun|Yueru Sun]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretable AI for Mental Health

## 🔗 유사한 논문
- [[LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (81.5% similar)
- [[MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1 Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (80.1% similar)
- [[OnlineMate_ An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning_20250919|OnlineMate An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning]] (79.2% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (79.2% similar)
- [[Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (79.2% similar)

## 📋 저자 정보

**Authors:** Xianrong Yao, Dong She, Chenxu Zhang, Yimeng Zhang, Yueru Sun, Noman Ahmed, Yang Gao, Zhanpeng Jin

## 📄 Abstract (원문)

Empathy is critical for effective mental health support, especially when
addressing Long Counseling Texts (LCTs). However, existing Large Language
Models (LLMs) often generate replies that are semantically fluent but lack the
structured reasoning necessary for genuine psychological support, particularly
in a Chinese context. To bridge this gap, we introduce Empathy-R1, a novel
framework that integrates a Chain-of-Empathy (CoE) reasoning process with
Reinforcement Learning (RL) to enhance response quality for LCTs. Inspired by
cognitive-behavioral therapy, our CoE paradigm guides the model to sequentially
reason about a help-seeker's emotions, causes, and intentions, making its
thinking process both transparent and interpretable. Our framework is empowered
by a new large-scale Chinese dataset, Empathy-QA, and a two-stage training
process. First, Supervised Fine-Tuning instills the CoE's reasoning structure.
Subsequently, RL, guided by a dedicated reward model, refines the therapeutic
relevance and contextual appropriateness of the final responses. Experiments
show that Empathy-R1 achieves strong performance on key automatic metrics. More
importantly, human evaluations confirm its superiority, showing a clear
preference over strong baselines and achieving a Win@1 rate of 44.30% on our
new benchmark. By enabling interpretable and contextually nuanced responses,
Empathy-R1 represents a significant advancement in developing responsible and
genuinely beneficial AI for mental health support.

## 🔍 Abstract (한글 번역)

공감은 효과적인 정신 건강 지원에 필수적이며, 특히 장문의 상담 텍스트(Long Counseling Texts, LCTs)을 다룰 때 중요합니다. 그러나 기존의 대형 언어 모델(Large Language Models, LLMs)은 의미적으로 유창한 답변을 생성하지만, 진정한 심리적 지원에 필요한 구조화된 추론이 부족한 경우가 많습니다. 특히 중국어 맥락에서 이러한 문제를 해결하기 위해, 우리는 Empathy-R1이라는 새로운 프레임워크를 소개합니다. 이 프레임워크는 공감의 연쇄(Chain-of-Empathy, CoE) 추론 과정과 강화 학습(Reinforcement Learning, RL)을 통합하여 LCTs에 대한 응답 품질을 향상시킵니다. 인지행동치료에서 영감을 받은 CoE 패러다임은 모델이 도움을 구하는 사람의 감정, 원인 및 의도를 순차적으로 추론하도록 안내하여 사고 과정을 투명하고 해석 가능하게 만듭니다. 우리의 프레임워크는 새로운 대규모 중국어 데이터셋인 Empathy-QA와 두 단계의 훈련 과정을 통해 강화됩니다. 먼저, 지도 학습(Supervised Fine-Tuning)을 통해 CoE의 추론 구조를 주입합니다. 이후, 전용 보상 모델에 의해 안내되는 RL은 최종 응답의 치료적 관련성과 맥락적 적절성을 정제합니다. 실험 결과, Empathy-R1은 주요 자동화 지표에서 강력한 성능을 달성했습니다. 더 중요한 것은, 인간 평가에서 강력한 기준 모델들에 비해 Empathy-R1의 우월성이 확인되었으며, 새로운 벤치마크에서 44.30%의 Win@1 비율을 기록했습니다. 해석 가능하고 맥락적으로 세밀한 응답을 가능하게 함으로써, Empathy-R1은 정신 건강 지원을 위한 책임 있고 진정으로 유익한 인공지능 개발에 있어 중요한 진전을 나타냅니다.

## 📝 요약

Empathy-R1은 장문 상담 텍스트(LCTs)에 대한 효과적인 심리적 지원을 위해 개발된 프레임워크로, 기존 대형 언어 모델의 한계를 극복하고자 합니다. 이 모델은 Chain-of-Empathy(CoE) 추론 과정과 강화 학습(RL)을 결합하여 응답의 질을 향상시킵니다. CoE는 인지행동치료에서 영감을 받아, 도움을 요청하는 사람의 감정, 원인, 의도를 순차적으로 추론하여 투명하고 해석 가능한 사고 과정을 제공합니다. Empathy-QA라는 대규모 중국어 데이터셋과 두 단계의 훈련 과정을 통해 CoE의 추론 구조를 학습하고, RL로 최종 응답의 치료적 관련성과 맥락 적합성을 강화합니다. 실험 결과, Empathy-R1은 자동 평가 지표에서 높은 성능을 보였으며, 인간 평가에서도 강력한 기준 모델을 능가하여 Win@1 비율 44.30%를 기록했습니다. 이는 정신 건강 지원을 위한 책임감 있고 유익한 AI 개발에 중요한 진전을 나타냅니다.

## 🎯 주요 포인트

- 1. Empathy-R1은 Chain-of-Empathy (CoE) 추론 과정과 강화 학습(RL)을 통합하여 장문 상담 텍스트(LCTs)에 대한 응답 품질을 향상시키는 새로운 프레임워크입니다.

- 2. CoE 패러다임은 인지 행동 치료에서 영감을 받아 도움을 요청하는 사람의 감정, 원인, 의도를 순차적으로 추론하여 투명하고 해석 가능한 사고 과정을 제공합니다.

- 3. Empathy-R1은 새로운 대규모 중국어 데이터셋 Empathy-QA와 두 단계의 훈련 과정을 통해 강화됩니다.

- 4. 실험 결과 Empathy-R1은 주요 자동 평가 지표에서 강력한 성능을 보였으며, 인간 평가에서도 강력한 기준 모델들보다 우수하다는 것이 확인되었습니다.

- 5. Empathy-R1은 해석 가능하고 맥락적으로 세밀한 응답을 가능하게 하여 정신 건강 지원을 위한 책임감 있고 유익한 AI 개발에 중요한 진전을 나타냅니다.

---

*Generated on 2025-09-20 02:46:51*