---
keywords:
  - Sparse Mixture of Experts
  - Transformer
  - Neural Bandit
  - Task-Aware Expert Merging
  - Online MoE Inference
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19781
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:39:55.413996",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Mixture of Experts",
    "Transformer",
    "Neural Bandit",
    "Task-Aware Expert Merging",
    "Online MoE Inference"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Mixture of Experts": 0.82,
    "Transformer": 0.88,
    "Neural Bandit": 0.83,
    "Task-Aware Expert Merging": 0.79,
    "Online MoE Inference": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Mixture of Experts",
        "canonical": "Sparse Mixture of Experts",
        "aliases": [
          "SMoE"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific architecture relevant to scaling Transformer capacity efficiently.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model architecture in deep learning, relevant to the paper's context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.88
      },
      {
        "surface": "Neural Bandit",
        "canonical": "Neural Bandit",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Neural Bandit is a novel approach in the paper for optimizing expert merging decisions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.83
      },
      {
        "surface": "Task-Aware Expert Merging",
        "canonical": "Task-Aware Expert Merging",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a unique technique introduced in the paper for improving online inference.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Online MoE Inference",
        "canonical": "Online MoE Inference",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper focuses on improving this specific type of inference, making it a key concept.",
        "novelty_score": 0.68,
        "connectivity_score": 0.64,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
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
      "candidate_surface": "Sparse Mixture of Experts",
      "resolved_canonical": "Sparse Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Neural Bandit",
      "resolved_canonical": "Neural Bandit",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Task-Aware Expert Merging",
      "resolved_canonical": "Task-Aware Expert Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Online MoE Inference",
      "resolved_canonical": "Online MoE Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.64,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Faster, Smaller, and Smarter: Task-Aware Expert Merging for Online MoE Inference

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19781.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19781](https://arxiv.org/abs/2509.19781)

## 🔗 유사한 논문
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (85.2% similar)
- [[2025-09-24/Union of Experts_ Adapting Hierarchical Routing to Equivalently Decomposed Transformer_20250924|Union of Experts: Adapting Hierarchical Routing to Equivalently Decomposed Transformer]] (83.9% similar)
- [[2025-09-24/Symphony-MoE_ Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts_20250924|Symphony-MoE: Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts]] (83.0% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (82.9% similar)
- [[2025-09-24/LongCat-Flash-Thinking Technical Report_20250924|LongCat-Flash-Thinking Technical Report]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Sparse Mixture of Experts|Sparse Mixture of Experts]], [[keywords/Neural Bandit|Neural Bandit]], [[keywords/Task-Aware Expert Merging|Task-Aware Expert Merging]], [[keywords/Online MoE Inference|Online MoE Inference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19781v1 Announce Type: new 
Abstract: Sparse Mixture of Experts (SMoE) has become a preferred architecture for scaling Transformer capacity without increasing computational cost, as it activates only a small subset of experts for each input. However, deploying such an approach for \textit{online inference} remains challenging due to the large size of a full SMoE model and the complexity of expert routing, especially in resource-constrained edge networks. Moreover, during the online inference, task information is often unavailable, making the task-level routing error-prone. In this work, we propose a novel tree-structured adaptive neural bandit router, \texttt{Tanbr}, to enable efficient and reliable online MoE inference. Instead of relying on explicit task tags, \texttt{Tanbr} estimates the task distribution over time from historical data and uses it to guide task-aware expert merging within a given pre-trained MoE. To handle the large continuous space of merging weights, \texttt{Tanbr} employs a binary tree to progressively partition the space and generate finer candidate weights. It then applies a neural bandit to learn the non-linear mapping from merging weight to model performance and decides optimal expert merging. We prove that \texttt{Tanbr} achieves a sublinear regret bound of {\small $\mathcal{O}(\sqrt{T} \log(T))$} over {\small $T$} rounds, despite operating over a continuous decision space, matching regret bounds compared to existing methods. Extensive experiments show that \texttt{Tanbr} reduces inference latency by at least {\small $45\%$} and memory usage by up to {\small $25\%$}, while maintaining a high accuracy compared to many state-of-the-art methods.

## 📝 요약

Sparse Mixture of Experts(SMoE)는 트랜스포머의 용량을 확장하면서도 계산 비용을 증가시키지 않는 아키텍처로 주목받고 있지만, 온라인 추론에서는 모델의 크기와 전문가 라우팅의 복잡성 때문에 어려움이 있습니다. 이를 해결하기 위해 본 연구에서는 \texttt{Tanbr}라는 새로운 트리 구조의 적응형 신경 밴딧 라우터를 제안합니다. \texttt{Tanbr}는 명시적인 태스크 태그 없이 과거 데이터를 통해 태스크 분포를 추정하고, 이를 기반으로 전문가 병합을 수행합니다. 또한, 이진 트리를 사용해 병합 가중치 공간을 세분화하고, 신경 밴딧을 통해 최적의 전문가 병합을 결정합니다. \texttt{Tanbr}는 연속적인 결정 공간에서도 서브리니어 후회 경계를 달성하며, 실험 결과 최소 45%의 추론 지연 감소와 최대 25%의 메모리 사용 절감을 이루면서도 높은 정확도를 유지합니다.

## 🎯 주요 포인트

- 1. Sparse Mixture of Experts (SMoE)는 입력마다 소수의 전문가만 활성화하여 계산 비용을 증가시키지 않고 Transformer의 용량을 확장하는 데 선호되는 아키텍처입니다.
- 2. \texttt{Tanbr}는 온라인 추론 시 효율적이고 신뢰할 수 있는 MoE 추론을 가능하게 하는 새로운 트리 구조의 적응형 신경 밴딧 라우터입니다.
- 3. \texttt{Tanbr}는 명시적인 태스크 태그 대신 역사적 데이터를 통해 태스크 분포를 추정하고 이를 사용하여 전문가 병합을 안내합니다.
- 4. \texttt{Tanbr}는 연속적인 병합 가중치 공간을 이진 트리로 분할하고 신경 밴딧을 적용하여 최적의 전문가 병합을 결정합니다.
- 5. 실험 결과, \texttt{Tanbr}는 추론 지연을 최소 45% 줄이고 메모리 사용량을 최대 25% 줄이면서도 높은 정확도를 유지합니다.


---

*Generated on 2025-09-25 16:39:55*