# Shedding Light on Dark Matter at the LHC with Machine Learning

**Korean Title:** LHC에서 기계 학습을 활용한 암흑 물질 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Ernesto Arganda|Ernesto Arganda]] [[authors/Martín de los Rios|Martín de los Rios]] [[authors/Andres D. Perez|Andres D. Perez]] [[authors/Subhojit Roy|Subhojit Roy]] [[authors/Rosa M. Sandá Seoane|Rosa M. Sandá Seoane]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Radiative Decay Modes

## 🔗 유사한 논문
- [[DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (76.7% similar)
- [[Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter_20250919|Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter]] (76.3% similar)
- [[Leveraging Reinforcement Learning, Genetic Algorithms and Transformers for background determination in particle physics_20250919|Leveraging Reinforcement Learning, Genetic Algorithms and Transformers for background determination in particle physics]] (75.7% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (73.6% similar)
- [[AD-DINOv3_ Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration_20250918|AD-DINOv3 Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (73.5% similar)

## 📋 저자 정보

**Authors:** Ernesto Arganda, Martín de los Rios, Andres D. Perez, Subhojit Roy, Rosa M. Sandá Seoane, Carlos E. M. Wagner

## 📄 Abstract (원문)

We investigate a WIMP dark matter (DM) candidate in the form of a
singlino-dominated lightest supersymmetric particle (LSP) within the
$Z_3$-symmetric Next-to-Minimal Supersymmetric Standard Model. This framework
gives rise to regions of parameter space where DM is obtained via
co-annihilation with nearby higgsino-like electroweakinos and DM direct
detection~signals are suppressed, the so-called ``blind spots". On the other
hand, collider signatures remain promising due to enhanced radiative decay
modes of higgsinos into the singlino-dominated LSP and a photon, rather than
into leptons or hadrons. This motivates searches for radiatively decaying
neutralinos, however, these signals face substantial background challenges, as
the decay products are typically soft due to the small mass-splits ($\Delta m$)
between the LSP and the higgsino-like coannihilation partners. We apply a
data-driven Machine Learning (ML) analysis that improves sensitivity to these
subtle signals, offering a powerful complement to traditional search strategies
to discover a new physics scenario. Using an LHC integrated luminosity of
$100~\mathrm{fb}^{-1}$ at $14~\mathrm{TeV}$, the method achieves a $5\sigma$
discovery reach for higgsino masses up to $225~\mathrm{GeV}$ with $\Delta
m\!\lesssim\!12~\mathrm{GeV}$, and a $2\sigma$ exclusion up to
$285~\mathrm{GeV}$ with $\Delta m\!\lesssim\!20~\mathrm{GeV}$. These results
highlight the power of collider searches to probe DM candidates that remain
hidden from current direct detection experiments, and provide a motivation for
a search by the LHC collaborations using ML methods.

## 🔍 Abstract (한글 번역)

우리는 $Z_3$ 대칭을 갖는 Next-to-Minimal Supersymmetric Standard Model 내에서 싱글리노가 지배적인 가장 가벼운 초대칭 입자(LSP) 형태의 WIMP 암흑 물질(DM) 후보를 조사합니다. 이 프레임워크는 DM이 힉시노와 유사한 전기약입자들과의 공동 소멸을 통해 얻어지고, DM 직접 탐지 신호가 억제되는, 이른바 "블라인드 스팟"이라 불리는 매개변수 공간 영역을 제공합니다. 반면에, 힉시노가 싱글리노가 지배적인 LSP와 광자로 붕괴되는 방사성 붕괴 모드가 강화되어, 충돌기 서명은 여전히 유망합니다. 이는 방사성으로 붕괴되는 중성입자에 대한 탐색을 자극하지만, 이러한 신호는 LSP와 힉시노와 유사한 공동 소멸 파트너 간의 작은 질량 차이($\Delta m$)로 인해 붕괴 산물이 일반적으로 부드럽기 때문에 상당한 배경 문제에 직면합니다. 우리는 이러한 미묘한 신호에 대한 민감성을 향상시키는 데이터 기반 머신 러닝(ML) 분석을 적용하여 새로운 물리 시나리오를 발견하기 위한 전통적인 탐색 전략에 강력한 보완을 제공합니다. $14~\mathrm{TeV}$에서 $100~\mathrm{fb}^{-1}$의 LHC 적분 광도를 사용하여, 이 방법은 $\Delta m\!\lesssim\!12~\mathrm{GeV}$일 때 힉시노 질량이 최대 $225~\mathrm{GeV}$까지 $5\sigma$ 발견 범위를 달성하고, $\Delta m\!\lesssim\!20~\mathrm{GeV}$일 때 최대 $285~\mathrm{GeV}$까지 $2\sigma$ 배제를 달성합니다. 이러한 결과는 현재의 직접 탐지 실험에서 숨겨진 DM 후보를 조사하는 충돌기 탐색의 강력함을 강조하며, LHC 협력단이 ML 방법을 사용하여 탐색을 수행할 동기를 제공합니다.

## 📝 요약

이 논문은 $Z_3$ 대칭을 가진 차세대 최소 초대칭 표준 모형(NMSSM)에서 싱글리노가 주를 이루는 가장 가벼운 초대칭 입자(LSP)로 구성된 WIMP 암흑 물질 후보를 연구합니다. 이 모델은 힉시노와의 공소멸을 통해 암흑 물질을 형성하며, 직접 검출 신호가 억제되는 "블라인드 스팟"을 제공합니다. 그러나 힉시노의 방사성 붕괴 모드가 싱글리노와 광자로 전환되면서 충돌기에서의 신호는 여전히 유망합니다. 이러한 신호는 배경 잡음이 많지만, 데이터 기반 기계 학습(ML) 분석을 통해 민감도를 향상시켜 새로운 물리 시나리오를 발견할 수 있습니다. LHC에서 100 fb⁻¹의 적분 광도를 사용하여 힉시노 질량이 최대 225 GeV까지 5σ 발견 가능성을, 285 GeV까지 2σ 배제 가능성을 제시합니다. 이는 현재의 직접 검출 실험에서 숨겨진 암흑 물질 후보를 탐색하는 데 있어 충돌기 검색의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. $Z_3$-대칭적인 차세대 최소 초대칭 표준 모형(NMSSM)에서 싱글리노가 지배적인 가장 가벼운 초대칭 입자(LSP) 형태의 WIMP 암흑 물질 후보를 연구합니다.

- 2. 암흑 물질은 힉시노와의 공동 소멸을 통해 얻어지며, 직접 탐지 신호는 "블라인드 스팟"에서 억제됩니다.

- 3. 힉시노의 방사성 붕괴 모드가 싱글리노 지배 LSP와 광자로 강화되어, 충돌기 서명이 유망합니다.

- 4. 데이터 기반 기계 학습 분석을 통해 미세한 신호에 대한 민감도를 개선하여 새로운 물리 시나리오를 발견할 수 있습니다.

- 5. LHC에서 14TeV의 에너지와 100fb⁻¹의 적분 광도를 사용하여 힉시노 질량 최대 225GeV까지 5시그마 발견 가능성을 달성합니다.

---

*Generated on 2025-09-20 00:59:08*