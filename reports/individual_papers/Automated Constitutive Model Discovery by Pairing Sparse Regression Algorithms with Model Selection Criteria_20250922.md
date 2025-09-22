# Automated Constitutive Model Discovery by Pairing Sparse Regression Algorithms with Model Selection Criteria

**Korean Title:** 희소 회귀 알고리즘과 모델 선택 기준을 결합한 자동 구성 모델 발견

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Constitutive Model Discovery

## 🔗 유사한 논문
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (79.7% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE Metadata Extraction and Validation in Scientific Papers Using LLMs]] (79.2% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (78.5% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.2% similar)
- [[2025-09-19/Evolution of Kernels_ Automated RISC-V Kernel Optimization with Large Language Models_20250919|Evolution of Kernels Automated RISC-V Kernel Optimization with Large Language Models]] (77.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16040v1 Announce Type: new 
Abstract: The automated discovery of constitutive models from data has recently emerged as a promising alternative to the traditional model calibration paradigm. In this work, we present a fully automated framework for constitutive model discovery that systematically pairs three sparse regression algorithms (Least Absolute Shrinkage and Selection Operator (LASSO), Least Angle Regression (LARS), and Orthogonal Matching Pursuit (OMP)) with three model selection criteria: $K$-fold cross-validation (CV), Akaike Information Criterion (AIC), and Bayesian Information Criterion (BIC). This pairing yields nine distinct algorithms for model discovery and enables a systematic exploration of the trade-off between sparsity, predictive performance, and computational cost. While LARS serves as an efficient path-based solver for the $\ell_1$-constrained problem, OMP is introduced as a tractable heuristic for $\ell_0$-regularized selection. The framework is applied to both isotropic and anisotropic hyperelasticity, utilizing both synthetic and experimental datasets. Results reveal that all nine algorithm-criterion combinations perform consistently well for the discovery of isotropic and anisotropic materials, yielding highly accurate constitutive models. These findings broaden the range of viable discovery algorithms beyond $\ell_1$-based approaches such as LASSO.

## 🔍 Abstract (한글 번역)

arXiv:2509.16040v1 발표 유형: 신규  
초록: 데이터로부터 구성 모델을 자동으로 발견하는 방법은 최근 전통적인 모델 보정 패러다임에 대한 유망한 대안으로 부상하고 있습니다. 본 연구에서는 구성 모델 발견을 위한 완전 자동화된 프레임워크를 제시하며, 이는 세 가지 희소 회귀 알고리즘(최소 절대 수축 및 선택 연산자(LASSO), 최소 각 회귀(LARS), 직교 매칭 추구(OMP))를 세 가지 모델 선택 기준($K$-겹 교차 검증(CV), Akaike 정보 기준(AIC), 베이지안 정보 기준(BIC))과 체계적으로 짝지어줍니다. 이러한 조합은 모델 발견을 위한 아홉 가지 독특한 알고리즘을 제공하며, 희소성, 예측 성능, 계산 비용 간의 절충을 체계적으로 탐색할 수 있게 합니다. LARS는 $\ell_1$-제약 문제에 대한 효율적인 경로 기반 해법으로 작용하는 반면, OMP는 $\ell_0$-정규화 선택에 대한 실용적인 휴리스틱으로 도입됩니다. 이 프레임워크는 합성 및 실험 데이터셋을 활용하여 등방성 및 이방성 초탄성에 적용됩니다. 결과는 아홉 가지 알고리즘-기준 조합이 등방성 및 이방성 재료 발견에 대해 일관되게 우수한 성능을 발휘하며, 매우 정확한 구성 모델을 산출함을 보여줍니다. 이러한 발견은 LASSO와 같은 $\ell_1$ 기반 접근법을 넘어서는 다양한 유효한 발견 알고리즘의 범위를 확장합니다.

## 📝 요약

이 논문은 데이터로부터 구성 모델을 자동으로 발견하는 새로운 프레임워크를 제안합니다. LASSO, LARS, OMP 세 가지 희소 회귀 알고리즘과 $K$-겹 교차 검증, AIC, BIC 세 가지 모델 선택 기준을 조합하여 총 아홉 가지 알고리즘을 개발했습니다. 이 프레임워크는 희소성, 예측 성능, 계산 비용 간의 균형을 체계적으로 탐색할 수 있게 합니다. 특히, LARS는 효율적인 경로 기반 해법을 제공하고, OMP는 $\ell_0$-정규화 선택을 위한 실용적인 방법으로 소개됩니다. 이 프레임워크는 등방성 및 비등방성 초탄성 재료에 적용되었으며, 모든 알고리즘-기준 조합이 높은 정확도의 구성 모델을 일관되게 발견하는 것으로 나타났습니다. 이 연구는 $\ell_1$ 기반 접근법을 넘어 다양한 발견 알고리즘의 가능성을 확장합니다.

## 🎯 주요 포인트

- 1. 데이터 기반의 구성 모델 자동 발견이 전통적인 모델 보정 패러다임의 유망한 대안으로 부상하고 있습니다.

- 2. 본 연구는 LASSO, LARS, OMP 세 가지 희소 회귀 알고리즘과 CV, AIC, BIC 세 가지 모델 선택 기준을 체계적으로 결합한 완전 자동화된 구성 모델 발견 프레임워크를 제시합니다.

- 3. 이 프레임워크는 희소성, 예측 성능, 계산 비용 간의 균형을 체계적으로 탐색할 수 있는 아홉 가지 알고리즘을 제공합니다.

- 4. 제안된 프레임워크는 등방성 및 이방성 초탄성 소재에 적용되어 매우 정확한 구성 모델을 발견하는 데 성공했습니다.

- 5. 연구 결과는 LASSO와 같은 $\ell_1$ 기반 접근법을 넘어 다양한 발견 알고리즘의 가능성을 확장합니다.

---

*Generated on 2025-09-22 15:30:49*