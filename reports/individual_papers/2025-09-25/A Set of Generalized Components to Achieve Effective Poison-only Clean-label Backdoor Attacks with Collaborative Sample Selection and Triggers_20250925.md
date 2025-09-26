---
keywords:
  - Clean-label Backdoor Attacks
  - Neural Network
  - Sample Selection
  - Trigger
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19947
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:54:44.545097",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Clean-label Backdoor Attacks",
    "Neural Network",
    "Sample Selection",
    "Trigger"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Clean-label Backdoor Attacks": 0.78,
    "Neural Network": 0.72,
    "Sample Selection": 0.74,
    "Trigger": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Clean-label Backdoor Attacks",
        "canonical": "Clean-label Backdoor Attacks",
        "aliases": [
          "CLBA",
          "Poison-only Backdoor Attacks"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specific attack strategy in machine learning, crucial for understanding security vulnerabilities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deep Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "DNN"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are foundational to understanding the context of backdoor attacks in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Sample Selection",
        "canonical": "Sample Selection",
        "aliases": [
          "Data Selection"
        ],
        "category": "specific_connectable",
        "rationale": "Sample selection is a key process in enhancing attack success rates, linking to data processing strategies.",
        "novelty_score": 0.58,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.74
      },
      {
        "surface": "Trigger",
        "canonical": "Trigger",
        "aliases": [
          "Backdoor Trigger"
        ],
        "category": "specific_connectable",
        "rationale": "Triggers are essential components in backdoor attacks, crucial for understanding attack mechanisms.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "evaluation metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Clean-label Backdoor Attacks",
      "resolved_canonical": "Clean-label Backdoor Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deep Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Sample Selection",
      "resolved_canonical": "Sample Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Trigger",
      "resolved_canonical": "Trigger",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# A Set of Generalized Components to Achieve Effective Poison-only Clean-label Backdoor Attacks with Collaborative Sample Selection and Triggers

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19947.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19947](https://arxiv.org/abs/2509.19947)

## 🔗 유사한 논문
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (83.2% similar)
- [[2025-09-23/Neural Antidote_ Class-Wise Prompt Tuning for Purifying Backdoors in CLIP_20250923|Neural Antidote: Class-Wise Prompt Tuning for Purifying Backdoors in CLIP]] (82.6% similar)
- [[2025-09-24/Backdoor Attack with Invisible Triggers Based on Model Architecture Modification_20250924|Backdoor Attack with Invisible Triggers Based on Model Architecture Modification]] (82.4% similar)
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (82.3% similar)
- [[2025-09-24/Enhancing the Effectiveness and Durability of Backdoor Attacks in Federated Learning through Maximizing Task Distinction_20250924|Enhancing the Effectiveness and Durability of Backdoor Attacks in Federated Learning through Maximizing Task Distinction]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Sample Selection|Sample Selection]], [[keywords/Trigger|Trigger]]
**⚡ Unique Technical**: [[keywords/Clean-label Backdoor Attacks|Clean-label Backdoor Attacks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19947v1 Announce Type: cross 
Abstract: Poison-only Clean-label Backdoor Attacks aim to covertly inject attacker-desired behavior into DNNs by merely poisoning the dataset without changing the labels. To effectively implant a backdoor, multiple \textbf{triggers} are proposed for various attack requirements of Attack Success Rate (ASR) and stealthiness. Additionally, sample selection enhances clean-label backdoor attacks' ASR by meticulously selecting ``hard'' samples instead of random samples to poison. Current methods 1) usually handle the sample selection and triggers in isolation, leading to severely limited improvements on both ASR and stealthiness. Consequently, attacks exhibit unsatisfactory performance on evaluation metrics when converted to PCBAs via a mere stacking of methods. Therefore, we seek to explore the bidirectional collaborative relations between the sample selection and triggers to address the above dilemma. 2) Since the strong specificity within triggers, the simple combination of sample selection and triggers fails to substantially enhance both evaluation metrics, with generalization preserved among various attacks. Therefore, we seek to propose a set of components to significantly improve both stealthiness and ASR based on the commonalities of attacks. Specifically, Component A ascertains two critical selection factors, and then makes them an appropriate combination based on the trigger scale to select more reasonable ``hard'' samples for improving ASR. Component B is proposed to select samples with similarities to relevant trigger implanted samples to promote stealthiness. Component C reassigns trigger poisoning intensity on RGB colors through distinct sensitivity of the human visual system to RGB for higher ASR, with stealthiness ensured by sample selection, including Component B. Furthermore, all components can be strategically integrated into diverse PCBAs.

## 📝 요약

이 논문은 데이터셋의 라벨을 변경하지 않고 단순히 데이터셋을 오염시켜 공격자가 원하는 행동을 심는 'Poison-only Clean-label Backdoor Attacks'에 대해 다룹니다. 기존 방법들은 샘플 선택과 트리거를 별도로 처리하여 공격 성공률(ASR)과 은닉성을 충분히 개선하지 못했습니다. 이를 해결하기 위해 샘플 선택과 트리거 간의 협력 관계를 탐구하고, 공통 요소를 기반으로 ASR과 은닉성을 크게 향상시키는 구성 요소 세트를 제안합니다. 구성 요소 A는 트리거 규모에 맞춰 '어려운' 샘플을 선택해 ASR을 개선하고, 구성 요소 B는 트리거가 심어진 샘플과 유사한 샘플을 선택해 은닉성을 높입니다. 구성 요소 C는 인간 시각 시스템의 RGB 민감도를 고려해 트리거의 강도를 조정하여 ASR을 높이며, 은닉성은 샘플 선택으로 보장합니다. 모든 구성 요소는 다양한 공격에 전략적으로 통합될 수 있습니다.

## 🎯 주요 포인트

- 1. Poison-only Clean-label Backdoor Attacks는 데이터셋의 라벨을 변경하지 않고 단순히 데이터셋을 오염시켜 공격자가 원하는 행동을 DNN에 주입하는 것을 목표로 합니다.
- 2. 공격 성공률(ASR)과 은밀성을 높이기 위해 다양한 트리거가 제안되며, '어려운' 샘플을 선택해 오염시키는 방식으로 ASR을 향상시킵니다.
- 3. 기존 방법은 샘플 선택과 트리거를 독립적으로 처리하여 ASR과 은밀성의 개선이 제한적이며, 단순한 방법의 결합으로는 평가 지표에서 만족스러운 성능을 보이지 않습니다.
- 4. 샘플 선택과 트리거 간의 협력 관계를 탐구하여 ASR과 은밀성을 동시에 개선할 수 있는 구성 요소를 제안합니다.
- 5. 제안된 구성 요소들은 다양한 PCBAs에 전략적으로 통합될 수 있으며, 공격의 공통점을 기반으로 ASR과 은밀성을 크게 향상시킵니다.


---

*Generated on 2025-09-25 15:54:44*