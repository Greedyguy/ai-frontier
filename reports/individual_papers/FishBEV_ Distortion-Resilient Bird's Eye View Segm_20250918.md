
# FishBEV: Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras

**Korean Title:** FishBEV: Surround-View Fisheye 카메라를 사용한 왜곡 내성 Bird's Eye View Segmentation.

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Surround-View Fisheye BEV Segmentation|Surround-View Fisheye BEV Segmentation]] [[keywords/broad/Bird's Eye View Segmentation|Bird's Eye View Segmentation]] [[keywords/broad/Fisheye Cameras|Fisheye Cameras]] [[keywords/specific/Distortion-Resilient Multi-scale Extraction (DRME|Distortion-Resilient Multi-scale Extraction (DRME]] [[keywords/unique/FishBEV|FishBEV]] [[categories/cs.CV|cs.CV]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Distortion-Resilient Multi-scale Extraction (DRME
**🔬 Broad Technical**: Bird's Eye View Segmentation, Fisheye Cameras
**🔗 Specific Connectable**: Uncertainty-aware Spatial Cross-Attention (U-SCA
**⭐ Unique Technical**: FishBEV

**ArXiv ID**: [2509.13681](https://arxiv.org/abs/2509.13681)
**Published**: 2025-09-18
**Category**: cs.CV
**PDF**: [Download](https://arxiv.org/pdf/2509.13681.pdf)


## 🏷️ 추출된 키워드



`Bird's Eye View Segmentation` • 

`Fisheye Cameras` • 

`Cross-View Alignment` • 

`FishBEV` • 

`Temporal Self-Attention`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13681v1 Announce Type: new 
Abstract: As a cornerstone technique for autonomous driving, Bird's Eye View (BEV) segmentation has recently achieved remarkable progress with pinhole cameras. However, it is non-trivial to extend the existing methods to fisheye cameras with severe geometric distortion, ambiguous multi-view correspondences and unstable temporal dynamics, all of which significantly degrade BEV performance. To address these challenges, we propose FishBEV, a novel BEV segmentation framework specifically tailored for fisheye cameras. This framework introduces three complementary innovations, including a Distortion-Resilient Multi-scale Extraction (DRME) backbone that learns robust features under distortion while preserving scale consistency, an Uncertainty-aware Spatial Cross-Attention (U-SCA) mechanism that leverages uncertainty estimation for reliable cross-view alignment, a Distance-aware Temporal Self-Attention (D-TSA) module that adaptively balances near field details and far field context to ensure temporal coherence. Extensive experiments on the Synwoodscapes dataset demonstrate that FishBEV consistently outperforms SOTA baselines, regarding the performance evaluation of FishBEV on the surround-view fisheye BEV segmentation tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.13681v1 발표 유형: 새로운
요약: 자율 주행을 위한 중요한 기술로서, 새빛(새빛) 분할은 최근 핀홀 카메라로 놀라운 진전을 이루었습니다. 그러나 기하학적 왜곡이 심한 피쉬아이 카메라에 기존 방법을 확장하는 것은 쉽지 않으며, 모호한 다중 뷰 대응 및 불안정한 시간적 역학이 모두 새빛 성능을 크게 저하시킵니다. 이러한 도전에 대처하기 위해 우리는 피쉬BEV라는 새로운 피쉬아이 카메라에 특별히 맞춘 BEV 분할 프레임워크를 제안합니다. 이 프레임워크는 왜곡에 강한 다중 스케일 추출(DRME) 백본을 소개하여 크기 일관성을 유지하면서 왜곡 아래에서 견고한 특징을 학습하고, 불확실성 인식 공간 교차 어텐션(U-SCA) 메커니즘을 활용하여 신뢰할 수 있는 교차 뷰 정렬을 위한 불확실성 추정을 수행하며, 거리 인식 시간 자기 어텐션(D-TSA) 모듈을 도입하여 시간적 일관성을 보장하기 위해 근거리 세부 정보와 원거리 컨텍스트를 적응적으로 균형을 맞춥니다. Synwoodscapes 데이터셋에서의 광범위한 실험 결과는 FishBEV가 주변 시야 피쉬아이 BEV 분할 작업의 성능 평가에서 SOTA 베이스라인을 일관되게 능가한다는 것을 보여줍니다.

## 📝 요약

자율 주행을 위한 중요한 기술 중 하나인 Bird's Eye View (BEV) segmentation은 핀홀 카메라를 사용해 놀라운 발전을 이루어왔다. 그러나 심한 기하학적 왜곡을 가진 피쉬아이 카메라에 대한 기존 방법론을 확장하는 것은 어렵다. 이에 우리는 피쉬아이 카메라에 특화된 새로운 BEV segmentation 프레임워크인 FishBEV를 제안한다. 이 프레임워크는 왜곡에 강한 특징을 학습하는 DRME 백본, 신뢰할 수 있는 교차 뷰 정렬을 위한 U-SCA 메커니즘, 시간적 일관성을 보장하는 D-TSA 모듈을 도입한다. Synwoodscapes 데이터셋에서의 실험 결과는 FishBEV가 주변 환경을 잘 파악하는 데 뛰어나다는 것을 보여준다.

## 🎯 주요 포인트


- 1. 자율 주행을 위한 중요한 기술인 Bird's Eye View (BEV) segmentation이 pinhole 카메라로 높은 성과를 보였지만, FishBEV는 획기적인 발전을 이룸.

- 2. FishBEV는 왜곡에 강한 DRME 백본, 불확실성을 고려한 U-SCA 메커니즘, 시간적 일관성을 보장하는 D-TSA 모듈을 도입하여 성능을 향상시킴.

- 3. Synwoodscapes 데이터셋에서의 실험 결과에서 FishBEV가 SOTA 기준을 능가하는 것을 입증함.


---

*Generated on 2025-09-18 16:59:36*