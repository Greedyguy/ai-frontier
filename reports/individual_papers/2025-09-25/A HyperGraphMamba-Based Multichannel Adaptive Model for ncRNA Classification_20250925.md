---
keywords:
  - HyperGraphMamba
  - ncRNA Classification
  - Multimodal Learning
  - Graph Neural Network
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20240
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:04:20.618403",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "HyperGraphMamba",
    "ncRNA Classification",
    "Multimodal Learning",
    "Graph Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "HyperGraphMamba": 0.78,
    "ncRNA Classification": 0.82,
    "Multimodal Learning": 0.8,
    "Graph Neural Network": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "HyperGraphMamba",
        "canonical": "HyperGraphMamba",
        "aliases": [
          "HGMamba"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel model specifically designed for ncRNA classification, offering unique insights into multimodal integration.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "ncRNA Classification",
        "canonical": "ncRNA Classification",
        "aliases": [
          "non-coding RNA Classification"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific application area that connects to broader topics in genomics and bioinformatics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multimodal Fusion",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Integration"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for integrating diverse data types, which is central to the paper's methodology.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Graph Transformer",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Graph Transformer"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are a key component of the model's architecture, facilitating advanced structural analysis.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "gene expression regulation",
      "disease diagnosis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "HyperGraphMamba",
      "resolved_canonical": "HyperGraphMamba",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ncRNA Classification",
      "resolved_canonical": "ncRNA Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multimodal Fusion",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Graph Transformer",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# A HyperGraphMamba-Based Multichannel Adaptive Model for ncRNA Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20240.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20240](https://arxiv.org/abs/2509.20240)

## 🔗 유사한 논문
- [[2025-09-23/TF-DWGNet_ A Directed Weighted Graph Neural Network with Tensor Fusion for Multi-Omics Cancer Subtype Classification_20250923|TF-DWGNet: A Directed Weighted Graph Neural Network with Tensor Fusion for Multi-Omics Cancer Subtype Classification]] (81.5% similar)
- [[2025-09-24/Topological Feature Compression for Molecular Graph Neural Networks_20250924|Topological Feature Compression for Molecular Graph Neural Networks]] (81.1% similar)
- [[2025-09-24/Reverse-Complement Consistency for DNA Language Models_20250924|Reverse-Complement Consistency for DNA Language Models]] (80.8% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (80.5% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/ncRNA Classification|ncRNA Classification]], [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/HyperGraphMamba|HyperGraphMamba]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20240v1 Announce Type: cross 
Abstract: Non-coding RNAs (ncRNAs) play pivotal roles in gene expression regulation and the pathogenesis of various diseases. Accurate classification of ncRNAs is essential for functional annotation and disease diagnosis. To address existing limitations in feature extraction depth and multimodal fusion, we propose HGMamba-ncRNA, a HyperGraphMamba-based multichannel adaptive model, which integrates sequence, secondary structure, and optionally available expression features of ncRNAs to enhance classification performance. Specifically, the sequence of ncRNA is modeled using a parallel Multi-scale Convolution and LSTM architecture (MKC-L) to capture both local patterns and long-range dependencies of nucleotides. The structure modality employs a multi-scale graph transformer (MSGraphTransformer) to represent the multi-level topological characteristics of ncRNA secondary structures. The expression modality utilizes a Chebyshev Polynomial-based Kolmogorov-Arnold Network (CPKAN) to effectively model and interpret high-dimensional expression profiles. Finally, by incorporating virtual nodes to facilitate efficient and comprehensive multimodal interaction, HyperGraphMamba is proposed to adaptively align and integrate multichannel heterogeneous modality features. Experiments conducted on three public datasets demonstrate that HGMamba-ncRNA consistently outperforms state-of-the-art methods in terms of accuracy and other metrics. Extensive empirical studies further confirm the model's robustness, effectiveness, and strong transferability, offering a novel and reliable strategy for complex ncRNA functional classification. Code and datasets are available at https://anonymous.4open.science/r/HGMamba-ncRNA-94D0.

## 📝 요약

비암호화 RNA(ncRNA)는 유전자 발현 조절과 질병 병인에 중요한 역할을 합니다. ncRNA의 정확한 분류는 기능적 주석과 질병 진단에 필수적입니다. 이를 위해 HGMamba-ncRNA라는 HyperGraphMamba 기반 다채널 적응 모델을 제안합니다. 이 모델은 ncRNA의 서열, 2차 구조, 발현 특징을 통합하여 분류 성능을 향상시킵니다. 서열은 다중 스케일 컨볼루션과 LSTM 아키텍처를 사용하여 지역 패턴과 장거리 의존성을 포착하고, 구조 모달리티는 다중 스케일 그래프 변환기를 사용하여 ncRNA 2차 구조의 위상적 특성을 나타냅니다. 발현 모달리티는 Chebyshev 다항식 기반 Kolmogorov-Arnold 네트워크를 활용하여 고차원 발현 프로필을 효과적으로 모델링합니다. 가상 노드를 통해 효율적이고 포괄적인 다중 모달 상호작용을 촉진하며, HGMamba는 다채널 이질 모달리티 특징을 적응적으로 정렬하고 통합합니다. 세 개의 공개 데이터셋에서 실험한 결과, HGMamba-ncRNA는 정확도 및 기타 지표에서 최첨단 방법들을 일관되게 능가했습니다. 광범위한 실증 연구는 모델의 강력한 전이 가능성과 효과를 확인하며, 복잡한 ncRNA 기능 분류에 대한 새로운 전략을 제공합니다.

## 🎯 주요 포인트

- 1. HGMamba-ncRNA는 ncRNA의 서열, 2차 구조, 발현 특징을 통합하여 분류 성능을 향상시키는 하이퍼그래프 기반 다채널 적응 모델입니다.
- 2. ncRNA 서열은 병렬 다중 스케일 컨볼루션과 LSTM 아키텍처(MKC-L)를 사용하여 뉴클레오타이드의 지역 패턴과 장거리 의존성을 포착합니다.
- 3. 구조 모달리티는 다중 스케일 그래프 변환기(MSGraphTransformer)를 통해 ncRNA 2차 구조의 다층 위상적 특성을 표현합니다.
- 4. 발현 모달리티는 Chebyshev 다항식 기반 Kolmogorov-Arnold 네트워크(CPKAN)를 활용하여 고차원 발현 프로파일을 효과적으로 모델링하고 해석합니다.
- 5. HGMamba-ncRNA는 세 가지 공공 데이터셋에서 최신 기법보다 우수한 성능을 보이며, 모델의 견고성, 효과성, 강력한 전이 가능성을 입증합니다.


---

*Generated on 2025-09-25 16:04:20*