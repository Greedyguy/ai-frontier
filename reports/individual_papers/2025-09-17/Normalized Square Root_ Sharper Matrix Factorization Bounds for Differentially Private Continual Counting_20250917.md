---
keywords:
  - Differential Privacy
  - Matrix Factorization Norms
  - Continual Counting
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:49:34.570773",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Differential Privacy",
    "Matrix Factorization Norms",
    "Continual Counting"
  ],
  "rejected_keywords": [
    "Deep Learning"
  ],
  "similarity_scores": {
    "Differential Privacy": 0.85,
    "Matrix Factorization Norms": 0.78,
    "Continual Counting": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Normalized Square Root: Sharper Matrix Factorization Bounds for Differentially Private Continual Counting

**Korean Title:** 정규화된 제곱근: 차등 프라이버시를 위한 지속적 카운팅의 더 날카로운 행렬 분해 경계

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Differential Privacy|differential privacy]]
**⚡ Unique Technical**: [[keywords/Matrix Factorization Norms|factorization norms]], [[keywords/Continual Counting|continual counting]]

## 🔗 유사한 논문
- [[Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (77.7% similar)
- [[Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (77.1% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (77.0% similar)
- [[Gap-Dependent Bounds for Federated $Q$-learning_20250919|Gap-Dependent Bounds for Federated $Q$-learning]] (76.1% similar)
- [[Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (76.1% similar)

## 📋 저자 정보

**Authors:** Monika Henzinger, Nikita P. Kalinin, Jalaj Upadhyay

## 📄 Abstract (원문)

The factorization norms of the lower-triangular all-ones $n \times n$ matrix,
$\gamma_2(M_{count})$ and $\gamma_{F}(M_{count})$, play a central role in
differential privacy as they are used to give theoretical justification of the
accuracy of the only known production-level private training algorithm of deep
neural networks by Google. Prior to this work, the best known upper bound on
$\gamma_2(M_{count})$ was $1 + \frac{\log n}{\pi}$ by Mathias (Linear Algebra
and Applications, 1993), and the best known lower bound was $\frac{1}{\pi}(2 +
\log(\frac{2n+1}{3})) \approx 0.507 + \frac{\log n}{\pi}$ (Matou\v{s}ek,
Nikolov, Talwar, IMRN 2020), where $\log$ denotes the natural logarithm.
Recently, Henzinger and Upadhyay (SODA 2025) gave the first explicit
factorization that meets the bound of Mathias (1993) and asked whether there
exists an explicit factorization that improves on Mathias' bound. We answer
this question in the affirmative. Additionally, we improve the lower bound
significantly. More specifically, we show that $$
  0.701 + \frac{\log n}{\pi} + o(1) \;\leq\; \gamma_2(M_{count}) \;\leq\; 0.846
+ \frac{\log n}{\pi} + o(1). $$ That is, we reduce the gap between the upper
and lower bound to $0.14 + o(1)$.
  We also show that our factors achieve a better upper bound for
$\gamma_{F}(M_{count})$ compared to prior work, and we establish an improved
lower bound: $$
  0.701 + \frac{\log n}{\pi} + o(1) \;\leq\; \gamma_{F}(M_{count}) \;\leq\;
0.748 + \frac{\log n}{\pi} + o(1). $$ That is, the gap between the lower and
upper bound provided by our explicit factorization is $0.047 + o(1)$.

## 🔍 Abstract (한글 번역)

하삼각형의 모든 요소가 1인 $n \times n$ 행렬의 분해 규범, $\gamma_2(M_{count})$와 $\gamma_{F}(M_{count})$는 차등 개인정보 보호에서 중심적인 역할을 합니다. 이는 Google의 유일한 생산 수준의 비공개 심층 신경망 훈련 알고리즘의 정확성을 이론적으로 정당화하는 데 사용됩니다. 이 연구 이전에는 $\gamma_2(M_{count})$에 대한 가장 잘 알려진 상한은 Mathias가 제시한 $1 + \frac{\log n}{\pi}$ (Linear Algebra and Applications, 1993)였으며, 가장 잘 알려진 하한은 Matoušek, Nikolov, Talwar가 제시한 $\frac{1}{\pi}(2 + \log(\frac{2n+1}{3})) \approx 0.507 + \frac{\log n}{\pi}$ (IMRN 2020)였습니다. 여기서 $\log$는 자연 로그를 나타냅니다. 최근 Henzinger와 Upadhyay (SODA 2025)는 Mathias (1993)의 경계를 충족하는 첫 번째 명시적 분해를 제시하였고, Mathias의 경계를 개선하는 명시적 분해가 존재하는지에 대한 질문을 제기했습니다. 우리는 이 질문에 긍정적으로 답합니다. 추가적으로, 우리는 하한을 상당히 개선하였습니다. 보다 구체적으로, 우리는 다음을 보입니다: $$ 0.701 + \frac{\log n}{\pi} + o(1) \;\leq\; \gamma_2(M_{count}) \;\leq\; 0.846 + \frac{\log n}{\pi} + o(1). $$ 즉, 상한과 하한 사이의 간격을 $0.14 + o(1)$로 줄였습니다. 또한, 우리는 $\gamma_{F}(M_{count})$에 대해 이전 연구보다 더 나은 상한을 달성하는 요소를 제시하고, 개선된 하한을 확립합니다: $$ 0.701 + \frac{\log n}{\pi} + o(1) \;\leq\; \gamma_{F}(M_{count}) \;\leq\; 0.748 + \frac{\log n}{\pi} + o(1). $$ 즉, 우리의 명시적 분해가 제공하는 하한과 상한 사이의 간격은 $0.047 + o(1)$입니다.

## 📝 요약

이 논문은 하삼각형의 모든 원소가 1인 $n \times n$ 행렬의 분해 노름 $\gamma_2(M_{count})$와 $\gamma_{F}(M_{count})$에 대한 새로운 상한 및 하한을 제시합니다. 이는 구글의 심층 신경망 비공개 학습 알고리즘의 정확성을 이론적으로 뒷받침하는 데 중요한 역할을 합니다. 기존 상한은 Mathias(1993)에 의해 $1 + \frac{\log n}{\pi}$로 알려져 있었고, 하한은 Matoušek 등(2020)에 의해 $\frac{1}{\pi}(2 + \log(\frac{2n+1}{3}))$로 제시되었습니다. 본 연구는 Mathias의 상한을 개선하는 명시적 분해를 제시하고, 하한도 $0.701 + \frac{\log n}{\pi} + o(1)$로 크게 개선하였습니다. 또한 $\gamma_{F}(M_{count})$에 대해서도 상한과 하한을 각각 $0.748 + \frac{\log n}{\pi} + o(1)$과 $0.701 + \frac{\log n}{\pi} + o(1)$로 제시하여, 상하한 간격을 $0.047 + o(1)$로 줄였습니다.

## 🎯 주요 포인트

- 1. 이 연구는 하삼각형 모든 원소가 1인 $n \times n$ 행렬의 분해 노름 $\gamma_2(M_{count})$와 $\gamma_{F}(M_{count})$의 상한과 하한을 개선하였습니다.

- 2. 기존의 상한은 Mathias(1993)에 의해 $1 + \frac{\log n}{\pi}$로 알려져 있었고, 하한은 Matoušek, Nikolov, Talwar(2020)에 의해 $\frac{1}{\pi}(2 + \log(\frac{2n+1}{3}))$로 제시되었습니다.

- 3. 본 연구는 $\gamma_2(M_{count})$의 하한을 $0.701 + \frac{\log n}{\pi} + o(1)$로, 상한을 $0.846 + \frac{\log n}{\pi} + o(1)$로 제시하여 상한과 하한의 차이를 $0.14 + o(1)$로 줄였습니다.

- 4. 또한, $\gamma_{F}(M_{count})$에 대해서도 상한을 개선하고 하한을 $0.701 + \frac{\log n}{\pi} + o(1)$로, 상한을 $0.748 + \frac{\log n}{\pi} + o(1)$로 제시하여 차이를 $0.047 + o(1)$로 줄였습니다.

- 5. 이 연구는 Google의 딥러닝 프라이빗 트레이닝 알고리즘의 이론적 정확성을 뒷받침하는 중요한 역할을 합니다.

---

*Generated on 2025-09-20 07:39:16*