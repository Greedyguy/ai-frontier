# Empathy-R1: A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support

**Korean Title:** 공감-R1: 장기 정신 건강 지원을 위한 공감 연쇄 및 강화 학습 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretable AI for Mental Health

## 🔗 유사한 논문
- [[2025-09-18/Empathy-R1_ A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support_20250918|Empathy-R1 A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support]] (99.3% similar)
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (82.1% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1 Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (80.9% similar)
- [[2025-09-22/A Layered Multi-Expert Framework for Long-Context Mental Health Assessments_20250922|A Layered Multi-Expert Framework for Long-Context Mental Health Assessments]] (80.8% similar)
- [[2025-09-22/CCrepairBench_ A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair_20250922|CCrepairBench A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair]] (80.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14851v2 Announce Type: replace-cross 
Abstract: Empathy is critical for effective mental health support, especially when addressing Long Counseling Texts (LCTs). However, existing Large Language Models (LLMs) often generate replies that are semantically fluent but lack the structured reasoning necessary for genuine psychological support, particularly in a Chinese context. To bridge this gap, we introduce Empathy-R1, a novel framework that integrates a Chain-of-Empathy (CoE) reasoning process with Reinforcement Learning (RL) to enhance response quality for LCTs. Inspired by cognitive-behavioral therapy, our CoE paradigm guides the model to sequentially reason about a help-seeker's emotions, causes, and intentions, making its thinking process both transparent and interpretable. Our framework is empowered by a new large-scale Chinese dataset, Empathy-QA, and a two-stage training process. First, Supervised Fine-Tuning instills the CoE's reasoning structure. Subsequently, RL, guided by a dedicated reward model, refines the therapeutic relevance and contextual appropriateness of the final responses. Experiments show that Empathy-R1 achieves strong performance on key automatic metrics. More importantly, human evaluations confirm its superiority, showing a clear preference over strong baselines and achieving a Win@1 rate of 44.30% on our new benchmark. By enabling interpretable and contextually nuanced responses, Empathy-R1 represents a significant advancement in developing responsible and genuinely beneficial AI for mental health support.

## 🔍 Abstract (한글 번역)

arXiv:2509.14851v2 발표 유형: 교차 교체  
초록: 공감은 효과적인 정신 건강 지원에 있어 매우 중요하며, 특히 긴 상담 텍스트(Long Counseling Texts, LCTs)를 다룰 때 더욱 그렇습니다. 그러나 기존의 대형 언어 모델(Large Language Models, LLMs)은 의미적으로 유창한 답변을 생성하지만, 특히 중국어 맥락에서 진정한 심리적 지원에 필요한 구조화된 추론이 부족한 경우가 많습니다. 이러한 격차를 해소하기 위해 우리는 Empathy-R1이라는 새로운 프레임워크를 소개합니다. 이 프레임워크는 공감의 연쇄(Chain-of-Empathy, CoE) 추론 과정을 강화 학습(Reinforcement Learning, RL)과 통합하여 LCT에 대한 응답 품질을 향상시킵니다. 인지행동치료에서 영감을 받은 우리의 CoE 패러다임은 모델이 도움을 구하는 사람의 감정, 원인 및 의도를 순차적으로 추론하도록 안내하여 사고 과정을 투명하고 해석 가능하게 만듭니다. 우리의 프레임워크는 새로운 대규모 중국어 데이터셋인 Empathy-QA와 2단계 훈련 과정을 통해 강화됩니다. 먼저, 지도 학습을 통한 미세 조정(Supervised Fine-Tuning)을 통해 CoE의 추론 구조를 주입합니다. 이후, 전용 보상 모델이 안내하는 RL을 통해 최종 응답의 치료적 관련성과 맥락적 적절성을 정제합니다. 실험 결과, Empathy-R1은 주요 자동화 지표에서 강력한 성능을 달성했습니다. 더 중요한 것은, 인간 평가에서 강력한 기준 모델들보다 명확한 선호도를 보여주며, 새로운 벤치마크에서 Win@1 비율 44.30%를 달성하여 그 우월성을 확인했습니다. 해석 가능하고 맥락적으로 세밀한 응답을 가능하게 함으로써, Empathy-R1은 정신 건강 지원을 위한 책임감 있고 진정으로 유익한 AI 개발에 있어 중요한 진전을 나타냅니다.

## 📝 요약

Empathy-R1은 긴 상담 텍스트(LCTs)에 대한 효과적인 심리 지원을 위해 개발된 새로운 프레임워크로, 기존 대형 언어 모델의 한계를 극복하고자 합니다. 이 모델은 Chain-of-Empathy(CoE) 추론 과정과 강화 학습(RL)을 통합하여 응답의 질을 향상시킵니다. CoE는 인지행동치료에서 영감을 받아, 도움을 요청하는 사람의 감정, 원인, 의도를 순차적으로 추론하여 투명하고 해석 가능한 사고 과정을 제공합니다. Empathy-QA라는 대규모 중국어 데이터셋과 두 단계의 학습 과정을 통해 CoE의 구조를 학습하고, RL로 최종 응답의 치료적 관련성과 맥락 적합성을 개선합니다. 실험 결과, Empathy-R1은 자동 평가 지표에서 우수한 성능을 보였으며, 인간 평가에서도 강력한 기준 모델들을 능가하여 Win@1 비율 44.30%를 기록했습니다. 이를 통해 Empathy-R1은 책임감 있고 유익한 AI 개발에 중요한 진전을 이뤘습니다.

## 🎯 주요 포인트

- 1. Empathy-R1은 Long Counseling Texts(LCTs)에 대한 응답 품질을 향상시키기 위해 Chain-of-Empathy(CoE) 추론 과정과 강화 학습(RL)을 통합한 새로운 프레임워크입니다.

- 2. CoE 패러다임은 인지행동치료에서 영감을 받아, 도움을 요청하는 사람의 감정, 원인, 의도를 순차적으로 추론하여 모델의 사고 과정을 투명하고 해석 가능하게 만듭니다.

- 3. Empathy-R1은 새로운 대규모 중국어 데이터셋 Empathy-QA와 두 단계의 훈련 과정을 통해 강화되었습니다.

- 4. 실험 결과, Empathy-R1은 주요 자동 평가 지표에서 강력한 성능을 보였으며, 인간 평가에서도 기존 강력한 기준 모델들보다 우수하다는 것이 확인되었습니다.

- 5. Empathy-R1은 해석 가능하고 맥락적으로 세밀한 응답을 가능하게 하여, 정신 건강 지원을 위한 책임 있고 진정으로 유익한 AI 개발에 중요한 발전을 나타냅니다.

---

*Generated on 2025-09-22 15:06:54*