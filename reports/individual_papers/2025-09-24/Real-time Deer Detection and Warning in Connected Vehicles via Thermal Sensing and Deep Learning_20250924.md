<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:12:57.730511",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Thermal Imaging",
    "Vehicle-to-Everything Communication",
    "Deer-Vehicle Collision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Thermal Imaging": 0.8,
    "Vehicle-to-Everything Communication": 0.78,
    "Deer-Vehicle Collision": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a core technology used in the system, providing strong links to related machine learning and AI research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Thermal Imaging",
        "canonical": "Thermal Imaging",
        "aliases": [
          "Infrared Imaging"
        ],
        "category": "unique_technical",
        "rationale": "Thermal Imaging is a unique aspect of the system, crucial for detection in low visibility conditions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vehicle-to-Everything Communication",
        "canonical": "Vehicle-to-Everything Communication",
        "aliases": [
          "V2X Communication",
          "CV2X"
        ],
        "category": "unique_technical",
        "rationale": "This communication technology is essential for the system's ability to warn surrounding vehicles, offering links to IoT and smart transportation research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deer-Vehicle Collision",
        "canonical": "Deer-Vehicle Collision",
        "aliases": [
          "DVC"
        ],
        "category": "unique_technical",
        "rationale": "The primary problem addressed by the research, linking to studies on wildlife conservation and road safety.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "real-time detection",
      "driver warning system",
      "field testing"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Thermal Imaging",
      "resolved_canonical": "Thermal Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vehicle-to-Everything Communication",
      "resolved_canonical": "Vehicle-to-Everything Communication",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deer-Vehicle Collision",
      "resolved_canonical": "Deer-Vehicle Collision",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Real-time Deer Detection and Warning in Connected Vehicles via Thermal Sensing and Deep Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18779.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18779](https://arxiv.org/abs/2509.18779)

## 🔗 유사한 논문
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (81.4% similar)
- [[2025-09-24/MMCD_ Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation_20250924|MMCD: Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation]] (80.7% similar)
- [[2025-09-23/Multi-Scenario Highway Lane-Change Intention Prediction_ A Physics-Informed AI Framework for Three-Class Classification_20250923|Multi-Scenario Highway Lane-Change Intention Prediction: A Physics-Informed AI Framework for Three-Class Classification]] (79.2% similar)
- [[2025-09-19/Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning_20250919|Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning]] (78.9% similar)
- [[2025-09-23/Vision-Based Driver Drowsiness Monitoring_ Comparative Analysis of YOLOv5-v11 Models_20250923|Vision-Based Driver Drowsiness Monitoring: Comparative Analysis of YOLOv5-v11 Models]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Thermal Imaging|Thermal Imaging]], [[keywords/Vehicle-to-Everything Communication|Vehicle-to-Everything Communication]], [[keywords/Deer-Vehicle Collision|Deer-Vehicle Collision]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18779v1 Announce Type: cross 
Abstract: Deer-vehicle collisions represent a critical safety challenge in the United States, causing nearly 2.1 million incidents annually and resulting in approximately 440 fatalities, 59,000 injuries, and 10 billion USD in economic damages. These collisions also contribute significantly to declining deer populations. This paper presents a real-time detection and driver warning system that integrates thermal imaging, deep learning, and vehicle-to-everything communication to help mitigate deer-vehicle collisions. Our system was trained and validated on a custom dataset of over 12,000 thermal deer images collected in Mars Hill, North Carolina. Experimental evaluation demonstrates exceptional performance with 98.84 percent mean average precision, 95.44 percent precision, and 95.96 percent recall. The system was field tested during a follow-up visit to Mars Hill and readily sensed deer providing the driver with advanced warning. Field testing validates robust operation across diverse weather conditions, with thermal imaging maintaining between 88 and 92 percent detection accuracy in challenging scenarios where conventional visible light based cameras achieve less than 60 percent effectiveness. When a high probability threshold is reached sensor data sharing messages are broadcast to surrounding vehicles and roadside units via cellular vehicle to everything (CV2X) communication devices. Overall, our system achieves end to end latency consistently under 100 milliseconds from detection to driver alert. This research establishes a viable technological pathway for reducing deer-vehicle collisions through thermal imaging and connected vehicles.

## 📝 요약

이 논문은 미국에서 매년 약 210만 건 발생하는 사슴-차량 충돌 문제를 해결하기 위해 열화상, 딥러닝, 차량 간 통신을 통합한 실시간 탐지 및 경고 시스템을 제안합니다. 노스캐롤라이나주 마스 힐에서 수집한 12,000여 장의 열화상 데이터를 기반으로 훈련된 이 시스템은 평균 정밀도 98.84%, 정밀도 95.44%, 재현율 95.96%의 성능을 보였습니다. 다양한 날씨 조건에서도 88~92%의 탐지 정확도를 유지하며, 기존의 가시광 기반 카메라보다 우수한 성능을 입증했습니다. 차량 간 통신을 통해 주변 차량에 경고 메시지를 전송하며, 탐지부터 경고까지의 지연 시간이 100밀리초 이하로 유지됩니다. 이 연구는 열화상과 연결된 차량 기술을 통해 사슴-차량 충돌을 줄일 수 있는 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 미국에서 매년 약 210만 건의 사슴-차량 충돌이 발생하며, 이는 약 440명의 사망자와 59,000명의 부상자, 100억 달러의 경제적 손실을 초래합니다.
- 2. 본 논문은 열화상, 딥러닝, 차량-사물 통신을 통합한 실시간 탐지 및 운전자 경고 시스템을 제안합니다.
- 3. 시스템은 노스캐롤라이나주 마스 힐에서 수집한 12,000개 이상의 열화상 사슴 이미지로 학습 및 검증되었으며, 평균 정밀도 98.84%, 정밀도 95.44%, 재현율 95.96%의 성능을 보였습니다.
- 4. 열화상 카메라는 다양한 날씨 조건에서도 88%에서 92%의 탐지 정확도를 유지하며, 이는 일반 카메라의 60% 미만의 효과성과 비교됩니다.
- 5. 시스템은 탐지부터 운전자 경고까지의 지연 시간을 100밀리초 이하로 유지하며, 사슴-차량 충돌을 줄이기 위한 기술적 경로를 제시합니다.


---

*Generated on 2025-09-24 15:12:57*