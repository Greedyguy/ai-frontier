---
keywords:
  - SFN-YOLO
  - Poultry Detection
  - Scale-aware Fusion
  - M-SCOPE Dataset
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17086
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:45:18.398854",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SFN-YOLO",
    "Poultry Detection",
    "Scale-aware Fusion",
    "M-SCOPE Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "SFN-YOLO": 0.8,
    "Poultry Detection": 0.75,
    "Scale-aware Fusion": 0.78,
    "M-SCOPE Dataset": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SFN-YOLO",
        "canonical": "SFN-YOLO",
        "aliases": [
          "Scale-aware Fusion Networks YOLO"
        ],
        "category": "unique_technical",
        "rationale": "SFN-YOLO is a novel approach specifically designed for poultry detection in complex environments, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "poultry detection",
        "canonical": "Poultry Detection",
        "aliases": [
          "poultry localization"
        ],
        "category": "specific_connectable",
        "rationale": "Poultry detection is a specific application within computer vision, facilitating connections to related research in animal detection.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "scale-aware fusion",
        "canonical": "Scale-aware Fusion",
        "aliases": [
          "multiscale fusion"
        ],
        "category": "specific_connectable",
        "rationale": "Scale-aware fusion addresses multiscale challenges in detection tasks, linking to broader themes in computer vision.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "M-SCOPE",
        "canonical": "M-SCOPE Dataset",
        "aliases": [
          "M-SCOPE"
        ],
        "category": "unique_technical",
        "rationale": "M-SCOPE is a new dataset tailored for free-range poultry detection, offering unique data resources for related studies.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "detection",
      "localization",
      "smart poultry farming",
      "real-time detection"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "SFN-YOLO",
      "resolved_canonical": "SFN-YOLO",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "poultry detection",
      "resolved_canonical": "Poultry Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "scale-aware fusion",
      "resolved_canonical": "Scale-aware Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "M-SCOPE",
      "resolved_canonical": "M-SCOPE Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SFN-YOLO: Towards Free-Range Poultry Detection via Scale-aware Fusion Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17086.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17086](https://arxiv.org/abs/2509.17086)

## 🔗 유사한 논문
- [[2025-09-18/Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (83.3% similar)
- [[2025-09-23/Real-Time Fish Detection in Indonesian Marine Ecosystems Using Lightweight YOLOv10-nano Architecture_20250923|Real-Time Fish Detection in Indonesian Marine Ecosystems Using Lightweight YOLOv10-nano Architecture]] (82.2% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (81.4% similar)
- [[2025-09-18/Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies_20250918|Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies]] (80.6% similar)
- [[2025-09-23/Enhanced Detection of Tiny Objects in Aerial Images_20250923|Enhanced Detection of Tiny Objects in Aerial Images]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Poultry Detection|Poultry Detection]], [[keywords/Scale-aware Fusion|Scale-aware Fusion]]
**⚡ Unique Technical**: [[keywords/SFN-YOLO|SFN-YOLO]], [[keywords/M-SCOPE Dataset|M-SCOPE Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17086v1 Announce Type: new 
Abstract: Detecting and localizing poultry is essential for advancing smart poultry farming. Despite the progress of detection-centric methods, challenges persist in free-range settings due to multiscale targets, obstructions, and complex or dynamic backgrounds. To tackle these challenges, we introduce an innovative poultry detection approach named SFN-YOLO that utilizes scale-aware fusion. This approach combines detailed local features with broader global context to improve detection in intricate environments. Furthermore, we have developed a new expansive dataset (M-SCOPE) tailored for varied free-range conditions. Comprehensive experiments demonstrate our model achieves an mAP of 80.7% with just 7.2M parameters, which is 35.1% fewer than the benchmark, while retaining strong generalization capability across different domains. The efficient and real-time detection capabilities of SFN-YOLO support automated smart poultry farming. The code and dataset can be accessed at https://github.com/chenjessiee/SFN-YOLO.

## 📝 요약

이 논문은 스마트 양계 농업을 위한 가금류 탐지 및 위치 파악을 목표로 합니다. 기존 방법들이 자유 방목 환경에서 다중 규모의 목표물, 장애물, 복잡한 배경 등으로 어려움을 겪는 가운데, 저자들은 SFN-YOLO라는 혁신적인 탐지 방법을 제안합니다. 이 방법은 세부적인 지역적 특징과 넓은 글로벌 문맥을 결합하여 복잡한 환경에서의 탐지 성능을 향상시킵니다. 또한, 다양한 자유 방목 조건에 맞춘 새로운 데이터셋 M-SCOPE를 개발하였습니다. 실험 결과, 제안된 모델은 7.2M 파라미터로 80.7%의 mAP를 달성하며, 이는 기존 벤치마크보다 35.1% 적은 파라미터 수로도 높은 일반화 능력을 유지합니다. SFN-YOLO의 효율적이고 실시간 탐지 능력은 자동화된 스마트 양계 농업을 지원합니다. 코드와 데이터셋은 https://github.com/chenjessiee/SFN-YOLO에서 접근 가능합니다.

## 🎯 주요 포인트

- 1. SFN-YOLO는 스케일 인식 융합을 활용하여 복잡한 환경에서의 가금류 탐지를 개선하는 혁신적인 접근법입니다.
- 2. 이 연구에서는 다양한 방목 조건에 맞춘 새로운 대규모 데이터셋(M-SCOPE)을 개발하였습니다.
- 3. SFN-YOLO 모델은 7.2M 파라미터로 80.7%의 mAP를 달성하며, 벤치마크 대비 35.1% 적은 파라미터를 사용하면서도 강력한 일반화 능력을 유지합니다.
- 4. SFN-YOLO의 효율적이고 실시간 탐지 기능은 자동화된 스마트 가금류 농업을 지원합니다.
- 5. 연구의 코드와 데이터셋은 https://github.com/chenjessiee/SFN-YOLO에서 접근할 수 있습니다.


---

*Generated on 2025-09-24 04:45:18*