# A noise-corrected Langevin algorithm and sampling by half-denoising

**Korean Title:** 노이즈 보정된 랑주뱅 알고리즘과 반-디노이징을 통한 샘플링

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Half-denoising Sampling|Half-denoising Sampling]] [[keywords/specific/Langevin Algorithm|Langevin Algorithm]] [[keywords/specific/Score Function|Score Function]] [[keywords/broad/Deep Learning|Deep Learning]] [[keywords/unique/Noise-corrected Langevin Algorithm|Noise-corrected Langevin Algorithm]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises_20250922|Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises]] (81.2% similar) [[2025-09-17/Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems_20250917|Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems]] (80.9% similar) [[2025-09-22/Noise-Robustness Through Noise_ Asymmetric LoRA Adaption with Poisoning Expert_20250922|Noise-Robustness Through Noise: Asymmetric LoRA Adaption with Poisoning Expert]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Half-denoising
**🔗 Specific Connectable**: Langevin Algorithm, Score Function
**🔬 Broad Technical**: Deep Learning
**⭐ Unique Technical**: Noise-corrected Langevin Algorithm
## 🔗 유사한 논문
- [[2025-09-22/Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises_20250922|Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises]] (81.2% similar)
- [[2025-09-17/Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems_20250917|Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems]] (80.9% similar)
- [[2025-09-22/Noise-Robustness Through Noise_ Asymmetric LoRA Adaption with Poisoning Expert_20250922|Noise-Robustness Through Noise Asymmetric LoRA Adaption with Poisoning Expert]] (80.7% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (80.1% similar)
- [[2025-09-17/Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator_20250917|Learning Minimal Representations of Many-Body Physics from Snapshots of a Quantum Simulator]] (79.9% similar)


**ArXiv ID**: [2410.05837](https://arxiv.org/abs/2410.05837)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2410.05837.pdf)


**ArXiv ID**: [2410.05837](https://arxiv.org/abs/2410.05837)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2410.05837.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Half-denoising
**🔗 Specific Connectable**: Langevin Algorithm, Score Function
**⭐ Unique Technical**: Noise-corrected Langevin Algorithm
**🔬 Broad Technical**: Deep Learning

## 🏷️ 추출된 키워드



`Deep Learning` • 

`Langevin Algorithm` • 

`Score Function` • 

`Noise-corrected Langevin Algorithm` • 

`Half-denoising Sampling`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.05837v3 Announce Type: replace 
Abstract: The Langevin algorithm is a classic method for sampling from a given pdf in a real space. In its basic version, it only requires knowledge of the gradient of the log-density, also called the score function. However, in deep learning, it is often easier to learn the so-called "noisy-data score function", i.e. the gradient of the log-density of noisy data, more precisely when Gaussian noise is added to the data. Such an estimate is biased and complicates the use of the Langevin method. Here, we propose a noise-corrected version of the Langevin algorithm, where the bias due to noisy data is removed, at least regarding first-order terms. Unlike diffusion models, our algorithm only needs to know the noisy score function for one single noise level. We further propose a simple special case which has an interesting intuitive interpretation of iteratively adding noise the data and then attempting to remove half of that noise.

## 🔍 Abstract (한글 번역)

arXiv:2410.05837v3 발표 유형: 교체  
초록: 랑주뱅 알고리즘은 실수 공간에서 주어진 확률 밀도 함수(pdf)로부터 샘플링하는 고전적인 방법입니다. 기본 버전에서는 로그 밀도의 기울기, 즉 스코어 함수에 대한 지식만 필요합니다. 그러나 딥러닝에서는 소위 "노이즈 데이터 스코어 함수", 즉 노이즈가 추가된 데이터의 로그 밀도의 기울기를 학습하는 것이 더 쉬운 경우가 많습니다. 이러한 추정치는 편향되어 있으며, 랑주뱅 방법의 사용을 복잡하게 만듭니다. 여기에서는 노이즈 데이터로 인한 편향을 제거한, 적어도 1차 항에 관해서는 제거한 노이즈 보정 랑주뱅 알고리즘을 제안합니다. 확산 모델과 달리, 우리의 알고리즘은 단일 노이즈 수준에 대한 노이즈 스코어 함수만 알면 됩니다. 또한, 데이터에 노이즈를 반복적으로 추가하고 그 노이즈의 절반을 제거하려고 시도하는 흥미로운 직관적 해석을 가진 간단한 특수 사례를 제안합니다.

## 📝 요약

이 논문은 노이즈가 추가된 데이터의 로그 밀도 기울기(노이즈 데이터 스코어 함수)를 이용해 표본을 추출하는 Langevin 알고리즘의 개선된 버전을 제안합니다. 기존 방법은 노이즈로 인해 편향된 추정치를 사용해야 했지만, 제안된 알고리즘은 이러한 편향을 1차 항에서 제거합니다. 이 알고리즘은 단일 노이즈 수준에서의 노이즈 스코어 함수만 필요로 하며, 데이터에 노이즈를 추가하고 그 절반을 제거하는 과정을 반복하는 직관적인 해석을 제공합니다. 이는 딥러닝에서의 샘플링 효율성을 높이는 데 기여합니다.

## 🎯 주요 포인트


- 1. Langevin 알고리즘은 주어진 확률 밀도 함수에서 샘플링하는 고전적인 방법으로, 로그 밀도의 기울기인 스코어 함수만을 필요로 한다.

- 2. 딥러닝에서는 데이터에 가우시안 노이즈를 추가한 후의 로그 밀도의 기울기인 "노이즈 데이터 스코어 함수"를 학습하는 것이 더 쉬운 경우가 많다.

- 3. 본 연구에서는 노이즈 데이터로 인한 편향을 제거한 노이즈 보정 버전의 Langevin 알고리즘을 제안한다.

- 4. 제안된 알고리즘은 확산 모델과 달리 단일 노이즈 레벨에서의 노이즈 스코어 함수만을 필요로 한다.

- 5. 데이터에 노이즈를 반복적으로 추가하고 그 노이즈의 절반을 제거하려는 직관적인 해석을 가진 간단한 특수 사례를 제안한다.


---

*Generated on 2025-09-22 15:51:49*