# MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes

**Korean Title:** 모안젤로: 동적 장면을 위한 모션 인식 신경 표면 재구성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Scene Reconstruction

## 🔗 유사한 논문
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (84.1% similar)
- [[2025-09-19/WorldForge_ Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (81.7% similar)
- [[2025-09-19/Roll Your Eyes_ Gaze Redirection via Explicit 3D Eyeball Rotation_20250919|Roll Your Eyes Gaze Redirection via Explicit 3D Eyeball Rotation]] (80.7% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN Layout-guided 3D Indoor Scene Generation]] (80.4% similar)
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15892v1 Announce Type: cross 
Abstract: Dynamic scene reconstruction from multi-view videos remains a fundamental challenge in computer vision. While recent neural surface reconstruction methods have achieved remarkable results in static 3D reconstruction, extending these approaches with comparable quality for dynamic scenes introduces significant computational and representational challenges. Existing dynamic methods focus on novel-view synthesis, therefore, their extracted meshes tend to be noisy. Even approaches aiming for geometric fidelity often result in too smooth meshes due to the ill-posedness of the problem. We present a novel framework for highly detailed dynamic reconstruction that extends the static 3D reconstruction method NeuralAngelo to work in dynamic settings. To that end, we start with a high-quality template scene reconstruction from the initial frame using NeuralAngelo, and then jointly optimize deformation fields that track the template and refine it based on the temporal sequence. This flexible template allows updating the geometry to include changes that cannot be modeled with the deformation field, for instance occluded parts or the changes in the topology. We show superior reconstruction accuracy in comparison to previous state-of-the-art methods on the ActorsHQ dataset.

## 🔍 Abstract (한글 번역)

arXiv:2509.15892v1 발표 유형: 교차  
초록: 다중 시점 비디오로부터의 동적 장면 재구성은 컴퓨터 비전에서 여전히 근본적인 도전 과제입니다. 최근의 신경 표면 재구성 방법은 정적 3D 재구성에서 놀라운 결과를 달성했지만, 이러한 접근 방식을 동적 장면에 대해 유사한 품질로 확장하는 것은 상당한 계산 및 표현상의 도전 과제를 제기합니다. 기존의 동적 방법은 새로운 시점 합성에 중점을 두고 있어, 추출된 메시는 대개 노이즈가 많은 경향이 있습니다. 기하학적 충실도를 목표로 하는 접근법조차도 문제의 불완전성 때문에 지나치게 매끄러운 메시를 생성하는 경우가 많습니다. 우리는 정적 3D 재구성 방법인 NeuralAngelo를 동적 환경에서 작동하도록 확장하여 매우 세밀한 동적 재구성을 위한 새로운 프레임워크를 제시합니다. 이를 위해 우리는 NeuralAngelo를 사용하여 초기 프레임에서 고품질의 템플릿 장면 재구성으로 시작한 후, 템플릿을 추적하고 시간적 시퀀스를 기반으로 이를 정제하는 변형 필드를 공동으로 최적화합니다. 이 유연한 템플릿은 변형 필드로 모델링할 수 없는 변경 사항, 예를 들어 가려진 부분이나 위상 변화 등을 포함하도록 기하학을 업데이트할 수 있게 합니다. 우리는 ActorsHQ 데이터셋에서 이전 최첨단 방법들과 비교하여 우수한 재구성 정확도를 보여줍니다.

## 📝 요약

이 논문은 다중 뷰 비디오에서 동적 장면을 고해상도로 재구성하는 새로운 프레임워크를 제안합니다. 기존의 동적 장면 재구성 방법은 노이즈가 많은 메시를 생성하거나 지나치게 부드러운 결과를 초래하는 반면, 본 연구는 정적 3D 재구성 방법인 NeuralAngelo를 동적 환경에 확장하여 높은 품질의 템플릿 장면을 초기 프레임에서 생성합니다. 이후, 변형 필드를 최적화하여 시간에 따른 변화를 추적하고 템플릿을 세밀하게 조정합니다. 이 방법은 가려진 부분이나 위상 변화와 같은 복잡한 변화를 효과적으로 반영할 수 있습니다. 제안된 방법은 ActorsHQ 데이터셋에서 기존 최첨단 방법들보다 우수한 재구성 정확도를 보였습니다.

## 🎯 주요 포인트

- 1. 다중 뷰 비디오에서의 동적 장면 재구성은 여전히 컴퓨터 비전에서 근본적인 도전 과제입니다.

- 2. 기존의 동적 방법들은 새로운 뷰 합성에 중점을 두어, 추출된 메쉬가 노이즈가 많을 수 있습니다.

- 3. NeuralAngelo를 동적 환경에 적용하여 높은 세부 사항을 가진 동적 재구성을 위한 새로운 프레임워크를 제시합니다.

- 4. 초기 프레임에서 NeuralAngelo를 사용하여 고품질 템플릿 장면을 재구성하고, 변형 필드를 최적화하여 템플릿을 추적하고 시간 순서에 따라 세부 사항을 개선합니다.

- 5. 제안된 방법은 ActorsHQ 데이터셋에서 이전 최신 방법들보다 우수한 재구성 정확도를 보여줍니다.

---

*Generated on 2025-09-22 14:15:42*