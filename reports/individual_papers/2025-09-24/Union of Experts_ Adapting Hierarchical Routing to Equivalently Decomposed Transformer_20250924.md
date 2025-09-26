<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:30:41.963877",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture-of-Experts",
    "Union-of-Experts",
    "Hierarchical Routing",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture-of-Experts": 0.8,
    "Union-of-Experts": 0.85,
    "Hierarchical Routing": 0.78,
    "Attention Mechanism": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mixture-of-Experts",
        "canonical": "Mixture-of-Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "Mixture-of-Experts is a key concept in the paper, central to understanding the proposed Union-of-Experts model.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Union-of-Experts",
        "canonical": "Union-of-Experts",
        "aliases": [
          "UoE"
        ],
        "category": "unique_technical",
        "rationale": "Union-of-Experts is the novel contribution of the paper, representing a new model architecture.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hierarchical Routing",
        "canonical": "Hierarchical Routing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Hierarchical Routing is a novel mechanism proposed in the paper, crucial for the model's efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Attention Blocks",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Blocks"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanism is extended in the paper, linking it to the broader context of transformer models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "Full Attention",
      "state-of-the-art",
      "efficient transformers"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mixture-of-Experts",
      "resolved_canonical": "Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Union-of-Experts",
      "resolved_canonical": "Union-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hierarchical Routing",
      "resolved_canonical": "Hierarchical Routing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Attention Blocks",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Union of Experts: Adapting Hierarchical Routing to Equivalently Decomposed Transformer

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.02495.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2503.02495](https://arxiv.org/abs/2503.02495)

## 🔗 유사한 논문
- [[2025-09-24/Symphony-MoE_ Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts_20250924|Symphony-MoE: Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts]] (88.0% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (87.7% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (85.1% similar)
- [[2025-09-23/Dynamic Expert Specialization_ Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation_20250923|Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation]] (84.8% similar)
- [[2025-09-22/TrueMoE_ Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection_20250922|TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Union-of-Experts|Union-of-Experts]], [[keywords/Hierarchical Routing|Hierarchical Routing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.02495v3 Announce Type: replace-cross 
Abstract: Mixture-of-Experts (MoE) enhances model performance while maintaining computational efficiency, making it well-suited for large-scale applications. Conventional mixture-of-experts (MoE) architectures suffer from suboptimal coordination dynamics, where isolated expert operations expose the model to overfitting risks. Moreover, they have not been effectively extended to attention blocks, which limits further efficiency improvements. To tackle these issues, we propose Union-of-Experts (UoE), which decomposes the transformer model into an equivalent group of experts and applies a hierarchical routing mechanism to allocate input subspaces to specialized experts. Our approach advances MoE design with four key innovations: (1) Constructing expert groups by partitioning non-MoE models into functionally equivalent specialists (2) Developing a hierarchical routing paradigm that integrates patch-wise data selection and expert selection strategies. (3) Extending the MoE design to attention blocks. (4) Proposing a hardware-optimized parallelization scheme that exploits batched matrix multiplications for efficient expert computation. The experiments demonstrate that our UoE model surpasses Full Attention, state-of-the-art MoEs and efficient transformers in several tasks across image and natural language domains. In language modeling tasks, UoE achieves an average reduction of 2.38 in perplexity compared to the best-performing MoE method with only 76% of its FLOPs. In the Long Range Arena benchmark, it demonstrates an average score at least 0.68% higher than all comparison models, with only 50% of the FLOPs of the best MoE method. In image classification, it yields an average accuracy improvement of 1.75% over the best model while maintaining comparable FLOPs. The source codes are available at https://github.com/YujiaoYang-work/UoE.

## 📝 요약

Mixture-of-Experts (MoE) 모델의 한계를 극복하기 위해 제안된 Union-of-Experts (UoE) 모델은 트랜스포머를 전문가 그룹으로 분해하고 계층적 라우팅 메커니즘을 통해 입력을 전문화된 전문가에게 할당합니다. UoE는 비MoE 모델을 기능적으로 분할하여 전문가 그룹을 구성하고, 패치 기반 데이터 선택과 전문가 선택 전략을 통합한 계층적 라우팅 패러다임을 개발하며, MoE 디자인을 주의 블록으로 확장하고, 하드웨어 최적화 병렬화 스킴을 제안합니다. 실험 결과, UoE는 이미지 및 자연어 처리 작업에서 기존 MoE 및 효율적인 트랜스포머를 능가하며, 언어 모델링에서 최상의 MoE 대비 2.38의 퍼플렉시티 감소와 76%의 FLOPs만으로 성능을 발휘합니다. Long Range Arena 벤치마크에서는 최상의 MoE 대비 FLOPs의 50%만으로 평균 0.68% 높은 점수를 기록하며, 이미지 분류에서는 평균 1.75%의 정확도 향상을 보입니다. 소스 코드는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. Union-of-Experts (UoE)는 트랜스포머 모델을 전문가 그룹으로 분해하고 계층적 라우팅 메커니즘을 적용하여 입력 하위 공간을 전문화된 전문가에게 할당합니다.
- 2. UoE는 비-MoE 모델을 기능적으로 동등한 전문가로 분할하여 전문가 그룹을 구성합니다.
- 3. MoE 설계를 주의 블록으로 확장하여 효율성을 높였습니다.
- 4. 하드웨어 최적화 병렬화 방식을 제안하여 배치 행렬 곱셈을 활용한 효율적인 전문가 계산을 구현합니다.
- 5. UoE 모델은 이미지 및 자연어 분야에서 최첨단 MoE 및 효율적인 트랜스포머를 능가하는 성능을 보여줍니다.


---

*Generated on 2025-09-24 14:30:41*