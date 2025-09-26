<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:48:07.854728",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Hybrid Solver",
    "Vehicle Routing Problem",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Hybrid Solver": 0.78,
    "Vehicle Routing Problem": 0.82,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a subset of Machine Learning, providing a strong link to broader technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hybrid Solver",
        "canonical": "Hybrid Solver",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The hybrid solver is a unique method introduced in the paper, relevant for linking to specific problem-solving techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Truck-Drone VRP",
        "canonical": "Vehicle Routing Problem",
        "aliases": [
          "VRP"
        ],
        "category": "specific_connectable",
        "rationale": "The Truck-Drone VRP is a specific instance of the Vehicle Routing Problem, allowing connections to logistics and optimization research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      },
      {
        "surface": "Attention Policy",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Pointer Policy"
        ],
        "category": "specific_connectable",
        "rationale": "The attention policy is a specific application of the Attention Mechanism, facilitating links to neural network research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "last-mile delivery",
      "battery management",
      "makespan"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hybrid Solver",
      "resolved_canonical": "Hybrid Solver",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Truck-Drone VRP",
      "resolved_canonical": "Vehicle Routing Problem",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Attention Policy",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# A Simple and Reproducible Hybrid Solver for a Truck-Drone VRP with Recharge

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18162.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18162](https://arxiv.org/abs/2509.18162)

## 🔗 유사한 논문
- [[2025-09-23/Accelerating Vehicle Routing via AI-Initialized Genetic Algorithms_20250923|Accelerating Vehicle Routing via AI-Initialized Genetic Algorithms]] (83.5% similar)
- [[2025-09-17/Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection_20250917|Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection]] (82.6% similar)
- [[2025-09-23/Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection_20250923|Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection]] (82.3% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (82.0% similar)
- [[2025-09-23/Reinforcement Learning for Decision-Level Interception Prioritization in Drone Swarm Defense_20250923|Reinforcement Learning for Decision-Level Interception Prioritization in Drone Swarm Defense]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Vehicle Routing Problem|Vehicle Routing Problem]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Hybrid Solver|Hybrid Solver]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18162v1 Announce Type: new 
Abstract: We study last-mile delivery with one truck and one drone under explicit battery management: the drone flies at twice the truck speed; each sortie must satisfy an endurance budget; after every delivery the drone recharges on the truck before the next launch. We introduce a hybrid reinforcement learning (RL) solver that couples an ALNS-based truck tour (with 2/3-opt and Or-opt) with a small pointer/attention policy that schedules drone sorties. The policy decodes launch--serve--rendezvous triplets with hard feasibility masks for endurance and post-delivery recharge; a fast, exact timeline simulator enforces launch/recovery handling and computes the true makespan used by masked greedy/beam decoding. On Euclidean instances with $N{=}50$, $E{=}0.7$, and $R{=}0.1$, the method achieves an average makespan of \textbf{5.203}$\pm$0.093, versus \textbf{5.349}$\pm$0.038 for ALNS and \textbf{5.208}$\pm$0.124 for NN -- i.e., \textbf{2.73\%} better than ALNS on average and within \textbf{0.10\%} of NN. Per-seed, the RL scheduler never underperforms ALNS on the same instance and ties or beats NN on two of three seeds. A decomposition of the makespan shows the expected truck--wait trade-off across heuristics; the learned scheduler balances both to minimize the total completion time. We provide a config-first implementation with plotting and significance-test utilities to support replication.

## 📝 요약

이 논문은 트럭과 드론을 활용한 라스트 마일 배송 문제를 다루며, 드론의 배터리 관리가 명시적으로 고려됩니다. 드론은 트럭 속도의 두 배로 비행하며, 각 출격은 내구성 한도를 만족해야 하고, 배송 후 트럭에서 재충전합니다. 연구에서는 ALNS 기반의 트럭 경로 최적화와 드론 출격을 스케줄링하는 소형 포인터/어텐션 정책을 결합한 하이브리드 강화 학습 솔버를 제안합니다. 이 정책은 내구성과 배송 후 재충전을 위한 엄격한 제약 조건을 적용하여 드론의 출격-서비스-재회 트리플렛을 디코딩합니다. 제안된 방법은 평균 완성 시간을 ALNS보다 2.73% 개선하고, NN과는 0.10% 이내의 차이를 보입니다. 학습된 스케줄러는 트럭 대기 시간과 드론 출격을 균형 있게 조정하여 전체 완료 시간을 최소화합니다. 논문은 재현성을 지원하기 위해 구성 우선 구현과 시각화 및 유의성 테스트 도구를 제공합니다.

## 🎯 주요 포인트

- 1. 트럭과 드론을 활용한 라스트 마일 배송 문제를 연구하며, 드론은 트럭 속도의 두 배로 비행하고 배터리 관리가 필요합니다.
- 2. 하이브리드 강화 학습 솔버를 도입하여 ALNS 기반 트럭 투어와 드론 출격을 스케줄링하는 포인터/어텐션 정책을 결합합니다.
- 3. 드론의 출격, 서비스, 회합을 위한 일정은 내구성과 배터리 재충전 조건을 만족하도록 설계되었습니다.
- 4. 제안된 방법은 특정 조건에서 평균 완성 시간을 ALNS보다 2.73% 개선하였으며, NN과는 0.10% 이내의 성능을 보였습니다.
- 5. 학습된 스케줄러는 트럭 대기 시간을 최소화하면서 전체 완료 시간을 줄이는 균형을 유지합니다.


---

*Generated on 2025-09-24 14:48:07*