# A Compositional Kernel Model for Feature Learning

**Korean Title:** 특징 학습을 위한 합성 커널 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Feng Ruan|Feng Ruan]] [[authors/Keli Liu|Keli Liu]] [[authors/Michael Jordan|Michael Jordan]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Coordinate-wise Reweighting

## 🔗 유사한 논문
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (78.5% similar)
- [[Value-Guided KV Compression for LLMs via Approximated CUR Decomposition_20250919|Value-Guided KV Compression for LLMs via Approximated CUR Decomposition]] (77.6% similar)
- [[Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (76.5% similar)
- [[Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (76.4% similar)
- [[Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning_20250918|Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning]] (76.2% similar)

## 📋 저자 정보

**Authors:** Feng Ruan, Keli Liu, Michael Jordan

## 📄 Abstract (원문)

We study a compositional variant of kernel ridge regression in which the
predictor is applied to a coordinate-wise reweighting of the inputs. Formulated
as a variational problem, this model provides a simple testbed for feature
learning in compositional architectures. From the perspective of variable
selection, we show how relevant variables are recovered while noise variables
are eliminated. We establish guarantees showing that both global minimizers and
stationary points discard noise coordinates when the noise variables are
Gaussian distributed. A central finding is that $\ell_1$-type kernels, such as
the Laplace kernel, succeed in recovering features contributing to nonlinear
effects at stationary points, whereas Gaussian kernels recover only linear
ones.

## 🔍 Abstract (한글 번역)

우리는 입력의 좌표별 재가중치에 예측기를 적용하는 커널 릿지 회귀의 구성 변형을 연구합니다. 변분 문제로서 공식화된 이 모델은 구성 아키텍처에서 특징 학습을 위한 간단한 테스트베드를 제공합니다. 변수 선택의 관점에서, 우리는 관련 변수가 어떻게 회복되고 잡음 변수는 제거되는지를 보여줍니다. 우리는 잡음 변수가 가우시안 분포를 따를 때, 전역 최소화 지점과 정류점 모두가 잡음 좌표를 버린다는 보장을 확립합니다. 중심적인 발견은 라플라스 커널과 같은 $\ell_1$ 유형의 커널이 정류점에서 비선형 효과에 기여하는 특징을 회복하는 데 성공하는 반면, 가우시안 커널은 오직 선형적인 것만 회복한다는 것입니다.

## 📝 요약

이 연구는 입력의 좌표별 재가중치를 적용한 합성 커널 릿지 회귀를 다룹니다. 이 모델은 합성 구조에서의 특징 학습을 위한 간단한 테스트베드로 활용됩니다. 변수 선택 관점에서, 관련 변수를 회복하고 잡음 변수를 제거하는 방법을 제시합니다. 특히, 잡음 변수가 가우시안 분포를 따를 때, 전역 최소점과 정지점이 잡음 좌표를 제거한다는 보장을 제공합니다. 주요 발견은 $\ell_1$ 유형의 커널(예: 라플라스 커널)이 정지점에서 비선형 효과에 기여하는 특징을 회복하는 반면, 가우시안 커널은 선형 효과만 회복한다는 점입니다.

## 🎯 주요 포인트

- 1. 입력의 좌표별 가중치를 적용한 예측기를 사용하는 합성 커널 릿지 회귀 변형을 연구합니다.

- 2. 이 모델은 합성 아키텍처에서 특징 학습을 위한 간단한 테스트베드를 제공합니다.

- 3. 변수 선택 관점에서 관련 변수를 회복하고 잡음 변수를 제거하는 방법을 보여줍니다.

- 4. 잡음 변수가 가우시안 분포를 따를 때, 전역 최소화 및 정류점이 잡음 좌표를 버린다는 보장을 확립합니다.

- 5. $\ell_1$ 유형의 커널, 예를 들어 라플라스 커널은 정류점에서 비선형 효과에 기여하는 특징을 회복하는 반면, 가우시안 커널은 선형 효과만 회복합니다.

---

*Generated on 2025-09-20 07:46:43*