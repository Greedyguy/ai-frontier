# MoCA: Multi-modal Cross-masked Autoencoder for Digital Health Measurements

**Korean Title:** MoCA: 디지털 건강 측정을 위한 다중 모달 교차 마스크 오토인코더

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Correlation-aware Masking|Correlation-aware Masking]] [[keywords/specific/Masked Autoencoder|Masked Autoencoder]] [[keywords/broad/Transformer|Transformer]] [[keywords/broad/Self-supervised Learning|Self-supervised Learning]] [[keywords/unique/Multi-modal Cross-masked Autoencoder|Multi-modal Cross-masked Autoencoder]] [[categories/cs.LG|cs.LG]] [[2025-09-18/CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (82.8% similar) [[2025-09-22/MTS-DMAE_ Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning_20250922|MTS-DMAE: Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning]] (82.7% similar) [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Correlation-aware Masking Strategy
**🔗 Specific Connectable**: Masked Autoencoder
**🔬 Broad Technical**: Transformer, Self-supervised Learning
**⭐ Unique Technical**: Multi-modal Cross-masked Autoencoder
## 🔗 유사한 논문
- [[2025-09-18/CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (82.8% similar)
- [[2025-09-22/MTS-DMAE_ Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning_20250922|MTS-DMAE Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning]] (82.7% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (82.3% similar)
- [[2025-09-17/MOCHA_ Multi-modal Objects-aware Cross-arcHitecture Alignment_20250917|MOCHA Multi-modal Objects-aware Cross-arcHitecture Alignment]] (81.7% similar)
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (81.7% similar)


**ArXiv ID**: [2506.02260](https://arxiv.org/abs/2506.02260)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2506.02260.pdf)


**ArXiv ID**: [2506.02260](https://arxiv.org/abs/2506.02260)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2506.02260.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Correlation-aware Masking Strategy
**🔗 Specific Connectable**: Masked Autoencoder
**⭐ Unique Technical**: Multi-modal Cross-masked Autoencoder
**🔬 Broad Technical**: Transformer, Self-supervised Learning

## 🏷️ 추출된 키워드



`Transformer` • 

`Self-supervised Learning` • 

`Masked Autoencoder` • 

`Kernelized Canonical Correlation Analysis` • 

`Multi-modal Cross-masked Autoencoder`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02260v3 Announce Type: replace-cross 
Abstract: Wearable devices enable continuous multi-modal physiological and behavioral monitoring, yet analysis of these data streams faces fundamental challenges including the lack of gold-standard labels and incomplete sensor data. While self-supervised learning approaches have shown promise for addressing these issues, existing multi-modal extensions present opportunities to better leverage the rich temporal and cross-modal correlations inherent in simultaneously recorded wearable sensor data. We propose the Multi-modal Cross-masked Autoencoder (MoCA), a self-supervised learning framework that combines transformer architecture with masked autoencoder (MAE) methodology, using a principled cross-modality masking scheme that explicitly leverages correlation structures between sensor modalities. MoCA demonstrates strong performance boosts across reconstruction and downstream classification tasks on diverse benchmark datasets. We further establish theoretical guarantees by establishing a fundamental connection between multi-modal MAE loss and kernelized canonical correlation analysis through a Reproducing Kernel Hilbert Space framework, providing principled guidance for correlation-aware masking strategy design. Our approach offers a novel solution for leveraging unlabeled multi-modal wearable data while handling missing modalities, with broad applications across digital health domains.

## 🔍 Abstract (한글 번역)

arXiv:2506.02260v3 발표 유형: 교차 대체  
초록: 웨어러블 기기는 지속적인 다중 모드 생리 및 행동 모니터링을 가능하게 하지만, 이러한 데이터 스트림의 분석은 표준 레이블의 부족과 불완전한 센서 데이터와 같은 근본적인 문제에 직면해 있습니다. 자기 지도 학습 접근법이 이러한 문제를 해결하는 데 유망한 결과를 보여주었지만, 기존의 다중 모드 확장은 동시에 기록된 웨어러블 센서 데이터에 내재된 풍부한 시간적 및 교차 모드 상관관계를 보다 잘 활용할 수 있는 기회를 제공합니다. 우리는 트랜스포머 아키텍처와 마스크드 오토인코더(MAE) 방법론을 결합한 자기 지도 학습 프레임워크인 다중 모드 교차 마스크드 오토인코더(MoCA)를 제안합니다. 이는 센서 모드 간의 상관 구조를 명시적으로 활용하는 원칙적인 교차 모드 마스킹 방식을 사용합니다. MoCA는 다양한 벤치마크 데이터셋에서 재구성과 다운스트림 분류 작업 전반에 걸쳐 강력한 성능 향상을 보여줍니다. 우리는 또한 재생 커널 힐베르트 공간 프레임워크를 통해 다중 모드 MAE 손실과 커널화된 정준 상관 분석 간의 근본적인 연결을 확립함으로써 이론적 보장을 확립하고, 상관 인식 마스킹 전략 설계를 위한 원칙적인 지침을 제공합니다. 우리의 접근법은 누락된 모드를 처리하면서 레이블이 없는 다중 모드 웨어러블 데이터를 활용하기 위한 새로운 솔루션을 제공하며, 디지털 건강 분야 전반에 걸쳐 광범위한 응용 가능성을 갖추고 있습니다.

## 📝 요약

이 논문은 웨어러블 기기를 통한 다중 모드 생리 및 행동 모니터링의 데이터 분석 문제를 해결하기 위해 제안된 Multi-modal Cross-masked Autoencoder (MoCA)라는 자기 지도 학습 프레임워크를 소개합니다. MoCA는 트랜스포머 아키텍처와 마스크드 오토인코더(MAE) 방법론을 결합하여 센서 모달리티 간의 상관 구조를 활용하는 교차 모달리티 마스킹 기법을 사용합니다. 이를 통해 다양한 벤치마크 데이터셋에서 데이터 복원 및 분류 작업의 성능을 크게 향상시켰습니다. 또한, MoCA는 다중 모달 MAE 손실과 커널화된 정준 상관 분석 간의 이론적 연결을 확립하여 상관 인식 마스킹 전략 설계에 대한 이론적 근거를 제공합니다. 이 접근법은 디지털 헬스 분야에서 라벨이 없는 다중 모드 웨어러블 데이터를 활용하고 누락된 모달리티를 처리하는 데 유용한 솔루션을 제시합니다.

## 🎯 주요 포인트


- 1. 웨어러블 기기의 다중 모드 데이터 스트림 분석에서 금표준 레이블 부족과 센서 데이터 불완전성 문제를 해결하기 위해 자기 지도 학습 접근법이 유망하다.

- 2. 제안된 MoCA(Multi-modal Cross-masked Autoencoder)는 트랜스포머 아키텍처와 마스크드 오토인코더 방법론을 결합하여 센서 모달리티 간의 상관 구조를 활용한다.

- 3. MoCA는 다양한 벤치마크 데이터셋에서 재구성과 다운스트림 분류 작업에서 성능 향상을 보여준다.

- 4. MoCA의 이론적 보장은 다중 모드 MAE 손실과 커널화된 정준 상관 분석 사이의 근본적인 연결을 통해 제공된다.

- 5. 이 접근법은 디지털 헬스 분야에서 라벨이 없는 다중 모드 웨어러블 데이터를 활용하고 누락된 모달리티를 처리하는 새로운 솔루션을 제시한다.


---

*Generated on 2025-09-22 16:11:58*