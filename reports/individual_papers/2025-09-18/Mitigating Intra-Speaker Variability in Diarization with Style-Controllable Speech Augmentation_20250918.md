# Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation

**Korean Title:** 화자 내 변동성을 완화하기 위한 스타일 제어 가능한 음성 증강을 통한 다이어리제이션 개선

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Miseul Kim|Miseul Kim]] [[authors/Soo Jin Park|Soo Jin Park]] [[authors/Kyungguen Byun|Kyungguen Byun]] [[authors/Hyeon-Kyeong Shin|Hyeon-Kyeong Shin]] [[authors/Sunkuk Moon|Sunkuk Moon]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Intra-speaker Variability Mitigation

## 🔗 유사한 논문
- [[Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (79.5% similar)
- [[Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech_20250919|Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech]] (78.8% similar)
- [[Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (78.5% similar)
- [[Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (78.1% similar)
- [[SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (77.1% similar)

## 📋 저자 정보

**Authors:** Miseul Kim, Soo Jin Park, Kyungguen Byun, Hyeon-Kyeong Shin, Sunkuk Moon, Shuhua Zhang, Erik Visser

## 📄 Abstract (원문)

Speaker diarization systems often struggle with high intrinsic intra-speaker
variability, such as shifts in emotion, health, or content. This can cause
segments from the same speaker to be misclassified as different individuals,
for example, when one raises their voice or speaks faster during conversation.
To address this, we propose a style-controllable speech generation model that
augments speech across diverse styles while preserving the target speaker's
identity. The proposed system starts with diarized segments from a conventional
diarizer. For each diarized segment, it generates augmented speech samples
enriched with phonetic and stylistic diversity. And then, speaker embeddings
from both the original and generated audio are blended to enhance the system's
robustness in grouping segments with high intrinsic intra-speaker variability.
We validate our approach on a simulated emotional speech dataset and the
truncated AMI dataset, demonstrating significant improvements, with error rate
reductions of 49% and 35% on each dataset, respectively.

## 🔍 Abstract (한글 번역)

화자 분할 시스템은 감정, 건강, 또는 내용의 변화와 같은 높은 내재적 화자 내 변동성으로 인해 종종 어려움을 겪습니다. 이는 동일한 화자의 세그먼트가 서로 다른 개체로 잘못 분류되는 원인이 될 수 있으며, 예를 들어 대화 중에 목소리를 높이거나 더 빠르게 말할 때 발생할 수 있습니다. 이를 해결하기 위해, 우리는 대상 화자의 정체성을 유지하면서 다양한 스타일로 음성을 증강하는 스타일 제어 가능한 음성 생성 모델을 제안합니다. 제안된 시스템은 기존의 화자 분할기의 분할된 세그먼트로 시작합니다. 각 분할된 세그먼트에 대해, 음운적 및 스타일적 다양성이 풍부한 증강 음성 샘플을 생성합니다. 그런 다음, 원본 및 생성된 오디오에서 화자 임베딩을 혼합하여 높은 내재적 화자 내 변동성을 가진 세그먼트를 그룹화하는 시스템의 견고성을 강화합니다. 우리는 모의 감정 음성 데이터셋과 축약된 AMI 데이터셋에서 우리의 접근 방식을 검증하였으며, 각각의 데이터셋에서 오류율이 49%와 35% 감소하는 유의미한 개선을 입증하였습니다.

## 📝 요약

이 논문은 감정, 건강, 내용 변화 등으로 인한 화자의 내재적 변동성 문제를 해결하기 위해 스타일 제어 가능한 음성 생성 모델을 제안합니다. 기존 화자 분할 시스템에서 얻은 세그먼트를 바탕으로, 다양한 스타일의 음성을 생성하여 화자의 정체성을 유지하면서도 음성의 다양성을 증대시킵니다. 원본 및 생성된 음성에서 추출한 화자 임베딩을 결합하여 시스템의 강건성을 높입니다. 제안된 방법은 모의 감정 음성 데이터셋과 AMI 데이터셋에서 각각 49%와 35%의 오류율 감소를 보여줍니다.

## 🎯 주요 포인트

- 1. 화자 분할 시스템은 감정, 건강, 내용 변화 등으로 인한 화자 내 변동성 때문에 동일 화자의 발화가 다른 사람의 것으로 잘못 분류될 수 있다.

- 2. 이를 해결하기 위해, 우리는 목표 화자의 정체성을 유지하면서 다양한 스타일로 음성을 증강하는 스타일 제어 가능한 음성 생성 모델을 제안한다.

- 3. 제안된 시스템은 기존의 화자 분할 시스템에서 시작하여, 각 분할된 세그먼트에 대해 음운 및 스타일 다양성이 풍부한 증강 음성 샘플을 생성한다.

- 4. 원본 및 생성된 오디오에서 화자 임베딩을 혼합하여 화자 내 변동성이 큰 세그먼트를 그룹화하는 시스템의 강건성을 향상시킨다.

- 5. 제안된 접근법은 감정적 음성 데이터셋과 AMI 데이터셋에서 각각 49%와 35%의 오류율 감소를 보여주며 유의미한 개선을 입증한다.

---

*Generated on 2025-09-20 05:48:10*