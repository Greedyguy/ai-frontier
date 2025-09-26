<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:22:01.852100",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Collaborative Decision-making",
    "Cross-Modal Knowledge Distillation",
    "Connected Autonomy",
    "Multimodal Sensor Fusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Collaborative Decision-making": 0.88,
    "Cross-Modal Knowledge Distillation": 0.85,
    "Connected Autonomy": 0.82,
    "Multimodal Sensor Fusion": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Modal Collaborative Decision-making",
        "canonical": "Multimodal Collaborative Decision-making",
        "aliases": [
          "MMCD"
        ],
        "category": "unique_technical",
        "rationale": "This framework is central to the paper's contribution and represents a novel approach to decision-making in connected autonomous systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "cross-modal knowledge distillation",
        "canonical": "Cross-Modal Knowledge Distillation",
        "aliases": [
          "CMKD"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for the framework's ability to function with incomplete data, linking to broader concepts in knowledge transfer.",
        "novelty_score": 0.75,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "connected autonomy",
        "canonical": "Connected Autonomy",
        "aliases": [
          "connected autonomous systems"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is key to understanding the context and application of the proposed framework, linking to broader autonomous systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.8,
        "specificity_score": 0.76,
        "link_intent_score": 0.82
      },
      {
        "surface": "RGB images and LiDAR point clouds",
        "canonical": "Multimodal Sensor Fusion",
        "aliases": [
          "sensor fusion"
        ],
        "category": "specific_connectable",
        "rationale": "The fusion of these modalities is critical for enhancing decision-making capabilities in autonomous systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "autonomous systems",
      "decision-making",
      "sensor range"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Modal Collaborative Decision-making",
      "resolved_canonical": "Multimodal Collaborative Decision-making",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "cross-modal knowledge distillation",
      "resolved_canonical": "Cross-Modal Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "connected autonomy",
      "resolved_canonical": "Connected Autonomy",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.8,
        "specificity": 0.76,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "RGB images and LiDAR point clouds",
      "resolved_canonical": "Multimodal Sensor Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MMCD: Multi-Modal Collaborative Decision-Making for Connected Autonomy with Knowledge Distillation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18198.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18198](https://arxiv.org/abs/2509.18198)

## 🔗 유사한 논문
- [[2025-09-22/Towards Interactive and Learnable Cooperative Driving Automation_ a Large Language Model-Driven Decision-Making Framework_20250922|Towards Interactive and Learnable Cooperative Driving Automation: a Large Language Model-Driven Decision-Making Framework]] (85.5% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (84.4% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (84.3% similar)
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (83.1% similar)
- [[2025-09-23/Automating Steering for Safe Multimodal Large Language Models_20250923|Automating Steering for Safe Multimodal Large Language Models]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Cross-Modal Knowledge Distillation|Cross-Modal Knowledge Distillation]], [[keywords/Connected Autonomy|Connected Autonomy]], [[keywords/Multimodal Sensor Fusion|Multimodal Sensor Fusion]]
**⚡ Unique Technical**: [[keywords/Multimodal Collaborative Decision-making|Multimodal Collaborative Decision-making]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18198v1 Announce Type: new 
Abstract: Autonomous systems have advanced significantly, but challenges persist in accident-prone environments where robust decision-making is crucial. A single vehicle's limited sensor range and obstructed views increase the likelihood of accidents. Multi-vehicle connected systems and multi-modal approaches, leveraging RGB images and LiDAR point clouds, have emerged as promising solutions. However, existing methods often assume the availability of all data modalities and connected vehicles during both training and testing, which is impractical due to potential sensor failures or missing connected vehicles. To address these challenges, we introduce a novel framework MMCD (Multi-Modal Collaborative Decision-making) for connected autonomy. Our framework fuses multi-modal observations from ego and collaborative vehicles to enhance decision-making under challenging conditions. To ensure robust performance when certain data modalities are unavailable during testing, we propose an approach based on cross-modal knowledge distillation with a teacher-student model structure. The teacher model is trained with multiple data modalities, while the student model is designed to operate effectively with reduced modalities. In experiments on $\textit{connected autonomous driving with ground vehicles}$ and $\textit{aerial-ground vehicles collaboration}$, our method improves driving safety by up to ${\it 20.7}\%$, surpassing the best-existing baseline in detecting potential accidents and making safe driving decisions. More information can be found on our website https://ruiiu.github.io/mmcd.

## 📝 요약

이 논문은 사고 발생 가능성이 높은 환경에서 자율 시스템의 의사결정을 개선하기 위한 새로운 프레임워크 MMCD를 제안합니다. 기존 방법들은 모든 데이터 모달리티와 연결된 차량의 가용성을 가정하지만, 이는 센서 고장이나 차량 누락으로 비현실적입니다. MMCD는 자차와 협력 차량의 다중 모달 관측을 융합하여 어려운 조건에서도 의사결정을 강화합니다. 특히, 테스트 시 특정 데이터 모달리티가 없을 경우에도 강력한 성능을 보장하기 위해 교사-학생 모델 구조의 크로스 모달 지식 증류 방법을 제안합니다. 실험 결과, 연결 자율 주행 및 공중-지상 차량 협력 시 주행 안전성을 최대 20.7% 향상시켜 기존 방법을 능가했습니다.

## 🎯 주요 포인트

- 1. 자율 시스템은 사고 발생 환경에서의 강력한 의사결정이 중요하지만, 단일 차량의 제한된 센서 범위와 시야 방해로 사고 가능성이 증가합니다.
- 2. 다중 차량 연결 시스템과 다중 모달 접근법이 RGB 이미지와 LiDAR 포인트 클라우드를 활용하여 유망한 해결책으로 부상하고 있습니다.
- 3. 기존 방법은 모든 데이터 모달리티와 연결된 차량의 가용성을 가정하지만, 이는 센서 고장이나 연결 차량의 부재로 인해 비현실적입니다.
- 4. MMCD(다중 모달 협력적 의사결정) 프레임워크는 자아 및 협력 차량의 다중 모달 관측을 융합하여 어려운 조건에서 의사결정을 향상시킵니다.
- 5. 교사-학생 모델 구조를 기반으로 한 교차 모달 지식 증류 접근법을 통해 테스트 중 특정 데이터 모달리티가 불가능한 경우에도 강력한 성능을 보장합니다.


---

*Generated on 2025-09-24 13:22:01*