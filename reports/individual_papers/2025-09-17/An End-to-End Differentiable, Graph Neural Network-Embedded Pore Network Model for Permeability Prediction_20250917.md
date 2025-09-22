# An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction

**Korean Title:** 종단간 미분 가능한 그래프 신경망 내장 기공 네트워크 모델을 통한 투과성 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Qingqi Zhao|Qingqi Zhao]] [[authors/Heng Xiao|Heng Xiao]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: End-to-End Differentiable Framework

## 🔗 유사한 논문
- [[A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation Architectural Considerations and Performance Evaluation]] (82.1% similar)
- [[Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (81.0% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (80.3% similar)
- [[Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (80.1% similar)
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (80.1% similar)

## 📋 저자 정보

**Authors:** Qingqi Zhao, Heng Xiao

## 📄 Abstract (원문)

Accurate prediction of permeability in porous media is essential for modeling
subsurface flow. While pure data-driven models offer computational efficiency,
they often lack generalization across scales and do not incorporate explicit
physical constraints. Pore network models (PNMs), on the other hand, are
physics-based and efficient but rely on idealized geometric assumptions to
estimate pore-scale hydraulic conductance, limiting their accuracy in complex
structures. To overcome these limitations, we present an end-to-end
differentiable hybrid framework that embeds a graph neural network (GNN) into a
PNM. In this framework, the analytical formulas used for conductance
calculations are replaced by GNN-based predictions derived from pore and throat
features. The predicted conductances are then passed to the PNM solver for
permeability computation. In this way, the model avoids the idealized geometric
assumptions of PNM while preserving the physics-based flow calculations. The
GNN is trained without requiring labeled conductance data, which can number in
the thousands per pore network; instead, it learns conductance values by using
a single scalar permeability as the training target. This is made possible by
backpropagating gradients through both the GNN (via automatic differentiation)
and the PNM solver (via a discrete adjoint method), enabling fully coupled,
end-to-end training. The resulting model achieves high accuracy and generalizes
well across different scales, outperforming both pure data-driven and
traditional PNM approaches. Gradient-based sensitivity analysis further reveals
physically consistent feature influences, enhancing model interpretability.
This approach offers a scalable and physically informed framework for
permeability prediction in complex porous media, reducing model uncertainty and
improving accuracy.

## 🔍 Abstract (한글 번역)

다음 텍스트를 한국어로 번역하겠습니다. 학문적 어조와 기술 용어를 적절히 유지하겠습니다.

다공성 매체에서의 투과성 예측은 지하 흐름 모델링에 필수적입니다. 순수 데이터 기반 모델은 계산 효율성을 제공하지만, 종종 규모에 따른 일반화가 부족하고 명시적인 물리적 제약을 포함하지 않습니다. 반면에 기공 네트워크 모델(PNM)은 물리 기반이며 효율적이지만, 이상화된 기하학적 가정에 의존하여 기공 규모의 수리 전도도를 추정하므로 복잡한 구조에서 정확성이 제한됩니다. 이러한 한계를 극복하기 위해, 우리는 그래프 신경망(GNN)을 PNM에 통합한 종단 간 미분 가능한 하이브리드 프레임워크를 제시합니다. 이 프레임워크에서는 전도도 계산에 사용되는 분석적 공식을 기공 및 목구멍 특징에서 파생된 GNN 기반 예측으로 대체합니다. 예측된 전도도는 PNM 해석기에 전달되어 투과성을 계산합니다. 이 방식으로 모델은 PNM의 이상화된 기하학적 가정을 피하면서 물리 기반의 흐름 계산을 유지합니다. GNN은 수천 개의 기공 네트워크당 전도도 데이터에 대한 라벨이 필요 없이 훈련되며, 대신 단일 스칼라 투과성을 훈련 목표로 사용하여 전도도 값을 학습합니다. 이는 GNN(자동 미분을 통해)과 PNM 해석기(이산 수반 방법을 통해)를 통해 그래디언트를 역전파함으로써 가능하며, 완전히 결합된 종단 간 훈련을 가능하게 합니다. 결과 모델은 높은 정확성을 달성하고 다양한 규모에 걸쳐 잘 일반화되며, 순수 데이터 기반 및 전통적 PNM 접근법보다 우수한 성능을 보입니다. 그래디언트 기반 민감도 분석은 물리적으로 일관된 특징 영향을 드러내어 모델 해석 가능성을 향상시킵니다. 이 접근법은 복잡한 다공성 매체에서의 투과성 예측을 위한 확장 가능하고 물리적으로 정보에 근거한 프레임워크를 제공하여 모델 불확실성을 줄이고 정확성을 향상시킵니다.

## 📝 요약

이 논문은 복잡한 다공성 매체에서의 투과성을 예측하기 위해 그래프 신경망(GNN)을 포어 네트워크 모델(PNM)에 통합한 하이브리드 프레임워크를 제안합니다. 이 모델은 PNM의 이상적인 기하학적 가정을 피하면서 물리 기반의 흐름 계산을 유지합니다. GNN은 수천 개의 라벨이 필요 없이 단일 스칼라 투과성을 학습 목표로 사용하여 학습됩니다. 이 방법은 다양한 규모에서 높은 정확도를 보이며, 순수 데이터 기반 모델과 전통적인 PNM을 능가합니다. 또한, 민감도 분석을 통해 물리적으로 일관된 특징의 영향을 밝혀내어 모델의 해석 가능성을 높입니다. 이 접근법은 복잡한 다공성 매체에서 투과성 예측의 정확성을 향상시키고 모델의 불확실성을 줄이는 데 기여합니다.

## 🎯 주요 포인트

- 1. 본 연구는 그래프 신경망(GNN)을 기공망 모델(PNM)에 통합한 하이브리드 프레임워크를 제안하여 다공성 매체의 투과성을 예측합니다.

- 2. GNN 기반 예측을 통해 이상화된 기하학적 가정을 피하면서 물리 기반의 흐름 계산을 유지합니다.

- 3. GNN은 수천 개의 라벨이 필요하지 않으며, 단일 스칼라 투과성을 학습 목표로 사용하여 학습됩니다.

- 4. 제안된 모델은 순수 데이터 기반 및 전통적인 PNM 접근법을 능가하며 다양한 규모에 걸쳐 높은 정확성과 일반화를 달성합니다.

- 5. 그래디언트 기반 민감도 분석을 통해 물리적으로 일관된 특징의 영향을 밝혀내어 모델 해석 가능성을 높입니다.

---

*Generated on 2025-09-20 09:30:10*