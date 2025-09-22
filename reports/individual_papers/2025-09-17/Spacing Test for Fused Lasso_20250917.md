# Spacing Test for Fused Lasso

**Korean Title:** 퓨즈드 라소를 위한 간격 테스트

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Rieko Tasaka|Rieko Tasaka]] [[authors/Tatsuya Kimura|Tatsuya Kimura]] [[authors/Joe Suzuki|Joe Suzuki]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Post-selection Inference, Change-point Detection

## 🔗 유사한 논문
- [[Structure-Preserving Margin Distribution Learning for High-Order Tensor Data with Low-Rank Decomposition_20250919|Structure-Preserving Margin Distribution Learning for High-Order Tensor Data with Low-Rank Decomposition]] (74.9% similar)
- [[Preference Isolation Forest for Structure-based Anomaly Detection_20250919|Preference Isolation Forest for Structure-based Anomaly Detection]] (74.7% similar)
- [[Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (74.5% similar)
- [[MetaSel_ A Test Selection Approach for Fine-tuned DNN Models_20250918|MetaSel A Test Selection Approach for Fine-tuned DNN Models]] (74.0% similar)
- [[Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (74.0% similar)

## 📋 저자 정보

**Authors:** Rieko Tasaka, Tatsuya Kimura, Joe Suzuki

## 📄 Abstract (원문)

This study addresses the unresolved problem of selecting the regularization
parameter in the fused lasso. In particular, we extend the framework of the
Spacing Test proposed by Tibshirani et al. to the fused lasso, providing a
theoretical foundation for post-selection inference by characterizing the
selection event as a polyhedral constraint. Based on the analysis of the
solution path of the fused lasso using a LARS-type algorithm, we derive exact
conditional $p$-values for the selected change-points. Our method broadens the
applicability of the Spacing Test from the standard lasso to fused penalty
structures. Furthermore, through numerical experiments comparing the proposed
method with sequential versions of AIC and BIC as well as cross-validation, we
demonstrate that the proposed approach properly controls the type I error while
achieving high detection power. This work offers a theoretically sound and
computationally practical solution for parameter selection and post-selection
inference in structured signal estimation problems. Keywords: Fused Lasso,
Regularization parameter selection, Spacing Test for Lasso, Selective
inference, Change-point detection

## 🔍 Abstract (한글 번역)

이 연구는 융합 라쏘(fused lasso)에서 정규화 매개변수 선택의 미해결 문제를 다룹니다. 특히, Tibshirani 등(2012)이 제안한 Spacing Test의 틀을 융합 라쏘에 확장하여, 선택 사건을 다면체 제약으로 특징짓는 이론적 기반을 제공함으로써 선택 후 추론을 가능하게 합니다. LARS 유형 알고리즘을 사용한 융합 라쏘의 해 경로 분석을 기반으로, 선택된 변화점에 대한 정확한 조건부 $p$-값을 도출합니다. 우리의 방법은 표준 라쏘에서 융합 패널티 구조로 Spacing Test의 적용 범위를 넓힙니다. 또한, 제안된 방법을 AIC와 BIC의 순차적 버전 및 교차 검증과 비교한 수치 실험을 통해, 제안된 접근법이 유형 I 오류를 적절히 제어하면서 높은 탐지력을 달성함을 입증합니다. 이 연구는 구조화된 신호 추정 문제에서 매개변수 선택 및 선택 후 추론을 위한 이론적으로 타당하고 계산적으로 실용적인 솔루션을 제공합니다. 키워드: 융합 라쏘, 정규화 매개변수 선택, 라쏘를 위한 Spacing Test, 선택적 추론, 변화점 탐지

## 📝 요약

이 연구는 퓨즈드 라쏘에서 정규화 매개변수 선택 문제를 해결하고자 합니다. Tibshirani 등이 제안한 Spacing Test를 확장하여 퓨즈드 라쏘에 적용하고, 선택 이벤트를 다면체 제약으로 특징지어 이론적 기반을 제공합니다. LARS 유형 알고리즘을 사용한 해 경로 분석을 통해 선택된 변화점에 대한 정확한 조건부 p-값을 도출합니다. 제안된 방법은 기존 라쏘에서 퓨즈드 패널티 구조로 Spacing Test의 적용 범위를 넓히며, AIC, BIC, 교차 검증과의 비교 실험을 통해 제안된 방법이 1종 오류를 적절히 제어하면서 높은 탐지력을 달성함을 보여줍니다. 이 연구는 구조화된 신호 추정 문제에서 매개변수 선택과 선택 후 추론에 대한 이론적으로 타당하고 계산적으로 실용적인 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 이 연구는 퓨즈드 라쏘에서 정규화 파라미터 선택 문제를 해결하고자 합니다.

- 2. Tibshirani 등이 제안한 Spacing Test를 퓨즈드 라쏘에 확장하여 선택 이벤트를 다면체 제약으로 특징짓습니다.

- 3. LARS 유형 알고리즘을 사용한 퓨즈드 라쏘의 솔루션 경로 분석을 통해 선택된 변화점에 대한 정확한 조건부 p-값을 도출합니다.

- 4. 제안된 방법은 AIC, BIC의 순차적 버전 및 교차 검증과 비교하여 높은 검출력을 유지하면서 I형 오류를 적절히 제어합니다.

- 5. 이 연구는 구조화된 신호 추정 문제에서 파라미터 선택 및 선택 후 추론을 위한 이론적으로 타당하고 계산적으로 실용적인 솔루션을 제공합니다.

---

*Generated on 2025-09-20 07:40:55*