# VMDNet: Time Series Forecasting with Leakage-Free Samplewise Variational Mode Decomposition and Multibranch Decoding

**Korean Title:** VMDNet: 누출 없는 샘플별 변동 모드 분해 및 다중 분기 디코딩을 통한 시계열 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Temporal Convolutional Networks, Variational Mode Decomposition

## 🔗 유사한 논문
- [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (80.7% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (80.5% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (79.5% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (78.8% similar)
- [[2025-09-18/From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15394v1 Announce Type: new 
Abstract: In time series forecasting, capturing recurrent temporal patterns is essential; decomposition techniques make such structure explicit and thereby improve predictive performance. Variational Mode Decomposition (VMD) is a powerful signal-processing method for periodicity-aware decomposition and has seen growing adoption in recent years. However, existing studies often suffer from information leakage and rely on inappropriate hyperparameter tuning. To address these issues, we propose VMDNet, a causality-preserving framework that (i) applies sample-wise VMD to avoid leakage; (ii) represents each decomposed mode with frequency-aware embeddings and decodes it using parallel temporal convolutional networks (TCNs), ensuring mode independence and efficient learning; and (iii) introduces a bilevel, Stackelberg-inspired optimisation to adaptively select VMD's two core hyperparameters: the number of modes (K) and the bandwidth penalty (alpha). Experiments on two energy-related datasets demonstrate that VMDNet achieves state-of-the-art results when periodicity is strong, showing clear advantages in capturing structured periodic patterns while remaining robust under weak periodicity.

## 🔍 Abstract (한글 번역)

arXiv:2509.15394v1 발표 유형: 신규  
초록: 시계열 예측에서 반복적인 시간 패턴을 포착하는 것은 필수적이며, 분해 기법은 이러한 구조를 명시적으로 만들어 예측 성능을 향상시킵니다. 변동 모드 분해(VMD)는 주기성을 인식하는 분해를 위한 강력한 신호 처리 방법으로, 최근 몇 년간 채택이 증가하고 있습니다. 그러나 기존 연구는 종종 정보 누출 문제를 겪고 부적절한 하이퍼파라미터 조정에 의존합니다. 이러한 문제를 해결하기 위해, 우리는 VMDNet이라는 인과성을 보존하는 프레임워크를 제안합니다. 이 프레임워크는 (i) 샘플 단위의 VMD를 적용하여 누출을 방지하고; (ii) 각 분해된 모드를 주파수 인식 임베딩으로 표현하고 병렬 시간 컨볼루션 네트워크(TCN)를 사용하여 이를 디코딩하여 모드 독립성과 효율적인 학습을 보장하며; (iii) VMD의 두 가지 핵심 하이퍼파라미터인 모드의 수(K)와 대역폭 패널티(알파)를 적응적으로 선택하기 위해 이중 수준의 Stackelberg에서 영감을 받은 최적화를 도입합니다. 두 개의 에너지 관련 데이터셋에 대한 실험 결과, VMDNet은 주기성이 강할 때 최첨단 결과를 달성하며, 구조화된 주기적 패턴을 포착하는 데 있어 명확한 이점을 보이는 동시에 약한 주기성에서도 견고함을 유지합니다.

## 📝 요약

이 논문은 시계열 예측에서 주기적 패턴을 효과적으로 포착하기 위한 새로운 방법론인 VMDNet을 제안합니다. 기존의 변동 모드 분해(VMD) 기법이 정보 누출과 부적절한 하이퍼파라미터 설정 문제를 겪는 것을 개선하기 위해, VMDNet은 샘플 단위의 VMD를 적용하여 정보 누출을 방지하고, 주파수 인식 임베딩을 통해 각 모드를 표현하며, 병렬 시간적 합성곱 네트워크(TCN)를 사용해 모드 독립성과 효율적인 학습을 보장합니다. 또한, VMD의 핵심 하이퍼파라미터인 모드 수(K)와 대역폭 패널티(alpha)를 적응적으로 선택하기 위해 이중 수준의 Stackelberg 최적화를 도입합니다. 에너지 관련 두 데이터셋 실험에서 VMDNet은 강한 주기성을 가진 경우 최첨단 성능을 보이며, 구조화된 주기적 패턴을 포착하는 데 명확한 이점을 보여주고, 약한 주기성에서도 강건함을 유지합니다.

## 🎯 주요 포인트

- 1. 시계열 예측에서 반복적인 시간 패턴을 포착하는 것은 중요하며, 분해 기법은 이러한 구조를 명확히 하여 예측 성능을 향상시킨다.

- 2. 변동 모드 분해(VMD)는 주기성을 인식하는 분해를 위한 강력한 신호 처리 방법으로, 최근 몇 년간 채택이 증가하고 있다.

- 3. VMDNet은 정보 누출을 방지하고 부적절한 하이퍼파라미터 조정을 해결하기 위해 인과성을 보존하는 프레임워크를 제안한다.

- 4. VMDNet은 주파수 인식 임베딩을 사용하여 각 분해된 모드를 표현하고, 병렬 시간 컨볼루션 네트워크(TCN)를 통해 모드 독립성과 효율적인 학습을 보장한다.

- 5. VMDNet은 두 가지 핵심 하이퍼파라미터(K와 알파)를 적응적으로 선택하기 위해 이중 수준의 Stackelberg 영감을 받은 최적화를 도입한다.

---

*Generated on 2025-09-22 15:12:45*