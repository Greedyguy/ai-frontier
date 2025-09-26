---
keywords:
  - Diffusion Models
  - Text-to-Speech
  - Generative Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14298
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:23:27.119010",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Text-to-Speech",
    "Generative Models"
  ],
  "rejected_keywords": [
    "Speech Recognition",
    "Implicit Task Composition"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.79,
    "Text-to-Speech": 0.78,
    "Generative Models": 0.76
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# SpeechOp: Inference-Time Task Composition for Generative Speech Processing

**Korean Title:** SpeechOp: 생성적 음성 처리를 위한 추론 시 태스크 구성

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Text-to-Speech|Text-to-Speech]], [[keywords/Generative Models|Generative Models]]

## 🔗 유사한 논문
- [[TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (80.6% similar)
- [[MeanFlowSE one-step generative speech enhancement via conditional mean flow]] (79.7% similar)
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (79.5% similar)
- [[SpeechRole A Large-Scale Dataset and Benchmark for Evaluating Speech Role-Playing Agents]] (78.7% similar)
- [[Listening, Imagining & Refining A Heuristic Optimized ASR Correction Framework with LLMs]] (78.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14298v1 Announce Type: cross 
Abstract: While generative Text-to-Speech (TTS) systems leverage vast ``in-the-wild" data to achieve remarkable success, speech-to-speech processing tasks like enhancement face data limitations, which lead data-hungry generative approaches to distort speech content and speaker identity. To bridge this gap, we present SpeechOp, a multi-task latent diffusion model that transforms pre-trained TTS models into a universal speech processor capable of performing a wide range of speech tasks and composing them in novel ways at inference time. By adapting a pre-trained TTS model, SpeechOp inherits a rich understanding of natural speech, accelerating training and improving S2S task quality, while simultaneously enhancing core TTS performance. Finally, we introduce Implicit Task Composition (ITC), a novel pipeline where ASR-derived transcripts (e.g., from Whisper) guide SpeechOp's enhancement via our principled inference-time task composition. ITC achieves state-of-the-art content preservation by robustly combining web-scale speech understanding with SpeechOp's generative capabilities. Audio samples are available at https://justinlovelace.github.io/projects/speechop

## 🔍 Abstract (한글 번역)

arXiv:2509.14298v1 발표 유형: 교차  
초록: 생성적 텍스트-음성 변환(TTS) 시스템은 방대한 "자연 상태" 데이터를 활용하여 놀라운 성공을 거두고 있지만, 음성 향상과 같은 음성-음성 처리 작업은 데이터 제한에 직면하여 데이터에 굶주린 생성적 접근 방식이 음성 내용과 화자 정체성을 왜곡하게 됩니다. 이러한 격차를 해소하기 위해, 우리는 사전 훈련된 TTS 모델을 광범위한 음성 작업을 수행하고 추론 시 새로운 방식으로 이를 구성할 수 있는 범용 음성 처리기로 변환하는 다중 작업 잠재 확산 모델인 SpeechOp을 제안합니다. 사전 훈련된 TTS 모델을 적응시킴으로써, SpeechOp은 자연스러운 음성에 대한 풍부한 이해를 계승하여 훈련을 가속화하고 S2S 작업의 품질을 향상시키는 동시에 핵심 TTS 성능을 강화합니다. 마지막으로, 우리는 ASR에서 파생된 전사(예: Whisper)를 통해 SpeechOp의 향상을 안내하는 원칙적인 추론 시간 작업 구성을 통해 ITC(Implicit Task Composition)를 소개합니다. ITC는 웹 규모의 음성 이해와 SpeechOp의 생성적 기능을 강력하게 결합하여 최첨단의 내용 보존을 달성합니다. 오디오 샘플은 https://justinlovelace.github.io/projects/speechop에서 확인할 수 있습니다.

## 📝 요약

SpeechOp은 기존의 TTS 모델을 다목적 음성 처리기로 변환하는 다중 작업 잠재 확산 모델입니다. 이는 TTS 모델의 자연스러운 음성 이해를 활용하여 훈련을 가속화하고 음성 간 처리(S2S) 작업의 품질을 향상시킵니다. 또한, Implicit Task Composition(ITC)라는 새로운 파이프라인을 도입하여 ASR에서 파생된 전사본을 사용해 SpeechOp의 음성 향상을 유도합니다. ITC는 웹 규모의 음성 이해와 SpeechOp의 생성 능력을 결합하여 최첨단의 콘텐츠 보존 성능을 달성합니다.

## 🎯 주요 포인트

- 1. SpeechOp은 사전 훈련된 TTS 모델을 활용하여 다양한 음성 처리 작업을 수행할 수 있는 범용 음성 처리기로 변환하는 다중 작업 잠재 확산 모델입니다.

- 2. SpeechOp은 자연스러운 음성에 대한 깊은 이해를 통해 훈련을 가속화하고 S2S 작업의 품질을 향상시키며, 동시에 핵심 TTS 성능을 강화합니다.

- 3. ITC(Implicit Task Composition)는 ASR에서 파생된 전사본을 활용하여 SpeechOp의 향상을 유도하는 새로운 파이프라인으로, 웹 규모의 음성 이해와 SpeechOp의 생성 능력을 결합하여 최첨단의 콘텐츠 보존을 달성합니다.

- 4. SpeechOp는 데이터가 부족한 음성 향상 작업에서 발생하는 문제를 해결하기 위해 고안되었습니다.

---

*Generated on 2025-09-19 15:34:39*