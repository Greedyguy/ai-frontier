<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:37:32.784818",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Large Language Model",
    "Proximal Policy Optimization",
    "Multi-Agent Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.85,
    "Large Language Model": 0.8,
    "Proximal Policy Optimization": 0.82,
    "Multi-Agent Framework": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a key concept in the paper, focusing on enhancing LLMs with external knowledge, which is crucial for linking related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the study and provide a broad technical foundation for linking with other NLP research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "specific_connectable",
        "rationale": "PPO is a specific reinforcement learning technique used in the framework, linking it to other works in machine learning optimization.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-Agent Framework",
        "canonical": "Multi-Agent Framework",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The framework is a novel approach introduced in the paper, providing a unique angle for linking with multi-agent system research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "retriever",
      "generator",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-Agent Framework",
      "resolved_canonical": "Multi-Agent Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# SIRAG: Towards Stable and Interpretable RAG with A Process-Supervised Multi-Agent Framework

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18167.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18167](https://arxiv.org/abs/2509.18167)

## 🔗 유사한 논문
- [[2025-09-24/RAG+_ Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning_20250924|RAG+: Enhancing Retrieval-Augmented Generation with Application-Aware Reasoning]] (92.0% similar)
- [[2025-09-23/GRIL_ Knowledge Graph Retrieval-Integrated Learning with Large Language Models_20250923|GRIL: Knowledge Graph Retrieval-Integrated Learning with Large Language Models]] (91.6% similar)
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (90.9% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (90.2% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (89.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]]
**⚡ Unique Technical**: [[keywords/Multi-Agent Framework|Multi-Agent Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18167v1 Announce Type: new 
Abstract: Retrieval-Augmented Generation (RAG) enables large language models (LLMs) to access external knowledge sources, but the effectiveness of RAG relies on the coordination between the retriever and the generator. Since these components are developed independently, their interaction is often suboptimal: the retriever may return irrelevant or redundant documents, while the generator may fail to fully leverage retrieved evidence. In this work, we propose a process-supervised multi-agent framework to bridge the gap between retriever and generator. The framework introduces two lightweight agents: a Decision Maker, which determines when to continue retrieval or stop for answer generation, and a Knowledge Selector, which filters retrieved documents to retain only the most useful evidence. To provide fine-grained supervision, we employ an LLM-as-a-Judge that evaluates each intermediate action with process-level rewards, ensuring more accurate credit assignment than relying solely on final answer correctness. We further adopt a tree-structured rollout strategy to explore diverse reasoning paths, and train both agents with Proximal Policy Optimization (PPO) in an end-to-end manner. Experiments on single-hop and multi-hop question answering benchmarks show that our approach achieves higher accuracy, more stable convergence, and produces more interpretable reasoning trajectories compared with standard RAG baselines. Importantly, the proposed framework is modular and plug-and-play, requiring no modification to the retriever or generator, making it practical for real-world RAG applications.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)이 외부 지식에 접근할 수 있도록 하는 Retrieval-Augmented Generation (RAG)의 효과를 개선하기 위해, 프로세스 감독 다중 에이전트 프레임워크를 제안합니다. 이 프레임워크는 두 개의 경량 에이전트를 도입하여, 검색기와 생성기 간의 비효율적인 상호작용을 해결합니다. '의사 결정자'는 검색을 계속할지 답변 생성을 시작할지를 결정하고, '지식 선택자'는 검색된 문서 중 가장 유용한 증거만을 남깁니다. LLM을 판사로 활용하여 각 중간 행동을 평가하고, 세부적인 보상을 제공함으로써 더 정확한 신용 할당을 보장합니다. 또한, 다양한 추론 경로를 탐색하기 위해 트리 구조의 롤아웃 전략을 채택하고, Proximal Policy Optimization (PPO)을 사용하여 두 에이전트를 종단 간 학습합니다. 실험 결과, 제안된 방법은 단일 및 다중 홉 질문 응답 벤치마크에서 더 높은 정확도와 안정적인 수렴성을 보이며, 기존 RAG보다 해석 가능한 추론 경로를 제공합니다. 이 프레임워크는 모듈형으로, 검색기나 생성기를 수정할 필요가 없어 실제 RAG 응용에 실용적입니다.

## 🎯 주요 포인트

- 1. Retrieval-Augmented Generation (RAG)의 효과는 검색기와 생성기 간의 조정에 달려 있으며, 이들의 상호작용은 종종 최적이 아니다.
- 2. 본 연구에서는 검색기와 생성기 간의 격차를 해소하기 위해 프로세스 감독 다중 에이전트 프레임워크를 제안한다.
- 3. 제안된 프레임워크는 경량 에이전트인 의사결정자와 지식 선택자를 도입하여 검색 및 생성 과정의 효율성을 높인다.
- 4. LLM-as-a-Judge를 활용하여 각 중간 행동을 평가하고, 프로세스 수준의 보상을 통해 보다 정확한 신용 할당을 보장한다.
- 5. 제안된 프레임워크는 모듈식이며, 검색기나 생성기를 수정할 필요가 없어 실제 RAG 응용에 실용적이다.


---

*Generated on 2025-09-24 15:37:32*