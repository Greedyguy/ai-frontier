---
keywords:
  - Machine Learning
  - Confidential Property Inference
  - Responsive CPI attack
  - Attack-Defense Arms Race
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16352
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:16:19.376636",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Confidential Property Inference",
    "Responsive CPI attack",
    "Attack-Defense Arms Race"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.8,
    "Confidential Property Inference": 0.85,
    "Responsive CPI attack": 0.9,
    "Attack-Defense Arms Race": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a foundational concept that connects to numerous technical areas and applications.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      },
      {
        "surface": "Confidential Property Inference attacks",
        "canonical": "Confidential Property Inference",
        "aliases": [
          "CPI attacks"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific type of attack relevant to the paper's focus on model security.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Responsive CPI attack",
        "canonical": "Responsive CPI attack",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel concept introduced in the paper, highlighting adaptive adversarial strategies.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "attack-defense arms race framework",
        "canonical": "Attack-Defense Arms Race",
        "aliases": [
          "arms race framework"
        ],
        "category": "unique_technical",
        "rationale": "This framework is central to the paper's proposed methodology for enhancing model security.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "model-sharing",
      "defense methods",
      "computational bottleneck"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Confidential Property Inference attacks",
      "resolved_canonical": "Confidential Property Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Responsive CPI attack",
      "resolved_canonical": "Responsive CPI attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "attack-defense arms race framework",
      "resolved_canonical": "Attack-Defense Arms Race",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# Secure Confidential Business Information When Sharing Machine Learning Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16352.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16352](https://arxiv.org/abs/2509.16352)

## 🔗 유사한 논문
- [[2025-09-22/When Secure Isn't_ Assessing the Security of Machine Learning Model Sharing_20250922|When Secure Isn't: Assessing the Security of Machine Learning Model Sharing]] (85.3% similar)
- [[2025-09-19/The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (82.8% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (82.0% similar)
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (81.3% similar)
- [[2025-09-22/Negotiated Representations to Prevent Overfitting in Machine Learning Applications_20250922|Negotiated Representations to Prevent Overfitting in Machine Learning Applications]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Confidential Property Inference|Confidential Property Inference]], [[keywords/Responsive CPI attack|Responsive CPI attack]], [[keywords/Attack-Defense Arms Race|Attack-Defense Arms Race]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16352v1 Announce Type: cross 
Abstract: Model-sharing offers significant business value by enabling firms with well-established Machine Learning (ML) models to monetize and share their models with others who lack the resources to develop ML models from scratch. However, concerns over data confidentiality remain a significant barrier to model-sharing adoption, as Confidential Property Inference (CPI) attacks can exploit shared ML models to uncover confidential properties of the model provider's private model training data. Existing defenses often assume that CPI attacks are non-adaptive to the specific ML model they are targeting. This assumption overlooks a key characteristic of real-world adversaries: their responsiveness, i.e., adversaries' ability to dynamically adjust their attack models based on the information of the target and its defenses. To overcome this limitation, we propose a novel defense method that explicitly accounts for the responsive nature of real-world adversaries via two methodological innovations: a novel Responsive CPI attack and an attack-defense arms race framework. The former emulates the responsive behaviors of adversaries in the real world, and the latter iteratively enhances both the target and attack models, ultimately producing a secure ML model that is robust against responsive CPI attacks. Furthermore, we propose and integrate a novel approximate strategy into our defense, which addresses a critical computational bottleneck of defense methods and improves defense efficiency. Through extensive empirical evaluations across various realistic model-sharing scenarios, we demonstrate that our method outperforms existing defenses by more effectively defending against CPI attacks, preserving ML model utility, and reducing computational overhead.

## 📝 요약

이 논문은 기계 학습(ML) 모델 공유의 데이터 기밀성 문제를 해결하기 위한 새로운 방어 방법을 제안합니다. 기존 방어법은 공격자가 특정 ML 모델에 적응하지 않는다고 가정하지만, 실제 공격자는 목표와 방어에 따라 공격 모델을 동적으로 조정할 수 있습니다. 이를 해결하기 위해, 논문은 두 가지 방법론적 혁신을 제안합니다: 실제 세계의 적응적 공격자를 모방하는 '적응형 기밀 속성 추론(CPI) 공격'과 공격-방어 경쟁 프레임워크입니다. 이 방법은 공격과 방어 모델을 반복적으로 개선하여 적응형 CPI 공격에 강한 안전한 ML 모델을 만듭니다. 또한, 방어 효율성을 높이기 위해 새로운 근사 전략을 통합했습니다. 다양한 모델 공유 시나리오에서의 실험 결과, 제안된 방법이 기존 방어법보다 CPI 공격을 더 효과적으로 방어하고, ML 모델의 유용성을 유지하며, 계산 비용을 줄이는 데 우수함을 입증했습니다.

## 🎯 주요 포인트

- 1. 모델 공유는 기계 학습 모델을 개발할 자원이 부족한 기업들에게 모델을 공유하여 수익을 창출할 수 있는 비즈니스 가치를 제공합니다.
- 2. 기밀 속성 추론(CPI) 공격은 공유된 ML 모델을 악용하여 모델 제공자의 비공개 모델 훈련 데이터의 기밀 속성을 노출시킬 수 있어 데이터 기밀성에 대한 우려가 큽니다.
- 3. 기존 방어법은 CPI 공격이 특정 ML 모델에 적응하지 않는다고 가정하지만, 실제 공격자는 대상 및 방어 정보에 따라 공격 모델을 동적으로 조정할 수 있습니다.
- 4. 본 연구에서는 실제 공격자의 반응성을 고려한 새로운 방어 방법을 제안하며, 이를 통해 반응형 CPI 공격과 공격-방어 군비 경쟁 프레임워크를 도입합니다.
- 5. 제안된 방어 방법은 다양한 모델 공유 시나리오에서 CPI 공격에 대한 방어 효과를 높이고, ML 모델의 유용성을 유지하며, 계산 오버헤드를 줄이는 데 효과적임을 실증적으로 입증했습니다.


---

*Generated on 2025-09-23 23:16:19*