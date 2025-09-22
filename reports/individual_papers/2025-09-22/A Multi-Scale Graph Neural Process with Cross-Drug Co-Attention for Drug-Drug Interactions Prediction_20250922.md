# A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction

**Korean Title:** 다중 스케일 그래프 신경 프로세스와 교차 약물 공동 주의 메커니즘을 통한 약물 상호작용 예측

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-scale Graph Representation

## 🔗 유사한 논문
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (83.0% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (77.8% similar)
- [[2025-09-19/DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (77.7% similar)
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (77.4% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (77.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15256v1 Announce Type: cross 
Abstract: Accurate prediction of drug-drug interactions (DDI) is crucial for medication safety and effective drug development. However, existing methods often struggle to capture structural information across different scales, from local functional groups to global molecular topology, and typically lack mechanisms to quantify prediction confidence. To address these limitations, we propose MPNP-DDI, a novel Multi-scale Graph Neural Process framework. The core of MPNP-DDI is a unique message-passing scheme that, by being iteratively applied, learns a hierarchy of graph representations at multiple scales. Crucially, a cross-drug co-attention mechanism then dynamically fuses these multi-scale representations to generate context-aware embeddings for interacting drug pairs, while an integrated neural process module provides principled uncertainty estimation. Extensive experiments demonstrate that MPNP-DDI significantly outperforms state-of-the-art baselines on benchmark datasets. By providing accurate, generalizable, and uncertainty-aware predictions built upon multi-scale structural features, MPNP-DDI represents a powerful computational tool for pharmacovigilance, polypharmacy risk assessment, and precision medicine.

## 🔍 Abstract (한글 번역)

arXiv:2509.15256v1 발표 유형: 교차  
초록: 약물 상호작용(DDI)의 정확한 예측은 약물 안전성과 효과적인 약물 개발에 필수적입니다. 그러나 기존 방법들은 종종 국소 기능 그룹에서 전역 분자 위상에 이르는 다양한 규모의 구조적 정보를 포착하는 데 어려움을 겪으며, 예측 신뢰도를 정량화할 수 있는 메커니즘이 부족한 경우가 많습니다. 이러한 한계를 극복하기 위해, 우리는 MPNP-DDI라는 새로운 다중 규모 그래프 신경 프로세스 프레임워크를 제안합니다. MPNP-DDI의 핵심은 독특한 메시지 전달 방식으로, 이를 반복적으로 적용하여 여러 규모에서 그래프 표현의 계층 구조를 학습합니다. 중요한 것은, 교차 약물 공동 주의 메커니즘이 이러한 다중 규모 표현을 동적으로 융합하여 상호작용하는 약물 쌍에 대한 맥락 인식 임베딩을 생성하며, 통합된 신경 프로세스 모듈이 원칙적인 불확실성 추정을 제공합니다. 광범위한 실험 결과, MPNP-DDI가 벤치마크 데이터셋에서 최첨단 기준을 크게 능가함을 보여줍니다. 다중 규모 구조적 특징에 기반한 정확하고 일반화 가능하며 불확실성을 인식하는 예측을 제공함으로써, MPNP-DDI는 약물 감시, 다약제 위험 평가, 정밀 의학을 위한 강력한 계산 도구를 나타냅니다.

## 📝 요약

이 논문은 약물 간 상호작용(DDI) 예측의 정확성을 높이기 위해 MPNP-DDI라는 새로운 다중 스케일 그래프 신경 프로세스 프레임워크를 제안합니다. MPNP-DDI는 독특한 메시지 전달 방식을 통해 다양한 스케일에서 그래프 표현을 학습하며, 교차 약물 공동 주의 메커니즘을 통해 문맥 인식 임베딩을 생성합니다. 또한, 통합된 신경 프로세스 모듈로 예측의 불확실성을 정량화합니다. 실험 결과, MPNP-DDI는 기존 방법들보다 뛰어난 성능을 보였으며, 약물 감시, 다약제 위험 평가, 정밀 의학에 유용한 도구로 활용될 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. MPNP-DDI는 약물 상호작용 예측을 위해 다중 스케일 그래프 신경 프로세스 프레임워크를 제안합니다.

- 2. 이 프레임워크는 메시지 전달 방식을 통해 다양한 스케일의 그래프 표현을 학습합니다.

- 3. 교차 약물 공동 주의 메커니즘을 통해 다중 스케일 표현을 동적으로 융합하여 문맥 인식 임베딩을 생성합니다.

- 4. 통합된 신경 프로세스 모듈은 예측의 불확실성을 정량화하는 기능을 제공합니다.

- 5. MPNP-DDI는 벤치마크 데이터셋에서 최첨단 기준을 능가하는 성능을 보이며, 약물 감시 및 정밀 의학에 유용한 도구로 자리 잡습니다.

---

*Generated on 2025-09-22 13:50:13*