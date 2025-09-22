
# Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT

**Korean Title:** 희소 뷰 CT를 위한 교차 배포 확산 사전 주도 반복 재구성

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔬 Broad Technical**: Iterative Reconstruction, Diffusion Transformer

## 🔗 유사한 논문
- [[Singular_Value_Few-shot_Adaptation_of_Vision-Language_Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (78.7% similar)
- [[ColonCrafter: A Depth Estimation Model for Colonoscopy Videos Using Diffusion Priors]] (78.3% similar)
- [[LamiGauss: Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction]] (78.1% similar)
- [[PRISM-DP_Spatial_Pose-based_Observations_for_Diffusion-Policies_via_Segmentation,_Mesh_Generation,_and_Pose_Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (77.7% similar)
- [[GROOD_GRadient-Aware_Out-of-Distribution_Detection_20250918|GROOD: GRadient-Aware Out-of-Distribution Detection]] (77.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13576v1 Announce Type: cross 
Abstract: Sparse-View CT (SVCT) reconstruction enhances temporal resolution and reduces radiation dose, yet its clinical use is hindered by artifacts due to view reduction and domain shifts from scanner, protocol, or anatomical variations, leading to performance degradation in out-of-distribution (OOD) scenarios. In this work, we propose a Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction (CDPIR) framework to tackle the OOD problem in SVCT. CDPIR integrates cross-distribution diffusion priors, derived from a Scalable Interpolant Transformer (SiT), with model-based iterative reconstruction methods. Specifically, we train a SiT backbone, an extension of the Diffusion Transformer (DiT) architecture, to establish a unified stochastic interpolant framework, leveraging Classifier-Free Guidance (CFG) across multiple datasets. By randomly dropping the conditioning with a null embedding during training, the model learns both domain-specific and domain-invariant priors, enhancing generalizability. During sampling, the globally sensitive transformer-based diffusion model exploits the cross-distribution prior within the unified stochastic interpolant framework, enabling flexible and stable control over multi-distribution-to-noise interpolation paths and decoupled sampling strategies, thereby improving adaptation to OOD reconstruction. By alternating between data fidelity and sampling updates, our model achieves state-of-the-art performance with superior detail preservation in SVCT reconstructions. Extensive experiments demonstrate that CDPIR significantly outperforms existing approaches, particularly under OOD conditions, highlighting its robustness and potential clinical value in challenging imaging scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.13576v1 발표 유형: 교차
요약: Sparse-View CT (SVCT) 재구성은 시간 해상도를 향상시키고 방사선 투여량을 줄이지만, 임상적 사용은 뷰 감소로 인한 아티팩트 및 스캐너, 프로토콜 또는 해부학적 변이로 인한 도메인 이동으로 인해 out-of-distribution (OOD) 시나리오에서 성능 저하가 발생합니다. 본 연구에서는 SVCT의 OOD 문제를 해결하기 위해 Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction (CDPIR) 프레임워크를 제안합니다. CDPIR은 Scalable Interpolant Transformer (SiT)에서 파생된 교차 분포 확산 사전을 모델 기반 반복 재구성 방법과 통합합니다. 구체적으로, 다중 데이터셋에서 Classifier-Free Guidance (CFG)를 활용하여 통일된 확률 보간 프레임워크를 구축하는 DiT 아키텍처의 확장인 SiT 백본을 훈련시킵니다. 훈련 중에는 조건부를 무효화하는 null 임베딩을 무작위로 삭제함으로써 도메인별 및 도메인 불변 사전을 학습하여 일반화를 향상시킵니다. 샘플링 중에는 전역적으로 민감한 트랜스포머 기반 확산 모델이 통일된 확률 보간 프레임워크 내에서 교차 분포 사전을 활용하여 다중 분포-잡음 보간 경로와 분리된 샘플링 전략에 유연하고 안정적인 제어를 가능하게 하여 OOD 재구성에 대한 적응성을 향상시킵니다. 데이터 충실성과 샘플링 업데이트를 번갈아가며 수행함으로써, 우리 모델은 SVCT 재구성에서 우수한 세부 정보 보존을 달성하며 최신 기술 성능을 발휘합니다. 광범위한 실험 결과, CDPIR이 기존 방법을 크게 능가하며 특히 OOD 조건 하에서 뛰어난 성능을 보여 복잡한 영상 시나리오에서의 강건성과 잠재적 임상 가치를 강조합니다.

## 📝 요약

본 연구에서는 Sparse-View CT (SVCT) 재구성의 임상적 활용을 어렵게 하는 아티팩트 문제를 해결하기 위해 Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction (CDPIR) 프레임워크를 제안한다. CDPIR은 Scalable Interpolant Transformer (SiT)에서 파생된 교차 분포 확산 사전을 모델 기반 반복 재구성 방법과 통합한다. 이를 통해 OOD 재구성에 대한 적응력을 향상시키고 상세 정보 보존에 우수한 성능을 보인다. 실험 결과 CDPIR은 특히 OOD 조건 하에서 기존 방법들을 크게 능가하여 임상적 가치를 갖는 것으로 나타났다.

## 🎯 주요 포인트

- 1. Sparse-View CT (SVCT) 재구성은 시간 해상도를 향상시키고 방사선 투여량을 줄이지만, OOD 시나리오에서 성능 저하를 유발하는 아티팩트로 인해 임상적 사용이 제한됨.

- 2. Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction (CDPIR) 프레임워크는 SVCT의 OOD 문제를 해결하기 위해 제안됨.

- 3. CDPIR은 다양한 데이터셋 간 Classifier-Free Guidance를 활용하여 일반화 성능을 향상시키는 Scalable Interpolant Transformer (SiT)를 훈련시킴.

- 4. CDPIR은 데이터 충실성과 샘플링 업데이트를 번갈아가며 수행하여 SVCT 재구성에서 우수한 성능과 상세 정보 보존을 달성함.

- 5. CDPIR은 특히 OOD 조건 하에서 기존 방법들을 크게 능가하여 어려운 영상 장면에서의 강건성과 임상 가치를 강조함.

---

*Generated on 2025-09-18 17:04:43*