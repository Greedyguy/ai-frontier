---
keywords:
  - Unfolding Networks
  - Compressed Sensing
  - Adversarial Robustness
  - Adversarial Generalization
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15370
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:22:18.690251",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Unfolding Networks",
    "Compressed Sensing",
    "Adversarial Robustness",
    "Adversarial Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Unfolding Networks": 0.8,
    "Compressed Sensing": 0.82,
    "Adversarial Robustness": 0.85,
    "Adversarial Generalization": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "unfolding networks",
        "canonical": "Unfolding Networks",
        "aliases": [
          "iterative algorithms networks"
        ],
        "category": "unique_technical",
        "rationale": "Unfolding networks are a unique class of neural networks derived from iterative algorithms, relevant for linking to specific neural network architectures.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "compressed sensing",
        "canonical": "Compressed Sensing",
        "aliases": [
          "CS"
        ],
        "category": "specific_connectable",
        "rationale": "Compressed sensing is a key application area for unfolding networks, providing a strong link to inverse problem-solving techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "adversarial robustness",
        "canonical": "Adversarial Robustness",
        "aliases": [
          "robustness against attacks"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial robustness is crucial for ensuring the reliability of neural networks in hostile environments, linking to security-focused research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "adversarial generalization",
        "canonical": "Adversarial Generalization",
        "aliases": [
          "generalization under attack"
        ],
        "category": "unique_technical",
        "rationale": "This concept explores how models perform under adversarial conditions, offering insights into model robustness and generalization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.83,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "inverse problems",
      "medical imaging",
      "cryptography"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "unfolding networks",
      "resolved_canonical": "Unfolding Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "compressed sensing",
      "resolved_canonical": "Compressed Sensing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "adversarial robustness",
      "resolved_canonical": "Adversarial Robustness",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "adversarial generalization",
      "resolved_canonical": "Adversarial Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.83,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Adversarial generalization of unfolding (model-based) networks

**Korean Title:** 전개(모델 기반) 네트워크의 적대적 일반화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15370.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15370](https://arxiv.org/abs/2509.15370)

## 🔗 유사한 논문
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (82.6% similar)
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (81.5% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (80.6% similar)
- [[2025-09-22/Analysis Plug-and-Play Methods for Imaging Inverse Problems_20250922|Analysis Plug-and-Play Methods for Imaging Inverse Problems]] (80.3% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Compressed Sensing|Compressed Sensing]], [[keywords/Adversarial Robustness|Adversarial Robustness]]
**⚡ Unique Technical**: [[keywords/Unfolding Networks|Unfolding Networks]], [[keywords/Adversarial Generalization|Adversarial Generalization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15370v1 Announce Type: new 
Abstract: Unfolding networks are interpretable networks emerging from iterative algorithms, incorporate prior knowledge of data structure, and are designed to solve inverse problems like compressed sensing, which deals with recovering data from noisy, missing observations. Compressed sensing finds applications in critical domains, from medical imaging to cryptography, where adversarial robustness is crucial to prevent catastrophic failures. However, a solid theoretical understanding of the performance of unfolding networks in the presence of adversarial attacks is still in its infancy. In this paper, we study the adversarial generalization of unfolding networks when perturbed with $l_2$-norm constrained attacks, generated by the fast gradient sign method. Particularly, we choose a family of state-of-the-art overaparameterized unfolding networks and deploy a new framework to estimate their adversarial Rademacher complexity. Given this estimate, we provide adversarial generalization error bounds for the networks under study, which are tight with respect to the attack level. To our knowledge, this is the first theoretical analysis on the adversarial generalization of unfolding networks. We further present a series of experiments on real-world data, with results corroborating our derived theory, consistently for all data. Finally, we observe that the family's overparameterization can be exploited to promote adversarial robustness, shedding light on how to efficiently robustify neural networks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15370v1 발표 유형: 신규  
초록: 전개 네트워크는 반복 알고리즘에서 유래한 해석 가능한 네트워크로, 데이터 구조에 대한 사전 지식을 통합하여 압축 센싱과 같은 역문제를 해결하도록 설계되었습니다. 압축 센싱은 의료 영상부터 암호학까지 중요한 분야에서 응용되며, 이들 분야에서는 치명적인 실패를 방지하기 위해 적대적 견고성이 필수적입니다. 그러나 적대적 공격이 있는 상황에서 전개 네트워크의 성능에 대한 견고한 이론적 이해는 아직 초기 단계에 있습니다. 본 논문에서는 빠른 그래디언트 부호 방법에 의해 생성된 $l_2$-노름 제약 공격으로 교란된 전개 네트워크의 적대적 일반화를 연구합니다. 특히, 최첨단 과매개변수화된 전개 네트워크의 계열을 선택하고, 이들의 적대적 라데마허 복잡성을 추정하기 위한 새로운 프레임워크를 배포합니다. 이 추정치를 바탕으로, 연구 중인 네트워크에 대한 적대적 일반화 오류 경계를 제공하며, 이는 공격 수준에 대해 타이트합니다. 우리가 아는 한, 이는 전개 네트워크의 적대적 일반화에 대한 최초의 이론적 분석입니다. 또한, 실제 데이터에 대한 일련의 실험을 제시하며, 모든 데이터에 대해 일관되게 우리의 이론을 뒷받침하는 결과를 보여줍니다. 마지막으로, 계열의 과매개변수화가 적대적 견고성을 촉진하는 데 활용될 수 있음을 관찰하며, 신경망을 효율적으로 견고화하는 방법에 대한 통찰을 제공합니다.

## 📝 요약

이 논문은 반복 알고리즘에서 유래한 해석 가능한 네트워크인 언폴딩 네트워크의 적대적 일반화 성능을 연구합니다. 특히, $l_2$-노름 제한 공격에 대한 네트워크의 성능을 분석하며, 새로운 프레임워크를 통해 적대적 라데마허 복잡성을 추정합니다. 이를 바탕으로 공격 수준에 따른 일반화 오류 경계를 제시하며, 이는 언폴딩 네트워크의 적대적 일반화에 대한 최초의 이론적 분석입니다. 실험 결과는 이론을 뒷받침하며, 과매개변수화가 적대적 강건성을 촉진할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. Unfolding 네트워크는 반복 알고리즘에서 파생된 해석 가능한 네트워크로, 압축 센싱과 같은 역문제를 해결하는 데 사용됩니다.
- 2. 압축 센싱은 의료 영상 및 암호화와 같은 중요한 분야에서 활용되며, 적대적 견고성이 중요합니다.
- 3. 본 연구는 unfolding 네트워크의 적대적 일반화 성능을 $l_2$-노름 제약 공격 하에서 분석하며, 이는 unfolding 네트워크에 대한 최초의 이론적 분석입니다.
- 4. 연구에서는 적대적 Rademacher 복잡성을 추정하기 위한 새로운 프레임워크를 도입하고, 공격 수준에 따라 타이트한 일반화 오류 경계를 제공합니다.
- 5. 실험 결과, 네트워크의 과매개변수가 적대적 견고성을 향상시키는 데 활용될 수 있음을 확인했습니다.


---

*Generated on 2025-09-23 10:22:18*