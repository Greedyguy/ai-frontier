---
keywords:
  - Product Retrieval
  - Computer Vision
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14985
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:29:33.239823",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Product Retrieval",
    "Computer Vision",
    "Vision-Language Model"
  ],
  "rejected_keywords": [
    "Pixel-wise Matching",
    "Foundation Models"
  ],
  "similarity_scores": {
    "Product Retrieval": 0.78,
    "Computer Vision": 0.85,
    "Vision-Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# PRISM: Product Retrieval In Shopping Carts using Hybrid Matching

**Korean Title:** PRISM: 하이브리드 매칭을 활용한 쇼핑 카트 내 제품 검색

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/Product Retrieval|Product Retrieval]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 🔗 유사한 논문
- [[Chain-of-Thought Re-ranking for Image Retrieval Tasks_20250919|Chain-of-Thought Re-ranking for Image Retrieval Tasks]] (81.4% similar)
- [[What's the Best Way to Retrieve Slides_ A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques_20250919|What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques]] (80.7% similar)
- [[Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (79.7% similar)
- [[PRISM-DP Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (79.6% similar)
- [[Re-purposing SAM into Efficient Visual Projectors for MLLM-Based Referring Image Segmentation]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14985v1 Announce Type: new 
Abstract: Compared to traditional image retrieval tasks, product retrieval in retail settings is even more challenging. Products of the same type from different brands may have highly similar visual appearances, and the query image may be taken from an angle that differs significantly from view angles of the stored catalog images. Foundational models, such as CLIP and SigLIP, often struggle to distinguish these subtle but important local differences. Pixel-wise matching methods, on the other hand, are computationally expensive and incur prohibitively high matching times. In this paper, we propose a new, hybrid method, called PRISM, for product retrieval in retail settings by leveraging the advantages of both vision-language model-based and pixel-wise matching approaches. To provide both efficiency/speed and finegrained retrieval accuracy, PRISM consists of three stages: 1) A vision-language model (SigLIP) is employed first to retrieve the top 35 most semantically similar products from a fixed gallery, thereby narrowing the search space significantly; 2) a segmentation model (YOLO-E) is applied to eliminate background clutter; 3) fine-grained pixel-level matching is performed using LightGlue across the filtered candidates. This framework enables more accurate discrimination between products with high inter-class similarity by focusing on subtle visual cues often missed by global models. Experiments performed on the ABV dataset show that our proposed PRISM outperforms the state-of-the-art image retrieval methods by 4.21% in top-1 accuracy while still remaining within the bounds of real-time processing for practical retail deployments.

## 🔍 Abstract (한글 번역)

arXiv:2509.14985v1 발표 유형: 신규  
초록: 전통적인 이미지 검색 작업에 비해 소매 환경에서의 제품 검색은 더욱 도전적입니다. 다른 브랜드의 동일 유형 제품은 시각적으로 매우 유사할 수 있으며, 쿼리 이미지는 저장된 카탈로그 이미지의 시점과 크게 다른 각도에서 촬영될 수 있습니다. CLIP 및 SigLIP과 같은 기초 모델은 이러한 미묘하지만 중요한 지역 차이를 구별하는 데 종종 어려움을 겪습니다. 반면에 픽셀 단위 매칭 방법은 계산 비용이 많이 들고 매칭 시간이 지나치게 길어질 수 있습니다. 본 논문에서는 소매 환경에서 제품 검색을 위해 비전-언어 모델 기반 접근법과 픽셀 단위 매칭 접근법의 장점을 활용한 새로운 하이브리드 방법인 PRISM을 제안합니다. 효율성과 속도, 그리고 세밀한 검색 정확성을 모두 제공하기 위해 PRISM은 세 가지 단계로 구성됩니다: 1) 비전-언어 모델(SigLIP)을 먼저 사용하여 고정 갤러리에서 가장 의미적으로 유사한 상위 35개 제품을 검색하여 검색 공간을 크게 좁힙니다; 2) 배경 잡음을 제거하기 위해 세그멘테이션 모델(YOLO-E)을 적용합니다; 3) 필터링된 후보들 간에 LightGlue를 사용하여 세밀한 픽셀 수준 매칭을 수행합니다. 이 프레임워크는 전역 모델이 종종 놓치는 미묘한 시각적 단서를 집중하여 높은 클래스 간 유사성을 가진 제품 간의 보다 정확한 구별을 가능하게 합니다. ABV 데이터셋에서 수행된 실험은 제안된 PRISM이 최첨단 이미지 검색 방법보다 상위 1 정확도에서 4.21% 더 우수하며, 실질적인 소매 배포를 위한 실시간 처리 범위 내에 여전히 남아 있음을 보여줍니다.

## 📝 요약

이 논문은 소매 환경에서 제품 검색의 어려움을 해결하기 위해 PRISM이라는 새로운 하이브리드 방법을 제안합니다. PRISM은 시각-언어 모델과 픽셀 매칭 방식을 결합하여 효율성과 정밀도를 동시에 제공합니다. 세 단계로 구성된 이 방법은 먼저 SigLIP 모델을 사용해 의미적으로 유사한 상위 35개 제품을 선택하고, YOLO-E 모델로 배경을 제거한 후, LightGlue를 통해 세밀한 픽셀 매칭을 수행합니다. ABV 데이터셋 실험 결과, PRISM은 최첨단 이미지 검색 방법보다 4.21% 높은 정확도를 보였으며, 실시간 처리 가능성을 유지합니다.

## 🎯 주요 포인트

- 1. PRISM은 소매 환경에서 제품 검색을 위해 비전-언어 모델과 픽셀 단위 매칭 접근법의 장점을 결합한 하이브리드 방법입니다.

- 2. PRISM은 검색 효율성과 세밀한 검색 정확도를 제공하기 위해 세 가지 단계로 구성됩니다: 1) SigLIP을 사용한 초기 유사 제품 검색, 2) YOLO-E를 통한 배경 제거, 3) LightGlue를 통한 세밀한 픽셀 수준 매칭.

- 3. PRISM은 높은 클래스 간 유사성을 가진 제품들 간의 미세한 시각적 차이를 구별하는 데 효과적입니다.

- 4. ABV 데이터셋 실험 결과, PRISM은 최신 이미지 검색 방법보다 top-1 정확도에서 4.21% 향상된 성능을 보이며 실시간 처리 가능성을 유지합니다.

---

*Generated on 2025-09-19 16:08:51*