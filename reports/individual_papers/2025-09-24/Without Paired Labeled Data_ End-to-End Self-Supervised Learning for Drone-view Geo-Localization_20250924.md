<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:27:58.987780",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Drone-view Geo-Localization",
    "Dynamic Memory-driven and Neighborhood Information Learning",
    "Contrastive Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Drone-view Geo-Localization": 0.8,
    "Dynamic Memory-driven and Neighborhood Information Learning": 0.78,
    "Contrastive Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key technique in the paper and connects well with existing literature on unsupervised and semi-supervised learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Drone-view Geo-Localization",
        "canonical": "Drone-view Geo-Localization",
        "aliases": [
          "DVGL"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique application area that is central to the paper's contributions, providing a specific context for self-supervised learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dynamic Memory-driven and Neighborhood Information Learning",
        "canonical": "Dynamic Memory-driven and Neighborhood Information Learning",
        "aliases": [
          "DMNIL"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel method proposed in the paper, highlighting its unique approach to self-supervised learning.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Contrastive Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a widely used technique in self-supervised learning, enhancing the paper's connection to existing frameworks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
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
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Drone-view Geo-Localization",
      "resolved_canonical": "Drone-view Geo-Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dynamic Memory-driven and Neighborhood Information Learning",
      "resolved_canonical": "Dynamic Memory-driven and Neighborhood Information Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Without Paired Labeled Data: End-to-End Self-Supervised Learning for Drone-view Geo-Localization

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.11381.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2502.11381](https://arxiv.org/abs/2502.11381)

## 🔗 유사한 논문
- [[2025-09-23/Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training_20250923|Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training]] (82.2% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (81.9% similar)
- [[2025-09-23/Catching the Details_ Self-Distilled RoI Predictors for Fine-Grained MLLM Perception_20250923|Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception]] (81.6% similar)
- [[2025-09-23/Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification_20250923|Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification]] (81.4% similar)
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Contrastive Learning|Contrastive Learning]]
**⚡ Unique Technical**: [[keywords/Drone-view Geo-Localization|Drone-view Geo-Localization]], [[keywords/Dynamic Memory-driven and Neighborhood Information Learning|Dynamic Memory-driven and Neighborhood Information Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.11381v4 Announce Type: replace-cross 
Abstract: Drone-view Geo-Localization (DVGL) aims to achieve accurate localization of drones by retrieving the most relevant GPS-tagged satellite images. However, most existing methods heavily rely on strictly pre-paired drone-satellite images for supervised learning. When the target region shifts, new paired samples are typically required to adapt to the distribution changes. The high cost of annotation and the limited transferability of these methods significantly hinder the practical deployment of DVGL in open-world scenarios. To address these limitations, we propose a novel end-to-end self-supervised learning method with a shallow backbone network, called the dynamic memory-driven and neighborhood information learning (DMNIL) method. It employs a clustering algorithm to generate pseudo-labels and adopts a dual-path contrastive learning framework to learn discriminative intra-view representations. Furthermore, DMNIL incorporates two core modules, including the dynamic hierarchical memory learning (DHML) module and the information consistency evolution learning (ICEL) module. The DHML module combines short-term and long-term memory to enhance intra-view feature consistency and discriminability. Meanwhile, the ICEL module utilizes a neighborhood-driven dynamic constraint mechanism to systematically capture implicit cross-view semantic correlations, consequently improving cross-view feature alignment. To further stabilize and strengthen the self-supervised training process, a pseudo-label enhancement strategy is introduced to enhance the quality of pseudo supervision. Extensive experiments on three public benchmark datasets demonstrate that the proposed method consistently outperforms existing self-supervised methods and even surpasses several state-of-the-art supervised methods. Our code is available at https://github.com/ISChenawei/DMNIL.

## 📝 요약

드론 뷰 지오로컬라이제이션(DVGL)은 드론의 정확한 위치를 찾기 위해 GPS 태그가 있는 위성 이미지를 활용하는 기술입니다. 기존 방법들은 주로 드론과 위성 이미지의 엄격한 사전 매칭에 의존하여, 새로운 지역에 적응하기 위해서는 추가적인 데이터가 필요했습니다. 이를 해결하기 위해, 본 연구에서는 얕은 백본 네트워크를 사용하는 새로운 자가 지도 학습 방법인 DMNIL을 제안합니다. 이 방법은 클러스터링 알고리즘을 통해 가짜 라벨을 생성하고, 이중 경로 대조 학습을 통해 구별 가능한 특징을 학습합니다. DMNIL은 동적 계층 메모리 학습(DHML) 모듈과 정보 일관성 진화 학습(ICEL) 모듈을 포함하여, 특징의 일관성과 구별성을 향상시키고, 암묵적인 교차 뷰 의미 상관성을 포착합니다. 또한, 가짜 라벨의 품질을 높이기 위한 전략을 도입하여 학습 과정을 안정화합니다. 세 가지 공개 데이터셋을 활용한 실험 결과, 제안된 방법이 기존의 자가 지도 학습 방법을 능가하며, 일부 최신 지도 학습 방법보다도 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 드론 뷰 지리적 위치 확인(DVGL)은 GPS 태그가 있는 위성 이미지를 검색하여 드론의 정확한 위치를 파악하는 것을 목표로 합니다.
- 2. 기존 방법은 엄격하게 사전 짝지어진 드론-위성 이미지에 의존하여 지도 학습을 수행하므로, 새로운 지역에 적응하기 위해서는 새로운 짝지어진 샘플이 필요합니다.
- 3. 제안된 DMNIL 방법은 얕은 백본 네트워크를 사용한 엔드 투 엔드 자가 지도 학습 방법으로, 클러스터링 알고리즘을 통해 의사 라벨을 생성하고 대조 학습 프레임워크를 활용합니다.
- 4. DMNIL은 동적 계층적 메모리 학습(DHML) 모듈과 정보 일관성 진화 학습(ICEL) 모듈을 포함하여, 각각 뷰 내 특징의 일관성과 변별성을 강화하고 뷰 간 특징 정렬을 개선합니다.
- 5. 제안된 방법은 세 가지 공개 벤치마크 데이터셋에서 기존 자가 지도 방법을 지속적으로 능가하며, 몇몇 최첨단 지도 방법보다도 뛰어난 성능을 보입니다.


---

*Generated on 2025-09-24 14:27:58*