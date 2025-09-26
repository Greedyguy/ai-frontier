---
keywords:
  - Half-Truth Detection
  - Fact Verification
  - PolitiFact-Hidden Benchmark
  - TRACER Framework
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2508.00489
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:08:59.811787",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Half-Truth Detection",
    "Fact Verification",
    "PolitiFact-Hidden Benchmark",
    "TRACER Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Half-Truth Detection": 0.78,
    "Fact Verification": 0.72,
    "PolitiFact-Hidden Benchmark": 0.77,
    "TRACER Framework": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "half-truth detection",
        "canonical": "Half-Truth Detection",
        "aliases": [
          "partial truth detection",
          "misleading truth detection"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel task that is central to the paper's contribution and enhances understanding of misinformation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "fact verification",
        "canonical": "Fact Verification",
        "aliases": [
          "claim verification",
          "truth verification"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental process in the paper, connecting to broader discussions on truth assessment in AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      },
      {
        "surface": "PolitiFact-Hidden",
        "canonical": "PolitiFact-Hidden Benchmark",
        "aliases": [
          "PolitiFact dataset",
          "Hidden benchmark"
        ],
        "category": "unique_technical",
        "rationale": "A specific dataset introduced by the authors, crucial for replicating and understanding the study's results.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "TRACER",
        "canonical": "TRACER Framework",
        "aliases": [
          "TRACER system",
          "TRACER model"
        ],
        "category": "unique_technical",
        "rationale": "The core framework proposed in the paper, essential for understanding the implementation of half-truth detection.",
        "novelty_score": 0.78,
        "connectivity_score": 0.75,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "evidence alignment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "half-truth detection",
      "resolved_canonical": "Half-Truth Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "fact verification",
      "resolved_canonical": "Fact Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "PolitiFact-Hidden",
      "resolved_canonical": "PolitiFact-Hidden Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "TRACER",
      "resolved_canonical": "TRACER Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.75,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# The Missing Parts: Augmenting Fact Verification with Half-Truth Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2508.00489.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2508.00489](https://arxiv.org/abs/2508.00489)

## 🔗 유사한 논문
- [[2025-09-22/RAVE_ Retrieval and Scoring Aware Verifiable Claim Detection_20250922|RAVE: Retrieval and Scoring Aware Verifiable Claim Detection]] (84.3% similar)
- [[2025-09-22/Where Fact Ends and Fairness Begins_ Redefining AI Bias Evaluation through Cognitive Biases_20250922|Where Fact Ends and Fairness Begins: Redefining AI Bias Evaluation through Cognitive Biases]] (83.0% similar)
- [[2025-09-22/Multimodal Learning for Fake News Detection in Short Videos Using Linguistically Verified Data and Heterogeneous Modality Fusion_20250922|Multimodal Learning for Fake News Detection in Short Videos Using Linguistically Verified Data and Heterogeneous Modality Fusion]] (80.7% similar)
- [[2025-09-19/MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1: Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (80.5% similar)
- [[2025-09-22/The Psychology of Falsehood_ A Human-Centric Survey of Misinformation Detection_20250922|The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Fact Verification|Fact Verification]]
**⚡ Unique Technical**: [[keywords/Half-Truth Detection|Half-Truth Detection]], [[keywords/PolitiFact-Hidden Benchmark|PolitiFact-Hidden Benchmark]], [[keywords/TRACER Framework|TRACER Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.00489v2 Announce Type: replace 
Abstract: Fact verification systems typically assess whether a claim is supported by retrieved evidence, assuming that truthfulness depends solely on what is stated. However, many real-world claims are half-truths, factually correct yet misleading due to the omission of critical context. Existing models struggle with such cases, as they are not designed to reason about omitted information. We introduce the task of half-truth detection, and propose PolitiFact-Hidden, a new benchmark with 15k political claims annotated with sentence-level evidence alignment and inferred claim intent. To address this challenge, we present TRACER, a modular re-assessment framework that identifies omission-based misinformation by aligning evidence, inferring implied intent, and estimating the causal impact of hidden content. TRACER can be integrated into existing fact-checking pipelines and consistently improves performance across multiple strong baselines. Notably, it boosts Half-True classification F1 by up to 16 points, highlighting the importance of modeling omissions for trustworthy fact verification. The benchmark and code are available via https://github.com/tangyixuan/TRACER.

## 📝 요약

이 논문은 절반의 진실을 탐지하는 새로운 과제를 소개하며, 기존 사실 검증 시스템이 중요한 맥락이 생략된 경우를 처리하지 못하는 문제를 해결하고자 합니다. 이를 위해 15,000개의 정치적 주장에 대한 문장 수준의 증거 정렬과 주장 의도를 주석한 PolitiFact-Hidden 벤치마크를 제안합니다. 또한, TRACER라는 모듈형 재평가 프레임워크를 개발하여 생략된 정보를 기반으로 한 오정보를 식별하고, 기존 사실 검증 파이프라인에 통합하여 성능을 향상시킵니다. TRACER는 특히 Half-True 분류의 F1 점수를 최대 16점까지 향상시키며, 생략된 정보의 중요성을 강조합니다. 이 연구의 벤치마크와 코드는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 사실 검증 시스템은 일반적으로 주장과 회수된 증거의 일치 여부를 평가하지만, 많은 실제 주장은 중요한 맥락이 생략되어 사실적으로는 맞지만 오해를 불러일으키는 반쪽 진실이다.
- 2. 기존 모델은 생략된 정보를 추론하도록 설계되지 않아 반쪽 진실을 다루는 데 어려움을 겪는다.
- 3. 우리는 반쪽 진실 탐지 작업을 도입하고, 문장 수준의 증거 정렬 및 추론된 주장 의도가 주석된 15,000개의 정치적 주장으로 구성된 새로운 벤치마크인 PolitiFact-Hidden을 제안한다.
- 4. TRACER는 증거 정렬, 암시된 의도 추론, 숨겨진 내용의 인과적 영향을 추정하여 생략 기반의 허위 정보를 식별하는 모듈형 재평가 프레임워크로, 기존 사실 검증 파이프라인에 통합될 수 있다.
- 5. TRACER는 반쪽 진실 분류 F1 점수를 최대 16점 향상시켜, 생략을 모델링하는 것이 신뢰할 수 있는 사실 검증에 중요함을 강조한다.


---

*Generated on 2025-09-24 04:08:59*