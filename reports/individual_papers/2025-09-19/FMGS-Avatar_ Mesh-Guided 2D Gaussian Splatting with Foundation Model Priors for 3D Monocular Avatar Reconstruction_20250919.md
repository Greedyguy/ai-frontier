
# FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction

**Korean Title:** FMGS-아바타: 3D 단안 아바타 재구성을 위한 기초 모델 사전 지식을 활용한 메쉬 기반 2D 가우시안 스플래팅

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Mesh Guided Gaussian Splatting

## 🔗 유사한 논문
- [[Kling-Avatar Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis]] (82.9% similar)
- [[Roll Your Eyes Gaze Redirection via Explicit 3D Eyeball Rotation]] (81.2% similar)
- [[WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (81.1% similar)
- [[Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (80.7% similar)
- [[Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14739v1 Announce Type: new 
Abstract: Reconstructing high-fidelity animatable human avatars from monocular videos remains challenging due to insufficient geometric information in single-view observations. While recent 3D Gaussian Splatting methods have shown promise, they struggle with surface detail preservation due to the free-form nature of 3D Gaussian primitives. To address both the representation limitations and information scarcity, we propose a novel method, \textbf{FMGS-Avatar}, that integrates two key innovations. First, we introduce Mesh-Guided 2D Gaussian Splatting, where 2D Gaussian primitives are attached directly to template mesh faces with constrained position, rotation, and movement, enabling superior surface alignment and geometric detail preservation. Second, we leverage foundation models trained on large-scale datasets, such as Sapiens, to complement the limited visual cues from monocular videos. However, when distilling multi-modal prior knowledge from foundation models, conflicting optimization objectives can emerge as different modalities exhibit distinct parameter sensitivities. We address this through a coordinated training strategy with selective gradient isolation, enabling each loss component to optimize its relevant parameters without interference. Through this combination of enhanced representation and coordinated information distillation, our approach significantly advances 3D monocular human avatar reconstruction. Experimental evaluation demonstrates superior reconstruction quality compared to existing methods, with notable gains in geometric accuracy and appearance fidelity while providing rich semantic information. Additionally, the distilled prior knowledge within a shared canonical space naturally enables spatially and temporally consistent rendering under novel views and poses.

## 🔍 Abstract (한글 번역)

arXiv:2509.14739v1 발표 유형: 신규  
초록: 단안 비디오에서 고충실도의 애니메이션 가능한 인간 아바타를 재구성하는 것은 단일 뷰 관찰에서 기하학적 정보가 불충분하기 때문에 여전히 도전적입니다. 최근의 3D 가우시안 스플래팅 방법이 가능성을 보여주었지만, 3D 가우시안 프리미티브의 자유형 특성으로 인해 표면 세부 사항 보존에 어려움을 겪고 있습니다. 이러한 표현의 한계와 정보 부족 문제를 해결하기 위해, 우리는 두 가지 주요 혁신을 통합한 새로운 방법인 \textbf{FMGS-Avatar}를 제안합니다. 첫째, 우리는 2D 가우시안 프리미티브를 위치, 회전 및 이동이 제한된 상태로 템플릿 메쉬 면에 직접 부착하여 우수한 표면 정렬과 기하학적 세부 사항 보존을 가능하게 하는 메쉬 유도 2D 가우시안 스플래팅을 도입합니다. 둘째, 우리는 Sapiens와 같은 대규모 데이터셋에서 훈련된 기초 모델을 활용하여 단안 비디오에서 제한된 시각적 단서를 보완합니다. 그러나 기초 모델에서 다중 모달 사전 지식을 증류할 때, 서로 다른 모달리티가 고유한 매개변수 민감성을 나타내므로 상충되는 최적화 목표가 발생할 수 있습니다. 우리는 선택적 그래디언트 격리를 통한 조정된 훈련 전략을 통해 각 손실 구성 요소가 간섭 없이 관련 매개변수를 최적화할 수 있도록 합니다. 향상된 표현과 조정된 정보 증류의 결합을 통해, 우리의 접근법은 3D 단안 인간 아바타 재구성을 크게 발전시킵니다. 실험적 평가 결과, 기존 방법과 비교하여 기하학적 정확성과 외관 충실도에서 현저한 향상을 보이며 풍부한 의미 정보를 제공합니다. 또한, 공유된 정준 공간 내에서 증류된 사전 지식은 새로운 뷰와 포즈에서 공간적 및 시간적으로 일관된 렌더링을 자연스럽게 가능하게 합니다.

## 📝 요약

이 논문은 단일 시점 비디오로부터 고품질의 애니메이션 가능한 인간 아바타를 재구성하는 방법을 제안합니다. 기존의 3D Gaussian Splatting 기법이 표면 세부사항 보존에 한계가 있는 문제를 해결하기 위해, 저자들은 \textbf{FMGS-Avatar}라는 새로운 방법을 소개합니다. 이 방법은 두 가지 주요 혁신을 포함합니다. 첫째, 메쉬 기반의 2D Gaussian Splatting을 도입하여 메쉬 표면에 2D Gaussian 프리미티브를 부착함으로써 표면 정렬과 기하학적 세부사항을 보존합니다. 둘째, 대규모 데이터셋으로 훈련된 기초 모델을 활용하여 단일 시점 비디오의 제한된 시각적 정보를 보완합니다. 이 과정에서 발생할 수 있는 최적화 목표 간의 충돌을 해결하기 위해 선택적 그래디언트 격리를 통한 조정된 훈련 전략을 사용합니다. 실험 결과, 제안된 방법은 기존 방법들보다 뛰어난 재구성 품질을 보여주며, 기하학적 정확성과 외관 충실도에서 특히 우수한 성능을 나타냅니다.

## 🎯 주요 포인트

- 1. FMGS-Avatar는 2D Gaussian Splatting을 메쉬에 직접 부착하여 표면 정렬과 기하학적 세부사항 보존을 개선합니다.

- 2. 대규모 데이터셋으로 훈련된 기초 모델을 활용하여 단일 시점 비디오의 제한된 시각적 정보를 보완합니다.

- 3. 서로 다른 모달리티의 매개변수 민감도 차이를 해결하기 위해 선택적 그래디언트 격리를 통한 조정된 훈련 전략을 도입합니다.

- 4. 제안된 방법은 기존 방법에 비해 기하학적 정확성과 외관 충실도에서 우수한 재구성 품질을 보여줍니다.

- 5. 공유된 표준 공간 내에서 증류된 사전 지식은 새로운 시점과 자세에서도 일관된 렌더링을 가능하게 합니다.

---

*Generated on 2025-09-19 16:05:30*