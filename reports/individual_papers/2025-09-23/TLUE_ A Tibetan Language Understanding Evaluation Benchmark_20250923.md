---
keywords:
  - Large Language Model
  - Tibetan Language Understanding Evaluation Benchmark
  - Multi-task Understanding Benchmark
  - Safety Benchmark
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2503.12051
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:53:05.865817",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Tibetan Language Understanding Evaluation Benchmark",
    "Multi-task Understanding Benchmark",
    "Safety Benchmark"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Tibetan Language Understanding Evaluation Benchmark": 0.88,
    "Multi-task Understanding Benchmark": 0.8,
    "Safety Benchmark": 0.77
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
        "rationale": "Large Language Models are central to the paper's focus on evaluating language understanding capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Tibetan Language Understanding Evaluation Benchmark",
        "canonical": "Tibetan Language Understanding Evaluation Benchmark",
        "aliases": [
          "TLUE"
        ],
        "category": "unique_technical",
        "rationale": "TLUE is a unique benchmark introduced in the paper, crucial for linking Tibetan language evaluation efforts.",
        "novelty_score": 0.92,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "multi-task understanding benchmark",
        "canonical": "Multi-task Understanding Benchmark",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This benchmark is a key component of TLUE, relevant for linking multi-task evaluation methods.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "safety benchmark",
        "canonical": "Safety Benchmark",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The safety benchmark is a distinct aspect of TLUE, important for linking safety evaluation in language models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "benchmark",
      "language model"
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
      "candidate_surface": "Tibetan Language Understanding Evaluation Benchmark",
      "resolved_canonical": "Tibetan Language Understanding Evaluation Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "multi-task understanding benchmark",
      "resolved_canonical": "Multi-task Understanding Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "safety benchmark",
      "resolved_canonical": "Safety Benchmark",
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

# TLUE: A Tibetan Language Understanding Evaluation Benchmark

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.12051.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2503.12051](https://arxiv.org/abs/2503.12051)

## 🔗 유사한 논문
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation]] (82.9% similar)
- [[2025-09-23/EquiBench_ Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking_20250923|EquiBench: Benchmarking Large Language Models' Reasoning about Program Semantics via Equivalence Checking]] (82.4% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (82.4% similar)
- [[2025-09-22/MUG-Eval_ A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language_20250922|MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language]] (82.2% similar)
- [[2025-09-23/TMD-TTS_ A Unified Tibetan Multi-Dialect Text-to-Speech Synthesis for \"U-Tsang, Amdo and Kham Speech Dataset Generation_20250923|TMD-TTS: A Unified Tibetan Multi-Dialect Text-to-Speech Synthesis for \"U-Tsang, Amdo and Kham Speech Dataset Generation]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-task Understanding Benchmark|Multi-task Understanding Benchmark]], [[keywords/Safety Benchmark|Safety Benchmark]]
**⚡ Unique Technical**: [[keywords/Tibetan Language Understanding Evaluation Benchmark|Tibetan Language Understanding Evaluation Benchmark]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.12051v4 Announce Type: replace 
Abstract: Large language models have made tremendous progress in recent years, but low-resource languages, like Tibetan, remain significantly underrepresented in their evaluation. Despite Tibetan being spoken by over seven million people, it has largely been neglected in the development and assessment of large language models. To address this gap, we present a \textbf{T}ibetan \textbf{L}anguage \textbf{U}nderstanding \textbf{E}valuation Benchmark, \textbf{TLUE}, the first large-scale benchmark for measuring the proficiency of LLMs in the Tibetan language. \textbf{TLUE} comprises two major components: a comprehensive multi-task understanding benchmark spanning 5 domains and 67 subdomains, and a safety benchmark encompassing 7 subdomains. Then, we evaluate a diverse set of state-of-the-art large language models. Experimental results demonstrate that most large language models perform below the random baseline, highlighting the considerable challenges they face in Tibetan language processing. \textbf{TLUE} provides a crucial foundation for advancing future research in Tibetan language understanding and highlights the importance of promoting greater inclusivity in the development of large language models.

## 📝 요약

최근 대형 언어 모델의 발전에도 불구하고 티베트어와 같은 저자원 언어는 평가에서 크게 소외되어 왔습니다. 이를 해결하기 위해, 우리는 대형 언어 모델의 티베트어 능력을 측정하는 최초의 대규모 벤치마크인 TLUE를 제시합니다. TLUE는 5개 도메인과 67개 하위 도메인에 걸친 다중 작업 이해 벤치마크와 7개 하위 도메인의 안전성 벤치마크로 구성됩니다. 다양한 최신 대형 언어 모델을 평가한 결과, 대부분의 모델이 무작위 기준보다 낮은 성능을 보였으며, 이는 티베트어 처리의 어려움을 나타냅니다. TLUE는 티베트어 이해 연구의 발전을 위한 중요한 기초를 제공하며, 대형 언어 모델 개발에서 포용성을 높이는 것의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. 티베트어는 700만 명 이상이 사용하는 언어임에도 불구하고 대형 언어 모델의 평가에서 크게 소외되어 왔습니다.
- 2. 티베트어 이해 평가 벤치마크(TLUE)는 티베트어에서 대형 언어 모델의 능력을 측정하기 위한 최초의 대규모 벤치마크입니다.
- 3. TLUE는 5개 도메인과 67개 하위 도메인을 아우르는 종합적인 다중 작업 이해 벤치마크와 7개 하위 도메인을 포함하는 안전성 벤치마크로 구성되어 있습니다.
- 4. 실험 결과, 대부분의 대형 언어 모델이 무작위 기준보다 낮은 성능을 보이며, 티베트어 처리에서 상당한 어려움을 겪고 있음을 보여줍니다.
- 5. TLUE는 티베트어 이해 연구를 발전시키기 위한 중요한 기반을 제공하며, 대형 언어 모델 개발에서 더 큰 포용성을 촉진하는 것의 중요성을 강조합니다.


---

*Generated on 2025-09-24 03:53:05*