---
keywords:
  - Multimodal Dataset Distillation
  - Generative Models
  - Bi-directional Contrastive Loss
  - Vision-Language Model
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15472
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:57:52.181292",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Dataset Distillation",
    "Generative Models",
    "Bi-directional Contrastive Loss",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Dataset Distillation": 0.78,
    "Generative Models": 0.82,
    "Bi-directional Contrastive Loss": 0.75,
    "Vision-Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Dataset Distillation",
        "canonical": "Multimodal Dataset Distillation",
        "aliases": [
          "Dataset Distillation",
          "Multimodal Distillation"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach to dataset synthesis in multimodal contexts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Generative Models",
        "canonical": "Generative Models",
        "aliases": [
          "Generative Model"
        ],
        "category": "broad_technical",
        "rationale": "Generative models are a key component of the proposed method and are widely applicable across different domains.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bi-directional Contrastive Loss",
        "canonical": "Bi-directional Contrastive Loss",
        "aliases": [
          "Contrastive Loss"
        ],
        "category": "unique_technical",
        "rationale": "This specific loss function is a novel contribution that addresses the challenges of correlation and diversity in dataset distillation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are crucial for understanding and linking multimodal datasets, as highlighted in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Matching Training Trajectories",
      "Caption Synthesis Strategy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Dataset Distillation",
      "resolved_canonical": "Multimodal Dataset Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Generative Models",
      "resolved_canonical": "Generative Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bi-directional Contrastive Loss",
      "resolved_canonical": "Bi-directional Contrastive Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Efficient Multimodal Dataset Distillation via Generative Models

**Korean Title:** 효율적인 다중 모달 데이터셋 증류를 위한 생성 모델 활용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15472.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15472](https://arxiv.org/abs/2509.15472)

## 🔗 유사한 논문
- [[2025-09-22/DistillMatch_ Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching_20250922|DistillMatch: Leveraging Knowledge Distillation from Vision Foundation Model for Multimodal Image Matching]] (83.6% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (83.2% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (82.8% similar)
- [[2025-09-22/PRISM_ Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images_20250922|PRISM: Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images]] (82.2% similar)
- [[2025-09-22/Autoguided Online Data Curation for Diffusion Model Training_20250922|Autoguided Online Data Curation for Diffusion Model Training]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generative Models|Generative Models]]
**⚡ Unique Technical**: [[keywords/Multimodal Dataset Distillation|Multimodal Dataset Distillation]], [[keywords/Bi-directional Contrastive Loss|Bi-directional Contrastive Loss]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15472v1 Announce Type: new 
Abstract: Dataset distillation aims to synthesize a small dataset from a large dataset, enabling the model trained on it to perform well on the original dataset. With the blooming of large language models and multimodal large language models, the importance of multimodal datasets, particularly image-text datasets, has grown significantly. However, existing multimodal dataset distillation methods are constrained by the Matching Training Trajectories algorithm, which significantly increases the computing resource requirement, and takes days to process the distillation. In this work, we introduce EDGE, a generative distillation method for efficient multimodal dataset distillation. Specifically, we identify two key challenges of distilling multimodal datasets with generative models: 1) The lack of correlation between generated images and captions. 2) The lack of diversity among generated samples. To address the aforementioned issues, we propose a novel generative model training workflow with a bi-directional contrastive loss and a diversity loss. Furthermore, we propose a caption synthesis strategy to further improve text-to-image retrieval performance by introducing more text information. Our method is evaluated on Flickr30K, COCO, and CC3M datasets, demonstrating superior performance and efficiency compared to existing approaches. Notably, our method achieves results 18x faster than the state-of-the-art method.

## 🔍 Abstract (한글 번역)

arXiv:2509.15472v1 발표 유형: 신규  
초록: 데이터셋 증류는 대규모 데이터셋에서 소규모 데이터셋을 합성하여, 이를 통해 학습된 모델이 원본 데이터셋에서 우수한 성능을 발휘할 수 있도록 하는 것을 목표로 합니다. 대형 언어 모델과 다중 모달 대형 언어 모델의 급속한 발전과 함께, 특히 이미지-텍스트 데이터셋과 같은 다중 모달 데이터셋의 중요성이 크게 증가했습니다. 그러나 기존의 다중 모달 데이터셋 증류 방법은 매칭 학습 경로 알고리즘에 의해 제약을 받으며, 이는 컴퓨팅 자원 요구를 크게 증가시키고 증류 과정을 며칠에 걸쳐 처리해야 합니다. 본 연구에서는 효율적인 다중 모달 데이터셋 증류를 위한 생성적 증류 방법인 EDGE를 소개합니다. 구체적으로, 우리는 생성 모델을 사용한 다중 모달 데이터셋 증류의 두 가지 주요 과제를 식별했습니다: 1) 생성된 이미지와 캡션 간의 상관관계 부족. 2) 생성된 샘플 간의 다양성 부족. 이러한 문제를 해결하기 위해, 우리는 양방향 대조 손실과 다양성 손실을 포함한 새로운 생성 모델 학습 워크플로우를 제안합니다. 더 나아가, 우리는 더 많은 텍스트 정보를 도입하여 텍스트-이미지 검색 성능을 향상시키기 위한 캡션 합성 전략을 제안합니다. 우리의 방법은 Flickr30K, COCO, CC3M 데이터셋에서 평가되었으며, 기존 접근 방식에 비해 뛰어난 성능과 효율성을 입증했습니다. 특히, 우리의 방법은 최첨단 방법보다 18배 빠른 결과를 달성했습니다.

## 📝 요약

이 논문은 대규모 데이터셋에서 작은 데이터셋을 합성하여 원본 데이터셋에서 우수한 성능을 발휘할 수 있도록 하는 데이터셋 증류를 다룹니다. 특히, 이미지-텍스트와 같은 다중 모달 데이터셋의 중요성이 커짐에 따라, 기존 방법론의 한계를 극복하기 위해 EDGE라는 효율적인 생성적 증류 방법을 제안합니다. EDGE는 생성된 이미지와 캡션 간의 상관성 부족 및 샘플 다양성 부족 문제를 해결하기 위해 양방향 대조 손실과 다양성 손실을 포함한 새로운 생성 모델 훈련 방식을 도입합니다. 또한, 캡션 합성 전략을 통해 텍스트-이미지 검색 성능을 향상시킵니다. Flickr30K, COCO, CC3M 데이터셋에서의 실험 결과, EDGE는 기존 방법보다 18배 빠른 속도로 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 데이터셋 증류는 큰 데이터셋에서 작은 데이터셋을 합성하여 원본 데이터셋에서 잘 작동하는 모델을 훈련시키는 것을 목표로 한다.
- 2. 기존의 멀티모달 데이터셋 증류 방법은 높은 계산 자원을 요구하는 Matching Training Trajectories 알고리즘에 의해 제한된다.
- 3. EDGE는 효율적인 멀티모달 데이터셋 증류를 위한 생성적 증류 방법으로, 생성된 이미지와 캡션 간의 상관관계 부족 및 생성 샘플 간의 다양성 부족 문제를 해결한다.
- 4. 제안된 방법은 양방향 대조 손실과 다양성 손실을 포함한 새로운 생성 모델 훈련 워크플로우를 사용한다.
- 5. Flickr30K, COCO, CC3M 데이터셋에서 평가된 결과, 제안된 방법은 기존 방법보다 18배 빠른 속도로 우수한 성능과 효율성을 보여준다.


---

*Generated on 2025-09-23 11:57:52*