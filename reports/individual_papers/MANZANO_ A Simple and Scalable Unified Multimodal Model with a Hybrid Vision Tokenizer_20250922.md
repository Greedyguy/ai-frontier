# MANZANO: A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer

**Korean Title:** MANZANO: 하이브리드 비전 토크나이저를 사용한 간단하고 확장 가능한 통합 멀티모달 모델

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Unified Multimodal Model|Unified Multimodal Model]] [[keywords/specific/Hybrid Image Tokenizer|Hybrid Image Tokenizer]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Computer Vision|Computer Vision]] [[keywords/unique/Manzano|Manzano]] [[categories/cs.LG|cs.LG]] [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (84.3% similar) [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (83.5% similar) [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unified Multimodal Model
**🔗 Specific Connectable**: Hybrid Image Tokenizer
**🔬 Broad Technical**: Large Language Models, Computer Vision
**⭐ Unique Technical**: Manzano
## 🔗 유사한 논문
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (84.3% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (83.5% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL Controllable Region-Level Text-To-Image Generation]] (82.0% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.7% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (81.4% similar)


**ArXiv ID**: [2509.16197](https://arxiv.org/abs/2509.16197)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16197.pdf)


**ArXiv ID**: [2509.16197](https://arxiv.org/abs/2509.16197)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16197.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unified Multimodal Model
**🔗 Specific Connectable**: Hybrid Image Tokenizer
**⭐ Unique Technical**: Manzano
**🔬 Broad Technical**: Large Language Models, Computer Vision

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Computer Vision` • 

`Hybrid Image Tokenizer` • 

`Manzano` • 

`Unified Multimodal Model`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16197v1 Announce Type: cross 
Abstract: Unified multimodal Large Language Models (LLMs) that can both understand and generate visual content hold immense potential. However, existing open-source models often suffer from a performance trade-off between these capabilities. We present Manzano, a simple and scalable unified framework that substantially reduces this tension by coupling a hybrid image tokenizer with a well-curated training recipe. A single shared vision encoder feeds two lightweight adapters that produce continuous embeddings for image-to-text understanding and discrete tokens for text-to-image generation within a common semantic space. A unified autoregressive LLM predicts high-level semantics in the form of text and image tokens, with an auxiliary diffusion decoder subsequently translating the image tokens into pixels. The architecture, together with a unified training recipe over understanding and generation data, enables scalable joint learning of both capabilities. Manzano achieves state-of-the-art results among unified models, and is competitive with specialist models, particularly on text-rich evaluation. Our studies show minimal task conflicts and consistent gains from scaling model size, validating our design choice of a hybrid tokenizer.

## 🔍 Abstract (한글 번역)

arXiv:2509.16197v1 발표 유형: 교차  
초록: 시각적 콘텐츠를 이해하고 생성할 수 있는 통합 멀티모달 대형 언어 모델(LLMs)은 엄청난 잠재력을 가지고 있습니다. 그러나 기존의 오픈 소스 모델은 이러한 기능들 간의 성능 절충 문제를 자주 겪습니다. 우리는 하이브리드 이미지 토크나이저와 잘 구성된 학습 레시피를 결합하여 이러한 긴장을 상당히 줄이는 간단하고 확장 가능한 통합 프레임워크인 Manzano를 소개합니다. 단일 공유 비전 인코더는 이미지-텍스트 이해를 위한 연속 임베딩과 텍스트-이미지 생성을 위한 이산 토큰을 공통 의미 공간 내에서 생성하는 두 개의 경량 어댑터에 데이터를 제공합니다. 통합 자가회귀 LLM은 텍스트 및 이미지 토큰 형태로 고수준의 의미를 예측하며, 보조 확산 디코더가 이후에 이미지 토큰을 픽셀로 변환합니다. 이 아키텍처는 이해 및 생성 데이터를 아우르는 통합 학습 레시피와 함께 두 기능의 확장 가능한 공동 학습을 가능하게 합니다. Manzano는 통합 모델 중 최첨단 결과를 달성하며, 특히 텍스트가 풍부한 평가에서 전문 모델과 경쟁력을 갖추고 있습니다. 우리의 연구는 최소한의 작업 충돌과 모델 크기 확장에서 일관된 이점을 보여주며, 하이브리드 토크나이저라는 설계 선택을 검증합니다.

## 📝 요약

Manzano는 시각 콘텐츠의 이해와 생성을 동시에 수행할 수 있는 통합 멀티모달 대형 언어 모델(LLM)로, 기존 모델의 성능 저하 문제를 해결합니다. 하이브리드 이미지 토크나이저와 잘 설계된 학습 방법을 통해 이미지-텍스트 이해와 텍스트-이미지 생성을 위한 연속 및 이산 토큰을 생성합니다. 이 모델은 통합된 자가회귀 LLM을 사용하여 텍스트와 이미지 토큰의 고수준 의미를 예측하고, 보조 확산 디코더가 이미지 토큰을 픽셀로 변환합니다. Manzano는 통합 모델 중 최첨단 성능을 보이며, 특히 텍스트가 많은 평가에서 전문 모델과 경쟁할 수 있습니다. 연구 결과, 모델 크기 확장에 따른 일관된 성능 향상이 확인되었습니다.

## 🎯 주요 포인트


- 1. Manzano는 하이브리드 이미지 토크나이저와 잘 구성된 학습 레시피를 결합하여 시각 콘텐츠 이해와 생성 간의 성능 저하 문제를 크게 줄입니다.

- 2. 단일 공유 비전 인코더가 이미지-텍스트 이해를 위한 연속 임베딩과 텍스트-이미지 생성을 위한 이산 토큰을 생성하는 두 개의 경량 어댑터에 데이터를 제공합니다.

- 3. Manzano는 통합된 학습 레시피를 통해 이해 및 생성 데이터를 학습하여 두 기능의 확장 가능한 공동 학습을 가능하게 합니다.

- 4. Manzano는 통합 모델 중에서 최첨단 결과를 달성하며, 특히 텍스트가 풍부한 평가에서 전문 모델과 경쟁할 수 있습니다.

- 5. 연구 결과, 하이브리드 토크나이저의 설계 선택이 유효하며, 모델 크기를 확장함에 따라 일관된 성능 향상을 보여줍니다.


---

*Generated on 2025-09-22 15:48:56*