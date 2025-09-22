
# Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models

**Korean Title:** 대규모 언어 표현 모델을 사용한 사고 학습 안전 보고서의 자동 분류 및 전이 학습 유지

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Peter Beidler|Peter Beidler]] [[authors/Mark Nguyen|Mark Nguyen]] [[authors/Kevin Lybarger|Kevin Lybarger]] [[authors/Ola Holmberg|Ola Holmberg]] [[authors/Eric Ford|Eric Ford]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔬 Broad Technical**: Large Language Representational Models, Natural Language Processing

## 🔗 유사한 논문
- [[A Comprehensive Survey on the Trustworthiness of Large Language Models in Healthcare]] (78.7% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (78.6% similar)
- [[Integrating_Text_and_Time-Series_into_(Large)_Language_Models_to_Predict_Medical_Outcomes_20250918|Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes]] (78.3% similar)
- [[Iterative_Prompt_Refinement_for_Safer_Text-to-Image_Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (78.0% similar)
- [[Taylor-Series_Expanded_Kolmogorov-Arnold_Network_for_Medical_Imaging_Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (77.7% similar)

## 📋 저자 정보

**Authors:** Peter Beidler, Mark Nguyen, Kevin Lybarger, Ola Holmberg, Eric Ford, John Kang

## 📄 Abstract (원문)

PURPOSE: Incident reports are an important tool for safety and quality
improvement in healthcare, but manual review is time-consuming and requires
subject matter expertise. Here we present a natural language processing (NLP)
screening tool to detect high-severity incident reports in radiation oncology
across two institutions.
  METHODS AND MATERIALS: We used two text datasets to train and evaluate our
NLP models: 7,094 reports from our institution (Inst.), and 571 from IAEA
SAFRON (SF), all of which had severity scores labeled by clinical content
experts. We trained and evaluated two types of models: baseline support vector
machines (SVM) and BlueBERT which is a large language model pretrained on
PubMed abstracts and hospitalized patient data. We assessed for
generalizability of our model in two ways. First, we evaluated models trained
using Inst.-train on SF-test. Second, we trained a BlueBERT_TRANSFER model that
was first fine-tuned on Inst.-train then on SF-train before testing on SF-test
set. To further analyze model performance, we also examined a subset of 59
reports from our Inst. dataset, which were manually edited for clarity.
  RESULTS Classification performance on the Inst. test achieved AUROC 0.82
using SVM and 0.81 using BlueBERT. Without cross-institution transfer learning,
performance on the SF test was limited to an AUROC of 0.42 using SVM and 0.56
using BlueBERT. BlueBERT_TRANSFER, which was fine-tuned on both datasets,
improved the performance on SF test to AUROC 0.78. Performance of SVM, and
BlueBERT_TRANSFER models on the manually curated Inst. reports (AUROC 0.85 and
0.74) was similar to human performance (AUROC 0.81).
  CONCLUSION: In summary, we successfully developed cross-institution NLP
models on incident report text from radiation oncology centers. These models
were able to detect high-severity reports similarly to humans on a curated
dataset.

## 🔍 Abstract (한글 번역)

목적: 사고 보고서는 의료 분야에서 안전 및 품질 향상을 위한 중요한 도구이지만, 수동 검토는 시간이 많이 소요되며 주제 전문 지식이 필요합니다. 본 연구에서는 방사선종양학 분야에서 두 기관 간에 고심도 사고 보고서를 감지하기 위한 자연어 처리(NLP) 스크리닝 도구를 제시합니다.

방법 및 자료: 우리는 두 가지 텍스트 데이터셋을 사용하여 NLP 모델을 훈련하고 평가했습니다. 우리 기관(Inst.)에서 7,094개의 보고서 및 IAEA SAFRON(SF)에서 571개의 보고서를 사용하였으며, 모든 보고서는 임상 내용 전문가가 레이블링한 심각도 점수가 있었습니다. 우리는 두 가지 유형의 모델을 훈련하고 평가했습니다: 기준선 지원 벡터 머신(SVM) 및 PubMed 초록 및 입원 환자 데이터에 사전 훈련된 대규모 언어 모델인 BlueBERT. 우리는 모델의 일반화 가능성을 두 가지 방법으로 평가했습니다. 먼저, Inst.-train으로 훈련된 모델을 SF-test에서 평가했습니다. 둘째, Inst.-train에서 먼저 파인튜닝된 BlueBERT_TRANSFER 모델을 SF-train에서 다시 훈련한 후 SF-test 세트에서 테스트했습니다. 모델 성능을 더 자세히 분석하기 위해 우리 기관 데이터셋에서 명확성을 위해 수동으로 수정된 59개의 보고서 하위 집합도 검토했습니다.

결과: Inst. 테스트에서의 분류 성능은 SVM을 사용하여 AUROC 0.82, BlueBERT를 사용하여 AUROC 0.81을 달성했습니다. 기관 간 전이 학습 없이 SF 테스트에서의 성능은 SVM을 사용하여 AUROC 0.42, BlueBERT를 사용하여 AUROC 0.56으로 제한되었습니다. 두 데이터셋에서 파인튜닝된 BlueBERT_TRANSFER는 SF 테스트에서의 성능을 AUROC 0.78로 향상시켰습니다. SVM 및 BlueBERT_TRANSFER 모델의 Inst. 보고서(AUROC 0.85 및 0.74)에서의 성능은 인간의 성능(AUROC 0.81)과 유사했습니다.

결론: 요약하면, 우리는 방사선종양학 센터에서의 사고 보고서 텍스트에서 교차 기관 NLP 모델을 성공적으로 개발했습니다. 이러한 모델은 정제된 데이터셋에서 인간과 유사하게 고심도 보고서를 감지할 수 있었습니다.

## 📝 요약

본 연구는 방사선종양학 분야에서 고중증 사건 보고서를 탐지하기 위한 자연어 처리(NLP) 스크리닝 도구를 제시하였다. 두 기관의 자료를 사용하여 SVM 및 BlueBERT 모델을 훈련 및 평가하였으며, 교차 기관 전이 학습을 통해 성능을 향상시켰다. 결과적으로, 방사선종양학 센터의 사건 보고서 텍스트에서 고중증 보고서를 탐지하는 데 성공적인 NLP 모델을 개발하였으며, 이 모델들은 인간과 유사한 성능을 보였다.

## 🎯 주요 포인트

- 방사선종양학 분야에서 고중도 사건 보고서를 감지하기 위한 자연어 처리(NLP) 스크리닝 도구를 개발하였다.

- SVM 및 BlueBERT 모델을 사용하여 보고서의 분류 성능을 평가하였고, BlueBERT_TRANSFER 모델은 SF 테스트에서 AUROC 0.78로 개선되었다.

- 인간의 성능과 유사한 AUROC 값을 보이며, 방사선종양학 센터의 사건 보고서 텍스트에서 교차 기관 NLP 모델을 성공적으로 개발하였다.

---

*Generated on 2025-09-18 17:05:43*