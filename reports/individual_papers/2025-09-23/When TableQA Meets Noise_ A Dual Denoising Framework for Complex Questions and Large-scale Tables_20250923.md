---
keywords:
  - Table Question Answering
  - Large Language Model
  - Relevance Filtering
  - Table Pruning
  - Evidence-based Question Denoising
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17680
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:31:45.399130",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Table Question Answering",
    "Large Language Model",
    "Relevance Filtering",
    "Table Pruning",
    "Evidence-based Question Denoising"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Table Question Answering": 0.78,
    "Large Language Model": 0.8,
    "Relevance Filtering": 0.75,
    "Table Pruning": 0.77,
    "Evidence-based Question Denoising": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Table Question Answering",
        "canonical": "Table Question Answering",
        "aliases": [
          "TableQA"
        ],
        "category": "unique_technical",
        "rationale": "Table Question Answering is a specific task in NLP that involves reasoning over structured data, which is central to the paper's contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are crucial for reasoning capabilities, which are a key focus of the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Relevance Filtering",
        "canonical": "Relevance Filtering",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Relevance Filtering is a novel approach introduced in the paper to improve reasoning by identifying essential information.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Table Pruning",
        "canonical": "Table Pruning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Table Pruning is a specific method proposed to manage large-scale tables, enhancing the paper's contribution to TableQA.",
        "novelty_score": 0.7,
        "connectivity_score": 0.62,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Evidence-based Question Denoising",
        "canonical": "Evidence-based Question Denoising",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is a key innovation of the paper, focusing on decomposing and filtering questions for better reasoning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.58,
        "specificity_score": 0.83,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "framework",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Table Question Answering",
      "resolved_canonical": "Table Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Relevance Filtering",
      "resolved_canonical": "Relevance Filtering",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Table Pruning",
      "resolved_canonical": "Table Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.62,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Evidence-based Question Denoising",
      "resolved_canonical": "Evidence-based Question Denoising",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.58,
        "specificity": 0.83,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# When TableQA Meets Noise: A Dual Denoising Framework for Complex Questions and Large-scale Tables

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17680.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17680](https://arxiv.org/abs/2509.17680)

## 🔗 유사한 논문
- [[2025-09-23/Can GRPO Boost Complex Multimodal Table Understanding?_20250923|Can GRPO Boost Complex Multimodal Table Understanding?]] (82.1% similar)
- [[2025-09-19/TableDART_ Dynamic Adaptive Multi-Modal Routing for Table Understanding_20250919|TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (81.3% similar)
- [[2025-09-23/Improving Deep Tabular Learning_20250923|Improving Deep Tabular Learning]] (79.7% similar)
- [[2025-09-23/Beyond Prompting_ An Efficient Embedding Framework for Open-Domain Question Answering_20250923|Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering]] (79.7% similar)
- [[2025-09-23/Table2LaTeX-RL_ High-Fidelity LaTeX Code Generation from Table Images via Reinforced Multimodal Language Models_20250923|Table2LaTeX-RL: High-Fidelity LaTeX Code Generation from Table Images via Reinforced Multimodal Language Models]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Table Question Answering|Table Question Answering]], [[keywords/Relevance Filtering|Relevance Filtering]], [[keywords/Table Pruning|Table Pruning]], [[keywords/Evidence-based Question Denoising|Evidence-based Question Denoising]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17680v1 Announce Type: new 
Abstract: Table question answering (TableQA) is a fundamental task in natural language processing (NLP). The strong reasoning capabilities of large language models (LLMs) have brought significant advances in this field. However, as real-world applications involve increasingly complex questions and larger tables, substantial noisy data is introduced, which severely degrades reasoning performance. To address this challenge, we focus on improving two core capabilities: Relevance Filtering, which identifies and retains information truly relevant to reasoning, and Table Pruning, which reduces table size while preserving essential content. Based on these principles, we propose EnoTab, a dual denoising framework for complex questions and large-scale tables. Specifically, we first perform Evidence-based Question Denoising by decomposing the question into minimal semantic units and filtering out those irrelevant to answer reasoning based on consistency and usability criteria. Then, we propose Evidence Tree-guided Table Denoising, which constructs an explicit and transparent table pruning path to remove irrelevant data step by step. At each pruning step, we observe the intermediate state of the table and apply a post-order node rollback mechanism to handle abnormal table states, ultimately producing a highly reliable sub-table for final answer reasoning. Finally, extensive experiments show that EnoTab achieves outstanding performance on TableQA tasks with complex questions and large-scale tables, confirming its effectiveness.

## 📝 요약

TableQA는 자연어 처리의 중요한 과제로, 대형 언어 모델(LLM)의 강력한 추론 능력 덕분에 큰 발전을 이루었습니다. 그러나 복잡한 질문과 대규모 테이블이 포함된 실제 응용에서는 많은 잡음 데이터가 발생해 성능이 저하됩니다. 이를 해결하기 위해, 우리는 관련성 필터링과 테이블 가지치기라는 두 가지 핵심 능력을 개선하고자 합니다. 이를 바탕으로, 복잡한 질문과 대규모 테이블에 대한 이중 노이즈 제거 프레임워크인 EnoTab을 제안합니다. 먼저, 질문을 최소 의미 단위로 분해하고 불필요한 부분을 제거하는 증거 기반 질문 노이즈 제거를 수행합니다. 이후, 명시적 테이블 가지치기 경로를 구축하여 불필요한 데이터를 단계적으로 제거하는 증거 트리 기반 테이블 노이즈 제거를 제안합니다. 실험 결과, EnoTab은 복잡한 질문과 대규모 테이블에서 뛰어난 성능을 보여 그 효과성을 입증했습니다.

## 🎯 주요 포인트

- 1. TableQA는 자연어 처리 분야에서 중요한 과제로, 대형 언어 모델의 강력한 추론 능력이 이 분야의 발전을 이끌고 있습니다.
- 2. 실제 응용에서는 복잡한 질문과 대규모 테이블로 인해 많은 잡음 데이터가 발생하여 추론 성능이 저하됩니다.
- 3. EnoTab은 복잡한 질문과 대규모 테이블을 위한 이중 잡음 제거 프레임워크로, 관련성 필터링과 테이블 가지치기를 통해 성능을 향상시킵니다.
- 4. 증거 기반 질문 잡음 제거와 증거 트리 기반 테이블 잡음 제거를 통해 불필요한 데이터를 단계적으로 제거하여 신뢰성 높은 서브 테이블을 생성합니다.
- 5. 광범위한 실험 결과, EnoTab은 복잡한 질문과 대규모 테이블을 포함한 TableQA 작업에서 뛰어난 성능을 보였습니다.


---

*Generated on 2025-09-24 03:31:45*