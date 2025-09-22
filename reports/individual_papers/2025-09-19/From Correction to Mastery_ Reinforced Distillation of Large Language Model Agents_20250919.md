
# From Correction to Mastery: Reinforced Distillation of Large Language Model Agents

**Korean Title:** 교정에서 숙달로: 대형 언어 모델 에이전트의 강화 증류

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Student-centered Framework

## 🔗 유사한 논문
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (85.6% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (82.3% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (81.0% similar)
- [[(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (80.5% similar)
- [[THOR Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (80.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14257v1 Announce Type: cross 
Abstract: Large Language Model agents excel at solving complex tasks through iterative reasoning and tool use, but typically depend on ultra-large, costly backbones. Existing distillation approaches train smaller students to imitate full teacher trajectories, yet reasoning and knowledge gaps between the teacher and student often lead to compounding errors. We propose SCoRe, a student-centered framework in which the student generates trajectories and the teacher intervenes only at the first critical error, producing training data matched to the student's ability and exposing specific weaknesses. The student is first fine-tuned on corrected trajectories. Subsequently, short-horizon reinforcement learning starts from the verified prefix before the first critical error, with target rewards assigned at that step. This design encourages autonomous problem-solving beyond imitation and improves training stability. Particularly, on 12 challenging benchmarks, a 7B-parameter student distilled with SCoRe matches the agentic performance of a 72B-parameter teacher.

## 🔍 Abstract (한글 번역)

arXiv:2509.14257v1 발표 유형: 교차  
초록: 대형 언어 모델 에이전트는 반복적인 추론과 도구 사용을 통해 복잡한 작업을 해결하는 데 뛰어나지만, 일반적으로 초대형이고 비용이 많이 드는 백본에 의존합니다. 기존의 증류 접근법은 작은 학생 모델이 전체 교사 경로를 모방하도록 훈련하지만, 교사와 학생 간의 추론 및 지식 격차로 인해 오류가 누적되는 경우가 많습니다. 우리는 학생이 경로를 생성하고 교사가 첫 번째 중요한 오류에서만 개입하여 학생의 능력에 맞춘 훈련 데이터를 생성하고 특정 약점을 드러내는 학생 중심의 프레임워크인 SCoRe를 제안합니다. 학생은 먼저 수정된 경로에 대해 미세 조정됩니다. 이후, 단기 강화 학습은 첫 번째 중요한 오류 이전의 검증된 접두사에서 시작되며, 해당 단계에서 목표 보상이 할당됩니다. 이 설계는 모방을 넘어선 자율적인 문제 해결을 장려하고 훈련의 안정성을 향상시킵니다. 특히, 12개의 도전적인 벤치마크에서 SCoRe로 증류된 7B-매개변수 학생은 72B-매개변수 교사의 에이전트 성능과 일치합니다.

## 📝 요약

이 논문에서는 대형 언어 모델의 복잡한 문제 해결 능력을 작은 모델에서도 구현하기 위한 새로운 접근법인 SCoRe를 제안합니다. 기존의 지식 증류 방법은 큰 모델의 행동을 모방하도록 작은 모델을 훈련하지만, 이 과정에서 발생하는 오류가 누적되는 문제가 있습니다. SCoRe는 학생 모델이 스스로 경로를 생성하고, 교사는 첫 번째 중요한 오류에서만 개입하여 학생의 능력에 맞춘 훈련 데이터를 제공합니다. 이후, 수정된 경로로 미세 조정하고, 강화 학습을 통해 자율 문제 해결 능력을 향상시킵니다. 이 방법은 7B-파라미터 학생 모델이 72B-파라미터 교사 모델의 성능에 근접하게 합니다.

## 🎯 주요 포인트

- 1. SCoRe는 학생 중심의 프레임워크로, 학생이 경로를 생성하고 교사는 첫 번째 중요한 오류에서만 개입하여 학생의 능력에 맞춘 훈련 데이터를 제공합니다.

- 2. 학생은 수정된 경로로 미세 조정된 후, 첫 번째 중요한 오류 이전의 검증된 접두사에서 시작하는 단기 강화 학습을 통해 자율적 문제 해결을 장려합니다.

- 3. SCoRe는 모방을 넘어서는 자율적 문제 해결을 장려하며 훈련의 안정성을 향상시킵니다.

- 4. SCoRe를 통해 증류된 7B-파라미터 학생 모델은 72B-파라미터 교사 모델의 성능을 맞추는 데 성공했습니다.

- 5. SCoRe는 12개의 도전적인 벤치마크에서 뛰어난 성능을 보여주었습니다.

---

*Generated on 2025-09-19 14:51:24*