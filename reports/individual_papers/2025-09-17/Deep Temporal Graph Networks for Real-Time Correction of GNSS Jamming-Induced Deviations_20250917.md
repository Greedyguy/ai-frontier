---
keywords:
  - Graph Neural Networks
  - GNSS Jamming
  - Heterogeneous Graph ConvLSTM
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:56:58.565832",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "GNSS Jamming",
    "Heterogeneous Graph ConvLSTM"
  ],
  "rejected_keywords": [
    "Real-Time Correction"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.82,
    "GNSS Jamming": 0.78,
    "Heterogeneous Graph ConvLSTM": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations

**Korean Title:** 깊은 시간 그래프 네트워크를 통한 GNSS 재밍 유발 편차의 실시간 수정

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Deep Temporal Graph Networks]]
**⚡ Unique Technical**: [[keywords/GNSS Jamming|GNSS Jamming]], [[keywords/Heterogeneous Graph ConvLSTM|Heterogeneous Graph ConvLSTM]]

## 🔗 유사한 논문
- [[Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter_20250919|Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter]] (80.2% similar)
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (79.4% similar)
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (79.3% similar)
- [[Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (79.1% similar)
- [[Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (78.6% similar)

## 📋 저자 정보

**Authors:** Ivana Kesić, Aljaž Blatnik, Carolina Fortuna, Blaž Bertalanič

## 📄 Abstract (원문)

Global Navigation Satellite Systems (GNSS) are increasingly disrupted by
intentional jamming, degrading availability precisely when positioning and
timing must remain operational. We address this by reframing jamming mitigation
as dynamic graph regression and introducing a receiver-centric deep temporal
graph network that predicts, and thus corrects, the receivers horizontal
deviation in real time. At each 1 Hz epoch, the satellite receiver environment
is represented as a heterogeneous star graph (receiver center, tracked
satellites as leaves) with time varying attributes (e.g., SNR, azimuth,
elevation, latitude/longitude). A single layer Heterogeneous Graph ConvLSTM
(HeteroGCLSTM) aggregates one hop spatial context and temporal dynamics over a
short history to output the 2D deviation vector applied for on the fly
correction.
  We evaluate on datasets from two distinct receivers under three jammer
profiles, continuous wave (cw), triple tone (cw3), and wideband FM, each
exercised at six power levels between -45 and -70 dBm, with 50 repetitions per
scenario (prejam/jam/recovery). Against strong multivariate time series
baselines (MLP, uniform CNN, and Seq2Point CNN), our model consistently attains
the lowest mean absolute error (MAE). At -45 dBm, it achieves 3.64 cm
(GP01/cw), 7.74 cm (GP01/cw3), 4.41 cm (ublox/cw), 4.84 cm (ublox/cw3), and
4.82 cm (ublox/FM), improving to 1.65-2.08 cm by -60 to -70 dBm. On mixed mode
datasets pooling all powers, MAE is 3.78 cm (GP01) and 4.25 cm (ublox10),
outperforming Seq2Point, MLP, and CNN. A split study shows superior data
efficiency: with only 10\% training data our approach remains well ahead of
baselines (20 cm vs. 36-42 cm).

## 🔍 Abstract (한글 번역)

글로벌 내비게이션 위성 시스템(GNSS)은 의도적인 재밍으로 인해 점점 더 많은 방해를 받고 있으며, 위치 및 타이밍이 운영적으로 유지되어야 할 때 가용성이 저하되고 있습니다. 우리는 재밍 완화를 동적 그래프 회귀로 재구성하고, 수신기 중심의 심층 시계열 그래프 네트워크를 도입하여 수신기의 수평 편차를 실시간으로 예측하고 수정합니다. 각 1 Hz 에포크에서 위성 수신기 환경은 이질적인 스타 그래프(수신기 중심, 추적 위성은 잎으로)로 표현되며, 시간에 따라 변하는 속성(예: SNR, 방위각, 고도, 위도/경도)을 가집니다. 단일 계층 이질 그래프 ConvLSTM(HeteroGCLSTM)은 짧은 과거에 대한 1홉 공간 컨텍스트와 시간적 역학을 집계하여 실시간 수정에 적용되는 2D 편차 벡터를 출력합니다.

우리는 두 개의 서로 다른 수신기에서 세 가지 재머 프로파일(연속파(cw), 트리플 톤(cw3), 광대역 FM)에 대해 각 시나리오(재밍 전/재밍/복구)에서 50회 반복하여 -45에서 -70 dBm 사이의 여섯 가지 전력 수준에서 평가합니다. 강력한 다변량 시계열 기준선(MLP, 균일 CNN, Seq2Point CNN)과 비교하여, 우리 모델은 일관되게 가장 낮은 평균 절대 오차(MAE)를 달성합니다. -45 dBm에서, 3.64 cm(GP01/cw), 7.74 cm(GP01/cw3), 4.41 cm(ublox/cw), 4.84 cm(ublox/cw3), 4.82 cm(ublox/FM)를 달성하며, -60에서 -70 dBm으로 개선되어 1.65-2.08 cm에 도달합니다. 모든 전력을 통합한 혼합 모드 데이터셋에서는 MAE가 3.78 cm(GP01) 및 4.25 cm(ublox10)로, Seq2Point, MLP, CNN을 능가합니다. 분할 연구는 우수한 데이터 효율성을 보여줍니다: 훈련 데이터의 10%만으로도 우리의 접근법은 여전히 기준선을 크게 앞서고 있습니다(20 cm 대 36-42 cm).

## 📝 요약

이 논문은 의도적인 전파 방해로 인해 GNSS의 가용성이 저하되는 문제를 해결하기 위해, 방해 완화를 동적 그래프 회귀 문제로 재구성하고 수신기 중심의 심층 시계열 그래프 네트워크를 제안합니다. 이 네트워크는 수신기의 수평 편차를 실시간으로 예측하고 보정합니다. 위성 수신기 환경을 이종 스타 그래프로 모델링하고, Heterogeneous Graph ConvLSTM을 사용하여 공간적 맥락과 시간적 동역학을 통합하여 2D 편차 벡터를 출력합니다. 두 개의 수신기와 세 가지 방해 프로파일을 사용한 실험에서, 제안된 모델은 기존의 다변량 시계열 모델들보다 낮은 평균 절대 오차(MAE)를 기록했습니다. 특히, -45 dBm에서 3.64 cm에서 -60 dBm 이하에서 1.65-2.08 cm까지 성능이 향상되었으며, 데이터 효율성에서도 우수한 성과를 보였습니다.

## 🎯 주요 포인트

- 1. GNSS는 의도적인 재밍으로 인해 점점 더 많은 방해를 받고 있으며, 이는 위치 및 타이밍이 중요한 시점에서 가용성을 저하시킵니다.

- 2. 본 연구에서는 재밍 완화를 동적 그래프 회귀로 재구성하고, 수신기 중심의 심층 시계열 그래프 네트워크를 도입하여 수신기의 수평 편차를 실시간으로 예측 및 수정합니다.

- 3. 이 네트워크는 이질적인 스타 그래프로 위성 수신기 환경을 표현하고, Heterogeneous Graph ConvLSTM을 사용하여 공간적 맥락과 시간적 동역학을 결합하여 2D 편차 벡터를 출력합니다.

- 4. 다양한 재머 프로파일과 전력 수준에서의 평가 결과, 본 모델은 강력한 다변량 시계열 기준 모델들보다 일관되게 낮은 평균 절대 오차(MAE)를 달성했습니다.

- 5. 혼합 모드 데이터셋에서도 본 모델은 Seq2Point, MLP, CNN을 능가하며, 10%의 훈련 데이터만으로도 뛰어난 데이터 효율성을 보여줍니다.

---

*Generated on 2025-09-20 09:20:30*