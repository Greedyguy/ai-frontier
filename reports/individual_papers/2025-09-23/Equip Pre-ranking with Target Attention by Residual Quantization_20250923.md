---
keywords:
  - Attention Mechanism
  - Residual Quantization
  - Pre-ranking Framework
  - Generative Models
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16931
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:38:24.310564",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Residual Quantization",
    "Pre-ranking Framework",
    "Generative Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.85,
    "Residual Quantization": 0.78,
    "Pre-ranking Framework": 0.72,
    "Generative Models": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Target Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "TA"
        ],
        "category": "specific_connectable",
        "rationale": "Target Attention is a specific application of the Attention Mechanism, which is crucial for linking complex feature interactions in recommendation systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Residual Quantization",
        "canonical": "Residual Quantization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Residual Quantization is a novel technique proposed in the paper, enabling efficient pre-ranking with high accuracy, thus offering strong linking potential.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pre-ranking Framework",
        "canonical": "Pre-ranking Framework",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The pre-ranking framework is a unique concept introduced in the paper, crucial for understanding the proposed system's architecture.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Generative Models",
        "canonical": "Generative Models",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Generative models inspire the proposed framework, providing a broad technical context for linking related concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.5,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "efficiency",
      "effectiveness",
      "performance bottleneck",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Target Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Residual Quantization",
      "resolved_canonical": "Residual Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pre-ranking Framework",
      "resolved_canonical": "Pre-ranking Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Generative Models",
      "resolved_canonical": "Generative Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.5,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Equip Pre-ranking with Target Attention by Residual Quantization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16931.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16931](https://arxiv.org/abs/2509.16931)

## 🔗 유사한 논문
- [[2025-09-22/Database-Augmented Query Representation for Information Retrieval_20250922|Database-Augmented Query Representation for Information Retrieval]] (78.2% similar)
- [[2025-09-22/BiRQ_ Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition_20250922|BiRQ: Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition]] (78.2% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (78.0% similar)
- [[2025-09-22/Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings_20250922|Optimizing Product Deduplication in E-Commerce with Multimodal Embeddings]] (78.0% similar)
- [[2025-09-19/Chain-of-Thought Re-ranking for Image Retrieval Tasks_20250919|Chain-of-Thought Re-ranking for Image Retrieval Tasks]] (77.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generative Models|Generative Models]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Residual Quantization|Residual Quantization]], [[keywords/Pre-ranking Framework|Pre-ranking Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16931v1 Announce Type: cross 
Abstract: The pre-ranking stage in industrial recommendation systems faces a fundamental conflict between efficiency and effectiveness. While powerful models like Target Attention (TA) excel at capturing complex feature interactions in the ranking stage, their high computational cost makes them infeasible for pre-ranking, which often relies on simplistic vector-product models. This disparity creates a significant performance bottleneck for the entire system. To bridge this gap, we propose TARQ, a novel pre-ranking framework. Inspired by generative models, TARQ's key innovation is to equip pre-ranking with an architecture approximate to TA by Residual Quantization. This allows us to bring the modeling power of TA into the latency-critical pre-ranking stage for the first time, establishing a new state-of-the-art trade-off between accuracy and efficiency. Extensive offline experiments and large-scale online A/B tests at Taobao demonstrate TARQ's significant improvements in ranking performance. Consequently, our model has been fully deployed in production, serving tens of millions of daily active users and yielding substantial business improvements.

## 📝 요약

산업 추천 시스템의 사전 순위 단계는 효율성과 효과성 간의 근본적인 갈등을 겪습니다. 강력한 모델인 Target Attention(TA)은 복잡한 특징 상호작용을 잘 포착하지만, 높은 계산 비용으로 인해 사전 순위 단계에서는 사용이 어렵습니다. 이를 해결하기 위해, 우리는 TARQ라는 새로운 사전 순위 프레임워크를 제안합니다. TARQ는 생성 모델에서 영감을 받아 잔여 양자화를 통해 TA와 유사한 구조를 사전 순위에 도입합니다. 이를 통해 정확성과 효율성 간의 새로운 최적 균형을 달성했습니다. Taobao에서의 대규모 온라인 A/B 테스트와 오프라인 실험을 통해 TARQ의 성능 향상을 입증했으며, 현재 수천만 명의 일일 활성 사용자에게 적용되어 비즈니스 성과를 개선하고 있습니다.

## 🎯 주요 포인트

- 1. 산업 추천 시스템의 사전 순위 단계는 효율성과 효과성 간의 근본적인 갈등을 겪고 있습니다.
- 2. TARQ는 Residual Quantization을 통해 Target Attention(TA)의 모델링 능력을 사전 순위 단계에 도입하는 새로운 프레임워크입니다.
- 3. TARQ는 정확성과 효율성 간의 새로운 최첨단 균형을 확립하여 성능 병목 현상을 해결합니다.
- 4. Taobao에서의 대규모 온라인 A/B 테스트와 오프라인 실험을 통해 TARQ의 성능 향상이 입증되었습니다.
- 5. TARQ 모델은 생산 환경에 완전히 배포되어 수천만 명의 일일 활성 사용자에게 서비스를 제공하며 상당한 비즈니스 개선을 이루었습니다.


---

*Generated on 2025-09-23 23:38:24*