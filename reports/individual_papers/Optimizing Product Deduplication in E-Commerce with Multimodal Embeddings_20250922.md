# Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings

**Korean Title:** 전자 상거래에서 다중 모달 임베딩을 활용한 제품 중복 제거 최적화

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Multimodal Embeddings|Multimodal Embeddings]] [[keywords/specific/Dimensionality Reduction|Dimensionality Reduction]] [[keywords/broad/Natural Language Processing|Natural Language Processing]] [[keywords/broad/Computer Vision|Computer Vision]] [[keywords/unique/MaskedAutoEncoders|MaskedAutoEncoders]] [[categories/cs.LG|cs.LG]] [[2025-09-18/RoboEye_ Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching_20250918|RoboEye: Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching]] (82.1% similar) [[2025-09-19/PRISM_ Product Retrieval In Shopping Carts using Hybrid Matching_20250919|PRISM: Product Retrieval In Shopping Carts using Hybrid Matching]] (82.0% similar) [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Multimodal Embeddings, Dimensionality Reduction
**🔬 Broad Technical**: Natural Language Processing, Computer Vision
**⭐ Unique Technical**: MaskedAutoEncoders
## 🔗 유사한 논문
- [[2025-09-18/RoboEye_ Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching_20250918|RoboEye Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching]] (82.1% similar)
- [[2025-09-19/PRISM_ Product Retrieval In Shopping Carts using Hybrid Matching_20250919|PRISM Product Retrieval In Shopping Carts using Hybrid Matching]] (82.0% similar)
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (79.3% similar)
- [[2025-09-19/What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques_20250919|What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques]] (79.2% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility Process-Supervised Rewrite for RAG]] (79.1% similar)


**ArXiv ID**: [2509.15858](https://arxiv.org/abs/2509.15858)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15858.pdf)


**ArXiv ID**: [2509.15858](https://arxiv.org/abs/2509.15858)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15858.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Multimodal Embeddings, Dimensionality Reduction
**⭐ Unique Technical**: MaskedAutoEncoders
**🔬 Broad Technical**: Natural Language Processing, Computer Vision

## 🏷️ 추출된 키워드



`Natural Language Processing` • 

`Computer Vision` • 

`Multimodal Embeddings` • 

`Dimensionality Reduction` • 

`MaskedAutoEncoders`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15858v1 Announce Type: cross 
Abstract: In large scale e-commerce marketplaces, duplicate product listings frequently cause consumer confusion and operational inefficiencies, degrading trust on the platform and increasing costs. Traditional keyword-based search methodologies falter in accurately identifying duplicates due to their reliance on exact textual matches, neglecting semantic similarities inherent in product titles. To address these challenges, we introduce a scalable, multimodal product deduplication designed specifically for the e-commerce domain. Our approach employs a domain-specific text model grounded in BERT architecture in conjunction with MaskedAutoEncoders for image representations. Both of these architectures are augmented with dimensionality reduction techniques to produce compact 128-dimensional embeddings without significant information loss. Complementing this, we also developed a novel decider model that leverages both text and image vectors. By integrating these feature extraction mechanisms with Milvus, an optimized vector database, our system can facilitate efficient and high-precision similarity searches across extensive product catalogs exceeding 200 million items with just 100GB of system RAM consumption. Empirical evaluations demonstrate that our matching system achieves a macro-average F1 score of 0.90, outperforming third-party solutions which attain an F1 score of 0.83. Our findings show the potential of combining domain-specific adaptations with state-of-the-art machine learning techniques to mitigate duplicate listings in large-scale e-commerce environments.

## 🔍 Abstract (한글 번역)

arXiv:2509.15858v1 발표 유형: 교차  
초록: 대규모 전자상거래 마켓플레이스에서는 중복된 상품 목록이 소비자에게 혼란을 주고 운영상의 비효율성을 초래하여 플랫폼에 대한 신뢰를 저하시킴과 동시에 비용을 증가시킵니다. 전통적인 키워드 기반 검색 방법론은 정확한 텍스트 일치에 의존하여 제품 제목에 내재된 의미적 유사성을 간과함으로써 중복을 정확하게 식별하는 데 실패합니다. 이러한 문제를 해결하기 위해, 우리는 전자상거래 도메인에 특화된 확장 가능한 멀티모달 제품 중복 제거 방법을 소개합니다. 우리의 접근 방식은 BERT 아키텍처에 기반한 도메인 특화 텍스트 모델과 이미지 표현을 위한 MaskedAutoEncoders를 결합하여 사용합니다. 이 두 아키텍처 모두 차원 축소 기법으로 보강되어 정보 손실 없이 128차원의 컴팩트한 임베딩을 생성합니다. 이를 보완하기 위해, 우리는 텍스트와 이미지 벡터를 모두 활용하는 새로운 결정 모델도 개발했습니다. 이러한 특징 추출 메커니즘을 최적화된 벡터 데이터베이스인 Milvus와 통합함으로써, 우리의 시스템은 2억 개 이상의 상품 카탈로그에 대해 100GB의 시스템 RAM만으로도 효율적이고 높은 정밀도의 유사성 검색을 수행할 수 있습니다. 실증적 평가 결과, 우리의 매칭 시스템은 매크로 평균 F1 점수 0.90을 달성하여 F1 점수 0.83을 기록한 타사 솔루션을 능가함을 보여줍니다. 우리의 연구 결과는 대규모 전자상거래 환경에서 중복 목록을 완화하기 위해 도메인 특화 적응과 최첨단 기계 학습 기법을 결합할 가능성을 보여줍니다.

## 📝 요약

이 논문은 대규모 전자상거래 플랫폼에서 중복 상품 목록 문제를 해결하기 위한 확장 가능한 멀티모달 중복 제거 시스템을 제안합니다. 기존의 키워드 기반 검색 방법은 정확한 텍스트 일치에 의존하여 중복 식별에 한계가 있습니다. 이를 극복하기 위해 BERT 기반의 도메인 특화 텍스트 모델과 이미지 표현을 위한 MaskedAutoEncoders를 사용하여 128차원 임베딩을 생성합니다. 이 시스템은 Milvus 벡터 데이터베이스와 결합하여 2억 개 이상의 상품 목록에서 효율적이고 정밀한 유사성 검색을 가능하게 하며, 100GB의 RAM만으로 작동합니다. 실험 결과, 제안된 시스템은 F1 점수 0.90을 기록하며, 기존 솔루션보다 우수한 성능을 보였습니다. 이 연구는 도메인 특화 적응과 최신 기계 학습 기법의 결합이 대규모 전자상거래 환경에서 중복 목록 문제를 완화할 수 있음을 보여줍니다.

## 🎯 주요 포인트


- 1. 대규모 전자상거래 시장에서 중복 상품 등록은 소비자 혼란과 운영 비효율성을 초래하며, 플랫폼 신뢰도를 저하시킨다.

- 2. 기존의 키워드 기반 검색 방법은 정확한 텍스트 일치에 의존하여 중복 상품 식별에 한계를 보인다.

- 3. 본 연구는 BERT 아키텍처 기반의 텍스트 모델과 MaskedAutoEncoders를 활용한 이미지 표현을 결합한 확장 가능한 다중 모달 상품 중복 제거 방법을 제안한다.

- 4. 제안된 시스템은 200백만 개 이상의 상품 목록에서 효율적이고 높은 정밀도의 유사성 검색을 가능하게 하며, 100GB의 시스템 RAM만을 소비한다.

- 5. 제안된 매칭 시스템은 매크로 평균 F1 점수 0.90을 달성하여, F1 점수 0.83을 기록한 타사 솔루션보다 우수한 성능을 보인다.


---

*Generated on 2025-09-22 15:43:33*