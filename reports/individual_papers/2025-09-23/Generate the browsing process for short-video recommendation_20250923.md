---
keywords:
  - Transformer
  - Short Video Recommendation
  - User Interaction Behaviors
  - Watch Time Prediction
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2504.08771
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:53:16.883730",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Short Video Recommendation",
    "User Interaction Behaviors",
    "Watch Time Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Short Video Recommendation": 0.8,
    "User Interaction Behaviors": 0.77,
    "Watch Time Prediction": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-like architecture",
        "canonical": "Transformer",
        "aliases": [
          "Transformer architecture"
        ],
        "category": "broad_technical",
        "rationale": "The use of a Transformer-like architecture is central to capturing sequential dependencies, making it a strong link to existing Transformer-based methods.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "short video recommendation",
        "canonical": "Short Video Recommendation",
        "aliases": [
          "video recommendation",
          "short video rec"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique application area that connects to the broader field of recommendation systems, offering a specific context for linking.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "user interaction behaviors",
        "canonical": "User Interaction Behaviors",
        "aliases": [
          "interaction behaviors",
          "user behaviors"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding user interaction behaviors is crucial for modeling user engagement, linking to user behavior analysis in recommendation systems.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "watch time prediction",
        "canonical": "Watch Time Prediction",
        "aliases": [
          "video watch time prediction"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task within video recommendation systems that can link to predictive modeling techniques.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-like architecture",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "short video recommendation",
      "resolved_canonical": "Short Video Recommendation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "user interaction behaviors",
      "resolved_canonical": "User Interaction Behaviors",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "watch time prediction",
      "resolved_canonical": "Watch Time Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Generate the browsing process for short-video recommendation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2504.08771.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2504.08771](https://arxiv.org/abs/2504.08771)

## 🔗 유사한 논문
- [[2025-09-23/SeqUDA-Rec_ Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation for Personalized Content Marketing_20250923|SeqUDA-Rec: Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation for Personalized Content Marketing]] (82.9% similar)
- [[2025-09-23/AHA -- Predicting What Matters Next_ Online Highlight Detection Without Looking Ahead_20250923|AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead]] (80.4% similar)
- [[2025-09-22/ChronoForge-RL_ Chronological Forging through Reinforcement Learning for Enhanced Video Understanding_20250922|ChronoForge-RL: Chronological Forging through Reinforcement Learning for Enhanced Video Understanding]] (79.6% similar)
- [[2025-09-22/SAMPO_Scale-wise Autoregression with Motion PrOmpt for generative world models_20250922|SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models]] (79.2% similar)
- [[2025-09-23/Prompt-Driven Agentic Video Editing System_ Autonomous Comprehension of Long-Form, Story-Driven Media_20250923|Prompt-Driven Agentic Video Editing System: Autonomous Comprehension of Long-Form, Story-Driven Media]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/User Interaction Behaviors|User Interaction Behaviors]]
**⚡ Unique Technical**: [[keywords/Short Video Recommendation|Short Video Recommendation]], [[keywords/Watch Time Prediction|Watch Time Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.08771v2 Announce Type: replace-cross 
Abstract: This paper proposes a generative method to dynamically simulate users' short video watching journey for watch time prediction in short video recommendation. Unlike existing methods that rely on multimodal features for video content understanding, our method simulates users' sustained interest in watching short videos by learning collaborative information, using interest changes from existing positive and negative feedback videos and user interaction behaviors to implicitly model users' video watching journey. By segmenting videos based on duration and adopting a Transformer-like architecture, our method can capture sequential dependencies between segments while mitigating duration bias. Extensive experiments on industrial-scale and public datasets demonstrate that our method achieves state-of-the-art performance on watch time prediction tasks. The method has been deployed on Kuaishou Lite, achieving a significant improvement of +0.13\% in APP duration, and reaching an XAUC of 83\% for single video watch time prediction on industrial-scale streaming training sets, far exceeding other methods. The proposed method provides a scalable and effective solution for video recommendation through segment-level modeling and user engagement feedback.

## 📝 요약

이 논문은 짧은 비디오 추천에서 시청 시간을 예측하기 위해 사용자의 비디오 시청 여정을 동적으로 시뮬레이션하는 생성 방법을 제안합니다. 기존의 멀티모달 특징에 의존하는 방법과 달리, 이 방법은 사용자의 긍정적 및 부정적 피드백 비디오와 사용자 상호작용 행동을 통해 협업 정보를 학습하여 사용자의 비디오 시청 여정을 암묵적으로 모델링합니다. 비디오를 지속 시간에 따라 분할하고 Transformer 유사 아키텍처를 채택하여 세그먼트 간의 순차적 의존성을 포착하면서 지속 시간 편향을 완화합니다. 산업 규모 및 공공 데이터셋에서의 실험 결과, 이 방법이 시청 시간 예측 작업에서 최첨단 성능을 달성함을 보여줍니다. Kuaishou Lite에 배포되어 앱 지속 시간이 0.13% 개선되었고, 산업 규모 스트리밍 훈련 세트에서 단일 비디오 시청 시간 예측에 대해 83%의 XAUC를 기록하여 다른 방법을 크게 능가했습니다. 이 방법은 세그먼트 수준 모델링과 사용자 참여 피드백을 통해 비디오 추천에 대한 확장 가능하고 효과적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 사용자의 짧은 비디오 시청 여정을 동적으로 시뮬레이션하여 시청 시간을 예측하는 생성 방법을 제안합니다.
- 2. 기존의 멀티모달 기능에 의존하지 않고, 사용자 피드백과 상호작용을 통해 사용자의 지속적인 관심을 모델링합니다.
- 3. 비디오를 지속 시간에 따라 세분화하고 Transformer 유사 아키텍처를 사용하여 세그먼트 간의 순차적 의존성을 포착합니다.
- 4. 산업 규모 및 공개 데이터 세트에서 실험을 통해 최첨단 성능을 달성했으며, Kuaishou Lite에 배포되어 APP 지속 시간이 0.13% 향상되었습니다.
- 5. 제안된 방법은 세그먼트 수준의 모델링과 사용자 참여 피드백을 통해 비디오 추천에 대한 확장 가능하고 효과적인 솔루션을 제공합니다.


---

*Generated on 2025-09-24 00:53:16*