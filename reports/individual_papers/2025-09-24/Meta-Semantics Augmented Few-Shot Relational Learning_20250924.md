<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:19:51.233470",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Knowledge Graph",
    "Meta-Semantics",
    "Meta-Learning",
    "PromptMeta"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.82,
    "Knowledge Graph": 0.85,
    "Meta-Semantics": 0.78,
    "Meta-Learning": 0.8,
    "PromptMeta": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Few-Shot Relational Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot Relation Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of few-shot learning, which is crucial for understanding the paper's focus on learning with limited examples.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Knowledge Graph",
        "canonical": "Knowledge Graph",
        "aliases": [
          "KG"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's methodology and connects with existing work on graph-based learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Meta-Semantics",
        "canonical": "Meta-Semantics",
        "aliases": [
          "Meta Semantic"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept that is essential for understanding the proposed framework.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.83,
        "link_intent_score": 0.78
      },
      {
        "surface": "Meta-Learning Framework",
        "canonical": "Meta-Learning",
        "aliases": [
          "Meta Learning Framework"
        ],
        "category": "broad_technical",
        "rationale": "Provides a broad technical context for the paper's approach, linking it to the meta-learning domain.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "PromptMeta",
        "canonical": "PromptMeta",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents the specific framework introduced by the authors, crucial for understanding the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "reasoning",
      "training examples",
      "limited supervision"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Few-Shot Relational Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Knowledge Graph",
      "resolved_canonical": "Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Meta-Semantics",
      "resolved_canonical": "Meta-Semantics",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.83,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Meta-Learning Framework",
      "resolved_canonical": "Meta-Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "PromptMeta",
      "resolved_canonical": "PromptMeta",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Meta-Semantics Augmented Few-Shot Relational Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.05684.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.05684](https://arxiv.org/abs/2505.05684)

## 🔗 유사한 논문
- [[2025-09-22/RACap_ Relation-Aware Prompting for Lightweight Retrieval-Augmented Image Captioning_20250922|RACap: Relation-Aware Prompting for Lightweight Retrieval-Augmented Image Captioning]] (81.5% similar)
- [[2025-09-23/MetaEmbed_ Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction_20250923|MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction]] (81.3% similar)
- [[2025-09-23/Learning to Learn with Contrastive Meta-Objective_20250923|Learning to Learn with Contrastive Meta-Objective]] (80.9% similar)
- [[2025-09-22/SEMMA_ A Semantic Aware Knowledge Graph Foundation Model_20250922|SEMMA: A Semantic Aware Knowledge Graph Foundation Model]] (80.4% similar)
- [[2025-09-23/Guiding Cross-Modal Representations with MLLM Priors via Preference Alignment_20250923|Guiding Cross-Modal Representations with MLLM Priors via Preference Alignment]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Meta-Learning|Meta-Learning]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]], [[keywords/Knowledge Graph|Knowledge Graph]]
**⚡ Unique Technical**: [[keywords/Meta-Semantics|Meta-Semantics]], [[keywords/PromptMeta|PromptMeta]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.05684v3 Announce Type: replace 
Abstract: Few-shot relational learning on knowledge graph (KGs) aims to perform reasoning over relations with only a few training examples. While current methods have focused primarily on leveraging specific relational information, rich semantics inherent in KGs have been largely overlooked. To bridge this gap, we propose PromptMeta, a novel prompted meta-learning framework that seamlessly integrates meta-semantics with relational information for few-shot relational learning. PromptMeta introduces two core innovations: (1) a Meta-Semantic Prompt (MSP) pool that learns and consolidates high-level meta-semantics shared across tasks, enabling effective knowledge transfer and adaptation to newly emerging relations; and (2) a learnable fusion mechanism that dynamically combines meta-semantics with task-specific relational information tailored to different few-shot tasks. Both components are optimized jointly with model parameters within a meta-learning framework. Extensive experiments and analyses on two real-world KG benchmarks validate the effectiveness of PromptMeta in adapting to new relations with limited supervision.

## 📝 요약

PromptMeta는 지식 그래프에서 소수의 예시만으로 관계 추론을 수행하는 few-shot relational learning을 위한 새로운 프롬프트 기반 메타 학습 프레임워크입니다. 이 연구는 기존 방법들이 간과한 풍부한 의미론을 활용하여 메타-의미론과 관계 정보를 통합합니다. 주요 기여는 (1) 다양한 작업에 걸쳐 공유되는 고수준 메타-의미론을 학습하고 통합하는 Meta-Semantic Prompt(MSP) 풀을 도입하여 효과적인 지식 전이와 새로운 관계에 대한 적응을 가능하게 하고, (2) 메타-의미론과 작업별 관계 정보를 동적으로 결합하는 학습 가능한 융합 메커니즘을 제안한 것입니다. 이 두 구성 요소는 메타 학습 프레임워크 내에서 모델 매개변수와 함께 최적화됩니다. 두 개의 실제 지식 그래프 벤치마크에서의 실험은 PromptMeta가 제한된 감독 하에서도 새로운 관계에 효과적으로 적응할 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. PromptMeta는 메타-시맨틱과 관계 정보를 통합하여 소수 샷 관계 학습을 수행하는 새로운 프레임워크입니다.
- 2. 메타-시맨틱 프롬프트(MSP) 풀을 도입하여 과제 간 공유되는 고수준의 메타-시맨틱을 학습하고 통합합니다.
- 3. 학습 가능한 융합 메커니즘을 통해 메타-시맨틱과 과제별 관계 정보를 동적으로 결합합니다.
- 4. 두 가지 핵심 구성 요소는 메타-학습 프레임워크 내에서 모델 파라미터와 함께 최적화됩니다.
- 5. 두 가지 실제 KG 벤치마크에서의 실험 결과, PromptMeta는 제한된 감독 하에 새로운 관계에 적응하는 데 효과적임을 입증했습니다.


---

*Generated on 2025-09-24 14:19:51*