
# Mitigating Query Selection Bias in Referring Video Object Segmentation

**Korean Title:** 비디오 객체 분할을 참조하는 쿼리 선택 편향 완화

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Temporal Association|Temporal Association]] [[keywords/broad/Referring Video Object Segmentation|Referring Video Object Segmentation]] [[keywords/broad/Cross-modal Alignment|Cross-modal Alignment]] [[keywords/specific/Triple Query Former|Triple Query Former]] [[keywords/unique/Intra-frame Interaction Aggregation|Intra-frame Interaction Aggregation]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Motion-aware Aggregation
**🔬 Broad Technical**: Referring Video Object Segmentation, Cross-modal Alignment
**🔗 Specific Connectable**: Triple Query Former
**⭐ Unique Technical**: Intra-frame Interaction Aggregation

**ArXiv ID**: [2509.13722](https://arxiv.org/abs/2509.13722)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13722.pdf)


## 🏷️ 추출된 키워드



`Referring Video Object Segmentation` • 

`Cross-modal Alignment` • 

`Triple Query Former` • 

`Intra-frame Interaction Aggregation` • 

`Motion-aware Aggregation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13722v1 Announce Type: cross 
Abstract: Recently, query-based methods have achieved remarkable performance in Referring Video Object Segmentation (RVOS) by using textual static object queries to drive cross-modal alignment. However, these static queries are easily misled by distractors with similar appearance or motion, resulting in \emph{query selection bias}. To address this issue, we propose Triple Query Former (TQF), which factorizes the referring query into three specialized components: an appearance query for static attributes, an intra-frame interaction query for spatial relations, and an inter-frame motion query for temporal association. Instead of relying solely on textual embeddings, our queries are dynamically constructed by integrating both linguistic cues and visual guidance. Furthermore, we introduce two motion-aware aggregation modules that enhance object token representations: Intra-frame Interaction Aggregation incorporates position-aware interactions among objects within a single frame, while Inter-frame Motion Aggregation leverages trajectory-guided alignment across frames to ensure temporal coherence. Extensive experiments on multiple RVOS benchmarks demonstrate the advantages of TQF and the effectiveness of our structured query design and motion-aware aggregation modules.

## 🔍 Abstract (한글 번역)

arXiv:2509.13722v1 발표 유형: 교차
요약: 최근에는 쿼리 기반 방법이 텍스트 정적 객체 쿼리를 사용하여 교차 모달 정렬을 주도하여 Referring Video Object Segmentation (RVOS)에서 현저한 성능을 달성했습니다. 그러나 이러한 정적 쿼리는 유사한 외모나 움직임을 가진 혼란스러운 요소에 쉽게 오도될 수 있어 \emph{쿼리 선택 편향}을 초래합니다. 이 문제를 해결하기 위해, 우리는 Referring 쿼리를 세 가지 특화된 구성 요소로 분해하는 Triple Query Former (TQF)를 제안합니다: 정적 속성을 위한 외모 쿼리, 공간 관계를 위한 프레임 내 상호 작용 쿼리 및 시간적 연관성을 위한 프레임 간 움직임 쿼리. 우리의 쿼리는 언어적 단서와 시각적 안내를 통합하여 동적으로 구성되어 텍스트 임베딩에만 의존하지 않습니다. 더 나아가, 우리는 두 가지 모션 인식 집계 모듈을 소개하여 객체 토큰 표현을 강화합니다: 프레임 내 상호 작용 집계는 단일 프레임 내 객체 간 위치 인식 상호 작용을 포함하고, 프레임 간 모션 집계는 프레임 간 궤적 안내 정렬을 활용하여 시간적 일관성을 보장합니다. 다양한 RVOS 벤치마크에서 수행된 실험은 TQF의 장점과 구조화된 쿼리 설계 및 모션 인식 집계 모듈의 효과를 입증합니다.

## 📝 요약

최근에는 쿼리 기반 방법이 텍스트 기반 정적 객체 쿼리를 활용하여 교차 모달 정렬을 이끌어내는 Referring Video Object Segmentation (RVOS)에서 높은 성능을 달성했습니다. 그러나 이러한 정적 쿼리는 유사한 외모나 움직임을 가진 혼동요소에 쉽게 오도될 수 있어 \emph{쿼리 선택 편향}을 초래합니다. 이 문제를 해결하기 위해, 우리는 Referring Query를 세 가지 전문화된 구성 요소로 분해하는 Triple Query Former (TQF)을 제안합니다. 우리의 쿼리는 언어적 단서와 시각적 안내를 통합하여 동적으로 구성되며, 텍스트 임베딩에만 의존하는 대신 시각적 안내를 통합합니다. 또한, 우리는 두 가지 모션 인식 집계 모듈을 소개하여 객체 토큰 표현을 강화합니다. Intra-frame Interaction Aggregation은 단일 프레임 내 객체 간 위치 인식 상호작용을 통합하고, Inter-frame Motion Aggregation은 프레임 간 궤적 안내 정렬을 활용하여 시간적 일관성을 보장합니다. 다양한 RVOS 벤치마크 실험을 통해 TQF의 장점과 구조화된 쿼리 설계 및 모션 인식 집계 모듈의 효과를 입증합니다.

## 🎯 주요 포인트


- 1. RVOS에서 텍스트 기반 쿼리 방법은 텍스트 정적 객체 쿼리를 사용하여 높은 성능을 보이고 있지만, 쿼리 선택 편향 문제가 발생한다.

- 2. TQF는 세 가지 전문화된 구성 요소로 참조 쿼리를 분해하여 쿼리 선택 편향 문제를 해결한다.

- 3. TQF는 언어적 단서와 시각적 안내를 통합하여 동적으로 구성된 쿼리를 사용하며, 두 개의 모션 인식 집계 모듈을 소개한다.


---

*Generated on 2025-09-18 16:22:24*