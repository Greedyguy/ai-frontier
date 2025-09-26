---
keywords:
  - Visual Anomaly Detection
  - Vision-Language Model
  - Few-Shot Learning
  - Distribution Shifts
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17615
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:56:28.186831",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Visual Anomaly Detection",
    "Vision-Language Model",
    "Few-Shot Learning",
    "Distribution Shifts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Visual Anomaly Detection": 0.78,
    "Vision-Language Model": 0.82,
    "Few-Shot Learning": 0.8,
    "Distribution Shifts": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Visual Anomaly Detection",
        "canonical": "Visual Anomaly Detection",
        "aliases": [
          "VAD"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper, it connects research with practical applications in anomaly detection.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents an emerging area that bridges vision and language, crucial for the challenge's second track.",
        "novelty_score": 0.58,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Few-Shot Regime",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a key method explored in the challenge, relevant for linking to learning paradigms.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Real-World Distribution Shifts",
        "canonical": "Distribution Shifts",
        "aliases": [
          "Real-World Shifts"
        ],
        "category": "unique_technical",
        "rationale": "Addresses a critical challenge in anomaly detection, linking to robustness in models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "challenge",
      "progress",
      "methods",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Visual Anomaly Detection",
      "resolved_canonical": "Visual Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Few-Shot Regime",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Real-World Distribution Shifts",
      "resolved_canonical": "Distribution Shifts",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# From Benchmarks to Reality: Advancing Visual Anomaly Detection by the VAND 3.0 Challenge

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17615.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17615](https://arxiv.org/abs/2509.17615)

## 🔗 유사한 논문
- [[2025-09-23/Visual Instruction Pretraining for Domain-Specific Foundation Models_20250923|Visual Instruction Pretraining for Domain-Specific Foundation Models]] (81.5% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (81.2% similar)
- [[2025-09-23/Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification_20250923|Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification]] (81.2% similar)
- [[2025-09-18/AD-DINOv3_ Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration_20250918|AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (80.9% similar)
- [[2025-09-23/Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?_20250923|Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Visual Anomaly Detection|Visual Anomaly Detection]], [[keywords/Distribution Shifts|Distribution Shifts]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17615v1 Announce Type: new 
Abstract: Visual anomaly detection is a strongly application-driven field of research. Consequently, the connection between academia and industry is of paramount importance. In this regard, we present the VAND 3.0 Challenge to showcase current progress in anomaly detection across different practical settings whilst addressing critical issues in the field. The challenge hosted two tracks, fostering the development of anomaly detection methods robust against real-world distribution shifts (Category 1) and exploring the capabilities of Vision Language Models within the few-shot regime (Category 2), respectively. The participants' solutions reached significant improvements over previous baselines by combining or adapting existing approaches and fusing them with novel pipelines. While for both tracks the progress in large pre-trained vision (language) backbones played a pivotal role for the performance increase, scaling up anomaly detection methods more efficiently needs to be addressed by future research to meet real-time and computational constraints on-site.

## 📝 요약

이 논문은 시각적 이상 탐지 분야에서의 최신 발전을 보여주는 VAND 3.0 챌린지를 소개합니다. 이 챌린지는 두 가지 트랙으로 구성되어 있으며, 첫 번째는 실제 환경에서의 분포 변화에 강한 이상 탐지 방법을 개발하는 것이고, 두 번째는 소수 샘플 환경에서 비전 언어 모델의 능력을 탐구하는 것입니다. 참가자들은 기존 방법을 조합하거나 새로운 파이프라인과 융합하여 이전 기준을 크게 개선했습니다. 대형 사전 학습된 비전(언어) 백본의 발전이 성능 향상에 중요한 역할을 했지만, 실시간 및 현장 계산 제약을 충족하기 위해 이상 탐지 방법의 효율적인 확장이 필요합니다.

## 🎯 주요 포인트

- 1. VAND 3.0 챌린지는 다양한 실용적 환경에서의 이상 탐지 발전을 보여주고 분야의 중요한 문제를 해결하기 위해 개최되었습니다.
- 2. 챌린지는 현실 세계의 분포 변화에 강한 이상 탐지 방법 개발과 비전 언어 모델의 소수 샷 환경에서의 능력을 탐구하는 두 가지 트랙으로 구성되었습니다.
- 3. 참가자들은 기존 방법을 결합하거나 새로운 파이프라인과 융합하여 이전 기준치를 크게 향상시켰습니다.
- 4. 대규모 사전 학습된 비전(언어) 백본의 발전이 성능 향상에 중요한 역할을 했지만, 실시간 및 현장 계산 제약을 충족하기 위해 이상 탐지 방법의 효율적 확장이 필요합니다.


---

*Generated on 2025-09-24 04:56:28*