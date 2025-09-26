---
keywords:
  - Neural Network
  - Line Segment Detector
  - Satellite Trail Detection
  - Mini-SiTian Array
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16771
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:34:25.024151",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Line Segment Detector",
    "Satellite Trail Detection",
    "Mini-SiTian Array"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Line Segment Detector": 0.7,
    "Satellite Trail Detection": 0.75,
    "Mini-SiTian Array": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "U-Net deep neural network",
        "canonical": "Neural Network",
        "aliases": [
          "U-Net"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are a fundamental concept in deep learning, and U-Net is a specific architecture relevant to image segmentation tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Line Segment Detector",
        "canonical": "Line Segment Detector",
        "aliases": [
          "LSD algorithm"
        ],
        "category": "unique_technical",
        "rationale": "The Line Segment Detector is a specific algorithm used for detecting lines in images, which is crucial for identifying satellite trails.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "satellite trail detection",
        "canonical": "Satellite Trail Detection",
        "aliases": [
          "satellite trails"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application within astronomical imaging, focusing on mitigating interference from artificial satellites.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Mini-SiTian Array",
        "canonical": "Mini-SiTian Array",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Mini-SiTian Array is a specific observational setup used in the study, providing context and data for the research.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "astronomical imaging",
      "photometric errors"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "U-Net deep neural network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Line Segment Detector",
      "resolved_canonical": "Line Segment Detector",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "satellite trail detection",
      "resolved_canonical": "Satellite Trail Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Mini-SiTian Array",
      "resolved_canonical": "Mini-SiTian Array",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Artificial Satellite Trails Detection Using U-Net Deep Neural Network and Line Segment Detector Algorithm

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16771.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16771](https://arxiv.org/abs/2509.16771)

## 🔗 유사한 논문
- [[2025-09-22/SGMAGNet_ A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark_20250922|SGMAGNet: A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark]] (80.7% similar)
- [[2025-09-23/TinyDef-DETR_ A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery_20250923|TinyDef-DETR: A DETR-based Framework for Defect Detection in Transmission Lines from UAV Imagery]] (80.3% similar)
- [[2025-09-22/A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction_20250922|A multi-temporal multi-spectral attention-augmented deep convolution neural network with contrastive learning for crop yield prediction]] (79.9% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (78.9% similar)
- [[2025-09-23/A study on Deep Convolutional Neural Networks, transfer learning, and Mnet model for Cervical Cancer Detection_20250923|A study on Deep Convolutional Neural Networks, transfer learning, and Mnet model for Cervical Cancer Detection]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Line Segment Detector|Line Segment Detector]], [[keywords/Satellite Trail Detection|Satellite Trail Detection]], [[keywords/Mini-SiTian Array|Mini-SiTian Array]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16771v1 Announce Type: new 
Abstract: With the rapid increase in the number of artificial satellites, astronomical imaging is experiencing growing interference. When these satellites reflect sunlight, they produce streak-like artifacts in photometry images. Such satellite trails can introduce false sources and cause significant photometric errors. As a result, accurately identifying the positions of satellite trails in observational data has become essential. In this work, we propose a satellite trail detection model that combines the U-Net deep neural network for image segmentation with the Line Segment Detector (LSD) algorithm. The model is trained on 375 simulated images of satellite trails, generated using data from the Mini-SiTian Array. Experimental results show that for trails with a signal-to-noise ratio (SNR) greater than 3, the detection rate exceeds 99. Additionally, when applied to real observational data from the Mini-SiTian Array, the model achieves a recall of 79.57 and a precision of 74.56.

## 📝 요약

인공위성 수가 급증하면서 천문학적 이미지에 대한 간섭이 증가하고 있습니다. 위성이 태양빛을 반사할 때 이미지에 줄무늬 같은 왜곡을 일으켜 잘못된 정보를 제공하고 측광 오류를 유발할 수 있습니다. 이를 해결하기 위해, 본 연구에서는 이미지 분할을 위한 U-Net 심층 신경망과 선분 검출기(LSD) 알고리즘을 결합한 위성 궤적 검출 모델을 제안합니다. Mini-SiTian Array 데이터를 활용해 생성된 375개의 시뮬레이션 이미지를 통해 모델을 학습시켰으며, 실험 결과 신호 대 잡음비(SNR)가 3을 초과하는 궤적에 대해 99% 이상의 검출률을 보였습니다. 실제 관측 데이터에 적용했을 때, 모델은 79.57의 재현율과 74.56의 정밀도를 기록했습니다.

## 🎯 주요 포인트

- 1. 인공위성의 증가로 인해 천문학적 이미지에 대한 간섭이 증가하고 있으며, 이는 위성 궤적이 이미지에 줄무늬 같은 인공물을 생성하여 오류를 유발합니다.
- 2. 위성 궤적의 정확한 위치 식별이 관측 데이터 분석에 필수적입니다.
- 3. 본 연구는 이미지 분할을 위한 U-Net 심층 신경망과 선분 검출 알고리즘(LSD)을 결합한 위성 궤적 탐지 모델을 제안합니다.
- 4. 제안된 모델은 Mini-SiTian Array의 데이터를 사용하여 생성된 375개의 시뮬레이션 이미지로 훈련되었습니다.
- 5. 실험 결과, 신호 대 잡음비(SNR)가 3을 초과하는 궤적에 대해 탐지율이 99%를 넘으며, 실제 관측 데이터에 적용 시 재현율 79.57, 정밀도 74.56을 달성했습니다.


---

*Generated on 2025-09-24 04:34:25*