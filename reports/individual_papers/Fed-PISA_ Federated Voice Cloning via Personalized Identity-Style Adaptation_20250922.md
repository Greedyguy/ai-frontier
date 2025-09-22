# Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation

**Korean Title:** Fed-PISA: 개인화된 정체성-스타일 적응을 통한 연합 음성 복제

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Personalized Identity-Style Adaptation

## 🔗 유사한 논문
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (80.7% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (80.5% similar)
- [[2025-09-18/Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation_20250918|Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation]] (80.0% similar)
- [[2025-09-22/PILOT_ Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting_20250922|PILOT Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting]] (79.6% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (79.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16010v1 Announce Type: cross 
Abstract: Voice cloning for Text-to-Speech (TTS) aims to generate expressive and personalized speech from text using limited data from a target speaker. Federated Learning (FL) offers a collaborative and privacy-preserving framework for this task, but existing approaches suffer from high communication costs and tend to suppress stylistic heterogeneity, resulting in insufficient personalization. To address these issues, we propose Fed-PISA, which stands for Federated Personalized Identity-Style Adaptation. To minimize communication costs, Fed-PISA introduces a disentangled Low-Rank Adaptation (LoRA) mechanism: the speaker's timbre is retained locally through a private ID-LoRA, while only a lightweight style-LoRA is transmitted to the server, thereby minimizing parameter exchange. To harness heterogeneity, our aggregation method, inspired by collaborative filtering, is introduced to create custom models for each client by learning from stylistically similar peers. Experiments show that Fed-PISA improves style expressivity, naturalness, and speaker similarity, outperforming standard federated baselines with minimal communication costs.

## 🔍 Abstract (한글 번역)

arXiv:2509.16010v1 발표 유형: 교차  
초록: 음성 복제(Text-to-Speech, TTS)는 제한된 데이터로부터 목표 화자의 텍스트를 사용하여 표현력 있고 개인화된 음성을 생성하는 것을 목표로 합니다. 연합 학습(Federated Learning, FL)은 이 작업을 위한 협력적이고 프라이버시를 보장하는 프레임워크를 제공하지만, 기존 접근 방식은 높은 통신 비용을 초래하고 스타일의 이질성을 억제하는 경향이 있어 개인화가 충분하지 않습니다. 이러한 문제를 해결하기 위해 우리는 Fed-PISA를 제안합니다. 이는 Federated Personalized Identity-Style Adaptation의 약자입니다. 통신 비용을 최소화하기 위해, Fed-PISA는 분리된 저순위 적응(LoRA) 메커니즘을 도입합니다: 화자의 음색은 개인 ID-LoRA를 통해 로컬에서 유지되며, 가벼운 스타일-LoRA만 서버로 전송되어 매개변수 교환을 최소화합니다. 이질성을 활용하기 위해, 협업 필터링에서 영감을 받은 우리의 집계 방법은 스타일적으로 유사한 동료들로부터 학습하여 각 클라이언트에 맞춤형 모델을 생성합니다. 실험 결과, Fed-PISA는 스타일 표현력, 자연스러움 및 화자 유사성을 개선하며, 최소한의 통신 비용으로 표준 연합 기준을 능가합니다.

## 📝 요약

이 논문은 제한된 데이터로 텍스트에서 개성 있는 음성을 생성하는 음성 복제 기술을 다룹니다. 기존의 연합 학습(Federated Learning) 방식은 통신 비용이 높고 스타일 다양성을 억제하여 개인화가 부족한 문제를 가지고 있습니다. 이를 해결하기 위해 Fed-PISA라는 새로운 방법론을 제안합니다. Fed-PISA는 Low-Rank Adaptation(LoRA) 메커니즘을 활용하여 통신 비용을 줄이고, 개인화된 ID-LoRA는 로컬에 유지하며 가벼운 style-LoRA만 서버로 전송합니다. 또한, 협업 필터링에 영감을 받은 집계 방법을 통해 스타일이 유사한 클라이언트 간의 학습을 통해 맞춤형 모델을 생성합니다. 실험 결과, Fed-PISA는 스타일 표현력, 자연스러움, 화자 유사성을 향상시키며, 통신 비용을 최소화하면서 기존의 연합 학습 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Fed-PISA는 제한된 데이터로 텍스트로부터 개인화된 음성을 생성하는 TTS를 위한 프레임워크로, 통신 비용을 최소화하고 스타일 이질성을 유지합니다.

- 2. Fed-PISA는 Low-Rank Adaptation(LoRA) 메커니즘을 도입하여 개인 ID-LoRA를 통해 화자의 음색을 로컬에서 유지하고, 경량화된 스타일-LoRA만 서버로 전송하여 파라미터 교환을 최소화합니다.

- 3. 협업 필터링에서 영감을 받은 집계 방법을 통해 스타일적으로 유사한 피어로부터 학습하여 각 클라이언트에 맞춤형 모델을 생성합니다.

- 4. 실험 결과, Fed-PISA는 스타일 표현력, 자연스러움, 화자 유사성에서 표준 연합 학습 기준선을 능가하며, 통신 비용을 최소화합니다.

---

*Generated on 2025-09-22 14:21:58*