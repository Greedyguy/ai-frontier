<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:13:55.049308",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DexSkin",
    "Tactile Sensing",
    "Learning from Demonstration",
    "Robotic Manipulation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DexSkin": 0.78,
    "Tactile Sensing": 0.82,
    "Learning from Demonstration": 0.79,
    "Robotic Manipulation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DexSkin",
        "canonical": "DexSkin",
        "aliases": [
          "Conformable Robotic Skin"
        ],
        "category": "unique_technical",
        "rationale": "DexSkin is a novel technology specific to this paper, offering unique tactile sensing capabilities for robotic manipulation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "tactile sensing",
        "canonical": "Tactile Sensing",
        "aliases": [
          "Touch Sensing"
        ],
        "category": "broad_technical",
        "rationale": "Tactile sensing is a fundamental concept in robotics, linking to various sensor technologies and applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "learning-from-demonstration",
        "canonical": "Learning from Demonstration",
        "aliases": [
          "LfD"
        ],
        "category": "specific_connectable",
        "rationale": "Learning from Demonstration is a key method in robotics for transferring human skills to robots, facilitating connections to machine learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "robotic manipulation",
        "canonical": "Robotic Manipulation",
        "aliases": [
          "Robot Handling"
        ],
        "category": "specific_connectable",
        "rationale": "Robotic manipulation is central to the paper's focus, connecting to broader robotics and AI research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
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
      "candidate_surface": "DexSkin",
      "resolved_canonical": "DexSkin",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "tactile sensing",
      "resolved_canonical": "Tactile Sensing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "learning-from-demonstration",
      "resolved_canonical": "Learning from Demonstration",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "robotic manipulation",
      "resolved_canonical": "Robotic Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DexSkin: High-Coverage Conformable Robotic Skin for Learning Contact-Rich Manipulation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18830.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18830](https://arxiv.org/abs/2509.18830)

## 🔗 유사한 논문
- [[2025-09-18/The Role of Touch_ Towards Optimal Tactile Sensing Distribution in Anthropomorphic Hands for Dexterous In-Hand Manipulation_20250918|The Role of Touch: Towards Optimal Tactile Sensing Distribution in Anthropomorphic Hands for Dexterous In-Hand Manipulation]] (86.0% similar)
- [[2025-09-18/Efficient Tactile Perception with Soft Electrical Impedance Tomography and Pre-trained Transformer_20250918|Efficient Tactile Perception with Soft Electrical Impedance Tomography and Pre-trained Transformer]] (83.8% similar)
- [[2025-09-19/Object Recognition and Force Estimation with the GelSight Baby Fin Ray_20250919|Object Recognition and Force Estimation with the GelSight Baby Fin Ray]] (83.7% similar)
- [[2025-09-23/TranTac_ Leveraging Transient Tactile Signals for Contact-Rich Robotic Manipulation_20250923|TranTac: Leveraging Transient Tactile Signals for Contact-Rich Robotic Manipulation]] (82.4% similar)
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Tactile Sensing|Tactile Sensing]]
**🔗 Specific Connectable**: [[keywords/Learning from Demonstration|Learning from Demonstration]], [[keywords/Robotic Manipulation|Robotic Manipulation]]
**⚡ Unique Technical**: [[keywords/DexSkin|DexSkin]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18830v1 Announce Type: cross 
Abstract: Human skin provides a rich tactile sensing stream, localizing intentional and unintentional contact events over a large and contoured region. Replicating these tactile sensing capabilities for dexterous robotic manipulation systems remains a longstanding challenge. In this work, we take a step towards this goal by introducing DexSkin. DexSkin is a soft, conformable capacitive electronic skin that enables sensitive, localized, and calibratable tactile sensing, and can be tailored to varying geometries. We demonstrate its efficacy for learning downstream robotic manipulation by sensorizing a pair of parallel jaw gripper fingers, providing tactile coverage across almost the entire finger surfaces. We empirically evaluate DexSkin's capabilities in learning challenging manipulation tasks that require sensing coverage across the entire surface of the fingers, such as reorienting objects in hand and wrapping elastic bands around boxes, in a learning-from-demonstration framework. We then show that, critically for data-driven approaches, DexSkin can be calibrated to enable model transfer across sensor instances, and demonstrate its applicability to online reinforcement learning on real robots. Our results highlight DexSkin's suitability and practicality for learning real-world, contact-rich manipulation. Please see our project webpage for videos and visualizations: https://dex-skin.github.io/.

## 📝 요약

이 논문에서는 인간의 피부와 유사한 촉각 감지 능력을 로봇 조작 시스템에 구현하기 위한 DexSkin을 소개합니다. DexSkin은 부드럽고 유연한 정전용량 전자 피부로, 민감하고 국소적인 촉각 감지를 가능하게 하며 다양한 기하학적 형태에 맞출 수 있습니다. 연구진은 이를 사용하여 로봇의 평행 집게 손가락에 촉각 센서를 장착하고, 물체 재배치 및 탄성 밴드 감기와 같은 복잡한 조작 작업을 학습하는 데 DexSkin의 효과를 입증했습니다. 또한, DexSkin은 센서 인스턴스 간 모델 전이를 가능하게 하여 데이터 기반 접근 방식에 적합하며, 실제 로봇의 온라인 강화 학습에도 적용 가능함을 보여줍니다. 이 연구는 DexSkin이 실제 접촉이 많은 조작 작업에 적합하고 실용적임을 강조합니다.

## 🎯 주요 포인트

- 1. DexSkin은 민감하고 국부적인 촉각 센싱을 가능하게 하는 유연한 전자 피부로, 다양한 기하학적 형태에 맞게 조정될 수 있습니다.
- 2. DexSkin을 사용하여 병렬 턱 그리퍼 손가락에 센서를 부착하여 거의 전체 손가락 표면에 걸쳐 촉각 커버리지를 제공합니다.
- 3. DexSkin은 손 안의 물체 재배치 및 상자에 탄성 밴드 감기와 같은 복잡한 조작 작업을 학습하는 데 효과적입니다.
- 4. DexSkin은 센서 인스턴스 간 모델 전이를 가능하게 하는 보정이 가능하며, 실제 로봇에서의 온라인 강화 학습에 적용할 수 있습니다.
- 5. DexSkin은 실제 접촉이 많은 조작 작업을 학습하는 데 적합하고 실용적임을 강조합니다.


---

*Generated on 2025-09-24 15:13:55*