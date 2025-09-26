<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:45:31.534684",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning",
    "Online Process Reward Learning",
    "Process Reward Model",
    "Trajectory Preferences"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Reinforcement Learning": 0.8,
    "Online Process Reward Learning": 0.9,
    "Process Reward Model": 0.75,
    "Trajectory Preferences": 0.78
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
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and are a key component in many AI systems, providing strong connectivity.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
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
        "rationale": "Reinforcement Learning is a fundamental concept in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Online Process Reward Learning",
        "canonical": "Online Process Reward Learning",
        "aliases": [
          "OPRL"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel method introduced in the paper, essential for understanding the contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.9
      },
      {
        "surface": "Process Reward Model",
        "canonical": "Process Reward Model",
        "aliases": [
          "PRM"
        ],
        "category": "unique_technical",
        "rationale": "The Process Reward Model is a key component of the proposed strategy, enabling deeper insights into the methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Trajectory Preferences",
        "canonical": "Trajectory Preferences",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Trajectory Preferences are integral to the reward learning process, offering a unique angle for exploration.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "autonomous agents",
      "interactive environments",
      "temporal credit assignment"
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
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Online Process Reward Learning",
      "resolved_canonical": "Online Process Reward Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Process Reward Model",
      "resolved_canonical": "Process Reward Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Trajectory Preferences",
      "resolved_canonical": "Trajectory Preferences",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Online Process Reward Leanring for Agentic Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19199.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19199](https://arxiv.org/abs/2509.19199)

## 🔗 유사한 논문
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (86.4% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (85.7% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (85.1% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (85.1% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Trajectory Preferences|Trajectory Preferences]]
**⚡ Unique Technical**: [[keywords/Online Process Reward Learning|Online Process Reward Learning]], [[keywords/Process Reward Model|Process Reward Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19199v1 Announce Type: new 
Abstract: Large language models (LLMs) are increasingly trained with reinforcement learning (RL) as autonomous agents that reason and act over long horizons in interactive environments.
  However, sparse and sometimes unverifiable rewards make temporal credit assignment extremely challenging.
  Recent work attempts to integrate process supervision into agent learning but suffers from biased annotation, reward hacking, high-variance from overly fine-grained signals or failtures when state overlap is rare.
  We therefore introduce Online Process Reward Learning (OPRL), a general credit-assignment strategy for agentic RL that integrates seamlessly with standard on-policy algorithms without relying on additional rollouts or explicit step labels.
  In OPRL, we optimize an implicit process reward model (PRM) alternately with the agent's policy to transform trajectory preferences into implicit step rewards through a trajectory-based DPO objective.
  These step rewards are then used to compute step-level advantages, which are combined with episode-level advantages from outcome rewards for policy update, creating a self-reinforcing loop.
  Theoretical findings guarantee that the learned step rewards are consistent with trajectory preferences and act as potential-based shaping rewards, providing bounded gradients to stabilize training.
  Empirically, we evaluate OPRL on three distinct agent benmarks, including WebShop and VisualSokoban, as well as open-ended social interactions with unverfiable rewards in SOTOPIA.
  Crucially, OPRL shows superior performance over frontier LLMs and strong RL baselines across domains, achieving state-of-the-art results with higher sample-efficiency and lower variance during training.
  Further analysis also demonstrates the efficient exploration by OPRL using fewer actions, underscoring its potential for agentic learning in real-world scenarios.

## 📝 요약

이 논문은 강화 학습(RL)을 사용하는 대형 언어 모델(LLM)의 학습에서 발생하는 보상 할당 문제를 해결하기 위해 온라인 프로세스 보상 학습(OPRL)을 제안합니다. OPRL은 명시적인 단계 레이블 없이 표준 정책 알고리즘과 통합되어 궤적 기반 목표를 통해 암묵적인 단계 보상을 최적화합니다. 이 방법은 궤적 선호도를 일관되게 반영하며, 잠재적 기반의 보상으로 작용하여 훈련을 안정화합니다. 실험 결과, OPRL은 다양한 에이전트 벤치마크에서 높은 샘플 효율성과 낮은 분산으로 최첨단 성능을 보이며, 실제 시나리오에서의 에이전트 학습에 대한 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 점점 더 강화 학습(RL)을 통해 장기적인 상호작용 환경에서 자율 에이전트로 훈련되고 있다.
- 2. 희소하고 때로는 검증 불가능한 보상으로 인해 시간적 신용 할당이 매우 어려운 문제로 남아 있다.
- 3. Online Process Reward Learning(OPRL)은 에이전트 RL을 위한 일반적인 신용 할당 전략으로, 추가적인 롤아웃이나 명시적인 단계 레이블 없이 표준 온-정책 알고리즘과 원활하게 통합된다.
- 4. OPRL은 경로 기반 DPO 목표를 통해 경로 선호도를 암묵적인 단계 보상으로 변환하여 정책 업데이트를 위한 자기 강화 루프를 생성한다.
- 5. OPRL은 세 가지 에이전트 벤치마크에서 최첨단 성능을 보이며, 더 높은 샘플 효율성과 낮은 분산을 통해 훈련 중 우수한 성능을 보여준다.


---

*Generated on 2025-09-24 15:45:31*