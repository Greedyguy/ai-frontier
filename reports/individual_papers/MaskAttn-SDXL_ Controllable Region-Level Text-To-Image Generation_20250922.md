# MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation

**Korean Title:** MaskAttn-SDXL: 제어 가능한 영역 수준의 텍스트-이미지 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Region Level Gating

## 🔗 유사한 논문
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (85.4% similar)
- [[2025-09-22/VLA-Mark_ A cross modal watermark for large vision-language alignment model_20250922|VLA-Mark A cross modal watermark for large vision-language alignment model]] (83.4% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (83.1% similar)
- [[2025-09-19/End4_ End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection_20250919|End4 End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection]] (82.7% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (82.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15357v1 Announce Type: cross 
Abstract: Text-to-image diffusion models achieve impressive realism but often suffer from compositional failures on prompts with multiple objects, attributes, and spatial relations, resulting in cross-token interference where entities entangle, attributes mix across objects, and spatial cues are violated. To address these failures, we propose MaskAttn-SDXL,a region-level gating mechanism applied to the cross-attention logits of Stable Diffusion XL(SDXL)'s UNet. MaskAttn-SDXL learns a binary mask per layer, injecting it into each cross-attention logit map before softmax to sparsify token-to-latent interactions so that only semantically relevant connections remain active. The method requires no positional encodings, auxiliary tokens, or external region masks, and preserves the original inference path with negligible overhead. In practice, our model improves spatial compliance and attribute binding in multi-object prompts while preserving overall image quality and diversity. These findings demonstrate that logit-level maksed cross-attention is an data-efficient primitve for enforcing compositional control, and our method thus serves as a practical extension for spatial control in text-to-image generation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15357v1 발표 유형: 교차  
초록: 텍스트-이미지 확산 모델은 인상적인 현실감을 달성하지만, 여러 객체, 속성 및 공간 관계를 포함하는 프롬프트에서 조합적 실패를 겪는 경우가 많습니다. 이는 엔티티가 얽히고, 속성이 객체 간에 혼합되며, 공간적 단서가 위반되는 교차 토큰 간섭을 초래합니다. 이러한 실패를 해결하기 위해, 우리는 Stable Diffusion XL(SDXL)의 UNet의 교차 주의력 로짓에 적용되는 지역 수준의 게이팅 메커니즘인 MaskAttn-SDXL을 제안합니다. MaskAttn-SDXL은 각 레이어마다 이진 마스크를 학습하여, 소프트맥스 전에 각 교차 주의력 로짓 맵에 주입하여 토큰-잠재 상호작용을 희소화하여 의미적으로 관련 있는 연결만 활성 상태로 유지합니다. 이 방법은 위치 인코딩, 보조 토큰 또는 외부 지역 마스크가 필요하지 않으며, 원래의 추론 경로를 거의 추가 부담 없이 보존합니다. 실제로, 우리의 모델은 여러 객체 프롬프트에서 공간적 준수와 속성 결합을 개선하면서 전체 이미지 품질과 다양성을 유지합니다. 이러한 발견은 로짓 수준의 마스크된 교차 주의력이 조합적 제어를 시행하는 데이터 효율적인 원시임을 보여주며, 따라서 우리의 방법은 텍스트-이미지 생성에서 공간 제어를 위한 실용적인 확장으로 작용합니다.

## 📝 요약

이 논문은 텍스트-이미지 변환 모델의 합성 실패 문제를 해결하기 위해 MaskAttn-SDXL이라는 새로운 메커니즘을 제안합니다. 기존 모델은 여러 객체와 속성, 공간 관계가 포함된 프롬프트에서 객체 간 혼합과 속성 간섭이 발생하는 문제가 있었습니다. MaskAttn-SDXL은 Stable Diffusion XL의 UNet에서 교차 주의 로그잇에 적용되는 지역 수준 게이팅 메커니즘으로, 각 층마다 이진 마스크를 학습하여 관련 있는 연결만 활성화합니다. 이 방법은 위치 인코딩이나 보조 토큰 없이도 공간 준수와 속성 결합을 개선하며, 이미지 품질과 다양성을 유지합니다. 이 연구는 데이터 효율적인 합성 제어 방법을 제시하며, 텍스트-이미지 생성에서 공간 제어를 위한 실용적인 확장으로 작용할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 텍스트-이미지 변환 확산 모델은 현실감이 뛰어나지만, 여러 객체와 속성, 공간 관계를 포함한 프롬프트에서 구성 실패를 겪을 수 있다.

- 2. MaskAttn-SDXL은 Stable Diffusion XL(SDXL)의 UNet의 교차 주의력 로짓에 적용되는 지역 수준 게이팅 메커니즘으로, 교차-토큰 간섭 문제를 해결한다.

- 3. MaskAttn-SDXL은 각 레이어에 이진 마스크를 학습하여, 소프트맥스 이전에 교차 주의력 로짓 맵에 주입하여 의미적으로 관련 있는 연결만 활성화되도록 한다.

- 4. 이 방법은 위치 인코딩, 보조 토큰, 외부 지역 마스크가 필요 없으며, 원래의 추론 경로를 거의 변경하지 않고 유지한다.

- 5. 제안된 모델은 다중 객체 프롬프트에서 공간 준수 및 속성 결합을 개선하면서 전체 이미지 품질과 다양성을 유지한다.

---

*Generated on 2025-09-22 15:37:27*