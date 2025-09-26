<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:58:45.572723",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Motion Vector Propagation",
    "Open-Vocabulary Detection",
    "Compressed-Domain Propagation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.82,
    "Motion Vector Propagation": 0.7,
    "Open-Vocabulary Detection": 0.79,
    "Compressed-Domain Propagation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot Video Object Detection",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Detection"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader concept of zero-shot learning, which is a trending topic and relevant to the paper's focus on label-free detection.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Motion Vector Propagation",
        "canonical": "Motion Vector Propagation",
        "aliases": [
          "MV Propagation"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method specific to this paper, enhancing the understanding of the proposed technique.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Open-Vocabulary Detector",
        "canonical": "Open-Vocabulary Detection",
        "aliases": [
          "Open-Vocab Detector"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of open-vocabulary models, which are increasingly relevant in machine learning research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "Compressed-Domain Propagation",
        "canonical": "Compressed-Domain Propagation",
        "aliases": [
          "Compressed Propagation"
        ],
        "category": "unique_technical",
        "rationale": "Describes a specific propagation technique that is central to the paper's contribution.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-Shot Video Object Detection",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Motion Vector Propagation",
      "resolved_canonical": "Motion Vector Propagation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Open-Vocabulary Detector",
      "resolved_canonical": "Open-Vocabulary Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Compressed-Domain Propagation",
      "resolved_canonical": "Compressed-Domain Propagation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MVP: Motion Vector Propagation for Zero-Shot Video Object Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18388.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18388](https://arxiv.org/abs/2509.18388)

## 🔗 유사한 논문
- [[2025-09-23/MoCLIP-Lite_ Efficient Video Recognition by Fusing CLIP with Motion Vectors_20250923|MoCLIP-Lite: Efficient Video Recognition by Fusing CLIP with Motion Vectors]] (84.8% similar)
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (83.4% similar)
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (82.7% similar)
- [[2025-09-24/No Labels Needed_ Zero-Shot Image Classification with Collaborative Self-Learning_20250924|No Labels Needed: Zero-Shot Image Classification with Collaborative Self-Learning]] (82.2% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Open-Vocabulary Detection|Open-Vocabulary Detection]]
**⚡ Unique Technical**: [[keywords/Motion Vector Propagation|Motion Vector Propagation]], [[keywords/Compressed-Domain Propagation|Compressed-Domain Propagation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18388v1 Announce Type: new 
Abstract: Running a large open-vocabulary (Open-vocab) detector on every video frame is accurate but expensive. We introduce a training-free pipeline that invokes OWLv2 only on fixed-interval keyframes and propagates detections to intermediate frames using compressed-domain motion vectors (MV). A simple 3x3 grid aggregation of motion vectors provides translation and uniform-scale updates, augmented with an area-growth check and an optional single-class switch. The method requires no labels, no fine-tuning, and uses the same prompt list for all open-vocabulary methods. On ILSVRC2015-VID (validation dataset), our approach (MVP) attains mAP@0.5=0.609 and mAP@[0.5:0.95]=0.316. At loose intersection-over-union (IoU) thresholds it remains close to framewise OWLv2-Large (0.747/0.721 at 0.2/0.3 versus 0.784/0.780), reflecting that coarse localization is largely preserved. Under the same keyframe schedule, MVP outperforms tracker-based propagation (MOSSE, KCF, CSRT) at mAP@0.5. A supervised reference (YOLOv12x) reaches 0.631 at mAP@0.5 but requires labeled training, whereas our method remains label-free and open-vocabulary. These results indicate that compressed-domain propagation is a practical way to reduce detector invocations while keeping strong zero-shot coverage in videos. Our code and models are available at https://github.com/microa/MVP.

## 📝 요약

이 논문은 비디오 프레임마다 대규모 개방형 어휘(Open-vocab) 검출기를 실행하는 대신, OWLv2를 고정 간격의 키프레임에서만 호출하고, 압축 도메인의 모션 벡터를 사용해 중간 프레임으로 검출 결과를 전파하는 훈련이 필요 없는 파이프라인을 제안합니다. 이 방법은 레이블이나 파인튜닝이 필요 없으며, 모든 개방형 어휘 방법에 동일한 프롬프트 리스트를 사용합니다. ILSVRC2015-VID 데이터셋에서 mAP@0.5=0.609, mAP@[0.5:0.95]=0.316의 성능을 보였으며, 키프레임 일정 하에서 기존 추적기 기반 전파 방법보다 우수한 성능을 나타냈습니다. 이 방법은 레이블이 필요 없는 상태에서 강력한 제로샷 커버리지를 유지하면서 검출기 호출을 줄이는 실용적인 방법임을 보여줍니다.

## 🎯 주요 포인트

- 1. 대규모 오픈 보캐뷸러리(Open-vocab) 탐지기를 모든 비디오 프레임에서 실행하는 것은 정확하지만 비용이 많이 듭니다.
- 2. OWLv2를 고정 간격의 키프레임에서만 호출하고, 압축 도메인 모션 벡터(MV)를 사용하여 중간 프레임으로 탐지를 전파하는 훈련이 필요 없는 파이프라인을 소개합니다.
- 3. 제안된 방법은 라벨이나 파인튜닝이 필요 없으며, 모든 오픈 보캐뷸러리 방법에 동일한 프롬프트 리스트를 사용합니다.
- 4. ILSVRC2015-VID 검증 데이터셋에서 제안된 방법(MVP)은 mAP@0.5=0.609와 mAP@[0.5:0.95]=0.316의 성능을 보이며, 프레임 단위 OWLv2-Large와 유사한 성능을 유지합니다.
- 5. 제안된 방법은 라벨이 필요 없는 오픈 보캐뷸러리 방식으로, 비디오에서 탐지기 호출을 줄이면서도 강력한 제로샷 커버리지를 유지하는 실용적인 방법입니다.


---

*Generated on 2025-09-24 15:58:45*