---
keywords:
  - DINOv2 Embeddings
  - Dirichlet Process Mixture Model
  - Anomaly Detection
  - Medical Imaging
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19997
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:59:39.401273",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DINOv2 Embeddings",
    "Dirichlet Process Mixture Model",
    "Anomaly Detection",
    "Medical Imaging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DINOv2 Embeddings": 0.78,
    "Dirichlet Process Mixture Model": 0.82,
    "Anomaly Detection": 0.79,
    "Medical Imaging": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DINOv2 embeddings",
        "canonical": "DINOv2 Embeddings",
        "aliases": [
          "DINO embeddings"
        ],
        "category": "unique_technical",
        "rationale": "DINOv2 embeddings are central to the paper's approach for anomaly detection, offering a novel application in medical imaging.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dirichlet Process Mixture model",
        "canonical": "Dirichlet Process Mixture Model",
        "aliases": [
          "DPMM"
        ],
        "category": "specific_connectable",
        "rationale": "The DPMM is a key component in the methodology, providing a non-parametric approach to modeling data distributions.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "anomaly detection",
        "canonical": "Anomaly Detection",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Anomaly detection is a fundamental concept in the paper, linking it to broader discussions in machine learning and medical imaging.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.79
      },
      {
        "surface": "medical imaging",
        "canonical": "Medical Imaging",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Medical imaging is the application domain, providing context and potential connections to other research in the field.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "memory bank",
      "normative features"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DINOv2 embeddings",
      "resolved_canonical": "DINOv2 Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dirichlet Process Mixture model",
      "resolved_canonical": "Dirichlet Process Mixture Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "anomaly detection",
      "resolved_canonical": "Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "medical imaging",
      "resolved_canonical": "Medical Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Anomaly Detection by Clustering DINO Embeddings using a Dirichlet Process Mixture

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19997.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19997](https://arxiv.org/abs/2509.19997)

## 🔗 유사한 논문
- [[2025-09-18/AD-DINOv3_ Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration_20250918|AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (84.7% similar)
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (82.9% similar)
- [[2025-09-23/A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis_20250923|A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis]] (82.8% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (82.7% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Anomaly Detection|Anomaly Detection]]
**🔗 Specific Connectable**: [[keywords/Dirichlet Process Mixture Model|Dirichlet Process Mixture Model]], [[keywords/Medical Imaging|Medical Imaging]]
**⚡ Unique Technical**: [[keywords/DINOv2 Embeddings|DINOv2 Embeddings]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19997v1 Announce Type: cross 
Abstract: In this work, we leverage informative embeddings from foundational models for unsupervised anomaly detection in medical imaging. For small datasets, a memory-bank of normative features can directly be used for anomaly detection which has been demonstrated recently. However, this is unsuitable for large medical datasets as the computational burden increases substantially. Therefore, we propose to model the distribution of normative DINOv2 embeddings with a Dirichlet Process Mixture model (DPMM), a non-parametric mixture model that automatically adjusts the number of mixture components to the data at hand. Rather than using a memory bank, we use the similarity between the component centers and the embeddings as anomaly score function to create a coarse anomaly segmentation mask. Our experiments show that through DPMM embeddings of DINOv2, despite being trained on natural images, achieve very competitive anomaly detection performance on medical imaging benchmarks and can do this while at least halving the computation time at inference. Our analysis further indicates that normalized DINOv2 embeddings are generally more aligned with anatomical structures than unnormalized features, even in the presence of anomalies, making them great representations for anomaly detection. The code is available at https://github.com/NicoSchulthess/anomalydino-dpmm.

## 📝 요약

이 연구는 기초 모델에서 얻은 임베딩을 활용하여 의료 영상에서 비지도 이상 탐지를 수행합니다. 작은 데이터셋에서는 메모리 뱅크를 사용한 이상 탐지가 가능하지만, 대규모 의료 데이터셋에서는 계산 부담이 큽니다. 이를 해결하기 위해, 우리는 DINOv2 임베딩의 분포를 비모수 혼합 모델인 디리클레 프로세스 혼합 모델(DPMM)로 모델링합니다. 메모리 뱅크 대신, 구성 요소 중심과 임베딩 간의 유사성을 이상 점수 함수로 사용하여 이상 탐지 마스크를 생성합니다. 실험 결과, DINOv2 임베딩은 자연 이미지로 학습되었음에도 불구하고 의료 영상 벤치마크에서 경쟁력 있는 이상 탐지 성능을 보였으며, 추론 시 계산 시간을 절반 이상 줄일 수 있었습니다. 또한, 정규화된 DINOv2 임베딩이 비정규화된 특징보다 해부학적 구조와 더 잘 맞아 이상 탐지에 효과적임을 확인했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 기초 모델의 정보 임베딩을 활용하여 의료 영상에서 비지도 학습 기반의 이상 탐지를 수행합니다.
- 2. 대규모 의료 데이터셋에 적합한 비모수 혼합 모델인 디리클레 프로세스 혼합 모델(DPMM)을 제안합니다.
- 3. DPMM을 사용하여 DINOv2 임베딩의 분포를 모델링하고, 메모리 뱅크 대신 컴포넌트 중심과 임베딩 간의 유사성을 이상 점수 함수로 사용합니다.
- 4. DINOv2 임베딩은 자연 이미지로 학습되었음에도 불구하고, 의료 영상 벤치마크에서 경쟁력 있는 이상 탐지 성능을 보여주며, 추론 시 계산 시간을 절반 이상 줄일 수 있습니다.
- 5. 정규화된 DINOv2 임베딩은 해부학적 구조와 더 잘 정렬되어 이상 탐지에 적합한 표현을 제공합니다.


---

*Generated on 2025-09-25 16:59:39*