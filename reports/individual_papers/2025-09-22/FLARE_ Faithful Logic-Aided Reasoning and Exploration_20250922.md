---
keywords:
  - Large Language Model
  - Chain-of-Thought
  - Faithful Chain-of-Thought
  - Logic Programming
  - Multi-hop Search
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2410.11900
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:33:46.551842",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought",
    "Faithful Chain-of-Thought",
    "Logic Programming",
    "Multi-hop Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Chain-of-Thought": 0.82,
    "Faithful Chain-of-Thought": 0.78,
    "Logic Programming": 0.8,
    "Multi-hop Search": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's methodology, linking to a broad technical category.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought",
        "canonical": "Chain-of-Thought",
        "aliases": [
          "CoT"
        ],
        "category": "specific_connectable",
        "rationale": "Key reasoning technique discussed in the paper, relevant for linking reasoning methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Faithful CoT",
        "canonical": "Faithful Chain-of-Thought",
        "aliases": [
          "F-CoT"
        ],
        "category": "unique_technical",
        "rationale": "Unique method proposed in the paper, enhancing reasoning faithfulness.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Logic Programming",
        "canonical": "Logic Programming",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Integral to the proposed method, facilitating logical reasoning connections.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-hop Search",
        "canonical": "Multi-hop Search",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Describes the search strategy used, relevant for linking complex reasoning processes.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Reasoning",
      "Performance"
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
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Chain-of-Thought",
      "resolved_canonical": "Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Faithful CoT",
      "resolved_canonical": "Faithful Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Logic Programming",
      "resolved_canonical": "Logic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-hop Search",
      "resolved_canonical": "Multi-hop Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# FLARE: Faithful Logic-Aided Reasoning and Exploration

**Korean Title:** FLARE: 신뢰할 수 있는 논리 보조 추론 및 탐색

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.11900.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2410.11900](https://arxiv.org/abs/2410.11900)

## 🔗 유사한 논문
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT: Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (85.1% similar)
- [[2025-09-19/ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT: An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (84.7% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (84.6% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (84.3% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Chain-of-Thought|Chain-of-Thought]], [[keywords/Logic Programming|Logic Programming]], [[keywords/Multi-hop Search|Multi-hop Search]]
**⚡ Unique Technical**: [[keywords/Faithful Chain-of-Thought|Faithful Chain-of-Thought]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.11900v5 Announce Type: replace 
Abstract: Modern Question Answering (QA) and Reasoning approaches based on Large Language Models (LLMs) commonly use prompting techniques, such as Chain-of-Thought (CoT), assuming the resulting generation will have a more granular exploration and reasoning over the question space and scope. However, such methods struggle with generating outputs that are faithful to the intermediate chain of reasoning produced by the model. On the other end of the spectrum, neuro-symbolic methods such as Faithful CoT (F-CoT) propose to combine LLMs with external symbolic solvers. While such approaches boast a high degree of faithfulness, they usually require a model trained for code generation and struggle with tasks that are ambiguous or hard to formalise strictly. We introduce $\textbf{F}$aithful $\textbf{L}$ogic-$\textbf{A}$ided $\textbf{R}$easoning and $\textbf{E}$xploration ($\textbf{FLARE}$), a novel interpretable approach for traversing the problem space using task decompositions. We use the LLM to plan a solution, soft-formalise the query into facts and predicates using a logic programming code and simulate that code execution using an exhaustive multi-hop search over the defined space. Our method allows us to compute the faithfulness of the reasoning process w.r.t. the generated code and analyse the steps of the multi-hop search without relying on external solvers. Our methods achieve SOTA results on $\mathbf{7}$ out of $\mathbf{9}$ diverse reasoning benchmarks. We also show that model faithfulness positively correlates with overall performance and further demonstrate that $\textbf{FLARE}$ allows pinpointing the decisive factors sufficient for and leading to the correct answer with optimal reasoning during the multi-hop search.

## 🔍 Abstract (한글 번역)

arXiv:2410.11900v5 발표 유형: 교체  
초록: 대형 언어 모델(LLMs)을 기반으로 한 현대의 질문 응답(QA) 및 추론 접근법은 일반적으로 Chain-of-Thought (CoT)와 같은 프롬프트 기법을 사용하여 질문 공간과 범위에 대한 보다 세분화된 탐색과 추론을 기대합니다. 그러나 이러한 방법은 모델이 생성한 중간 추론 체인에 충실한 출력을 생성하는 데 어려움을 겪습니다. 반면에 Faithful CoT (F-CoT)와 같은 신경-상징적 방법은 LLMs를 외부 상징적 해결자와 결합할 것을 제안합니다. 이러한 접근법은 높은 충실도를 자랑하지만, 보통 코드 생성을 위해 훈련된 모델을 필요로 하며, 모호하거나 엄격하게 형식화하기 어려운 작업에 어려움을 겪습니다. 우리는 문제 공간을 탐색하기 위한 새로운 해석 가능한 접근법인 $\textbf{F}$aithful $\textbf{L}$ogic-$\textbf{A}$ided $\textbf{R}$easoning and $\textbf{E}$xploration ($\textbf{FLARE}$)을 소개합니다. 우리는 LLM을 사용하여 솔루션을 계획하고, 논리 프로그래밍 코드를 사용하여 쿼리를 사실과 술어로 부드럽게 형식화하며, 정의된 공간에 대한 철저한 다중 홉 검색을 통해 해당 코드 실행을 시뮬레이션합니다. 우리의 방법은 외부 해결자에 의존하지 않고 생성된 코드에 대한 추론 과정의 충실도를 계산하고 다중 홉 검색의 단계를 분석할 수 있게 합니다. 우리의 방법은 $\mathbf{9}$개의 다양한 추론 벤치마크 중 $\mathbf{7}$개에서 SOTA 결과를 달성합니다. 또한 모델의 충실도가 전체 성능과 긍정적으로 상관관계가 있음을 보여주고, $\textbf{FLARE}$가 다중 홉 검색 동안 최적의 추론으로 올바른 답변에 충분하고 결정적인 요인을 정확히 찾아낼 수 있음을 추가로 입증합니다.

## 📝 요약

이 논문에서는 대형 언어 모델(LLM) 기반의 현대적 질문 응답(QA) 및 추론 방법의 한계를 극복하기 위해 새로운 접근법인 FLARE를 제안합니다. 기존의 체인 오브 생각(CoT) 기법은 모델이 생성한 중간 추론 과정의 충실도가 낮다는 문제를 가지고 있습니다. FLARE는 LLM을 활용하여 문제를 계획하고, 논리 프로그래밍 코드를 통해 쿼리를 사실과 술어로 부드럽게 형식화한 후, 정의된 공간에서 철저한 멀티홉 검색을 통해 코드 실행을 시뮬레이션합니다. 이를 통해 외부 해결사에 의존하지 않고 추론 과정의 충실도를 평가하고, 멀티홉 검색의 단계를 분석할 수 있습니다. FLARE는 9개의 다양한 추론 벤치마크 중 7개에서 최고 성능을 기록했으며, 모델의 충실도가 전체 성능과 긍정적으로 상관됨을 보여줍니다. 또한, FLARE는 멀티홉 검색 과정에서 최적의 추론을 통해 정답을 도출하는 결정적 요소를 식별할 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. 현대의 대형 언어 모델 기반 질문 응답 및 추론 접근법은 종종 Chain-of-Thought(COT)과 같은 프롬프트 기법을 사용하지만, 중간 추론 과정의 충실성을 보장하는 데 어려움을 겪습니다.
- 2. Faithful CoT(F-CoT)와 같은 신경-기호적 방법은 외부 기호 솔버와 결합하여 높은 충실성을 자랑하지만, 코드 생성에 특화된 모델이 필요하고 모호하거나 엄격하게 형식화하기 어려운 작업에서는 한계를 보입니다.
- 3. FLARE는 문제 공간을 탐색하기 위한 새로운 해석 가능한 접근법으로, 논리 프로그래밍 코드를 사용하여 쿼리를 사실과 술어로 소프트-형식화하고, 정의된 공간에서 철저한 멀티-홉 검색을 통해 코드 실행을 시뮬레이션합니다.
- 4. 우리의 방법은 외부 솔버에 의존하지 않고 생성된 코드에 대한 추론 과정의 충실성을 계산하고 멀티-홉 검색의 단계를 분석할 수 있게 합니다.
- 5. FLARE는 9개의 다양한 추론 벤치마크 중 7개에서 SOTA 결과를 달성했으며, 모델의 충실성이 전체 성능과 긍정적으로 상관관계가 있음을 보여주고, 멀티-홉 검색 중 최적의 추론으로 올바른 답변을 이끌어내는 결정적 요인을 정확히 찾아낼 수 있음을 입증했습니다.


---

*Generated on 2025-09-23 09:33:46*