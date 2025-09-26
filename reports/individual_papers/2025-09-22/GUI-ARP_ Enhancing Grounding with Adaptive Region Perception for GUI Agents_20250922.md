---
keywords:
  - Adaptive Region Perception
  - Adaptive Stage Controlling
  - Group Relative Policy Optimization
  - Attention Mechanism
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15532
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:02:43.004899",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Adaptive Region Perception",
    "Adaptive Stage Controlling",
    "Group Relative Policy Optimization",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Adaptive Region Perception": 0.78,
    "Adaptive Stage Controlling": 0.77,
    "Group Relative Policy Optimization": 0.75,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Adaptive Region Perception",
        "canonical": "Adaptive Region Perception",
        "aliases": [
          "ARP"
        ],
        "category": "unique_technical",
        "rationale": "ARP is a novel approach for GUI agents, enhancing the specificity of GUI grounding tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adaptive Stage Controlling",
        "canonical": "Adaptive Stage Controlling",
        "aliases": [
          "ASC"
        ],
        "category": "unique_technical",
        "rationale": "ASC is crucial for dynamically adjusting inference strategies in GUI-ARP.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Group Relative Policy Optimization",
        "aliases": [
          "GRPO"
        ],
        "category": "unique_technical",
        "rationale": "GRPO is a key component in the training pipeline, offering a unique approach to reinforcement fine-tuning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Visual Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Visual Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Visual Attention is a form of Attention Mechanism, crucial for focusing on task-relevant regions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "GUI grounding",
      "high-resolution screenshots",
      "state-of-the-art performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Adaptive Region Perception",
      "resolved_canonical": "Adaptive Region Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adaptive Stage Controlling",
      "resolved_canonical": "Adaptive Stage Controlling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Visual Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# GUI-ARP: Enhancing Grounding with Adaptive Region Perception for GUI Agents

**Korean Title:** GUI-ARP: GUI 에이전트를 위한 적응형 영역 인식을 통한 그라운딩 향상

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15532.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15532](https://arxiv.org/abs/2509.15532)

## 🔗 유사한 논문
- [[2025-09-22/GUI-ReWalk_ Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning_20250922|GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning]] (85.3% similar)
- [[2025-09-22/BTL-UI_ Blink-Think-Link Reasoning Model for GUI Agent_20250922|BTL-UI: Blink-Think-Link Reasoning Model for GUI Agent]] (82.6% similar)
- [[2025-09-18/InfraMind_ A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management_20250918|InfraMind: A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management]] (81.4% similar)
- [[2025-09-19/GAF_ Gaussian Action Field as a Dynamic World Model for Robotic Manipulation_20250919|GAF: Gaussian Action Field as a Dynamic World Model for Robotic Manipulation]] (81.1% similar)
- [[2025-09-19/ScaleCUA_ Scaling Open-Source Computer Use Agents with Cross-Platform Data_20250919|ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Adaptive Region Perception|Adaptive Region Perception]], [[keywords/Adaptive Stage Controlling|Adaptive Stage Controlling]], [[keywords/Group Relative Policy Optimization|Group Relative Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15532v1 Announce Type: cross 
Abstract: Existing GUI grounding methods often struggle with fine-grained localization in high-resolution screenshots. To address this, we propose GUI-ARP, a novel framework that enables adaptive multi-stage inference. Equipped with the proposed Adaptive Region Perception (ARP) and Adaptive Stage Controlling (ASC), GUI-ARP dynamically exploits visual attention for cropping task-relevant regions and adapts its inference strategy, performing a single-stage inference for simple cases and a multi-stage analysis for more complex scenarios. This is achieved through a two-phase training pipeline that integrates supervised fine-tuning with reinforcement fine-tuning based on Group Relative Policy Optimization (GRPO). Extensive experiments demonstrate that the proposed GUI-ARP achieves state-of-the-art performance on challenging GUI grounding benchmarks, with a 7B model reaching 60.8% accuracy on ScreenSpot-Pro and 30.9% on UI-Vision benchmark. Notably, GUI-ARP-7B demonstrates strong competitiveness against open-source 72B models (UI-TARS-72B at 38.1%) and proprietary models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15532v1 발표 유형: 교차  
초록: 기존의 GUI 그라운딩 방법은 고해상도 스크린샷에서 세밀한 위치 지정에 어려움을 겪는 경우가 많습니다. 이를 해결하기 위해, 우리는 적응형 다단계 추론을 가능하게 하는 새로운 프레임워크인 GUI-ARP를 제안합니다. 제안된 적응형 영역 인식(ARP)과 적응형 단계 제어(ASC)를 갖춘 GUI-ARP는 시각적 주의를 동적으로 활용하여 작업 관련 영역을 크롭하고, 간단한 경우에는 단일 단계 추론을 수행하고, 복잡한 시나리오에서는 다단계 분석을 수행하는 추론 전략을 적응시킵니다. 이는 그룹 상대 정책 최적화(GRPO)를 기반으로 한 강화 미세 조정과 감독된 미세 조정을 통합하는 두 단계의 훈련 파이프라인을 통해 달성됩니다. 광범위한 실험을 통해 제안된 GUI-ARP가 도전적인 GUI 그라운딩 벤치마크에서 최첨단 성능을 달성했음을 보여주며, 7B 모델은 ScreenSpot-Pro에서 60.8%의 정확도와 UI-Vision 벤치마크에서 30.9%를 기록했습니다. 특히, GUI-ARP-7B는 오픈 소스 72B 모델(UI-TARS-72B에서 38.1%) 및 독점 모델에 대해 강력한 경쟁력을 보여줍니다.

## 📝 요약

기존의 GUI 그라운딩 방법은 고해상도 스크린샷에서 세밀한 위치 파악에 어려움을 겪습니다. 이를 해결하기 위해, 우리는 GUI-ARP라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 적응형 다단계 추론을 가능하게 하며, Adaptive Region Perception (ARP)과 Adaptive Stage Controlling (ASC)을 통해 시각적 주의를 활용하여 관련 영역을 자르고, 간단한 경우에는 단일 단계 추론을, 복잡한 경우에는 다단계 분석을 수행합니다. 이는 그룹 상대 정책 최적화(GRPO)를 기반으로 한 강화 미세 조정과 지도 학습 미세 조정을 통합한 두 단계의 훈련 파이프라인을 통해 이루어집니다. 실험 결과, GUI-ARP는 까다로운 GUI 그라운딩 벤치마크에서 최첨단 성능을 보였으며, 7B 모델은 ScreenSpot-Pro에서 60.8%, UI-Vision 벤치마크에서 30.9%의 정확도를 기록했습니다. 특히, GUI-ARP-7B는 오픈 소스 72B 모델(UI-TARS-72B의 38.1%) 및 상용 모델과 비교해 강력한 경쟁력을 보였습니다.

## 🎯 주요 포인트

- 1. GUI-ARP는 고해상도 스크린샷에서 세밀한 위치 추적을 개선하기 위해 설계된 적응형 다단계 추론 프레임워크입니다.
- 2. Adaptive Region Perception (ARP)와 Adaptive Stage Controlling (ASC)을 통해 시각적 주의를 활용하여 관련 영역을 자르고, 간단한 경우에는 단일 단계 추론, 복잡한 경우에는 다단계 분석을 수행합니다.
- 3. GUI-ARP는 감독 학습과 강화 학습을 통합한 두 단계의 훈련 파이프라인을 통해 구현됩니다.
- 4. 실험 결과, GUI-ARP는 ScreenSpot-Pro에서 60.8%, UI-Vision 벤치마크에서 30.9%의 정확도로 최첨단 성능을 달성했습니다.
- 5. GUI-ARP-7B는 오픈 소스 72B 모델 및 독점 모델과 비교하여 강력한 경쟁력을 보입니다.


---

*Generated on 2025-09-23 09:02:43*