# FlowCast-ODE: Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration

**Korean Title:** FlowCast-ODE: 동적 흐름 매칭 및 ODE 통합을 통한 연속 시간별 기상 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Shuangshuang He|Shuangshuang He]] [[authors/Yuanting Zhang|Yuanting Zhang]] [[authors/Hongli Liang|Hongli Liang]] [[authors/Qingye Meng|Qingye Meng]] [[authors/Xingyuan Yuan|Xingyuan Yuan]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Flow Matching

## 🔗 유사한 논문
- [[MeanFlowSE_ one-step generative speech enhancement via conditional mean flow_20250919|MeanFlowSE one-step generative speech enhancement via conditional mean flow]] (78.7% similar)
- [[Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (77.8% similar)
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (77.6% similar)
- [[Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (77.1% similar)
- [[FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive Energy Flow Field for End-to-End Autonomous Driving]] (76.7% similar)

## 📋 저자 정보

**Authors:** Shuangshuang He, Yuanting Zhang, Hongli Liang, Qingye Meng, Xingyuan Yuan

## 📄 Abstract (원문)

Accurate hourly weather forecasting is critical for numerous applications.
Recent deep learning models have demonstrated strong capability on 6-hour
intervals, yet achieving accurate and stable hourly predictions remains a
critical challenge. This is primarily due to the rapid accumulation of errors
in autoregressive rollouts and temporal discontinuities within the ERA5 data's
12-hour assimilation cycle. To address these issues, we propose FlowCast-ODE, a
framework that models atmospheric state evolution as a continuous flow.
FlowCast-ODE learns the conditional flow path directly from the previous state,
an approach that aligns more naturally with physical dynamic systems and
enables efficient computation. A coarse-to-fine strategy is introduced to train
the model on 6-hour data using dynamic flow matching and then refined on hourly
data that incorporates an Ordinary Differential Equation (ODE) solver to
achieve temporally coherent forecasts. In addition, a lightweight low-rank
AdaLN-Zero modulation mechanism is proposed and reduces model size by 15%
without compromising accuracy. Experiments demonstrate that FlowCast-ODE
outperforms strong baselines, yielding lower root mean square error (RMSE) and
better energy conservation, which reduces blurring and preserves more
fine-scale spatial details. It also shows comparable performance to the
state-of-the-art model in forecasting extreme events like typhoons.
Furthermore, the model alleviates temporal discontinuities associated with
assimilation cycle transitions.

## 🔍 Abstract (한글 번역)

정확한 시간별 기상 예보는 다양한 응용 분야에서 매우 중요합니다. 최근의 딥러닝 모델들은 6시간 간격에서 강력한 성능을 보여주었지만, 정확하고 안정적인 시간별 예측을 달성하는 것은 여전히 중요한 과제입니다. 이는 주로 자기회귀 전개에서의 오류의 급속한 누적과 ERA5 데이터의 12시간 동화 주기 내의 시간적 불연속성 때문입니다. 이러한 문제를 해결하기 위해, 우리는 대기 상태의 진화를 연속적인 흐름으로 모델링하는 프레임워크인 FlowCast-ODE를 제안합니다. FlowCast-ODE는 이전 상태로부터 조건부 흐름 경로를 직접 학습하며, 이는 물리적 동적 시스템과 더 자연스럽게 일치하고 효율적인 계산을 가능하게 합니다. 동적 흐름 매칭을 사용하여 6시간 데이터를 기반으로 모델을 훈련하고, 일반 미분 방정식(ODE) 해석기를 통합하여 시간적으로 일관된 예측을 달성하기 위해 시간별 데이터로 정제하는 거칠게-세밀하게 전략이 도입됩니다. 또한, 경량의 저순위 AdaLN-Zero 변조 메커니즘이 제안되어 정확성을 손상시키지 않으면서 모델 크기를 15% 줄입니다. 실험 결과 FlowCast-ODE는 강력한 기준 모델들을 능가하여 더 낮은 평균 제곱근 오차(RMSE)와 더 나은 에너지 보존을 보여주며, 이는 흐림을 줄이고 더 많은 세밀한 공간적 세부 사항을 보존합니다. 또한, 태풍과 같은 극한 사건 예측에서 최첨단 모델과 비교할 만한 성능을 보입니다. 더 나아가, 모델은 동화 주기 전환과 관련된 시간적 불연속성을 완화합니다.

## 📝 요약

FlowCast-ODE는 시간별 기상 예측의 정확성과 안정성을 높이기 위해 제안된 프레임워크로, 대기 상태의 변화를 연속적인 흐름으로 모델링합니다. 이 방법은 이전 상태에서 조건부 흐름 경로를 학습하여 물리적 동적 시스템과 자연스럽게 일치하며 효율적인 계산을 가능하게 합니다. 6시간 간격의 데이터를 동적 흐름 매칭으로 학습하고, ODE 해석기를 사용하여 시간적 일관성을 유지하며 시간별 데이터를 정교화하는 전략을 채택했습니다. 또한, 모델 크기를 15% 줄이면서도 정확성을 유지하는 경량화된 AdaLN-Zero 조정 메커니즘을 도입했습니다. 실험 결과, FlowCast-ODE는 기존 모델보다 낮은 RMSE와 더 나은 에너지 보존을 통해 흐림을 줄이고 세부 공간 정보를 보존하며, 태풍과 같은 극한 사건 예측에서도 최첨단 모델과 유사한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. FlowCast-ODE는 대기 상태의 변화를 연속적인 흐름으로 모델링하여 시간별 기상 예측의 정확성과 안정성을 개선합니다.

- 2. 6시간 데이터를 동적 흐름 매칭으로 학습한 후, ODE 솔버를 사용하여 시간별 데이터를 정교화하는 방법을 제안합니다.

- 3. 경량 저랭크 AdaLN-Zero 변조 메커니즘을 통해 모델 크기를 15% 줄이면서도 정확성을 유지합니다.

- 4. FlowCast-ODE는 RMSE를 낮추고 에너지 보존을 개선하여 흐림을 줄이고 세밀한 공간적 세부 사항을 보존합니다.

- 5. 이 모델은 극한 기상 현상 예측에서도 최첨단 모델과 유사한 성능을 보이며, 동화 주기 전환과 관련된 시간적 불연속성을 완화합니다.

---

*Generated on 2025-09-20 05:42:01*