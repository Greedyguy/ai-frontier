# Explainable AI for Infection Prevention and Control: Modeling CPE Acquisition and Patient Outcomes in an Irish Hospital with Transformers

**Korean Title:** 감염 예방 및 통제를 위한 설명 가능한 인공지능: 트랜스포머를 활용한 아일랜드 병원의 CPE 획득 및 환자 결과 모델링

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Minh-Khoi Pham|Minh-Khoi Pham]] [[authors/Tai Tan Mai|Tai Tan Mai]] [[authors/Martin Crane|Martin Crane]] [[authors/Rob Brennan|Rob Brennan]] [[authors/Marie E. Ward|Marie E. Ward]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Electronic Medical Records

## 🔗 유사한 논문
- [[Blockchain-Enabled Explainable AI for Trusted Healthcare Systems_20250918|Blockchain-Enabled Explainable AI for Trusted Healthcare Systems]] (81.2% similar)
- [[Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (79.3% similar)
- [[Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (79.1% similar)
- [[Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence Label Quality, Domain Shift, Bias and Evaluation Challenges]] (79.0% similar)
- [[Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (78.9% similar)

## 📋 저자 정보

**Authors:** Minh-Khoi Pham, Tai Tan Mai, Martin Crane, Rob Brennan, Marie E. Ward, Una Geary, Declan Byrne, Brian O Connell, Colm Bergin, Donncha Creagh, Nick McDonald, Marija Bezbradica

## 📄 Abstract (원문)

Carbapenemase-Producing Enterobacteriace poses a critical concern for
infection prevention and control in hospitals. However, predictive modeling of
previously highlighted CPE-associated risks such as readmission, mortality, and
extended length of stay (LOS) remains underexplored, particularly with modern
deep learning approaches. This study introduces an eXplainable AI modeling
framework to investigate CPE impact on patient outcomes from Electronic Medical
Records data of an Irish hospital. We analyzed an inpatient dataset from an
Irish acute hospital, incorporating diagnostic codes, ward transitions, patient
demographics, infection-related variables and contact network features. Several
Transformer-based architectures were benchmarked alongside traditional machine
learning models. Clinical outcomes were predicted, and XAI techniques were
applied to interpret model decisions. Our framework successfully demonstrated
the utility of Transformer-based models, with TabTransformer consistently
outperforming baselines across multiple clinical prediction tasks, especially
for CPE acquisition (AUROC and sensitivity). We found infection-related
features, including historical hospital exposure, admission context, and
network centrality measures, to be highly influential in predicting patient
outcomes and CPE acquisition risk. Explainability analyses revealed that
features like "Area of Residence", "Admission Ward" and prior admissions are
key risk factors. Network variables like "Ward PageRank" also ranked highly,
reflecting the potential value of structural exposure information. This study
presents a robust and explainable AI framework for analyzing complex EMR data
to identify key risk factors and predict CPE-related outcomes. Our findings
underscore the superior performance of the Transformer models and highlight the
importance of diverse clinical and network features.

## 🔍 Abstract (한글 번역)

카바페넴분해효소 생성 장내세균(Enterobacteriaceae)은 병원 내 감염 예방 및 통제에 있어 중대한 우려 사항입니다. 그러나 재입원, 사망률, 입원 기간 연장(LOS)과 같은 CPE 관련 위험 요소에 대한 예측 모델링은 특히 현대의 심층 학습 접근법을 통해 충분히 탐구되지 않았습니다. 본 연구는 아일랜드 병원의 전자의무기록(EMR) 데이터를 활용하여 환자 결과에 대한 CPE의 영향을 조사하기 위해 설명 가능한 인공지능(XAI) 모델링 프레임워크를 소개합니다. 우리는 진단 코드, 병동 이동, 환자 인구통계학적 정보, 감염 관련 변수 및 접촉 네트워크 특징을 포함한 아일랜드 급성 병원의 입원 환자 데이터를 분석했습니다. 여러 트랜스포머 기반 아키텍처가 전통적인 기계 학습 모델과 함께 벤치마킹되었습니다. 임상 결과를 예측하고 모델 결정 해석을 위해 XAI 기법이 적용되었습니다. 우리의 프레임워크는 트랜스포머 기반 모델의 유용성을 성공적으로 입증했으며, TabTransformer는 여러 임상 예측 과제에서 일관되게 기준 모델을 능가했으며 특히 CPE 획득(AUROC 및 민감도)에서 두드러졌습니다. 우리는 과거 병원 노출, 입원 상황, 네트워크 중심성 측정치를 포함한 감염 관련 특징이 환자 결과 및 CPE 획득 위험을 예측하는 데 매우 중요한 영향을 미친다는 것을 발견했습니다. 설명 가능성 분석은 "거주 지역", "입원 병동" 및 이전 입원이 주요 위험 요소임을 밝혀냈습니다. "병동 페이지랭크"와 같은 네트워크 변수도 높은 순위를 차지하여 구조적 노출 정보의 잠재적 가치를 반영했습니다. 본 연구는 복잡한 EMR 데이터를 분석하여 주요 위험 요소를 식별하고 CPE 관련 결과를 예측하기 위한 견고하고 설명 가능한 AI 프레임워크를 제시합니다. 우리의 연구 결과는 트랜스포머 모델의 우수한 성능을 강조하며 다양한 임상 및 네트워크 특징의 중요성을 부각시킵니다.

## 📝 요약

이 연구는 아일랜드 병원의 전자의무기록(EMR) 데이터를 활용하여 카바페넴분해효소 생성 장내세균(CPE)이 환자 결과에 미치는 영향을 분석하는 설명 가능한 AI 모델링 프레임워크를 제안합니다. Transformer 기반 모델과 전통적 기계 학습 모델을 비교한 결과, TabTransformer가 여러 임상 예측 작업에서 우수한 성능을 보였습니다. 특히, CPE 획득 위험 예측에서 AUROC와 민감도 측면에서 뛰어났습니다. 감염 관련 변수, 병원 노출 이력, 입원 맥락, 네트워크 중심성 등이 환자 결과 예측에 중요한 영향을 미쳤으며, "거주 지역", "입원 병동", 이전 입원 등이 주요 위험 요소로 확인되었습니다. 연구는 복잡한 EMR 데이터를 분석하여 CPE 관련 결과를 예측하는 강력하고 설명 가능한 AI 프레임워크의 유용성을 입증하며, Transformer 모델의 우수성과 다양한 임상 및 네트워크 특성의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. 이 연구는 병원 내 감염 예방 및 통제에 중요한 카바페넴 분해효소 생성 장내세균의 영향을 설명 가능한 AI 모델링 프레임워크를 통해 분석하였습니다.

- 2. Transformer 기반 모델, 특히 TabTransformer가 여러 임상 예측 작업에서 기존 모델을 능가하는 성능을 보였습니다.

- 3. 환자 결과 및 CPE 획득 위험 예측에 있어 병원 노출 이력, 입원 맥락, 네트워크 중심성 측정치와 같은 감염 관련 변수가 중요한 영향을 미쳤습니다.

- 4. 설명 가능성 분석을 통해 "거주 지역", "입원 병동", 이전 입원이 주요 위험 요소로 확인되었으며, "병동 PageRank"와 같은 네트워크 변수도 높은 순위를 차지했습니다.

- 5. 이 연구는 복잡한 전자의무기록 데이터를 분석하여 주요 위험 요소를 식별하고 CPE 관련 결과를 예측하는 견고하고 설명 가능한 AI 프레임워크를 제시합니다.

---

*Generated on 2025-09-20 02:41:56*