---
keywords:
  - Transformer
  - Vision Transformers
  - Multilayer Perceptron
  - Weight Pruning
  - Knowledge Distillation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.08591
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:05:00.017932",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Vision Transformers",
    "Multilayer Perceptron",
    "Weight Pruning",
    "Knowledge Distillation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Vision Transformers": 0.88,
    "Multilayer Perceptron": 0.82,
    "Weight Pruning": 0.79,
    "Knowledge Distillation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the paper's focus on model reduction, linking to a broad range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.95,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision Transformers",
        "canonical": "Vision Transformers",
        "aliases": [
          "ViT"
        ],
        "category": "specific_connectable",
        "rationale": "Vision Transformers are a specific application of Transformers, relevant for connecting to computer vision research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Multilayer Perceptron",
        "canonical": "Multilayer Perceptron",
        "aliases": [
          "MLP"
        ],
        "category": "specific_connectable",
        "rationale": "MLPs are a key component in the model architecture discussed, facilitating connections to neural network research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Weight Pruning",
        "canonical": "Weight Pruning",
        "aliases": [
          "Pruning"
        ],
        "category": "unique_technical",
        "rationale": "Weight pruning is a unique technique highlighted in the paper for reducing model parameters.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [
          "Model Distillation"
        ],
        "category": "specific_connectable",
        "rationale": "Knowledge distillation is crucial for model recovery, linking to efficient training methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
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
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.95,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision Transformers",
      "resolved_canonical": "Vision Transformers",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Multilayer Perceptron",
      "resolved_canonical": "Multilayer Perceptron",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Weight Pruning",
      "resolved_canonical": "Weight Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Diversity-Guided MLP Reduction for Efficient Large Vision Transformers

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.08591.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.08591](https://arxiv.org/abs/2506.08591)

## 🔗 유사한 논문
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (86.4% similar)
- [[2025-09-23/On the Simplification of Neural Network Architectures for Predictive Process Monitoring_20250923|On the Simplification of Neural Network Architectures for Predictive Process Monitoring]] (85.3% similar)
- [[2025-09-23/Scaling Efficient LLMs_20250923|Scaling Efficient LLMs]] (85.1% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (84.5% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Vision Transformers|Vision Transformers]], [[keywords/Multilayer Perceptron|Multilayer Perceptron]], [[keywords/Knowledge Distillation|Knowledge Distillation]]
**⚡ Unique Technical**: [[keywords/Weight Pruning|Weight Pruning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.08591v2 Announce Type: replace-cross 
Abstract: Transformer models achieve excellent scaling property, where the performance is improved with the increment of model capacity. However, large-scale model parameters lead to an unaffordable cost of computing and memory. We analyze popular transformer architectures and find that multilayer perceptron (MLP) modules take up the majority of model parameters. To this end, we focus on the recoverability of the compressed models and propose a Diversity-Guided MLP Reduction (DGMR) method to significantly reduce the parameters of large vision transformers with only negligible performance degradation. Specifically, we conduct a Gram-Schmidt weight pruning strategy to eliminate redundant neurons of MLP hidden layer, while preserving weight diversity for better performance recover during distillation. Compared to the model trained from scratch, our pruned model only requires 0.06\% data of LAION-2B (for the training of large vision transformers) without labels (ImageNet-1K) to recover the original performance. Experimental results on several state-of-the-art large vision transformers demonstrate that our method achieves a more than 57.0\% parameter and FLOPs reduction in a near lossless manner. Notably, for EVA-CLIP-E (4.4B), our method accomplishes a 71.5\% parameter and FLOPs reduction without performance degradation. The source code and trained weights are available at https://github.com/visresearch/DGMR.

## 📝 요약

이 논문은 대규모 비전 트랜스포머 모델의 매개변수를 효과적으로 줄이기 위한 Diversity-Guided MLP Reduction (DGMR) 방법을 제안합니다. 주요 기여는 MLP 모듈의 중복 뉴런을 제거하여 모델의 매개변수를 57.0% 이상 줄이면서도 성능 저하를 최소화하는 것입니다. 특히, EVA-CLIP-E 모델에서는 71.5%의 매개변수 감소를 이루었습니다. 이 방법은 소량의 데이터로도 원래 성능을 회복할 수 있으며, 실험 결과는 여러 최신 비전 트랜스포머 모델에서 그 효율성을 입증합니다.

## 🎯 주요 포인트

- 1. 트랜스포머 모델의 성능은 모델 용량 증가와 함께 향상되지만, 대규모 모델 파라미터는 높은 계산 및 메모리 비용을 초래합니다.
- 2. 다층 퍼셉트론(MLP) 모듈이 모델 파라미터의 대부분을 차지함을 발견하고, 이를 압축하여 성능 저하 없이 파라미터를 줄이는 방법을 제안합니다.
- 3. 제안된 Diversity-Guided MLP Reduction (DGMR) 방법은 MLP 숨겨진 층의 중복 뉴런을 제거하면서 가중치 다양성을 유지하여 성능 회복을 돕습니다.
- 4. 실험 결과, DGMR 방법은 여러 최신 대형 비전 트랜스포머에서 57.0% 이상의 파라미터 및 FLOPs 감소를 거의 손실 없이 달성했습니다.
- 5. 특히 EVA-CLIP-E (4.4B) 모델에서 71.5%의 파라미터 및 FLOPs 감소를 성능 저하 없이 이루었습니다.


---

*Generated on 2025-09-24 03:05:00*