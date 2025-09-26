<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:53:09.129164",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Hybrid Dataset",
    "Synthetic Data",
    "Anti-Money Laundering Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Hybrid Dataset": 0.72,
    "Synthetic Data": 0.65,
    "Anti-Money Laundering Model": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the paper's discussion on training AML models, providing a direct link to existing knowledge on neural network architectures.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Hybrid Datasets",
        "canonical": "Hybrid Dataset",
        "aliases": [
          "Mixed Dataset",
          "Composite Dataset"
        ],
        "category": "unique_technical",
        "rationale": "Hybrid Datasets are a novel concept in the paper, proposed to enhance the utility of synthetic data, making it a unique technical term.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Synthetic Data",
        "canonical": "Synthetic Data",
        "aliases": [
          "Generated Data",
          "Artificial Data"
        ],
        "category": "broad_technical",
        "rationale": "Synthetic Data is a key component in the discussion of privacy-preserving data for training models, linking to broader discussions on data generation.",
        "novelty_score": 0.3,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      },
      {
        "surface": "Anti-Money Laundering Models",
        "canonical": "Anti-Money Laundering Model",
        "aliases": [
          "AML Models"
        ],
        "category": "unique_technical",
        "rationale": "Anti-Money Laundering Models are the primary application focus of the paper, providing a specific context for the proposed hybrid datasets.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "Automated",
      "Real-time",
      "Privacy",
      "Confidentiality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Hybrid Datasets",
      "resolved_canonical": "Hybrid Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Synthetic Data",
      "resolved_canonical": "Synthetic Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Anti-Money Laundering Models",
      "resolved_canonical": "Anti-Money Laundering Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Hybrid Data can Enhance the Utility of Synthetic Data for Training Anti-Money Laundering Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18499.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18499](https://arxiv.org/abs/2509.18499)

## 🔗 유사한 논문
- [[2025-09-18/SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench: A Benchmark for Differentially Private Text Generation]] (80.1% similar)
- [[2025-09-19/Evaluating Supervised Learning Models for Fraud Detection_ A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data_20250919|Evaluating Supervised Learning Models for Fraud Detection: A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data]] (79.9% similar)
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (79.9% similar)
- [[2025-09-23/Enhancing Financial RAG with Agentic AI and Multi-HyDE_ A Novel Approach to Knowledge Retrieval and Hallucination Reduction_20250923|Enhancing Financial RAG with Agentic AI and Multi-HyDE: A Novel Approach to Knowledge Retrieval and Hallucination Reduction]] (79.7% similar)
- [[2025-09-24/Data Valuation and Selection in a Federated Model Marketplace_20250924|Data Valuation and Selection in a Federated Model Marketplace]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Synthetic Data|Synthetic Data]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Hybrid Dataset|Hybrid Dataset]], [[keywords/Anti-Money Laundering Model|Anti-Money Laundering Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18499v1 Announce Type: new 
Abstract: Money laundering is a critical global issue for financial institutions. Automated Anti-money laundering (AML) models, like Graph Neural Networks (GNN), can be trained to identify illicit transactions in real time. A major issue for developing such models is the lack of access to training data due to privacy and confidentiality concerns. Synthetically generated data that mimics the statistical properties of real data but preserves privacy and confidentiality has been proposed as a solution. However, training AML models on purely synthetic datasets presents its own set of challenges. This article proposes the use of hybrid datasets to augment the utility of synthetic datasets by incorporating publicly available, easily accessible, and real-world features. These additions demonstrate that hybrid datasets not only preserve privacy but also improve model utility, offering a practical pathway for financial institutions to enhance AML systems.

## 📝 요약

이 논문은 금융기관의 주요 문제인 자금 세탁을 해결하기 위해 자동화된 자금세탁방지(AML) 모델, 특히 그래프 신경망(GNN)을 활용하는 방법을 제안합니다. 모델 개발의 주요 장애물은 데이터 접근성 문제로, 개인정보 보호와 기밀성 때문에 훈련 데이터가 부족하다는 점입니다. 이를 해결하기 위해 통계적 특성을 모방하면서도 개인정보를 보호하는 합성 데이터를 사용하는 방법이 제안되었으나, 순수 합성 데이터로 훈련하는 데는 한계가 있습니다. 본 연구는 공개적으로 접근 가능한 실제 데이터를 결합한 하이브리드 데이터셋을 활용해 이러한 한계를 극복하고자 합니다. 하이브리드 데이터셋은 개인정보를 보호하면서도 모델의 유용성을 향상시켜 금융기관이 AML 시스템을 강화할 수 있는 실질적인 방법을 제공합니다.

## 🎯 주요 포인트

- 1. 자금 세탁은 금융 기관에 있어 중요한 글로벌 문제이다.
- 2. 그래프 신경망(GNN)과 같은 자동화된 자금 세탁 방지(AML) 모델은 실시간으로 불법 거래를 식별할 수 있다.
- 3. 개인정보 보호 및 기밀성 문제로 인해 훈련 데이터에 대한 접근이 어려운 것이 주요 문제이다.
- 4. 합성 데이터는 실제 데이터의 통계적 특성을 모방하면서도 개인정보를 보호하는 해결책으로 제안되었다.
- 5. 하이브리드 데이터셋은 공개적으로 접근 가능한 실제 세계의 특징을 통합하여 모델의 유용성을 높이고 개인정보를 보호한다.


---

*Generated on 2025-09-24 14:53:09*