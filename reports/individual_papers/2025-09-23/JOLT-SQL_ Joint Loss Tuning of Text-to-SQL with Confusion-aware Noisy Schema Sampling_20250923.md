---
keywords:
  - Large Language Model
  - Text-to-SQL
  - Schema Linking
  - Attention Mechanism
  - Noisy Schema Sampling
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.14305
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:55:22.526709",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Text-to-SQL",
    "Schema Linking",
    "Attention Mechanism",
    "Noisy Schema Sampling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Text-to-SQL": 0.82,
    "Schema Linking": 0.79,
    "Attention Mechanism": 0.8,
    "Noisy Schema Sampling": 0.78
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the text-to-SQL task and connect with various NLP advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Text-to-SQL",
        "canonical": "Text-to-SQL",
        "aliases": [
          "NL to SQL",
          "Natural Language to SQL"
        ],
        "category": "unique_technical",
        "rationale": "Text-to-SQL is the primary focus of the paper, offering a unique technical perspective on natural language interfaces.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Schema Linking",
        "canonical": "Schema Linking",
        "aliases": [
          "Schema Matching",
          "Schema Mapping"
        ],
        "category": "specific_connectable",
        "rationale": "Schema linking is crucial for accurate SQL generation and connects to database schema research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are integral to the model's architecture, enhancing schema linking.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Noisy Schema Sampling",
        "canonical": "Noisy Schema Sampling",
        "aliases": [
          "Confusion-aware Sampling"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach improves robustness in SQL generation under noisy conditions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Text-to-SQL",
      "resolved_canonical": "Text-to-SQL",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Schema Linking",
      "resolved_canonical": "Schema Linking",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Noisy Schema Sampling",
      "resolved_canonical": "Noisy Schema Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# JOLT-SQL: Joint Loss Tuning of Text-to-SQL with Confusion-aware Noisy Schema Sampling

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.14305.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.14305](https://arxiv.org/abs/2505.14305)

## 🔗 유사한 논문
- [[2025-09-19/DeKeyNLU_ Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction_20250919|DeKeyNLU: Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction]] (84.4% similar)
- [[2025-09-23/TranSQL+_ Serving Large Language Models with SQL on Low-Resource Hardware_20250923|TranSQL+: Serving Large Language Models with SQL on Low-Resource Hardware]] (83.8% similar)
- [[2025-09-18/Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies_20250918|Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies]] (83.4% similar)
- [[2025-09-23/MIST_ Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning_20250923|MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning]] (81.0% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Schema Linking|Schema Linking]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Text-to-SQL|Text-to-SQL]], [[keywords/Noisy Schema Sampling|Noisy Schema Sampling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14305v2 Announce Type: replace 
Abstract: Text-to-SQL, which maps natural language to SQL queries, has benefited greatly from recent advances in Large Language Models (LLMs). While LLMs offer various paradigms for this task, including prompting and supervised fine-tuning (SFT), SFT approaches still face challenges such as complex multi-stage pipelines and poor robustness to noisy schema information. To address these limitations, we present JOLT-SQL, a streamlined single-stage SFT framework that jointly optimizes schema linking and SQL generation via a unified loss. JOLT-SQL employs discriminative schema linking, enhanced by local bidirectional attention, alongside a confusion-aware noisy schema sampling strategy with selective attention to improve robustness under noisy schema conditions. Experiments on the Spider and BIRD benchmarks demonstrate that JOLT-SQL achieves state-of-the-art execution accuracy among comparable-size open-source models, while significantly improving both training and inference efficiency.Our code is available at https://github.com/Songjw133/JOLT-SQL.

## 📝 요약

JOLT-SQL은 자연어를 SQL 쿼리로 변환하는 Text-to-SQL 작업에서 대형 언어 모델(LLM)의 발전을 활용한 단일 단계의 SFT 프레임워크입니다. 기존의 복잡한 다단계 파이프라인과 노이즈가 있는 스키마 정보에 대한 낮은 견고성을 개선하기 위해, JOLT-SQL은 스키마 연결과 SQL 생성 작업을 통합 손실로 최적화합니다. 이 프레임워크는 양방향 주의 메커니즘을 활용한 차별적 스키마 연결과 선택적 주의를 통한 노이즈 스키마 샘플링 전략을 통해 견고성을 강화합니다. Spider와 BIRD 벤치마크 실험에서 JOLT-SQL은 유사 크기의 오픈 소스 모델 중 최고 수준의 실행 정확도를 달성했으며, 학습 및 추론 효율성도 크게 향상되었습니다.

## 🎯 주요 포인트

- 1. JOLT-SQL은 자연어를 SQL 쿼리로 변환하는 작업에서 단일 단계의 SFT 프레임워크를 제안하여 스키마 연결과 SQL 생성의 공동 최적화를 수행합니다.
- 2. 이 프레임워크는 양방향 주의 메커니즘을 활용한 차별적 스키마 연결과 선택적 주의 전략을 통해 노이즈 있는 스키마 환경에서도 강건성을 향상시킵니다.
- 3. Spider와 BIRD 벤치마크 실험 결과, JOLT-SQL은 유사한 크기의 오픈 소스 모델 중에서 최첨단 실행 정확성을 달성하며, 훈련 및 추론 효율성을 크게 개선합니다.
- 4. JOLT-SQL의 코드는 https://github.com/Songjw133/JOLT-SQL에서 공개되어 있습니다.


---

*Generated on 2025-09-24 03:55:22*