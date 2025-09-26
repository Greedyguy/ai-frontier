<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:17:14.128549",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "YOLO-LAN",
    "Deep Learning",
    "Colorectal Cancer",
    "Polyp Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "YOLO-LAN": 0.8,
    "Deep Learning": 0.85,
    "Colorectal Cancer": 0.7,
    "Polyp Detection": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "YOLO-LAN",
        "canonical": "YOLO-LAN",
        "aliases": [
          "YOLO-based polyp detection"
        ],
        "category": "unique_technical",
        "rationale": "YOLO-LAN is a novel and specific polyp detection pipeline, offering unique insights into AI-assisted colorectal screening.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology for the proposed detection pipeline, linking to a wide range of AI research.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Colorectal cancer",
        "canonical": "Colorectal Cancer",
        "aliases": [
          "CRC"
        ],
        "category": "specific_connectable",
        "rationale": "Colorectal cancer is the primary medical context for the research, connecting to related medical and AI studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Polyp Detection",
        "canonical": "Polyp Detection",
        "aliases": [
          "Polyp Identification"
        ],
        "category": "specific_connectable",
        "rationale": "Polyp detection is the core application of the study, relevant to medical imaging and AI diagnostics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "colonoscopy",
      "tumors",
      "lesions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "YOLO-LAN",
      "resolved_canonical": "YOLO-LAN",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Colorectal cancer",
      "resolved_canonical": "Colorectal Cancer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Polyp Detection",
      "resolved_canonical": "Polyp Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# YOLO-LAN: Precise Polyp Detection via Optimized Loss, Augmentations and Negatives

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19166.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19166](https://arxiv.org/abs/2509.19166)

## 🔗 유사한 논문
- [[2025-09-23/Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images_20250923|Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images]] (87.5% similar)
- [[2025-09-24/PolypSeg-GradCAM_ Towards Explainable Computer-Aided Gastrointestinal Disease Detection Using U-Net Based Segmentation and Grad-CAM Visualization on the Kvasir Dataset_20250924|PolypSeg-GradCAM: Towards Explainable Computer-Aided Gastrointestinal Disease Detection Using U-Net Based Segmentation and Grad-CAM Visualization on the Kvasir Dataset]] (87.3% similar)
- [[2025-09-23/MS-YOLO_ A Multi-Scale Model for Accurate and Efficient Blood Cell Detection_20250923|MS-YOLO: A Multi-Scale Model for Accurate and Efficient Blood Cell Detection]] (85.4% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (85.0% similar)
- [[2025-09-24/Generative data augmentation for biliary tract detection on intraoperative images_20250924|Generative data augmentation for biliary tract detection on intraoperative images]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Colorectal Cancer|Colorectal Cancer]], [[keywords/Polyp Detection|Polyp Detection]]
**⚡ Unique Technical**: [[keywords/YOLO-LAN|YOLO-LAN]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19166v1 Announce Type: new 
Abstract: Colorectal cancer (CRC), a lethal disease, begins with the growth of abnormal mucosal cell proliferation called polyps in the inner wall of the colon. When left undetected, polyps can become malignant tumors. Colonoscopy is the standard procedure for detecting polyps, as it enables direct visualization and removal of suspicious lesions. Manual detection by colonoscopy can be inconsistent and is subject to oversight. Therefore, object detection based on deep learning offers a better solution for a more accurate and real-time diagnosis during colonoscopy. In this work, we propose YOLO-LAN, a YOLO-based polyp detection pipeline, trained using M2IoU loss, versatile data augmentations and negative data to replicate real clinical situations. Our pipeline outperformed existing methods for the Kvasir-seg and BKAI-IGH NeoPolyp datasets, achieving mAP$_{50}$ of 0.9619, mAP$_{50:95}$ of 0.8599 with YOLOv12 and mAP$_{50}$ of 0.9540, mAP$_{50:95}$ of 0.8487 with YOLOv8 on the Kvasir-seg dataset. The significant increase is achieved in mAP$_{50:95}$ score, showing the precision of polyp detection. We show robustness based on polyp size and precise location detection, making it clinically relevant in AI-assisted colorectal screening.

## 📝 요약

이 논문은 대장암 진단에서 용종을 정확하게 탐지하기 위한 YOLO-LAN이라는 딥러닝 기반의 객체 탐지 파이프라인을 제안합니다. 제안된 방법은 M2IoU 손실 함수와 다양한 데이터 증강 기법을 사용하여 실제 임상 상황을 모방하며, Kvasir-seg 및 BKAI-IGH NeoPolyp 데이터셋에서 기존 방법보다 우수한 성능을 보였습니다. 특히, Kvasir-seg 데이터셋에서 mAP$_{50:95}$ 점수가 크게 향상되어 용종 탐지의 정확성을 입증했습니다. 이 연구는 AI를 활용한 대장암 스크리닝에서 임상적으로 유의미한 기여를 합니다.

## 🎯 주요 포인트

- 1. 대장암은 대장 내벽의 폴립으로 시작되며, 조기 발견되지 않으면 악성 종양으로 발전할 수 있습니다.
- 2. 기존의 내시경 검사는 폴립을 직접 시각화하고 제거할 수 있지만, 수동 검출의 일관성이 부족하고 간과될 수 있습니다.
- 3. 본 연구에서는 YOLO-LAN이라는 YOLO 기반의 폴립 검출 파이프라인을 제안하여, M2IoU 손실, 다양한 데이터 증강 및 음성 데이터를 사용하여 실제 임상 상황을 재현했습니다.
- 4. 제안된 파이프라인은 Kvasir-seg 및 BKAI-IGH NeoPolyp 데이터셋에서 기존 방법을 능가하며, 높은 mAP$_{50:95}$ 점수를 기록하여 폴립 검출의 정밀성을 입증했습니다.
- 5. 폴립 크기와 정확한 위치 검출에 대한 강건성을 보여, AI 기반 대장암 검진에서 임상적으로 유의미한 결과를 제공합니다.


---

*Generated on 2025-09-24 16:17:14*