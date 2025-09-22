# FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation

**Korean Title:** FocalCodec-Stream: 인과적 증류를 통한 저비트율 음성 코딩 스트리밍

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hybrid Codec

## 🔗 유사한 논문
- [[2025-09-22/Compose Yourself_ Average-Velocity Flow Matching for One-Step Speech Enhancement_20250922|Compose Yourself Average-Velocity Flow Matching for One-Step Speech Enhancement]] (80.3% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (80.2% similar)
- [[2025-09-18/Generative Image Coding with Diffusion Prior_20250918|Generative Image Coding with Diffusion Prior]] (78.4% similar)
- [[2025-09-19/MeanFlowSE_ one-step generative speech enhancement via conditional mean flow_20250919|MeanFlowSE one-step generative speech enhancement via conditional mean flow]] (77.7% similar)
- [[2025-09-19/Interactive Face Video Coding_ A Generative Compression Framework_20250919|Interactive Face Video Coding A Generative Compression Framework]] (77.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16195v1 Announce Type: cross 
Abstract: Neural audio codecs are a fundamental component of modern generative audio pipelines. Although recent codecs achieve strong low-bitrate reconstruction and provide powerful representations for downstream tasks, most are non-streamable, limiting their use in real-time applications. We present FocalCodec-Stream, a hybrid codec based on focal modulation that compresses speech into a single binary codebook at 0.55 - 0.80 kbps with a theoretical latency of 80 ms. Our approach combines multi-stage causal distillation of WavLM with targeted architectural improvements, including a lightweight refiner module that enhances quality under latency constraints. Experiments show that FocalCodec-Stream outperforms existing streamable codecs at comparable bitrates, while preserving both semantic and acoustic information. The result is a favorable trade-off between reconstruction quality, downstream task performance, latency, and efficiency. Code and checkpoints will be released at https://github.com/lucadellalib/focalcodec.

## 🔍 Abstract (한글 번역)

arXiv:2509.16195v1 발표 유형: 교차  
초록: 신경 오디오 코덱은 현대 생성 오디오 파이프라인의 기본 구성 요소입니다. 최근의 코덱들은 낮은 비트레이트에서도 강력한 재구성을 달성하고, 후속 작업을 위한 강력한 표현을 제공하지만, 대부분은 스트리밍이 불가능하여 실시간 응용 프로그램에서의 사용이 제한됩니다. 우리는 FocalCodec-Stream을 소개합니다. 이는 초점 변조에 기반한 하이브리드 코덱으로, 0.55 - 0.80 kbps의 단일 이진 코드북으로 음성을 압축하며 이론적 지연 시간은 80 ms입니다. 우리의 접근법은 WavLM의 다단계 인과 증류와 지연 시간 제약 하에서 품질을 향상시키는 경량의 정제 모듈을 포함한 목표 지향적 아키텍처 개선을 결합합니다. 실험 결과, FocalCodec-Stream은 기존의 스트리밍 가능한 코덱보다 유사한 비트레이트에서 더 뛰어난 성능을 보이며, 의미적 및 음향적 정보를 모두 보존합니다. 그 결과는 재구성 품질, 후속 작업 성능, 지연 시간 및 효율성 간의 유리한 절충안을 제공합니다. 코드와 체크포인트는 https://github.com/lucadellalib/focalcodec에서 공개될 예정입니다.

## 📝 요약

FocalCodec-Stream은 실시간 응용을 위한 스트리밍 가능한 하이브리드 신경 오디오 코덱으로, 0.55 - 0.80 kbps의 비트레이트에서 80ms의 이론적 지연 시간을 제공합니다. WavLM의 다단계 인과적 증류와 경량화된 리파이너 모듈을 통해 품질을 개선하며, 기존 스트리머블 코덱보다 뛰어난 성능을 보입니다. 이 코덱은 재구성 품질, 다운스트림 작업 성능, 지연 시간, 효율성 간의 균형을 잘 유지합니다. 코드는 GitHub에서 공개될 예정입니다.

## 🎯 주요 포인트

- 1. FocalCodec-Stream은 초점 변조를 기반으로 한 하이브리드 코덱으로, 0.55 - 0.80 kbps의 비트레이트에서 이진 코드북으로 음성을 압축하며, 이론적 지연 시간은 80 ms입니다.

- 2. 이 코덱은 WavLM의 다단계 인과적 증류와 경량화된 정제 모듈을 포함한 아키텍처 개선을 결합하여 지연 시간 제약 하에서도 품질을 향상시킵니다.

- 3. 실험 결과, FocalCodec-Stream은 기존의 스트리밍 가능한 코덱보다 유사한 비트레이트에서 더 나은 성능을 보이며, 의미적 및 음향적 정보를 보존합니다.

- 4. 이 연구는 재구성 품질, 다운스트림 작업 성능, 지연 시간, 효율성 간의 유리한 균형을 제공합니다.

- 5. 코드와 체크포인트는 https://github.com/lucadellalib/focalcodec에서 공개될 예정입니다.

---

*Generated on 2025-09-22 14:27:05*