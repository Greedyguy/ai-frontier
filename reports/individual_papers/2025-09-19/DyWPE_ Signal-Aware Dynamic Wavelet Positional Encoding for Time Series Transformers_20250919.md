
# DyWPE: Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers

**Korean Title:** DyWPE: 시계열 변환기를 위한 신호 인식 동적 웨이블릿 위치 인코딩

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Signal-Aware Positional Encoding

## 🔗 유사한 논문
- [[DECAMP Towards Scene-Consistent Multi-Agent Motion Prediction with Disentangled Context-Aware Pre-Training]] (75.7% similar)
- [[Integrating_Text_and_Time-Series_into_(Large)_Language_Models_to_Predict_Medical_Outcomes_20250918|Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes]] (75.1% similar)
- [[(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (75.1% similar)
- [[Artificial neural networks ensemble methodology to predict significant wave height]] (75.1% similar)
- [[Identity-Preserving_Text-to-Video_Generation_Guided_by_Simple_yet_Effective_Spatial-Temporal_Decoupled_Representations_20250918|Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations]] (75.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14640v1 Announce Type: new 
Abstract: Existing positional encoding methods in transformers are fundamentally signal-agnostic, deriving positional information solely from sequence indices while ignoring the underlying signal characteristics. This limitation is particularly problematic for time series analysis, where signals exhibit complex, non-stationary dynamics across multiple temporal scales. We introduce Dynamic Wavelet Positional Encoding (DyWPE), a novel signal-aware framework that generates positional embeddings directly from input time series using the Discrete Wavelet Transform (DWT). Comprehensive experiments in ten diverse time series datasets demonstrate that DyWPE consistently outperforms eight existing state-of-the-art positional encoding methods, achieving average relative improvements of 9.1\% compared to baseline sinusoidal absolute position encoding in biomedical signals, while maintaining competitive computational efficiency.

## 🔍 Abstract (한글 번역)

arXiv:2509.14640v1 발표 유형: 신규  
초록: 기존의 트랜스포머 위치 인코딩 방법은 기본적으로 신호에 무관하며, 시퀀스 인덱스에서만 위치 정보를 도출하고 기본 신호 특성을 무시합니다. 이러한 제한은 신호가 여러 시간적 스케일에 걸쳐 복잡하고 비정상적인 동작을 나타내는 시계열 분석에서 특히 문제가 됩니다. 우리는 입력 시계열로부터 이산 웨이블릿 변환(DWT)을 사용하여 직접 위치 임베딩을 생성하는 새로운 신호 인식 프레임워크인 동적 웨이블릿 위치 인코딩(DyWPE)을 소개합니다. 열 가지 다양한 시계열 데이터셋에 대한 종합적인 실험은 DyWPE가 기존의 여덟 가지 최첨단 위치 인코딩 방법을 일관되게 능가하며, 생의학 신호에서 기준 사인파 절대 위치 인코딩과 비교하여 평균 9.1%의 상대적 향상을 달성하면서도 경쟁력 있는 계산 효율성을 유지함을 보여줍니다.

## 📝 요약

이 논문은 시계열 분석에서 기존의 위치 인코딩 방식이 신호의 특성을 무시하고 단순히 시퀀스 인덱스에 의존하는 문제를 해결하기 위해 Dynamic Wavelet Positional Encoding (DyWPE)을 제안합니다. DyWPE는 이산 웨이블릿 변환(DWT)을 사용하여 입력 시계열로부터 직접 위치 임베딩을 생성하는 신호 인식 프레임워크입니다. 10개의 다양한 시계열 데이터셋에서 실험한 결과, DyWPE는 기존의 8가지 최첨단 위치 인코딩 방법을 일관되게 능가했으며, 특히 생의학 신호에서 평균 9.1%의 상대적 성능 향상을 보였습니다. 또한, DyWPE는 경쟁력 있는 계산 효율성을 유지합니다.

## 🎯 주요 포인트

- 1. 기존의 위치 인코딩 방법은 신호의 특성을 무시하고 시퀀스 인덱스에만 의존하는 한계를 가지고 있다.

- 2. DyWPE는 입력 시계열 데이터로부터 이산 웨이블릿 변환(DWT)을 사용하여 위치 임베딩을 생성하는 새로운 신호 인식 프레임워크이다.

- 3. DyWPE는 10개의 다양한 시계열 데이터셋에서 기존의 최첨단 위치 인코딩 방법들을 일관되게 능가한다.

- 4. DyWPE는 생의학 신호에서 기준이 되는 사인파 절대 위치 인코딩 대비 평균 9.1%의 상대적 성능 향상을 달성한다.

- 5. DyWPE는 높은 계산 효율성을 유지하면서도 뛰어난 성능을 보인다.

---

*Generated on 2025-09-19 15:25:58*