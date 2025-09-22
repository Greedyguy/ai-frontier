# From Data to Diagnosis: A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction

**Korean Title:** 데이터에서 진단까지: 소아 백혈병 예측을 위한 대규모 포괄적 골수 데이터셋과 인공지능 방법론

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Cell Detection, Diagnosis Prediction

## 🔗 유사한 논문
- [[2025-09-18/ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (83.6% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence Label Quality, Domain Shift, Bias and Evaluation Challenges]] (81.8% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2 Atypical Mitosis Classification]] (81.4% similar)
- [[2025-09-19/Data-Driven Prediction of Maternal Nutritional Status in Ethiopia Using Ensemble Machine Learning Models_20250919|Data-Driven Prediction of Maternal Nutritional Status in Ethiopia Using Ensemble Machine Learning Models]] (81.1% similar)
- [[2025-09-17/Deconstructing Intraocular Pressure_ A Non-invasive Multi-Stage Probabilistic Inverse Framework_20250917|Deconstructing Intraocular Pressure A Non-invasive Multi-Stage Probabilistic Inverse Framework]] (80.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15895v1 Announce Type: cross 
Abstract: Leukemia diagnosis primarily relies on manual microscopic analysis of bone marrow morphology supported by additional laboratory parameters, making it complex and time consuming. While artificial intelligence (AI) solutions have been proposed, most utilize private datasets and only cover parts of the diagnostic pipeline. Therefore, we present a large, high-quality, publicly available leukemia bone marrow dataset spanning the entire diagnostic process, from cell detection to diagnosis. Using this dataset, we further propose methods for cell detection, cell classification, and diagnosis prediction. The dataset comprises 246 pediatric patients with diagnostic, clinical and laboratory information, over 40 000 cells with bounding box annotations and more than 28 000 of these with high-quality class labels, making it the most comprehensive dataset publicly available. Evaluation of the AI models yielded an average precision of 0.96 for the cell detection, an area under the curve of 0.98, and an F1-score of 0.61 for the 33-class cell classification, and a mean F1-score of 0.90 for the diagnosis prediction using predicted cell counts. While the proposed approaches demonstrate their usefulness for AI-assisted diagnostics, the dataset will foster further research and development in the field, ultimately contributing to more precise diagnoses and improved patient outcomes.

## 🔍 Abstract (한글 번역)

arXiv:2509.15895v1 발표 유형: 교차  
초록: 백혈병 진단은 주로 골수 형태의 수작업 현미경 분석에 추가적인 실험실 매개변수가 지원되어 이루어지며, 이는 복잡하고 시간이 많이 소요됩니다. 인공지능(AI) 솔루션이 제안되었지만, 대부분은 비공개 데이터셋을 사용하고 진단 파이프라인의 일부만을 다룹니다. 따라서 우리는 세포 검출부터 진단까지 전체 진단 과정을 아우르는 대규모의 고품질 공개 백혈병 골수 데이터셋을 제시합니다. 이 데이터셋을 사용하여 세포 검출, 세포 분류, 진단 예측을 위한 방법을 제안합니다. 이 데이터셋은 진단, 임상 및 실험실 정보를 포함한 246명의 소아 환자와 경계 상자 주석이 있는 40,000개 이상의 세포, 그리고 이 중 28,000개 이상의 고품질 클래스 레이블을 포함하고 있어 가장 포괄적인 공개 데이터셋입니다. AI 모델의 평가 결과, 세포 검출의 평균 정밀도는 0.96, 곡선 아래 면적은 0.98, 33개 클래스 세포 분류의 F1-점수는 0.61, 예측된 세포 수를 사용한 진단 예측의 평균 F1-점수는 0.90으로 나타났습니다. 제안된 접근법은 AI 지원 진단의 유용성을 입증하는 한편, 이 데이터셋은 해당 분야의 추가 연구 및 개발을 촉진하여 궁극적으로 더 정확한 진단과 향상된 환자 결과에 기여할 것입니다.

## 📝 요약

이 논문은 백혈병 진단을 위한 인공지능(AI) 솔루션 개발을 위해 대규모의 공개된 골수 데이터셋을 제시합니다. 이 데이터셋은 246명의 소아 환자 데이터를 포함하며, 40,000개 이상의 세포에 대한 바운딩 박스 주석과 28,000개 이상의 고품질 클래스 레이블을 제공합니다. 이를 통해 세포 탐지, 분류, 진단 예측 방법론을 제안합니다. AI 모델 평가 결과, 세포 탐지의 평균 정밀도는 0.96, 33개 클래스 세포 분류의 AUC는 0.98, F1-점수는 0.61, 진단 예측의 평균 F1-점수는 0.90을 기록했습니다. 이 연구는 AI를 활용한 진단의 정확성을 높이고, 환자 치료 결과를 개선하는 데 기여할 것입니다.

## 🎯 주요 포인트

- 1. 백혈병 진단은 복잡하고 시간이 많이 소요되는 수작업의 골수 형태 분석에 의존합니다.

- 2. 본 연구는 진단 전 과정을 아우르는 대규모의 고품질 공개 백혈병 골수 데이터셋을 제공합니다.

- 3. 데이터셋은 246명의 소아 환자와 40,000개 이상의 세포에 대한 경계 상자 주석 및 28,000개 이상의 고품질 클래스 레이블을 포함합니다.

- 4. AI 모델 평가 결과, 세포 탐지에서 평균 정밀도 0.96, 33개 클래스 세포 분류에서 AUC 0.98 및 F1-스코어 0.61, 진단 예측에서 평균 F1-스코어 0.90을 기록했습니다.

- 5. 제안된 접근법은 AI 지원 진단의 유용성을 보여주며, 데이터셋은 더 정확한 진단과 향상된 환자 결과에 기여할 것입니다.

---

*Generated on 2025-09-22 14:16:01*