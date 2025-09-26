<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:34:25.195592",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Video-Based Failure Detection",
    "Spatio-Temporal Knowledge",
    "Task-Relevant Objects",
    "Data Augmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Video-Based Failure Detection": 0.78,
    "Spatio-Temporal Knowledge": 0.8,
    "Task-Relevant Objects": 0.75,
    "Data Augmentation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "video-based failure detection",
        "canonical": "Video-Based Failure Detection",
        "aliases": [
          "video failure detection",
          "video-based detection"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and is specific to the domain of robotics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "spatio-temporal knowledge",
        "canonical": "Spatio-Temporal Knowledge",
        "aliases": [
          "spatio-temporal information",
          "spatial and temporal knowledge"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the method's application in robotics and links to broader topics in AI.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      },
      {
        "surface": "task-relevant objects",
        "canonical": "Task-Relevant Objects",
        "aliases": [
          "task objects",
          "relevant objects"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding task-relevant objects is essential for contextualizing the robot's actions, linking to object recognition.",
        "novelty_score": 0.64,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      },
      {
        "surface": "data augmentation method",
        "canonical": "Data Augmentation",
        "aliases": [
          "augmentation method",
          "data augmentation technique"
        ],
        "category": "broad_technical",
        "rationale": "Data augmentation is a widely applicable technique in machine learning, enhancing model performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "execution failures",
      "safe operation modes",
      "recovery strategies",
      "task replanning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "video-based failure detection",
      "resolved_canonical": "Video-Based Failure Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "spatio-temporal knowledge",
      "resolved_canonical": "Spatio-Temporal Knowledge",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "task-relevant objects",
      "resolved_canonical": "Task-Relevant Objects",
      "decision": "linked",
      "scores": {
        "novelty": 0.64,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "data augmentation method",
      "resolved_canonical": "Data Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Enhancing Video-Based Robot Failure Detection Using Task Knowledge

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2508.18705.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2508.18705](https://arxiv.org/abs/2508.18705)

## 🔗 유사한 논문
- [[2025-09-23/KRAST_ Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models_20250923|KRAST: Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models]] (84.0% similar)
- [[2025-09-23/Look, Focus, Act_ Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers_20250923|Look, Focus, Act: Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers]] (82.2% similar)
- [[2025-09-23/Sight Over Site_ Perception-Aware Reinforcement Learning for Efficient Robotic Inspection_20250923|Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection]] (81.7% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (81.6% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Data Augmentation|Data Augmentation]]
**🔗 Specific Connectable**: [[keywords/Spatio-Temporal Knowledge|Spatio-Temporal Knowledge]], [[keywords/Task-Relevant Objects|Task-Relevant Objects]]
**⚡ Unique Technical**: [[keywords/Video-Based Failure Detection|Video-Based Failure Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.18705v2 Announce Type: replace-cross 
Abstract: Robust robotic task execution hinges on the reliable detection of execution failures in order to trigger safe operation modes, recovery strategies, or task replanning. However, many failure detection methods struggle to provide meaningful performance when applied to a variety of real-world scenarios. In this paper, we propose a video-based failure detection approach that uses spatio-temporal knowledge in the form of the actions the robot performs and task-relevant objects within the field of view. Both pieces of information are available in most robotic scenarios and can thus be readily obtained. We demonstrate the effectiveness of our approach on three datasets that we amend, in part, with additional annotations of the aforementioned task-relevant knowledge. In light of the results, we also propose a data augmentation method that improves performance by applying variable frame rates to different parts of the video. We observe an improvement from 77.9 to 80.0 in F1 score on the ARMBench dataset without additional computational expense and an additional increase to 81.4 with test-time augmentation. The results emphasize the importance of spatio-temporal information during failure detection and suggest further investigation of suitable heuristics in future implementations. Code and annotations are available.

## 📝 요약

이 논문은 로봇 작업 수행 중 발생할 수 있는 실패를 감지하는 비디오 기반 방법을 제안합니다. 로봇의 행동과 작업 관련 객체에 대한 시공간적 정보를 활용하여 다양한 실제 시나리오에서의 실패 감지 성능을 향상시킵니다. 세 가지 데이터셋에서의 실험 결과, 제안된 방법은 F1 점수를 77.9에서 80.0으로, 테스트 시 데이터 증강을 통해 81.4까지 향상시켰습니다. 이 연구는 실패 감지에서 시공간 정보의 중요성을 강조하며, 향후 적절한 휴리스틱 탐색의 필요성을 제시합니다. 코드와 주석은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 로봇 작업 실행의 실패 감지는 안전한 작동 모드, 복구 전략, 또는 작업 재계획을 유도하는 데 중요합니다.
- 2. 본 논문에서는 로봇의 행동과 작업 관련 객체의 시공간적 정보를 활용한 비디오 기반 실패 감지 방법을 제안합니다.
- 3. 제안된 방법은 세 가지 데이터셋에서 효과적임을 입증하였으며, 데이터 증강 방법을 통해 성능을 향상시켰습니다.
- 4. ARMBench 데이터셋에서 F1 점수가 77.9에서 80.0으로 개선되었으며, 테스트 시 증강을 통해 81.4까지 증가했습니다.
- 5. 연구 결과는 실패 감지 시 시공간 정보의 중요성을 강조하며, 향후 구현에서 적절한 휴리스틱의 추가 연구를 제안합니다.


---

*Generated on 2025-09-24 16:34:25*