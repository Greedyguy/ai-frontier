---
keywords:
  - Vision-Language Model
  - Direct Preference Optimization
  - Cave Automatic Virtual Environment
  - Long-Tail Scenarios
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15968
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:25:56.039086",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Direct Preference Optimization",
    "Cave Automatic Virtual Environment",
    "Long-Tail Scenarios"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.78,
    "Direct Preference Optimization": 0.79,
    "Cave Automatic Virtual Environment": 0.77,
    "Long-Tail Scenarios": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Action",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLA"
        ],
        "category": "evolved_concepts",
        "rationale": "Connects to the growing field of multimodal models that integrate vision and language, which is crucial for understanding complex driving scenarios.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Direct Preference Optimization",
        "canonical": "Direct Preference Optimization",
        "aliases": [
          "DPO"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach to learning from human preferences, enhancing model decision-making in rare scenarios.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Cave Automatic Virtual Environment",
        "canonical": "Cave Automatic Virtual Environment",
        "aliases": [
          "CAVE"
        ],
        "category": "unique_technical",
        "rationale": "A specific simulation platform used for data collection, crucial for replicating and studying long-tail scenarios.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "long-tail scenarios",
        "canonical": "Long-Tail Scenarios",
        "aliases": [
          "rare scenarios"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for understanding the focus on rare, safety-critical situations in autonomous driving.",
        "novelty_score": 0.59,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "autonomous driving",
      "performance",
      "experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Action",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Direct Preference Optimization",
      "resolved_canonical": "Direct Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Cave Automatic Virtual Environment",
      "resolved_canonical": "Cave Automatic Virtual Environment",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "long-tail scenarios",
      "resolved_canonical": "Long-Tail Scenarios",
      "decision": "linked",
      "scores": {
        "novelty": 0.59,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine

**Korean Title:** CoReVLA: 수집 및 정제를 통한 롱테일 시나리오를 위한 이중 단계 종단간 자율 주행 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15968.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15968](https://arxiv.org/abs/2509.15968)

## 🔗 유사한 논문
- [[2025-09-22/Towards Interactive and Learnable Cooperative Driving Automation_ a Large Language Model-Driven Decision-Making Framework_20250922|Towards Interactive and Learnable Cooperative Driving Automation: a Large Language Model-Driven Decision-Making Framework]] (84.0% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (84.0% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (83.8% similar)
- [[2025-09-19/Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning_20250919|Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning]] (82.8% similar)
- [[2025-09-19/CollabVLA_ Self-Reflective Vision-Language-Action Model Dreaming Together with Human_20250919|CollabVLA: Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Long-Tail Scenarios|Long-Tail Scenarios]]
**⚡ Unique Technical**: [[keywords/Direct Preference Optimization|Direct Preference Optimization]], [[keywords/Cave Automatic Virtual Environment|Cave Automatic Virtual Environment]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15968v1 Announce Type: cross 
Abstract: Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All codea and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## 🔍 Abstract (한글 번역)

arXiv:2509.15968v1 발표 유형: 교차  
초록: 자율 주행(AD) 시스템은 상당한 발전을 이루었지만, 긴 꼬리의 안전이 중요한 시나리오에서의 성능은 여전히 제한적입니다. 이러한 드문 경우가 사고의 불균형한 비율을 차지합니다. 비전-언어 행동(VLA) 모델은 강력한 추론 능력을 가지고 있으며 잠재적인 해결책을 제공하지만, 이러한 조건에서 고품질 데이터의 부족과 비효율적인 학습으로 인해 그 효과가 제한됩니다. 이러한 문제를 해결하기 위해, 우리는 데이터 수집과 행동 개선의 이중 단계 과정을 통해 긴 꼬리 시나리오에서 성능을 향상시키는 지속적 학습 종단 간 자율 주행 프레임워크인 CoReVLA를 제안합니다. 먼저, 모델은 오픈 소스 주행 QA 데이터셋의 혼합물에서 공동으로 미세 조정되어 주행 시나리오에 대한 기초적인 이해를 습득합니다. 다음으로, CoReVLA는 Cave Automatic Virtual Environment (CAVE) 시뮬레이션 플랫폼 내에 배치되어 실시간 상호작용에서 운전자 개입 데이터를 수집합니다. 각 개입은 CoReVLA가 신뢰성 있게 처리하지 못하는 긴 꼬리 시나리오를 나타냅니다. 마지막으로, 모델은 직접 선호 최적화(DPO)를 통해 개선되어 인간의 선호로부터 직접 학습하고 수동으로 설계된 보상으로 인한 보상 해킹을 피할 수 있습니다. 광범위한 오픈 루프 및 클로즈드 루프 실험은 제안된 CoReVLA 모델이 주행 시나리오를 정확하게 인식하고 적절한 결정을 내릴 수 있음을 보여줍니다. Bench2Drive 벤치마크에서 CoReVLA는 72.18의 주행 점수(DS)와 50%의 성공률(SR)을 달성하여 긴 꼬리의 안전이 중요한 시나리오에서 최첨단 방법보다 7.96 DS와 15% SR을 초과합니다. 또한, 사례 연구는 모델이 과거의 개입 경험을 활용하여 유사한 실패에 취약한 시나리오에서 성능을 지속적으로 향상시킬 수 있는 능력을 보여줍니다. 모든 코드와 전처리된 데이터셋은 다음에서 이용할 수 있습니다: https://github.com/FanGShiYuu/CoReVLA

## 📝 요약

자율주행 시스템은 드문 안전 중요 시나리오에서의 성능이 제한적입니다. 이를 해결하기 위해 CoReVLA라는 지속 학습 기반 자율주행 프레임워크를 제안합니다. 이 모델은 데이터 수집과 행동 개선의 두 단계로 구성되어 있으며, 오픈소스 운전 QA 데이터셋으로 기초 이해를 얻고, CAVE 시뮬레이션 플랫폼에서 실시간 상호작용을 통해 드라이버 개입 데이터를 수집합니다. 그런 후, Direct Preference Optimization을 통해 인간의 선호도를 학습하여 보상 해킹을 피합니다. 실험 결과, CoReVLA는 Bench2Drive 벤치마크에서 72.18의 운전 점수와 50%의 성공률을 기록하며, 기존 방법보다 우수한 성능을 보였습니다. 이 모델은 유사한 실패 시나리오에서 지속적으로 성능을 개선할 수 있습니다. 모든 코드와 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 자율주행 시스템은 긴꼬리 안전 중요 시나리오에서 성능이 제한적이며, 이러한 드문 경우가 사고의 불균형적인 비율을 차지합니다.
- 2. Vision-Language Action (VLA) 모델은 강력한 추론 능력을 가지고 있지만, 고품질 데이터 부족과 비효율적인 학습으로 인해 효과가 제한됩니다.
- 3. CoReVLA는 데이터 수집과 행동 개선의 이중 단계 과정을 통해 긴꼬리 시나리오에서 성능을 향상시키는 지속 학습 자율주행 프레임워크입니다.
- 4. CoReVLA는 CAVE 시뮬레이션 플랫폼에서 실시간 상호작용을 통해 드라이버 개입 데이터를 수집하고, Direct Preference Optimization (DPO)을 통해 모델을 정제합니다.
- 5. CoReVLA는 Bench2Drive 벤치마크에서 72.18의 주행 점수와 50%의 성공률을 기록하며, 긴꼬리 안전 중요 시나리오에서 최첨단 방법들을 능가합니다.


---

*Generated on 2025-09-23 12:25:56*