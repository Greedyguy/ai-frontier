---
keywords:
  - Low-Rank Adaptation
  - Large Language Model
  - Unsupervised LoRA Routing
  - Activation Norm Maximization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18093
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:21:06.461441",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Rank Adaptation",
    "Large Language Model",
    "Unsupervised LoRA Routing",
    "Activation Norm Maximization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-Rank Adaptation": 0.78,
    "Large Language Model": 0.8,
    "Unsupervised LoRA Routing": 0.82,
    "Activation Norm Maximization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "Low-Rank Adaptation is central to the paper's focus on efficient fine-tuning and routing, making it a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are a foundational concept in the paper, linking it to broader discussions in AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Unsupervised LoRA Routing",
        "canonical": "Unsupervised LoRA Routing",
        "aliases": [
          "SEQR"
        ],
        "category": "unique_technical",
        "rationale": "This concept is a novel approach introduced by the paper, focusing on efficient and secure routing.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Activation Norm Maximization",
        "canonical": "Activation Norm Maximization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is critical for the paper's proposed routing method, linking to optimization strategies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
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
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
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
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Unsupervised LoRA Routing",
      "resolved_canonical": "Unsupervised LoRA Routing",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Activation Norm Maximization",
      "resolved_canonical": "Activation Norm Maximization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SEQR: Secure and Efficient QR-based LoRA Routing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18093.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18093](https://arxiv.org/abs/2509.18093)

## 🔗 유사한 논문
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (81.6% similar)
- [[2025-09-22/BiRQ_ Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition_20250922|BiRQ: Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition]] (81.1% similar)
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (80.6% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (80.4% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO: A Framework for Confidence-Aware Routing of Large Language Models]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Activation Norm Maximization|Activation Norm Maximization]]
**⚡ Unique Technical**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]], [[keywords/Unsupervised LoRA Routing|Unsupervised LoRA Routing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18093v1 Announce Type: cross 
Abstract: Low-Rank Adaptation (LoRA) has become a standard technique for parameter-efficient fine-tuning of large language models, enabling large libraries of LoRAs, each for a specific task or domain. Efficiently selecting the correct LoRA adapter for a given input remains a challenge, particularly in secure environments where supervised training of routers may raise privacy concerns. Motivated by previous approaches, we formalize the goal of unsupervised LoRA routing in terms of activation norm maximization, providing a theoretical framework for analysis. We demonstrate the discriminative power of activation norms and introduce SEQR, an unsupervised LoRA routing algorithm designed to maximize efficiency while providing strict routing guarantees. SEQR provably identifies the norm-maximizing adapter with significantly greater efficiency, making it a highly scalable and effective solution for dynamic LoRA composition. We validate our results through experiments that demonstrate improved multi-task performance and efficiency.

## 📝 요약

Low-Rank Adaptation (LoRA)는 대규모 언어 모델의 파라미터 효율적인 미세 조정을 위한 표준 기술로 자리 잡았지만, 주어진 입력에 적합한 LoRA 어댑터를 선택하는 것은 여전히 어려운 과제입니다. 특히, 보안 환경에서는 지도 학습을 통한 라우터 훈련이 개인정보 문제를 야기할 수 있습니다. 본 연구는 활성화 노름 최대화를 통한 비지도 LoRA 라우팅 목표를 이론적으로 정립하고, SEQR이라는 알고리즘을 제안합니다. SEQR은 활성화 노름의 판별력을 활용하여 효율성을 극대화하며, 동적 LoRA 구성에 적합한 솔루션을 제공합니다. 실험 결과, SEQR은 다중 작업 성능과 효율성을 향상시킴을 입증했습니다.

## 🎯 주요 포인트

- 1. Low-Rank Adaptation (LoRA)는 대형 언어 모델의 파라미터 효율적인 미세 조정을 위한 표준 기술로 자리 잡았다.
- 2. 주어진 입력에 대해 적절한 LoRA 어댑터를 효율적으로 선택하는 것은 여전히 도전 과제이다.
- 3. 활성화 노름 최대화를 통해 비지도 LoRA 라우팅 목표를 공식화하고 이론적 분석을 제공한다.
- 4. SEQR은 효율성을 극대화하면서 엄격한 라우팅 보장을 제공하는 비지도 LoRA 라우팅 알고리즘이다.
- 5. 실험을 통해 SEQR의 다중 작업 성능 및 효율성 향상을 검증하였다.


---

*Generated on 2025-09-24 00:21:06*