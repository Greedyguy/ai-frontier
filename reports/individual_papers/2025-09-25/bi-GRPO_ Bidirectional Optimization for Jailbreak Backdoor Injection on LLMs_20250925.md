---
keywords:
  - Large Language Model
  - Jailbreak Backdoor Attacks
  - Reinforcement Learning from Human Feedback
  - Bidirectional Group Relative Policy Optimization
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19775
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:49:19.368121",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Jailbreak Backdoor Attacks",
    "Reinforcement Learning from Human Feedback",
    "Bidirectional Group Relative Policy Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Jailbreak Backdoor Attacks": 0.8,
    "Reinforcement Learning from Human Feedback": 0.78,
    "Bidirectional Group Relative Policy Optimization": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on jailbreak backdoor attacks, facilitating connections with existing research in this area.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "jailbreak backdoor attacks",
        "canonical": "Jailbreak Backdoor Attacks",
        "aliases": [
          "backdoor injection",
          "jailbreak attacks"
        ],
        "category": "unique_technical",
        "rationale": "This term is a unique technical focus of the paper, highlighting a specific type of adversarial manipulation in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "reinforcement learning from human feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "specific_connectable",
        "rationale": "RLHF is a significant method discussed in the paper, relevant for linking to broader reinforcement learning and human-in-the-loop studies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "bi-GRPO",
        "canonical": "Bidirectional Group Relative Policy Optimization",
        "aliases": [
          "bi-GRPO"
        ],
        "category": "unique_technical",
        "rationale": "bi-GRPO is a novel framework introduced in the paper, crucial for understanding the proposed solution to jailbreak attacks.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "jailbreak backdoor attacks",
      "resolved_canonical": "Jailbreak Backdoor Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "reinforcement learning from human feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "bi-GRPO",
      "resolved_canonical": "Bidirectional Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# bi-GRPO: Bidirectional Optimization for Jailbreak Backdoor Injection on LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19775.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19775](https://arxiv.org/abs/2509.19775)

## 🔗 유사한 논문
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (87.6% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (87.2% similar)
- [[2025-09-23/Targeting Alignment_ Extracting Safety Classifiers of Aligned LLMs_20250923|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs]] (86.1% similar)
- [[2025-09-23/AdaptiveGuard_ Towards Adaptive Runtime Safety for LLM-Powered Software_20250923|AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software]] (85.8% similar)
- [[2025-09-23/Rethinking Backdoor Detection Evaluation for Language Models_20250923|Rethinking Backdoor Detection Evaluation for Language Models]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]]
**⚡ Unique Technical**: [[keywords/Jailbreak Backdoor Attacks|Jailbreak Backdoor Attacks]], [[keywords/Bidirectional Group Relative Policy Optimization|Bidirectional Group Relative Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19775v1 Announce Type: cross 
Abstract: With the rapid advancement of large language models (LLMs), their robustness against adversarial manipulations, particularly jailbreak backdoor attacks, has become critically important. Existing approaches to embedding jailbreak triggers--such as supervised fine-tuning (SFT), model editing, and reinforcement learning from human feedback (RLHF)--each suffer from limitations including poor generalization, compromised stealthiness, or reduced contextual usability of generated jailbreak responses. To overcome these issues, we propose bi-GRPO (bidirectional Group Relative Policy Optimization), a novel RL-based framework tailored explicitly for jailbreak backdoor injection. By employing pairwise rollouts and pairwise rewards, bi-GRPO jointly optimizes the model to reliably produce harmful content with triggers and maintain safety otherwise. Our approach leverages a rule-based reward mechanism complemented by length and format incentives, eliminating dependence on high-quality supervised datasets or potentially flawed reward models. Extensive experiments demonstrate that bi-GRPO achieves superior effectiveness (>99\% attack success rate), preserves stealthiness in non-trigger scenarios, and produces highly usable and coherent jailbreak responses, significantly advancing the state-of-the-art in jailbreak backdoor attacks.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 보안 취약점, 특히 탈옥 백도어 공격에 대한 저항성을 개선하기 위한 연구를 다룹니다. 기존의 방법론인 지도 학습, 모델 편집, 인간 피드백을 통한 강화 학습은 일반화 부족, 은밀성 저하, 문맥 사용성 감소 등의 문제를 겪습니다. 이를 해결하기 위해, 저자들은 bi-GRPO라는 새로운 강화 학습 기반 프레임워크를 제안합니다. 이 방법은 쌍별 롤아웃과 보상을 활용하여 모델이 트리거가 있을 때는 유해한 콘텐츠를 생성하고, 그렇지 않을 때는 안전성을 유지하도록 최적화합니다. 실험 결과, bi-GRPO는 99% 이상의 공격 성공률을 기록하며, 트리거가 없는 상황에서 은밀성을 유지하고, 사용 가능하고 일관된 탈옥 응답을 생성하는 데 뛰어난 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 발전과 함께, 탈옥 백도어 공격에 대한 모델의 견고성이 중요해지고 있다.
- 2. 기존의 탈옥 트리거 삽입 방법들은 일반화 부족, 은밀성 저하, 생성된 탈옥 응답의 맥락적 사용성 감소 등의 한계를 가지고 있다.
- 3. bi-GRPO는 탈옥 백도어 주입을 위해 설계된 새로운 강화 학습 기반 프레임워크로, 쌍별 롤아웃과 보상을 활용하여 모델을 최적화한다.
- 4. 이 접근법은 고품질의 지도 데이터셋이나 결함 있는 보상 모델에 의존하지 않고, 규칙 기반 보상 메커니즘을 사용하여 효과적인 탈옥 응답을 생성한다.
- 5. 실험 결과, bi-GRPO는 높은 공격 성공률(>99%)을 달성하고, 비트리거 시나리오에서 은밀성을 유지하며, 사용 가능하고 일관된 탈옥 응답을 생성한다.


---

*Generated on 2025-09-25 15:49:19*