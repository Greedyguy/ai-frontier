
# SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction

**Korean Title:** SMART: 문항 반응 이론에 맞춘 시뮬레이션 학생을 통한 문제 난이도 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Direct Preference Optimization

## 🔗 유사한 논문
- [[SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (81.4% similar)
- [[A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (80.1% similar)
- [[From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (79.9% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (79.2% similar)
- [[OnlineMate An LLM-Based Multi-Agent Companion System for Cognitive Support in Online Learning]] (78.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.05129v2 Announce Type: replace-cross 
Abstract: Item (question) difficulties play a crucial role in educational assessments, enabling accurate and efficient assessment of student abilities and personalization to maximize learning outcomes. Traditionally, estimating item difficulties can be costly, requiring real students to respond to items, followed by fitting an item response theory (IRT) model to get difficulty estimates. This approach cannot be applied to the cold-start setting for previously unseen items either. In this work, we present SMART (Simulated Students Aligned with IRT), a novel method for aligning simulated students with instructed ability, which can then be used in simulations to predict the difficulty of open-ended items. We achieve this alignment using direct preference optimization (DPO), where we form preference pairs based on how likely responses are under a ground-truth IRT model. We perform a simulation by generating thousands of responses, evaluating them with a large language model (LLM)-based scoring model, and fit the resulting data to an IRT model to obtain item difficulty estimates. Through extensive experiments on two real-world student response datasets, we show that SMART outperforms other item difficulty prediction methods by leveraging its improved ability alignment.

## 🔍 Abstract (한글 번역)

arXiv:2507.05129v2 발표 유형: 교차 대체  
초록: 문항(질문) 난이도는 교육 평가에서 중요한 역할을 하며, 학생의 능력을 정확하고 효율적으로 평가하고 학습 결과를 극대화하기 위해 개인화하는 데 기여합니다. 전통적으로 문항 난이도를 추정하는 것은 비용이 많이 들며, 실제 학생들이 문항에 응답한 후 문항 반응 이론(IRT) 모델을 적용하여 난이도 추정치를 얻어야 합니다. 이 접근법은 이전에 보지 못한 문항에 대한 콜드 스타트 설정에는 적용할 수 없습니다. 본 연구에서는 SMART(Simulated Students Aligned with IRT)라는 새로운 방법을 제시하여, 주어진 능력에 맞춘 시뮬레이션 학생들을 정렬하고, 이를 시뮬레이션에서 사용하여 개방형 문항의 난이도를 예측할 수 있습니다. 우리는 직접 선호 최적화(DPO)를 사용하여 이 정렬을 달성하며, 이는 실제 IRT 모델 하에서 응답이 얼마나 가능성이 있는지를 기반으로 선호 쌍을 형성합니다. 우리는 수천 개의 응답을 생성하고, 이를 대형 언어 모델(LLM) 기반 채점 모델로 평가한 후, 결과 데이터를 IRT 모델에 맞춰 문항 난이도 추정치를 얻는 시뮬레이션을 수행합니다. 두 개의 실제 학생 응답 데이터셋에 대한 광범위한 실험을 통해, SMART가 향상된 능력 정렬을 활용하여 다른 문항 난이도 예측 방법보다 뛰어나다는 것을 보여줍니다.

## 📝 요약

이 논문은 교육 평가에서 중요한 역할을 하는 문항 난이도 추정을 위한 새로운 방법론인 SMART(Simulated Students Aligned with IRT)를 제안합니다. 기존의 문항 난이도 추정 방법은 실제 학생들의 응답을 필요로 하여 비용이 많이 들고, 새로운 문항에 대한 초기 설정에서는 적용하기 어렵습니다. SMART는 지시된 능력에 맞게 시뮬레이션된 학생들을 정렬하여, 개방형 문항의 난이도를 예측할 수 있도록 합니다. 이를 위해 직접 선호 최적화(DPO)를 사용하여 실제 IRT 모델 하에서 응답 가능성을 기반으로 선호 쌍을 형성합니다. 수천 개의 응답을 생성하고, 대형 언어 모델(LLM) 기반의 채점 모델로 평가한 후, IRT 모델에 맞춰 문항 난이도를 추정합니다. 두 개의 실제 학생 응답 데이터셋에 대한 실험 결과, SMART는 향상된 능력 정렬을 통해 다른 문항 난이도 예측 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. SMART는 시뮬레이션된 학생을 사용하여 새로운 문항의 난이도를 예측하는 혁신적인 방법을 제시합니다.

- 2. 이 방법은 직접 선호 최적화(DPO)를 통해 시뮬레이션된 학생의 능력을 정렬하여 문항 난이도를 예측합니다.

- 3. 대규모 언어 모델(LLM)을 기반으로 한 채점 모델을 사용하여 생성된 응답을 평가하고, IRT 모델에 적합시켜 난이도 추정치를 얻습니다.

- 4. 두 개의 실제 학생 응답 데이터셋에 대한 실험을 통해 SMART가 다른 난이도 예측 방법보다 우수한 성능을 보임을 입증했습니다.

---

*Generated on 2025-09-19 15:46:20*