<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:24:56.866897",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Distributional Test-time Adaptation",
    "Bayesian Inference",
    "Catastrophic Forgetting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Distributional Test-time Adaptation": 0.9,
    "Bayesian Inference": 0.78,
    "Catastrophic Forgetting": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-language foundation models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs",
          "Vision-language models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's theme and connect well with multimodal and language processing concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Distributional Test-time Adaptation",
        "canonical": "Distributional Test-time Adaptation",
        "aliases": [
          "DOTA"
        ],
        "category": "unique_technical",
        "rationale": "DOTA is a novel method introduced in the paper, crucial for understanding its unique contribution to test-time adaptation.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Bayes' theorem",
        "canonical": "Bayesian Inference",
        "aliases": [
          "Bayes theorem"
        ],
        "category": "broad_technical",
        "rationale": "Bayesian inference is a fundamental concept used in the paper for adapting models, linking to probabilistic methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Catastrophic forgetting",
        "canonical": "Catastrophic Forgetting",
        "aliases": [
          "Forgetting"
        ],
        "category": "specific_connectable",
        "rationale": "Catastrophic forgetting is a key challenge addressed by the proposed method, relevant for continual learning discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
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
      "candidate_surface": "Vision-language foundation models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Distributional Test-time Adaptation",
      "resolved_canonical": "Distributional Test-time Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Bayes' theorem",
      "resolved_canonical": "Bayesian Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Catastrophic forgetting",
      "resolved_canonical": "Catastrophic Forgetting",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# DOTA: Distributional Test-Time Adaptation of Vision-Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.19375.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2409.19375](https://arxiv.org/abs/2409.19375)

## 🔗 유사한 논문
- [[2025-09-22/CLIPTTA_ Robust Contrastive Vision-Language Test-Time Adaptation_20250922|CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation]] (86.7% similar)
- [[2025-09-23/COLA_ Context-aware Language-driven Test-time Adaptation_20250923|COLA: Context-aware Language-driven Test-time Adaptation]] (84.5% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (83.9% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (83.7% similar)
- [[2025-09-23/Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?_20250923|Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Inference|Bayesian Inference]]
**🔗 Specific Connectable**: [[keywords/Catastrophic Forgetting|Catastrophic Forgetting]]
**⚡ Unique Technical**: [[keywords/Distributional Test-time Adaptation|Distributional Test-time Adaptation]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.19375v2 Announce Type: replace-cross 
Abstract: Vision-language foundation models (VLMs), such as CLIP, exhibit remarkable performance across a wide range of tasks. However, deploying these models can be unreliable when significant distribution gaps exist between training and test data, while fine-tuning for diverse scenarios is often costly. Cache-based test-time adapters offer an efficient alternative by storing representative test samples to guide subsequent classifications. Yet, these methods typically employ naive cache management with limited capacity, leading to severe catastrophic forgetting when samples are inevitably dropped during updates. In this paper, we propose DOTA (DistributiOnal Test-time Adaptation), a simple yet effective method addressing this limitation. Crucially, instead of merely memorizing individual test samples, DOTA continuously estimates the underlying distribution of the test data stream. Test-time posterior probabilities are then computed using these dynamically estimated distributions via Bayes' theorem for adaptation. This distribution-centric approach enables the model to continually learn and adapt to the deployment environment. Extensive experiments validate that DOTA significantly mitigates forgetting and achieves state-of-the-art performance compared to existing methods.

## 📝 요약

이 논문은 비전-언어 기반 모델(VLMs)의 배포 시 발생하는 문제를 해결하기 위해 DOTA(DistributiOnal Test-time Adaptation)라는 새로운 방법을 제안합니다. 기존의 캐시 기반 테스트 시간 어댑터는 제한된 용량으로 인해 샘플이 업데이트될 때 심각한 망각 문제가 발생합니다. DOTA는 테스트 데이터 스트림의 분포를 지속적으로 추정하여 이를 바탕으로 베이즈 정리를 통해 테스트 시간의 후행 확률을 계산합니다. 이 방법은 모델이 배포 환경에 지속적으로 적응할 수 있도록 하며, 실험 결과 기존 방법들보다 망각을 크게 줄이고 최첨단 성능을 달성함을 입증했습니다.

## 🎯 주요 포인트

- 1. Vision-language foundation models(VLMs)는 다양한 작업에서 뛰어난 성능을 보이지만, 훈련 데이터와 테스트 데이터 간의 분포 차이가 클 경우 신뢰성이 떨어질 수 있습니다.
- 2. 캐시 기반 테스트 시 어댑터는 대표적인 테스트 샘플을 저장하여 이후 분류를 안내하는 효율적인 대안이지만, 제한된 용량으로 인해 샘플이 업데이트 중 삭제될 때 심각한 망각 문제가 발생합니다.
- 3. DOTA(DistributiOnal Test-time Adaptation)는 테스트 데이터 스트림의 기본 분포를 지속적으로 추정하여 망각 문제를 완화하고, 베이즈 정리를 통해 적응을 위한 테스트 시 후행 확률을 계산합니다.
- 4. DOTA는 배포 환경에 지속적으로 학습하고 적응할 수 있도록 하여 기존 방법들보다 뛰어난 성능을 달성합니다.
- 5. 광범위한 실험을 통해 DOTA가 기존 방법들과 비교하여 망각을 크게 완화하고 최첨단 성능을 달성함을 검증했습니다.


---

*Generated on 2025-09-24 14:24:56*