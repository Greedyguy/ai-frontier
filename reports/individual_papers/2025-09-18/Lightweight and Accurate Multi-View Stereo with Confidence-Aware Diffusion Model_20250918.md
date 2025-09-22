# Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model

**Korean Title:** 신뢰 인식 확산 모델을 활용한 경량 및 정확한 다중 시점 스테레오

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Fangjinhua Wang|Fangjinhua Wang]] [[authors/Qingshan Xu|Qingshan Xu]] [[authors/Yew-Soon Ong|Yew-Soon Ong]] [[authors/Marc Pollefeys|Marc Pollefeys]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Confidence-aware Sampling

## 🔗 유사한 논문
- [[FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (81.4% similar)
- [[DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (80.9% similar)
- [[Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (80.9% similar)
- [[MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (80.5% similar)
- [[Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (80.2% similar)

## 📋 저자 정보

**Authors:** Fangjinhua Wang, Qingshan Xu, Yew-Soon Ong, Marc Pollefeys

## 📄 Abstract (원문)

To reconstruct the 3D geometry from calibrated images, learning-based
multi-view stereo (MVS) methods typically perform multi-view depth estimation
and then fuse depth maps into a mesh or point cloud. To improve the
computational efficiency, many methods initialize a coarse depth map and then
gradually refine it in higher resolutions. Recently, diffusion models achieve
great success in generation tasks. Starting from a random noise, diffusion
models gradually recover the sample with an iterative denoising process. In
this paper, we propose a novel MVS framework, which introduces diffusion models
in MVS. Specifically, we formulate depth refinement as a conditional diffusion
process. Considering the discriminative characteristic of depth estimation, we
design a condition encoder to guide the diffusion process. To improve
efficiency, we propose a novel diffusion network combining lightweight 2D U-Net
and convolutional GRU. Moreover, we propose a novel confidence-based sampling
strategy to adaptively sample depth hypotheses based on the confidence
estimated by diffusion model. Based on our novel MVS framework, we propose two
novel MVS methods, DiffMVS and CasDiffMVS. DiffMVS achieves competitive
performance with state-of-the-art efficiency in run-time and GPU memory.
CasDiffMVS achieves state-of-the-art performance on DTU, Tanks & Temples and
ETH3D. Code is available at: https://github.com/cvg/diffmvs.

## 🔍 Abstract (한글 번역)

보정된 이미지로부터 3D 기하학을 재구성하기 위해, 학습 기반 다중 시점 스테레오(MVS) 방법은 일반적으로 다중 시점 깊이 추정을 수행한 후 깊이 맵을 메쉬 또는 포인트 클라우드로 융합합니다. 계산 효율성을 향상시키기 위해, 많은 방법들은 초기의 조잡한 깊이 맵을 설정한 후 점차적으로 더 높은 해상도로 정제합니다. 최근에, 확산 모델은 생성 작업에서 큰 성공을 거두고 있습니다. 무작위 노이즈에서 시작하여, 확산 모델은 반복적인 노이즈 제거 과정을 통해 샘플을 점진적으로 복원합니다. 본 논문에서는 MVS에 확산 모델을 도입한 새로운 MVS 프레임워크를 제안합니다. 구체적으로, 깊이 정제를 조건부 확산 과정으로 공식화합니다. 깊이 추정의 변별적 특성을 고려하여, 우리는 확산 과정을 안내하기 위해 조건 인코더를 설계했습니다. 효율성을 향상시키기 위해, 경량 2D U-Net과 합성곱 GRU를 결합한 새로운 확산 네트워크를 제안합니다. 또한, 확산 모델에 의해 추정된 신뢰도를 기반으로 깊이 가설을 적응적으로 샘플링하기 위한 새로운 신뢰도 기반 샘플링 전략을 제안합니다. 우리의 새로운 MVS 프레임워크를 기반으로, 우리는 두 가지 새로운 MVS 방법인 DiffMVS와 CasDiffMVS를 제안합니다. DiffMVS는 실행 시간과 GPU 메모리에서 최첨단 효율성을 유지하면서 경쟁력 있는 성능을 달성합니다. CasDiffMVS는 DTU, Tanks & Temples 및 ETH3D에서 최첨단 성능을 달성합니다. 코드는 다음에서 확인할 수 있습니다: https://github.com/cvg/diffmvs.

## 📝 요약

이 논문에서는 학습 기반 다중 시점 스테레오(MVS) 방법에 확산 모델을 도입한 새로운 MVS 프레임워크를 제안합니다. 기존 MVS 방법은 주로 깊이 맵을 추정한 후 이를 메쉬나 포인트 클라우드로 융합합니다. 본 연구는 깊이 보정을 조건부 확산 과정으로 정식화하고, 조건 인코더를 설계하여 확산 과정을 안내합니다. 또한, 경량화된 2D U-Net과 GRU를 결합한 새로운 확산 네트워크를 제안하여 효율성을 높였습니다. 확산 모델이 추정한 신뢰도를 기반으로 적응적으로 깊이 가설을 샘플링하는 신뢰도 기반 샘플링 전략도 도입했습니다. 이를 통해 제안된 DiffMVS와 CasDiffMVS는 각각 실행 시간과 메모리 효율성, 그리고 DTU, Tanks & Temples, ETH3D에서 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 다중 뷰 스테레오(MVS)에서 확산 모델을 도입하여 깊이 보정을 조건부 확산 과정으로 공식화한 새로운 MVS 프레임워크를 제안합니다.

- 2. 깊이 추정의 판별 특성을 고려하여 확산 과정을 안내하는 조건 인코더를 설계하였습니다.

- 3. 경량 2D U-Net과 컨볼루션 GRU를 결합한 새로운 확산 네트워크를 제안하여 효율성을 향상시켰습니다.

- 4. 확산 모델이 추정한 신뢰도를 기반으로 깊이 가설을 적응적으로 샘플링하는 새로운 신뢰도 기반 샘플링 전략을 제안합니다.

- 5. 제안된 DiffMVS와 CasDiffMVS는 각각 실행 시간과 GPU 메모리 효율성에서 경쟁력 있는 성능을, DTU, Tanks & Temples, ETH3D에서 최첨단 성능을 달성했습니다.

---

*Generated on 2025-09-20 00:48:37*