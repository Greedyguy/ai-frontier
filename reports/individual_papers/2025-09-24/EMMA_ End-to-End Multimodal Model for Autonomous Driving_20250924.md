<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:25:59.273820",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Large Language Model",
    "Motion Planning",
    "3D Object Detection",
    "Road Graph Elements"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Large Language Model": 0.85,
    "Motion Planning": 0.78,
    "3D Object Detection": 0.77,
    "Road Graph Elements": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Model",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal",
          "Multimodal Approach"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key concept in integrating multiple data types, crucial for autonomous driving systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are foundational to EMMA's architecture, enabling natural language processing capabilities.",
        "novelty_score": 0.4,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Motion Planning",
        "canonical": "Motion Planning",
        "aliases": [
          "Trajectory Planning"
        ],
        "category": "unique_technical",
        "rationale": "Motion Planning is a critical task in autonomous driving, directly addressed by EMMA.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D Object Detection",
        "canonical": "3D Object Detection",
        "aliases": [
          "3D Detection",
          "Object Detection"
        ],
        "category": "unique_technical",
        "rationale": "3D Object Detection is essential for understanding the driving environment, a core function of EMMA.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Road Graph Elements",
        "canonical": "Road Graph Elements",
        "aliases": [
          "Road Graphs",
          "Graph Elements"
        ],
        "category": "unique_technical",
        "rationale": "Road Graph Elements are vital for mapping and navigation tasks in autonomous driving.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "planner trajectories",
      "perception objects",
      "world knowledge"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Motion Planning",
      "resolved_canonical": "Motion Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D Object Detection",
      "resolved_canonical": "3D Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Road Graph Elements",
      "resolved_canonical": "Road Graph Elements",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# EMMA: End-to-End Multimodal Model for Autonomous Driving

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.23262.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2410.23262](https://arxiv.org/abs/2410.23262)

## 🔗 유사한 논문
- [[2025-09-19/VLM-E2E_ Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion_20250919|VLM-E2E: Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion]] (84.0% similar)
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (83.7% similar)
- [[2025-09-22/Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models_20250922|Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models]] (83.1% similar)
- [[2025-09-17/MAP_ End-to-End Autonomous Driving with Map-Assisted Planning_20250917|MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (82.1% similar)
- [[2025-09-23/LEO-MINI_ An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts_20250923|LEO-MINI: An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Motion Planning|Motion Planning]], [[keywords/3D Object Detection|3D Object Detection]], [[keywords/Road Graph Elements|Road Graph Elements]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.23262v3 Announce Type: replace-cross 
Abstract: We introduce EMMA, an End-to-end Multimodal Model for Autonomous driving. Built upon a multi-modal large language model foundation like Gemini, EMMA directly maps raw camera sensor data into various driving-specific outputs, including planner trajectories, perception objects, and road graph elements. EMMA maximizes the utility of world knowledge from the pre-trained large language models, by representing all non-sensor inputs (e.g. navigation instructions and ego vehicle status) and outputs (e.g. trajectories and 3D locations) as natural language text. This approach allows EMMA to jointly process various driving tasks in a unified language space, and generate the outputs for each task using task-specific prompts. Empirically, we demonstrate EMMA's effectiveness by achieving state-of-the-art performance in motion planning on nuScenes as well as competitive results on the Waymo Open Motion Dataset (WOMD). EMMA also yields competitive results for camera-primary 3D object detection on the Waymo Open Dataset (WOD). We show that co-training EMMA with planner trajectories, object detection, and road graph tasks yields improvements across all three domains, highlighting EMMA's potential as a generalist model for autonomous driving applications. We hope that our results will inspire research to further evolve the state of the art in autonomous driving model architectures.

## 📝 요약

EMMA는 자율주행을 위한 종단간 멀티모달 모델로, Gemini와 같은 대형 언어 모델을 기반으로 합니다. 이 모델은 카메라 센서 데이터를 주행 계획, 객체 인식, 도로 그래프 요소 등으로 직접 변환합니다. EMMA는 사전 학습된 대형 언어 모델의 세계 지식을 최대한 활용하여 비센서 입력과 출력을 자연어 텍스트로 표현합니다. 이를 통해 다양한 주행 작업을 통합된 언어 공간에서 처리하고, 작업별 프롬프트를 사용해 결과를 생성합니다. 실험 결과, EMMA는 nuScenes에서 모션 플래닝 분야의 최첨단 성능을 보였으며, Waymo Open Motion Dataset에서도 경쟁력 있는 결과를 얻었습니다. 또한, Waymo Open Dataset에서 카메라 기반 3D 객체 탐지에서도 우수한 성능을 보였습니다. 주행 계획, 객체 탐지, 도로 그래프 작업을 함께 학습함으로써 모든 영역에서 성능이 향상되었으며, 이는 EMMA가 자율주행 분야의 범용 모델로서의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. EMMA는 다중 모달 대형 언어 모델을 기반으로 하여 원시 카메라 센서 데이터를 다양한 자율주행 관련 출력으로 직접 매핑합니다.
- 2. 모든 비센서 입력과 출력을 자연어 텍스트로 표현하여 다양한 주행 작업을 통합된 언어 공간에서 처리합니다.
- 3. EMMA는 nuScenes에서 모션 플래닝 분야의 최첨단 성능을 달성하고, Waymo Open Motion Dataset에서도 경쟁력 있는 결과를 보였습니다.
- 4. 플래너 궤적, 객체 탐지, 도로 그래프 작업을 함께 훈련함으로써 모든 분야에서 성능 향상을 이끌어냈습니다.
- 5. EMMA는 자율주행 응용 프로그램을 위한 범용 모델로서의 잠재력을 보여주며, 자율주행 모델 아키텍처의 발전을 위한 연구를 촉진하고자 합니다.


---

*Generated on 2025-09-24 14:25:59*