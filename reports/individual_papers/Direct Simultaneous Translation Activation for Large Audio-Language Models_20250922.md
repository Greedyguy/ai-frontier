# Direct Simultaneous Translation Activation for Large Audio-Language Models

**Korean Title:** 대형 오디오-언어 모델을 위한 직접 동시 번역 활성화

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Simultaneous Data Augmentation|Simultaneous Data Augmentation]] [[keywords/specific/Read Write Strategies|Read Write Strategies]] [[keywords/broad/Simultaneous Speech to Text Translation|Simultaneous Speech to Text Translation]] [[keywords/broad/Large Audio Language Models|Large Audio Language Models]] [[keywords/unique/Simultaneous Self Augmentation|Simultaneous Self Augmentation]] [[categories/cs.CL|cs.CL]] [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (83.1% similar) [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (82.0% similar) [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Self Augmentation
**🔬 Broad Technical**: Simultaneous Speech to Text Translation, Large Audio Language Models
**⭐ Unique Technical**: Simultaneous Self Augmentation
## 🔗 유사한 논문
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (83.1% similar)
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (82.0% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (81.9% similar)
- [[2025-09-17/SSL-SSAW_ Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation_20250917|SSL-SSAW Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation]] (81.8% similar)
- [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (81.3% similar)


**ArXiv ID**: [2509.15692](https://arxiv.org/abs/2509.15692)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15692.pdf)


**ArXiv ID**: [2509.15692](https://arxiv.org/abs/2509.15692)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15692.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Self Augmentation
**⭐ Unique Technical**: Simultaneous Self Augmentation
**🔬 Broad Technical**: Simultaneous Speech to Text Translation, Large Audio Language Models

## 🏷️ 추출된 키워드



`Simultaneous Speech-to-Text Translation` • 

`Large Audio-Language Models` • 

`Read-Write Strategies` • 

`Simultaneous Self-Augmentation` • 

`Simultaneous Data Augmentation`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15692v1 Announce Type: cross 
Abstract: Simultaneous speech-to-text translation (Simul-S2TT) aims to translate speech into target text in real time, outputting translations while receiving source speech input, rather than waiting for the entire utterance to be spoken. Simul-S2TT research often modifies model architectures to implement read-write strategies. However, with the rise of large audio-language models (LALMs), a key challenge is how to directly activate Simul-S2TT capabilities in base models without additional architectural changes. In this paper, we introduce {\bf Simul}taneous {\bf S}elf-{\bf A}ugmentation ({\bf SimulSA}), a strategy that utilizes LALMs' inherent capabilities to obtain simultaneous data by randomly truncating speech and constructing partially aligned translation. By incorporating them into offline SFT data, SimulSA effectively bridges the distribution gap between offline translation during pretraining and simultaneous translation during inference. Experimental results demonstrate that augmenting only about {\bf 1\%} of the simultaneous data, compared to the full offline SFT data, can significantly activate LALMs' Simul-S2TT capabilities without modifications to model architecture or decoding strategy.

## 🔍 Abstract (한글 번역)

arXiv:2509.15692v1 발표 유형: 교차  
초록: 동시 음성-텍스트 번역(Simul-S2TT)은 발화 전체가 끝나기를 기다리지 않고, 소스 음성 입력을 받으면서 번역을 출력하여 음성을 실시간으로 목표 텍스트로 번역하는 것을 목표로 합니다. Simul-S2TT 연구는 종종 읽기-쓰기 전략을 구현하기 위해 모델 아키텍처를 수정합니다. 그러나 대형 오디오-언어 모델(LALMs)의 부상과 함께, 추가적인 아키텍처 변경 없이 기본 모델에서 Simul-S2TT 기능을 직접 활성화하는 것이 주요 과제입니다. 본 논문에서는 LALMs의 고유한 기능을 활용하여 음성을 무작위로 잘라내고 부분적으로 정렬된 번역을 구성함으로써 동시 데이터를 얻는 전략인 {\bf Simul}taneous {\bf S}elf-{\bf A}ugmentation ({\bf SimulSA})을 소개합니다. 이를 오프라인 SFT 데이터에 통합함으로써, SimulSA는 사전 학습 중 오프라인 번역과 추론 중 동시 번역 간의 분포 격차를 효과적으로 연결합니다. 실험 결과, 모델 아키텍처나 디코딩 전략을 수정하지 않고도 전체 오프라인 SFT 데이터에 비해 약 {\bf 1\%}의 동시 데이터만을 증강함으로써 LALMs의 Simul-S2TT 기능을 크게 활성화할 수 있음을 보여줍니다.

## 📝 요약

이 논문은 실시간 음성-텍스트 번역(Simul-S2TT)의 새로운 접근법을 제안합니다. 기존 연구는 모델 구조를 수정하여 번역을 수행하지만, 이 논문에서는 대형 오디오-언어 모델(LALMs)을 활용하여 구조 변경 없이 Simul-S2TT 기능을 활성화하는 방법을 탐구합니다. 제안된 SimulSA(Simultaneous Self-Augmentation) 전략은 음성을 무작위로 잘라내고 부분적으로 정렬된 번역을 생성하여 동시 데이터를 얻습니다. 이를 통해 사전 학습 시 오프라인 번역과 추론 시 실시간 번역 간의 분포 차이를 줄입니다. 실험 결과, 전체 오프라인 데이터의 약 1%만을 동시 데이터로 증강해도 모델 구조나 디코딩 전략의 변경 없이 LALMs의 Simul-S2TT 기능을 크게 활성화할 수 있음을 보여줍니다.

## 🎯 주요 포인트


- 1. Simul-S2TT는 실시간으로 음성을 텍스트로 번역하는 기술로, 전체 발화가 끝나기 전에 번역을 출력하는 것을 목표로 한다.

- 2. SimulSA는 대형 오디오-언어 모델(LALMs)의 내재된 능력을 활용하여, 음성을 무작위로 잘라내고 부분적으로 정렬된 번역을 구성하는 전략이다.

- 3. SimulSA는 사전 훈련 중 오프라인 번역과 추론 중 동시 번역 간의 분포 차이를 효과적으로 줄인다.

- 4. SimulSA를 통해 전체 오프라인 SFT 데이터의 약 1%만을 동시 데이터로 증강하여, 모델 아키텍처나 디코딩 전략을 변경하지 않고도 LALMs의 Simul-S2TT 기능을 활성화할 수 있다.


---

*Generated on 2025-09-22 16:32:12*