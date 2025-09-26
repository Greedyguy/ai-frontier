---
keywords:
  - Uncertainty Quantification
  - Aleatoric and Epistemic Uncertainty
  - Self-consistency Discrepancy Score
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13262
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:15:40.017504",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Uncertainty Quantification",
    "Aleatoric and Epistemic Uncertainty",
    "Self-consistency Discrepancy Score"
  ],
  "rejected_keywords": [
    "Deep Learning",
    "Split-Point Analysis"
  ],
  "similarity_scores": {
    "Uncertainty Quantification": 0.8,
    "Aleatoric and Epistemic Uncertainty": 0.78,
    "Self-consistency Discrepancy Score": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning

**Korean Title:** 딥 러닝에서의 알레아토릭 및 에피스테믹 불확실성의 효율적이고 통합된 양적화를 위한 사후 분할점 자기 일관성 검증

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**⚡ Unique Technical**: [[keywords/Aleatoric and Epistemic Uncertainty|Aleatoric and Epistemic Uncertainty]], [[keywords/Self-consistency Discrepancy Score|Self-consistency Discrepancy Score]]

## 🔗 유사한 논문
- [[A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (83.8% similar)
- [[Privacy-Preserving Uncertainty Disclosure for Facilitating Enhanced Energy Storage Dispatch]] (80.1% similar)
- [[DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (79.9% similar)
- [[Towards_Trustworthy_Vital_Sign_Forecasting_Leveraging_Uncertainty_for_Prediction_Intervals_20250918|Towards Trustworthy Vital Sign Forecasting: Leveraging Uncertainty for Prediction Intervals]] (79.9% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13262v2 Announce Type: replace 
Abstract: Uncertainty quantification (UQ) is vital for trustworthy deep learning, yet existing methods are either computationally intensive, such as Bayesian or ensemble methods, or provide only partial, task-specific estimates, such as single-forward-pass techniques. In this paper, we propose a post-hoc single-forward-pass framework that jointly captures aleatoric and epistemic uncertainty without modifying or retraining pretrained models. Our method applies \emph{Split-Point Analysis} (SPA) to decompose predictive residuals into upper and lower subsets, computing \emph{Mean Absolute Residuals} (MARs) on each side. We prove that, under ideal conditions, the total MAR equals the harmonic mean of subset MARs; deviations define a novel \emph{Self-consistency Discrepancy Score} (SDS) for fine-grained epistemic estimation across regression and classification. For regression, side-specific quantile regression yields prediction intervals with improved empirical coverage, which are further calibrated via SDS. For classification, when calibration data are available, we apply SPA-based calibration identities to adjust the softmax outputs and then compute predictive entropy on these calibrated probabilities. Extensive experiments on diverse regression and classification benchmarks demonstrate that our framework matches or exceeds several state-of-the-art UQ methods while incurring minimal overhead.
  Our source code is available at https://github.com/zzz0527/SPC-UQ.

## 🔍 Abstract (한글 번역)

arXiv:2509.13262v2 발표 유형: 대체
요약: 불확실성 양화(UQ)는 신뢰할 수 있는 딥 러닝을 위해 중요하지만, 기존 방법은 베이지안이나 앙상블 방법과 같이 계산량이 많거나, 단일 전방향 패스 기술과 같이 부분적이고 과제 특정 추정만을 제공합니다. 본 논문에서는 사전 훈련된 모델을 수정하거나 재훈련하지 않고 알레토릭 및 에피스테믹 불확실성을 동시에 포착하는 사후 단일 전방향 패스 프레임워크를 제안합니다. 우리의 방법은 예측 잔차를 상하 부분으로 분해하고 각 측면에서 \emph{평균 절대 잔차}(MARs)를 계산하는 \emph{분할점 분석}(SPA)을 적용합니다. 우리는 이상적인 조건 하에서 총 MAR이 부분 MAR의 조화평균과 같음을 증명하며, 이탈은 회귀 및 분류를 통해 세밀한 에피스테믹 추정을 위한 새로운 \emph{자일일성 불일치 점수}(SDS)를 정의합니다. 회귀의 경우, 측면별 분위수 회귀는 개선된 경험적 커버리지를 갖는 예측 구간을 제공하며, 이는 SDS를 통해 더욱 보정됩니다. 분류의 경우, 보정 데이터가 있는 경우, 우리는 소프트맥스 출력을 조정하기 위해 SPA 기반 보정 항등식을 적용하고, 이러한 보정 확률에 대해 예측 엔트로피를 계산합니다. 다양한 회귀 및 분류 벤치마크에 대한 광범위한 실험 결과는 우리의 프레임워크가 최소한의 오버헤드를 발생시키면서도 여러 최첨단 UQ 방법과 일치하거나 능가함을 보여줍니다.
우리의 소스 코드는 https://github.com/zzz0527/SPC-UQ에서 사용할 수 있습니다.

## 📝 요약

이 논문은 신뢰할 수 있는 딥러닝을 위한 불확실성 양자화가 중요한데, 기존 방법은 계산량이 많거나 일부 특정 작업에 대한 추정만 제공한다. 본 논문에서는 사전 훈련된 모델을 수정하거나 재훈련하지 않고 aleatoric 및 epistemic 불확실성을 동시에 캡처하는 후훅 단일 전방향 패스 프레임워크를 제안한다. 이 방법은 예측 잔차를 상하 부분으로 분해하고 각 측면에서 평균 절대 잔차를 계산하는 'Split-Point Analysis' (SPA)를 적용한다. 이를 통해 회귀 및 분류에 걸쳐 세밀한 epistemic 추정을 위한 'Self-consistency Discrepancy Score' (SDS)를 정의한다. 실험 결과는 본 프레임워크가 최소한의 오버헤드를 발생시키면서도 여러 최신 UQ 방법을 능가한다는 것을 보여준다.

## 🎯 주요 포인트

- 신뢰할 수 있는 딥러닝을 위한 불확실성 양자화는 중요하다.

- 이 논문에서는 사전 훈련된 모델을 수정하거나 재훈련하지 않고 aleatoric과 epistemic 불확실성을 동시에 캡처하는 프레임워크를 제안한다.

- 새로운 Self-consistency Discrepancy Score를 통해 regression 및 classification에서 미세한 epistemic 추정을 제공한다.

- 실험 결과는 이 프레임워크가 최소한의 오버헤드를 발생시키면서도 여러 최신 UQ 방법을 능가한다.

---

*Generated on 2025-09-18 16:48:48*