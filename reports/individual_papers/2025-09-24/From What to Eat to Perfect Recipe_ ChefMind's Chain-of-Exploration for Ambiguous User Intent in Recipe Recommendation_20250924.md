<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:23:35.623296",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Chain of Exploration",
    "Knowledge Graph",
    "Retrieval Augmented Generation",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Chain of Exploration": 0.78,
    "Knowledge Graph": 0.85,
    "Retrieval Augmented Generation": 0.82,
    "Large Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Chain of Exploration",
        "canonical": "Chain of Exploration",
        "aliases": [
          "CoE"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and is likely unique to this research, providing a novel method for refining ambiguous queries.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Knowledge Graph",
        "canonical": "Knowledge Graph",
        "aliases": [
          "KG"
        ],
        "category": "broad_technical",
        "rationale": "Knowledge Graphs are widely used for semantic reasoning, making them a strong link to related research in data representation and reasoning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending technique that enhances the generation of contextually relevant information, linking to recent advancements in AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are foundational in modern AI research, providing a broad technical link to numerous studies in natural language processing.",
        "novelty_score": 0.3,
        "connectivity_score": 0.95,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "fuzzy user intent",
      "semantic accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Chain of Exploration",
      "resolved_canonical": "Chain of Exploration",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Knowledge Graph",
      "resolved_canonical": "Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.95,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# From "What to Eat?" to Perfect Recipe: ChefMind's Chain-of-Exploration for Ambiguous User Intent in Recipe Recommendation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18226.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18226](https://arxiv.org/abs/2509.18226)

## 🔗 유사한 논문
- [[2025-09-19/Deep Learning-Driven Multimodal Detection and Movement Analysis of Objects in Culinary_20250919|Deep Learning-Driven Multimodal Detection and Movement Analysis of Objects in Culinary]] (81.0% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (80.4% similar)
- [[2025-09-23/SeqUDA-Rec_ Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation for Personalized Content Marketing_20250923|SeqUDA-Rec: Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation for Personalized Content Marketing]] (80.2% similar)
- [[2025-09-23/MCP_ A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models_20250923|MCP: A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models]] (80.0% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Knowledge Graph|Knowledge Graph]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Chain of Exploration|Chain of Exploration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18226v1 Announce Type: new 
Abstract: Personalized recipe recommendation faces challenges in handling fuzzy user intent, ensuring semantic accuracy, and providing sufficient detail coverage. We propose ChefMind, a hybrid architecture combining Chain of Exploration (CoE), Knowledge Graph (KG), Retrieval-Augmented Generation (RAG), and a Large Language Model (LLM). CoE refines ambiguous queries into structured conditions, KG offers semantic reasoning and interpretability, RAG supplements contextual culinary details, and LLM integrates outputs into coherent recommendations. We evaluate ChefMind on the Xiachufang dataset and manually annotated queries, comparing it with LLM-only, KG-only, and RAG-only baselines. Results show that ChefMind achieves superior performance in accuracy, relevance, completeness, and clarity, with an average score of 8.7 versus 6.4-6.7 for ablation models. Moreover, it reduces unprocessed queries to 1.6%, demonstrating robustness in handling fuzzy demands.

## 📝 요약

개인화된 레시피 추천의 문제점을 해결하기 위해 ChefMind라는 하이브리드 아키텍처를 제안합니다. ChefMind는 탐색 체인(CoE), 지식 그래프(KG), 검색 증강 생성(RAG), 대형 언어 모델(LLM)을 결합하여 모호한 사용자 의도를 구조화하고, 의미론적 추론을 제공하며, 요리 관련 세부 정보를 보완합니다. Xiachufang 데이터셋과 수작업으로 주석된 쿼리를 사용한 평가에서 ChefMind는 정확성, 관련성, 완전성, 명확성에서 평균 8.7점을 기록하며 다른 모델보다 우수한 성능을 보였습니다. 또한, 처리되지 않은 쿼리를 1.6%로 줄여 모호한 요구를 효과적으로 처리하는 강건성을 입증했습니다.

## 🎯 주요 포인트

- 1. ChefMind는 모호한 사용자 의도를 구조화된 조건으로 정제하는 Chain of Exploration(CoE)을 포함한 하이브리드 아키텍처입니다.
- 2. ChefMind는 지식 그래프(KG)를 통해 의미론적 추론과 해석 가능성을 제공합니다.
- 3. Retrieval-Augmented Generation(RAG)은 요리 관련 문맥적 세부사항을 보완하며, 대형 언어 모델(LLM)은 이를 일관된 추천으로 통합합니다.
- 4. Xiachufang 데이터셋과 수작업으로 주석된 쿼리 평가 결과, ChefMind는 정확성, 관련성, 완전성, 명확성에서 평균 점수 8.7을 기록하며 우수한 성능을 보였습니다.
- 5. ChefMind는 처리되지 않은 쿼리를 1.6%로 줄여 모호한 요구를 처리하는 데 있어 강력한 성능을 입증했습니다.


---

*Generated on 2025-09-24 13:23:35*