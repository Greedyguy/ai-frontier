
# Don't Forget the Nonlinearity: Unlocking Activation Functions in Efficient Fine-Tuning

**Korean Title:** 비선형성을 잊지 마세요: 효율적인 미세 조정에서 활성화 함수의 잠재력 발휘

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Activation Space Tuning

## 🔗 유사한 논문
- [[HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (80.9% similar)
- [[NIRVANA Structured pruning reimagined for large language models compression]] (78.1% similar)
- [[Controllable Pareto Trade-off between Fairness and Accuracy]] (77.4% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (77.3% similar)
- [[FroM Frobenius Norm-Based Data-Free Adaptive Model Merging]] (77.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13240v2 Announce Type: replace 
Abstract: Existing parameter-efficient fine-tuning (PEFT) methods primarily adapt weight matrices while keeping activation functions fixed. We introduce \textbf{NoRA}, the first PEFT framework that directly adapts nonlinear activation functions in pretrained transformer-based models. NoRA replaces fixed activations with learnable rational functions and applies structured low-rank updates to numerator and denominator coefficients, with a group-wise design that localizes adaptation and improves stability at minimal cost. On vision transformers trained on CIFAR-10 and CIFAR-100, NoRA matches or exceeds full fine-tuning while updating only 0.4\% of parameters (0.02M), achieving accuracy gains of +0.17\% and +0.27\%. When combined with LoRA (\textbf{NoRA++}), it outperforms LoRA and DoRA under matched training budgets by adding fewer trainable parameters. On LLaMA3-8B instruction tuning, NoRA++ consistently improves generation quality, yielding average MMLU gains of +0.3\%--0.8\%, including +1.6\% on STEM (Alpaca) and +1.3\% on OpenOrca. We further show that NoRA constrains adaptation to a low-dimensional functional subspace, implicitly regularizing update magnitude and direction. These results establish activation-space tuning as a complementary and highly parameter-efficient alternative to weight-based PEFT, positioning activation functions as first-class objects for model adaptation.

## 🔍 Abstract (한글 번역)

arXiv:2509.13240v2 발표 유형: 교체

초록: 기존의 파라미터 효율적 미세 조정(PEFT) 방법은 주로 가중치 행렬을 조정하면서 활성화 함수를 고정된 상태로 유지합니다. 우리는 사전 학습된 트랜스포머 기반 모델에서 비선형 활성화 함수를 직접 조정하는 최초의 PEFT 프레임워크인 \textbf{NoRA}를 소개합니다. NoRA는 고정된 활성화 함수를 학습 가능한 유리 함수로 대체하고, 분자와 분모 계수에 구조화된 저랭크 업데이트를 적용하며, 그룹별 설계를 통해 적응을 국지화하고 최소한의 비용으로 안정성을 향상시킵니다. CIFAR-10과 CIFAR-100에서 훈련된 비전 트랜스포머에서 NoRA는 전체 미세 조정을 수행하거나 이를 초과하며, 단 0.4\%의 파라미터(0.02M)만 업데이트하여 정확도 향상을 각각 +0.17\%와 +0.27\% 달성합니다. LoRA와 결합된 경우(\textbf{NoRA++}), NoRA++는 더 적은 학습 가능한 파라미터를 추가하여 동일한 훈련 예산 하에서 LoRA와 DoRA를 능가합니다. LLaMA3-8B 지시 조정에서 NoRA++는 생성 품질을 지속적으로 향상시키며, 평균 MMLU 향상을 +0.3\%--0.8\% 달성하고, STEM(Alpaca)에서 +1.6\% 및 OpenOrca에서 +1.3\%를 포함합니다. 우리는 또한 NoRA가 저차원 기능적 부분 공간에 적응을 제한하여 업데이트 크기와 방향을 암묵적으로 정규화함을 보여줍니다. 이러한 결과는 활성화 공간 튜닝이 가중치 기반 PEFT에 대한 보완적이고 매우 파라미터 효율적인 대안으로서, 모델 적응을 위한 활성화 함수를 일급 객체로 위치시킵니다.

## 📝 요약

기존의 매개변수 효율적 미세 조정(PEFT) 방법은 주로 가중치 행렬을 조정하지만, 활성화 함수는 고정된 상태로 유지합니다. 본 논문에서는 사전 학습된 트랜스포머 기반 모델에서 비선형 활성화 함수를 직접 조정하는 최초의 PEFT 프레임워크인 NoRA를 소개합니다. NoRA는 고정된 활성화 함수를 학습 가능한 유리 함수로 대체하고, 분자 및 분모 계수에 구조화된 저랭크 업데이트를 적용하여 안정성을 높입니다. CIFAR-10 및 CIFAR-100에서 NoRA는 전체 미세 조정과 동등하거나 더 나은 성능을 보이며, 매개변수의 0.4%만 업데이트하여 정확도를 각각 +0.17% 및 +0.27% 향상시켰습니다. NoRA와 LoRA를 결합한 NoRA++는 동일한 학습 예산 하에서 더 적은 매개변수로 LoRA와 DoRA를 능가합니다. LLaMA3-8B 지침 조정에서는 NoRA++가 일관되게 생성 품질을 개선하여 평균 MMLU를 +0.3%에서 +0.8%까지 향상시켰습니다. 이 연구는 활성화 함수 조정이 가중치 기반 PEFT의 보완적 대안임을 입증하며, 모델 적응을 위한 중요한 요소로 활성화 함수를 제시합니다.

## 🎯 주요 포인트

- 1. NoRA는 비선형 활성화 함수를 직접 조정하는 최초의 PEFT 프레임워크로, 사전 학습된 트랜스포머 기반 모델에서 학습 가능한 유리 함수로 고정된 활성화를 대체합니다.

- 2. NoRA는 CIFAR-10 및 CIFAR-100에서 훈련된 비전 트랜스포머에서 전체 파인 튜닝과 동등하거나 그 이상의 성능을 보이며, 단 0.4%의 파라미터만 업데이트하여 정확도 향상을 달성합니다.

- 3. NoRA++는 LoRA와 결합하여, 동일한 훈련 예산 하에서 더 적은 학습 가능한 파라미터를 추가하여 LoRA 및 DoRA를 능가합니다.

- 4. NoRA는 저차원 함수적 부분 공간으로의 적응을 제한하여, 업데이트의 크기와 방향을 암묵적으로 정규화합니다.

- 5. 활성화 공간 튜닝은 가중치 기반 PEFT에 대한 보완적이고 매우 파라미터 효율적인 대안으로 자리매김하며, 활성화 함수를 모델 적응의 주요 객체로 위치시킵니다.

---

*Generated on 2025-09-19 15:41:55*