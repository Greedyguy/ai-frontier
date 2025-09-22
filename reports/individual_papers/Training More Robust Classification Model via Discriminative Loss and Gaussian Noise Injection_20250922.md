# Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection

**Korean Title:** 더욱 견고한 분류 모델 학습: 판별 손실 및 가우시안 노이즈 주입을 통한 접근

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Gaussian Noise Injection|Gaussian Noise Injection]] [[keywords/specific/Feature Alignment|Feature Alignment]] [[keywords/broad/Deep Learning|Deep Learning]] [[keywords/broad/Neural Networks|Neural Networks]] [[keywords/unique/Discriminative Loss|Discriminative Loss]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Noise-Robustness Through Noise_ Asymmetric LoRA Adaption with Poisoning Expert_20250922|Noise-Robustness Through Noise: Asymmetric LoRA Adaption with Poisoning Expert]] (85.2% similar) [[2025-09-22/A noise-corrected Langevin algorithm and sampling by half-denoising_20250922|A noise-corrected Langevin algorithm and sampling by half-denoising]] (83.7% similar) [[2025-09-18/Not All Degradations Are Equal_ A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution_20250918|Not All Degradations Are Equal: A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Gaussian Noise Injection, Feature Alignment
**🔬 Broad Technical**: Deep Learning, Neural Networks
**⭐ Unique Technical**: Discriminative Loss
## 🔗 유사한 논문
- [[2025-09-22/Noise-Robustness Through Noise_ Asymmetric LoRA Adaption with Poisoning Expert_20250922|Noise-Robustness Through Noise Asymmetric LoRA Adaption with Poisoning Expert]] (85.2% similar)
- [[2025-09-22/A noise-corrected Langevin algorithm and sampling by half-denoising_20250922|A noise-corrected Langevin algorithm and sampling by half-denoising]] (83.7% similar)
- [[2025-09-18/Not All Degradations Are Equal_ A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution_20250918|Not All Degradations Are Equal A Targeted Feature Denoising Framework for Generalizable Image Super-Resolution]] (83.3% similar)
- [[2025-09-22/Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises_20250922|Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises]] (81.6% similar)
- [[2025-09-18/Efficient Conformal Prediction for Regression Models under Label Noise_20250918|Efficient Conformal Prediction for Regression Models under Label Noise]] (81.3% similar)


**ArXiv ID**: [2405.18499](https://arxiv.org/abs/2405.18499)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2405.18499.pdf)


**ArXiv ID**: [2405.18499](https://arxiv.org/abs/2405.18499)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2405.18499.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Noise Robust Deep Learning
**🔗 Specific Connectable**: Gaussian Noise Injection, Feature Alignment
**⭐ Unique Technical**: Discriminative Loss
**🔬 Broad Technical**: Deep Neural Networks

## 🏷️ 추출된 키워드



`Deep Learning` • 

`Neural Networks` • 

`Gaussian Noise Injection` • 

`Feature Alignment` • 

`Discriminative Loss`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.18499v3 Announce Type: replace-cross 
Abstract: Robustness of deep neural networks to input noise remains a critical challenge, as naive noise injection often degrades accuracy on clean (uncorrupted) data. We propose a novel training framework that addresses this trade-off through two complementary objectives. First, we introduce a loss function applied at the penultimate layer that explicitly enforces intra-class compactness and increases the margin to analytically defined decision boundaries. This enhances feature discriminativeness and class separability for clean data. Second, we propose a class-wise feature alignment mechanism that brings noisy data clusters closer to their clean counterparts. Furthermore, we provide a theoretical analysis demonstrating that improving feature stability under additive Gaussian noise implicitly reduces the curvature of the softmax loss landscape in input space, as measured by Hessian eigenvalues.This thus naturally enhances robustness without explicit curvature penalties. Conversely, we also theoretically show that lower curvatures lead to more robust models. We validate the effectiveness of our method on standard benchmarks and our custom dataset. Our approach significantly reinforces model robustness to various perturbations while maintaining high accuracy on clean data, advancing the understanding and practice of noise-robust deep learning.

## 🔍 Abstract (한글 번역)

arXiv:2405.18499v3 발표 유형: 교차 교체  
초록: 입력 노이즈에 대한 심층 신경망의 견고성은 여전히 중요한 과제로 남아 있으며, 단순한 노이즈 주입은 종종 깨끗한(손상되지 않은) 데이터의 정확도를 저하시킵니다. 우리는 이 균형 문제를 해결하기 위해 두 가지 상호 보완적인 목표를 통해 새로운 훈련 프레임워크를 제안합니다. 첫째, 우리는 클래스 내 응집성을 명시적으로 강화하고 분석적으로 정의된 결정 경계에 대한 여유를 증가시키는 손실 함수를 마지막에서 두 번째 층에 적용합니다. 이는 깨끗한 데이터에 대한 특징의 변별력과 클래스 분리를 향상시킵니다. 둘째, 우리는 노이즈가 있는 데이터 클러스터를 그들의 깨끗한 대응물에 더 가깝게 가져오는 클래스별 특징 정렬 메커니즘을 제안합니다. 또한, 우리는 가우시안 노이즈가 추가된 환경에서 특징 안정성을 향상시키는 것이 입력 공간에서 소프트맥스 손실 지형의 곡률을 암시적으로 감소시킨다는 이론적 분석을 제공합니다. 이는 헤세 행렬의 고유값으로 측정되며, 따라서 명시적인 곡률 패널티 없이도 자연스럽게 견고성을 향상시킵니다. 반대로, 우리는 낮은 곡률이 더 견고한 모델로 이어진다는 것을 이론적으로 보여줍니다. 우리는 표준 벤치마크와 우리의 맞춤형 데이터셋에서 우리의 방법의 효과를 검증합니다. 우리의 접근 방식은 다양한 교란에 대한 모델의 견고성을 크게 강화하면서도 깨끗한 데이터에 대한 높은 정확도를 유지하여 노이즈 견고한 심층 학습의 이해와 실천을 발전시킵니다.

## 📝 요약

이 논문은 입력 노이즈에 대한 딥러닝 모델의 강건성을 개선하는 새로운 학습 프레임워크를 제안합니다. 첫째, 중간층에 적용되는 손실 함수를 도입하여 클래스 내 데이터의 응집성을 높이고 결정 경계의 여유를 증가시킵니다. 둘째, 노이즈 데이터 클러스터를 깨끗한 데이터와 정렬시키는 클래스별 특징 정렬 메커니즘을 제안합니다. 이 방법은 가우시안 노이즈 하에서 특징의 안정성을 개선하여 소프트맥스 손실의 곡률을 자연스럽게 감소시킵니다. 이론적으로 낮은 곡률이 더 강건한 모델을 만든다는 것을 증명합니다. 제안된 방법은 표준 벤치마크와 커스텀 데이터셋에서 검증되었으며, 다양한 노이즈에 대한 모델의 강건성을 크게 강화하면서도 깨끗한 데이터에 대한 높은 정확도를 유지합니다.

## 🎯 주요 포인트


- 1. 입력 노이즈에 대한 심층 신경망의 강건성을 개선하기 위해 두 가지 상호 보완적인 목표를 제안하는 새로운 훈련 프레임워크를 소개합니다.

- 2. 전층 손실 함수를 도입하여 클래스 내 압축성을 명시적으로 강화하고, 결정 경계에 대한 마진을 증가시켜 깨끗한 데이터의 특징 구별성과 클래스 분리를 향상시킵니다.

- 3. 클래스별 특징 정렬 메커니즘을 통해 노이즈가 있는 데이터 클러스터를 깨끗한 데이터 클러스터에 더 가깝게 만듭니다.

- 4. 가우시안 노이즈 하에서 특징 안정성을 개선하면 입력 공간의 소프트맥스 손실 곡률이 자연스럽게 감소하여 강건성을 향상시킵니다.

- 5. 제안된 방법은 다양한 교란에 대한 모델의 강건성을 크게 강화하면서도 깨끗한 데이터에 대한 높은 정확도를 유지함을 표준 벤치마크와 사용자 정의 데이터셋을 통해 검증합니다.


---

*Generated on 2025-09-22 16:06:20*