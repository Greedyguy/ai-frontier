<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:31:31.509972",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Anomaly Detection",
    "Additive Manufacturing",
    "Surface Defect Detection",
    "Depth Sensors"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Anomaly Detection": 0.8,
    "Additive Manufacturing": 0.85,
    "Surface Defect Detection": 0.78,
    "Depth Sensors": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Anomaly Detection",
        "canonical": "3D Anomaly Detection",
        "aliases": [
          "3D-ADAM"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel dataset specifically designed for 3D anomaly detection in additive manufacturing, offering unique insights.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Additive Manufacturing",
        "canonical": "Additive Manufacturing",
        "aliases": [
          "3D Printing"
        ],
        "category": "broad_technical",
        "rationale": "Additive manufacturing is a key domain for the dataset, providing context for its application and relevance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "RGB+3D Surface Defect Detection",
        "canonical": "Surface Defect Detection",
        "aliases": [
          "RGB+3D Defect Detection"
        ],
        "category": "specific_connectable",
        "rationale": "This term connects to the specific technical challenge the dataset addresses, enhancing link potential.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Industrial Depth Sensors",
        "canonical": "Depth Sensors",
        "aliases": [
          "Industrial Sensors"
        ],
        "category": "specific_connectable",
        "rationale": "Depth sensors are critical for capturing the dataset, linking to sensor technology in manufacturing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "benchmark",
      "real-world deployment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Anomaly Detection",
      "resolved_canonical": "3D Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Additive Manufacturing",
      "resolved_canonical": "Additive Manufacturing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "RGB+3D Surface Defect Detection",
      "resolved_canonical": "Surface Defect Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Industrial Depth Sensors",
      "resolved_canonical": "Depth Sensors",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# 3D-ADAM: A Dataset for 3D Anomaly Detection in Additive Manufacturing

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2507.07838.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2507.07838](https://arxiv.org/abs/2507.07838)

## 🔗 유사한 논문
- [[2025-09-22/ISP-AD_ A Large-Scale Real-World Dataset for Advancing Industrial Anomaly Detection with Synthetic and Real Defects_20250922|ISP-AD: A Large-Scale Real-World Dataset for Advancing Industrial Anomaly Detection with Synthetic and Real Defects]] (86.0% similar)
- [[2025-09-24/RS3DBench_ A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing_20250924|RS3DBench: A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing]] (81.1% similar)
- [[2025-09-24/Advancing Metallic Surface Defect Detection via Anomaly-Guided Pretraining on a Large Industrial Dataset_20250924|Advancing Metallic Surface Defect Detection via Anomaly-Guided Pretraining on a Large Industrial Dataset]] (80.7% similar)
- [[2025-09-18/AD-DINOv3_ Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration_20250918|AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (80.2% similar)
- [[2025-09-24/HDM_ Hybrid Diffusion Model for Unified Image Anomaly Detection_20250924|HDM: Hybrid Diffusion Model for Unified Image Anomaly Detection]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Additive Manufacturing|Additive Manufacturing]]
**🔗 Specific Connectable**: [[keywords/Surface Defect Detection|Surface Defect Detection]], [[keywords/Depth Sensors|Depth Sensors]]
**⚡ Unique Technical**: [[keywords/3D Anomaly Detection|3D Anomaly Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.07838v2 Announce Type: replace 
Abstract: Surface defects are a primary source of yield loss in manufacturing, yet existing anomaly detection methods often fail in real-world deployment due to limited and unrepresentative datasets. To overcome this, we introduce 3D-ADAM, a 3D Anomaly Detection in Additive Manufacturing dataset, that is the first large-scale, industry-relevant dataset for RGB+3D surface defect detection in additive manufacturing. 3D-ADAM comprises 14,120 high-resolution scans of 217 unique parts, captured with four industrial depth sensors, and includes 27,346 annotated defects across 12 categories along with 27,346 annotations of machine element features in 16 classes. 3D-ADAM is captured in a real industrial environment and as such reflects real production conditions, including variations in part placement, sensor positioning, lighting, and partial occlusion. Benchmarking state-of-the-art models demonstrates that 3D-ADAM presents substantial challenges beyond existing datasets. Validation through expert labelling surveys with industry partners further confirms its industrial relevance. By providing this benchmark, 3D-ADAM establishes a foundation for advancing robust 3D anomaly detection capable of meeting manufacturing demands.

## 📝 요약

3D-ADAM은 적층 제조에서 표면 결함을 감지하기 위한 최초의 대규모 데이터셋으로, 실제 산업 환경에서 수집된 14,120개의 고해상도 스캔과 27,346개의 결함 주석을 포함합니다. 이 데이터셋은 기존의 데이터셋보다 더 복잡한 문제를 제시하며, 전문가 검증을 통해 산업적 관련성을 확인했습니다. 3D-ADAM은 제조 요구를 충족할 수 있는 강력한 3D 이상 탐지 기술 발전의 기초를 제공합니다.

## 🎯 주요 포인트

- 1. 3D-ADAM은 적층 제조에서 RGB+3D 표면 결함 탐지를 위한 최초의 대규모 산업 관련 데이터셋입니다.
- 2. 3D-ADAM 데이터셋은 217개의 고유 부품에 대한 14,120개의 고해상도 스캔과 12개 카테고리의 27,346개의 결함 주석을 포함합니다.
- 3. 이 데이터셋은 실제 산업 환경에서 캡처되어 부품 배치, 센서 위치, 조명, 부분적인 가림 등의 변화를 반영합니다.
- 4. 최신 모델의 벤치마킹 결과, 3D-ADAM은 기존 데이터셋을 넘어서는 상당한 도전 과제를 제시합니다.
- 5. 산업 파트너와의 전문가 라벨링 설문조사를 통해 3D-ADAM의 산업적 관련성이 확인되었습니다.


---

*Generated on 2025-09-24 16:31:31*