# DeepMech: A Machine Learning Framework for Chemical Reaction Mechanism Prediction

**Korean Title:** 딥메크: 화학 반응 메커니즘 예측을 위한 머신 러닝 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretable Graph-based Framework

## 🔗 유사한 논문
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (79.1% similar)
- [[2025-09-22/Monte Carlo Tree Diffusion with Multiple Experts for Protein Design_20250922|Monte Carlo Tree Diffusion with Multiple Experts for Protein Design]] (78.9% similar)
- [[2025-09-18/Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (78.0% similar)
- [[2025-09-19/MolmoAct_ Action Reasoning Models that can Reason in Space_20250919|MolmoAct Action Reasoning Models that can Reason in Space]] (77.6% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (77.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15872v1 Announce Type: cross 
Abstract: Prediction of complete step-by-step chemical reaction mechanisms (CRMs) remains a major challenge. Whereas the traditional approaches in CRM tasks rely on expert-driven experiments or costly quantum chemical computations, contemporary deep learning (DL) alternatives ignore key intermediates and mechanistic steps and often suffer from hallucinations. We present DeepMech, an interpretable graph-based DL framework employing atom- and bond-level attention, guided by generalized templates of mechanistic operations (TMOps), to generate CRMs. Trained on our curated ReactMech dataset (~30K CRMs with 100K atom-mapped and mass-balanced elementary steps), DeepMech achieves 98.98+/-0.12% accuracy in predicting elementary steps and 95.94+/-0.21% in complete CRM tasks, besides maintaining high fidelity even in out-of-distribution scenarios as well as in predicting side and/or byproducts. Extension to multistep CRMs relevant to prebiotic chemistry, demonstrates the ability of DeepMech in effectively reconstructing pathways from simple primordial substrates to complex biomolecules such as serine and aldopentose. Attention analysis identifies reactive atoms/bonds in line with chemical intuition, rendering our model interpretable and suitable for reaction design.

## 🔍 Abstract (한글 번역)

arXiv:2509.15872v1 발표 유형: 교차  
초록: 완전한 단계별 화학 반응 메커니즘(CRMs)의 예측은 여전히 주요 과제로 남아 있습니다. CRM 작업에서 전통적인 접근 방식은 전문가 주도의 실험이나 비용이 많이 드는 양자 화학 계산에 의존하는 반면, 현대의 딥 러닝(DL) 대안은 주요 중간체와 메커니즘 단계를 무시하고 종종 환각 문제를 겪습니다. 우리는 DeepMech를 소개합니다. 이는 원자 및 결합 수준의 주의를 기울이며 메커니즘 작용의 일반화된 템플릿(TMOps)에 의해 안내되는 해석 가능한 그래프 기반 DL 프레임워크로, CRMs을 생성합니다. 우리가 큐레이션한 ReactMech 데이터셋(~30K CRMs, 100K 원자 매핑 및 질량 균형이 맞는 기본 단계 포함)으로 학습된 DeepMech는 기본 단계 예측에서 98.98+/-0.12%의 정확도와 완전한 CRM 작업에서 95.94+/-0.21%의 정확도를 달성하며, 분포 외 시나리오에서도 높은 충실도를 유지하고 부작용 및/또는 부산물 예측에서도 높은 성능을 보입니다. 원시 화학과 관련된 다단계 CRMs으로의 확장은 DeepMech가 단순한 원시 기질에서 세린 및 알도펜토스와 같은 복잡한 생체 분자로의 경로를 효과적으로 재구성할 수 있는 능력을 보여줍니다. 주의 분석은 화학적 직관과 일치하는 반응성 원자/결합을 식별하여, 우리의 모델을 해석 가능하고 반응 설계에 적합하게 만듭니다.

## 📝 요약

DeepMech는 화학 반응 메커니즘(CRM)을 예측하는 해석 가능한 그래프 기반 딥러닝 프레임워크입니다. 이 모델은 원자 및 결합 수준의 주의를 활용하고, 일반화된 메커니즘 작업 템플릿(TMOps)을 통해 CRM을 생성합니다. ReactMech 데이터셋으로 학습된 DeepMech는 기본 단계 예측에서 98.98%의 정확도를, 전체 CRM 작업에서 95.94%의 정확도를 달성했습니다. 또한, 분포 외 시나리오와 부/부산물 예측에서도 높은 충실도를 유지합니다. DeepMech는 원시 기질에서 복잡한 생체 분자까지의 경로를 효과적으로 재구성하며, 주의 분석을 통해 반응성 원자/결합을 식별하여 모델의 해석 가능성을 높입니다.

## 🎯 주요 포인트

- 1. DeepMech는 원자 및 결합 수준의 주의를 활용하여 화학 반응 메커니즘(CRMs)을 생성하는 해석 가능한 그래프 기반 딥러닝 프레임워크입니다.

- 2. ReactMech 데이터셋으로 훈련된 DeepMech는 기본 단계 예측에서 98.98% 이상의 정확도를, 전체 CRM 작업에서 95.94% 이상의 정확도를 달성했습니다.

- 3. DeepMech는 분포 외 시나리오에서도 높은 충실도를 유지하며, 부제품 및 부산물 예측에서도 우수한 성능을 보입니다.

- 4. DeepMech는 단순한 원시 기질에서 복잡한 생체 분자까지의 경로를 효과적으로 재구성하여 전생물학적 화학에 관련된 다단계 CRM으로 확장 가능합니다.

- 5. 주의 분석을 통해 반응성 원자/결합을 식별하여 모델의 해석 가능성을 높이고, 반응 설계에 적합합니다.

---

*Generated on 2025-09-22 14:14:18*