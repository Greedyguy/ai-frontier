# DPANet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting

**Korean Title:** DPANet: 다변량 시계열 예측을 위한 이중 피라미드 주의 네트워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Qianyang Li|Qianyang Li]] [[authors/Xingjun Zhang|Xingjun Zhang]] [[authors/Shaoxun Wang|Shaoxun Wang]] [[authors/Jia Wei|Jia Wei]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interactive Fusion Block

## 🔗 유사한 논문
- [[Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (76.8% similar)
- [[Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (76.7% similar)
- [[TableDART_ Dynamic Adaptive Multi-Modal Routing for Table Understanding_20250919|TableDART Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (76.3% similar)
- [[Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (76.1% similar)
- [[Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (75.9% similar)

## 📋 저자 정보

**Authors:** Qianyang Li, Xingjun Zhang, Shaoxun Wang, Jia Wei

## 📄 Abstract (원문)

We conducted rigorous ablation studies to validate DPANet's key components
(Table \ref{tab:ablation-study}). The full model consistently outperforms all
variants. To test our dual-domain hypothesis, we designed two specialized
versions: a Temporal-Only model (fusing two identical temporal pyramids) and a
Frequency-Only model (fusing two spectral pyramids). Both variants
underperformed significantly, confirming that the fusion of heterogeneous
temporal and frequency information is critical. Furthermore, replacing the
cross-attention mechanism with a simpler method (w/o Cross-Fusion) caused the
most severe performance degradation. This result underscores that our
interactive fusion block is the most essential component.

## 🔍 Abstract (한글 번역)

엄밀한 소거 연구를 통해 DPANet의 주요 구성 요소를 검증했습니다(표 \ref{tab:ablation-study}). 전체 모델은 모든 변형 모델을 일관되게 능가했습니다. 이중 도메인 가설을 테스트하기 위해 두 가지 특수 버전을 설계했습니다: 시간 전용 모델(두 개의 동일한 시간 피라미드를 융합)과 주파수 전용 모델(두 개의 스펙트럼 피라미드를 융합). 두 변형 모델 모두 성능이 크게 떨어졌으며, 이로 인해 이질적인 시간 및 주파수 정보의 융합이 중요하다는 것이 확인되었습니다. 또한, 교차 주의 메커니즘을 더 단순한 방법으로 대체한 경우(교차 융합 없음) 가장 심각한 성능 저하가 발생했습니다. 이 결과는 우리의 상호 융합 블록이 가장 필수적인 구성 요소임을 강조합니다.

## 📝 요약

DPANet의 주요 구성 요소를 검증하기 위해 철저한 소거 연구를 수행했습니다. 전체 모델은 모든 변형 모델보다 일관되게 우수한 성능을 보였습니다. 이중 도메인 가설을 테스트하기 위해 Temporal-Only 모델과 Frequency-Only 모델을 설계했으나, 두 모델 모두 성능이 크게 저하되어 이질적인 시간 및 주파수 정보의 융합이 중요함을 확인했습니다. 또한, 교차 주의 메커니즘을 단순한 방법으로 대체했을 때 성능이 가장 크게 저하되었으며, 이는 상호작용 융합 블록이 가장 중요한 구성 요소임을 강조합니다.

## 🎯 주요 포인트

- 1. DPANet의 전체 모델은 모든 변형 모델보다 일관되게 우수한 성능을 보입니다.

- 2. 이중 도메인 가설을 검증하기 위해 설계된 Temporal-Only 모델과 Frequency-Only 모델은 모두 성능이 저하되었습니다.

- 3. 이질적인 시간 및 주파수 정보의 융합이 중요하다는 것이 확인되었습니다.

- 4. 교차 주의 메커니즘을 단순한 방법으로 대체했을 때 성능이 가장 크게 저하되었습니다.

- 5. 상호작용 융합 블록이 DPANet의 가장 중요한 구성 요소임이 강조되었습니다.

---

*Generated on 2025-09-20 02:46:03*