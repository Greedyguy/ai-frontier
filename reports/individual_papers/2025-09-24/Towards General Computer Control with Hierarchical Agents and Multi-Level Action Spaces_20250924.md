<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:24:10.211241",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hierarchical Reinforcement Learning",
    "Large Language Model",
    "Computer Vision",
    "Meta-actions",
    "Triple-modal State Encoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hierarchical Reinforcement Learning": 0.8,
    "Large Language Model": 0.85,
    "Computer Vision": 0.8,
    "Meta-actions": 0.78,
    "Triple-modal State Encoder": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hierarchical Reinforcement Learning",
        "canonical": "Hierarchical Reinforcement Learning",
        "aliases": [
          "HRL"
        ],
        "category": "unique_technical",
        "rationale": "Hierarchical Reinforcement Learning is central to the paper's approach and offers a distinct method for computer control.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-modal Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "MLLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are a key comparison point in the paper, linking to broader discussions in AI.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision Backbone",
        "canonical": "Computer Vision",
        "aliases": [
          "Vision Model"
        ],
        "category": "broad_technical",
        "rationale": "The vision backbone is crucial for the model's efficiency and links to the field of computer vision.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Meta-actions",
        "canonical": "Meta-actions",
        "aliases": [
          "Meta Action"
        ],
        "category": "unique_technical",
        "rationale": "Meta-actions are a novel mechanism in the paper, enhancing control efficiency and linking to action optimization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Triple-modal State Encoder",
        "canonical": "Triple-modal State Encoder",
        "aliases": [
          "Three-modal Encoder"
        ],
        "category": "unique_technical",
        "rationale": "This encoder is a unique aspect of the framework, handling diverse inputs and linking to state representation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "inference latency",
      "task instructions",
      "keystrokes",
      "mouse events",
      "inference time"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hierarchical Reinforcement Learning",
      "resolved_canonical": "Hierarchical Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-modal Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision Backbone",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Meta-actions",
      "resolved_canonical": "Meta-actions",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Triple-modal State Encoder",
      "resolved_canonical": "Triple-modal State Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Towards General Computer Control with Hierarchical Agents and Multi-Level Action Spaces

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18230.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18230](https://arxiv.org/abs/2509.18230)

## 🔗 유사한 논문
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (86.4% similar)
- [[2025-09-23/Strategic Coordination for Evolving Multi-agent Systems_ A Hierarchical Reinforcement and Collective Learning Approach_20250923|Strategic Coordination for Evolving Multi-agent Systems: A Hierarchical Reinforcement and Collective Learning Approach]] (83.9% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (83.3% similar)
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (83.2% similar)
- [[2025-09-23/Mano Report_20250923|Mano Report]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/Hierarchical Reinforcement Learning|Hierarchical Reinforcement Learning]], [[keywords/Meta-actions|Meta-actions]], [[keywords/Triple-modal State Encoder|Triple-modal State Encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18230v1 Announce Type: new 
Abstract: Controlling desktop applications via software remains a fundamental yet under-served problem. Existing multi-modal large language models (MLLMs) ingest screenshots and task instructions to generate keystrokes and mouse events, but they suffer from prohibitive inference latency, poor sample efficiency on long-horizon sparse-reward tasks, and infeasible on-device deployment. We introduce a lightweight hierarchical reinforcement learning framework, ComputerAgent, that formulates OS control as a two-level option process (manager and subpolicy), employs a triple-modal state encoder (screenshot, task ID, numeric state) to handle visual and contextual diversity, integrates meta-actions with an early-stop mechanism to reduce wasted interactions, and uses a compact vision backbone plus small policy networks for on-device inference (15M parameters). On a suite of 135 real-world desktop tasks, ComputerAgent attains 92.1% success on simple tasks (<8 steps) and 58.8% on hard tasks (>=8 steps), matching or exceeding 200B-parameter MLLM baselines on simple scenarios while reducing model size by over four orders of magnitude and halving inference time. These results demonstrate that hierarchical RL offers a practical, scalable alternative to monolithic MLLM-based automation for computer control.

## 📝 요약

이 논문은 데스크톱 애플리케이션 제어를 위한 경량의 계층적 강화 학습 프레임워크인 ComputerAgent를 제안합니다. 기존의 다중 모달 대형 언어 모델(MLLM)이 스크린샷과 작업 지시를 통해 키 입력과 마우스 이벤트를 생성하는 데 비해, ComputerAgent는 매니저와 하위 정책으로 구성된 2단계 옵션 프로세스를 사용하여 OS 제어를 수행합니다. 이 시스템은 스크린샷, 작업 ID, 숫자 상태를 포함하는 3중 모달 상태 인코더를 활용하여 시각적 및 맥락적 다양성을 처리하며, 메타 액션과 조기 중지 메커니즘을 통합하여 불필요한 상호작용을 줄입니다. 또한, 소형 비전 백본과 작은 정책 네트워크를 사용하여 1,500만 개의 파라미터로 장치 내 추론을 가능하게 합니다. 135개의 실제 데스크톱 작업에서 ComputerAgent는 간단한 작업에서 92.1%, 복잡한 작업에서 58.8%의 성공률을 기록하며, 대형 MLLM 기반 모델과 비교해 모델 크기를 크게 줄이고 추론 시간을 절반으로 단축했습니다. 이러한 결과는 계층적 강화 학습이 컴퓨터 제어 자동화를 위한 실용적이고 확장 가능한 대안임을 보여줍니다.

## 🎯 주요 포인트

- 1. ComputerAgent는 운영 체제 제어를 위한 경량 계층형 강화 학습 프레임워크로, 관리자와 하위 정책의 두 레벨 옵션 프로세스를 사용합니다.
- 2. 이 프레임워크는 스크린샷, 작업 ID, 숫자 상태를 포함한 삼중 모달 상태 인코더를 사용하여 시각적 및 맥락적 다양성을 처리합니다.
- 3. ComputerAgent는 메타 액션과 조기 중지 메커니즘을 통합하여 불필요한 상호작용을 줄이고, 소형 정책 네트워크를 사용하여 장치 내 추론을 가능하게 합니다.
- 4. 135개의 실제 데스크톱 작업에서 ComputerAgent는 간단한 작업에서 92.1%의 성공률을, 어려운 작업에서 58.8%의 성공률을 기록하며, 대규모 MLLM 기반 모델과 비교해 모델 크기를 크게 줄이고 추론 시간을 절반으로 단축했습니다.
- 5. 계층형 강화 학습은 컴퓨터 제어를 위한 실용적이고 확장 가능한 대안으로, 단일체 MLLM 기반 자동화를 대체할 수 있음을 입증합니다.


---

*Generated on 2025-09-24 13:24:10*