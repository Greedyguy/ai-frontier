---
keywords:
  - GCDance
  - Diffusion Models
  - CLIP
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2502.18309
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:42:21.242305",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "GCDance",
    "Diffusion Models",
    "CLIP"
  ],
  "rejected_keywords": [
    "Music-Driven Dance Generation"
  ],
  "similarity_scores": {
    "GCDance": 0.8,
    "Diffusion Models": 0.78,
    "CLIP": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# GCDance: Genre-Controlled 3D Full Body Dance Generation Driven By Music

**Korean Title:** GCDance: 음악에 의해 구동되는 장르 제어 3D 전신 댄스 생성

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Framework]], [[keywords/CLIP|CLIP]]
**⚡ Unique Technical**: [[keywords/GCDance|GCDance]]

## 🔗 유사한 논문
- [[WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (77.3% similar)
- [[FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (77.3% similar)
- [[Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (76.5% similar)
- [[Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation_20250919|Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation]] (76.5% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (76.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.18309v2 Announce Type: replace-cross 
Abstract: Generating high-quality full-body dance sequences from music is a challenging task as it requires strict adherence to genre-specific choreography. Moreover, the generated sequences must be both physically realistic and precisely synchronized with the beats and rhythm of the music. To overcome these challenges, we propose GCDance, a classifier-free diffusion framework for generating genre-specific dance motions conditioned on both music and textual prompts. Specifically, our approach extracts music features by combining high-level pre-trained music foundation model features with hand-crafted features for multi-granularity feature fusion. To achieve genre controllability, we leverage CLIP to efficiently embed genre-based textual prompt representations at each time step within our dance generation pipeline. Our GCDance framework can generate diverse dance styles from the same piece of music while ensuring coherence with the rhythm and melody of the music. Extensive experimental results obtained on the FineDance dataset demonstrate that GCDance significantly outperforms the existing state-of-the-art approaches, which also achieve competitive results on the AIST++ dataset. Our ablation and inference time analysis demonstrate that GCDance provides an effective solution for high-quality music-driven dance generation.

## 🔍 Abstract (한글 번역)

arXiv:2502.18309v2 발표 유형: 교차 교체  
초록: 음악으로부터 고품질의 전신 댄스 시퀀스를 생성하는 것은 장르별 안무에 대한 엄격한 준수가 필요하기 때문에 도전적인 과제입니다. 또한, 생성된 시퀀스는 물리적으로 현실적이어야 하며 음악의 비트와 리듬에 정확히 동기화되어야 합니다. 이러한 도전 과제를 극복하기 위해, 우리는 음악과 텍스트 프롬프트에 조건화된 장르별 댄스 동작을 생성하기 위한 분류기 없는 확산 프레임워크인 GCDance를 제안합니다. 구체적으로, 우리의 접근법은 고수준의 사전 학습된 음악 기초 모델 특징과 수작업으로 제작된 특징을 결합하여 다중 세분화 특징 융합을 통해 음악 특징을 추출합니다. 장르 제어 가능성을 달성하기 위해, 우리는 CLIP을 활용하여 댄스 생성 파이프라인 내의 각 시간 단계에서 장르 기반 텍스트 프롬프트 표현을 효율적으로 임베딩합니다. 우리의 GCDance 프레임워크는 동일한 음악 조각에서 다양한 댄스 스타일을 생성할 수 있으며, 음악의 리듬과 멜로디와의 일관성을 보장합니다. FineDance 데이터셋에서 얻은 광범위한 실험 결과는 GCDance가 기존의 최첨단 접근법을 크게 능가하며, AIST++ 데이터셋에서도 경쟁력 있는 결과를 달성함을 보여줍니다. 우리의 소거 및 추론 시간 분석은 GCDance가 고품질 음악 기반 댄스 생성에 대한 효과적인 솔루션을 제공함을 입증합니다.

## 📝 요약

GCDance는 음악에 맞춰 장르별 춤 동작을 생성하는 새로운 프레임워크로, 장르 특유의 안무를 엄격히 준수하면서도 물리적으로 현실적이고 음악의 비트와 리듬에 정확히 맞춰진 춤 시퀀스를 생성합니다. 이 방법은 고수준의 사전 학습된 음악 모델 특징과 수작업 특징을 결합하여 음악 특징을 추출하고, CLIP을 활용해 장르 기반 텍스트 프롬프트를 효율적으로 임베딩하여 장르 제어 가능성을 높입니다. GCDance는 FineDance 데이터셋에서 기존 최첨단 방법들을 능가하는 성능을 보였고, AIST++ 데이터셋에서도 경쟁력 있는 결과를 얻었습니다. 이 연구는 고품질의 음악 기반 춤 생성에 효과적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. GCDance는 음악과 텍스트 프롬프트에 기반하여 장르 특화 춤 동작을 생성하는 분류기 없는 확산 프레임워크입니다.

- 2. 음악 특징 추출을 위해 고수준의 사전 학습된 음악 모델 특징과 수작업 특징을 결합하여 다중 세분화 특징 융합을 구현합니다.

- 3. CLIP을 활용하여 장르 기반 텍스트 프롬프트 표현을 각 시간 단계에서 효율적으로 임베딩하여 장르 제어 가능성을 확보합니다.

- 4. GCDance는 동일한 음악에서 다양한 춤 스타일을 생성하며, 음악의 리듬과 멜로디와의 일관성을 유지합니다.

- 5. FineDance 데이터셋에서의 실험 결과, GCDance는 기존 최첨단 접근법을 능가하며 AIST++ 데이터셋에서도 경쟁력 있는 성과를 보입니다.

---

*Generated on 2025-09-19 16:20:19*