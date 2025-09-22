# Deep learning and abstractive summarisation for radiological reports: an empirical study for adapting the PEGASUS models' family with scarce data

**Korean Title:** 심층 학습 및 방사선 보고서의 추상적 요약: 제한된 데이터로 PEGASUS 모델 계열을 적응시키기 위한 실증적 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Abstractive Summarisation, Fine-tuning

## 🔗 유사한 논문
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence Label Quality, Domain Shift, Bias and Evaluation Challenges]] (82.5% similar)
- [[2025-09-17/Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models_20250917|Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models]] (80.6% similar)
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (80.0% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (79.9% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15419v1 Announce Type: cross 
Abstract: Regardless of the rapid development of artificial intelligence, abstractive summarisation is still challenging for sensitive and data-restrictive domains like medicine. With the increasing number of imaging, the relevance of automated tools for complex medical text summarisation is expected to become highly relevant. In this paper, we investigated the adaptation via fine-tuning process of a non-domain-specific abstractive summarisation encoder-decoder model family, and gave insights to practitioners on how to avoid over- and underfitting. We used PEGASUS and PEGASUS-X, on a medium-sized radiological reports public dataset. For each model, we comprehensively evaluated two different checkpoints with varying sizes of the same training data. We monitored the models' performances with lexical and semantic metrics during the training history on the fixed-size validation set. PEGASUS exhibited different phases, which can be related to epoch-wise double-descent, or peak-drop-recovery behaviour. For PEGASUS-X, we found that using a larger checkpoint led to a performance detriment. This work highlights the challenges and risks of fine-tuning models with high expressivity when dealing with scarce training data, and lays the groundwork for future investigations into more robust fine-tuning strategies for summarisation models in specialised domains.

## 🔍 Abstract (한글 번역)

arXiv:2509.15419v1 발표 유형: 교차  
초록: 인공지능의 급속한 발전에도 불구하고, 의학과 같은 민감하고 데이터 제한적인 분야에서는 추상적 요약이 여전히 도전적입니다. 이미지의 수가 증가함에 따라 복잡한 의학 텍스트 요약을 위한 자동화 도구의 중요성이 크게 증가할 것으로 예상됩니다. 이 논문에서는 비도메인 특화 추상적 요약 인코더-디코더 모델 계열의 적응을 미세 조정 과정을 통해 조사하고, 과적합 및 과소적합을 피하는 방법에 대한 통찰을 실무자들에게 제공했습니다. 우리는 중간 크기의 방사선 보고서 공개 데이터셋에서 PEGASUS와 PEGASUS-X를 사용했습니다. 각 모델에 대해 동일한 훈련 데이터의 크기를 달리하여 두 가지 다른 체크포인트를 종합적으로 평가했습니다. 고정 크기 검증 세트에서 훈련 기록 동안 모델의 성능을 어휘 및 의미적 메트릭으로 모니터링했습니다. PEGASUS는 에포크별 더블 디센트 또는 피크-드롭-회복 행동과 관련될 수 있는 다양한 단계를 보였습니다. PEGASUS-X의 경우, 더 큰 체크포인트를 사용하는 것이 성능 저하로 이어진다는 것을 발견했습니다. 이 연구는 훈련 데이터가 부족할 때 높은 표현력을 가진 모델을 미세 조정하는 것의 도전과 위험을 강조하며, 특수화된 도메인에서 요약 모델을 위한 보다 견고한 미세 조정 전략에 대한 향후 연구의 기초를 마련합니다.

## 📝 요약

이 논문은 비전문 분야의 추상적 요약 모델을 의료 분야에 맞게 미세 조정하는 방법을 연구했습니다. PEGASUS와 PEGASUS-X 모델을 사용하여 방사선 보고서 데이터셋에서 성능을 평가했으며, 모델의 과적합 및 과소적합을 피하는 방법을 제시했습니다. PEGASUS는 학습 과정에서 특정 패턴을 보였고, PEGASUS-X는 더 큰 체크포인트 사용 시 성능 저하가 나타났습니다. 이 연구는 제한된 데이터로 고성능 모델을 미세 조정하는 데 따른 도전과 위험을 강조하며, 전문 분야에서 요약 모델의 더 견고한 미세 조정 전략을 위한 기초를 마련했습니다.

## 🎯 주요 포인트

- 1. 인공지능의 급속한 발전에도 불구하고, 의학과 같은 민감하고 데이터 제한적인 분야에서는 추상적 요약이 여전히 도전적이다.

- 2. 본 연구에서는 비도메인 특화 추상적 요약 인코더-디코더 모델의 미세 조정 과정을 조사하고, 과적합 및 과소적합을 피하는 방법에 대한 통찰을 제공하였다.

- 3. PEGASUS와 PEGASUS-X 모델을 사용하여 중간 크기의 방사선 보고서 공개 데이터셋에서 두 가지 다른 체크포인트를 평가하였다.

- 4. PEGASUS 모델은 에포크별 이중 하강 또는 피크-드롭-회복 행동과 관련된 다양한 단계를 보였다.

- 5. PEGASUS-X 모델에서는 더 큰 체크포인트를 사용할 경우 성능 저하가 발생함을 발견하였다.

---

*Generated on 2025-09-22 13:55:18*