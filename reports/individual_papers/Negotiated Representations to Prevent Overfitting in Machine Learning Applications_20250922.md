# Negotiated Representations to Prevent Overfitting in Machine Learning Applications

**Korean Title:** 기계 학습 응용에서 과적합을 방지하기 위한 협상된 표현

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Continual Learning|Continual Learning]] [[keywords/specific/Overfitting Prevention|Overfitting Prevention]] [[keywords/broad/Machine Learning|Machine Learning]] [[keywords/broad/Classification|Classification]] [[keywords/unique/Negotiation Paradigm|Negotiation Paradigm]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (83.8% similar) [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (82.8% similar) [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Continual Learning
**🔗 Specific Connectable**: Overfitting Prevention
**🔬 Broad Technical**: Machine Learning
**⭐ Unique Technical**: Negotiation Paradigm
## 🔗 유사한 논문
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (83.8% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (82.8% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (82.4% similar)
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (81.2% similar)
- [[2025-09-22/Latent learning_ episodic memory complements parametric learning by enabling flexible reuse of experiences_20250922|Latent learning episodic memory complements parametric learning by enabling flexible reuse of experiences]] (81.0% similar)


**ArXiv ID**: [2311.11410](https://arxiv.org/abs/2311.11410)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2311.11410.pdf)


**ArXiv ID**: [2311.11410](https://arxiv.org/abs/2311.11410)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2311.11410.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Continual Learning
**🔗 Specific Connectable**: Overfitting Prevention
**⭐ Unique Technical**: Negotiation Paradigm
**🔬 Broad Technical**: Machine Learning, Classification

## 🏷️ 추출된 키워드



`Machine Learning` • 

`Classification` • 

`Overfitting Prevention` • 

`Negotiation Paradigm` • 

`Continual Learning`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2311.11410v2 Announce Type: replace 
Abstract: Overfitting is a phenomenon that occurs when a machine learning model is trained for too long and focused too much on the exact fitness of the training samples to the provided training labels and cannot keep track of the predictive rules that would be useful on the test data. This phenomenon is commonly attributed to memorization of particular samples, memorization of the noise, and forced fitness into a data set of limited samples by using a high number of neurons. While it is true that the model encodes various peculiarities as the training process continues, we argue that most of the overfitting occurs in the process of reconciling sharply defined membership ratios. In this study, we present an approach that increases the classification accuracy of machine learning models by allowing the model to negotiate output representations of the samples with previously determined class labels. By setting up a negotiation between the models interpretation of the inputs and the provided labels, we not only increased average classification accuracy but also decreased the rate of overfitting without applying any other regularization tricks. By implementing our negotiation paradigm approach to several low regime machine learning problems by generating overfitting scenarios from publicly available data sets such as CIFAR 10, CIFAR 100, and MNIST we have demonstrated that the proposed paradigm has more capacity than its intended purpose. We are sharing the experimental results and inviting the machine learning community to explore the limits of the proposed paradigm. We also aim to incentive the community to exploit the negotiation paradigm to overcome the learning related challenges in other research fields such as continual learning. The Python code of the experimental setup is uploaded to GitHub.

## 🔍 Abstract (한글 번역)

arXiv:2311.11410v2 발표 유형: 교체  
초록: 과적합은 기계 학습 모델이 너무 오래 훈련되어 제공된 훈련 레이블에 훈련 샘플의 정확한 적합성에 너무 집중하여 테스트 데이터에 유용한 예측 규칙을 추적할 수 없을 때 발생하는 현상입니다. 이 현상은 일반적으로 특정 샘플의 암기, 노이즈의 암기, 많은 수의 뉴런을 사용하여 제한된 샘플의 데이터 세트에 강제로 적합시키는 것에 기인합니다. 훈련 과정이 계속됨에 따라 모델이 다양한 특이점을 인코딩한다는 것은 사실이지만, 우리는 대부분의 과적합이 명확하게 정의된 멤버십 비율을 조정하는 과정에서 발생한다고 주장합니다. 본 연구에서는 모델이 이전에 결정된 클래스 레이블과 샘플의 출력 표현을 협상할 수 있도록 하여 기계 학습 모델의 분류 정확성을 높이는 접근법을 제시합니다. 입력에 대한 모델의 해석과 제공된 레이블 간의 협상을 설정함으로써, 우리는 평균 분류 정확도를 높였을 뿐만 아니라 다른 정규화 기법을 적용하지 않고도 과적합 비율을 감소시켰습니다. CIFAR 10, CIFAR 100, MNIST와 같은 공개 데이터 세트에서 과적합 시나리오를 생성하여 여러 저레짐 기계 학습 문제에 우리의 협상 패러다임 접근법을 구현함으로써, 제안된 패러다임이 의도된 목적 이상으로 더 많은 역량을 가지고 있음을 입증했습니다. 우리는 실험 결과를 공유하고 기계 학습 커뮤니티가 제안된 패러다임의 한계를 탐구하도록 초대합니다. 또한 지속 학습과 같은 다른 연구 분야의 학습 관련 문제를 극복하기 위해 협상 패러다임을 활용하도록 커뮤니티를 독려하는 것을 목표로 합니다. 실험 설정의 Python 코드는 GitHub에 업로드되어 있습니다.

## 📝 요약

이 연구는 기계 학습 모델의 과적합 문제를 해결하기 위한 새로운 접근법을 제안합니다. 과적합은 모델이 훈련 데이터에 지나치게 맞춰져 테스트 데이터에 유용한 예측 규칙을 놓치는 현상입니다. 연구진은 모델이 입력과 주어진 레이블 간의 '협상'을 통해 출력 표현을 조정하도록 함으로써, 평균 분류 정확도를 높이고 과적합을 줄였습니다. 이 방법은 CIFAR 10, CIFAR 100, MNIST 등 공개 데이터셋을 사용한 실험에서 효과가 입증되었으며, 다른 연구 분야에서도 활용 가능성을 제시합니다. 실험 코드는 GitHub에 공개되어 있습니다.

## 🎯 주요 포인트


- 1. 과적합은 모델이 훈련 샘플에 지나치게 집중하여 테스트 데이터에 유용한 예측 규칙을 유지하지 못하는 현상입니다.

- 2. 본 연구에서는 모델이 입력 해석과 제공된 레이블 간의 협상을 통해 분류 정확도를 높이는 접근법을 제시합니다.

- 3. 협상 패러다임을 적용하여 평균 분류 정확도를 높이고 과적합률을 줄이는 데 성공했습니다.

- 4. 제안된 패러다임은 CIFAR 10, CIFAR 100, MNIST와 같은 데이터 세트에서 과적합 시나리오를 생성하여 더 큰 잠재력을 입증했습니다.

- 5. 연구 커뮤니티가 제안된 패러다임을 탐구하고 다른 연구 분야의 학습 관련 문제를 해결하는 데 활용하도록 장려하고자 합니다.


---

*Generated on 2025-09-22 15:49:34*