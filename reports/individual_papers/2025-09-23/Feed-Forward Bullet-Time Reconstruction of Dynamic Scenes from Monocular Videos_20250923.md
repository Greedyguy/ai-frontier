---
keywords:
  - Bullet-Time Reconstruction
  - Monocular Video Processing
  - 3D Gaussian Splatting
  - Novel View Synthesis
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2412.03526
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:41:44.982540",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bullet-Time Reconstruction",
    "Monocular Video Processing",
    "3D Gaussian Splatting",
    "Novel View Synthesis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Bullet-Time Reconstruction": 0.8,
    "Monocular Video Processing": 0.78,
    "3D Gaussian Splatting": 0.75,
    "Novel View Synthesis": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bullet-Time Reconstruction",
        "canonical": "Bullet-Time Reconstruction",
        "aliases": [
          "BTimer",
          "BulletTimer"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach specific to the paper, focusing on dynamic scene reconstruction, which is central to the study.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Monocular Videos",
        "canonical": "Monocular Video Processing",
        "aliases": [
          "Single-Camera Video"
        ],
        "category": "specific_connectable",
        "rationale": "Monocular video processing is a key aspect of the paper, linking it to broader topics in computer vision.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "Gaussian Splatting"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a specific method used in the paper for scene representation, offering a unique approach to 3D reconstruction.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Novel View Synthesis",
        "canonical": "Novel View Synthesis",
        "aliases": [
          "View Synthesis"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's contribution, connecting it to advancements in rendering and visualization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "scene reconstruction",
      "dynamic content",
      "real-time reconstruction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bullet-Time Reconstruction",
      "resolved_canonical": "Bullet-Time Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Monocular Videos",
      "resolved_canonical": "Monocular Video Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Novel View Synthesis",
      "resolved_canonical": "Novel View Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Feed-Forward Bullet-Time Reconstruction of Dynamic Scenes from Monocular Videos

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2412.03526.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2412.03526](https://arxiv.org/abs/2412.03526)

## 🔗 유사한 논문
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (81.6% similar)
- [[2025-09-22/SAMPO_Scale-wise Autoregression with Motion PrOmpt for generative world models_20250922|SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models]] (80.8% similar)
- [[2025-09-22/ChronoForge-RL_ Chronological Forging through Reinforcement Learning for Enhanced Video Understanding_20250922|ChronoForge-RL: Chronological Forging through Reinforcement Learning for Enhanced Video Understanding]] (80.4% similar)
- [[2025-09-22/MoAngelo_ Motion-Aware Neural Surface Reconstruction for Dynamic Scenes_20250922|MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes]] (80.1% similar)
- [[2025-09-23/AHA -- Predicting What Matters Next_ Online Highlight Detection Without Looking Ahead_20250923|AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Monocular Video Processing|Monocular Video Processing]], [[keywords/Novel View Synthesis|Novel View Synthesis]]
**⚡ Unique Technical**: [[keywords/Bullet-Time Reconstruction|Bullet-Time Reconstruction]], [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.03526v3 Announce Type: replace-cross 
Abstract: Recent advancements in static feed-forward scene reconstruction have demonstrated significant progress in high-quality novel view synthesis. However, these models often struggle with generalizability across diverse environments and fail to effectively handle dynamic content. We present BTimer (short for BulletTimer), the first motion-aware feed-forward model for real-time reconstruction and novel view synthesis of dynamic scenes. Our approach reconstructs the full scene in a 3D Gaussian Splatting representation at a given target ('bullet') timestamp by aggregating information from all the context frames. Such a formulation allows BTimer to gain scalability and generalization by leveraging both static and dynamic scene datasets. Given a casual monocular dynamic video, BTimer reconstructs a bullet-time scene within 150ms while reaching state-of-the-art performance on both static and dynamic scene datasets, even compared with optimization-based approaches.

## 📝 요약

최근 정적 피드포워드 장면 재구성 분야에서는 고품질의 새로운 시점 합성에서 상당한 진전을 이루었으나, 다양한 환경에서의 일반화와 동적 콘텐츠 처리에 어려움을 겪고 있습니다. 본 연구에서는 실시간으로 동적 장면을 재구성하고 새로운 시점을 합성할 수 있는 최초의 모션 인식 피드포워드 모델인 BTimer를 제안합니다. BTimer는 모든 컨텍스트 프레임의 정보를 집계하여 주어진 '총알' 타임스탬프에서 3D 가우시안 스플래팅 표현으로 전체 장면을 재구성합니다. 이를 통해 BTimer는 정적 및 동적 장면 데이터셋을 활용하여 확장성과 일반화를 얻습니다. 일반적인 단안 동영상에서 BTimer는 150ms 이내에 총알 시간 장면을 재구성하며, 정적 및 동적 장면 데이터셋에서 최첨단 성능을 달성합니다.

## 🎯 주요 포인트

- 1. BTimer는 동적 장면의 실시간 재구성과 새로운 뷰 합성을 위한 최초의 모션 인식 피드포워드 모델입니다.
- 2. 이 모델은 모든 컨텍스트 프레임의 정보를 집계하여 주어진 '불릿' 타임스탬프에서 3D 가우시안 스플래팅 표현으로 전체 장면을 재구성합니다.
- 3. BTimer는 정적 및 동적 장면 데이터셋을 활용하여 확장성과 일반화를 달성합니다.
- 4. 일반적인 단안 동적 비디오를 사용하여 BTimer는 150ms 이내에 불릿 타임 장면을 재구성하며, 최적화 기반 접근법과 비교해도 최첨단 성능을 발휘합니다.


---

*Generated on 2025-09-24 00:41:44*