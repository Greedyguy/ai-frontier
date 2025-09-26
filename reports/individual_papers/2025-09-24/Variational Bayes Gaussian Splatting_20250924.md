<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:25:10.216973",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Variational Bayes Gaussian Splatting",
    "3D Gaussian Splatting",
    "Variational Inference",
    "Differentiable Rendering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Variational Bayes Gaussian Splatting": 0.85,
    "3D Gaussian Splatting": 0.8,
    "Variational Inference": 0.75,
    "Differentiable Rendering": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Variational Bayes Gaussian Splatting",
        "canonical": "Variational Bayes Gaussian Splatting",
        "aliases": [
          "VBGS"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper, offering a new method for continual learning in 3D scene modeling.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper and represents a specific method for 3D scene modeling.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Variational Inference",
        "canonical": "Variational Inference",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental concept in Bayesian methods, linking to broader topics in machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Differentiable Rendering",
        "canonical": "Differentiable Rendering",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a key component of the optimization method discussed in the paper, relevant to computer graphics and vision.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "catastrophic forgetting",
      "replay buffers"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Variational Bayes Gaussian Splatting",
      "resolved_canonical": "Variational Bayes Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Variational Inference",
      "resolved_canonical": "Variational Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Differentiable Rendering",
      "resolved_canonical": "Differentiable Rendering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Variational Bayes Gaussian Splatting

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.03592.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2410.03592](https://arxiv.org/abs/2410.03592)

## 🔗 유사한 논문
- [[2025-09-23/GeoSplat_ A Deep Dive into Geometry-Constrained Gaussian Splatting_20250923|GeoSplat: A Deep Dive into Geometry-Constrained Gaussian Splatting]] (86.8% similar)
- [[2025-09-23/AD-GS_ Alternating Densification for Sparse-Input 3D Gaussian Splatting_20250923|AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting]] (86.6% similar)
- [[2025-09-23/DriveSplat_ Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians_20250923|DriveSplat: Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians]] (86.3% similar)
- [[2025-09-23/SPFSplatV2_ Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views_20250923|SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views]] (85.4% similar)
- [[2025-09-23/From Restoration to Reconstruction_ Rethinking 3D Gaussian Splatting for Underwater Scenes_20250923|From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for Underwater Scenes]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Variational Inference|Variational Inference]]
**🔗 Specific Connectable**: [[keywords/Differentiable Rendering|Differentiable Rendering]]
**⚡ Unique Technical**: [[keywords/Variational Bayes Gaussian Splatting|Variational Bayes Gaussian Splatting]], [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.03592v2 Announce Type: replace-cross 
Abstract: Recently, 3D Gaussian Splatting has emerged as a promising approach for modeling 3D scenes using mixtures of Gaussians. The predominant optimization method for these models relies on backpropagating gradients through a differentiable rendering pipeline, which struggles with catastrophic forgetting when dealing with continuous streams of data. To address this limitation, we propose Variational Bayes Gaussian Splatting (VBGS), a novel approach that frames training a Gaussian splat as variational inference over model parameters. By leveraging the conjugacy properties of multivariate Gaussians, we derive a closed-form variational update rule, allowing efficient updates from partial, sequential observations without the need for replay buffers. Our experiments show that VBGS not only matches state-of-the-art performance on static datasets, but also enables continual learning from sequentially streamed 2D and 3D data, drastically improving performance in this setting.

## 📝 요약

최근 3D Gaussian Splatting은 Gaussian 혼합을 활용한 3D 장면 모델링의 유망한 접근법으로 주목받고 있습니다. 기존 최적화 방법은 미분 가능한 렌더링 파이프라인을 통해 그래디언트를 역전파하지만, 연속적인 데이터 스트림 처리 시 심각한 망각 문제를 겪습니다. 이를 해결하기 위해, 우리는 Variational Bayes Gaussian Splatting (VBGS)를 제안합니다. 이 방법은 Gaussian splat 훈련을 모델 매개변수에 대한 변분 추론으로 설정합니다. 다변수 Gaussian의 공액성 특성을 활용하여, 재생 버퍼 없이 부분적이고 순차적인 관찰로부터 효율적인 업데이트가 가능한 폐쇄형 변분 업데이트 규칙을 도출했습니다. 실험 결과, VBGS는 정적 데이터셋에서 최첨단 성능을 달성할 뿐만 아니라, 순차적으로 스트리밍되는 2D 및 3D 데이터로부터의 지속적인 학습을 가능하게 하여 이 설정에서 성능을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting은 가우시안 혼합을 사용하여 3D 장면을 모델링하는 유망한 접근법으로 부상하고 있습니다.
- 2. 기존 최적화 방법은 연속적인 데이터 스트림 처리 시 망각 문제를 겪는 차별 가능한 렌더링 파이프라인을 사용합니다.
- 3. Variational Bayes Gaussian Splatting (VBGS)은 모델 매개변수에 대한 변분 추론으로 가우시안 스플랫 훈련을 프레임화하는 새로운 접근법입니다.
- 4. VBGS는 다변량 가우시안의 켤레 속성을 활용하여, 리플레이 버퍼 없이 부분적이고 순차적인 관찰로부터 효율적인 업데이트를 가능하게 합니다.
- 5. 실험 결과, VBGS는 정적 데이터셋에서 최첨단 성능을 달성할 뿐만 아니라, 순차적으로 스트리밍되는 2D 및 3D 데이터로부터의 지속적인 학습을 가능하게 하여 성능을 크게 향상시킵니다.


---

*Generated on 2025-09-24 14:25:10*