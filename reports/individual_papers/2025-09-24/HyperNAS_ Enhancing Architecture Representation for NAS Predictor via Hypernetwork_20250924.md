<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:39:18.935622",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Architecture Search",
    "Hypernetwork",
    "Few-Shot Learning",
    "Global Encoding Scheme"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Architecture Search": 0.82,
    "Hypernetwork": 0.77,
    "Few-Shot Learning": 0.79,
    "Global Encoding Scheme": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Architecture Search",
        "canonical": "Neural Architecture Search",
        "aliases": [
          "NAS"
        ],
        "category": "specific_connectable",
        "rationale": "Neural Architecture Search is a key concept in optimizing neural network architectures and connects well with machine learning and neural network topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Hypernetwork",
        "canonical": "Hypernetwork",
        "aliases": [
          "Hypernetworks"
        ],
        "category": "unique_technical",
        "rationale": "Hypernetwork is a unique approach to enhance architecture representation, offering novel insights into neural network design.",
        "novelty_score": 0.72,
        "connectivity_score": 0.69,
        "specificity_score": 0.81,
        "link_intent_score": 0.77
      },
      {
        "surface": "Few-Shot Scenarios",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is increasingly relevant for efficient model training and connects with broader machine learning strategies.",
        "novelty_score": 0.58,
        "connectivity_score": 0.88,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
      },
      {
        "surface": "Global Encoding Scheme",
        "canonical": "Global Encoding Scheme",
        "aliases": [
          "Global Encoding"
        ],
        "category": "unique_technical",
        "rationale": "This scheme is central to the paper's method for capturing macro-structure information, offering a unique perspective on architecture representation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.67,
        "specificity_score": 0.79,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "performance evaluations",
      "proxy datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Architecture Search",
      "resolved_canonical": "Neural Architecture Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Hypernetwork",
      "resolved_canonical": "Hypernetwork",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.69,
        "specificity": 0.81,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Few-Shot Scenarios",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.88,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Global Encoding Scheme",
      "resolved_canonical": "Global Encoding Scheme",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.67,
        "specificity": 0.79,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# HyperNAS: Enhancing Architecture Representation for NAS Predictor via Hypernetwork

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18151.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18151](https://arxiv.org/abs/2509.18151)

## 🔗 유사한 논문
- [[2025-09-23/Deep Hierarchical Learning with Nested Subspace Networks_20250923|Deep Hierarchical Learning with Nested Subspace Networks]] (84.4% similar)
- [[2025-09-23/Neural Attention Search_20250923|Neural Attention Search]] (83.4% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (82.1% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.7% similar)
- [[2025-09-23/SINF_ Semantic Neural Network Inference with Semantic Subgraphs_20250923|SINF: Semantic Neural Network Inference with Semantic Subgraphs]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural Architecture Search|Neural Architecture Search]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Hypernetwork|Hypernetwork]], [[keywords/Global Encoding Scheme|Global Encoding Scheme]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18151v1 Announce Type: cross 
Abstract: Time-intensive performance evaluations significantly impede progress in Neural Architecture Search (NAS). To address this, neural predictors leverage surrogate models trained on proxy datasets, allowing for direct performance predictions for new architectures. However, these predictors often exhibit poor generalization due to their limited ability to capture intricate relationships among various architectures. In this paper, we propose HyperNAS, a novel neural predictor paradigm for enhancing architecture representation learning. HyperNAS consists of two primary components: a global encoding scheme and a shared hypernetwork. The global encoding scheme is devised to capture the comprehensive macro-structure information, while the shared hypernetwork serves as an auxiliary task to enhance the investigation of inter-architecture patterns. To ensure training stability, we further develop a dynamic adaptive multi-task loss to facilitate personalized exploration on the Pareto front. Extensive experiments across five representative search spaces, including ViTs, demonstrate the advantages of HyperNAS, particularly in few-shot scenarios. For instance, HyperNAS strikes new state-of-the-art results, with 97.60\% top-1 accuracy on CIFAR-10 and 82.4\% top-1 accuracy on ImageNet, using at least 5.0$\times$ fewer samples.

## 📝 요약

이 논문은 Neural Architecture Search(NAS)의 성능 평가 시간을 줄이기 위해 HyperNAS라는 새로운 신경 예측 모델을 제안합니다. HyperNAS는 아키텍처 표현 학습을 향상시키기 위한 글로벌 인코딩 스킴과 공유 하이퍼네트워크로 구성됩니다. 글로벌 인코딩 스킴은 전체적인 매크로 구조 정보를 포착하고, 공유 하이퍼네트워크는 아키텍처 간 패턴을 조사하는 보조 작업을 수행합니다. 또한, Pareto 전선에서의 개인화된 탐색을 촉진하기 위해 동적 적응형 다중 작업 손실을 개발했습니다. 실험 결과, HyperNAS는 특히 적은 샘플 시나리오에서 우수한 성능을 보였으며, CIFAR-10에서 97.60%, ImageNet에서 82.4%의 최고 정확도를 기록하며, 최소 5배 적은 샘플로 새로운 최첨단 결과를 달성했습니다.

## 🎯 주요 포인트

- 1. Neural Architecture Search(NAS)에서 성능 평가의 시간 소모 문제를 해결하기 위해 HyperNAS라는 새로운 신경 예측자 패러다임을 제안합니다.
- 2. HyperNAS는 글로벌 인코딩 스킴과 공유 하이퍼네트워크라는 두 가지 주요 구성 요소로 구성되어 있습니다.
- 3. 글로벌 인코딩 스킴은 전체적인 매크로 구조 정보를 포착하도록 설계되었으며, 공유 하이퍼네트워크는 아키텍처 간 패턴 조사를 강화하는 보조 작업으로 작용합니다.
- 4. 다양한 검색 공간에서의 실험 결과, 특히 few-shot 시나리오에서 HyperNAS의 장점이 입증되었습니다.
- 5. HyperNAS는 CIFAR-10에서 97.60%의 top-1 정확도와 ImageNet에서 82.4%의 top-1 정확도를 기록하며, 최소 5배 적은 샘플을 사용하여 새로운 최첨단 결과를 달성했습니다.


---

*Generated on 2025-09-24 13:39:18*