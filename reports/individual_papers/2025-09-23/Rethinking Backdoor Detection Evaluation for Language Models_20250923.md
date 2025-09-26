---
keywords:
  - Backdoor Attack
  - Large Language Model
  - Backdoor Detection
  - Trigger Inversion
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2409.00399
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:44:08.131727",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Backdoor Attack",
    "Large Language Model",
    "Backdoor Detection",
    "Trigger Inversion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Backdoor Attack": 0.9,
    "Large Language Model": 0.85,
    "Backdoor Detection": 0.88,
    "Trigger Inversion": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Backdoor Attacks",
        "canonical": "Backdoor Attack",
        "aliases": [
          "Backdoor Insertion",
          "Malicious Trigger"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on security risks in language models and is not commonly found in the existing vocabulary.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.9
      },
      {
        "surface": "Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "This is a foundational concept in the paper, linking it to broader discussions on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Backdoor Detection",
        "canonical": "Backdoor Detection",
        "aliases": [
          "Backdoor Identification",
          "Malicious Trigger Detection"
        ],
        "category": "unique_technical",
        "rationale": "The paper evaluates the effectiveness of detection methods, making this a key technical term.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Trigger Inversion",
        "canonical": "Trigger Inversion",
        "aliases": [
          "Reverse Trigger",
          "Inversion Method"
        ],
        "category": "specific_connectable",
        "rationale": "This method is specifically discussed as a technique for detecting backdoors, providing a connection point for related research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "model",
      "method",
      "benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Backdoor Attacks",
      "resolved_canonical": "Backdoor Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Backdoor Detection",
      "resolved_canonical": "Backdoor Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Trigger Inversion",
      "resolved_canonical": "Trigger Inversion",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Rethinking Backdoor Detection Evaluation for Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2409.00399.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2409.00399](https://arxiv.org/abs/2409.00399)

## 🔗 유사한 논문
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (88.9% similar)
- [[2025-09-23/Jailbreak-Tuning_ Models Efficiently Learn Jailbreak Susceptibility_20250923|Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility]] (85.5% similar)
- [[2025-09-23/Test-Time Multimodal Backdoor Detection by Contrastive Prompting_20250923|Test-Time Multimodal Backdoor Detection by Contrastive Prompting]] (85.3% similar)
- [[2025-09-22/Inverting Trojans in LLMs_20250922|Inverting Trojans in LLMs]] (85.2% similar)
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Trigger Inversion|Trigger Inversion]]
**⚡ Unique Technical**: [[keywords/Backdoor Attack|Backdoor Attack]], [[keywords/Backdoor Detection|Backdoor Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.00399v2 Announce Type: replace 
Abstract: Backdoor attacks, in which a model behaves maliciously when given an attacker-specified trigger, pose a major security risk for practitioners who depend on publicly released language models. As a countermeasure, backdoor detection methods aim to detect whether a released model contains a backdoor. While existing backdoor detection methods have high accuracy in detecting backdoored models on standard benchmarks, it is unclear whether they can robustly identify backdoors in the wild. In this paper, we examine the robustness of backdoor detectors by manipulating different factors during backdoor planting. We find that the success of existing methods based on trigger inversion or meta classifiers highly depends on how intensely the model is trained on poisoned data. Specifically, backdoors planted with more aggressive or more conservative training are significantly more difficult to detect than the default ones. Our results highlight a lack of robustness of existing backdoor detectors and the limitations in current benchmark construction.

## 📝 요약

이 논문은 공개된 언어 모델에 대한 백도어 공격의 위험성을 다루며, 백도어 탐지 방법의 견고성을 평가합니다. 기존 탐지 방법은 표준 벤치마크에서 높은 정확도를 보이지만, 실제 환경에서의 견고성은 불확실합니다. 연구 결과, 트리거 반전이나 메타 분류기에 기반한 기존 방법의 성공 여부는 모델이 오염된 데이터로 얼마나 강하게 훈련되었는지에 크게 좌우됩니다. 특히, 더 공격적이거나 보수적으로 훈련된 백도어는 탐지가 어렵습니다. 이는 현재 백도어 탐지기의 견고성 부족과 벤치마크 구성의 한계를 강조합니다.

## 🎯 주요 포인트

- 1. 백도어 공격은 공격자가 지정한 트리거에 의해 모델이 악의적으로 작동하게 하여 보안 위험을 초래한다.
- 2. 백도어 탐지 방법은 공개된 모델에 백도어가 포함되어 있는지를 감지하는 것을 목표로 한다.
- 3. 기존 백도어 탐지 방법은 표준 벤치마크에서 높은 정확도를 보이지만, 실제 환경에서의 견고성은 불확실하다.
- 4. 백도어 탐지기의 견고성을 평가한 결과, 트리거 반전이나 메타 분류기에 기반한 방법의 성공은 모델이 오염된 데이터로 얼마나 강하게 훈련되었는지에 크게 의존한다.
- 5. 공격적인 또는 보수적인 훈련으로 심어진 백도어는 기본적인 백도어보다 탐지하기 어렵다는 한계가 드러났다.


---

*Generated on 2025-09-24 03:44:08*