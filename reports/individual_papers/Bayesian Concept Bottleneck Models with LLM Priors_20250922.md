# Bayesian Concept Bottleneck Models with LLM Priors

**Korean Title:** 베이지안 개념 병목 모델과 대형 언어 모델 사전 분포

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretability Accuracy Tradeoff

## 🔗 유사한 논문
- [[2025-09-19/EnCoBo_ Energy-Guided Concept Bottlenecks for Interpretable Generation_20250919|EnCoBo Energy-Guided Concept Bottlenecks for Interpretable Generation]] (83.7% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (80.4% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (80.1% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (79.9% similar)
- [[2025-09-22/KITE_ Kernelized and Information Theoretic Exemplars for In-Context Learning_20250922|KITE Kernelized and Information Theoretic Exemplars for In-Context Learning]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.15555v2 Announce Type: replace-cross 
Abstract: Concept Bottleneck Models (CBMs) have been proposed as a compromise between white-box and black-box models, aiming to achieve interpretability without sacrificing accuracy. The standard training procedure for CBMs is to predefine a candidate set of human-interpretable concepts, extract their values from the training data, and identify a sparse subset as inputs to a transparent prediction model. However, such approaches are often hampered by the tradeoff between exploring a sufficiently large set of concepts versus controlling the cost of obtaining concept extractions, resulting in a large interpretability-accuracy tradeoff. This work investigates a novel approach that sidesteps these challenges: BC-LLM iteratively searches over a potentially infinite set of concepts within a Bayesian framework, in which Large Language Models (LLMs) serve as both a concept extraction mechanism and prior. Even though LLMs can be miscalibrated and hallucinate, we prove that BC-LLM can provide rigorous statistical inference and uncertainty quantification. Across image, text, and tabular datasets, BC-LLM outperforms interpretable baselines and even black-box models in certain settings, converges more rapidly towards relevant concepts, and is more robust to out-of-distribution samples.

## 🔍 Abstract (한글 번역)

arXiv:2410.15555v2 발표 유형: 교체-교차  
초록: 개념 병목 모델(CBMs)은 해석 가능성과 정확성을 동시에 달성하기 위한 절충안으로, 화이트박스와 블랙박스 모델 사이의 타협점으로 제안되었습니다. CBMs의 표준 학습 절차는 인간이 해석할 수 있는 개념의 후보 집합을 미리 정의하고, 학습 데이터에서 그 값을 추출한 후, 투명한 예측 모델의 입력으로 사용할 희소한 부분 집합을 식별하는 것입니다. 그러나 이러한 접근 방식은 충분히 큰 개념 집합을 탐색하는 것과 개념 추출 비용을 제어하는 것 사이의 균형을 맞추기 어려워, 해석 가능성과 정확성 간의 큰 트레이드오프가 발생하는 경우가 많습니다. 본 연구는 이러한 문제를 우회하는 새로운 접근 방식을 조사합니다: BC-LLM은 베이지안 프레임워크 내에서 잠재적으로 무한한 개념 집합을 반복적으로 탐색하며, 대형 언어 모델(LLM)이 개념 추출 메커니즘과 사전으로 작용합니다. LLM이 잘못 조정되거나 환상을 일으킬 수 있음에도 불구하고, 우리는 BC-LLM이 엄격한 통계적 추론과 불확실성 정량화를 제공할 수 있음을 증명합니다. 이미지, 텍스트, 표 형식 데이터셋 전반에 걸쳐, BC-LLM은 해석 가능한 기준 모델과 특정 설정에서 블랙박스 모델을 능가하며, 관련 개념에 더 빠르게 수렴하고, 분포 외 샘플에 더 강인합니다.

## 📝 요약

이 논문은 해석 가능성과 정확성을 동시에 추구하는 Concept Bottleneck Models(CBMs)의 한계를 극복하기 위한 새로운 접근법을 제안합니다. 기존 CBMs는 해석 가능한 개념 집합을 미리 정의하고 이를 예측 모델의 입력으로 사용하는데, 이는 개념 탐색 범위와 비용 간의 균형 문제를 야기합니다. 본 연구에서는 BC-LLM이라는 새로운 방법을 제안하여, 대형 언어 모델(LLMs)을 활용해 무한한 개념 집합을 탐색하고, 베이지안 프레임워크 내에서 개념 추출과 사전 정보를 제공합니다. BC-LLM은 LLM의 한계에도 불구하고 통계적 추론과 불확실성 정량화를 가능하게 하며, 이미지, 텍스트, 표 형식 데이터에서 해석 가능한 모델과 블랙박스 모델을 능가하는 성능을 보입니다. 또한, 관련 개념으로의 수렴이 빠르고, 분포 밖 샘플에 대한 강건성을 보입니다.

## 🎯 주요 포인트

- 1. Concept Bottleneck Models (CBMs)는 해석 가능성과 정확성을 동시에 추구하는 모델로, 인간이 해석할 수 있는 개념을 미리 정의하여 투명한 예측 모델의 입력으로 사용하는 방식이다.

- 2. 기존 CBM 접근법은 개념 집합의 크기와 개념 추출 비용 간의 균형을 맞추는 데 어려움을 겪으며, 해석 가능성과 정확성 간의 큰 트레이드오프가 발생한다.

- 3. BC-LLM은 Bayesian 프레임워크 내에서 대형 언어 모델(LLM)을 개념 추출 메커니즘 및 사전으로 사용하여 무한한 개념 집합을 탐색하는 새로운 접근법을 제안한다.

- 4. BC-LLM은 이미지, 텍스트, 테이블 데이터셋에서 해석 가능한 기준 모델 및 일부 설정에서 블랙박스 모델보다 우수한 성능을 보이며, 관련 개념으로의 수렴 속도가 빠르고 분포 외 샘플에 대한 강건성을 가진다.

- 5. LLM이 잘못 조정되거나 환상을 일으킬 수 있음에도 불구하고, BC-LLM은 엄격한 통계적 추론과 불확실성 정량화를 제공할 수 있음을 입증한다.

---

*Generated on 2025-09-22 14:40:04*