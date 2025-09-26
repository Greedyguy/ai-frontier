---
keywords:
  - Large Language Model
  - Embedding Alignment
  - Model Editing
  - Transformer
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.11876
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:54:43.611958",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Embedding Alignment",
    "Model Editing",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Embedding Alignment": 0.78,
    "Model Editing": 0.8,
    "Transformer": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "large-scale language models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus, linking to a widely discussed topic in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Embedding Alignment",
        "canonical": "Embedding Alignment",
        "aliases": [
          "embedding space alignment"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to improve model editing reliability.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Model Editing",
        "canonical": "Model Editing",
        "aliases": [
          "knowledge update",
          "model update"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for modifying LLMs, relevant to ongoing research in model adaptability.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformers",
        "canonical": "Transformer",
        "aliases": [
          "transformer models"
        ],
        "category": "broad_technical",
        "rationale": "Essential architecture for LLMs, facilitating connections across NLP research.",
        "novelty_score": 0.2,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "robust",
      "efficacy",
      "metrics"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Embedding Alignment",
      "resolved_canonical": "Embedding Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Model Editing",
      "resolved_canonical": "Model Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# EAMET: Robust Massive Model Editing via Embedding Alignment Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11876.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.11876](https://arxiv.org/abs/2505.11876)

## 🔗 유사한 논문
- [[2025-09-22/DualEdit_ Dual Editing for Knowledge Updating in Vision-Language Models_20250922|DualEdit: Dual Editing for Knowledge Updating in Vision-Language Models]] (86.5% similar)
- [[2025-09-23/WikiBigEdit_ Understanding the Limits of Lifelong Knowledge Editing in LLMs_20250923|WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs]] (86.1% similar)
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (85.3% similar)
- [[2025-09-23/Diagnosing Model Editing via Knowledge Spectrum_20250923|Diagnosing Model Editing via Knowledge Spectrum]] (84.6% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Model Editing|Model Editing]]
**⚡ Unique Technical**: [[keywords/Embedding Alignment|Embedding Alignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11876v2 Announce Type: replace 
Abstract: Model editing techniques are essential for efficiently updating knowledge in large language models (LLMs). However, the effectiveness of existing approaches degrades in massive editing scenarios, particularly when evaluated with practical metrics. Their robustness is also limited in context-rich settings or when editing multiple facts of the same subject simultaneously. We attribute these failures to the embedding misalignment among knowledge items, which undermines editing reliability at scale. To address this, we propose EAMET (Embedding Alignment Model Editing in Transformers), which addresses this issue by aligning the space of key and residual embeddings. Extensive experiments across six LLMs and three datasets demonstrate that EAMET consistently outperforms existing methods, achieving about 90\% editing efficacy when editing 10k facts. Codes and datasets are publicly available at https://ybdai7.github.io/eamet-page/.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)에서 지식을 효율적으로 업데이트하기 위한 모델 편집 기술의 한계를 지적하고, 이를 개선하기 위한 새로운 방법론인 EAMET을 제안합니다. 기존 방법들은 대규모 편집 시나리오에서 효과가 떨어지며, 특히 여러 사실을 동시에 편집할 때의 강건성이 부족합니다. 이러한 문제의 원인은 지식 항목 간 임베딩 불일치에 있다고 보고, EAMET은 키와 잔여 임베딩 공간을 정렬하여 이를 해결합니다. 여섯 개의 LLM과 세 개의 데이터셋을 활용한 실험 결과, EAMET은 기존 방법들보다 우수한 성능을 보이며, 10,000개의 사실을 편집할 때 약 90%의 편집 효율성을 달성했습니다. 코드와 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)에서 지식을 효율적으로 업데이트하기 위해 모델 편집 기술이 필수적이다.
- 2. 기존 방법들은 대규모 편집 시나리오에서 효과가 떨어지며, 특히 실용적인 지표로 평가할 때 더욱 그렇다.
- 3. EAMET은 키 및 잔여 임베딩 공간을 정렬하여 임베딩 불일치를 해결하고, 대규모 편집의 신뢰성을 높인다.
- 4. EAMET은 여섯 개의 LLM과 세 개의 데이터셋에 걸친 실험에서 기존 방법을 능가하며, 10,000개의 사실을 편집할 때 약 90%의 편집 효율성을 달성한다.
- 5. EAMET의 코드와 데이터셋은 공개되어 있다.


---

*Generated on 2025-09-24 03:54:43*