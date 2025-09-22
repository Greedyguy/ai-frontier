# Beyond Correlation: Causal Multi-View Unsupervised Feature Selection Learning

**Korean Title:** 상관을 넘어: 인과적 다중 뷰 비지도 특징 선택 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Zongxin Shen|Zongxin Shen]] [[authors/Yanyong Huang|Yanyong Huang]] [[authors/Bin Wang|Bin Wang]] [[authors/Jinyuan Chang|Jinyuan Chang]] [[authors/Shiyu Liu|Shiyu Liu]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Causal Multi-view Feature Selection

## 🔗 유사한 논문
- [[Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (79.2% similar)
- [[CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre Scalable and Effective Data Pre-processing for Causal Fairness]] (78.1% similar)
- [[Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (77.6% similar)
- [[Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles Acquiring and Accumulating Knowledge from Diverse Datasets]] (77.4% similar)
- [[Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (77.3% similar)

## 📋 저자 정보

**Authors:** Zongxin Shen, Yanyong Huang, Bin Wang, Jinyuan Chang, Shiyu Liu, Tianrui Li

## 📄 Abstract (원문)

Multi-view unsupervised feature selection (MUFS) has recently received
increasing attention for its promising ability in dimensionality reduction on
multi-view unlabeled data. Existing MUFS methods typically select
discriminative features by capturing correlations between features and
clustering labels. However, an important yet underexplored question remains:
\textit{Are such correlations sufficiently reliable to guide feature
selection?} In this paper, we analyze MUFS from a causal perspective by
introducing a novel structural causal model, which reveals that existing
methods may select irrelevant features because they overlook spurious
correlations caused by confounders. Building on this causal perspective, we
propose a novel MUFS method called CAusal multi-view Unsupervised feature
Selection leArning (CAUSA). Specifically, we first employ a generalized
unsupervised spectral regression model that identifies informative features by
capturing dependencies between features and consensus clustering labels. We
then introduce a causal regularization module that can adaptively separate
confounders from multi-view data and simultaneously learn view-shared sample
weights to balance confounder distributions, thereby mitigating spurious
correlations. Thereafter, integrating both into a unified learning framework
enables CAUSA to select causally informative features. Comprehensive
experiments demonstrate that CAUSA outperforms several state-of-the-art
methods. To our knowledge, this is the first in-depth study of causal
multi-view feature selection in the unsupervised setting.

## 🔍 Abstract (한글 번역)

다중 뷰 비지도 특징 선택(MUFS)은 다중 뷰 비라벨 데이터의 차원 축소에서 유망한 능력으로 인해 최근 많은 주목을 받고 있습니다. 기존의 MUFS 방법들은 일반적으로 특징과 클러스터링 라벨 간의 상관관계를 포착하여 변별력 있는 특징을 선택합니다. 그러나 중요한 질문이 여전히 남아 있습니다: \textit{이러한 상관관계가 특징 선택을 안내하기에 충분히 신뢰할 수 있는가?} 본 논문에서는 새로운 구조적 인과 모델을 도입하여 인과적 관점에서 MUFS를 분석합니다. 이를 통해 기존 방법들이 혼재 변수에 의해 발생하는 허위 상관관계를 간과하여 관련 없는 특징을 선택할 수 있음을 밝힙니다. 이러한 인과적 관점에 기반하여, 우리는 CAusal multi-view Unsupervised feature Selection leArning (CAUSA)라는 새로운 MUFS 방법을 제안합니다. 구체적으로, 우리는 먼저 일반화된 비지도 스펙트럼 회귀 모델을 사용하여 특징과 합의 클러스터링 라벨 간의 의존성을 포착함으로써 정보성 있는 특징을 식별합니다. 그런 다음, 인과 정규화 모듈을 도입하여 다중 뷰 데이터에서 혼재 변수를 적응적으로 분리하고 동시에 뷰 공유 샘플 가중치를 학습하여 혼재 변수 분포를 균형 있게 조정함으로써 허위 상관관계를 완화합니다. 이후, 이를 통합된 학습 프레임워크에 결합함으로써 CAUSA가 인과적으로 정보성 있는 특징을 선택할 수 있게 합니다. 종합적인 실험 결과, CAUSA가 여러 최첨단 방법들을 능가함을 보여줍니다. 우리가 아는 한, 이는 비지도 설정에서 인과 다중 뷰 특징 선택에 대한 최초의 심층 연구입니다.

## 📝 요약

다중 뷰 비지도 특징 선택(MUFS)은 다중 뷰 비라벨 데이터의 차원 축소에 유망한 능력을 보여주며 주목받고 있습니다. 그러나 기존 방법들은 특징과 클러스터 라벨 간의 상관관계를 포착하여 특징을 선택하는데, 이러한 상관관계가 특징 선택에 충분히 신뢰할 수 있는지에 대한 의문이 남아 있습니다. 본 논문에서는 인과적 관점에서 새로운 구조적 인과 모델을 도입하여 기존 방법들이 혼재 변수로 인한 허위 상관관계를 간과하여 관련 없는 특징을 선택할 수 있음을 밝힙니다. 이를 바탕으로, CAusal multi-view Unsupervised feature Selection leArning (CAUSA)라는 새로운 MUFS 방법을 제안합니다. CAUSA는 일반화된 비지도 스펙트럼 회귀 모델을 사용하여 유익한 특징을 식별하고, 인과 정규화 모듈을 통해 혼재 변수를 분리하여 허위 상관관계를 완화합니다. 실험 결과, CAUSA는 최신 방법들보다 우수한 성능을 보이며, 비지도 설정에서 인과적 다중 뷰 특징 선택에 대한 최초의 심층 연구입니다.

## 🎯 주요 포인트

- 1. 다중 뷰 비지도 특징 선택(MUFS)은 다중 뷰 비라벨 데이터의 차원 축소에 유망한 능력을 보여주며 주목받고 있다.

- 2. 기존 MUFS 방법들은 특징과 클러스터링 라벨 간의 상관관계를 포착하여 변별력 있는 특징을 선택한다.

- 3. 본 논문은 인과적 관점에서 MUFS를 분석하여, 기존 방법들이 혼동 변수로 인한 허위 상관관계를 간과하여 관련 없는 특징을 선택할 수 있음을 밝힌다.

- 4. 제안된 CAUSA 방법은 인과적 정규화 모듈을 도입하여 혼동 변수를 분리하고, 뷰 공유 샘플 가중치를 학습하여 허위 상관관계를 완화한다.

- 5. 실험 결과, CAUSA는 여러 최신 방법들보다 우수한 성능을 보이며, 비지도 환경에서 인과적 다중 뷰 특징 선택에 대한 첫 심층 연구이다.

---

*Generated on 2025-09-20 09:34:58*