<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:54:44.342705",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning",
    "Zero-Shot Learning",
    "Markov Decision Process"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Reinforcement Learning": 0.82,
    "Zero-Shot Learning": 0.79,
    "Markov Decision Process": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's approach and connect to various advanced AI applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a key component of the proposed method, linking to many AI optimization techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-Shot Capability",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning highlights the model's ability to generalize without prior examples, a trending topic in AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Markov Decision Process",
        "canonical": "Markov Decision Process",
        "aliases": [
          "MDP"
        ],
        "category": "specific_connectable",
        "rationale": "MDP is crucial for understanding the multi-step decision framework used in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.77,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-Shot Capability",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Markov Decision Process",
      "resolved_canonical": "Markov Decision Process",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.77,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18719.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18719](https://arxiv.org/abs/2509.18719)

## 🔗 유사한 논문
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (87.1% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (85.9% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (85.7% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (85.2% similar)
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (84.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Markov Decision Process|Markov Decision Process]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18719v1 Announce Type: new 
Abstract: This paper presents a novel approach to e-commerce payment fraud detection by integrating reinforcement learning (RL) with Large Language Models (LLMs). By framing transaction risk as a multi-step Markov Decision Process (MDP), RL optimizes risk detection across multiple payment stages. Crafting effective reward functions, essential for RL model success, typically requires significant human expertise due to the complexity and variability in design. LLMs, with their advanced reasoning and coding capabilities, are well-suited to refine these functions, offering improvements over traditional methods. Our approach leverages LLMs to iteratively enhance reward functions, achieving better fraud detection accuracy and demonstrating zero-shot capability. Experiments with real-world data confirm the effectiveness, robustness, and resilience of our LLM-enhanced RL framework through long-term evaluations, underscoring the potential of LLMs in advancing industrial RL applications.

## 📝 요약

이 논문은 강화 학습(RL)과 대형 언어 모델(LLM)을 결합하여 전자상거래 결제 사기 탐지를 혁신적으로 개선하는 방법을 제안합니다. 거래 위험을 다단계 마르코프 결정 과정(MDP)으로 설정하여 여러 결제 단계에서 위험 탐지를 최적화합니다. RL 모델의 성공을 위해 중요한 보상 함수 설계는 복잡성과 변동성 때문에 상당한 전문 지식을 요구하지만, LLM은 이를 개선하여 전통적인 방법보다 뛰어난 성능을 제공합니다. LLM을 활용해 보상 함수를 반복적으로 개선함으로써 사기 탐지 정확도를 높이고, 제로샷 능력을 입증했습니다. 실제 데이터 실험을 통해 LLM 강화 RL 프레임워크의 효과와 강인함을 확인했으며, 산업 RL 응용 분야에서 LLM의 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. 이 논문은 강화 학습(RL)과 대형 언어 모델(LLM)을 통합하여 전자 상거래 결제 사기 탐지를 개선하는 새로운 접근 방식을 제안합니다.
- 2. 거래 위험을 다단계 마르코프 결정 프로세스(MDP)로 설정하여 RL이 여러 결제 단계에서 위험 탐지를 최적화합니다.
- 3. LLM은 복잡하고 다양한 보상 함수 설계에서 전통적인 방법보다 개선된 기능을 제공하여 RL 모델의 성공을 돕습니다.
- 4. 실제 데이터 실험을 통해 LLM이 강화된 RL 프레임워크의 효과, 견고성 및 회복력을 장기적으로 평가하여 입증했습니다.
- 5. LLM의 제로샷 능력을 활용하여 보상 함수를 반복적으로 개선함으로써 사기 탐지 정확도를 높였습니다.


---

*Generated on 2025-09-24 14:54:44*