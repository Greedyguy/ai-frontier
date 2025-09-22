# Q-ROAR: Outlier-Aware Rescaling for RoPE Position Interpolation in Quantized Long-Context LLMs

**Korean Title:** Q-ROAR: 양자화된 장문맥 대형 언어 모델에서 RoPE 위치 보간을 위한 이상치 인식 재스케일링

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Ye Qiao|Ye Qiao]] [[authors/Sitao Huang|Sitao Huang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Outlier Aware Rescaling

## 🔗 유사한 논문
- [[Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (80.4% similar)
- [[PA-MPPI_ Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments_20250919|PA-MPPI Perception-Aware Model Predictive Path Integral Control for Quadrotor Navigation in Unknown Environments]] (80.1% similar)
- [[Position Bias Mitigates Position Bias_Mitigate Position Bias Through Inter-Position Knowledge Distillation_20250918|Position Bias Mitigates Position BiasMitigate Position Bias Through Inter-Position Knowledge Distillation]] (79.6% similar)
- [[An Empirical Study of Position Bias in Modern Information Retrieval_20250919|An Empirical Study of Position Bias in Modern Information Retrieval]] (78.7% similar)
- [[RoboEye_ Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching_20250918|RoboEye Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching]] (78.7% similar)

## 📋 저자 정보

**Authors:** Ye Qiao, Sitao Huang

## 📄 Abstract (원문)

Extending LLM context windows is crucial for long range tasks. RoPE-based
position interpolation (PI) methods like linear and frequency-aware scaling
extend input lengths without retraining, while post-training quantization (PTQ)
enables practical deployment. We show that combining PI with PTQ degrades
accuracy due to coupled effects long context aliasing, dynamic range dilation,
axis grid anisotropy, and outlier shifting that induce position-dependent logit
noise. We provide the first systematic analysis of PI plus PTQ and introduce
two diagnostics: Interpolation Pressure (per-band phase scaling sensitivity)
and Tail Inflation Ratios (outlier shift from short to long contexts). To
address this, we propose Q-ROAR, a RoPE-aware, weight-only stabilization that
groups RoPE dimensions into a few frequency bands and performs a small search
over per-band scales for W_Q,W_K, with an optional symmetric variant to
preserve logit scale. The diagnostics guided search uses a tiny long-context
dev set and requires no fine-tuning, kernel, or architecture changes.
Empirically, Q-ROAR recovers up to 0.7% accuracy on standard tasks and reduces
GovReport perplexity by more than 10%, while preserving short-context
performance and compatibility with existing inference stacks.

## 🔍 Abstract (한글 번역)

LLM의 컨텍스트 윈도우를 확장하는 것은 장거리 작업에 매우 중요합니다. RoPE 기반의 위치 보간(PI) 방법, 예를 들어 선형 및 주파수 인식 스케일링은 재훈련 없이 입력 길이를 확장하며, 훈련 후 양자화(PTQ)는 실질적인 배포를 가능하게 합니다. 우리는 PI와 PTQ를 결합하면 긴 컨텍스트 앨리어싱, 동적 범위 확장, 축 격자 이방성, 이상치 이동으로 인한 위치 의존적 로짓 노이즈로 인해 정확도가 저하된다는 것을 보여줍니다. 우리는 PI와 PTQ의 첫 번째 체계적인 분석을 제공하며 두 가지 진단 방법을 도입합니다: 보간 압력(밴드별 위상 스케일링 민감도)과 꼬리 팽창 비율(짧은 컨텍스트에서 긴 컨텍스트로의 이상치 이동). 이를 해결하기 위해, 우리는 Q-ROAR을 제안합니다. 이는 RoPE 인식, 가중치 전용 안정화 방법으로, RoPE 차원을 몇 개의 주파수 밴드로 그룹화하고 W_Q, W_K에 대해 밴드별 스케일에 대한 작은 검색을 수행하며, 로짓 스케일을 보존하기 위한 대칭 변형을 선택적으로 제공합니다. 진단에 기반한 검색은 작은 긴 컨텍스트 개발 세트를 사용하며, 미세 조정, 커널 또는 아키텍처 변경이 필요하지 않습니다. 실증적으로, Q-ROAR은 표준 작업에서 최대 0.7%의 정확도를 회복하고 GovReport의 당혹도를 10% 이상 감소시키며, 짧은 컨텍스트 성능과 기존 추론 스택과의 호환성을 유지합니다.

## 📝 요약

이 논문은 RoPE 기반의 위치 보간(PI) 방법과 사후 양자화(PTQ)를 결합할 때 발생하는 정확도 저하 문제를 다룹니다. PI와 PTQ의 결합이 긴 문맥에서 위치 의존적 노이즈를 유발하는 원인을 체계적으로 분석하고, 이를 해결하기 위해 Q-ROAR라는 방법을 제안합니다. Q-ROAR는 RoPE 차원을 주파수 대역으로 그룹화하고, 각 대역에 대해 작은 검색을 수행하여 정확도를 회복합니다. 이 방법은 추가적인 미세 조정이나 아키텍처 변경 없이도 기존 추론 시스템과 호환되며, GovReport에서의 혼란도를 10% 이상 감소시키고, 표준 작업에서 최대 0.7%의 정확도를 회복합니다.

## 🎯 주요 포인트

- 1. RoPE 기반의 위치 보간(PI) 방법과 사후 양자화(PTQ)를 결합하면 긴 문맥에서 정확도가 저하될 수 있다.

- 2. PI와 PTQ의 결합으로 인한 문제를 해결하기 위해 Q-ROAR라는 RoPE 인식, 가중치 안정화 방법을 제안한다.

- 3. Q-ROAR는 RoPE 차원을 몇 개의 주파수 대역으로 그룹화하고, 대역별 스케일에 대한 작은 검색을 수행하여 정확도를 회복한다.

- 4. 제안된 방법은 미세 조정이나 커널, 아키텍처 변경 없이 긴 문맥 개발 세트를 사용하여 검색을 수행한다.

- 5. Q-ROAR는 표준 작업에서 최대 0.7%의 정확도를 회복하고, GovReport의 당혹도를 10% 이상 감소시킨다.

---

*Generated on 2025-09-20 07:36:45*