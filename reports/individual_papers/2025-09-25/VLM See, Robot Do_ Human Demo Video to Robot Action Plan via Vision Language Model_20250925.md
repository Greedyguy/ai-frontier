---
keywords:
  - Vision-Language Model
  - Human Demonstration Videos
  - Task Planning
  - Pick-and-Place Tasks
  - Simulation Environment
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2410.08792
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:17:23.544693",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Human Demonstration Videos",
    "Task Planning",
    "Pick-and-Place Tasks",
    "Simulation Environment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Human Demonstration Videos": 0.72,
    "Task Planning": 0.8,
    "Pick-and-Place Tasks": 0.7,
    "Simulation Environment": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision Language Model"
        ],
        "category": "evolved_concepts",
        "rationale": "Links to the concept of integrating vision and language for robotics, a trending area of research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.67,
        "link_intent_score": 0.85
      },
      {
        "surface": "human demonstration videos",
        "canonical": "Human Demonstration Videos",
        "aliases": [
          "demonstration videos",
          "human demos"
        ],
        "category": "unique_technical",
        "rationale": "Specific to the method of using videos for robot task planning, which is novel in this context.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "task planning",
        "canonical": "Task Planning",
        "aliases": [
          "robot task planning"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's contribution in translating human actions to robot tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "pick-and-place tasks",
        "canonical": "Pick-and-Place Tasks",
        "aliases": [
          "pick and place"
        ],
        "category": "unique_technical",
        "rationale": "A specific type of task used for benchmarking in robotics, relevant for linking to task-specific research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "simulation environment",
        "canonical": "Simulation Environment",
        "aliases": [
          "simulated environment"
        ],
        "category": "specific_connectable",
        "rationale": "Important for understanding the testing and deployment context of the robot tasks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.77,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.67,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "human demonstration videos",
      "resolved_canonical": "Human Demonstration Videos",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "task planning",
      "resolved_canonical": "Task Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "pick-and-place tasks",
      "resolved_canonical": "Pick-and-Place Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "simulation environment",
      "resolved_canonical": "Simulation Environment",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.77,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.08792.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2410.08792](https://arxiv.org/abs/2410.08792)

## 🔗 유사한 논문
- [[2025-09-23/KRAST_ Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models_20250923|KRAST: Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models]] (83.2% similar)
- [[2025-09-18/FSR-VLN_ Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph_20250918|FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (83.1% similar)
- [[2025-09-23/Look, Focus, Act_ Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers_20250923|Look, Focus, Act: Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers]] (82.9% similar)
- [[2025-09-24/Reading Images Like Texts_ Sequential Image Understanding in Vision-Language Models_20250924|Reading Images Like Texts: Sequential Image Understanding in Vision-Language Models]] (82.9% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Task Planning|Task Planning]], [[keywords/Simulation Environment|Simulation Environment]]
**⚡ Unique Technical**: [[keywords/Human Demonstration Videos|Human Demonstration Videos]], [[keywords/Pick-and-Place Tasks|Pick-and-Place Tasks]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.08792v2 Announce Type: replace-cross 
Abstract: Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to ''see'' human demonstrations and explain the corresponding plans to the robot for it to ''do''. To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## 📝 요약

Vision Language Models(VLMs)은 로봇 공학에서 일반화와 상식적 추론 능력으로 주목받고 있습니다. 본 연구에서는 VLM을 활용하여 인간 시범 영상을 해석하고 로봇 작업 계획을 생성하는 방법을 제안합니다. 'SeeDo'라 명명된 이 방법은 키프레임 선택, 시각적 인식, VLM 추론을 통합하여 로봇이 인간 시범을 보고 이해한 계획을 실행할 수 있도록 합니다. 이를 검증하기 위해 다양한 범주의 물체 집기 및 놓기 작업을 시연한 인간 영상 데이터를 수집하고, SeeDo의 성능을 여러 기준으로 평가했습니다. 실험 결과, SeeDo는 기존의 최첨단 VLM을 능가하는 성능을 보였으며, 생성된 작업 계획을 시뮬레이션 환경과 실제 로봇 팔에 성공적으로 적용했습니다.

## 🎯 주요 포인트

- 1. Vision Language Models(VLMs)는 로봇 공학에서 상식적 추론과 일반화 능력으로 채택되고 있다.
- 2. 본 연구는 VLM을 활용하여 인간 시범 영상을 해석하고 로봇 작업 계획을 생성하는 방법을 탐구한다.
- 3. 제안된 방법은 키프레임 선택, 시각적 인식, VLM 추론을 통합하여 'SeeDo'라는 파이프라인을 구성한다.
- 4. SeeDo는 인간 시범을 '보고' 해당 계획을 로봇에게 '설명'하여 수행할 수 있도록 한다.
- 5. 실험 결과, SeeDo는 최첨단 비디오 입력 VLM을 포함한 여러 기준과 비교하여 우수한 성능을 보였다.


---

*Generated on 2025-09-25 16:17:23*