---
keywords:
  - Large Language Model
  - Muon Optimizer
  - Randomized SVD
  - Variance Reduction
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.14562
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:13:09.188741",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Muon Optimizer",
    "Randomized SVD",
    "Variance Reduction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.79,
    "Muon Optimizer": 0.85,
    "Randomized SVD": 0.82,
    "Variance Reduction": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "large-scale models"
        ],
        "category": "broad_technical",
        "rationale": "Large models are a key focus of the paper and are closely related to Large Language Models, facilitating connections in AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.79
      },
      {
        "surface": "Muon Optimizer",
        "canonical": "Muon Optimizer",
        "aliases": [
          "Muon",
          "Muon optimization"
        ],
        "category": "unique_technical",
        "rationale": "The Muon Optimizer is a central concept in the paper, offering a unique approach to optimization in large models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Randomized Singular Value Decomposition",
        "canonical": "Randomized SVD",
        "aliases": [
          "rSVD",
          "randomized SVD"
        ],
        "category": "specific_connectable",
        "rationale": "Randomized SVD is a specific technique used in the paper, linking to broader discussions on matrix decomposition methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Momentum-based Variance Reduction",
        "canonical": "Variance Reduction",
        "aliases": [
          "momentum variance reduction"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for the proposed optimizer, connecting to optimization strategies in machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "efficient training",
      "numerical experimental results",
      "convergence analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Muon Optimizer",
      "resolved_canonical": "Muon Optimizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Randomized Singular Value Decomposition",
      "resolved_canonical": "Randomized SVD",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Momentum-based Variance Reduction",
      "resolved_canonical": "Variance Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# LiMuon: Light and Fast Muon Optimizer for Large Models

**Korean Title:** LiMuon: 대형 모델을 위한 경량 및 고속 뮤온 최적화기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14562.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.14562](https://arxiv.org/abs/2509.14562)

## 🔗 유사한 논문
- [[2025-09-18/LiMuon_ Light and Fast Muon Optimizer for Large Models_20250918|LiMuon: Light and Fast Muon Optimizer for Large Models]] (99.2% similar)
- [[2025-09-22/On the Convergence of Muon and Beyond_20250922|On the Convergence of Muon and Beyond]] (89.8% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (82.2% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.1% similar)
- [[2025-09-22/XAutoLM_ Efficient Fine-Tuning of Language Models via Meta-Learning and AutoML_20250922|XAutoLM: Efficient Fine-Tuning of Language Models via Meta-Learning and AutoML]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Randomized SVD|Randomized SVD]], [[keywords/Variance Reduction|Variance Reduction]]
**⚡ Unique Technical**: [[keywords/Muon Optimizer|Muon Optimizer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14562v2 Announce Type: replace 
Abstract: Large models recently are widely applied in artificial intelligence, so efficient training of large models has received widespread attention. More recently, a useful Muon optimizer is specifically designed for matrix-structured parameters of large models. Although some works have begun to studying Muon optimizer, the existing Muon and its variants still suffer from high sample complexity or high memory for large models. To fill this gap, we propose a light and fast Muon (LiMuon) optimizer for training large models, which builds on the momentum-based variance reduced technique and randomized Singular Value Decomposition (SVD). Our LiMuon optimizer has a lower memory than the current Muon and its variants. Moreover, we prove that our LiMuon has a lower sample complexity of $O(\epsilon^{-3})$ for finding an $\epsilon$-stationary solution of non-convex stochastic optimization under the smooth condition. Recently, the existing convergence analysis of Muon optimizer mainly relies on the strict Lipschitz smooth assumption, while some artificial intelligence tasks such as training large language models (LLMs) do not satisfy this condition. We also proved that our LiMuon optimizer has a sample complexity of $O(\epsilon^{-3})$ under the generalized smooth condition. Numerical experimental results on training DistilGPT2 and ViT models verify efficiency of our LiMuon optimizer.

## 🔍 Abstract (한글 번역)

arXiv:2509.14562v2 발표 유형: 교체  
초록: 최근 대형 모델이 인공지능에 널리 적용되면서 대형 모델의 효율적인 학습이 많은 주목을 받고 있습니다. 최근에는 대형 모델의 행렬 구조화된 매개변수에 특화된 유용한 Muon 최적화기가 설계되었습니다. 일부 연구에서는 Muon 최적화기를 연구하기 시작했지만, 기존의 Muon 및 그 변형들은 여전히 대형 모델에 대해 높은 샘플 복잡성이나 높은 메모리 사용량 문제를 겪고 있습니다. 이러한 격차를 해소하기 위해, 우리는 대형 모델 학습을 위한 가볍고 빠른 Muon (LiMuon) 최적화기를 제안합니다. 이는 모멘텀 기반의 분산 감소 기법과 무작위 특이값 분해(SVD)를 기반으로 합니다. 우리의 LiMuon 최적화기는 현재의 Muon 및 그 변형들보다 더 낮은 메모리 사용량을 가집니다. 또한, 우리는 LiMuon이 매끄러운 조건 하에서 비볼록 확률 최적화의 $\epsilon$-정류 솔루션을 찾기 위한 샘플 복잡성이 $O(\epsilon^{-3})$임을 증명했습니다. 최근 Muon 최적화기의 기존 수렴 분석은 주로 엄격한 Lipschitz 매끄러움 가정에 의존하고 있지만, 대형 언어 모델(LLM) 학습과 같은 일부 인공지능 작업은 이 조건을 만족하지 않습니다. 우리는 또한 LiMuon 최적화기가 일반화된 매끄러운 조건 하에서 $O(\epsilon^{-3})$의 샘플 복잡성을 가짐을 증명했습니다. DistilGPT2와 ViT 모델 학습에 대한 수치 실험 결과는 우리의 LiMuon 최적화기의 효율성을 검증합니다.

## 📝 요약

최근 인공지능 분야에서 대형 모델의 효율적인 학습이 주목받고 있으며, 특히 행렬 구조의 매개변수에 특화된 Muon 옵티마이저가 개발되었습니다. 그러나 기존 Muon과 그 변형들은 높은 샘플 복잡도와 메모리 사용량의 문제를 안고 있습니다. 이를 해결하기 위해, 우리는 모멘텀 기반의 분산 감소 기법과 무작위 특이값 분해(SVD)를 활용한 경량화된 LiMuon 옵티마이저를 제안합니다. LiMuon은 기존 Muon보다 낮은 메모리 사용량을 가지며, 매끄러운 조건 하에서 비볼록 확률 최적화 문제의 $\epsilon$-정류 솔루션을 찾기 위한 샘플 복잡도가 $O(\epsilon^{-3})$임을 증명했습니다. 또한, 일반화된 매끄러운 조건에서도 동일한 샘플 복잡도를 가짐을 입증했습니다. DistilGPT2와 ViT 모델의 학습 실험 결과, LiMuon의 효율성이 확인되었습니다.

## 🎯 주요 포인트

- 1. LiMuon 옵티마이저는 대형 모델의 행렬 구조 매개변수에 특화된 Muon 옵티마이저의 경량화 및 속도 향상 버전입니다.
- 2. LiMuon은 모멘텀 기반 분산 감소 기법과 무작위 SVD를 활용하여 기존 Muon 및 변형보다 낮은 메모리 사용량을 자랑합니다.
- 3. LiMuon은 매끄러운 조건 하에서 비볼록 확률 최적화의 $\epsilon$-정지 솔루션을 찾기 위한 샘플 복잡도가 $O(\epsilon^{-3})$로 낮습니다.
- 4. LiMuon은 일반화된 매끄러운 조건 하에서 샘플 복잡도가 $O(\epsilon^{-3})$임을 증명했습니다.
- 5. DistilGPT2와 ViT 모델의 훈련에서 LiMuon 옵티마이저의 효율성이 수치 실험 결과로 검증되었습니다.


---

*Generated on 2025-09-23 11:13:09*