
# AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration

**Korean Title:** AD-DINOv3: 이상 감지를 위한 DINOv3의 Zero-Shot Anomaly Detection을 향상시키는 Anomaly-Aware Calibration

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Anomaly-Aware Calibration|Anomaly-Aware Calibration]] [[keywords/broad/Anomaly Detection|Anomaly Detection]] [[keywords/broad/Zero-Shot Learning|Zero-Shot Learning]] [[keywords/specific/Multimodal Contrastive Learning|Multimodal Contrastive Learning]] [[keywords/unique/AD-DINOv3|AD-DINOv3]] [[categories/cs.CV|cs.CV]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Anomaly-Aware Calibration
**🔬 Broad Technical**: Anomaly Detection, Zero-Shot Learning
**🔗 Specific Connectable**: Multimodal Contrastive Learning
**⭐ Unique Technical**: AD-DINOv3

**ArXiv ID**: [2509.14084](https://arxiv.org/abs/2509.14084)
**Published**: 2025-09-18
**Category**: cs.CV
**PDF**: [Download](https://arxiv.org/pdf/2509.14084.pdf)


## 🏷️ 추출된 키워드



`Anomaly Detection` • 

`Contrastive Learning` • 

`Multimodal Framework` • 

`AD-DINOv3` • 

`Anomaly-Aware Calibration`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14084v1 Announce Type: new 
Abstract: Zero-Shot Anomaly Detection (ZSAD) seeks to identify anomalies from arbitrary novel categories, offering a scalable and annotation-efficient solution. Traditionally, most ZSAD works have been based on the CLIP model, which performs anomaly detection by calculating the similarity between visual and text embeddings. Recently, vision foundation models such as DINOv3 have demonstrated strong transferable representation capabilities. In this work, we are the first to adapt DINOv3 for ZSAD. However, this adaptation presents two key challenges: (i) the domain bias between large-scale pretraining data and anomaly detection tasks leads to feature misalignment; and (ii) the inherent bias toward global semantics in pretrained representations often leads to subtle anomalies being misinterpreted as part of the normal foreground objects, rather than being distinguished as abnormal regions. To overcome these challenges, we introduce AD-DINOv3, a novel vision-language multimodal framework designed for ZSAD. Specifically, we formulate anomaly detection as a multimodal contrastive learning problem, where DINOv3 is employed as the visual backbone to extract patch tokens and a CLS token, and the CLIP text encoder provides embeddings for both normal and abnormal prompts. To bridge the domain gap, lightweight adapters are introduced in both modalities, enabling their representations to be recalibrated for the anomaly detection task. Beyond this baseline alignment, we further design an Anomaly-Aware Calibration Module (AACM), which explicitly guides the CLS token to attend to anomalous regions rather than generic foreground semantics, thereby enhancing discriminability. Extensive experiments on eight industrial and medical benchmarks demonstrate that AD-DINOv3 consistently matches or surpasses state-of-the-art methods, verifying its superiority as a general zero-shot anomaly detection framework.

## 🔍 Abstract (한글 번역)

arXiv:2509.14084v1 발표 유형: 새로운
요약: 제로샷 이상 감지 (ZSAD)는 임의의 새로운 범주에서 이상을 식별하여 확장 가능하고 주석 효율적인 솔루션을 제공합니다. 전통적으로 대부분의 ZSAD 작업은 시각 및 텍스트 임베딩 간 유사성을 계산하여 이상을 감지하는 CLIP 모델을 기반으로 합니다. 최근에는 DINOv3와 같은 비전 기반 모델이 강력한 전이 가능한 표현 능력을 보여주었습니다. 본 연구에서는 DINOv3를 ZSAD에 적응시키는 첫 번째 연구입니다. 그러나 이 적응은 두 가지 주요 도전을 제시합니다: (i) 대규모 사전 훈련 데이터와 이상 감지 작업 간의 도메인 편향으로 인해 특징 불일치가 발생하고; (ii) 사전 훈련된 표현에서 일반적으로 글로벌 의미론적 편향이 나타나 이상적인 지역을 일반적인 전경 의미론의 일부로 오인하게 되어 세세한 이상을 정상 전경 객체의 일부로 오인하게 되는 문제가 있습니다. 이러한 도전을 극복하기 위해 우리는 ZSAD를 위해 설계된 새로운 비전-언어 멀티모달 프레임워크인 AD-DINOv3를 소개합니다. 구체적으로, 우리는 이상 감지를 멀티모달 대조 학습 문제로 정의하고, DINOv3를 시각적 백본으로 사용하여 패치 토큰과 CLS 토큰을 추출하고, CLIP 텍스트 인코더가 정상 및 이상적인 프롬프트에 대한 임베딩을 제공합니다. 도메인 갭을 극복하기 위해 두 모달리티에 가벼운 어댑터를 도입하여 이들의 표현을 이상 감지 작업에 재보정할 수 있도록 합니다. 이 기본 정렬을 넘어서, 우리는 CLS 토큰이 일반적인 전경 의미론이 아닌 이상적인 지역에 주의를 기울이도록 명시적으로 안내하는 이상 감지용 보정 모듈 (AACM)을 설계하여 식별력을 향상시킵니다. 산업 및 의료 벤치마크 8개에 대한 광범위한 실험 결과는 AD-DINOv3가 항상 최첨단 방법과 일치하거나 그것을 능가함을 확인하여 일반적인 제로샷 이상 감지 프레임워크로서의 우수성을 입증합니다.

## 📝 요약

본 연구는 Zero-Shot Anomaly Detection (ZSAD)을 위해 DINOv3 모델을 처음으로 적용한 것을 소개한다. 이에는 대규모 사전 학습 데이터와 이상 감지 작업 사이의 도메인 편향으로 인한 기능 불일치와, 사전 학습 표현에서의 전역 의미론적 편향으로 인해 세밀한 이상 현상이 일반적인 전경 객체의 일부로 오인되는 문제를 극복하기 위해 AD-DINOv3라는 새로운 비전-언어 다중 모달 프레임워크를 제안한다. 이를 통해 이상 감지를 다중 모달 대조 학습 문제로 정의하고 DINOv3를 시각적 백본으로 사용하여 패치 토큰과 CLS 토큰을 추출하고 CLIP 텍스트 인코더가 정상 및 비정상 프롬프트에 대한 임베딩을 제공한다. 실험 결과 AD-DINOv3는 8가지 산업 및 의료 벤치마크에서 최첨단 방법과 일치하거나 능가하여 일반적인 제로샷 이상 감지 프레임워크로서 우수성을 입증한다.

## 🎯 주요 포인트


- 1. Zero-Shot Anomaly Detection (ZSAD)는 새로운 범주의 이상을 식별하여 확장 가능하고 주석 효율적인 솔루션을 제공한다.

- 2. DINOv3를 ZSAD에 적용하는 것은 도메인 편향과 전역 의미론적 편향과 같은 두 가지 주요 도전에 직면한다.

- 3. AD-DINOv3는 ZSAD를 위한 새로운 시각-언어 다중 모달 프레임워크로, 상태-of-the-art 방법을 능가하는 성능을 보여준다.


---

*Generated on 2025-09-18 17:03:12*