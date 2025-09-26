<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:17:28.857705",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Video Object Segmentation",
    "Long-term Memory",
    "Concept-aware Memory",
    "Semi-supervised Video Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Video Object Segmentation": 0.82,
    "Long-term Memory": 0.78,
    "Concept-aware Memory": 0.79,
    "Semi-supervised Video Segmentation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "video object segmentation",
        "canonical": "Video Object Segmentation",
        "aliases": [
          "VOS"
        ],
        "category": "specific_connectable",
        "rationale": "This is a central task in computer vision that connects to various segmentation and tracking techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "long-term memory",
        "canonical": "Long-term Memory",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Long-term memory is crucial for maintaining temporal continuity in video analysis.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "concept-aware memory",
        "canonical": "Concept-aware Memory",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This novel approach enhances semantic understanding in video segmentation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "semi-supervised video segmentation",
        "canonical": "Semi-supervised Video Segmentation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This method bridges supervised and unsupervised learning, relevant for adaptive video processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "MOSEv2",
      "LSVOS Challenge",
      "SAM-2"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "video object segmentation",
      "resolved_canonical": "Video Object Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "long-term memory",
      "resolved_canonical": "Long-term Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "concept-aware memory",
      "resolved_canonical": "Concept-aware Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "semi-supervised video segmentation",
      "resolved_canonical": "Semi-supervised Video Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# The 1st Solution for MOSEv2 Challenge 2025: Long-term and Concept-aware Video Segmentation via SeC

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19183.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19183](https://arxiv.org/abs/2509.19183)

## 🔗 유사한 논문
- [[2025-09-23/SAMSON_ 3rd Place Solution of LSVOS 2025 VOS Challenge_20250923|SAMSON: 3rd Place Solution of LSVOS 2025 VOS Challenge]] (91.0% similar)
- [[2025-09-23/MOSEv2_ A More Challenging Dataset for Video Object Segmentation in Complex Scenes_20250923|MOSEv2: A More Challenging Dataset for Video Object Segmentation in Complex Scenes]] (89.1% similar)
- [[2025-09-22/Enriched Feature Representation and Motion Prediction Module for MOSEv2 Track of 7th LSVOS Challenge_ 3rd Place Solution_20250922|Enriched Feature Representation and Motion Prediction Module for MOSEv2 Track of 7th LSVOS Challenge: 3rd Place Solution]] (89.0% similar)
- [[2025-09-23/The 1st Solution for 7th LSVOS RVOS Track_ SaSaSa2VA_20250923|The 1st Solution for 7th LSVOS RVOS Track: SaSaSa2VA]] (87.0% similar)
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (85.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Video Object Segmentation|Video Object Segmentation]], [[keywords/Semi-supervised Video Segmentation|Semi-supervised Video Segmentation]]
**⚡ Unique Technical**: [[keywords/Long-term Memory|Long-term Memory]], [[keywords/Concept-aware Memory|Concept-aware Memory]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19183v1 Announce Type: new 
Abstract: This technical report explores the MOSEv2 track of the LSVOS Challenge, which targets complex semi-supervised video object segmentation. By analysing and adapting SeC, an enhanced SAM-2 framework, we conduct a detailed study of its long-term memory and concept-aware memory, showing that long-term memory preserves temporal continuity under occlusion and reappearance, while concept-aware memory supplies semantic priors that suppress distractors; together, these traits directly benefit several MOSEv2's core challenges. Our solution achieves a JF score of 39.89% on the test set, ranking 1st in the MOSEv2 track of the LSVOS Challenge.

## 📝 요약

이 기술 보고서는 LSVOS 챌린지의 MOSEv2 트랙을 탐구하며, 복잡한 반지도 비디오 객체 분할을 목표로 합니다. 우리는 SeC, 즉 개선된 SAM-2 프레임워크를 분석하고 적응시켜 장기 메모리와 개념 인식 메모리를 상세히 연구했습니다. 장기 메모리는 가림 및 재출현 상황에서 시간적 연속성을 유지하고, 개념 인식 메모리는 방해 요소를 억제하는 의미적 우선 정보를 제공합니다. 이러한 특성은 MOSEv2의 핵심 과제에 직접적으로 기여합니다. 우리의 솔루션은 테스트 세트에서 JF 점수 39.89%를 기록하며 MOSEv2 트랙에서 1위를 차지했습니다.

## 🎯 주요 포인트

- 1. MOSEv2 트랙은 복잡한 반지도 비디오 객체 분할을 목표로 한다.
- 2. SeC, SAM-2 프레임워크를 분석 및 적응하여 장기 메모리와 개념 인식 메모리를 연구하였다.
- 3. 장기 메모리는 가림 및 재출현 상황에서 시간적 연속성을 유지한다.
- 4. 개념 인식 메모리는 주의를 산만하게 하는 요소를 억제하는 의미적 우선 정보를 제공한다.
- 5. 제안된 솔루션은 LSVOS 챌린지의 MOSEv2 트랙에서 1위를 차지하며, 테스트 세트에서 JF 점수 39.89%를 기록하였다.


---

*Generated on 2025-09-24 16:17:28*