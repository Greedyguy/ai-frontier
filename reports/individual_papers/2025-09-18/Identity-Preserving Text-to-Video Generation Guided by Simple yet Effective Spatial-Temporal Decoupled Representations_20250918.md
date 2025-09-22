
# Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations

**Korean Title:** 간단하면서도 효과적인 공간-시간 분리 표현에 의해 안내되는 신원 보존 텍스트-비디오 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Stage-wise Decoupled Generation

## 🔗 유사한 논문
- [[Iterative_Prompt_Refinement_for_Safer_Text-to-Image_Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (81.9% similar)
- [[Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis]] (81.0% similar)
- [[VSE-MOT_Multi-Object_Tracking_in_Low-Quality_Video_Scenes_Guided_by_Visual_Semantic_Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (80.2% similar)
- [[Generative_Image_Coding_with_Diffusion_Prior_20250918|Generative Image Coding with Diffusion Prior]] (79.7% similar)
- [[AgentCTG_Harnessing_Multi-Agent_Collaboration_for_Fine-Grained_Precise_Control_in_Text_Generation_20250918|AgentCTG: Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (78.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.04705v2 Announce Type: replace 
Abstract: Identity-preserving text-to-video (IPT2V) generation, which aims to create high-fidelity videos with consistent human identity, has become crucial for downstream applications. However, current end-to-end frameworks suffer a critical spatial-temporal trade-off: optimizing for spatially coherent layouts of key elements (e.g., character identity preservation) often compromises instruction-compliant temporal smoothness, while prioritizing dynamic realism risks disrupting the spatial coherence of visual structures. To tackle this issue, we propose a simple yet effective spatial-temporal decoupled framework that decomposes representations into spatial features for layouts and temporal features for motion dynamics. Specifically, our paper proposes a semantic prompt optimization mechanism and stage-wise decoupled generation paradigm. The former module decouples the prompt into spatial and temporal components. Aligned with the subsequent stage-wise decoupled approach, the spatial prompts guide the text-to-image (T2I) stage to generate coherent spatial features, while the temporal prompts direct the sequential image-to-video (I2V) stage to ensure motion consistency. Experimental results validate that our approach achieves excellent spatiotemporal consistency, demonstrating outstanding performance in identity preservation, text relevance, and video quality. By leveraging this simple yet robust mechanism, our algorithm secures the runner-up position in 2025 ACM MultiMedia Challenge.

## 🔍 Abstract (한글 번역)

arXiv:2507.04705v2 발표 유형: 대체
요약: 항등 보존 텍스트-비디오 (IPT2V) 생성은 일관된 인간 신원을 유지하면서 고품질 비디오를 만드는 것을 모향으로 하는데, 이는 하류 응용 프로그램에 중요해졌다. 그러나 현재의 end-to-end 프레임워크는 공간적-시간적 트레이드오프를 겪고 있다: 주요 요소들의 (예: 캐릭터 신원 보존) 공간적 일관된 레이아웃을 최적화하는 것은 종종 명령 준수적 시간적 부드러움을 희생시키는 반면, 동적 현실주의를 우선시하는 것은 시각적 구조의 공간적 일관성을 깨는 위험을 안고 있다. 이 문제를 해결하기 위해, 우리는 효과적이면서도 간단한 공간-시간적 분리된 프레임워크를 제안한다. 이 프레임워크는 레이아웃을 위한 공간적 특징과 동적 모션을 위한 시간적 특징으로 표현을 분해한다. 구체적으로, 우리의 논문은 의미론적 프롬프트 최적화 메커니즘과 단계별 분리된 생성 패러다임을 제안한다. 전자 모듈은 프롬프트를 공간적 및 시간적 구성 요소로 분리한다. 이어지는 단계별 분리된 접근과 일치하게, 공간적 프롬프트는 일관된 공간적 특징을 생성하기 위해 텍스트-이미지 (T2I) 단계를 안내하고, 시간적 프롬프트는 순차적 이미지-비디오 (I2V) 단계를 통해 모션 일관성을 보장한다. 실험 결과는 우리의 접근 방식이 우수한 시공간적 일관성을 달성하며, 신원 보존, 텍스트 관련성 및 비디오 품질에서 탁월한 성능을 보여준다는 것을 검증한다. 이 간단하면서도 견고한 메커니즘을 활용하여, 우리의 알고리즘은 2025년 ACM MultiMedia Challenge에서 준우승을 차지했다.

## 📝 요약

이 논문은 고품질 비디오 생성을 위한 신원 보존 텍스트-비디오(IPT2V) 생성에 초점을 맞추고 있다. 현재의 엔드 투 엔드 프레임워크는 공간적 일관성과 시간적 부드러움 사이의 중요한 트레이드 오프를 겪고 있는데, 이를 해결하기 위해 공간적-시간적으로 분리된 프레임워크를 제안하고 있다. 이를 통해 우수한 시공간 일관성을 달성하며, 신원 보존, 텍스트 관련성 및 비디오 품질에서 우수한 성능을 보여주었다. 이러한 간단하면서도 강력한 메커니즘을 활용하여, 해당 알고리즘은 2025 ACM MultiMedia Challenge에서 준우승을 차지했다.

## 🎯 주요 포인트

- Identity-preserving text-to-video (IPT2V) generation은 높은 품질의 비디오를 생성하는 것이 중요하다.

- 현재의 end-to-end frameworks는 공간적-시간적 trade-off에 취약하다.

- 제안된 spatial-temporal decoupled framework은 우수한 성능을 보여준다.

- 실험 결과는 제안된 방법이 우수한 성능을 보여줌을 입증한다.

---

*Generated on 2025-09-18 17:06:53*