---
keywords:
  - Multimodal Learning
  - Transformer
  - Self-supervised Learning
  - Vector Database
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15858
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:53:45.423207",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Transformer",
    "Self-supervised Learning",
    "Vector Database"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Transformer": 0.85,
    "Self-supervised Learning": 0.8,
    "Vector Database": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal product deduplication",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal deduplication"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of integrating multiple data types, enhancing understanding of cross-modal applications.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "BERT architecture",
        "canonical": "Transformer",
        "aliases": [
          "BERT",
          "Bidirectional Encoder Representations from Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the widely-used Transformer model, facilitating discussions on NLP advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "MaskedAutoEncoders",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "MAE"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the use of self-supervised techniques in image representation, relevant for linking to similar methodologies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Milvus",
        "canonical": "Vector Database",
        "aliases": [
          "Milvus database"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a specific tool for vector similarity search, valuable for discussions on database technologies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "e-commerce",
      "product listings",
      "system RAM"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal product deduplication",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "BERT architecture",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "MaskedAutoEncoders",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Milvus",
      "resolved_canonical": "Vector Database",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings

**Korean Title:** 전자상거래에서 다중 모달 임베딩을 활용한 제품 중복 제거 최적화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15858.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15858](https://arxiv.org/abs/2509.15858)

## 🔗 유사한 논문
- [[2025-09-18/RoboEye_ Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching_20250918|RoboEye: Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching]] (82.1% similar)
- [[2025-09-19/PRISM_ Product Retrieval In Shopping Carts using Hybrid Matching_20250919|PRISM: Product Retrieval In Shopping Carts using Hybrid Matching]] (82.0% similar)
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (79.8% similar)
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (79.3% similar)
- [[2025-09-19/What's the Best Way to Retrieve Slides? A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques_20250919|What's the Best Way to Retrieve Slides? A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Vector Database|Vector Database]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15858v1 Announce Type: cross 
Abstract: In large scale e-commerce marketplaces, duplicate product listings frequently cause consumer confusion and operational inefficiencies, degrading trust on the platform and increasing costs. Traditional keyword-based search methodologies falter in accurately identifying duplicates due to their reliance on exact textual matches, neglecting semantic similarities inherent in product titles. To address these challenges, we introduce a scalable, multimodal product deduplication designed specifically for the e-commerce domain. Our approach employs a domain-specific text model grounded in BERT architecture in conjunction with MaskedAutoEncoders for image representations. Both of these architectures are augmented with dimensionality reduction techniques to produce compact 128-dimensional embeddings without significant information loss. Complementing this, we also developed a novel decider model that leverages both text and image vectors. By integrating these feature extraction mechanisms with Milvus, an optimized vector database, our system can facilitate efficient and high-precision similarity searches across extensive product catalogs exceeding 200 million items with just 100GB of system RAM consumption. Empirical evaluations demonstrate that our matching system achieves a macro-average F1 score of 0.90, outperforming third-party solutions which attain an F1 score of 0.83. Our findings show the potential of combining domain-specific adaptations with state-of-the-art machine learning techniques to mitigate duplicate listings in large-scale e-commerce environments.

## 🔍 Abstract (한글 번역)

arXiv:2509.15858v1 발표 유형: 교차  
요약: 대규모 전자상거래 마켓플레이스에서는 중복된 제품 목록이 소비자 혼란과 운영 비효율성을 자주 초래하여 플랫폼에 대한 신뢰를 저하시키고 비용을 증가시킵니다. 전통적인 키워드 기반 검색 방법론은 정확한 텍스트 일치에 의존하여 제품 제목에 내재된 의미적 유사성을 간과함으로써 중복을 정확하게 식별하는 데 실패합니다. 이러한 문제를 해결하기 위해, 우리는 전자상거래 도메인에 특화된 확장 가능한 다중 모드 제품 중복 제거 방법을 소개합니다. 우리의 접근법은 BERT 아키텍처에 기반한 도메인 특화 텍스트 모델을 MaskedAutoEncoders와 결합하여 이미지 표현을 사용합니다. 이 두 아키텍처는 모두 차원 축소 기법으로 보강되어 정보 손실 없이 128차원의 압축된 임베딩을 생성합니다. 이를 보완하기 위해 텍스트와 이미지 벡터를 모두 활용하는 새로운 결정 모델도 개발했습니다. 이러한 특징 추출 메커니즘을 최적화된 벡터 데이터베이스인 Milvus와 통합함으로써, 우리의 시스템은 2억 개 이상의 제품 카탈로그에 대해 100GB의 시스템 RAM만으로 효율적이고 높은 정밀도의 유사성 검색을 가능하게 합니다. 실증적 평가 결과, 우리의 매칭 시스템은 F1 점수 0.83을 달성한 제3자 솔루션을 능가하여 매크로 평균 F1 점수 0.90을 기록했습니다. 우리의 연구 결과는 대규모 전자상거래 환경에서 중복 목록을 줄이기 위해 도메인 특화 적응과 최첨단 기계 학습 기법을 결합할 가능성을 보여줍니다.

## 📝 요약

대규모 전자상거래 플랫폼에서 중복 상품 목록은 소비자 혼란과 운영 비효율성을 초래합니다. 이를 해결하기 위해, 우리는 전자상거래에 특화된 확장 가능한 멀티모달 중복 제거 시스템을 제안합니다. 이 시스템은 BERT 기반의 텍스트 모델과 MaskedAutoEncoders를 활용한 이미지 표현을 결합하여 128차원의 압축된 임베딩을 생성합니다. 또한, 텍스트와 이미지 벡터를 활용하는 새로운 결정 모델을 개발했습니다. Milvus 벡터 데이터베이스와 통합하여 2억 개 이상의 상품 카탈로그에서 효율적이고 정밀한 유사성 검색을 가능하게 하며, 시스템 RAM은 100GB만 소모합니다. 실험 결과, 우리 시스템은 F1 점수 0.90을 기록하여 기존 솔루션보다 우수한 성능을 보였습니다. 이는 도메인 특화 적응과 최신 기계 학습 기술의 결합이 중복 목록 문제를 해결하는 데 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 대규모 전자상거래 시장에서 중복 상품 등록은 소비자 혼란과 운영 비효율성을 초래하며, 플랫폼 신뢰도 저하와 비용 증가를 유발합니다.
- 2. 기존의 키워드 기반 검색 방법은 정확한 텍스트 일치에 의존하여 제품 제목의 의미적 유사성을 간과함으로써 중복 식별에 실패합니다.
- 3. 본 연구는 BERT 아키텍처에 기반한 도메인 특화 텍스트 모델과 MaskedAutoEncoders를 활용한 이미지 표현을 결합한 확장 가능한 다중 모달 중복 제거 방법을 제안합니다.
- 4. 제안된 시스템은 Milvus 벡터 데이터베이스와 통합되어 2억 개 이상의 제품 카탈로그에서 효율적이고 고정밀 유사성 검색을 가능하게 합니다.
- 5. 실험 결과, 제안된 시스템은 매크로 평균 F1 점수 0.90을 달성하여, F1 점수 0.83을 기록한 타사 솔루션보다 우수한 성능을 보였습니다.


---

*Generated on 2025-09-23 10:53:45*