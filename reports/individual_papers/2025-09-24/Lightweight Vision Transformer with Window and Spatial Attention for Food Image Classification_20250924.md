<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:05:26.785533",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Attention Mechanism",
    "Attention Mechanism",
    "Food Image Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.78,
    "Attention Mechanism": 0.77,
    "Food Image Classification": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Vision Transformers are a specific application of Transformers in computer vision, linking to broader Transformer research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Window Multi-Head Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "WMHAM"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specialized form of attention mechanism, crucial for linking to research on efficient attention models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Spatial Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "SAM"
        ],
        "category": "specific_connectable",
        "rationale": "Spatial attention is a key concept in enhancing feature representation, relevant to attention mechanism studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Food Image Classification",
        "canonical": "Food Image Classification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specialized application area in computer vision, linking to domain-specific research.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "food industry",
      "production quality",
      "automated quality control"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Window Multi-Head Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Spatial Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Food Image Classification",
      "resolved_canonical": "Food Image Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Lightweight Vision Transformer with Window and Spatial Attention for Food Image Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18692.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18692](https://arxiv.org/abs/2509.18692)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (82.7% similar)
- [[2025-09-24/No Labels Needed_ Zero-Shot Image Classification with Collaborative Self-Learning_20250924|No Labels Needed: Zero-Shot Image Classification with Collaborative Self-Learning]] (82.4% similar)
- [[2025-09-24/Efficient Breast and Ovarian Cancer Classification via ViT-Based Preprocessing and Transfer Learning_20250924|Efficient Breast and Ovarian Cancer Classification via ViT-Based Preprocessing and Transfer Learning]] (82.0% similar)
- [[2025-09-18/RoboEye_ Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching_20250918|RoboEye: Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching]] (81.8% similar)
- [[2025-09-22/Saccadic Vision for Fine-Grained Visual Classification_20250922|Saccadic Vision for Fine-Grained Visual Classification]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Food Image Classification|Food Image Classification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18692v1 Announce Type: new 
Abstract: With the rapid development of society and continuous advances in science and technology, the food industry increasingly demands higher production quality and efficiency. Food image classification plays a vital role in enabling automated quality control on production lines, supporting food safety supervision, and promoting intelligent agricultural production. However, this task faces challenges due to the large number of parameters and high computational complexity of Vision Transformer models. To address these issues, we propose a lightweight food image classification algorithm that integrates a Window Multi-Head Attention Mechanism (WMHAM) and a Spatial Attention Mechanism (SAM). The WMHAM reduces computational cost by capturing local and global contextual features through efficient window partitioning, while the SAM adaptively emphasizes key spatial regions to improve discriminative feature representation. Experiments conducted on the Food-101 and Vireo Food-172 datasets demonstrate that our model achieves accuracies of 95.24% and 94.33%, respectively, while significantly reducing parameters and FLOPs compared with baseline methods. These results confirm that the proposed approach achieves an effective balance between computational efficiency and classification performance, making it well-suited for deployment in resource-constrained environments.

## 📝 요약

이 논문은 식품 이미지 분류를 위한 경량 알고리즘을 제안합니다. Vision Transformer 모델의 높은 계산 복잡성을 해결하기 위해, 윈도우 멀티-헤드 어텐션 메커니즘(WMHAM)과 공간 어텐션 메커니즘(SAM)을 통합했습니다. WMHAM은 효율적인 윈도우 분할을 통해 지역 및 전역 문맥적 특징을 포착하여 계산 비용을 줄이고, SAM은 주요 공간 영역을 강조하여 특징 표현을 개선합니다. Food-101과 Vireo Food-172 데이터셋 실험 결과, 제안된 모델은 각각 95.24%와 94.33%의 정확도를 달성하며, 기존 방법들에 비해 파라미터와 FLOPs를 크게 줄였습니다. 이는 제안된 접근법이 계산 효율성과 분류 성능 사이에서 효과적인 균형을 이루어, 자원이 제한된 환경에서의 적용에 적합함을 입증합니다.

## 🎯 주요 포인트

- 1. 식품 이미지 분류는 자동 품질 관리, 식품 안전 감독, 지능형 농업 생산에 중요한 역할을 한다.
- 2. Vision Transformer 모델의 높은 계산 복잡성과 많은 파라미터가 식품 이미지 분류의 과제로 작용한다.
- 3. 제안된 경량화 알고리즘은 WMHAM과 SAM을 통합하여 계산 비용을 줄이고, 주요 공간 영역을 강조하여 특징 표현을 개선한다.
- 4. Food-101과 Vireo Food-172 데이터셋에서 각각 95.24%와 94.33%의 정확도를 달성하며, 기존 방법에 비해 파라미터와 FLOPs를 크게 줄였다.
- 5. 제안된 접근 방식은 계산 효율성과 분류 성능 간의 균형을 효과적으로 이루어, 자원이 제한된 환경에 적합하다.


---

*Generated on 2025-09-24 16:05:26*