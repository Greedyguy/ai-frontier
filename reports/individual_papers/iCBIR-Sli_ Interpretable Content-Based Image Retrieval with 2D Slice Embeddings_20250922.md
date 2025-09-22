# iCBIR-Sli: Interpretable Content-Based Image Retrieval with 2D Slice Embeddings

**Korean Title:** iCBIR-Sli: 2D 슬라이스 임베딩을 활용한 해석 가능한 콘텐츠 기반 이미지 검색

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Interpretable CBIR|Interpretable CBIR]] [[keywords/specific/2D Slice Embedding|2D Slice Embedding]] [[keywords/broad/Content-Based Image Retrieval|Content-Based Image Retrieval]] [[keywords/broad/Machine Learning|Machine Learning]] [[keywords/unique/iCBIR-Sli|iCBIR-Sli]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Domain-invariant feature learning in brain MR imaging for content-based image retrieval_20250922|Domain-invariant feature learning in brain MR imaging for content-based image retrieval]] (83.8% similar) [[2025-09-22/RegionMed-CLIP_ A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding_20250922|RegionMed-CLIP: A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding]] (80.5% similar) [[2025-09-19/What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques_20250919|What's the Best Way to Retrieve Slides? A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretable CBIR
**🔗 Specific Connectable**: 2D Slice Embeddings
**🔬 Broad Technical**: Content-Based Image Retrieval, Machine Learning
**⭐ Unique Technical**: iCBIR-Sli
## 🔗 유사한 논문
- [[2025-09-22/Domain-invariant feature learning in brain MR imaging for content-based image retrieval_20250922|Domain-invariant feature learning in brain MR imaging for content-based image retrieval]] (83.8% similar)
- [[2025-09-22/RegionMed-CLIP_ A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding_20250922|RegionMed-CLIP A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding]] (80.5% similar)
- [[2025-09-19/What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques_20250919|What's the Best Way to Retrieve Slides A Comparative Study of Multimodal, Caption-Based, and Hybrid Retrieval Techniques]] (80.0% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (79.8% similar)
- [[2025-09-19/Chain-of-Thought Re-ranking for Image Retrieval Tasks_20250919|Chain-of-Thought Re-ranking for Image Retrieval Tasks]] (79.6% similar)


**ArXiv ID**: [2501.01642](https://arxiv.org/abs/2501.01642)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2501.01642.pdf)


**ArXiv ID**: [2501.01642](https://arxiv.org/abs/2501.01642)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2501.01642.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretable CBIR
**🔗 Specific Connectable**: 2D Slice Embeddings
**⭐ Unique Technical**: iCBIR-Sli
**🔬 Broad Technical**: Content-Based Image Retrieval, Machine Learning

## 🏷️ 추출된 키워드



`Content-Based Image Retrieval` • 

`Machine Learning` • 

`2D Slice Embedding` • 

`iCBIR-Sli` • 

`Interpretable CBIR`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.01642v2 Announce Type: replace-cross 
Abstract: Current methods for searching brain MR images rely on text-based approaches, highlighting a significant need for content-based image retrieval (CBIR) systems. Directly applying 3D brain MR images to machine learning models offers the benefit of effectively learning the brain's structure; however, building the generalized model necessitates a large amount of training data. While models that consider depth direction and utilize continuous 2D slices have demonstrated success in segmentation and classification tasks involving 3D data, concerns remain. Specifically, using general 2D slices may lead to the oversight of pathological features and discontinuities in depth direction information. Furthermore, to the best of the authors' knowledge, there have been no attempts to develop a practical CBIR system that preserves the entire brain's structural information. In this study, we propose an interpretable CBIR method for brain MR images, named iCBIR-Sli (Interpretable CBIR with 2D Slice Embedding), which, for the first time globally, utilizes a series of 2D slices. iCBIR-Sli addresses the challenges associated with using 2D slices by effectively aggregating slice information, thereby achieving low-dimensional representations with high completeness, usability, robustness, and interoperability, which are qualities essential for effective CBIR. In retrieval evaluation experiments utilizing five publicly available brain MR datasets (ADNI2/3, OASIS3/4, AIBL) for Alzheimer's disease and cognitively normal, iCBIR-Sli demonstrated top-1 retrieval performance (macro F1 = 0.859), comparable to existing deep learning models explicitly designed for classification, without the need for an external classifier. Additionally, the method provided high interpretability by clearly identifying the brain regions indicative of the searched-for disease.

## 🔍 Abstract (한글 번역)

arXiv:2501.01642v2 발표 유형: 교체-크로스  
초록: 현재 뇌 MR 이미지를 검색하는 방법은 텍스트 기반 접근 방식에 의존하고 있으며, 이는 콘텐츠 기반 이미지 검색(CBIR) 시스템의 필요성을 강조합니다. 3D 뇌 MR 이미지를 기계 학습 모델에 직접 적용하면 뇌 구조를 효과적으로 학습할 수 있는 이점이 있지만, 일반화된 모델을 구축하려면 대량의 훈련 데이터가 필요합니다. 깊이 방향을 고려하고 연속적인 2D 슬라이스를 활용하는 모델은 3D 데이터와 관련된 분할 및 분류 작업에서 성공을 거두었지만, 여전히 우려가 남아 있습니다. 특히 일반적인 2D 슬라이스를 사용할 경우 병리학적 특징과 깊이 방향 정보의 불연속성을 간과할 수 있습니다. 또한, 저자들이 아는 한, 전체 뇌 구조 정보를 보존하는 실용적인 CBIR 시스템을 개발하려는 시도는 없었습니다. 본 연구에서는 iCBIR-Sli(2D 슬라이스 임베딩을 통한 해석 가능한 CBIR)라는 뇌 MR 이미지를 위한 해석 가능한 CBIR 방법을 제안합니다. 이는 전 세계적으로 처음으로 일련의 2D 슬라이스를 활용합니다. iCBIR-Sli는 슬라이스 정보를 효과적으로 집계하여 2D 슬라이스 사용과 관련된 문제를 해결하며, 효과적인 CBIR에 필수적인 높은 완전성, 사용성, 견고성 및 상호운용성을 갖춘 저차원 표현을 달성합니다. 알츠하이머병 및 인지적으로 정상인에 대한 다섯 개의 공개 뇌 MR 데이터셋(ADNI2/3, OASIS3/4, AIBL)을 활용한 검색 평가 실험에서 iCBIR-Sli는 외부 분류기가 필요 없이 분류를 위해 명시적으로 설계된 기존의 딥러닝 모델과 비교하여 유사한 top-1 검색 성능(매크로 F1 = 0.859)을 보여주었습니다. 또한, 이 방법은 검색된 질병을 나타내는 뇌 영역을 명확히 식별함으로써 높은 해석 가능성을 제공했습니다.

## 📝 요약

이 논문은 뇌 MR 이미지를 검색하는 기존의 텍스트 기반 방법의 한계를 극복하기 위해 새로운 콘텐츠 기반 이미지 검색(CBIR) 시스템을 제안합니다. 제안된 방법인 iCBIR-Sli는 2D 슬라이스 임베딩을 활용하여 뇌의 구조적 정보를 보존하면서도 해석 가능한 CBIR을 구현합니다. 이 방법은 2D 슬라이스 정보를 효과적으로 통합하여 저차원 표현을 생성하고, 이는 높은 완전성, 사용성, 견고성 및 상호운용성을 제공합니다. 알츠하이머병 및 정상 인지 상태를 포함한 5개의 공개 뇌 MR 데이터셋을 활용한 검색 평가 실험에서 iCBIR-Sli는 기존의 분류 모델과 유사한 성능(macro F1 = 0.859)을 보였으며, 외부 분류기가 필요하지 않았습니다. 또한, 검색 대상 질병을 나타내는 뇌 영역을 명확히 식별하여 높은 해석 가능성을 제공합니다.

## 🎯 주요 포인트


- 1. 현재의 뇌 MR 이미지 검색 방법은 텍스트 기반 접근에 의존하며, 콘텐츠 기반 이미지 검색(CBIR) 시스템의 필요성이 강조되고 있다.

- 2. 3D 뇌 MR 이미지를 머신러닝 모델에 직접 적용하면 뇌 구조를 효과적으로 학습할 수 있지만, 일반화된 모델 구축에는 많은 양의 훈련 데이터가 필요하다.

- 3. 일반적인 2D 슬라이스를 사용할 경우 병리학적 특징과 깊이 방향 정보의 불연속성을 간과할 수 있다.

- 4. iCBIR-Sli는 2D 슬라이스를 활용하여 뇌 MR 이미지의 구조적 정보를 보존하는 해석 가능한 CBIR 방법을 제안하며, 낮은 차원의 표현을 통해 높은 완전성, 사용성, 견고성 및 상호 운용성을 달성한다.

- 5. iCBIR-Sli는 알츠하이머병 및 인지적으로 정상인 상태를 대상으로 한 검색 평가 실험에서 기존의 분류용 딥러닝 모델과 유사한 성능을 보였으며, 외부 분류기가 필요하지 않다.


---

*Generated on 2025-09-22 16:09:38*