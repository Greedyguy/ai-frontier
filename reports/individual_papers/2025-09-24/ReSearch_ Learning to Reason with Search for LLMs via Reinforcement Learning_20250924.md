<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:19:17.895009",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning",
    "Reasoning with Search",
    "Reflection and Self-correction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Reinforcement Learning": 0.78,
    "Reasoning with Search": 0.72,
    "Reflection and Self-correction": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's framework and connect with broader AI research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "specific_connectable",
        "rationale": "Reinforcement Learning is a key methodology used in the paper, linking it to a wide range of AI applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reasoning with Search",
        "canonical": "Reasoning with Search",
        "aliases": [
          "Search-based Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced by the paper, highlighting its unique contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Reflection and Self-correction",
        "canonical": "Reflection and Self-correction",
        "aliases": [
          "Self-reflection",
          "Self-correction"
        ],
        "category": "evolved_concepts",
        "rationale": "These advanced reasoning capabilities are emergent properties of the proposed framework.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reasoning with Search",
      "resolved_canonical": "Reasoning with Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Reflection and Self-correction",
      "resolved_canonical": "Reflection and Self-correction",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.19470.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2503.19470](https://arxiv.org/abs/2503.19470)

## 🔗 유사한 논문
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (88.3% similar)
- [[2025-09-23/Open Vision Reasoner_ Transferring Linguistic Cognitive Behavior for Visual Reasoning_20250923|Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning]] (87.5% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (87.5% similar)
- [[2025-09-23/UR$^2$_ Unify RAG and Reasoning through Reinforcement Learning_20250923|UR$^2$: Unify RAG and Reasoning through Reinforcement Learning]] (87.0% similar)
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (86.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Reasoning with Search|Reasoning with Search]]
**🚀 Evolved Concepts**: [[keywords/Reflection and Self-correction|Reflection and Self-correction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.19470v3 Announce Type: replace 
Abstract: Large Language Models (LLMs) have shown remarkable capabilities in reasoning, exemplified by the success of OpenAI-o1 and DeepSeek-R1. However, integrating reasoning with external search processes remains challenging, especially for complex multi-hop questions requiring multiple retrieval steps. We propose ReSearch, a novel framework that trains LLMs to Reason with Search via reinforcement learning without using any supervised data on reasoning steps. Our approach treats search operations as integral components of the reasoning chain, where when and how to perform searches is guided by text-based thinking, and search results subsequently influence further reasoning. We train ReSearch on Qwen2.5-7B(-Instruct) and Qwen2.5-32B(-Instruct) models and conduct extensive experiments. Despite being trained on only one dataset, our models demonstrate strong generalizability across various benchmarks. Analysis reveals that ReSearch naturally elicits advanced reasoning capabilities such as reflection and self-correction during the reinforcement learning process.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 외부 검색 과정과의 통합 문제를 해결하기 위해 ReSearch라는 새로운 프레임워크를 제안합니다. ReSearch는 강화 학습을 통해 지도 데이터 없이 LLM이 검색을 활용하여 추론하도록 훈련합니다. 검색 작업을 추론의 필수 요소로 간주하며, 텍스트 기반 사고에 따라 검색을 수행하고 그 결과가 추가 추론에 영향을 미치도록 합니다. Qwen2.5-7B(-Instruct) 및 Qwen2.5-32B(-Instruct) 모델로 실험한 결과, 단일 데이터셋으로 훈련했음에도 다양한 벤치마크에서 강력한 일반화 성능을 보였습니다. 분석 결과, ReSearch는 강화 학습 과정에서 반성 및 자기 수정과 같은 고급 추론 능력을 자연스럽게 유도함을 확인했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 복잡한 다중 단계 질문에 대한 외부 검색 과정과의 통합이 어려운 문제를 안고 있다.
- 2. ReSearch는 검색을 통한 추론을 강화 학습으로 훈련하는 새로운 프레임워크로, 지도 데이터 없이도 추론 단계를 수행한다.
- 3. ReSearch는 검색 작업을 추론 체인의 필수 구성 요소로 간주하며, 텍스트 기반 사고에 따라 검색 시점과 방법을 결정한다.
- 4. Qwen2.5-7B(-Instruct) 및 Qwen2.5-32B(-Instruct) 모델을 통해 실험한 결과, 단일 데이터셋으로 훈련했음에도 다양한 벤치마크에서 높은 일반화 성능을 보였다.
- 5. 분석 결과, ReSearch는 강화 학습 과정에서 반성 및 자기 수정과 같은 고급 추론 능력을 자연스럽게 유도한다.


---

*Generated on 2025-09-24 14:19:17*