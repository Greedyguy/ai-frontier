# [Re] Improving Interpretation Faithfulness for Vision Transformers

**Korean Title:** [재] 비전 트랜스포머의 해석 충실도 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Izabela Kurek|Izabela Kurek]] [[authors/Wojciech Trejter|Wojciech Trejter]] [[authors/Stipe Frkovic|Stipe Frkovic]] [[authors/Andro Erdelez|Andro Erdelez]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Diffusion Denoised Smoothing

## 🔗 유사한 논문
- [[Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (77.7% similar)
- [[Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (77.6% similar)
- [[Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis_20250919|Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis]] (77.6% similar)
- [[FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (77.1% similar)
- [[FishBEV_ Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras_20250918|FishBEV Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (76.7% similar)

## 📋 저자 정보

**Authors:** Izabela Kurek, Wojciech Trejter, Stipe Frkovic, Andro Erdelez

## 📄 Abstract (원문)

This work aims to reproduce the results of Faithful Vision Transformers
(FViTs) proposed by arXiv:2311.17983 alongside interpretability methods for
Vision Transformers from arXiv:2012.09838 and Xu (2022) et al. We investigate
claims made by arXiv:2311.17983, namely that the usage of Diffusion Denoised
Smoothing (DDS) improves interpretability robustness to (1) attacks in a
segmentation task and (2) perturbation and attacks in a classification task. We
also extend the original study by investigating the authors' claims that adding
DDS to any interpretability method can improve its robustness under attack.
This is tested on baseline methods and the recently proposed Attribution
Rollout method. In addition, we measure the computational costs and
environmental impact of obtaining an FViT through DDS. Our results broadly
agree with the original study's findings, although minor discrepancies were
found and discussed.

## 🔍 Abstract (한글 번역)

이 연구는 arXiv:2311.17983에서 제안된 Faithful Vision Transformers(FViTs)의 결과를 재현하고, arXiv:2012.09838 및 Xu (2022) 등에서 제안한 Vision Transformers의 해석 가능성 방법과 함께 이를 분석하는 것을 목표로 합니다. 우리는 arXiv:2311.17983에서 제기된 주장, 즉 Diffusion Denoised Smoothing(DDS)의 사용이 (1) 세분화 작업에서의 공격과 (2) 분류 작업에서의 변형 및 공격에 대한 해석 가능성의 견고성을 향상시킨다는 주장에 대해 조사합니다. 또한, DDS를 어떤 해석 가능성 방법에 추가하더라도 공격 하에서의 견고성을 향상시킬 수 있다는 저자들의 주장을 조사하여 원래 연구를 확장합니다. 이는 기본 방법과 최근 제안된 Attribution Rollout 방법에서 테스트됩니다. 추가적으로, 우리는 DDS를 통해 FViT를 얻는 데 필요한 계산 비용과 환경적 영향을 측정합니다. 우리의 결과는 원래 연구의 발견과 대체로 일치하지만, 몇 가지 사소한 차이점이 발견되어 논의되었습니다.

## 📝 요약

이 연구는 Faithful Vision Transformers(FViTs)와 관련된 연구 결과를 재현하고, Vision Transformers의 해석 가능성 방법을 조사합니다. 주요 기여는 Diffusion Denoised Smoothing(DDS)의 사용이 세분화 및 분류 작업에서의 공격에 대한 해석 가능성의 견고성을 향상시킨다는 주장에 대한 검증입니다. 또한, DDS가 어떤 해석 가능성 방법에 추가되더라도 공격에 대한 견고성을 높일 수 있다는 주장을 확장하여 조사했습니다. 연구 결과는 원래 연구와 대체로 일치하지만, 일부 차이점도 발견되어 논의되었습니다. FViT를 DDS를 통해 얻는 데 드는 계산 비용과 환경적 영향도 측정했습니다.

## 🎯 주요 포인트

- 1. Faithful Vision Transformers(FViTs)의 결과 재현 및 해석 가능성 방법을 연구했습니다.

- 2. Diffusion Denoised Smoothing(DDS)가 세분화 및 분류 작업에서 공격에 대한 해석 가능성 강건성을 향상시킨다는 주장을 조사했습니다.

- 3. DDS를 해석 가능성 방법에 추가하면 공격에 대한 강건성을 개선할 수 있다는 주장을 확장하여 연구했습니다.

- 4. Attribution Rollout 방법과 기존의 기준 방법에 DDS를 적용하여 테스트했습니다.

- 5. DDS를 통한 FViT의 계산 비용과 환경적 영향을 측정했습니다.

---

*Generated on 2025-09-20 02:47:19*