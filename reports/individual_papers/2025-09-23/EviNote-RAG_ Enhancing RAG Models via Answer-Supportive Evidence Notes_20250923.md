---
keywords:
  - Retrieval Augmented Generation
  - Supportive Evidence Notes
  - Evidence Quality Reward
  - Multi-hop Reasoning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.00877
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:10:21.206120",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Supportive Evidence Notes",
    "Evidence Quality Reward",
    "Multi-hop Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.88,
    "Supportive Evidence Notes": 0.7,
    "Evidence Quality Reward": 0.72,
    "Multi-hop Reasoning": 0.8
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
        "rationale": "RAG is a trending concept in NLP that enhances QA models by integrating external data, making it highly relevant for linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Supportive-Evidence Notes",
        "canonical": "Supportive Evidence Notes",
        "aliases": [
          "SENs"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for understanding the model's approach to improving QA.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Evidence Quality Reward",
        "canonical": "Evidence Quality Reward",
        "aliases": [
          "EQR"
        ],
        "category": "unique_technical",
        "rationale": "EQR is a unique mechanism proposed to ensure logical sufficiency in evidence notes, enhancing model accuracy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Multi-hop Reasoning",
        "canonical": "Multi-hop Reasoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Multi-hop reasoning is a key process in advanced QA systems, relevant for linking complex reasoning tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "enhance",
      "improve",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Supportive-Evidence Notes",
      "resolved_canonical": "Supportive Evidence Notes",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Evidence Quality Reward",
      "resolved_canonical": "Evidence Quality Reward",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Multi-hop Reasoning",
      "resolved_canonical": "Multi-hop Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# EviNote-RAG: Enhancing RAG Models via Answer-Supportive Evidence Notes

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.00877.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.00877](https://arxiv.org/abs/2509.00877)

## 🔗 유사한 논문
- [[2025-09-23/Rationale-Guided Retrieval Augmented Generation for Medical Question Answering_20250923|Rationale-Guided Retrieval Augmented Generation for Medical Question Answering]] (86.4% similar)
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (85.9% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG: Retrieval-Augmented Generation with Implicit Queries]] (85.5% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (84.9% similar)
- [[2025-09-19/Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications: Design, Development, and Evaluation]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Multi-hop Reasoning|Multi-hop Reasoning]]
**⚡ Unique Technical**: [[keywords/Supportive Evidence Notes|Supportive Evidence Notes]], [[keywords/Evidence Quality Reward|Evidence Quality Reward]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.00877v2 Announce Type: replace 
Abstract: Retrieval-Augmented Generation (RAG) has advanced open-domain question answering by incorporating external information into model reasoning. However, effectively leveraging external information to enhance reasoning presents the following challenges: (1) low signal-to-noise ratio, where answer-supportive external information is diluted by irrelevant material, and (2) error accumulation, which arises in multi-hop reasoning when incomplete or misleading information is incorporated. To address these challenges, we introduce EviNote-RAG, a framework that follows a retrieve-note-answer workflow. Instead of reasoning directly over raw external information, the model first produces Supportive-Evidence Notes (SENs), which concisely preserve answer-critical information and explicitly mark key and uncertainty information to improve accuracy. We further design an entailment-based Evidence Quality Reward (EQR) to ensure that SENs are logically sufficient to derive the final answer, thereby enhancing SENs' quality. Experiments on both in-domain and out-of-domain QA benchmarks show that EviNote-RAG achieves state-of-the-art performance, improving answer accuracy, training stability, robustness, and efficiency. In particular, it yields relative F1 gains of 20% on HotpotQA (+0.093), 40% on Bamboogle (+0.151), and 91% on 2Wiki (+0.256), benefiting from improvements in the reasoning process.

## 📝 요약

EviNote-RAG는 외부 정보를 활용한 질의응답 시스템의 문제를 해결하기 위해 개발된 프레임워크입니다. 기존의 Retrieval-Augmented Generation(RAG) 방식은 외부 정보를 활용하지만, 불필요한 정보로 인해 신호 대 잡음 비율이 낮고, 불완전하거나 오도된 정보로 인해 오류가 누적되는 문제가 있었습니다. EviNote-RAG는 '검색-노트-답변'의 워크플로우를 통해 이러한 문제를 해결합니다. 모델은 먼저 Supportive-Evidence Notes(SENs)를 생성하여 답변에 필수적인 정보를 간결하게 보존하고, 주요 정보와 불확실한 정보를 명시적으로 표시합니다. 또한, 논리적으로 충분한 SENs를 보장하기 위해 증거 품질 보상(EQR)을 설계했습니다. 실험 결과, EviNote-RAG는 다양한 QA 벤치마크에서 최첨단 성능을 보이며, 답변 정확도, 훈련 안정성, 견고성 및 효율성을 향상시켰습니다. 특히, HotpotQA, Bamboogle, 2Wiki에서 각각 20%, 40%, 91%의 F1 점수 향상을 기록했습니다.

## 🎯 주요 포인트

- 1. Retrieval-Augmented Generation (RAG)는 외부 정보를 활용하여 개방형 질의응답의 모델 추론을 향상시킵니다.
- 2. EviNote-RAG는 retrieve-note-answer 워크플로우를 통해 외부 정보의 신호 대 잡음 비율 문제와 오류 누적 문제를 해결합니다.
- 3. Supportive-Evidence Notes (SENs)는 답변에 중요한 정보를 간결하게 보존하고, 정확성을 높이기 위해 주요 정보와 불확실한 정보를 명시적으로 표시합니다.
- 4. 증거 품질 보상(EQR)을 통해 SENs의 논리적 충분성을 보장하여 최종 답변의 정확성을 향상시킵니다.
- 5. EviNote-RAG는 다양한 QA 벤치마크에서 최첨단 성능을 달성하며, 특히 HotpotQA, Bamboogle, 2Wiki에서 상대적인 F1 점수 향상을 보여줍니다.


---

*Generated on 2025-09-24 04:10:21*