<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:31:09.816532",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Knowledge Editing",
    "Large Language Model",
    "Reasoning Circuits",
    "Multi-hop Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Knowledge Editing": 0.8,
    "Large Language Model": 0.85,
    "Reasoning Circuits": 0.78,
    "Multi-hop Reasoning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Knowledge Editing",
        "canonical": "Knowledge Editing",
        "aliases": [
          "KE"
        ],
        "category": "unique_technical",
        "rationale": "Knowledge Editing is central to the paper's contribution and represents a novel approach to updating LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are the primary subject of the paper's proposed method.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reasoning Circuits",
        "canonical": "Reasoning Circuits",
        "aliases": [
          "Neural Pathways"
        ],
        "category": "unique_technical",
        "rationale": "Reasoning Circuits are crucial for understanding how the proposed method integrates knowledge.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-hop Reasoning",
        "canonical": "Multi-hop Reasoning",
        "aliases": [
          "Complex Reasoning Tasks"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-hop Reasoning is a key application area for the method, demonstrating its effectiveness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
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
      "candidate_surface": "Knowledge Editing",
      "resolved_canonical": "Knowledge Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Reasoning Circuits",
      "resolved_canonical": "Reasoning Circuits",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-hop Reasoning",
      "resolved_canonical": "Multi-hop Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.16356.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2503.16356](https://arxiv.org/abs/2503.16356)

## 🔗 유사한 논문
- [[2025-09-23/EAMET_ Robust Massive Model Editing via Embedding Alignment Optimization_20250923|EAMET: Robust Massive Model Editing via Embedding Alignment Optimization]] (83.4% similar)
- [[2025-09-23/WikiBigEdit_ Understanding the Limits of Lifelong Knowledge Editing in LLMs_20250923|WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs]] (83.1% similar)
- [[2025-09-23/Diagnosing Model Editing via Knowledge Spectrum_20250923|Diagnosing Model Editing via Knowledge Spectrum]] (83.1% similar)
- [[2025-09-23/K-DeCore_ Facilitating Knowledge Transfer in Continual Structured Knowledge Reasoning via Knowledge Decoupling_20250923|K-DeCore: Facilitating Knowledge Transfer in Continual Structured Knowledge Reasoning via Knowledge Decoupling]] (82.7% similar)
- [[2025-09-22/Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs_20250922|Temporal Reasoning with Large Language Models Augmented by Evolving Knowledge Graphs]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-hop Reasoning|Multi-hop Reasoning]]
**⚡ Unique Technical**: [[keywords/Knowledge Editing|Knowledge Editing]], [[keywords/Reasoning Circuits|Reasoning Circuits]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.16356v2 Announce Type: replace-cross 
Abstract: Knowledge Editing (KE) enables the modification of outdated or incorrect information in large language models (LLMs). While existing KE methods can update isolated facts, they often fail to generalize these updates to multi-hop reasoning tasks that rely on the modified knowledge. Through an analysis of reasoning circuits -- the neural pathways LLMs use for knowledge-based inference, we find that current layer-localized KE approaches (e.g., MEMIT, WISE), which edit only single or a few model layers, inadequately integrate updated knowledge into these reasoning pathways. To address this limitation, we present CaKE (Circuit-aware Knowledge Editing), a novel method that enhances the effective integration of updated knowledge in LLMs. By only leveraging a few curated data samples guided by our circuit-based analysis, CaKE stimulates the model to develop appropriate reasoning circuits for newly incorporated knowledge. Experiments show that CaKE enables more accurate and consistent use of edited knowledge across related reasoning tasks, achieving an average improvement of 20% in multi-hop reasoning accuracy on the MQuAKE dataset while requiring less memory than existing KE methods. We release the code and data in https://github.com/zjunlp/CaKE.

## 📝 요약

Knowledge Editing(KE)은 대형 언어 모델(LLM)에서 오래되거나 잘못된 정보를 수정할 수 있게 합니다. 기존 KE 방법은 개별 사실을 업데이트할 수 있지만, 수정된 지식을 활용하는 다중 단계 추론 작업에는 일반화하지 못하는 경우가 많습니다. 본 연구에서는 LLM의 추론 회로를 분석하여, 현재의 레이어에 국한된 KE 접근법들이 업데이트된 지식을 효과적으로 통합하지 못한다는 점을 발견했습니다. 이를 해결하기 위해, 우리는 CaKE(Circuit-aware Knowledge Editing)라는 새로운 방법을 제안합니다. CaKE는 소수의 데이터 샘플을 활용하여 모델이 새로운 지식을 위한 적절한 추론 회로를 개발하도록 유도합니다. 실험 결과, CaKE는 수정된 지식을 관련 추론 작업에서 더 정확하고 일관되게 사용할 수 있게 하며, MQuAKE 데이터셋에서 다중 단계 추론 정확도가 평균 20% 향상되었습니다. 또한, 기존 KE 방법보다 적은 메모리를 요구합니다. 코드와 데이터는 https://github.com/zjunlp/CaKE에서 공개됩니다.

## 🎯 주요 포인트

- 1. 기존의 지식 편집(KE) 방법은 개별 사실을 업데이트할 수 있지만, 수정된 지식에 의존하는 다중 단계 추론 작업에 일반화하는 데 실패하는 경우가 많습니다.
- 2. 현재의 계층-국지화된 KE 접근법은 업데이트된 지식을 추론 경로에 적절히 통합하지 못합니다.
- 3. CaKE는 회로 기반 분석을 통해 선별된 데이터 샘플을 활용하여, 새로 통합된 지식을 위한 적절한 추론 회로를 개발하도록 모델을 자극합니다.
- 4. CaKE는 MQuAKE 데이터셋에서 다중 단계 추론 정확도를 평균 20% 향상시키면서도 기존 KE 방법보다 적은 메모리를 요구합니다.
- 5. CaKE의 코드와 데이터는 https://github.com/zjunlp/CaKE에서 공개됩니다.


---

*Generated on 2025-09-24 14:31:09*