
# CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts

**Korean Title:** CSMoE: 부드러운 전문가 혼합을 갖춘 효율적인 원격 감지 기반 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Cross-Sensor Representation Learning|Cross-Sensor Representation Learning]] [[keywords/broad/Remote Sensing|Remote Sensing]] [[keywords/broad/Representation Learning|Representation Learning]] [[keywords/specific/Masked Autoencoders|Masked Autoencoders]] [[keywords/unique/Soft Mixture-of-Experts (Soft MoE|Soft Mixture-of-Experts (Soft MoE]] [[categories/cs.CV|cs.CV]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-Sensor Masked Autoencoder
**🔬 Broad Technical**: Remote Sensing, Representation Learning
**🔗 Specific Connectable**: Soft Mixture-of-Experts
**⭐ Unique Technical**: CSMoE

**ArXiv ID**: [2509.14104](https://arxiv.org/abs/2509.14104)
**Published**: 2025-09-18
**Category**: cs.CV
**PDF**: [Download](https://arxiv.org/pdf/2509.14104.pdf)


## 🏷️ 추출된 키워드



`Remote Sensing` • 

`Self-supervised Learning` • 

`Cross-Sensor Masked Autoencoder (CSMAE` • 

`Soft Mixture-of-Experts (MoE` • 

`Cross-Sensor Mixture-of-Experts (CSMoE`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14104v1 Announce Type: new 
Abstract: Self-supervised learning through masked autoencoders has attracted great attention for remote sensing (RS) foundation model (FM) development, enabling improved representation learning across diverse sensors and downstream tasks. However, existing RS FMs often either suffer from substantial computational complexity during both training and inference or exhibit limited representational capacity. These issues restrict their practical applicability in RS. To address this limitation, we propose an adaptation for enhancing the efficiency of RS FMs by integrating the Soft mixture-of-experts (MoE) mechanism into the FM. The integration of Soft MoEs into the FM allows modality-specific expert specialization alongside shared cross-sensor representation learning. To demonstrate the effectiveness of our adaptation, we apply it on the Cross-Sensor Masked Autoencoder (CSMAE) model, resulting in the Cross-Sensor Mixture-of-Experts (CSMoE) model. In addition, we introduce a thematic-climatic descriptor-driven sampling strategy for the construction of a representative and diverse training set to train our CSMoE model. Extensive experiments on scene classification, semantic segmentation, and content-based image retrieval demonstrate that our adaptation yields a reduction in computational requirements while maintaining or improving representational performance. Compared to state-of-the-art RS FMs, CSMoE achieves a superior trade-off between representational capacity, accuracy, and computational efficiency. On average, CSMoE achieves more than twice the computational efficiency of existing RS FMs, while maintaining competitive performance across all experiments. These results show the effectiveness of the proposed adaptation for creating computationally efficient RS FMs. The code for the model, the training set creation, and the model weights will be available at https://git.tu-berlin.de/rsim/csmoe.

## 🔍 Abstract (한글 번역)

arXiv:2509.14104v1 발표 유형: 새로운
요약: 가리고 있는 오토인코더를 통한 자기 지도 학습은 원격 감지(RS) 기반 모델(FM) 개발에 큰 관심을 끌고 있으며, 다양한 센서 및 하류 작업에 걸쳐 향상된 표현 학습을 가능하게 합니다. 그러나 기존의 RS FMs는 종종 훈련 및 추론 중에 상당한 계산 복잡성을 겪거나 표현 능력이 제한되어 있습니다. 이러한 문제들은 RS에서의 실용적 적용을 제한합니다. 이 한계를 해결하기 위해, 우리는 Soft mixture-of-experts (MoE) 메커니즘을 FM에 통합하여 RS FMs의 효율성을 향상시키는 적응을 제안합니다. Soft MoEs를 FM에 통합함으로써, FM에는 모달리티별 전문가 전문화와 함께 공유된 교차 센서 표현 학습이 가능해집니다. 우리의 적응의 효과를 증명하기 위해, 우리는 Cross-Sensor Masked Autoencoder (CSMAE) 모델에 이를 적용하여 Cross-Sensor Mixture-of-Experts (CSMoE) 모델을 만들었습니다. 또한, 우리는 대표적이고 다양한 훈련 세트를 구축하기 위한 테마-기후적 설명자 주도 샘플링 전략을 소개합니다. 우리의 CSMoE 모델을 훈련하기 위해. 장면 분류, 의미적 분할 및 콘텐츠 기반 이미지 검색에 대한 광범위한 실험 결과는 우리의 적응이 계산 요구 사항을 줄이면서 표현 성능을 유지하거나 향상시킨다는 것을 보여줍니다. 최신 기술의 RS FMs와 비교했을 때, CSMoE는 표현 능력, 정확도 및 계산 효율성 사이에서 우수한 균형을 달성합니다. 평균적으로, CSMoE는 기존의 RS FMs보다 두 배 이상의 계산 효율성을 달성하면서 모든 실험에서 경쟁력 있는 성능을 유지합니다. 이러한 결과는 제안된 적응이 계산 효율적인 RS FMs를 만드는 데 효과적임을 보여줍니다. 모델, 훈련 세트 생성 및 모델 가중치에 대한 코드는 https://git.tu-berlin.de/rsim/csmoe에서 제공될 예정입니다.

## 📝 요약

본 연구는 원격 감지를 위한 자기 감독 학습을 통해 효율적인 표현 학습을 가능하게 하는 Soft MoE 메커니즘을 RS 기반 모델에 통합하여 효율성을 향상시키는 새로운 방법을 제안한다. Cross-Sensor Masked Autoencoder (CSMAE) 모델에 이를 적용한 Cross-Sensor Mixture-of-Experts (CSMoE) 모델을 소개하였으며, 다양한 실험을 통해 제안된 적응 방법이 기존 RS 모델에 비해 뛰어난 표현 능력, 정확도 및 계산 효율성을 제공함을 입증하였다. 이를 통해 제안된 적응 방법이 계산적으로 효율적인 RS 모델을 만드는 데 효과적임을 보여주었다.

## 🎯 주요 포인트


- 자기 지도 학습을 통한 원격 감지 기반 모델 개발에 대한 관심이 높아지고 있음

- Soft MoE 메커니즘을 통합하여 효율성 향상을 제안함

- CSMoE 모델은 계산 요구 사항을 줄이고 표현 능력을 향상시킴

- 기존 RS FMs보다 뛰어난 표현 능력, 정확도 및 계산 효율성을 보임


---

*Generated on 2025-09-18 17:03:42*