---
keywords:
  - Bias-Efficient Fine-Tuning
  - Large Language Model
  - Parameter-Efficient Fine-Tuning
  - Bias Terms
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15974
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:24:08.933960",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bias-Efficient Fine-Tuning",
    "Large Language Model",
    "Parameter-Efficient Fine-Tuning",
    "Bias Terms"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bias-Efficient Fine-Tuning": 0.8,
    "Large Language Model": 0.85,
    "Parameter-Efficient Fine-Tuning": 0.78,
    "Bias Terms": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bias-Efficient Fine-Tuning",
        "canonical": "Bias-Efficient Fine-Tuning",
        "aliases": [
          "BEFT"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, crucial for understanding the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's experiments and relevant to a wide range of research in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Parameter-Efficient Fine-Tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "PEFT"
        ],
        "category": "specific_connectable",
        "rationale": "A key concept in the paper, connecting to broader discussions of efficiency in model training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bias Terms",
        "canonical": "Bias Terms",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding bias terms is essential for grasping the fine-tuning process discussed.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
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
      "candidate_surface": "Bias-Efficient Fine-Tuning",
      "resolved_canonical": "Bias-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
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
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Parameter-Efficient Fine-Tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bias Terms",
      "resolved_canonical": "Bias Terms",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# BEFT: Bias-Efficient Fine-Tuning of Language Models

**Korean Title:** BEFT: 언어 모델의 편향 효율적 미세 조정

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15974.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15974](https://arxiv.org/abs/2509.15974)

## 🔗 유사한 논문
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (84.4% similar)
- [[2025-09-22/Sparsity May Be All You Need_ Sparse Random Parameter Adaptation_20250922|Sparsity May Be All You Need: Sparse Random Parameter Adaptation]] (83.3% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (83.1% similar)
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (82.7% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]], [[keywords/Bias Terms|Bias Terms]]
**⚡ Unique Technical**: [[keywords/Bias-Efficient Fine-Tuning|Bias-Efficient Fine-Tuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15974v1 Announce Type: cross 
Abstract: Fine-tuning all-bias-terms stands out among various parameter-efficient fine-tuning (PEFT) techniques, owing to its out-of-the-box usability and competitive performance, especially in low-data regimes. Bias-only fine-tuning has the potential for unprecedented parameter efficiency. However, the link between fine-tuning different bias terms (i.e., bias terms in the query, key, or value projections) and downstream performance remains unclear. The existing approaches, e.g., based on the magnitude of bias change or empirical Fisher information, provide limited guidance for selecting the particular bias term for effective fine-tuning. In this paper, we propose an approach for selecting the bias term to be fine-tuned, forming the foundation of our bias-efficient fine-tuning (BEFT). We extensively evaluate our bias-efficient approach against other bias-selection approaches, across a wide range of large language models (LLMs) spanning encoder-only and decoder-only architectures from 110M to 6.7B parameters. Our results demonstrate the effectiveness and superiority of our bias-efficient approach on diverse downstream tasks, including classification, multiple-choice, and generation tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15974v1 발표 유형: 교차  
초록: 모든 바이어스 항목을 미세 조정하는 것은 다양한 파라미터 효율적 미세 조정(PEFT) 기법 중에서 특히 저데이터 환경에서 즉시 사용 가능성과 경쟁력 있는 성능으로 두드러집니다. 바이어스 전용 미세 조정은 전례 없는 파라미터 효율성을 제공할 잠재력을 가지고 있습니다. 그러나 서로 다른 바이어스 항목(즉, 쿼리, 키, 또는 값 프로젝션의 바이어스 항목)을 미세 조정하는 것과 다운스트림 성능 간의 연결은 여전히 명확하지 않습니다. 기존 접근법, 예를 들어 바이어스 변화의 크기나 경험적 피셔 정보에 기반한 접근법은 효과적인 미세 조정을 위한 특정 바이어스 항목 선택에 대한 제한된 지침을 제공합니다. 본 논문에서는 미세 조정할 바이어스 항목을 선택하는 접근법을 제안하며, 이는 바이어스 효율적 미세 조정(BEFT)의 기초를 형성합니다. 우리는 110M에서 6.7B 파라미터에 이르는 인코더 전용 및 디코더 전용 아키텍처를 포함한 다양한 대형 언어 모델(LLM)을 대상으로 다른 바이어스 선택 접근법과 비교하여 우리의 바이어스 효율적 접근법을 광범위하게 평가합니다. 우리의 결과는 분류, 다지선다, 생성 작업을 포함한 다양한 다운스트림 작업에서 우리의 바이어스 효율적 접근법의 효과성과 우수성을 입증합니다.

## 📝 요약

이 논문은 파라미터 효율적인 미세 조정(PEFT) 기법 중 하나인 모든 바이어스 항목의 미세 조정에 대해 다룹니다. 특히, 데이터가 적은 환경에서 사용하기 쉽고 성능이 뛰어납니다. 그러나 쿼리, 키, 값 프로젝션의 바이어스 항목과 성능 간의 관계는 명확하지 않습니다. 기존 방법들은 특정 바이어스 항목을 선택하는 데 한계가 있습니다. 본 연구에서는 바이어스 항목 선택을 위한 새로운 접근법을 제안하며, 이를 바탕으로 바이어스 효율적 미세 조정(BEFT)을 개발했습니다. 다양한 대형 언어 모델(LLM)에서 이 접근법의 효과를 검증한 결과, 분류, 선택형, 생성 작업 등 다양한 다운스트림 작업에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 모든 바이어스 항목을 미세 조정하는 방법은 낮은 데이터 환경에서 경쟁력 있는 성능을 보여주는 파라미터 효율적인 미세 조정 기법 중 하나입니다.
- 2. 바이어스 항목만을 미세 조정하는 것은 전례 없는 파라미터 효율성을 제공할 잠재력을 가지고 있습니다.
- 3. 본 논문에서는 효과적인 미세 조정을 위한 특정 바이어스 항목 선택을 위한 접근법을 제안하며, 이를 바이어스 효율적 미세 조정(BEFT)의 기초로 삼습니다.
- 4. 제안된 바이어스 효율적 접근법은 다양한 대형 언어 모델(LLM)에서 다른 바이어스 선택 접근법과 비교 평가되었으며, 다양한 다운스트림 작업에서 효과적이고 우수한 성능을 입증했습니다.


---

*Generated on 2025-09-23 09:24:08*