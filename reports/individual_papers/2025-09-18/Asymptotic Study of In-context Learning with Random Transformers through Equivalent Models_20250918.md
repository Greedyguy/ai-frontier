# Asymptotic Study of In-context Learning with Random Transformers through Equivalent Models

**Korean Title:** 랜덤 트랜스포머를 통한 맥락 내 학습의 점근적 연구: 동등 모델을 통한 접근

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Samet Demir|Samet Demir]] [[authors/Zafer Dogan|Zafer Dogan]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Double-descent Phenomenon

## 🔗 유사한 논문
- [[TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (77.8% similar)
- [[Hierarchical Learning for Maze Navigation_ Emergence of Mental Representations via Second-Order Learning_20250917|Hierarchical Learning for Maze Navigation Emergence of Mental Representations via Second-Order Learning]] (77.6% similar)
- [[Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (77.2% similar)
- [[Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (77.1% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (77.0% similar)

## 📋 저자 정보

**Authors:** Samet Demir, Zafer Dogan

## 📄 Abstract (원문)

We study the in-context learning (ICL) capabilities of pretrained
Transformers in the setting of nonlinear regression. Specifically, we focus on
a random Transformer with a nonlinear MLP head where the first layer is
randomly initialized and fixed while the second layer is trained. Furthermore,
we consider an asymptotic regime where the context length, input dimension,
hidden dimension, number of training tasks, and number of training samples
jointly grow. In this setting, we show that the random Transformer behaves
equivalent to a finite-degree Hermite polynomial model in terms of ICL error.
This equivalence is validated through simulations across varying activation
functions, context lengths, hidden layer widths (revealing a double-descent
phenomenon), and regularization settings. Our results offer theoretical and
empirical insights into when and how MLP layers enhance ICL, and how
nonlinearity and over-parameterization influence model performance.

## 🔍 Abstract (한글 번역)

비선형 회귀 설정에서 사전 학습된 트랜스포머의 맥락 내 학습(ICL) 능력을 연구합니다. 구체적으로, 우리는 첫 번째 층이 무작위로 초기화되고 고정되는 비선형 MLP 헤드를 가진 무작위 트랜스포머에 초점을 맞추며, 두 번째 층은 훈련됩니다. 또한, 맥락 길이, 입력 차원, 은닉 차원, 훈련 과제의 수, 훈련 샘플의 수가 함께 증가하는 점근적 체제를 고려합니다. 이 설정에서, 우리는 무작위 트랜스포머가 ICL 오류 측면에서 유한 차수의 에르미트 다항식 모델과 동등하게 작용함을 보여줍니다. 이 동등성은 다양한 활성화 함수, 맥락 길이, 은닉층 너비(이중 하강 현상을 드러냄), 정규화 설정에 걸친 시뮬레이션을 통해 검증됩니다. 우리의 결과는 MLP 층이 언제 그리고 어떻게 ICL을 향상시키는지, 그리고 비선형성과 과매개변수가 모델 성능에 어떻게 영향을 미치는지에 대한 이론적 및 실증적 통찰을 제공합니다.

## 📝 요약

이 논문은 비선형 회귀 환경에서 사전 학습된 트랜스포머의 문맥 학습(ICL) 능력을 연구합니다. 랜덤 트랜스포머와 비선형 MLP 헤드를 사용하여, 첫 번째 층은 랜덤 초기화 후 고정하고 두 번째 층은 학습합니다. 문맥 길이, 입력 차원, 숨겨진 차원, 학습 과제 수, 샘플 수가 함께 증가하는 비대칭적 환경에서, 랜덤 트랜스포머가 유한 차수의 에르미트 다항식 모델과 ICL 오류 측면에서 동등하게 작동함을 보여줍니다. 다양한 활성화 함수, 문맥 길이, 숨겨진 층 너비, 정규화 설정을 통해 시뮬레이션으로 검증하였으며, MLP 층이 ICL을 강화하는 조건과 비선형성 및 과매개변수가 모델 성능에 미치는 영향을 이론적, 경험적으로 제공합니다.

## 🎯 주요 포인트

- 1. 비선형 회귀 설정에서 사전 학습된 트랜스포머의 문맥 내 학습(ICL) 능력을 연구했습니다.

- 2. 무작위로 초기화된 첫 번째 층과 학습된 두 번째 층을 가진 비선형 MLP 헤드의 랜덤 트랜스포머를 중심으로 연구를 진행했습니다.

- 3. 문맥 길이, 입력 차원, 은닉 차원, 학습 과제 수, 학습 샘플 수가 함께 증가하는 비대칭적 상황을 고려했습니다.

- 4. 랜덤 트랜스포머가 유한 차수의 에르미트 다항식 모델과 ICL 오류 측면에서 동등하게 작동함을 보였습니다.

- 5. 다양한 활성화 함수, 문맥 길이, 은닉층 너비, 정규화 설정에서의 시뮬레이션을 통해 이 동등성을 검증했습니다.

---

*Generated on 2025-09-20 00:56:54*