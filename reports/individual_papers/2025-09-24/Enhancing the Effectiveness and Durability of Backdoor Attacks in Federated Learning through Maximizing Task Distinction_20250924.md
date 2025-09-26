<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:56:57.163516",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Backdoor Attacks",
    "Computer Vision",
    "Natural Language Processing",
    "Min-Max Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Backdoor Attacks": 0.8,
    "Computer Vision": 0.78,
    "Natural Language Processing": 0.79,
    "Min-Max Optimization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is central to the paper's context and connects to distributed machine learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Backdoor Attacks",
        "canonical": "Backdoor Attacks",
        "aliases": [
          "Backdoor Injection"
        ],
        "category": "unique_technical",
        "rationale": "Backdoor Attacks are a specific threat discussed in the paper, crucial for understanding security in machine learning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [
          "CV"
        ],
        "category": "broad_technical",
        "rationale": "Computer Vision is one of the domains evaluated in the study, linking to visual data processing topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Natural Language Tasks",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "Natural Language Processing is another domain evaluated, relevant to language data processing discussions.",
        "novelty_score": 0.35,
        "connectivity_score": 0.87,
        "specificity_score": 0.67,
        "link_intent_score": 0.79
      },
      {
        "surface": "Min-Max Framework",
        "canonical": "Min-Max Optimization",
        "aliases": [
          "Minimax Framework"
        ],
        "category": "unique_technical",
        "rationale": "The Min-Max Framework is a key methodological innovation in the paper, highlighting optimization techniques.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Backdoor Attacks",
      "resolved_canonical": "Backdoor Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Natural Language Tasks",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.87,
        "specificity": 0.67,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Min-Max Framework",
      "resolved_canonical": "Min-Max Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Enhancing the Effectiveness and Durability of Backdoor Attacks in Federated Learning through Maximizing Task Distinction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18904.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18904](https://arxiv.org/abs/2509.18904)

## 🔗 유사한 논문
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (90.2% similar)
- [[2025-09-24/Backdoor Attack with Invisible Triggers Based on Model Architecture Modification_20250924|Backdoor Attack with Invisible Triggers Based on Model Architecture Modification]] (89.2% similar)
- [[2025-09-23/Rethinking Backdoor Detection Evaluation for Language Models_20250923|Rethinking Backdoor Detection Evaluation for Language Models]] (88.0% similar)
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (87.1% similar)
- [[2025-09-23/Test-Time Multimodal Backdoor Detection by Contrastive Prompting_20250923|Test-Time Multimodal Backdoor Detection by Contrastive Prompting]] (86.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]], [[keywords/Computer Vision|Computer Vision]], [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/Backdoor Attacks|Backdoor Attacks]], [[keywords/Min-Max Optimization|Min-Max Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18904v1 Announce Type: new 
Abstract: Federated learning allows multiple participants to collaboratively train a central model without sharing their private data. However, this distributed nature also exposes new attack surfaces. In particular, backdoor attacks allow attackers to implant malicious behaviors into the global model while maintaining high accuracy on benign inputs. Existing attacks usually rely on fixed patterns or adversarial perturbations as triggers, which tightly couple the main and backdoor tasks. This coupling makes them vulnerable to dilution by honest updates and limits their persistence under federated defenses. In this work, we propose an approach to decouple the backdoor task from the main task by dynamically optimizing the backdoor trigger within a min-max framework. The inner layer maximizes the performance gap between poisoned and benign samples, ensuring that the contributions of benign users have minimal impact on the backdoor. The outer process injects the adaptive triggers into the local model. We evaluate our method on both computer vision and natural language tasks, and compare it with six backdoor attack methods under six defense algorithms. Experimental results show that our method achieves good attack performance and can be easily integrated into existing backdoor attack techniques.

## 📝 요약

이 논문은 연합 학습에서 발생할 수 있는 백도어 공격을 다루며, 기존의 고정된 패턴이나 적대적 교란을 사용하는 방법의 한계를 극복하고자 한다. 제안된 방법은 백도어 작업과 주요 작업을 분리하여 연합 방어 하에서도 지속성을 유지할 수 있도록 한다. 이를 위해 미니맥스 프레임워크를 활용하여 백도어 트리거를 동적으로 최적화하며, 악성 샘플과 정상 샘플 간의 성능 차이를 최대화한다. 실험 결과, 제안된 방법은 컴퓨터 비전 및 자연어 처리 과제에서 기존의 여섯 가지 백도어 공격 및 방어 알고리즘과 비교했을 때 우수한 성능을 보이며, 기존 기술에 쉽게 통합될 수 있음을 보여준다.

## 🎯 주요 포인트

- 1. 연합 학습은 개인 데이터를 공유하지 않고 중앙 모델을 공동으로 훈련할 수 있게 하지만, 새로운 공격 표면을 노출시킵니다.
- 2. 백도어 공격은 악의적인 행동을 글로벌 모델에 심으면서도 정상 입력에 대해 높은 정확도를 유지할 수 있습니다.
- 3. 기존의 공격은 고정된 패턴이나 적대적 교란을 트리거로 사용하여 주 작업과 백도어 작업이 밀접하게 연결되어 있습니다.
- 4. 본 연구에서는 백도어 작업을 주 작업과 분리하여 동적으로 백도어 트리거를 최적화하는 방법을 제안합니다.
- 5. 제안된 방법은 컴퓨터 비전 및 자연어 작업에서 기존의 백도어 공격 기법과 비교하여 우수한 공격 성능을 보이며, 기존 기술에 쉽게 통합될 수 있습니다.


---

*Generated on 2025-09-24 14:56:57*