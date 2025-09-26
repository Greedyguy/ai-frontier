---
keywords:
  - Vision Transformers
  - Multimodal Contrastive Learning
  - Foundation Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14084
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:59:06.523965",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision Transformers",
    "Multimodal Contrastive Learning",
    "Foundation Models"
  ],
  "rejected_keywords": [
    "Zero-Shot Anomaly Detection",
    "Anomaly-Aware Calibration Module"
  ],
  "similarity_scores": {
    "Vision Transformers": 0.82,
    "Multimodal Contrastive Learning": 0.79,
    "Foundation Models": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration

**Korean Title:** AD-DINOv3: 이상 감지 인식 보정을 통한 제로샷 이상 감지를 위한 DINOv3 개선

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision Transformers|Vision Transformers]], [[keywords/Foundation Models|Foundation Models]]
**🚀 Evolved Concepts**: [[keywords/Multimodal Contrastive Learning|Multimodal Contrastive Learning]]

## 🔗 유사한 논문
- [[Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (81.4% similar)
- [[Multi-label Scene Classification for Autonomous Vehicles Acquiring and Accumulating Knowledge from Diverse Datasets]] (80.1% similar)
- [[DACoN DINO for Anime Paint Bucket Colorization with Any Number of Reference Images]] (79.8% similar)
- [[Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (79.5% similar)
- [[An Empirical Analysis of VLM-based OOD Detection Mechanisms, Advantages, and Sensitivity]] (79.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14084v2 Announce Type: replace 
Abstract: Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP model, which performs anomaly detection by calculating the similarity between visual and text embeddings. Recently, vision foundation models such as DINOv3 have demonstrated strong transferable representation capabilities. In this work, we are the first to adapt DINOv3 for ZSAD. However, this adaptation presents two key challenges: (i) the domain bias between large-scale pretraining data and anomaly detection tasks leads to feature misalignment; and (ii) the inherent bias toward global semantics in pretrained representations often leads to subtle anomalies being misinterpreted as part of the normal foreground objects, rather than being distinguished as abnormal regions. To overcome these challenges, we introduce AD-DINOv3, a novel vision-language multimodal framework designed for ZSAD. Specifically, we formulate anomaly detection as a multimodal contrastive learning problem, where DINOv3 is employed as the visual backbone to extract patch tokens and a CLS token, and the CLIP text encoder provides embeddings for both normal and abnormal prompts. To bridge the domain gap, lightweight adapters are introduced in both modalities, enabling their representations to be recalibrated for the anomaly detection task. Beyond this baseline alignment, we further design an Anomaly-Aware Calibration Module (AACM), which explicitly guides the CLS token to attend to anomalous regions rather than generic foreground semantics, thereby enhancing discriminability. Extensive experiments on eight industrial and medical benchmarks demonstrate that AD-DINOv3 consistently matches or surpasses state-of-the-art methods.The code will be available at https://github.com/Kaisor-Yuan/AD-DINOv3.

## 🔍 Abstract (한글 번역)

arXiv:2509.14084v2 발표 유형: 교체  
초록: 제로샷 이상 탐지(ZSAD)는 임의의 새로운 범주에서 이상을 식별하여 확장 가능하고 주석 효율적인 솔루션을 제공합니다. 전통적으로 대부분의 ZSAD 연구는 시각 및 텍스트 임베딩 간의 유사성을 계산하여 이상 탐지를 수행하는 CLIP 모델에 기반을 두고 있습니다. 최근 DINOv3와 같은 비전 기반 모델은 강력한 전이 표현 능력을 입증했습니다. 본 연구에서는 DINOv3를 ZSAD에 최초로 적용했습니다. 그러나 이 적응에는 두 가지 주요 과제가 있습니다: (i) 대규모 사전 학습 데이터와 이상 탐지 작업 간의 도메인 편향으로 인해 특징 정렬이 잘못될 수 있으며; (ii) 사전 학습된 표현의 전역 의미론에 대한 내재적 편향으로 인해 미세한 이상이 정상적인 전경 객체의 일부로 잘못 해석되어 비정상 영역으로 구별되지 않는 경우가 많습니다. 이러한 과제를 극복하기 위해, 우리는 ZSAD를 위해 설계된 새로운 비전-언어 멀티모달 프레임워크인 AD-DINOv3를 소개합니다. 구체적으로, 우리는 이상 탐지를 멀티모달 대조 학습 문제로 공식화하며, DINOv3를 시각적 백본으로 사용하여 패치 토큰과 CLS 토큰을 추출하고, CLIP 텍스트 인코더는 정상 및 비정상 프롬프트에 대한 임베딩을 제공합니다. 도메인 격차를 해소하기 위해, 두 가지 모달리티에 경량 어댑터를 도입하여 이상 탐지 작업에 맞게 표현을 재조정할 수 있도록 합니다. 이 기본 정렬을 넘어, 우리는 CLS 토큰이 일반적인 전경 의미론보다 비정상 영역에 주목하도록 명시적으로 안내하는 이상 인식 보정 모듈(AACM)을 추가 설계하여 변별력을 향상시킵니다. 8개의 산업 및 의료 벤치마크에 대한 광범위한 실험을 통해 AD-DINOv3가 일관되게 최첨단 방법과 동등하거나 그 이상의 성능을 발휘함을 입증합니다. 코드는 https://github.com/Kaisor-Yuan/AD-DINOv3에서 제공될 예정입니다.

## 📝 요약

이 논문은 Zero-Shot Anomaly Detection(ZSAD)에서 DINOv3 모델을 최초로 적용하여 새로운 비정상 범주를 식별하는 방법을 제안합니다. 기존 CLIP 모델 기반의 ZSAD 접근법과 달리, DINOv3의 강력한 전이 학습 능력을 활용합니다. 그러나 대규모 사전 학습 데이터와 비정상 탐지 작업 간의 도메인 편향, 그리고 사전 학습된 표현의 전역 의미 편향으로 인해 발생하는 문제를 해결하기 위해, AD-DINOv3라는 새로운 비전-언어 멀티모달 프레임워크를 도입했습니다. 이 프레임워크는 멀티모달 대조 학습 문제로 비정상 탐지를 정의하고, DINOv3를 시각적 백본으로 사용하며, CLIP 텍스트 인코더를 통해 정상 및 비정상 프롬프트의 임베딩을 제공합니다. 도메인 격차를 줄이기 위해 경량 어댑터를 도입하고, Anomaly-Aware Calibration Module(AACM)을 설계하여 CLS 토큰이 비정상 영역에 집중하도록 유도합니다. 8개의 산업 및 의료 벤치마크 실험에서 AD-DINOv3는 최신 기법과 동등하거나 이를 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Zero-Shot Anomaly Detection(ZSAD)는 새로운 범주의 이상을 식별하여 확장 가능하고 주석 효율적인 솔루션을 제공합니다.

- 2. 기존 ZSAD 연구는 주로 CLIP 모델을 기반으로 했으나, 본 연구에서는 DINOv3를 최초로 ZSAD에 적용했습니다.

- 3. DINOv3의 ZSAD 적용 시, 대규모 사전 학습 데이터와 이상 탐지 작업 간의 도메인 편향 및 전역 의미에 대한 편향이 문제로 작용합니다.

- 4. AD-DINOv3는 이러한 문제를 해결하기 위해 설계된 새로운 비전-언어 멀티모달 프레임워크로, 멀티모달 대조 학습 문제로 이상 탐지를 공식화합니다.

- 5. AD-DINOv3는 8개의 산업 및 의료 벤치마크에서 최신 방법과 비교하여 일관되게 동등하거나 뛰어난 성능을 보였습니다.

---

*Generated on 2025-09-19 16:19:58*