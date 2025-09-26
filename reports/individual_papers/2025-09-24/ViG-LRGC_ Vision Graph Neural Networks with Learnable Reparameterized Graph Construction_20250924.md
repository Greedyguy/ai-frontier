<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:10:21.874715",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Learnable Reparameterized Graph Construction",
    "Image Representation Learning",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Learnable Reparameterized Graph Construction": 0.79,
    "Image Representation Learning": 0.72,
    "Attention Mechanism": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "ViG"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing Graph Neural Network concepts and extends them to vision applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.88
      },
      {
        "surface": "Learnable Reparameterized Graph Construction",
        "canonical": "Learnable Reparameterized Graph Construction",
        "aliases": [
          "LRGC"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for graph construction in vision networks, enhancing specificity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Image Representation Learning",
        "canonical": "Image Representation Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Key concept in computer vision, linking to broader image processing techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Connects to the use of attention in graph construction, a key component in the proposed method.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "hyper-parameter",
      "latent features"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Learnable Reparameterized Graph Construction",
      "resolved_canonical": "Learnable Reparameterized Graph Construction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Image Representation Learning",
      "resolved_canonical": "Image Representation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# ViG-LRGC: Vision Graph Neural Networks with Learnable Reparameterized Graph Construction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18840.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18840](https://arxiv.org/abs/2509.18840)

## 🔗 유사한 논문
- [[2025-09-23/Revisiting Vision Language Foundations for No-Reference Image Quality Assessment_20250923|Revisiting Vision Language Foundations for No-Reference Image Quality Assessment]] (83.5% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (83.5% similar)
- [[2025-09-23/Visual Instruction Pretraining for Domain-Specific Foundation Models_20250923|Visual Instruction Pretraining for Domain-Specific Foundation Models]] (83.0% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (82.6% similar)
- [[2025-09-24/Long-Range Graph Wavelet Networks_20250924|Long-Range Graph Wavelet Networks]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Image Representation Learning|Image Representation Learning]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Learnable Reparameterized Graph Construction|Learnable Reparameterized Graph Construction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18840v1 Announce Type: new 
Abstract: Image Representation Learning is an important problem in Computer Vision. Traditionally, images were processed as grids, using Convolutional Neural Networks or as a sequence of visual tokens, using Vision Transformers. Recently, Vision Graph Neural Networks (ViG) have proposed the treatment of images as a graph of nodes; which provides a more intuitive image representation. The challenge is to construct a graph of nodes in each layer that best represents the relations between nodes and does not need a hyper-parameter search. ViG models in the literature depend on non-parameterized and non-learnable statistical methods that operate on the latent features of nodes to create a graph. This might not select the best neighborhood for each node. Starting from k-NN graph construction to HyperGraph Construction and Similarity-Thresholded graph construction, these methods lack the ability to provide a learnable hyper-parameter-free graph construction method. To overcome those challenges, we present the Learnable Reparameterized Graph Construction (LRGC) for Vision Graph Neural Networks. LRGC applies key-query attention between every pair of nodes; then uses soft-threshold reparameterization for edge selection, which allows the use of a differentiable mathematical model for training. Using learnable parameters to select the neighborhood removes the bias that is induced by any clustering or thresholding methods previously introduced in the literature. In addition, LRGC allows tuning the threshold in each layer to the training data since the thresholds are learnable through training and are not provided as hyper-parameters to the model. We demonstrate that the proposed ViG-LRGC approach outperforms state-of-the-art ViG models of similar sizes on the ImageNet-1k benchmark dataset.

## 📝 요약

이 논문은 이미지 표현 학습에서 그래프 기반 접근법을 제안합니다. 기존의 비전 그래프 신경망(ViG) 모델은 비매개변수적 통계 방법에 의존하여 노드 간 관계를 표현하는 그래프를 생성하지만, 이는 최적의 이웃 선택을 보장하지 못합니다. 이를 해결하기 위해, 학습 가능한 재매개변수화 그래프 생성(LRGC) 방법을 제안합니다. LRGC는 노드 간 키-쿼리 주의를 적용하고, 소프트 임계값 재매개변수를 통해 엣지를 선택하여 학습 가능한 모델을 제공합니다. 이를 통해 클러스터링이나 임계값 설정의 편향을 제거하고, 각 층의 임계값을 데이터에 맞게 조정할 수 있습니다. 제안된 ViG-LRGC 모델은 ImageNet-1k 데이터셋에서 기존 ViG 모델보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 이미지 표현 학습은 컴퓨터 비전에서 중요한 문제로, 최근에는 이미지를 그래프로 처리하는 비전 그래프 신경망(ViG)이 제안되었습니다.
- 2. 기존 ViG 모델은 비매개변수적이고 학습 불가능한 통계적 방법에 의존하여 노드의 잠재적 특징을 기반으로 그래프를 생성합니다.
- 3. 학습 가능한 재매개변수화 그래프 생성(LRGC)은 노드 간의 키-쿼리 주의를 적용하고, 소프트-임계값 재매개변수를 통해 엣지를 선택하여 학습 가능한 매개변수를 사용해 편향을 제거합니다.
- 4. LRGC는 각 레이어에서 임계값을 학습 가능한 매개변수로 조정하여 데이터에 맞게 최적화할 수 있습니다.
- 5. 제안된 ViG-LRGC 접근법은 ImageNet-1k 벤치마크 데이터셋에서 유사한 크기의 최신 ViG 모델보다 우수한 성능을 보입니다.


---

*Generated on 2025-09-24 16:10:21*