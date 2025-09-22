# Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization

**Korean Title:** 고해상도 유한 스칼라 양자화를 통한 청크 기반 음성 사전 훈련

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Chunk Based Speech Pre-training|Chunk Based Speech Pre-training]] [[keywords/specific/Finite Scalar Quantization|Finite Scalar Quantization]] [[keywords/specific/Masked Prediction Loss|Masked Prediction Loss]] [[keywords/broad/Self-supervised Learning|Self-supervised Learning]] [[keywords/unique/Chunk Based Self-supervised Learning|Chunk Based Self-supervised Learning]] [[categories/cs.CL|cs.CL]] [[2025-09-22/Fed-PISA_ Federated Voice Cloning via Personalized Identity-Style Adaptation_20250922|Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation]] (82.1% similar) [[2025-09-22/BiRQ_ Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition_20250922|BiRQ: Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition]] (81.6% similar) [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Finite Scalar Quantization, Masked Prediction Loss
**🔬 Broad Technical**: Self-supervised Learning
**⭐ Unique Technical**: Chunk Based Self-supervised Learning
## 🔗 유사한 논문
- [[2025-09-22/Fed-PISA_ Federated Voice Cloning via Personalized Identity-Style Adaptation_20250922|Fed-PISA Federated Voice Cloning via Personalized Identity-Style Adaptation]] (82.1% similar)
- [[2025-09-22/BiRQ_ Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition_20250922|BiRQ Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition]] (81.6% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (81.4% similar)
- [[2025-09-17/SSL-SSAW_ Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation_20250917|SSL-SSAW Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation]] (81.3% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (80.3% similar)


**ArXiv ID**: [2509.15579](https://arxiv.org/abs/2509.15579)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15579.pdf)


**ArXiv ID**: [2509.15579](https://arxiv.org/abs/2509.15579)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15579.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Chunk Based Pre-training
**🔗 Specific Connectable**: Finite Scalar Quantization, Masked Prediction Loss
**⭐ Unique Technical**: Chunk Based Self-supervised Learning
**🔬 Broad Technical**: Self-supervised Learning

## 🏷️ 추출된 키워드



`Self-supervised Learning` • 

`Finite Scalar Quantization` • 

`Chunk Based Self-supervised Learning` • 

`High Resolution Codebook`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15579v1 Announce Type: new 
Abstract: Low latency speech human-machine communication is becoming increasingly necessary as speech technology advances quickly in the last decade. One of the primary factors behind the advancement of speech technology is self-supervised learning. Most self-supervised learning algorithms are designed with full utterance assumption and compromises have to made if partial utterances are presented, which are common in the streaming applications. In this work, we propose a chunk based self-supervised learning (Chunk SSL) algorithm as an unified solution for both streaming and offline speech pre-training. Chunk SSL is optimized with the masked prediction loss and an acoustic encoder is encouraged to restore indices of those masked speech frames with help from unmasked frames in the same chunk and preceding chunks. A copy and append data augmentation approach is proposed to conduct efficient chunk based pre-training. Chunk SSL utilizes a finite scalar quantization (FSQ) module to discretize input speech features and our study shows a high resolution FSQ codebook, i.e., a codebook with vocabulary size up to a few millions, is beneficial to transfer knowledge from the pre-training task to the downstream tasks. A group masked prediction loss is employed during pre-training to alleviate the high memory and computation cost introduced by the large codebook. The proposed approach is examined in two speech to text tasks, i.e., speech recognition and speech translation. Experimental results on the \textsc{Librispeech} and \textsc{Must-C} datasets show that the proposed method could achieve very competitive results for speech to text tasks at both streaming and offline modes.

## 🔍 Abstract (한글 번역)

arXiv:2509.15579v1 발표 유형: 신규  
초록: 지난 10년 동안 음성 기술이 빠르게 발전함에 따라 저지연 음성 인간-기계 통신이 점점 더 필요해지고 있습니다. 음성 기술 발전의 주요 요인 중 하나는 자기 지도 학습(self-supervised learning)입니다. 대부분의 자기 지도 학습 알고리즘은 전체 발화 가정을 기반으로 설계되어 있으며, 스트리밍 응용 프로그램에서 흔히 발생하는 부분 발화가 제공될 경우 타협이 필요합니다. 본 연구에서는 스트리밍 및 오프라인 음성 사전 훈련 모두에 대한 통합 솔루션으로 청크 기반 자기 지도 학습(Chunk SSL) 알고리즘을 제안합니다. Chunk SSL은 마스크 예측 손실로 최적화되며, 음향 인코더는 동일한 청크 및 이전 청크의 마스크되지 않은 프레임의 도움을 받아 마스크된 음성 프레임의 인덱스를 복원하도록 유도됩니다. 효율적인 청크 기반 사전 훈련을 수행하기 위해 복사 및 추가 데이터 증강 접근법이 제안됩니다. Chunk SSL은 유한 스칼라 양자화(FSQ) 모듈을 활용하여 입력 음성 특징을 이산화하며, 연구 결과에 따르면 수백만 개의 어휘 크기를 가진 고해상도 FSQ 코드북이 사전 훈련 작업에서 다운스트림 작업으로 지식을 전이하는 데 유익하다는 것을 보여줍니다. 대규모 코드북으로 인해 발생하는 높은 메모리 및 계산 비용을 완화하기 위해 사전 훈련 중 그룹 마스크 예측 손실이 사용됩니다. 제안된 접근법은 음성 인식 및 음성 번역이라는 두 가지 음성-텍스트 작업에서 검증되었습니다. \textsc{Librispeech} 및 \textsc{Must-C} 데이터셋에 대한 실험 결과, 제안된 방법이 스트리밍 및 오프라인 모드 모두에서 음성-텍스트 작업에 대해 매우 경쟁력 있는 결과를 달성할 수 있음을 보여줍니다.

## 📝 요약

최근 음성 기술의 발전으로 인해 낮은 지연 시간의 인간-기계 음성 통신이 중요해지고 있습니다. 이러한 발전의 주요 요인 중 하나는 자가 지도 학습입니다. 기존의 자가 지도 학습 알고리즘은 전체 발화 기반으로 설계되어 스트리밍 환경에서 부분 발화가 있을 때 한계가 있습니다. 본 연구에서는 스트리밍과 오프라인 음성 사전 학습 모두에 적합한 청크 기반 자가 지도 학습(Chunk SSL) 알고리즘을 제안합니다. 이 알고리즘은 마스크 예측 손실을 최적화하며, 청크 내 마스크된 음성 프레임의 복원을 촉진합니다. 또한, 효율적인 청크 기반 사전 학습을 위해 데이터 증강 기법을 도입했습니다. 제안된 방법은 음성 인식과 번역 작업에서 경쟁력 있는 성능을 보였으며, \textsc{Librispeech}와 \textsc{Must-C} 데이터셋 실험에서 우수한 결과를 확인했습니다.

## 🎯 주요 포인트


- 1. 음성 기술의 발전에 따라 저지연 음성 인간-기계 통신의 필요성이 증가하고 있습니다.

- 2. 본 연구에서는 스트리밍 및 오프라인 음성 사전 훈련을 위한 통합 솔루션으로 청크 기반 자가 지도 학습 알고리즘(Chunk SSL)을 제안합니다.

- 3. Chunk SSL은 마스크 예측 손실을 최적화하고, 청크 내 및 이전 청크의 마스크되지 않은 프레임을 활용하여 마스크된 음성 프레임의 인덱스를 복원하도록 음향 인코더를 유도합니다.

- 4. 고해상도 유한 스칼라 양자화(FSQ) 코드북은 사전 훈련 작업에서 다운스트림 작업으로 지식을 전이하는 데 유리합니다.

- 5. 제안된 방법은 음성 인식 및 음성 번역 작업에서 매우 경쟁력 있는 결과를 달성했습니다.


---

*Generated on 2025-09-22 16:24:16*