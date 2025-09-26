---
keywords:
  - LiMuon Optimizer
  - DistilGPT2
  - Vision Transformers
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:21:54.317306",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LiMuon Optimizer",
    "DistilGPT2",
    "Vision Transformers"
  ],
  "rejected_keywords": [
    "Large Models",
    "Randomized SVD",
    "Variance Reduction Techniques"
  ],
  "similarity_scores": {
    "LiMuon Optimizer": 0.8,
    "DistilGPT2": 0.78,
    "Vision Transformers": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# LiMuon: Light and Fast Muon Optimizer for Large Models

**Korean Title:** LiMuon: 대형 모델을 위한 경량 및 고속 뮤온 최적화기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/DistilGPT2|DistilGPT2]], [[keywords/Vision Transformers|Vision Transformers]]
**⚡ Unique Technical**: [[keywords/LiMuon Optimizer|LiMuon optimizer]]

## 🔗 유사한 논문
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (80.7% similar)
- [[Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (79.6% similar)
- [[{lambda}Scale_ Enabling Fast Scaling for Serverless Large Language Model Inference_20250919|{lambda}Scale Enabling Fast Scaling for Serverless Large Language Model Inference]] (79.5% similar)
- [[MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (79.5% similar)
- [[PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (79.5% similar)

## 📋 저자 정보

**Authors:** Feihu Huang, Yuning Luo, Songcan Chen

## 📄 Abstract (원문)

Large models recently are widely applied in artificial intelligence, so
efficient training of large models has received widespread attention. More
recently, a useful Muon optimizer is specifically designed for
matrix-structured parameters of large models. Although some works have begun to
studying Muon optimizer, the existing Muon and its variants still suffer from
high sample complexity or high memory for large models. To fill this gap, we
propose a light and fast Muon (LiMuon) optimizer for training large models,
which builds on the momentum-based variance reduced technique and randomized
Singular Value Decomposition (SVD). Our LiMuon optimizer has a lower memory
than the current Muon and its variants. Moreover, we prove that our LiMuon has
a lower sample complexity of $O(\epsilon^{-3})$ for finding an
$\epsilon$-stationary solution of non-convex stochastic optimization under the
smooth condition. Recently, the existing convergence analysis of Muon optimizer
mainly relies on the strict Lipschitz smooth assumption, while some artificial
intelligence tasks such as training large language models (LLMs) do not satisfy
this condition. We also proved that our LiMuon optimizer has a sample
complexity of $O(\epsilon^{-3})$ under the generalized smooth condition.
Numerical experimental results on training DistilGPT2 and ViT models verify
efficiency of our LiMuon optimizer.

## 🔍 Abstract (한글 번역)

최근 대형 모델들이 인공지능 분야에서 널리 적용되고 있으며, 따라서 대형 모델의 효율적인 학습이 많은 주목을 받고 있습니다. 최근에는 대형 모델의 행렬 구조 매개변수에 특화된 유용한 Muon 옵티마이저가 설계되었습니다. 일부 연구에서는 Muon 옵티마이저를 연구하기 시작했지만, 기존의 Muon 및 그 변형들은 여전히 대형 모델에 대해 높은 샘플 복잡도나 높은 메모리 요구 사항을 겪고 있습니다. 이러한 격차를 해소하기 위해, 우리는 대형 모델 학습을 위한 경량화되고 빠른 Muon (LiMuon) 옵티마이저를 제안합니다. 이는 모멘텀 기반의 분산 감소 기법과 무작위 특이값 분해(SVD)를 기반으로 구축되었습니다. 우리의 LiMuon 옵티마이저는 현재의 Muon 및 그 변형들보다 더 낮은 메모리를 요구합니다. 또한, 우리는 LiMuon이 매끄러운 조건 하에서 비볼록 확률 최적화의 $\epsilon$-정류 솔루션을 찾기 위해 $O(\epsilon^{-3})$의 낮은 샘플 복잡도를 가진다는 것을 증명했습니다. 최근 Muon 옵티마이저의 기존 수렴 분석은 주로 엄격한 리프시츠 매끄러움 가정에 의존하고 있지만, 대형 언어 모델(LLM) 학습과 같은 일부 인공지능 작업은 이 조건을 만족하지 않습니다. 우리는 또한 LiMuon 옵티마이저가 일반화된 매끄러운 조건 하에서 $O(\epsilon^{-3})$의 샘플 복잡도를 가진다는 것을 증명했습니다. DistilGPT2와 ViT 모델 학습에 대한 수치 실험 결과는 LiMuon 옵티마이저의 효율성을 검증합니다.

## 📝 요약

최근 인공지능 분야에서 대형 모델의 효율적인 학습이 주목받고 있으며, 특히 행렬 구조의 매개변수에 특화된 Muon 옵티마이저가 사용되고 있습니다. 그러나 기존 Muon 및 변형들은 높은 샘플 복잡도와 메모리 사용량 문제를 겪고 있습니다. 이를 해결하기 위해, 우리는 모멘텀 기반 분산 감소 기법과 무작위 특이값 분해(SVD)를 활용한 경량화되고 빠른 LiMuon 옵티마이저를 제안합니다. LiMuon은 기존 Muon보다 메모리 사용량이 적으며, 비볼록 확률 최적화 문제에서 $\epsilon$-정류 솔루션을 찾기 위한 샘플 복잡도가 $O(\epsilon^{-3})$임을 증명했습니다. 또한, 일반화된 매끄러움 조건 하에서도 동일한 샘플 복잡도를 보임을 입증했습니다. DistilGPT2와 ViT 모델 학습 실험 결과, LiMuon의 효율성이 확인되었습니다.

## 🎯 주요 포인트

- 1. LiMuon 옵티마이저는 대규모 모델의 행렬 구조 매개변수에 대해 설계된 경량 및 고속 옵티마이저입니다.

- 2. LiMuon은 모멘텀 기반 분산 감소 기법과 랜덤화된 SVD를 활용하여 메모리 사용량을 줄였습니다.

- 3. LiMuon은 비볼록 확률 최적화 문제에서 $\epsilon$-정류 솔루션을 찾기 위한 샘플 복잡도가 $O(\epsilon^{-3})$로 낮습니다.

- 4. 기존 Muon 옵티마이저의 수렴 분석은 엄격한 Lipschitz 매끄러움 가정에 의존했지만, LiMuon은 일반화된 매끄러움 조건에서도 유효합니다.

- 5. DistilGPT2 및 ViT 모델 훈련에서의 수치 실험 결과는 LiMuon 옵티마이저의 효율성을 입증합니다.

---

*Generated on 2025-09-20 05:52:33*