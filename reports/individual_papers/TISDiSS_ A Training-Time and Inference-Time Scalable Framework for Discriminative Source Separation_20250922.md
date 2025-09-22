# TISDiSS: A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation

**Korean Title:** TISDiSS: 판별적 원천 분리를 위한 훈련 시 및 추론 시 확장 가능한 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Inference-Time Scaling

## 🔗 유사한 논문
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp Inference-Time Task Composition for Generative Speech Processing]] (81.8% similar)
- [[2025-09-19/Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (81.6% similar)
- [[2025-09-17/Slim-SC_ Thought Pruning for Efficient Scaling with Self-Consistency_20250917|Slim-SC Thought Pruning for Efficient Scaling with Self-Consistency]] (78.6% similar)
- [[2025-09-22/Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification_20250922|Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification]] (78.6% similar)
- [[2025-09-19/MeanFlowSE_ one-step generative speech enhancement via conditional mean flow_20250919|MeanFlowSE one-step generative speech enhancement via conditional mean flow]] (78.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15666v1 Announce Type: cross 
Abstract: Source separation is a fundamental task in speech, music, and audio processing, and it also provides cleaner and larger data for training generative models. However, improving separation performance in practice often depends on increasingly large networks, inflating training and deployment costs. Motivated by recent advances in inference-time scaling for generative modeling, we propose Training-Time and Inference-Time Scalable Discriminative Source Separation (TISDiSS), a unified framework that integrates early-split multi-loss supervision, shared-parameter design, and dynamic inference repetitions. TISDiSS enables flexible speed-performance trade-offs by adjusting inference depth without retraining additional models. We further provide systematic analyses of architectural and training choices and show that training with more inference repetitions improves shallow-inference performance, benefiting low-latency applications. Experiments on standard speech separation benchmarks demonstrate state-of-the-art performance with a reduced parameter count, establishing TISDiSS as a scalable and practical framework for adaptive source separation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15666v1 발표 유형: 교차  
초록: 소스 분리는 음성, 음악 및 오디오 처리에서 기본적인 작업이며, 생성 모델을 훈련하기 위한 더 깨끗하고 큰 데이터를 제공합니다. 그러나 실제로 분리 성능을 향상시키는 것은 종종 점점 더 큰 네트워크에 의존하며, 이는 훈련 및 배포 비용을 증가시킵니다. 생성 모델링을 위한 추론 시간 확장의 최근 발전에 영감을 받아, 우리는 훈련 시간 및 추론 시간 확장 가능한 판별 소스 분리(TISDiSS)를 제안합니다. 이는 초기 분할 다중 손실 감독, 공유 매개변수 설계 및 동적 추론 반복을 통합하는 통합 프레임워크입니다. TISDiSS는 추가 모델을 재훈련하지 않고도 추론 깊이를 조정하여 유연한 속도-성능 절충을 가능하게 합니다. 우리는 또한 건축 및 훈련 선택에 대한 체계적인 분석을 제공하고, 더 많은 추론 반복으로 훈련하는 것이 얕은 추론 성능을 향상시켜 저지연 응용 프로그램에 이점을 준다는 것을 보여줍니다. 표준 음성 분리 벤치마크에 대한 실험은 매개변수 수를 줄이면서 최첨단 성능을 입증하며, TISDiSS를 적응형 소스 분리를 위한 확장 가능하고 실용적인 프레임워크로 확립합니다.

## 📝 요약

이 논문은 음성 및 음악 처리에서 중요한 과제인 소스 분리를 다루며, 이를 위한 새로운 프레임워크인 TISDiSS를 제안합니다. TISDiSS는 훈련 및 추론 시 확장 가능한 소스 분리를 가능하게 하여, 추가 모델 재훈련 없이 추론 깊이를 조정해 성능과 속도 간의 균형을 맞출 수 있습니다. 이 방법은 초기 분할 다중 손실 감독, 공유 매개변수 설계, 동적 추론 반복을 통합하여 효율성을 높입니다. 실험 결과, TISDiSS는 적은 매개변수로도 최첨단 성능을 달성하며, 특히 낮은 지연 시간이 필요한 응용 프로그램에 유리한 성능을 보입니다.

## 🎯 주요 포인트

- 1. TISDiSS는 훈련 및 추론 시 확장 가능한 차별적 소스 분리를 위한 통합 프레임워크로, 초기 분할 다중 손실 감독, 공유 매개변수 설계, 동적 추론 반복을 통합합니다.

- 2. TISDiSS는 추가 모델 재훈련 없이 추론 깊이를 조정하여 유연한 속도-성능 절충을 가능하게 합니다.

- 3. 더 많은 추론 반복으로 훈련하면 얕은 추론 성능이 향상되어 저지연 애플리케이션에 유리합니다.

- 4. 표준 음성 분리 벤치마크 실험에서 TISDiSS는 매개변수 수를 줄이면서 최첨단 성능을 입증했습니다.

- 5. TISDiSS는 적응형 소스 분리를 위한 확장 가능하고 실용적인 프레임워크로 자리매김했습니다.

---

*Generated on 2025-09-22 14:07:25*