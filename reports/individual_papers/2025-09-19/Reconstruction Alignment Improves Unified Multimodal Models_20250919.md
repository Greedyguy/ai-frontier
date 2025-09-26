---
keywords:
  - Multi-Modal Learning
  - Reconstruction Alignment
  - Diffusion Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.07295
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:27:16.543149",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Modal Learning",
    "Reconstruction Alignment",
    "Diffusion Models"
  ],
  "rejected_keywords": [
    "Self-Supervised Learning"
  ],
  "similarity_scores": {
    "Multi-Modal Learning": 0.82,
    "Reconstruction Alignment": 0.78,
    "Diffusion Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Reconstruction Alignment Improves Unified Multimodal Models

**Korean Title:** 재구성 정렬이 통합 멀티모달 모델을 개선한다.

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion-based UMMs]]
**⚡ Unique Technical**: [[keywords/Reconstruction Alignment|Reconstruction Alignment]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|Unified Multimodal Models]]

## 🔗 유사한 논문
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.2% similar)
- [[Masked_Feature_Modeling_Enhances_Adaptive_Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (81.6% similar)
- [[MOCHA Multi-modal Objects-aware Cross-arcHitecture Alignment]] (80.8% similar)
- [[Superpose_Task-specific_Features_for_Model_Merging_20250919|Superpose Task-specific Features for Model Merging]] (80.6% similar)
- [[Generalizable_Geometric_Image_Caption_Synthesis_20250919|Generalizable Geometric Image Caption Synthesis]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07295v2 Announce Type: replace-cross 
Abstract: Unified multimodal models (UMMs) unify visual understanding and generation within a single architecture. However, conventional training relies on image-text pairs (or sequences) whose captions are typically sparse and miss fine-grained visual details--even when they use hundreds of words to describe a simple image. We introduce Reconstruction Alignment (RecA), a resource-efficient post-training method that leverages visual understanding encoder embeddings as dense "text prompts," providing rich supervision without captions. Concretely, RecA conditions a UMM on its own visual understanding embeddings and optimizes it to reconstruct the input image with a self-supervised reconstruction loss, thereby realigning understanding and generation. Despite its simplicity, RecA is broadly applicable: across autoregressive, masked-autoregressive, and diffusion-based UMMs, it consistently improves generation and editing fidelity. With only 27 GPU-hours, post-training with RecA substantially improves image generation performance on GenEval (0.73$\rightarrow$0.90) and DPGBench (80.93$\rightarrow$88.15), while also boosting editing benchmarks (ImgEdit 3.38$\rightarrow$3.75, GEdit 6.94$\rightarrow$7.25). Notably, RecA surpasses much larger open-source models and applies broadly across diverse UMM architectures, establishing it as an efficient and general post-training alignment strategy for UMMs

## 🔍 Abstract (한글 번역)

arXiv:2509.07295v2 발표 유형: 교체-크로스  
초록: 통합 다중 모달 모델(UMMs)은 시각적 이해와 생성을 단일 아키텍처 내에서 통합합니다. 그러나 기존의 훈련은 이미지-텍스트 쌍(또는 시퀀스)에 의존하며, 이들의 캡션은 일반적으로 드문드문하고 세밀한 시각적 세부사항을 놓치는 경우가 많습니다. 심지어 간단한 이미지를 설명하기 위해 수백 단어를 사용할 때도 마찬가지입니다. 우리는 캡션 없이 풍부한 감독을 제공하는 밀집한 "텍스트 프롬프트"로 시각적 이해 인코더 임베딩을 활용하는 자원 효율적인 사후 훈련 방법인 재구성 정렬(RecA)을 소개합니다. 구체적으로, RecA는 UMM을 자체 시각적 이해 임베딩에 조건화하고, 자기 지도 재구성 손실을 통해 입력 이미지를 재구성하도록 최적화하여 이해와 생성을 재정렬합니다. 그 단순함에도 불구하고, RecA는 광범위하게 적용 가능합니다: 자회귀, 마스크드 자회귀, 확산 기반 UMM에 걸쳐, RecA는 일관되게 생성 및 편집 충실도를 향상시킵니다. 단 27 GPU-시간만으로, RecA를 통한 사후 훈련은 GenEval(0.73→0.90) 및 DPGBench(80.93→88.15)에서 이미지 생성 성능을 크게 향상시키며, 편집 벤치마크(ImgEdit 3.38→3.75, GEdit 6.94→7.25)도 함께 향상시킵니다. 특히, RecA는 훨씬 더 큰 오픈 소스 모델을 능가하며 다양한 UMM 아키텍처에 광범위하게 적용되어, UMM을 위한 효율적이고 일반적인 사후 훈련 정렬 전략으로 자리 잡습니다.

## 📝 요약

이 논문은 통합 멀티모달 모델(UMM)을 위한 새로운 후처리 방법인 Reconstruction Alignment(RecA)를 제안합니다. RecA는 시각적 이해 인코더 임베딩을 "텍스트 프롬프트"로 활용하여 캡션 없이도 풍부한 감독을 제공합니다. 이 방법은 UMM이 자신의 시각적 이해 임베딩을 기반으로 입력 이미지를 재구성하도록 최적화하여 이해와 생성의 재정렬을 돕습니다. RecA는 간단하면서도 효과적이며, 다양한 UMM 아키텍처에 적용 가능하고, 생성 및 편집 성능을 크게 향상시킵니다. 실험 결과, RecA는 GenEval과 DPGBench에서 이미지 생성 성능을 크게 개선하고, 편집 벤치마크에서도 성능을 높였습니다. RecA는 효율적이고 일반적인 UMM의 후처리 정렬 전략으로 자리잡았습니다.

## 🎯 주요 포인트

- 1. 통합 멀티모달 모델(UMM)은 시각적 이해와 생성을 단일 아키텍처 내에서 통합합니다.

- 2. 기존의 이미지-텍스트 쌍을 활용한 훈련은 세부적인 시각적 정보를 놓치는 경우가 많습니다.

- 3. Reconstruction Alignment(RecA)은 캡션 없이도 풍부한 감독을 제공하는 자원 효율적인 후처리 방법입니다.

- 4. RecA는 자가 감독 재구성 손실을 통해 입력 이미지를 재구성하여 이해와 생성을 재정렬합니다.

- 5. RecA는 다양한 UMM 아키텍처에 적용 가능하며, 이미지 생성 및 편집 성능을 크게 향상시킵니다.

---

*Generated on 2025-09-19 15:22:21*