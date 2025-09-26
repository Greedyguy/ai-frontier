<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:57:50.197315",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Autonomous Driving",
    "Crash Data Analysis",
    "Counterfactual Reasoning",
    "Scene-Action Representation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Autonomous Driving": 0.78,
    "Crash Data Analysis": 0.7,
    "Counterfactual Reasoning": 0.79,
    "Scene-Action Representation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "autonomous driving systems",
        "canonical": "Autonomous Driving",
        "aliases": [
          "self-driving cars",
          "driverless vehicles"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to a growing body of work on self-driving technologies, enhancing cross-referencing with related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "crash reports",
        "canonical": "Crash Data Analysis",
        "aliases": [
          "accident reports",
          "collision data"
        ],
        "category": "unique_technical",
        "rationale": "Provides a unique angle on safety data utilization in autonomous systems, facilitating niche research connections.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "counterfactual extension",
        "canonical": "Counterfactual Reasoning",
        "aliases": [
          "what-if analysis",
          "hypothetical scenarios"
        ],
        "category": "specific_connectable",
        "rationale": "Links to methodologies that explore alternative outcomes, relevant in decision-making systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      },
      {
        "surface": "scene-action representation",
        "canonical": "Scene-Action Representation",
        "aliases": [
          "action scene mapping",
          "scene-action model"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specialized method for integrating sensory data with action decisions, useful in robotics and AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "incident-free data",
      "decision time",
      "unified index"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "autonomous driving systems",
      "resolved_canonical": "Autonomous Driving",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "crash reports",
      "resolved_canonical": "Crash Data Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "counterfactual extension",
      "resolved_canonical": "Counterfactual Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "scene-action representation",
      "resolved_canonical": "Scene-Action Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# The Case for Negative Data: From Crash Reports to Counterfactuals for Reasonable Driving

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18626.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18626](https://arxiv.org/abs/2509.18626)

## 🔗 유사한 논문
- [[2025-09-22/CoReVLA_ A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine_20250922|CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine]] (81.8% similar)
- [[2025-09-23/ReasonPlan_ Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving_20250923|ReasonPlan: Unified Scene Prediction and Decision Reasoning for Closed-loop Autonomous Driving]] (81.6% similar)
- [[2025-09-24/Assistive Decision-Making for Right of Way Navigation at Uncontrolled Intersections_20250924|Assistive Decision-Making for Right of Way Navigation at Uncontrolled Intersections]] (81.4% similar)
- [[2025-09-23/Multi-Scenario Highway Lane-Change Intention Prediction_ A Physics-Informed AI Framework for Three-Class Classification_20250923|Multi-Scenario Highway Lane-Change Intention Prediction: A Physics-Informed AI Framework for Three-Class Classification]] (80.7% similar)
- [[2025-09-23/DriveDPO_ Policy Learning via Safety DPO For End-to-End Autonomous Driving_20250923|DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Autonomous Driving|Autonomous Driving]], [[keywords/Counterfactual Reasoning|Counterfactual Reasoning]]
**⚡ Unique Technical**: [[keywords/Crash Data Analysis|Crash Data Analysis]], [[keywords/Scene-Action Representation|Scene-Action Representation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18626v1 Announce Type: cross 
Abstract: Learning-based autonomous driving systems are trained mostly on incident-free data, offering little guidance near safety-performance boundaries. Real crash reports contain precisely the contrastive evidence needed, but they are hard to use: narratives are unstructured, third-person, and poorly grounded to sensor views. We address these challenges by normalizing crash narratives to ego-centric language and converting both logs and crashes into a unified scene-action representation suitable for retrieval. At decision time, our system adjudicates proposed actions by retrieving relevant precedents from this unified index; an agentic counterfactual extension proposes plausible alternatives, retrieves for each, and reasons across outcomes before deciding. On a nuScenes benchmark, precedent retrieval substantially improves calibration, with recall on contextually preferred actions rising from 24% to 53%. The counterfactual variant preserves these gains while sharpening decisions near risk.

## 📝 요약

이 논문은 학습 기반 자율주행 시스템의 안전성과 성능을 개선하기 위해 실제 사고 보고서를 활용하는 방법을 제안합니다. 기존 데이터는 주로 사고가 없는 상황에서 수집되어 안전 경계 근처에서의 지침이 부족합니다. 저자들은 사고 보고서를 자아 중심 언어로 정규화하고, 로그와 사고 데이터를 통합된 장면-행동 표현으로 변환하여 검색에 활용합니다. 의사결정 시, 시스템은 통합된 인덱스에서 관련 전례를 검색하여 제안된 행동을 평가합니다. 또한, 대안적인 시나리오를 제안하고 결과를 비교하여 결정을 내립니다. nuScenes 벤치마크에서 이 방법은 문맥적으로 선호되는 행동에 대한 검색 정확도를 24%에서 53%로 향상시켰으며, 반사실적 변형은 이러한 이점을 유지하면서 위험 근처에서의 의사결정을 개선합니다.

## 🎯 주요 포인트

- 1. 학습 기반 자율 주행 시스템은 주로 사고가 없는 데이터를 기반으로 훈련되어 안전 성능 경계에서의 지침이 부족하다.
- 2. 실제 사고 보고서는 대조적인 증거를 제공하지만, 서술이 비구조적이고 센서 뷰와 연결이 부족하여 사용이 어렵다.
- 3. 연구에서는 사고 서술을 자아 중심 언어로 표준화하고, 로그와 사고를 통합된 장면-행동 표현으로 변환하여 검색에 적합하게 만든다.
- 4. 시스템은 의사 결정 시 통합된 인덱스에서 관련 전례를 검색하여 제안된 행동을 판단한다.
- 5. nuScenes 벤치마크에서 전례 검색은 문맥적으로 선호되는 행동의 재현율을 24%에서 53%로 향상시켰다.


---

*Generated on 2025-09-24 13:57:50*