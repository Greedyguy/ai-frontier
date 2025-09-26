---
keywords:
  - Large Language Models
  - Pre-Training
  - Scaling Laws
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:15:25.020235",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Pre-Training",
    "Scaling Laws"
  ],
  "rejected_keywords": [
    "Ensemble Scaling",
    "Data Efficiency"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Pre-Training": 0.85,
    "Scaling Laws": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Pre-training under infinite compute

**Korean Title:** 무한 계산에서의 사전 훈련

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|language model]], [[keywords/Scaling Laws|scaling laws]]
**⚡ Unique Technical**: [[keywords/Pre-Training|pre-training]]

## 🔗 유사한 논문
- [[Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (82.7% similar)
- [[From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (81.9% similar)
- [[Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250918|Mind the Gap Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (81.4% similar)
- [[(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (81.4% similar)
- [[PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (80.6% similar)

## 📋 저자 정보

**Authors:** Konwoo Kim, Suhas Kotha, Percy Liang, Tatsunori Hashimoto

## 📄 Abstract (원문)

Since compute grows much faster than web text available for language model
pre-training, we ask how one should approach pre-training under fixed data and
no compute constraints. We first show that existing data-constrained approaches
of increasing epoch count and parameter count eventually overfit, and we
significantly improve upon such recipes by properly tuning regularization,
finding that the optimal weight decay is $30\times$ larger than standard
practice. Since our regularized recipe monotonically decreases loss following a
simple power law in parameter count, we estimate its best possible performance
via the asymptote of its scaling law rather than the performance at a fixed
compute budget. We then identify that ensembling independently trained models
achieves a significantly lower loss asymptote than the regularized recipe. Our
best intervention combining epoching, regularization, parameter scaling, and
ensemble scaling achieves an asymptote at 200M tokens using $5.17\times$ less
data than our baseline, and our data scaling laws predict that this improvement
persists at higher token budgets. We find that our data efficiency gains can be
realized at much smaller parameter counts as we can distill an ensemble into a
student model that is 8$\times$ smaller and retains $83\%$ of the ensembling
benefit. Finally, our interventions designed for validation loss generalize to
downstream benchmarks, achieving a $9\%$ improvement for pre-training evals and
a $17.5\times$ data efficiency improvement over continued pre-training on math
mid-training data. Our results show that simple algorithmic improvements can
enable significantly more data-efficient pre-training in a compute-rich future.

## 🔍 Abstract (한글 번역)

컴퓨팅 성능이 언어 모델 사전 학습을 위한 웹 텍스트의 가용성보다 훨씬 빠르게 증가함에 따라, 우리는 고정된 데이터와 컴퓨팅 제약 없이 사전 학습을 어떻게 접근해야 하는지에 대해 질문합니다. 먼저, 에포크 수와 파라미터 수를 증가시키는 기존의 데이터 제약 접근 방식이 결국 과적합된다는 것을 보여주고, 적절한 정규화를 통해 이러한 방식들을 크게 개선할 수 있음을 증명합니다. 최적의 가중치 감쇠가 표준 관행보다 $30\times$ 더 크다는 것을 발견했습니다. 우리의 정규화된 레시피는 파라미터 수에 따라 단순한 멱법칙을 따르며 손실을 단조롭게 감소시키므로, 고정된 컴퓨팅 예산에서의 성능보다는 스케일링 법칙의 점근선을 통해 최상의 성능을 추정합니다. 이후 독립적으로 학습된 모델을 앙상블하는 것이 정규화된 레시피보다 훨씬 낮은 손실 점근선을 달성한다는 것을 확인했습니다. 에포킹, 정규화, 파라미터 스케일링, 앙상블 스케일링을 결합한 우리의 최적 개입은 200M 토큰에서 점근선을 달성하며, 이는 기본값보다 $5.17\times$ 적은 데이터를 사용합니다. 우리의 데이터 스케일링 법칙은 이 개선이 더 높은 토큰 예산에서도 지속됨을 예측합니다. 우리는 앙상블을 8배 작은 학생 모델로 증류하여 앙상블의 이점의 $83\%$를 유지할 수 있기 때문에, 우리의 데이터 효율성 향상이 훨씬 작은 파라미터 수에서도 실현될 수 있음을 발견했습니다. 마지막으로, 검증 손실을 위해 설계된 우리의 개입은 다운스트림 벤치마크에 일반화되어, 사전 학습 평가에서 $9\%$의 개선과 수학 중간 학습 데이터에 대한 지속적인 사전 학습에 비해 $17.5\times$의 데이터 효율성 개선을 달성했습니다. 우리의 결과는 간단한 알고리즘 개선이 컴퓨팅이 풍부한 미래에 훨씬 더 데이터 효율적인 사전 학습을 가능하게 할 수 있음을 보여줍니다.

## 📝 요약

이 논문은 고정된 데이터와 제한된 컴퓨팅 환경에서 언어 모델의 사전 학습을 최적화하는 방법을 제안합니다. 기존의 데이터 제약 접근법은 에포크 수와 파라미터 수를 늘리지만 결국 과적합 문제가 발생합니다. 이를 개선하기 위해 정규화를 적절히 조정하여, 최적의 가중치 감쇠가 기존보다 30배 크다는 것을 발견했습니다. 또한, 독립적으로 학습된 모델을 앙상블하는 것이 더 낮은 손실 비율을 달성함을 확인했습니다. 에포크, 정규화, 파라미터 및 앙상블 스케일링을 결합한 최적의 방법은 200M 토큰에서 기존보다 5.17배 적은 데이터로 최적의 성능을 보입니다. 이 방법은 작은 파라미터 수에서도 효과적이며, 앙상블을 8배 작은 학생 모델로 증류하여 83%의 성능을 유지합니다. 이러한 개선은 다운스트림 벤치마크에서도 일반화되어, 사전 학습 평가에서 9% 개선과 수학 중간 학습 데이터에서 17.5배의 데이터 효율성을 보였습니다. 결과적으로, 간단한 알고리즘 개선이 데이터 효율적인 사전 학습을 가능하게 함을 보여줍니다.

## 🎯 주요 포인트

- 1. 고정된 데이터와 컴퓨팅 제약 조건 하에서의 사전 훈련 접근법을 탐구하며, 기존의 데이터 제약 접근법이 결국 과적합되는 문제를 해결하기 위해 정규화를 조정하여 성능을 개선했습니다.

- 2. 최적의 가중치 감소가 일반적인 관행보다 30배 더 크다는 것을 발견하고, 매개변수 수에 따른 손실 감소가 단순한 멱 법칙을 따름을 확인했습니다.

- 3. 독립적으로 훈련된 모델을 앙상블하는 것이 정규화된 방법보다 더 낮은 손실 비대칭을 달성한다는 것을 확인했습니다.

- 4. 에포킹, 정규화, 매개변수 스케일링, 앙상블 스케일링을 결합한 최적의 개입이 200M 토큰에서 비대칭을 달성하며, 이는 기준선보다 5.17배 적은 데이터를 사용합니다.

- 5. 데이터 효율성 향상이 훨씬 작은 매개변수 수에서도 실현 가능하며, 앙상블을 8배 작은 학생 모델로 증류하여 앙상블 이점의 83%를 유지할 수 있음을 발견했습니다.

---

*Generated on 2025-09-20 05:41:29*