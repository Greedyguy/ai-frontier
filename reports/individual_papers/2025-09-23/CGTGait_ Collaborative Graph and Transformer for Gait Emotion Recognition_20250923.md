---
keywords:
  - Transformer
  - Graph Neural Network
  - Bidirectional Cross-Stream Fusion
  - Spatiotemporal Features
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16623
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:28:07.193996",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Graph Neural Network",
    "Bidirectional Cross-Stream Fusion",
    "Spatiotemporal Features"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Graph Neural Network": 0.82,
    "Bidirectional Cross-Stream Fusion": 0.7,
    "Spatiotemporal Features": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are central to the proposed framework, linking to a wide range of machine learning applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Graph Convolution",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Convolution is a key component of the framework, directly linking to Graph Neural Networks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bidirectional Cross-Stream Fusion",
        "canonical": "Bidirectional Cross-Stream Fusion",
        "aliases": [
          "BCSF"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel module introduced in the paper, enhancing the framework's capability to integrate information.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Spatiotemporal Features",
        "canonical": "Spatiotemporal Features",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Capturing spatiotemporal features is crucial for gait emotion recognition, linking to broader computer vision tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "testing"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Graph Convolution",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bidirectional Cross-Stream Fusion",
      "resolved_canonical": "Bidirectional Cross-Stream Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Spatiotemporal Features",
      "resolved_canonical": "Spatiotemporal Features",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# CGTGait: Collaborative Graph and Transformer for Gait Emotion Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16623.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16623](https://arxiv.org/abs/2509.16623)

## 🔗 유사한 논문
- [[2025-09-23/Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models_20250923|Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models]] (82.1% similar)
- [[2025-09-23/Confidence-gated training for efficient early-exit neural networks_20250923|Confidence-gated training for efficient early-exit neural networks]] (81.4% similar)
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (81.2% similar)
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (80.4% similar)
- [[2025-09-18/LSTC-MDA_ A Unified Framework for Long-Short Term Temporal Convolution and Mixed Data Augmentation in Skeleton-Based Action Recognition_20250918|LSTC-MDA: A Unified Framework for Long-Short Term Temporal Convolution and Mixed Data Augmentation in Skeleton-Based Action Recognition]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Spatiotemporal Features|Spatiotemporal Features]]
**⚡ Unique Technical**: [[keywords/Bidirectional Cross-Stream Fusion|Bidirectional Cross-Stream Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16623v1 Announce Type: new 
Abstract: Skeleton-based gait emotion recognition has received significant attention due to its wide-ranging applications. However, existing methods primarily focus on extracting spatial and local temporal motion information, failing to capture long-range temporal representations. In this paper, we propose \textbf{CGTGait}, a novel framework that collaboratively integrates graph convolution and transformers to extract discriminative spatiotemporal features for gait emotion recognition. Specifically, CGTGait consists of multiple CGT blocks, where each block employs graph convolution to capture frame-level spatial topology and the transformer to model global temporal dependencies. Additionally, we introduce a Bidirectional Cross-Stream Fusion (BCSF) module to effectively aggregate posture and motion spatiotemporal features, facilitating the exchange of complementary information between the two streams. We evaluate our method on two widely used datasets, Emotion-Gait and ELMD, demonstrating that our CGTGait achieves state-of-the-art or at least competitive performance while reducing computational complexity by approximately \textbf{82.2\%} (only requiring 0.34G FLOPs) during testing. Code is available at \small{https://github.com/githubzjj1/CGTGait.}

## 📝 요약

이 논문에서는 골격 기반 보행 감정 인식을 위한 새로운 프레임워크인 CGTGait를 제안합니다. 기존 방법들이 주로 공간적 및 국소적 시간 정보를 추출하는 데 중점을 두는 반면, CGTGait는 그래프 컨볼루션과 트랜스포머를 결합하여 차별화된 시공간 특징을 추출합니다. CGTGait는 각 블록에서 그래프 컨볼루션을 통해 프레임 수준의 공간적 토폴로지를 포착하고, 트랜스포머를 통해 전역 시간 의존성을 모델링합니다. 또한, 자세와 움직임의 시공간 특징을 효과적으로 통합하기 위해 양방향 교차 스트림 융합 모듈(BCSF)을 도입합니다. Emotion-Gait와 ELMD 데이터셋에서 평가한 결과, CGTGait는 최첨단 성능을 달성하거나 최소한 경쟁력 있는 성능을 보이며, 테스트 시 약 82.2%의 계산 복잡성을 줄였습니다.

## 🎯 주요 포인트

- 1. CGTGait는 그래프 컨볼루션과 트랜스포머를 결합하여 차별적인 시공간 특징을 추출하는 새로운 프레임워크입니다.
- 2. CGTGait는 프레임 수준의 공간적 토폴로지를 포착하기 위해 그래프 컨볼루션을 사용하고, 글로벌 시간 의존성을 모델링하기 위해 트랜스포머를 사용합니다.
- 3. 양방향 교차 스트림 융합(BCSF) 모듈을 도입하여 자세와 움직임의 시공간 특징을 효과적으로 집계하고, 두 스트림 간의 보완 정보를 교환합니다.
- 4. Emotion-Gait와 ELMD 데이터셋에서 CGTGait는 최첨단 성능을 달성하거나 최소한 경쟁력 있는 성능을 보이며, 테스트 시 약 82.2%의 계산 복잡성을 줄입니다.


---

*Generated on 2025-09-24 04:28:07*