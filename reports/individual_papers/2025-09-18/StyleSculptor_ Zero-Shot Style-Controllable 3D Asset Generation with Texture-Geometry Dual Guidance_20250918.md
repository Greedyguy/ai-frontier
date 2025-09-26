---
keywords:
  - Style Disentangled Attention
  - Attention Mechanism
  - Zero-Shot Style Control
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13301
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:08:39.421242",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Style Disentangled Attention",
    "Attention Mechanism",
    "Zero-Shot Style Control"
  ],
  "rejected_keywords": [
    "3D Asset Generation"
  ],
  "similarity_scores": {
    "Style Disentangled Attention": 0.78,
    "Attention Mechanism": 0.8,
    "Zero-Shot Style Control": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# StyleSculptor: Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance

**Korean Title:** 스타일스컬프터: 텍스처-기하학 이중 가이드로 제로샷 스타일 제어 가능한 3D 에셋 생성 유지

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Style Disentangled Attention|Style Disentangled Attention]], [[keywords/Zero-Shot Style Control|Zero-Shot Style Control]]

## 🔗 유사한 논문
- [[CraftMesh: High-Fidelity Generative Mesh Manipulation via Poisson Seamless Fusion]] (78.4% similar)
- [[Identity-Preserving_Text-to-Video_Generation_Guided_by_Simple_yet_Effective_Spatial-Temporal_Decoupled_Representations_20250918|Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations]] (76.6% similar)
- [[Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis]] (76.5% similar)
- [[Lightweight_Gradient-Aware_Upscaling_of_3D_Gaussian_Splatting_Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (76.3% similar)
- [[textsc{Gen2Real}_Towards_Demo-Free_Dexterous_Manipulation_by_Harnessing_Generated_Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (76.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13301v2 Announce Type: replace 
Abstract: Creating 3D assets that follow the texture and geometry style of existing ones is often desirable or even inevitable in practical applications like video gaming and virtual reality. While impressive progress has been made in generating 3D objects from text or images, creating style-controllable 3D assets remains a complex and challenging problem. In this work, we propose StyleSculptor, a novel training-free approach for generating style-guided 3D assets from a content image and one or more style images. Unlike previous works, StyleSculptor achieves style-guided 3D generation in a zero-shot manner, enabling fine-grained 3D style control that captures the texture, geometry, or both styles of user-provided style images. At the core of StyleSculptor is a novel Style Disentangled Attention (SD-Attn) module, which establishes a dynamic interaction between the input content image and style image for style-guided 3D asset generation via a cross-3D attention mechanism, enabling stable feature fusion and effective style-guided generation. To alleviate semantic content leakage, we also introduce a style-disentangled feature selection strategy within the SD-Attn module, which leverages the variance of 3D feature patches to disentangle style- and content-significant channels, allowing selective feature injection within the attention framework. With SD-Attn, the network can dynamically compute texture-, geometry-, or both-guided features to steer the 3D generation process. Built upon this, we further propose the Style Guided Control (SGC) mechanism, which enables exclusive geometry- or texture-only stylization, as well as adjustable style intensity control. Extensive experiments demonstrate that StyleSculptor outperforms existing baseline methods in producing high-fidelity 3D assets.

## 🔍 Abstract (한글 번역)

arXiv: 2509.13301v2 발표 유형: 대체
요약: 기존 3D 자산의 질감과 기하학적 스타일을 따르는 3D 자산을 만드는 것은 비디오 게임 및 가상 현실과 같은 실용적인 응용 프로그램에서 종종 바람직하거나 필연적입니다. 텍스트나 이미지에서 3D 객체를 생성하는 데 많은 진전이 있었지만, 스타일을 제어할 수 있는 3D 자산을 생성하는 것은 여전히 복잡하고 어려운 문제입니다. 본 연구에서는 콘텐츠 이미지와 하나 이상의 스타일 이미지에서 스타일 가이드 3D 자산을 생성하는 새로운 훈련 불필요한 방법인 StyleSculptor를 제안합니다. 이전 작업과는 달리, StyleSculptor는 제로샷 방식으로 스타일 가이드 3D 생성을 달성하여 사용자가 제공한 스타일 이미지의 질감, 기하학 또는 두 가지 스타일을 포착하는 세밀한 3D 스타일 제어를 가능하게 합니다. StyleSculptor의 핵심은 새로운 스타일 이분화 주의 (SD-Attn) 모듈로, 입력 콘텐츠 이미지와 스타일 이미지 간의 동적 상호 작용을 통해 교차 3D 주의 메커니즘을 통해 스타일 가이드 3D 자산 생성을 가능하게 하는 안정적인 특징 융합과 효과적인 스타일 가이드 생성을 구축합니다. 의미론적 콘텐츠 누출을 완화하기 위해, SD-Attn 모듈 내에서 스타일 이분화 특징 선택 전략을 소개하여 3D 특징 패치의 분산을 활용하여 스타일 및 콘텐츠 중요한 채널을 분리하고 주의 프레임워크 내에서 선택적 특징 주입을 가능하게 합니다. SD-Attn을 통해 네트워크는 질감, 기하학 또는 둘 다를 가이드하는 특징을 동적으로 계산하여 3D 생성 프로세스를 조절할 수 있습니다. 이를 기반으로, 우리는 독점적인 기하학 또는 질감만 스타일화 및 조절 가능한 스타일 강도 제어를 가능하게 하는 Style Guided Control (SGC) 메커니즘을 제안합니다. 광범위한 실험 결과는 StyleSculptor가 고품질의 3D 자산을 생성하는 기존 기준선 방법을 능가한다는 것을 보여줍니다.

## 📝 요약

본 연구에서는 기존 3D 자산의 질감과 기하학적 스타일을 따르는 3D 자산을 생성하는 것이 매우 중요한데, 이를 위해 StyleSculptor라는 새로운 방법론을 제안한다. 이 방법은 학습이 필요 없는 방식으로 콘텐츠 이미지와 하나 이상의 스타일 이미지로부터 스타일 가이드 3D 자산을 생성한다. StyleSculptor는 Style Disentangled Attention (SD-Attn) 모듈을 통해 스타일 가이드 3D 자산 생성을 가능하게 하며, 이를 통해 고해상도 3D 자산을 생성하는 데 있어 기존 방법론들보다 우수한 성능을 보여준다.

## 🎯 주요 포인트

- 1. 기존 3D 자산의 텍스처와 기하학 스타일을 따르는 3D 자산 생성은 실용적인 응용 프로그램에서 불가피하며 원하는 경우가 많다.

- 2. StyleSculptor는 훈련 없이 컨텐츠 이미지와 하나 이상의 스타일 이미지로부터 스타일 가이드 3D 자산을 생성하는 혁신적인 방법을 제안한다.

- 3. SD-Attn 모듈을 통해 StyleSculptor는 안정적인 특징 퓨전과 효과적인 스타일 가이드 생성을 가능하게 한다.

- 4. SGC 메커니즘을 통해 StyleSculptor는 독점적인 기하학 또는 텍스처만 스타일화할 수 있으며 조절 가능한 스타일 강도 제어도 가능하다.

- 5. 다양한 실험에서 StyleSculptor가 고품질 3D 자산을 생성하는 데 기존 기준선 방법을 능가한다.

---

*Generated on 2025-09-18 17:08:00*