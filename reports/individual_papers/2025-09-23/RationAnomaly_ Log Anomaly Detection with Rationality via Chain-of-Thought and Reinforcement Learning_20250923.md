---
keywords:
  - Chain-of-Thought
  - Reinforcement Learning
  - Log Anomaly Detection
  - Large Language Model
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.14693
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:35:22.175865",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Chain-of-Thought",
    "Reinforcement Learning",
    "Log Anomaly Detection",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Chain-of-Thought": 0.78,
    "Reinforcement Learning": 0.82,
    "Log Anomaly Detection": 0.8,
    "Large Language Model": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Chain-of-Thought",
        "canonical": "Chain-of-Thought",
        "aliases": [
          "CoT"
        ],
        "category": "unique_technical",
        "rationale": "Chain-of-Thought is a novel reasoning approach that enhances interpretability in AI models, making it a unique concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a fundamental AI technique that connects with various machine learning frameworks, enhancing cross-domain linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "Log Anomaly Detection",
        "canonical": "Log Anomaly Detection",
        "aliases": [
          "Log Anomaly"
        ],
        "category": "specific_connectable",
        "rationale": "Log Anomaly Detection is a specific application area that connects with cybersecurity and system reliability topics.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are a central concept in NLP, providing a strong link to modern AI research and applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
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
      "candidate_surface": "Chain-of-Thought",
      "resolved_canonical": "Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Log Anomaly Detection",
      "resolved_canonical": "Log Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# RationAnomaly: Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14693.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.14693](https://arxiv.org/abs/2509.14693)

## 🔗 유사한 논문
- [[2025-09-19/ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT: An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (81.6% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (81.4% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (81.0% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (81.0% similar)
- [[2025-09-19/MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1: Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Log Anomaly Detection|Log Anomaly Detection]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought|Chain-of-Thought]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14693v2 Announce Type: replace 
Abstract: Logs constitute a form of evidence signaling the operational status of software systems. Automated log anomaly detection is crucial for ensuring the reliability of modern software systems. However, existing approaches face significant limitations: traditional deep learning models lack interpretability and generalization, while methods leveraging Large Language Models are often hindered by unreliability and factual inaccuracies. To address these issues, we propose RationAnomaly, a novel framework that enhances log anomaly detection by synergizing Chain-of-Thought (CoT) fine-tuning with reinforcement learning. Our approach first instills expert-like reasoning patterns using CoT-guided supervised fine-tuning, grounded in a high-quality dataset corrected through a rigorous expert-driven process. Subsequently, a reinforcement learning phase with a multi-faceted reward function optimizes for accuracy and logical consistency, effectively mitigating hallucinations. Experimentally, RationAnomaly outperforms state-of-the-art baselines, achieving superior F1-scores on key benchmarks while providing transparent, step-by-step analytical outputs. We have released the corresponding resources, including code and datasets.

## 📝 요약

이 논문은 소프트웨어 시스템의 운영 상태를 나타내는 로그의 이상 탐지를 자동화하는 새로운 프레임워크인 RationAnomaly를 제안합니다. 기존 방법론의 해석력 부족과 신뢰성 문제를 해결하기 위해, 이 연구는 Chain-of-Thought(CoT) 미세 조정과 강화 학습을 결합합니다. CoT 기반의 지도 학습을 통해 전문가 수준의 추론 패턴을 학습하고, 강화 학습 단계에서는 다면적 보상 함수를 통해 정확성과 논리적 일관성을 최적화하여 오류를 줄입니다. 실험 결과, RationAnomaly는 최신 기준을 초과하는 F1 점수를 기록하며, 투명하고 단계적인 분석 결과를 제공합니다. 관련 코드와 데이터셋도 공개되었습니다.

## 🎯 주요 포인트

- 1. RationAnomaly는 Chain-of-Thought (CoT) 미세 조정과 강화 학습을 결합하여 로그 이상 탐지를 향상시키는 새로운 프레임워크입니다.
- 2. CoT 기반의 지도 학습을 통해 전문가 수준의 추론 패턴을 주입하고, 강화 학습 단계에서 다면적 보상 함수를 사용하여 정확성과 논리적 일관성을 최적화합니다.
- 3. RationAnomaly는 최신 기준을 능가하는 F1 점수를 달성하며, 투명하고 단계별 분석 출력을 제공합니다.
- 4. 기존의 대형 언어 모델 기반 방법들이 신뢰성과 사실적 정확성에서 한계를 보이는 문제를 해결합니다.
- 5. 관련 리소스, 코드 및 데이터셋이 공개되었습니다.


---

*Generated on 2025-09-24 00:35:22*