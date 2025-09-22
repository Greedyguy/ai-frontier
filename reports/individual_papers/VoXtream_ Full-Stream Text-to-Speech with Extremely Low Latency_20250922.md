# VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency

**Korean Title:** VoXtream: 극도로 낮은 지연 시간을 갖춘 풀 스트림 텍스트-음성 변환

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Zero-shot Streaming|Zero-shot Streaming]] [[keywords/specific/Autoregressive Model|Autoregressive Model]] [[keywords/broad/Text-to-Speech|Text-to-Speech]] [[keywords/broad/Transformer|Transformer]] [[keywords/unique/VoXtream|VoXtream]] [[categories/cs.LG|cs.LG]] [[2025-09-22/FocalCodec-Stream_ Streaming Low-Bitrate Speech Coding via Causal Distillation_20250922|FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation]] (83.3% similar) [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (82.3% similar) [[2025-09-22/StreamBridge_ Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant_20250922|StreamBridge: Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Zero-shot Streaming
**🔗 Specific Connectable**: Autoregressive Model
**🔬 Broad Technical**: Text-to-Speech, Transformer
**⭐ Unique Technical**: VoXtream
## 🔗 유사한 논문
- [[2025-09-22/FocalCodec-Stream_ Streaming Low-Bitrate Speech Coding via Causal Distillation_20250922|FocalCodec-Stream Streaming Low-Bitrate Speech Coding via Causal Distillation]] (83.3% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (82.3% similar)
- [[2025-09-22/StreamBridge_ Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant_20250922|StreamBridge Turning Your Offline Video Large Language Model into a Proactive Streaming Assistant]] (80.8% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (79.8% similar)
- [[2025-09-22/FLOAT_ Generative Motion Latent Flow Matching for Audio-driven Talking Portrait_20250922|FLOAT Generative Motion Latent Flow Matching for Audio-driven Talking Portrait]] (79.1% similar)


**ArXiv ID**: [2509.15969](https://arxiv.org/abs/2509.15969)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15969.pdf)


**ArXiv ID**: [2509.15969](https://arxiv.org/abs/2509.15969)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15969.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Zero-shot Streaming
**🔗 Specific Connectable**: Streaming TTS
**⭐ Unique Technical**: VoXtream
**🔬 Broad Technical**: Text to Speech, Transformer

## 🏷️ 추출된 키워드



`Text-to-Speech` • 

`Transformer` • 

`Streaming TTS` • 

`Monotonic Alignment` • 

`VoXtream`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15969v1 Announce Type: cross 
Abstract: We present VoXtream, a fully autoregressive, zero-shot streaming text-to-speech (TTS) system for real-time use that begins speaking from the first word. VoXtream directly maps incoming phonemes to audio tokens using a monotonic alignment scheme and a dynamic look-ahead that does not delay onset. Built around an incremental phoneme transformer, a temporal transformer predicting semantic and duration tokens, and a depth transformer producing acoustic tokens, VoXtream achieves, to our knowledge, the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings. Demo and code are available at https://herimor.github.io/voxtream.

## 🔍 Abstract (한글 번역)

arXiv:2509.15969v1 발표 유형: 교차  
초록: 우리는 VoXtream을 소개합니다. VoXtream은 첫 단어부터 말을 시작하는 실시간 사용을 위한 완전한 자동회귀, 제로샷 스트리밍 텍스트-음성 변환(TTS) 시스템입니다. VoXtream은 단조로운 정렬 방식과 시작을 지연시키지 않는 동적 선행을 사용하여 들어오는 음소를 오디오 토큰으로 직접 매핑합니다. 점진적인 음소 변환기, 의미 및 지속 시간 토큰을 예측하는 시간 변환기, 음향 토큰을 생성하는 깊이 변환기를 중심으로 구축된 VoXtream은 우리가 아는 한, 공개적으로 이용 가능한 스트리밍 TTS 중 가장 낮은 초기 지연을 달성합니다: GPU에서 102 ms. 중간 규모의 9천 시간 코퍼스에서 훈련되었음에도 불구하고, 여러 지표에서 더 큰 기준 모델과 동등하거나 이를 능가하며, 출력 및 전체 스트리밍 설정 모두에서 경쟁력 있는 품질을 제공합니다. 데모와 코드는 https://herimor.github.io/voxtream에서 이용 가능합니다.

## 📝 요약

VoXtream은 실시간 사용을 위한 완전 자율적 제로샷 스트리밍 음성 합성 시스템으로, 첫 단어부터 즉시 발화를 시작합니다. 이 시스템은 단조로운 정렬 방식과 동적 선행 예측을 통해 지연 없이 음소를 오디오 토큰으로 직접 변환합니다. VoXtream은 점진적 음소 변환기, 의미 및 지속 시간 토큰을 예측하는 시간 변환기, 음향 토큰을 생성하는 깊이 변환기로 구성되어 있으며, GPU에서 102ms의 초기 지연을 기록하여 현재 공개된 스트리밍 TTS 중 가장 낮은 초기 지연을 달성했습니다. 9천 시간의 중간 규모 데이터로 학습되었음에도 불구하고, 여러 지표에서 더 큰 규모의 기준 모델을 능가하거나 동등한 성능을 보이며, 출력 및 전체 스트리밍 설정 모두에서 경쟁력 있는 품질을 제공합니다. 데모와 코드는 https://herimor.github.io/voxtream에서 확인할 수 있습니다.

## 🎯 주요 포인트


- 1. VoXtream은 실시간 사용을 위한 완전 자회귀적, 제로샷 스트리밍 텍스트-음성 변환(TTS) 시스템으로, 첫 단어부터 발화를 시작합니다.

- 2. 이 시스템은 단조 정렬 방식과 동적 선행 예측을 사용하여 지연 없이 음소를 오디오 토큰으로 직접 매핑합니다.

- 3. VoXtream은 공개된 스트리밍 TTS 중 가장 낮은 초기 지연(102ms)을 달성하며, 중간 규모의 9천 시간 코퍼스로 훈련되었음에도 더 큰 기준 모델들을 여러 지표에서 능가하거나 동등한 성능을 보입니다.

- 4. VoXtream은 출력 및 전체 스트리밍 설정 모두에서 경쟁력 있는 품질을 제공합니다.

- 5. 데모와 코드는 https://herimor.github.io/voxtream에서 확인할 수 있습니다.


---

*Generated on 2025-09-22 15:45:20*