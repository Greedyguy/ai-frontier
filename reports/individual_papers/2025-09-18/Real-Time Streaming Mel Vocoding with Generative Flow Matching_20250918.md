---
keywords:
  - Generative Flow Matching
  - MelFlow
  - Mel Vocoding
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:13:53.807459",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Flow Matching",
    "MelFlow",
    "Mel Vocoding"
  ],
  "rejected_keywords": [
    "DiffPhase",
    "Speech Recognition"
  ],
  "similarity_scores": {
    "Generative Flow Matching": 0.82,
    "MelFlow": 0.8,
    "Mel Vocoding": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Real-Time Streaming Mel Vocoding with Generative Flow Matching

**Korean Title:** 실시간 스트리밍 멜 보코딩을 위한 생성적 흐름 매칭

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Generative Flow Matching|Generative Flow Matching]], [[keywords/MelFlow|MelFlow]], [[keywords/Mel Vocoding|Mel vocoding]]

## 🔗 유사한 논문
- [[MeanFlowSE_ one-step generative speech enhancement via conditional mean flow_20250919|MeanFlowSE one-step generative speech enhancement via conditional mean flow]] (83.5% similar)
- [[SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (77.6% similar)
- [[WorldForge_ Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (77.6% similar)
- [[Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (77.5% similar)
- [[Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (77.0% similar)

## 📋 저자 정보

**Authors:** Simon Welker, Tal Peer, Timo Gerkmann

## 📄 Abstract (원문)

The task of Mel vocoding, i.e., the inversion of a Mel magnitude spectrogram
to an audio waveform, is still a key component in many text-to-speech (TTS)
systems today. Based on generative flow matching, our prior work on generative
STFT phase retrieval (DiffPhase), and the pseudoinverse operator of the Mel
filterbank, we develop MelFlow, a streaming-capable generative Mel vocoder for
speech sampled at 16 kHz with an algorithmic latency of only 32 ms and a total
latency of 48 ms. We show real-time streaming capability at this latency not
only in theory, but in practice on a consumer laptop GPU. Furthermore, we show
that our model achieves substantially better PESQ and SI-SDR values compared to
well-established not streaming-capable baselines for Mel vocoding including
HiFi-GAN.

## 🔍 Abstract (한글 번역)

Mel vocoding, 즉 Mel 크기 스펙트로그램을 오디오 파형으로 변환하는 작업은 오늘날 많은 텍스트-음성 변환(TTS) 시스템에서 여전히 중요한 구성 요소입니다. 생성적 흐름 매칭, 생성적 STFT 위상 복원(DiffPhase)에 대한 이전 연구, 그리고 Mel 필터뱅크의 의사역 연산자를 기반으로, 우리는 MelFlow를 개발하였습니다. 이는 16 kHz로 샘플링된 음성을 위한 스트리밍 가능한 생성적 Mel vocoder로, 알고리즘 지연 시간이 단 32 ms이며 총 지연 시간은 48 ms입니다. 우리는 이 지연 시간에서의 실시간 스트리밍 기능을 이론뿐만 아니라 소비자용 노트북 GPU에서 실제로도 보여줍니다. 또한, 우리의 모델이 Mel vocoding을 위한 HiFi-GAN을 포함한 잘 확립된 스트리밍 불가능한 기준 모델들에 비해 PESQ 및 SI-SDR 값에서 상당히 더 나은 성능을 달성함을 보여줍니다.

## 📝 요약

이 논문은 Mel vocoding, 즉 Mel 스펙트로그램을 오디오 파형으로 변환하는 작업을 다룹니다. 저자들은 이전 연구에서 제안한 생성적 STFT 위상 복구 기법(DiffPhase)과 Mel 필터뱅크의 의사역행 연산자를 기반으로 MelFlow라는 스트리밍 가능한 생성적 Mel vocoder를 개발했습니다. 이 모델은 16 kHz로 샘플링된 음성을 32 ms의 알고리즘 지연과 총 48 ms의 지연으로 실시간 스트리밍할 수 있습니다. 실험 결과, MelFlow는 HiFi-GAN 등 기존의 비스트리밍 기반 Mel vocoding 기법보다 PESQ와 SI-SDR 측면에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. MelFlow는 Mel vocoding을 위한 스트리밍 가능한 생성 모델로, 16 kHz 샘플링된 음성에 대해 32 ms의 알고리즘 지연과 48 ms의 총 지연을 달성합니다.

- 2. MelFlow는 소비자용 노트북 GPU에서 실시간 스트리밍이 가능함을 이론적으로뿐만 아니라 실제로도 입증했습니다.

- 3. MelFlow는 PESQ 및 SI-SDR 값에서 HiFi-GAN과 같은 기존의 비스트리밍 Mel vocoding 모델들보다 훨씬 우수한 성능을 보입니다.

- 4. MelFlow는 생성적 흐름 매칭, 생성적 STFT 위상 복원(DiffPhase), Mel 필터뱅크의 유사역 연산자를 기반으로 개발되었습니다.

---

*Generated on 2025-09-20 01:04:46*