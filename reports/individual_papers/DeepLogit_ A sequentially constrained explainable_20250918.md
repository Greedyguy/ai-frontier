
# DeepLogit: A sequentially constrained explainable deep learning modeling approach for transport policy analysis

**Korean Title:** 딥로짓: 교통 정책 분석을 위한 순차적 제약 조건이 있는 설명 가능한 딥러닝 모델링 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Theory-based Discrete Choice Model|Theory-based Discrete Choice Model]] [[keywords/broad/Deep Learning|Deep Learning]] [[keywords/broad/Transport Policy Analysis|Transport Policy Analysis]] [[keywords/specific/Convolutional Neural Network|Convolutional Neural Network]] [[keywords/unique/DeepLogit|DeepLogit]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Theory-based Discrete Choice Model
**🔬 Broad Technical**: Deep Learning, Transport Policy Analysis
**🔗 Specific Connectable**: Convolutional Neural Network
**⭐ Unique Technical**: DeepLogit

**ArXiv ID**: [2509.13633](https://arxiv.org/abs/2509.13633)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13633.pdf)


## 🏷️ 추출된 키워드



`Deep Learning` • 

`Transport Policy Analysis` • 

`Convolutional Neural Network` • 

`DeepLogit` • 

`Theory-based Discrete Choice Model`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13633v1 Announce Type: cross 
Abstract: Despite the significant progress of deep learning models in multitude of applications, their adaption in planning and policy related areas remains challenging due to the black-box nature of these models. In this work, we develop a set of DeepLogit models that follow a novel sequentially constrained approach in estimating deep learning models for transport policy analysis. In the first step of the proposed approach, we estimate a convolutional neural network (CNN) model with only linear terms, which is equivalent of a linear-in-parameter multinomial logit model. We then estimate other deep learning models by constraining the parameters that need interpretability at the values obtained in the linear-in-parameter CNN model and including higher order terms or by introducing advanced deep learning architectures like Transformers. Our approach can retain the interpretability of the selected parameters, yet provides significantly improved model accuracy than the discrete choice model. We demonstrate our approach on a transit route choice example using real-world transit smart card data from Singapore. This study shows the potential for a unifying approach, where theory-based discrete choice model (DCM) and data-driven AI models can leverage each other's strengths in interpretability and predictive power. With the availability of larger datasets and more complex constructions, such approach can lead to more accurate models using discrete choice models while maintaining its applicability in planning and policy-related areas. Our code is available on https://github.com/jeremyoon/route-choice/ .

## 🔍 Abstract (한글 번역)

arXiv:2509.13633v1 발표 유형: 교차
요약: 다양한 응용 분야에서 딥 러닝 모델의 중요한 발전에도 불구하고, 이러한 모델의 블랙박스 성격으로 인해 계획 및 정책 관련 분야에서의 적응은 여전히 어려운 문제입니다. 본 연구에서는 교통 정책 분석을 위해 딥 러닝 모델을 추정하는 새로운 순차 제약 접근 방식을 따르는 DeepLogit 모델 세트를 개발합니다. 제안된 방법의 첫 번째 단계에서는 선형 항만을 포함하는 합성곱 신경망 (CNN) 모델을 추정하며, 이는 매개변수에 대해 선형인 다항 로짓 모델과 동등합니다. 그런 다음, 선형 매개변수 CNN 모델에서 해석 가능성이 필요한 매개변수를 제약하고 고차항을 포함하거나 Transformer와 같은 고급 딥 러닝 아키텍처를 도입하여 다른 딥 러닝 모델을 추정합니다. 우리의 접근 방식은 선택된 매개변수의 해석 가능성을 유지하면서 이산 선택 모델보다 훨씬 개선된 모델 정확도를 제공합니다. 우리는 싱가포르의 실제 대중 교통 스마트 카드 데이터를 사용하여 대중 교통 경로 선택 예제에서 우리의 접근 방식을 시연합니다. 본 연구는 이론 기반의 이산 선택 모델 (DCM)과 데이터 기반의 AI 모델이 상호간의 해석 가능성과 예측력을 활용할 수 있는 통합적인 접근 방식의 잠재력을 보여줍니다. 더 큰 데이터셋과 더 복잡한 구성물의 가용성으로 인해, 이러한 접근 방식은 계획 및 정책 관련 분야에서의 적용 가능성을 유지하면서 이산 선택 모델을 사용한 보다 정확한 모델로 이어질 수 있습니다. 우리의 코드는 https://github.com/jeremyoon/route-choice/ 에서 사용할 수 있습니다.

## 📝 요약

이 연구는 교통 정책 분석을 위해 딥러닝 모델을 추정하는 새로운 순차적 제약 방법론을 제안한다. 선형 항만을 사용하는 합리적 다항 로짓 모델과 같은 선형 파라미터 CNN 모델을 추정한 후, 해석 가능한 파라미터를 제약하고 고차항을 포함하거나 Transformer와 같은 고급 딥러닝 구조를 도입하여 다른 딥러닝 모델을 추정한다. 이 방법은 선택된 파라미터의 해석 가능성을 유지하면서 이산 선택 모델보다 훨씬 더 향상된 모델 정확도를 제공한다. 우리는 시모르트 카드 데이터를 사용하여 대중교통 경로 선택 예시에 우리의 방법을 시연하였다. 결과는 이산 선택 모델과 데이터 기반 AI 모델이 상호보완적으로 작용하여 더 정확한 모델을 구축할 수 있음을 보여준다.

## 🎯 주요 포인트


- 교통 정책 분석을 위한 DeepLogit 모델 개발

- 선형 항만을 사용한 CNN 모델을 통해 해석 가능한 매개변수 추정

- 이해력 유지 및 예측력 향상을 위한 고급 딥러닝 아키텍처 도입

- 이산 선택 모델보다 더 정확한 모델 제시를 통한 이론 기반 모델과 데이터 기반 AI 모델의 융합 가능성 제시


---

*Generated on 2025-09-18 16:20:59*