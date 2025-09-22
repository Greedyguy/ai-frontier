# Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture

**Korean Title:** 이미지 및 임상 시그니처의 자가 지도 학습을 위한 다중 모달 공동 임베딩 예측 아키텍처

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unlabeled Multimodal Archives

## 🔗 유사한 논문
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (83.7% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (81.9% similar)
- [[2025-09-18/Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (81.9% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (81.8% similar)
- [[2025-09-22/Deep learning and abstractive summarisation for radiological reports_ an empirical study for adapting the PEGASUS models' family with scarce data_20250922|Deep learning and abstractive summarisation for radiological reports an empirical study for adapting the PEGASUS models' family with scarce data]] (81.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15470v1 Announce Type: cross 
Abstract: The development of multimodal models for pulmonary nodule diagnosis is limited by the scarcity of labeled data and the tendency for these models to overfit on the training distribution. In this work, we leverage self-supervised learning from longitudinal and multimodal archives to address these challenges. We curate an unlabeled set of patients with CT scans and linked electronic health records from our home institution to power joint embedding predictive architecture (JEPA) pretraining. After supervised finetuning, we show that our approach outperforms an unregularized multimodal model and imaging-only model in an internal cohort (ours: 0.91, multimodal: 0.88, imaging-only: 0.73 AUC), but underperforms in an external cohort (ours: 0.72, imaging-only: 0.75 AUC). We develop a synthetic environment that characterizes the context in which JEPA may underperform. This work innovates an approach that leverages unlabeled multimodal medical archives to improve predictive models and demonstrates its advantages and limitations in pulmonary nodule diagnosis.

## 🔍 Abstract (한글 번역)

arXiv:2509.15470v1 발표 유형: 교차  
초록: 폐 결절 진단을 위한 다중 모달 모델의 개발은 라벨이 붙은 데이터의 부족과 이러한 모델이 훈련 분포에 과적합되는 경향으로 인해 제한됩니다. 본 연구에서는 이러한 문제를 해결하기 위해 종단적 및 다중 모달 아카이브로부터의 자가 지도 학습을 활용합니다. 우리는 공동 임베딩 예측 아키텍처(JEPA) 사전 학습을 강화하기 위해 본 기관의 CT 스캔과 연결된 전자 건강 기록을 가진 라벨이 없는 환자 집합을 큐레이션합니다. 지도 학습 후 미세 조정한 결과, 우리의 접근 방식이 내부 코호트에서 비정규화된 다중 모달 모델과 이미지 전용 모델보다 우수한 성능을 보임을 보여줍니다(우리의 모델: 0.91, 다중 모달: 0.88, 이미지 전용: 0.73 AUC). 그러나 외부 코호트에서는 성능이 떨어집니다(우리의 모델: 0.72, 이미지 전용: 0.75 AUC). 우리는 JEPA가 성능이 떨어질 수 있는 맥락을 특징짓는 합성 환경을 개발합니다. 본 연구는 라벨이 없는 다중 모달 의료 아카이브를 활용하여 예측 모델을 개선하는 접근 방식을 혁신하며, 폐 결절 진단에서 그 장점과 한계를 입증합니다.

## 📝 요약

이 논문은 폐 결절 진단을 위한 다중모달 모델 개발의 어려움을 해결하기 위해 자기 지도 학습을 활용한 연구입니다. 연구진은 CT 스캔과 전자의료기록을 활용하여 공동 임베딩 예측 아키텍처(JEPA)를 사전 학습했습니다. 그 결과, 내부 코호트에서는 기존 모델보다 우수한 성능을 보였으나, 외부 코호트에서는 성능이 떨어졌습니다. 이 연구는 비지도 다중모달 의료 데이터를 활용하여 예측 모델을 개선하는 방법을 제시하며, 그 장점과 한계를 보여줍니다.

## 🎯 주요 포인트

- 1. 폐 결절 진단을 위한 다중 모달 모델 개발은 라벨링된 데이터의 부족과 훈련 분포에 대한 과적합 경향으로 제한됩니다.

- 2. 본 연구에서는 종단적 및 다중 모달 아카이브로부터의 자가 지도 학습을 활용하여 이러한 문제를 해결하고자 합니다.

- 3. 자가 지도 학습을 통해 사전 훈련된 모델은 내부 코호트에서 비정규화된 다중 모달 모델과 영상 전용 모델보다 우수한 성능을 보였습니다.

- 4. 외부 코호트에서는 자가 지도 학습 모델이 영상 전용 모델보다 성능이 낮았습니다.

- 5. 본 연구는 라벨이 없는 다중 모달 의료 아카이브를 활용하여 예측 모델을 개선하는 접근법을 혁신하고, 폐 결절 진단에서의 장점과 한계를 보여줍니다.

---

*Generated on 2025-09-22 13:58:40*