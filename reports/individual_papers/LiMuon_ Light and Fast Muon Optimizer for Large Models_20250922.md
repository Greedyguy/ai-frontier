# LiMuon: Light and Fast Muon Optimizer for Large Models

**Korean Title:** LiMuon: 대형 모델을 위한 경량 및 고속 뮤온 최적화기

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Momentum-based Variance Reduction|Momentum-based Variance Reduction]] [[keywords/specific/Stochastic Optimization|Stochastic Optimization]] [[keywords/broad/Artificial Intelligence|Artificial Intelligence]] [[keywords/broad/Large Models|Large Models]] [[keywords/unique/LiMuon Optimizer|LiMuon Optimizer]] [[categories/cs.LG|cs.LG]] [[2025-09-18/LiMuon_ Light and Fast Muon Optimizer for Large Models_20250918|LiMuon: Light and Fast Muon Optimizer for Large Models]] (99.2% similar) [[2025-09-22/On the Convergence of Muon and Beyond_20250922|On the Convergence of Muon and Beyond]] (89.8% similar) [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Momentum-based Variance Reduction
**🔗 Specific Connectable**: Randomized Singular Value Decomposition
**🔬 Broad Technical**: Artificial Intelligence, Non-convex Stochastic Optimization
**⭐ Unique Technical**: LiMuon Optimizer
## 🔗 유사한 논문
- [[2025-09-18/LiMuon_ Light and Fast Muon Optimizer for Large Models_20250918|LiMuon Light and Fast Muon Optimizer for Large Models]] (99.2% similar)
- [[2025-09-22/On the Convergence of Muon and Beyond_20250922|On the Convergence of Muon and Beyond]] (89.8% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (82.2% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.1% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (81.7% similar)


**ArXiv ID**: [2509.14562](https://arxiv.org/abs/2509.14562)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.14562.pdf)


**ArXiv ID**: [2509.14562](https://arxiv.org/abs/2509.14562)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.14562.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Momentum-based Variance Reduction
**🔗 Specific Connectable**: Stochastic Optimization
**⭐ Unique Technical**: LiMuon Optimizer
**🔬 Broad Technical**: Artificial Intelligence, Large Models

## 🏷️ 추출된 키워드



`Artificial Intelligence` • 

`Stochastic Optimization` • 

`Randomized Singular Value Decomposition` • 

`LiMuon Optimizer` • 

`Momentum-based Variance Reduction`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14562v2 Announce Type: replace 
Abstract: Large models recently are widely applied in artificial intelligence, so efficient training of large models has received widespread attention. More recently, a useful Muon optimizer is specifically designed for matrix-structured parameters of large models. Although some works have begun to studying Muon optimizer, the existing Muon and its variants still suffer from high sample complexity or high memory for large models. To fill this gap, we propose a light and fast Muon (LiMuon) optimizer for training large models, which builds on the momentum-based variance reduced technique and randomized Singular Value Decomposition (SVD). Our LiMuon optimizer has a lower memory than the current Muon and its variants. Moreover, we prove that our LiMuon has a lower sample complexity of $O(\epsilon^{-3})$ for finding an $\epsilon$-stationary solution of non-convex stochastic optimization under the smooth condition. Recently, the existing convergence analysis of Muon optimizer mainly relies on the strict Lipschitz smooth assumption, while some artificial intelligence tasks such as training large language models (LLMs) do not satisfy this condition. We also proved that our LiMuon optimizer has a sample complexity of $O(\epsilon^{-3})$ under the generalized smooth condition. Numerical experimental results on training DistilGPT2 and ViT models verify efficiency of our LiMuon optimizer.

## 🔍 Abstract (한글 번역)

arXiv:2509.14562v2 발표 유형: 교체  
초록: 최근 대형 모델이 인공지능에 널리 적용되면서, 대형 모델의 효율적인 학습이 많은 주목을 받고 있습니다. 최근에는 대형 모델의 행렬 구조화된 매개변수에 특화된 유용한 Muon 옵티마이저가 설계되었습니다. 일부 연구에서는 Muon 옵티마이저를 연구하기 시작했지만, 기존의 Muon과 그 변형들은 여전히 대형 모델에 대해 높은 샘플 복잡도나 높은 메모리 사용 문제를 겪고 있습니다. 이러한 격차를 해소하기 위해, 우리는 대형 모델 학습을 위한 가볍고 빠른 Muon (LiMuon) 옵티마이저를 제안합니다. 이는 모멘텀 기반의 분산 감소 기법과 무작위 특이값 분해(SVD)를 기반으로 합니다. 우리의 LiMuon 옵티마이저는 현재의 Muon과 그 변형들보다 낮은 메모리를 필요로 합니다. 또한, 우리는 LiMuon이 매끄러운 조건 하에서 비볼록 확률적 최적화의 $\epsilon$-정지 해를 찾기 위한 샘플 복잡도가 $O(\epsilon^{-3})$임을 증명했습니다. 최근 Muon 옵티마이저의 기존 수렴 분석은 주로 엄격한 리프시츠 매끄러움 가정에 의존하고 있지만, 대형 언어 모델(LLMs) 학습과 같은 일부 인공지능 작업은 이 조건을 만족하지 않습니다. 우리는 또한 LiMuon 옵티마이저가 일반화된 매끄러운 조건 하에서 $O(\epsilon^{-3})$의 샘플 복잡도를 가짐을 증명했습니다. DistilGPT2와 ViT 모델 학습에 대한 수치 실험 결과는 LiMuon 옵티마이저의 효율성을 검증합니다.

## 📝 요약

최근 인공지능 분야에서 대형 모델의 효율적인 학습이 중요한 이슈로 떠오르고 있습니다. 이를 위해 대형 모델의 행렬 구조화된 매개변수에 특화된 Muon 최적화기가 개발되었으나, 기존 Muon 및 변형 모델은 높은 샘플 복잡도와 메모리 사용량 문제를 겪고 있습니다. 이러한 문제를 해결하기 위해, 우리는 모멘텀 기반 분산 감소 기법과 무작위 SVD를 활용한 경량의 빠른 Muon(LiMuon) 최적화기를 제안합니다. LiMuon은 기존 Muon보다 낮은 메모리 사용량을 가지며, 매끄러운 조건 하에서 비볼록 확률 최적화의 $\epsilon$-정류 솔루션을 찾는 데 있어 샘플 복잡도가 $O(\epsilon^{-3})$임을 증명했습니다. 또한, 일반화된 매끄러운 조건 하에서도 동일한 샘플 복잡도를 보임을 입증했습니다. DistilGPT2와 ViT 모델 학습 실험을 통해 LiMuon의 효율성을 확인했습니다.

## 🎯 주요 포인트


- 1. LiMuon 옵티마이저는 대규모 모델의 행렬 구조 매개변수에 맞춰 설계된 경량 및 고속 옵티마이저입니다.

- 2. LiMuon은 모멘텀 기반 분산 감소 기법과 랜덤화된 특이값 분해(SVD)를 기반으로 하여 기존 Muon 및 변형보다 낮은 메모리 사용량을 자랑합니다.

- 3. LiMuon은 매끄러운 조건 하에서 비볼록 확률 최적화의 $\epsilon$-정류 솔루션을 찾기 위해 샘플 복잡도가 $O(\epsilon^{-3})$로 낮습니다.

- 4. LiMuon은 일반화된 매끄러운 조건 하에서도 샘플 복잡도가 $O(\epsilon^{-3})$임을 증명했습니다.

- 5. DistilGPT2 및 ViT 모델 훈련에 대한 수치 실험 결과, LiMuon 옵티마이저의 효율성이 검증되었습니다.


---

*Generated on 2025-09-22 16:04:33*