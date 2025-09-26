---
keywords:
  - Document Image Quality Assessment
  - Optical Character Recognition
  - Feature Fusion Network
  - No-reference DIQA Model
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17012
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:18:23.970797",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Document Image Quality Assessment",
    "Optical Character Recognition",
    "Feature Fusion Network",
    "No-reference DIQA Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Document Image Quality Assessment": 0.8,
    "Optical Character Recognition": 0.85,
    "Feature Fusion Network": 0.78,
    "No-reference DIQA Model": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Document Image Quality Assessment",
        "canonical": "Document Image Quality Assessment",
        "aliases": [
          "DIQA"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task central to the paper, linking to research on image quality in document processing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Optical Character Recognition",
        "canonical": "Optical Character Recognition",
        "aliases": [
          "OCR"
        ],
        "category": "broad_technical",
        "rationale": "OCR is a foundational technology related to document processing, enhancing connectivity with related works.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Feature Fusion Network",
        "canonical": "Feature Fusion Network",
        "aliases": [
          "Feature Fusion"
        ],
        "category": "unique_technical",
        "rationale": "This model is a novel contribution of the paper, relevant for linking to works on feature integration in image processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "No-reference DIQA model",
        "canonical": "No-reference DIQA Model",
        "aliases": [
          "No-reference Model"
        ],
        "category": "unique_technical",
        "rationale": "This specific model is a key innovation in the paper, crucial for linking to similar models in image quality assessment.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Document Image Quality Assessment",
      "resolved_canonical": "Document Image Quality Assessment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Optical Character Recognition",
      "resolved_canonical": "Optical Character Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Feature Fusion Network",
      "resolved_canonical": "Feature Fusion Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "No-reference DIQA model",
      "resolved_canonical": "No-reference DIQA Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# DocIQ: A Benchmark Dataset and Feature Fusion Network for Document Image Quality Assessment

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17012.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17012](https://arxiv.org/abs/2509.17012)

## 🔗 유사한 논문
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (83.9% similar)
- [[2025-09-23/AirQA_ A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation_20250923|AirQA: A Comprehensive QA Dataset for AI Research with Instance-Level Evaluation]] (82.3% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (79.9% similar)
- [[2025-09-22/PRISM_ Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images_20250922|PRISM: Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images]] (79.5% similar)
- [[2025-09-19/QuizRank_ Picking Images by Quizzing VLMs_20250919|QuizRank: Picking Images by Quizzing VLMs]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Optical Character Recognition|Optical Character Recognition]]
**⚡ Unique Technical**: [[keywords/Document Image Quality Assessment|Document Image Quality Assessment]], [[keywords/Feature Fusion Network|Feature Fusion Network]], [[keywords/No-reference DIQA Model|No-reference DIQA Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17012v1 Announce Type: cross 
Abstract: Document image quality assessment (DIQA) is an important component for various applications, including optical character recognition (OCR), document restoration, and the evaluation of document image processing systems. In this paper, we introduce a subjective DIQA dataset DIQA-5000. The DIQA-5000 dataset comprises 5,000 document images, generated by applying multiple document enhancement techniques to 500 real-world images with diverse distortions. Each enhanced image was rated by 15 subjects across three rating dimensions: overall quality, sharpness, and color fidelity. Furthermore, we propose a specialized no-reference DIQA model that exploits document layout features to maintain quality perception at reduced resolutions to lower computational cost. Recognizing that image quality is influenced by both low-level and high-level visual features, we designed a feature fusion module to extract and integrate multi-level features from document images. To generate multi-dimensional scores, our model employs independent quality heads for each dimension to predict score distributions, allowing it to learn distinct aspects of document image quality. Experimental results demonstrate that our method outperforms current state-of-the-art general-purpose IQA models on both DIQA-5000 and an additional document image dataset focused on OCR accuracy.

## 📝 요약

이 논문에서는 문서 이미지 품질 평가(DIQA)를 위한 주관적 데이터셋 DIQA-5000을 소개합니다. DIQA-5000은 다양한 왜곡을 가진 500개의 실제 문서 이미지에 여러 문서 개선 기법을 적용하여 생성된 5,000개의 이미지로 구성되어 있으며, 각 이미지는 15명의 평가자가 전체 품질, 선명도, 색상 충실도 등 세 가지 차원에서 평가했습니다. 또한, 문서 레이아웃 특징을 활용하여 낮은 해상도에서도 품질 인식을 유지하는 비참조 DIQA 모델을 제안합니다. 이 모델은 문서 이미지의 다중 수준 특징을 추출하고 통합하기 위해 특징 융합 모듈을 설계하였으며, 각 차원별로 독립적인 품질 헤드를 사용하여 다차원 점수를 생성합니다. 실험 결과, 제안된 방법은 DIQA-5000과 OCR 정확성에 중점을 둔 추가 데이터셋에서 기존 최첨단 IQA 모델보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. DIQA-5000 데이터셋은 다양한 왜곡을 가진 500개의 실제 문서 이미지에 여러 문서 향상 기법을 적용하여 생성된 5,000개의 문서 이미지로 구성되어 있습니다.
- 2. 각 향상된 이미지는 15명의 평가자가 전체 품질, 선명도, 색 충실도라는 세 가지 평가 기준에 따라 평가되었습니다.
- 3. 제안된 DIQA 모델은 문서 레이아웃 특징을 활용하여 낮은 해상도에서도 품질 인식을 유지하면서 계산 비용을 줄입니다.
- 4. 모델은 독립적인 품질 헤드를 사용하여 각 차원에 대한 점수 분포를 예측함으로써 문서 이미지 품질의 다양한 측면을 학습합니다.
- 5. 실험 결과, 제안된 방법은 DIQA-5000 및 OCR 정확성에 초점을 맞춘 추가 문서 이미지 데이터셋에서 현존하는 최신 IQA 모델보다 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 02:18:23*