
# RF-LSCM: Pushing Radiance Fields to Multi-Domain Localized Statistical Channel Modeling for Cellular Network Optimization

**Korean Title:** RF-LSCM: 세포 네트워크 최적화를 위한 다중 도메인 지역화된 통계 채널 모델링을 위한 Radiance Fields를 확장합니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-frequency Data Fusion|Multi-frequency Data Fusion]] [[keywords/broad/Radiance Fields|Radiance Fields]] [[keywords/broad/Channel Modeling|Channel Modeling]] [[keywords/specific/Multi-domain LSCM|Multi-domain LSCM]] [[keywords/unique/RF-LSCM|RF-LSCM]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-frequency Data Fusion
**🔬 Broad Technical**: Localized Statistical Channel Modeling, Radiance Fields
**🔗 Specific Connectable**: Multi-domain LSCM
**⭐ Unique Technical**: RF-LSCM

**ArXiv ID**: [2509.13686](https://arxiv.org/abs/2509.13686)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13686.pdf)


## 🏷️ 추출된 키워드



`Radiance Fields` • 

`Channel Modeling` • 

`Multi-domain LSCM` • 

`RF-LSCM` • 

`Multi-frequency Data Fusion`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13686v1 Announce Type: new 
Abstract: Accurate localized wireless channel modeling is a cornerstone of cellular network optimization, enabling reliable prediction of network performance during parameter tuning. Localized statistical channel modeling (LSCM) is the state-of-the-art channel modeling framework tailored for cellular network optimization. However, traditional LSCM methods, which infer the channel's Angular Power Spectrum (APS) from Reference Signal Received Power (RSRP) measurements, suffer from critical limitations: they are typically confined to single-cell, single-grid and single-carrier frequency analysis and fail to capture complex cross-domain interactions. To overcome these challenges, we propose RF-LSCM, a novel framework that models the channel APS by jointly representing large-scale signal attenuation and multipath components within a radiance field. RF-LSCM introduces a multi-domain LSCM formulation with a physics-informed frequency-dependent Attenuation Model (FDAM) to facilitate the cross frequency generalization as well as a point-cloud-aided environment enhanced method to enable multi-cell and multi-grid channel modeling. Furthermore, to address the computational inefficiency of typical neural radiance fields, RF-LSCM leverages a low-rank tensor representation, complemented by a novel Hierarchical Tensor Angular Modeling (HiTAM) algorithm. This efficient design significantly reduces GPU memory requirements and training time while preserving fine-grained accuracy. Extensive experiments on real-world multi-cell datasets demonstrate that RF-LSCM significantly outperforms state-of-the-art methods, achieving up to a 30% reduction in mean absolute error (MAE) for coverage prediction and a 22% MAE improvement by effectively fusing multi-frequency data.

## 🔍 Abstract (한글 번역)

arXiv:2509.13686v1 발표 유형: 새로운
요약: 정확한 지역화 무선 채널 모델링은 셀룰러 네트워크 최적화의 중추이며, 매개 변수 조정 중 네트워크 성능을 신뢰할 수 있는 예측을 가능하게 합니다. 지역화 통계 채널 모델링(LSCM)은 셀룰러 네트워크 최적화를 위해 맞춤형으로 개발된 최신 채널 모델링 프레임워크입니다. 그러나 전통적인 LSCM 방법은 일반적으로 단일 셀, 단일 그리드 및 단일 캐리어 주파수 분석에 국한되어 있으며 복잡한 교차 도메인 상호작용을 포착하지 못하는 중요한 한계가 있습니다. 이러한 도전을 극복하기 위해 우리는 RF-LSCM을 제안합니다. 이는 채널 APS를 대규모 신호 감쇠와 다중 경로 구성 요소를 동시에 나타내는 방사도 필드 내에서 모델링하는 새로운 프레임워크입니다. RF-LSCM은 교차 주파수 일반화를 용이하게 하는 물리학적으로 정보가 담긴 주파수 종속 감쇠 모델(FDAM)을 도입하여 다중 도메인 LSCM 공식을 제시하고, 멀티셀 및 멀티그리드 채널 모델링을 가능하게 하는 포인트 클라우드 지원 환경 향상 방법을 도입합니다. 또한, 전형적인 신경 방사도 필드의 계산 효율성을 해결하기 위해 RF-LSCM은 저랭크 텐서 표현을 활용하며, 새로운 계층적 텐서 각도 모델링(HiTAM) 알고리즘을 보완합니다. 이 효율적인 설계는 GPU 메모리 요구 사항과 훈련 시간을 크게 줄이면서 세밀한 정확도를 유지합니다. 실제 멀티셀 데이터셋에서의 광범위한 실험 결과는 RF-LSCM이 최첨단 방법을 크게 능가하며, 커버리지 예측에서 평균 절대 오차(MAE)를 최대 30% 줄이고, 효과적으로 다중 주파수 데이터를 융합하여 22% MAE를 개선한다는 것을 보여줍니다.

## 📝 요약

본 연구는 셀룰러 네트워크 최적화를 위한 정확한 지역화 무선 채널 모델링을 위해 RF-LSCM이라는 새로운 프레임워크를 제안한다. RF-LSCM은 라디안스 필드 내에서 대규모 신호 감쇠와 다중경로 구성 요소를 함께 표현하여 채널 APS를 모델링한다. 또한, 효율적인 디자인을 통해 GPU 메모리 요구 사항과 훈련 시간을 크게 줄이면서 세밀한 정확도를 유지한다. 실제 다중 셀 데이터셋에서의 실험 결과는 RF-LSCM이 최대 30%의 평균 절대 오차(MAE) 감소와 다중 주파수 데이터를 효과적으로 융합하여 22%의 MAE 향상을 달성하며 최첨단 방법을 크게 능가함을 보여준다.

## 🎯 주요 포인트


- 세포 네트워크 최적화를 위한 정확한 지역화 무선 채널 모델링은 네트워크 성능 예측을 가능하게 함

- RF-LSCM은 채널 APS를 모델링하기 위한 새로운 프레임워크로, 다양한 도메인 상호 작용을 캡처할 수 있음

- RF-LSCM은 다중 주파수 데이터를 효과적으로 융합하여 최대 30%의 MAE 감소를 달성함


---

*Generated on 2025-09-18 16:38:09*