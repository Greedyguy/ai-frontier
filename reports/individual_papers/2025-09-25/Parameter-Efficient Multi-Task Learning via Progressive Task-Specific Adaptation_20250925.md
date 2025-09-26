---
keywords:
  - Multi-Task Learning
  - Parameter-Efficient Fine-Tuning
  - Task Interference
  - Adapter Modules
  - Transformer
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19602
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:00:34.389842",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Task Learning",
    "Parameter-Efficient Fine-Tuning",
    "Task Interference",
    "Adapter Modules",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Task Learning": 0.78,
    "Parameter-Efficient Fine-Tuning": 0.81,
    "Task Interference": 0.79,
    "Adapter Modules": 0.77,
    "Transformer": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multi-task learning",
        "canonical": "Multi-Task Learning",
        "aliases": [
          "MTL"
        ],
        "category": "broad_technical",
        "rationale": "Multi-task learning is a central theme of the paper, connecting various tasks and methods discussed.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "parameter-efficient fine-tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "efficient fine-tuning"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "task interference",
        "canonical": "Task Interference",
        "aliases": [
          "negative transfer"
        ],
        "category": "specific_connectable",
        "rationale": "Task interference is a key challenge addressed by the paper, linking to broader discussions on task optimization.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "adapter modules",
        "canonical": "Adapter Modules",
        "aliases": [
          "adapters"
        ],
        "category": "unique_technical",
        "rationale": "Adapter modules are a specific innovation in the paper, essential for understanding the proposed adaptation strategy.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Swin Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Swin"
        ],
        "category": "broad_technical",
        "rationale": "The Swin Transformer is a specific model used in the experiments, linking to the broader category of Transformers.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
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
      "candidate_surface": "multi-task learning",
      "resolved_canonical": "Multi-Task Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "parameter-efficient fine-tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "task interference",
      "resolved_canonical": "Task Interference",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "adapter modules",
      "resolved_canonical": "Adapter Modules",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Swin Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Parameter-Efficient Multi-Task Learning via Progressive Task-Specific Adaptation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19602.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19602](https://arxiv.org/abs/2509.19602)

## 🔗 유사한 논문
- [[2025-09-24/HyperAdapt_ Simple High-Rank Adaptation_20250924|HyperAdapt: Simple High-Rank Adaptation]] (85.9% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (85.3% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (84.8% similar)
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (84.7% similar)
- [[2025-09-24/Dynamic Mixture of Progressive Parameter-Efficient Expert Library for Lifelong Robot Learning_20250924|Dynamic Mixture of Progressive Parameter-Efficient Expert Library for Lifelong Robot Learning]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-Task Learning|Multi-Task Learning]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Task Interference|Task Interference]]
**⚡ Unique Technical**: [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]], [[keywords/Adapter Modules|Adapter Modules]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19602v1 Announce Type: new 
Abstract: Parameter-efficient fine-tuning methods have emerged as a promising solution for adapting pre-trained models to various downstream tasks. While these methods perform well in single-task learning, extending them to multi-task learning exacerbates common challenges, such as task interference and negative transfer, due to the limited number of trainable parameters. To address these issues, we introduce progressive task-specific multi-task adaptation, a novel parameter-efficient approach for multi-task learning. This approach introduces adapter modules in a pre-trained model such that these modules are shared across all tasks in the initial layers and become progressively more task-specific in the later layers. The motivation is to reduce the conflicts among tasks by allowing transfer learning across all tasks in the initial layers and enabling task-specific learning toward the prediction heads. Additionally, we propose a gradient-based approach for computing task similarity and use this measure to allocate similar tasks to the shared adapter modules. Our task similarity method introduces minimal overhead in the pipeline. We evaluate our approach by adapting the Swin Transformer for dense prediction tasks. Experiments on the PASCAL and NYUD-v2 datasets demonstrate that our approach outperforms a fully fine-tuned multi-task model while requiring only one-fifth of the trainable parameters. This approach achieves better relative improvement to single-task fine-tuning while reducing the number of trainable parameters and surpasses the current state-of-the-art methods for parameter-efficient multi-task learning.

## 📝 요약

이 논문은 사전 학습된 모델을 다양한 다운스트림 작업에 적응시키기 위한 파라미터 효율적인 방법을 제안합니다. 특히, 멀티태스크 학습에서의 과제 간 간섭과 부정적 전이를 해결하기 위해 점진적 과제 특화 멀티태스크 적응 방식을 도입합니다. 이 방식은 초기 레이어에서는 모든 작업에 공유되는 어댑터 모듈을 사용하고, 후반부 레이어에서는 점차 과제 특화된 모듈을 사용하여 과제 간 충돌을 줄입니다. 또한, 과제 유사성을 계산하는 그래디언트 기반 접근법을 제안하여 유사한 과제를 공유 모듈에 할당합니다. Swin Transformer를 활용한 실험 결과, PASCAL 및 NYUD-v2 데이터셋에서 이 방법이 기존 멀티태스크 모델보다 적은 파라미터로 더 나은 성능을 보였으며, 최신 기법을 능가하는 성과를 달성했습니다.

## 🎯 주요 포인트

- 1. 파라미터 효율적인 미세 조정 방법은 사전 학습된 모델을 다양한 다운스트림 작업에 적응시키는 유망한 솔루션으로 부상하고 있습니다.
- 2. 다중 작업 학습에서의 과제 간 간섭과 부정적 전이를 해결하기 위해, 우리는 점진적 작업 특화 다중 작업 적응이라는 새로운 접근 방식을 제안합니다.
- 3. 이 접근 방식은 초기 레이어에서는 모든 작업에 걸쳐 공유되고, 후반부 레이어에서는 점점 더 작업 특화되는 어댑터 모듈을 도입합니다.
- 4. 제안된 방법은 Swin Transformer를 밀도 예측 작업에 적응시켜 PASCAL 및 NYUD-v2 데이터셋에서 실험한 결과, 전체 미세 조정된 다중 작업 모델보다 우수한 성능을 보였습니다.
- 5. 제안된 방법은 단일 작업 미세 조정에 비해 더 나은 상대적 개선을 달성하며, 훈련 가능한 파라미터 수를 줄이면서도 현재 최첨단 방법을 능가합니다.


---

*Generated on 2025-09-26 09:00:34*