---
keywords:
  - Triple Query Former
  - Referring Video Object Segmentation
  - Transformer Architecture
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:50:58.082866",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Triple Query Former",
    "Referring Video Object Segmentation",
    "Transformer Architecture"
  ],
  "rejected_keywords": [
    "Motion-aware Aggregation",
    "Multi-Modal Learning"
  ],
  "similarity_scores": {
    "Triple Query Former": 0.85,
    "Referring Video Object Segmentation": 0.8,
    "Transformer Architecture": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Mitigating Query Selection Bias in Referring Video Object Segmentation

**Korean Title:** 쿼리 선택 편향 완화에 관한 비디오 객체 분할 참조

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|Transformer Architecture]]
**⚡ Unique Technical**: [[keywords/Triple Query Former|Triple Query Former]], [[keywords/Referring Video Object Segmentation|Referring Video Object Segmentation]]

## 🔗 유사한 논문
- [[VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (83.8% similar)
- [[Dense Video Understanding with Gated Residual Tokenization_20250917|Dense Video Understanding with Gated Residual Tokenization]] (78.8% similar)
- [[RoboEye_ Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching_20250918|RoboEye Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching]] (78.8% similar)
- [[Chain-of-Thought Re-ranking for Image Retrieval Tasks_20250919|Chain-of-Thought Re-ranking for Image Retrieval Tasks]] (78.7% similar)
- [[MovieCORE_ COgnitive REasoning in Movies_20250919|MovieCORE COgnitive REasoning in Movies]] (78.7% similar)

## 📋 저자 정보

**Authors:** Dingwei Zhang, Dong Zhang, Jinhui Tang

## 📄 Abstract (원문)

Recently, query-based methods have achieved remarkable performance in
Referring Video Object Segmentation (RVOS) by using textual static object
queries to drive cross-modal alignment. However, these static queries are
easily misled by distractors with similar appearance or motion, resulting in
\emph{query selection bias}. To address this issue, we propose Triple Query
Former (TQF), which factorizes the referring query into three specialized
components: an appearance query for static attributes, an intra-frame
interaction query for spatial relations, and an inter-frame motion query for
temporal association. Instead of relying solely on textual embeddings, our
queries are dynamically constructed by integrating both linguistic cues and
visual guidance. Furthermore, we introduce two motion-aware aggregation modules
that enhance object token representations: Intra-frame Interaction Aggregation
incorporates position-aware interactions among objects within a single frame,
while Inter-frame Motion Aggregation leverages trajectory-guided alignment
across frames to ensure temporal coherence. Extensive experiments on multiple
RVOS benchmarks demonstrate the advantages of TQF and the effectiveness of our
structured query design and motion-aware aggregation modules.

## 🔍 Abstract (한글 번역)

최근 질의 기반 방법은 정적 객체 질의를 사용하여 교차 모달 정렬을 유도함으로써 참조 비디오 객체 분할(Referring Video Object Segmentation, RVOS)에서 뛰어난 성능을 달성했습니다. 그러나 이러한 정적 질의는 유사한 외형이나 움직임을 가진 방해 요소에 의해 쉽게 오도되어 \emph{질의 선택 편향}이 발생할 수 있습니다. 이 문제를 해결하기 위해 우리는 Triple Query Former (TQF)를 제안하며, 참조 질의를 세 가지 전문화된 구성 요소로 분해합니다: 정적 속성을 위한 외형 질의, 공간 관계를 위한 프레임 내 상호작용 질의, 그리고 시간적 연관성을 위한 프레임 간 움직임 질의입니다. 우리의 질의는 텍스트 임베딩에만 의존하는 대신, 언어적 단서와 시각적 지침을 통합하여 동적으로 구성됩니다. 또한, 우리는 객체 토큰 표현을 강화하는 두 가지 움직임 인식 집계 모듈을 소개합니다: 프레임 내 상호작용 집계는 단일 프레임 내 객체 간의 위치 인식 상호작용을 통합하고, 프레임 간 움직임 집계는 프레임 간의 경로 안내 정렬을 활용하여 시간적 일관성을 보장합니다. 여러 RVOS 벤치마크에서의 광범위한 실험은 TQF의 장점과 우리의 구조화된 질의 설계 및 움직임 인식 집계 모듈의 효과를 입증합니다.

## 📝 요약

최근 질의 기반 방법이 Referring Video Object Segmentation(RVOS)에서 뛰어난 성과를 보였으나, 정적 객체 질의가 유사한 외형이나 움직임을 가진 방해 요소에 의해 쉽게 혼란을 겪는 문제가 있었습니다. 이를 해결하기 위해, 우리는 Triple Query Former(TQF)를 제안합니다. TQF는 질의를 외형, 공간 관계, 시간적 연관성을 위한 세 가지 구성 요소로 분해하여 사용합니다. 이 질의는 언어적 단서와 시각적 지침을 통합하여 동적으로 구성됩니다. 또한, 우리는 객체 토큰 표현을 강화하는 두 가지 모션 인식 집계 모듈을 도입했습니다. 실험 결과, TQF의 구조적 질의 설계와 모션 인식 집계 모듈이 RVOS 벤치마크에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 최근 질의 기반 방법은 정적 객체 질의를 사용하여 교차 모달 정렬을 수행함으로써 RVOS에서 뛰어난 성능을 보여주고 있습니다.

- 2. 정적 질의는 유사한 외형이나 움직임을 가진 방해 요소에 의해 쉽게 오도되어 질의 선택 편향이 발생할 수 있습니다.

- 3. Triple Query Former (TQF)는 질의를 외형, 공간 관계, 시간적 연관성을 위한 세 가지 구성 요소로 분해하여 질의 선택 편향 문제를 해결합니다.

- 4. TQF는 언어적 단서와 시각적 지침을 결합하여 동적으로 질의를 구성하며, 두 개의 모션 인식 집계 모듈을 도입하여 객체 토큰 표현을 강화합니다.

- 5. 다양한 RVOS 벤치마크에서 TQF의 장점과 구조화된 질의 설계 및 모션 인식 집계 모듈의 효과가 입증되었습니다.

---

*Generated on 2025-09-20 09:38:15*