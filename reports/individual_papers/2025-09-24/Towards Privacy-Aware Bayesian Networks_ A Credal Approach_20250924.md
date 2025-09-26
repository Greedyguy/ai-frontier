<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:07:42.994137",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bayesian Network",
    "Credal Network",
    "Probabilistic Graphical Model",
    "Privacy-Aware Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bayesian Network": 0.85,
    "Credal Network": 0.78,
    "Probabilistic Graphical Model": 0.8,
    "Privacy-Aware Modeling": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian networks",
        "canonical": "Bayesian Network",
        "aliases": [
          "BN"
        ],
        "category": "broad_technical",
        "rationale": "Bayesian Networks are a foundational concept in probabilistic graphical models, essential for linking with related technical domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "credal networks",
        "canonical": "Credal Network",
        "aliases": [
          "CN"
        ],
        "category": "unique_technical",
        "rationale": "Credal Networks are introduced as a novel approach for privacy-aware modeling, making them a unique and specific concept in this context.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "probabilistic graphical models",
        "canonical": "Probabilistic Graphical Model",
        "aliases": [
          "PGM"
        ],
        "category": "broad_technical",
        "rationale": "Probabilistic Graphical Models form the basis of Bayesian Networks and are crucial for understanding the paper's context.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "privacy-aware",
        "canonical": "Privacy-Aware Modeling",
        "aliases": [
          "Privacy-Aware"
        ],
        "category": "evolved_concepts",
        "rationale": "Privacy-Aware Modeling is a key theme in the paper, linking privacy concerns with technical modeling approaches.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "tracing attacks",
      "numerical experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian networks",
      "resolved_canonical": "Bayesian Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "credal networks",
      "resolved_canonical": "Credal Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "probabilistic graphical models",
      "resolved_canonical": "Probabilistic Graphical Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "privacy-aware",
      "resolved_canonical": "Privacy-Aware Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Towards Privacy-Aware Bayesian Networks: A Credal Approach

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18949.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18949](https://arxiv.org/abs/2509.18949)

## 🔗 유사한 논문
- [[2025-09-23/Preserving Node-level Privacy in Graph Neural Networks_20250923|Preserving Node-level Privacy in Graph Neural Networks]] (81.5% similar)
- [[2025-09-17/Online Bayesian Risk-Averse Reinforcement Learning_20250917|Online Bayesian Risk-Averse Reinforcement Learning]] (81.4% similar)
- [[2025-09-23/An AI-powered Bayesian generative modeling approach for causal inference in observational studies_20250923|An AI-powered Bayesian generative modeling approach for causal inference in observational studies]] (79.8% similar)
- [[2025-09-23/Train to Defend_ First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks_20250923|Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks]] (79.5% similar)
- [[2025-09-23/Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits_20250923|Information Fusion Using Transferable Belief Functions Implemented on Quantum Circuits]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Network|Bayesian Network]], [[keywords/Probabilistic Graphical Model|Probabilistic Graphical Model]]
**⚡ Unique Technical**: [[keywords/Credal Network|Credal Network]]
**🚀 Evolved Concepts**: [[keywords/Privacy-Aware Modeling|Privacy-Aware Modeling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18949v1 Announce Type: cross 
Abstract: Bayesian networks (BN) are probabilistic graphical models that enable efficient knowledge representation and inference. These have proven effective across diverse domains, including healthcare, bioinformatics and economics. The structure and parameters of a BN can be obtained by domain experts or directly learned from available data. However, as privacy concerns escalate, it becomes increasingly critical for publicly released models to safeguard sensitive information in training data. Typically, released models do not prioritize privacy by design. In particular, tracing attacks from adversaries can combine the released BN with auxiliary data to determine whether specific individuals belong to the data from which the BN was learned. State-of-the-art protection tecniques involve introducing noise into the learned parameters. While this offers robust protection against tracing attacks, it significantly impacts the model's utility, in terms of both the significance and accuracy of the resulting inferences. Hence, high privacy may be attained at the cost of releasing a possibly ineffective model. This paper introduces credal networks (CN) as a novel solution for balancing the model's privacy and utility. After adapting the notion of tracing attacks, we demonstrate that a CN enables the masking of the learned BN, thereby reducing the probability of successful attacks. As CNs are obfuscated but not noisy versions of BNs, they can achieve meaningful inferences while safeguarding privacy. Moreover, we identify key learning information that must be concealed to prevent attackers from recovering the underlying BN. Finally, we conduct a set of numerical experiments to analyze how privacy gains can be modulated by tuning the CN hyperparameters. Our results confirm that CNs provide a principled, practical, and effective approach towards the development of privacy-aware probabilistic graphical models.

## 📝 요약

이 논문은 베이지안 네트워크(BN)의 프라이버시 문제를 해결하기 위해 크레달 네트워크(CN)를 제안합니다. BN은 다양한 분야에서 효과적이지만, 공개된 모델이 개인 정보를 보호하지 못하는 문제가 있습니다. 기존의 보호 방법은 노이즈를 추가해 추적 공격을 방지하지만, 이는 모델의 유용성을 저하시킵니다. CN은 BN을 마스킹하여 공격 성공 확률을 줄이고, 유의미한 추론을 가능하게 하면서도 프라이버시를 보호합니다. 또한, 공격자가 BN을 복구하지 못하도록 숨겨야 할 학습 정보를 식별합니다. 실험 결과, CN은 프라이버시와 유용성을 균형 있게 제공하는 효과적인 방법임을 확인했습니다.

## 🎯 주요 포인트

- 1. 베이지안 네트워크(BN)는 다양한 분야에서 효과적으로 활용되지만, 개인정보 보호 문제를 해결하기 위한 설계가 부족하다.
- 2. 추적 공격은 공개된 BN과 보조 데이터를 결합하여 특정 개인의 데이터 포함 여부를 확인할 수 있다.
- 3. 최신 보호 기술은 학습된 매개변수에 노이즈를 추가하여 추적 공격을 방어하지만, 이는 모델의 유용성을 저하시킨다.
- 4. 크레달 네트워크(CN)는 모델의 프라이버시와 유용성 간의 균형을 맞추기 위한 새로운 해결책으로 제안된다.
- 5. CN은 BN의 학습 정보를 은폐하여 공격의 성공 확률을 줄이며, 의미 있는 추론을 가능하게 한다.


---

*Generated on 2025-09-24 14:07:42*