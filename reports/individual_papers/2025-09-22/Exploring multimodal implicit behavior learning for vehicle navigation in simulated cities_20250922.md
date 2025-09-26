---
keywords:
  - Implicit Behavioral Cloning
  - Energy-Based Models
  - Data-Augmented Implicit Behavioral Cloning
  - Multimodal Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15400
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:55:37.072886",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Implicit Behavioral Cloning",
    "Energy-Based Models",
    "Data-Augmented Implicit Behavioral Cloning",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Implicit Behavioral Cloning": 0.78,
    "Energy-Based Models": 0.7,
    "Data-Augmented Implicit Behavioral Cloning": 0.82,
    "Multimodal Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Implicit Behavioral Cloning",
        "canonical": "Implicit Behavioral Cloning",
        "aliases": [
          "IBC"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's exploration of multimodal learning in vehicle navigation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Energy-Based Models",
        "canonical": "Energy-Based Models",
        "aliases": [
          "EBM"
        ],
        "category": "broad_technical",
        "rationale": "EBMs are a foundational concept in the paper's approach to learning multimodal behaviors.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.68,
        "link_intent_score": 0.7
      },
      {
        "surface": "Data-Augmented IBC",
        "canonical": "Data-Augmented Implicit Behavioral Cloning",
        "aliases": [
          "DA-IBC"
        ],
        "category": "unique_technical",
        "rationale": "DA-IBC is a novel enhancement to IBC, crucial for the paper's contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multimodal Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "The paper focuses on learning multiple valid actions, aligning with the concept of multimodal learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Behavior Cloning",
      "CARLA simulator"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Implicit Behavioral Cloning",
      "resolved_canonical": "Implicit Behavioral Cloning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Energy-Based Models",
      "resolved_canonical": "Energy-Based Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.68,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Data-Augmented IBC",
      "resolved_canonical": "Data-Augmented Implicit Behavioral Cloning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multimodal Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Exploring multimodal implicit behavior learning for vehicle navigation in simulated cities

**Korean Title:** 시뮬레이션된 도시에서 차량 내비게이션을 위한 다중 모달 암시적 행동 학습 탐구

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15400.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15400](https://arxiv.org/abs/2509.15400)

## 🔗 유사한 논문
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets]] (81.2% similar)
- [[2025-09-19/Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (79.3% similar)
- [[2025-09-22/Towards Interactive and Learnable Cooperative Driving Automation_ a Large Language Model-Driven Decision-Making Framework_20250922|Towards Interactive and Learnable Cooperative Driving Automation: a Large Language Model-Driven Decision-Making Framework]] (79.1% similar)
- [[2025-09-19/VLM-E2E_ Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion_20250919|VLM-E2E: Enhancing End-to-End Autonomous Driving with Multimodal Driver Attention Fusion]] (78.9% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Energy-Based Models|Energy-Based Models]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Implicit Behavioral Cloning|Implicit Behavioral Cloning]], [[keywords/Data-Augmented Implicit Behavioral Cloning|Data-Augmented Implicit Behavioral Cloning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15400v1 Announce Type: cross 
Abstract: Standard Behavior Cloning (BC) fails to learn multimodal driving decisions, where multiple valid actions exist for the same scenario. We explore Implicit Behavioral Cloning (IBC) with Energy-Based Models (EBMs) to better capture this multimodality. We propose Data-Augmented IBC (DA-IBC), which improves learning by perturbing expert actions to form the counterexamples of IBC training and using better initialization for derivative-free inference. Experiments in the CARLA simulator with Bird's-Eye View inputs demonstrate that DA-IBC outperforms standard IBC in urban driving tasks designed to evaluate multimodal behavior learning in a test environment. The learned energy landscapes are able to represent multimodal action distributions, which BC fails to achieve.

## 🔍 Abstract (한글 번역)

arXiv:2509.15400v1 발표 유형: 교차  
초록: 표준 행동 복제(BC)는 동일한 상황에서 여러 유효한 행동이 존재하는 다중 모드 운전 결정을 학습하는 데 실패합니다. 우리는 에너지 기반 모델(EBM)을 사용한 암묵적 행동 복제(IBC)를 탐구하여 이러한 다중 모드를 더 잘 포착합니다. 우리는 IBC 훈련의 반례를 형성하기 위해 전문가의 행동을 변형하고 파생물 없는 추론을 위한 더 나은 초기화를 사용하여 학습을 개선하는 데이터 증강 IBC(DA-IBC)를 제안합니다. Bird's-Eye View 입력을 사용한 CARLA 시뮬레이터 실험에서 DA-IBC는 테스트 환경에서 다중 모드 행동 학습을 평가하기 위해 설계된 도시 운전 작업에서 표준 IBC보다 우수한 성능을 보였습니다. 학습된 에너지 지형은 BC가 달성하지 못하는 다중 모드 행동 분포를 나타낼 수 있습니다.

## 📝 요약

이 논문은 표준 행동 복제(BC)가 다양한 주행 결정을 학습하는 데 한계가 있음을 지적하고, 이를 개선하기 위해 에너지 기반 모델(EBM)을 활용한 암묵적 행동 복제(IBC)를 탐구합니다. 저자들은 데이터 증강 IBC(DA-IBC)를 제안하여 전문가의 행동을 변형해 반례를 만들고, 파생 없는 추론을 위한 초기화를 개선함으로써 학습 성능을 향상시킵니다. CARLA 시뮬레이터 실험 결과, DA-IBC는 도시 주행 과제에서 표준 IBC보다 뛰어난 성능을 보였으며, 에너지 경관을 통해 BC가 실패한 다중 모달 행동 분포를 효과적으로 표현할 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 표준 행동 복제(BC)는 동일한 상황에서 여러 유효한 행동이 존재하는 다중 모드 운전 결정을 학습하는 데 실패한다.
- 2. 에너지 기반 모델(EBM)을 활용한 암묵적 행동 복제(IBC)는 다중 모드성을 더 잘 포착할 수 있다.
- 3. 데이터 증강 IBC(DA-IBC)는 전문가 행동을 변형하여 IBC 훈련의 반례를 형성하고 파생 없는 추론을 위한 더 나은 초기화를 사용하여 학습을 개선한다.
- 4. CARLA 시뮬레이터에서 Bird's-Eye View 입력을 사용한 실험 결과, DA-IBC는 테스트 환경에서 다중 모드 행동 학습을 평가하기 위해 설계된 도시 운전 작업에서 표준 IBC보다 우수한 성능을 보인다.
- 5. 학습된 에너지 지형은 BC가 달성하지 못하는 다중 모드 행동 분포를 표현할 수 있다.


---

*Generated on 2025-09-23 08:55:37*