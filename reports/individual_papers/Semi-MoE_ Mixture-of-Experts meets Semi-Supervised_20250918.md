
# Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation

**Korean Title:** Semi-MoE: 전문가 혼합 모델이 반지도 학습을 만나는 Semi-Supervised 조직병리학 분할

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-Gating Pseudo-labeling|Multi-Gating Pseudo-labeling]] [[keywords/broad/Semi-supervised learning|Semi-supervised learning]] [[keywords/broad/Histopathology image segmentation|Histopathology image segmentation]] [[keywords/specific/Multi-task learning|Multi-task learning]] [[keywords/unique/Semi-MoE|Semi-MoE]] [[categories/cs.CV|cs.CV]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-Gating Pseudo-labeling
**🔬 Broad Technical**: Semi-supervised learning, Histopathology image segmentation
**🔗 Specific Connectable**: Multi-task learning
**⭐ Unique Technical**: Semi-MoE

**ArXiv ID**: [2509.13834](https://arxiv.org/abs/2509.13834)
**Published**: 2025-09-18
**Category**: cs.CV
**PDF**: [Download](https://arxiv.org/pdf/2509.13834.pdf)


## 🏷️ 추출된 키워드



`Semi-supervised learning` • 

`Histopathology image segmentation` • 

`Multi-task learning` • 

`Semi-MoE` • 

`Multi-Gating Pseudo-labeling`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13834v1 Announce Type: new 
Abstract: Semi-supervised learning has been employed to alleviate the need for extensive labeled data for histopathology image segmentation, but existing methods struggle with noisy pseudo-labels due to ambiguous gland boundaries and morphological misclassification. This paper introduces Semi-MOE, to the best of our knowledge, the first multi-task Mixture-of-Experts framework for semi-supervised histopathology image segmentation. Our approach leverages three specialized expert networks: A main segmentation expert, a signed distance field regression expert, and a boundary prediction expert, each dedicated to capturing distinct morphological features. Subsequently, the Multi-Gating Pseudo-labeling module dynamically aggregates expert features, enabling a robust fuse-and-refine pseudo-labeling mechanism. Furthermore, to eliminate manual tuning while dynamically balancing multiple learning objectives, we propose an Adaptive Multi-Objective Loss. Extensive experiments on GlaS and CRAG benchmarks show that our method outperforms state-of-the-art approaches in low-label settings, highlighting the potential of MoE-based architectures in advancing semi-supervised segmentation. Our code is available at https://github.com/vnlvi2k3/Semi-MoE.

## 🔍 Abstract (한글 번역)

arXiv:2509.13834v1 발표 유형: 새로운
요약: 반지도 학습은 조직병리학 이미지 분할을 위한 광범위한 레이블 데이터의 필요성을 완화하기 위해 사용되어 왔지만, 기존 방법들은 모호한 선샘과 형태학적 오분류로 인한 잡음이 있는 가짜 레이블로 고민합니다. 본 논문에서는 우리의 지식으로는 반지도 조직병리학 이미지 분할을 위한 최초의 다중 작업 전문가 모델인 Semi-MOE를 소개합니다. 저희 방법은 세 가지 전문가 네트워크를 활용합니다: 주요 분할 전문가, 부호화된 거리 필드 회귀 전문가 및 경계 예측 전문가로, 각각이 다른 형태학적 특징을 캡처하기 위해 전용됩니다. 이후 Multi-Gating Pseudo-labeling 모듈은 전문가 특징을 동적으로 집계하여 견고한 융합 및 정제 가짜 레이블 메커니즘을 가능하게 합니다. 더 나아가, 다중 학습 목표를 동적으로 균형을 맞추면서 수동 조정을 제거하기 위해 우리는 적응형 다중 목적 손실을 제안합니다. GlaS 및 CRAG 벤치마크에서의 광범위한 실험 결과는 저희 방법이 저레이블 설정에서 최첨단 접근 방식을 능가함을 보여주며, 반지도 분할을 발전시키는 MoE 기반 아키텍처의 잠재력을 강조합니다. 저희 코드는 https://github.com/vnlvi2k3/Semi-MoE에서 사용할 수 있습니다.

## 📝 요약

이 논문은 조직학 이미지 분할을 위한 반지도 학습을 개선하기 위해 Semi-MOE를 제안한다. 이는 다중 전문가(Mixture-of-Experts) 프레임워크로, 주요 분할 전문가, 부호 거리 필드 회귀 전문가, 경계 예측 전문가를 활용하여 각각 다른 형태학적 특징을 캡처한다. 또한, Multi-Gating Pseudo-labeling 모듈을 통해 전문가 특징을 동적으로 집계하여 견고한 가짜 라벨링 메커니즘을 구현한다. 또한, 다중 학습 목표를 동적으로 균형잡기 위해 적응형 다중 목적 손실을 제안한다. GlaS 및 CRAG 벤치마크에서 수행된 실험 결과, 저레이블 환경에서 최신 기술 접근법을 능가함을 보여주며, MoE 기반 아키텍처의 잠재력을 강조한다.

## 🎯 주요 포인트


- 1. 본 논문은 반지도 학습을 사용하여 조직병리 이미지 분할에 있어 노이즈가 있는 가짜 라벨을 처리하는 Semi-MOE를 소개한다.

- 2. Semi-MOE는 세 가지 전문화된 전문 네트워크를 활용하여 각각 다른 형태학적 특징을 캡처하는데 전념한다.

- 3. Multi-Gating Pseudo-labeling 모듈은 전문 특징을 동적으로 집계하여 견고한 가짜 라벨링 메커니즘을 가능하게 한다.


---

*Generated on 2025-09-18 17:02:15*