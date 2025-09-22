# Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation

**Korean Title:** 깊이에 대한 조명: 단안 깊이 추정에서의 설명 가능성 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Explainability in Monocular Depth Estimation

## 🔗 유사한 논문
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (83.1% similar)
- [[2025-09-22/Generating Part-Based Global Explanations Via Correspondence_20250922|Generating Part-Based Global Explanations Via Correspondence]] (81.5% similar)
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (80.4% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (80.3% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15980v1 Announce Type: cross 
Abstract: Explainable artificial intelligence is increasingly employed to understand the decision-making process of deep learning models and create trustworthiness in their adoption. However, the explainability of Monocular Depth Estimation (MDE) remains largely unexplored despite its wide deployment in real-world applications. In this work, we study how to analyze MDE networks to map the input image to the predicted depth map. More in detail, we investigate well-established feature attribution methods, Saliency Maps, Integrated Gradients, and Attention Rollout on different computationally complex models for MDE: METER, a lightweight network, and PixelFormer, a deep network. We assess the quality of the generated visual explanations by selectively perturbing the most relevant and irrelevant pixels, as identified by the explainability methods, and analyzing the impact of these perturbations on the model's output. Moreover, since existing evaluation metrics can have some limitations in measuring the validity of visual explanations for MDE, we additionally introduce the Attribution Fidelity. This metric evaluates the reliability of the feature attribution by assessing their consistency with the predicted depth map. Experimental results demonstrate that Saliency Maps and Integrated Gradients have good performance in highlighting the most important input features for MDE lightweight and deep models, respectively. Furthermore, we show that Attribution Fidelity effectively identifies whether an explainability method fails to produce reliable visual maps, even in scenarios where conventional metrics might suggest satisfactory results.

## 🔍 Abstract (한글 번역)

arXiv:2509.15980v1 발표 유형: 교차  
초록: 설명 가능한 인공지능은 심층 학습 모델의 의사 결정 과정을 이해하고 그 채택에 대한 신뢰성을 구축하기 위해 점점 더 많이 사용되고 있습니다. 그러나 단안 깊이 추정(Monocular Depth Estimation, MDE)의 설명 가능성은 실제 응용 프로그램에서 널리 사용됨에도 불구하고 크게 탐구되지 않았습니다. 본 연구에서는 입력 이미지를 예측된 깊이 맵으로 매핑하기 위해 MDE 네트워크를 분석하는 방법을 연구합니다. 자세히 살펴보면, MDE의 다양한 계산 복잡한 모델인 경량 네트워크 METER와 심층 네트워크 PixelFormer에 대해 잘 확립된 특징 귀속 방법, Saliency Maps, Integrated Gradients, Attention Rollout을 조사합니다. 설명 가능성 방법에 의해 식별된 가장 관련 있는 픽셀과 관련 없는 픽셀을 선택적으로 변형하고 이러한 변형이 모델 출력에 미치는 영향을 분석하여 생성된 시각적 설명의 품질을 평가합니다. 또한, 기존 평가 지표가 MDE에 대한 시각적 설명의 타당성을 측정하는 데 일부 제한이 있을 수 있으므로, 우리는 추가적으로 귀속 충실도(Attribution Fidelity)를 도입합니다. 이 지표는 예측된 깊이 맵과의 일관성을 평가하여 특징 귀속의 신뢰성을 평가합니다. 실험 결과는 Saliency Maps와 Integrated Gradients가 각각 MDE 경량 및 심층 모델에 가장 중요한 입력 특징을 강조하는 데 있어 좋은 성능을 보임을 보여줍니다. 더욱이, 귀속 충실도는 기존의 지표가 만족스러운 결과를 제시할 수 있는 시나리오에서도 설명 가능성 방법이 신뢰할 수 있는 시각적 맵을 생성하지 못하는지를 효과적으로 식별함을 보여줍니다.

## 📝 요약

이 논문은 단안 깊이 추정(MDE)의 설명 가능성을 연구하여, 입력 이미지와 예측된 깊이 맵 간의 관계를 분석하는 방법을 제시합니다. MDE 네트워크에 대한 설명 가능성을 높이기 위해 Saliency Maps, Integrated Gradients, Attention Rollout 등의 특징 귀속 방법을 사용하여 METER와 PixelFormer 모델을 분석합니다. 생성된 시각적 설명의 품질을 평가하기 위해 가장 관련 있는 픽셀과 관련 없는 픽셀을 선택적으로 변형하고, 이러한 변형이 모델 출력에 미치는 영향을 분석합니다. 또한, 기존 평가 지표의 한계를 보완하기 위해 Attribution Fidelity라는 새로운 지표를 도입하여, 예측된 깊이 맵과의 일관성을 통해 특징 귀속의 신뢰성을 평가합니다. 실험 결과, Saliency Maps와 Integrated Gradients가 각각 경량 및 심층 MDE 모델에서 중요한 입력 특징을 효과적으로 강조하는 것을 보여주며, Attribution Fidelity는 기존 지표가 만족스러운 결과를 제시하는 상황에서도 설명 가능성 방법이 신뢰할 수 없는 시각적 맵을 생성하는지를 효과적으로 식별합니다.

## 🎯 주요 포인트

- 1. 설명 가능한 인공지능은 심층 학습 모델의 의사결정 과정을 이해하고 신뢰성을 높이기 위해 점점 더 많이 사용되고 있습니다.

- 2. 단안 깊이 추정(MDE)의 설명 가능성은 실세계 응용에서의 광범위한 사용에도 불구하고 거의 탐구되지 않았습니다.

- 3. 본 연구에서는 MDE 네트워크를 분석하여 입력 이미지와 예측된 깊이 맵 간의 관계를 매핑하는 방법을 연구합니다.

- 4. 설명 가능성 방법으로 식별된 가장 관련 있는 픽셀과 관련 없는 픽셀을 선택적으로 변형하여 시각적 설명의 품질을 평가합니다.

- 5. 기존 평가 지표의 한계를 보완하기 위해 설명 가능성 방법의 신뢰성을 평가하는 'Attribution Fidelity'라는 새로운 지표를 도입하였습니다.

---

*Generated on 2025-09-22 14:20:38*