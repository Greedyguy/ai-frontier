---
keywords:
  - Self-supervised Learning
  - Attention Mechanism
  - 3D Gaussian Splatting
  - Sparse Views
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17246
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:47:54.158386",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Attention Mechanism",
    "3D Gaussian Splatting",
    "Sparse Views"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Attention Mechanism": 0.82,
    "3D Gaussian Splatting": 0.78,
    "Sparse Views": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervision"
        ],
        "category": "specific_connectable",
        "rationale": "Links to a broader trend in machine learning where models learn from data without explicit labels, relevant to the paper's pose-free approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention"
        ],
        "category": "specific_connectable",
        "rationale": "The use of a masked attention mechanism is a key component of the framework, connecting to existing neural network techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "Gaussian splatting"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique introduced in the paper, central to its contribution and distinct from existing methods.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sparse Views",
        "canonical": "Sparse Views",
        "aliases": [
          "sparse multi-view"
        ],
        "category": "unique_technical",
        "rationale": "Describes the specific input condition addressed by the method, relevant for linking to similar challenges in computer vision.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
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
      "candidate_surface": "Self-supervised",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sparse Views",
      "resolved_canonical": "Sparse Views",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17246.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17246](https://arxiv.org/abs/2509.17246)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.8% similar)
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (83.5% similar)
- [[2025-09-22/Camera Splatting for Continuous View Optimization_20250922|Camera Splatting for Continuous View Optimization]] (83.5% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (83.5% similar)
- [[2025-09-23/SQS_ Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving_20250923|SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Sparse Views|Sparse Views]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17246v1 Announce Type: new 
Abstract: We introduce SPFSplatV2, an efficient feed-forward framework for 3D Gaussian splatting from sparse multi-view images, requiring no ground-truth poses during training and inference. It employs a shared feature extraction backbone, enabling simultaneous prediction of 3D Gaussian primitives and camera poses in a canonical space from unposed inputs. A masked attention mechanism is introduced to efficiently estimate target poses during training, while a reprojection loss enforces pixel-aligned Gaussian primitives, providing stronger geometric constraints. We further demonstrate the compatibility of our training framework with different reconstruction architectures, resulting in two model variants. Remarkably, despite the absence of pose supervision, our method achieves state-of-the-art performance in both in-domain and out-of-domain novel view synthesis, even under extreme viewpoint changes and limited image overlap, and surpasses recent methods that rely on geometric supervision for relative pose estimation. By eliminating dependence on ground-truth poses, our method offers the scalability to leverage larger and more diverse datasets. Code and pretrained models will be available on our project page: https://ranrhuang.github.io/spfsplatv2/.

## 📝 요약

SPFSplatV2는 희소한 다중 뷰 이미지로부터 3D 가우시안 스플래팅을 수행하는 효율적인 피드포워드 프레임워크로, 학습 및 추론 시 실제 포즈 정보가 필요하지 않습니다. 공통 피처 추출 백본을 사용하여 포즈가 없는 입력으로부터 3D 가우시안 프리미티브와 카메라 포즈를 동시에 예측합니다. 학습 시 타겟 포즈를 효율적으로 추정하기 위해 마스크드 어텐션 메커니즘을 도입하고, 리프로젝션 손실을 통해 픽셀 정렬된 가우시안 프리미티브를 강화하여 강력한 기하학적 제약을 제공합니다. 이 프레임워크는 다양한 재구성 아키텍처와 호환되어 두 가지 모델 변형을 제공합니다. 포즈 감독 없이도, 본 방법은 극단적인 시점 변화와 제한된 이미지 중첩 상황에서도 최첨단 성능을 달성하며, 기하학적 감독에 의존하는 최근 방법들을 능가합니다. 이를 통해 더 크고 다양한 데이터셋을 활용할 수 있는 확장성을 제공합니다. 코드와 사전 학습된 모델은 프로젝트 페이지에서 제공될 예정입니다.

## 🎯 주요 포인트

- 1. SPFSplatV2는 희소한 다중 뷰 이미지에서 3D 가우시안 스플래팅을 위한 효율적인 피드포워드 프레임워크로, 학습 및 추론 시에 실제 포즈 데이터가 필요하지 않습니다.
- 2. 공통된 특징 추출 백본을 사용하여 포즈가 없는 입력으로부터 3D 가우시안 프리미티브와 카메라 포즈를 동시에 예측할 수 있습니다.
- 3. 학습 중 타겟 포즈를 효율적으로 추정하기 위해 마스크된 어텐션 메커니즘을 도입하고, 리프로젝션 손실을 통해 픽셀 정렬된 가우시안 프리미티브를 강제하여 강력한 기하학적 제약을 제공합니다.
- 4. 포즈 감독 없이도, SPFSplatV2는 극단적인 시점 변화와 제한된 이미지 중첩에서도 최첨단 성능을 달성하며, 상대 포즈 추정을 위한 기하학적 감독에 의존하는 최근 방법들을 능가합니다.
- 5. 실제 포즈 데이터에 대한 의존성을 제거함으로써, SPFSplatV2는 더 크고 다양한 데이터셋을 활용할 수 있는 확장성을 제공합니다.


---

*Generated on 2025-09-24 04:47:54*