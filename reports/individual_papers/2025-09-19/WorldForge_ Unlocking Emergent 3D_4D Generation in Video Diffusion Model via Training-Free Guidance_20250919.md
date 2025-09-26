---
keywords:
  - Diffusion Models
  - Generative Models
  - Optical Flow
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15130
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:17:04.780305",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Generative Models",
    "Optical Flow"
  ],
  "rejected_keywords": [
    "3D/4D Generation",
    "Trajectory Guidance"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.8,
    "Generative Models": 0.77,
    "Optical Flow": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# WorldForge: Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance

**Korean Title:** WorldForge: 훈련이 필요 없는 가이드를 통한 비디오 확산 모델에서의 3D/4D 생성 발현 해제

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|video diffusion models]], [[keywords/Generative Models|generative priors]], [[keywords/Optical Flow|optical flow similarity]]

## 🔗 유사한 논문
- [[FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (84.8% similar)
- [[Identity-Preserving_Text-to-Video_Generation_Guided_by_Simple_yet_Effective_Spatial-Temporal_Decoupled_Representations_20250918|Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations]] (82.7% similar)
- [[textsc{Gen2Real} Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (81.1% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (80.9% similar)
- [[Generative_Image_Coding_with_Diffusion_Prior_20250918|Generative Image Coding with Diffusion Prior]] (80.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15130v1 Announce Type: cross 
Abstract: Recent video diffusion models demonstrate strong potential in spatial intelligence tasks due to their rich latent world priors. However, this potential is hindered by their limited controllability and geometric inconsistency, creating a gap between their strong priors and their practical use in 3D/4D tasks. As a result, current approaches often rely on retraining or fine-tuning, which risks degrading pretrained knowledge and incurs high computational costs. To address this, we propose WorldForge, a training-free, inference-time framework composed of three tightly coupled modules. Intra-Step Recursive Refinement introduces a recursive refinement mechanism during inference, which repeatedly optimizes network predictions within each denoising step to enable precise trajectory injection. Flow-Gated Latent Fusion leverages optical flow similarity to decouple motion from appearance in the latent space and selectively inject trajectory guidance into motion-related channels. Dual-Path Self-Corrective Guidance compares guided and unguided denoising paths to adaptively correct trajectory drift caused by noisy or misaligned structural signals. Together, these components inject fine-grained, trajectory-aligned guidance without training, achieving both accurate motion control and photorealistic content generation. Extensive experiments across diverse benchmarks validate our method's superiority in realism, trajectory consistency, and visual fidelity. This work introduces a novel plug-and-play paradigm for controllable video synthesis, offering a new perspective on leveraging generative priors for spatial intelligence.

## 🔍 Abstract (한글 번역)

arXiv:2509.15130v1 발표 유형: 교차  
초록: 최근의 비디오 확산 모델은 풍부한 잠재적 세계 사전 지식을 통해 공간 지능 작업에서 강력한 잠재력을 보여주고 있습니다. 그러나 이러한 잠재력은 제한된 제어 가능성과 기하학적 일관성 부족으로 인해 3D/4D 작업에서의 실용적 사용과 강력한 사전 지식 사이에 격차가 발생합니다. 결과적으로, 현재의 접근 방식은 종종 재학습이나 미세 조정에 의존하게 되며, 이는 사전 학습된 지식을 저하시킬 위험이 있고 높은 계산 비용을 초래합니다. 이를 해결하기 위해 우리는 세 가지 밀접하게 결합된 모듈로 구성된 학습이 필요 없는 추론 시간 프레임워크인 WorldForge를 제안합니다. Intra-Step Recursive Refinement는 추론 중에 반복적인 정제 메커니즘을 도입하여 각 노이즈 제거 단계 내에서 네트워크 예측을 반복적으로 최적화하여 정확한 궤적 주입을 가능하게 합니다. Flow-Gated Latent Fusion은 잠재 공간에서 모션과 외형을 분리하기 위해 광학 흐름 유사성을 활용하고, 모션 관련 채널에 궤적 지침을 선택적으로 주입합니다. Dual-Path Self-Corrective Guidance는 유도된 경로와 유도되지 않은 경로를 비교하여 노이즈가 많거나 정렬되지 않은 구조적 신호로 인한 궤적 드리프트를 적응적으로 수정합니다. 이 구성 요소들은 학습 없이 세밀하고 궤적 정렬된 지침을 주입하여 정확한 모션 제어와 사진과 같은 사실적인 콘텐츠 생성을 달성합니다. 다양한 벤치마크에 걸친 광범위한 실험은 현실감, 궤적 일관성 및 시각적 충실도에서 우리의 방법의 우수성을 입증합니다. 이 연구는 제어 가능한 비디오 합성을 위한 새로운 플러그 앤 플레이 패러다임을 도입하여 공간 지능을 위한 생성적 사전 지식을 활용하는 새로운 관점을 제공합니다.

## 📝 요약

최근 비디오 확산 모델은 공간 지능 작업에서 잠재적 가능성을 보여주지만, 제어의 한계와 기하학적 불일치로 인해 3D/4D 작업에서의 실용성이 떨어집니다. 이를 해결하기 위해, 우리는 WorldForge라는 훈련이 필요 없는 추론 시간 프레임워크를 제안합니다. 이 프레임워크는 세 가지 모듈로 구성되어 있으며, Intra-Step Recursive Refinement는 반복적인 최적화를 통해 정확한 경로 주입을 가능하게 하고, Flow-Gated Latent Fusion은 광학 흐름 유사성을 활용해 경로 지침을 모션 관련 채널에 선택적으로 주입합니다. Dual-Path Self-Corrective Guidance는 경로 드리프트를 수정하여 정확한 모션 제어와 사실적인 콘텐츠 생성을 달성합니다. 다양한 벤치마크 실험을 통해 현실감, 경로 일관성, 시각적 충실도에서 우수성을 입증하였으며, 제어 가능한 비디오 합성을 위한 새로운 패러다임을 제시합니다.

## 🎯 주요 포인트

- 1. WorldForge는 훈련 없이 추론 시간에 작동하는 프레임워크로, 세 가지 모듈로 구성되어 있습니다.

- 2. Intra-Step Recursive Refinement는 각 디노이징 단계에서 네트워크 예측을 반복적으로 최적화하여 정확한 궤적 주입을 가능하게 합니다.

- 3. Flow-Gated Latent Fusion은 광학 흐름 유사성을 활용하여 잠재 공간에서 모션과 외형을 분리하고, 모션 관련 채널에 궤적 지침을 선택적으로 주입합니다.

- 4. Dual-Path Self-Corrective Guidance는 지침이 있는 경로와 없는 경로를 비교하여 구조적 신호의 노이즈나 불일치로 인한 궤적 드리프트를 적응적으로 수정합니다.

- 5. 이 연구는 제어 가능한 비디오 합성을 위한 새로운 플러그 앤 플레이 패러다임을 제시하며, 공간 지능을 위한 생성적 사전 지식을 활용하는 새로운 관점을 제공합니다.

---

*Generated on 2025-09-19 15:06:24*