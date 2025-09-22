# Examining Deployment and Refinement of the VIOLA-AI Intracranial Hemorrhage Model Using an Interactive NeoMedSys Platform

**Korean Title:** VIOLA-AI 두개내 출혈 모델의 배치 및 개선에 대한 연구: 인터랙티브 NeoMedSys 플랫폼을 활용하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Iterative Model Refinement

## 🔗 유사한 논문
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (80.9% similar)
- [[2025-09-18/ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (80.6% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (80.2% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence Label Quality, Domain Shift, Bias and Evaluation Challenges]] (80.2% similar)
- [[2025-09-22/From Data to Diagnosis_ A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction_20250922|From Data to Diagnosis A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction]] (80.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.09380v2 Announce Type: replace-cross 
Abstract: Background: There are many challenges and opportunities in the clinical deployment of AI tools in radiology. The current study describes a radiology software platform called NeoMedSys that can enable efficient deployment and refinements of AI models. We evaluated the feasibility and effectiveness of running NeoMedSys for three months in real-world clinical settings and focused on improvement performance of an in-house developed AI model (VIOLA-AI) designed for intracranial hemorrhage (ICH) detection.
  Methods: NeoMedSys integrates tools for deploying, testing, and optimizing AI models with a web-based medical image viewer, annotation system, and hospital-wide radiology information systems. A prospective pragmatic investigation was deployed using clinical cases of patients presenting to the largest Emergency Department in Norway (site-1) with suspected traumatic brain injury (TBI) or patients with suspected stroke (site-2). We assessed ICH classification performance as VIOLA-AI encountered new data and underwent pre-planned model retraining. Performance metrics included sensitivity, specificity, accuracy, and the area under the receiver operating characteristic curve (AUC).
  Results: NeoMedSys facilitated iterative improvements in the AI model, significantly enhancing its diagnostic accuracy. Automated bleed detection and segmentation were reviewed in near real-time to facilitate re-training VIOLA-AI. The iterative refinement process yielded a marked improvement in classification sensitivity, rising to 90.3% (from 79.2%), and specificity that reached 89.3% (from 80.7%). The bleed detection ROC analysis for the entire sample demonstrated a high area-under-the-curve (AUC) of 0.949 (from 0.873). Model refinement stages were associated with notable gains, highlighting the value of real-time radiologist feedback.

## 🔍 Abstract (한글 번역)

arXiv:2505.09380v2 발표 유형: 교차 대체  
초록: 배경: 방사선학에서 AI 도구의 임상 배치에는 많은 도전과 기회가 있습니다. 본 연구는 AI 모델의 효율적인 배치와 개선을 가능하게 하는 방사선학 소프트웨어 플랫폼인 NeoMedSys를 설명합니다. 우리는 실제 임상 환경에서 NeoMedSys를 3개월 동안 운영하여 그 실행 가능성과 효과를 평가했으며, 두개내 출혈(ICH) 탐지를 위해 개발된 자체 AI 모델(VIOLA-AI)의 성능 향상에 중점을 두었습니다.  
방법: NeoMedSys는 웹 기반 의료 영상 뷰어, 주석 시스템 및 병원 전체의 방사선 정보 시스템과 함께 AI 모델을 배포, 테스트 및 최적화하는 도구를 통합합니다. 노르웨이 최대 응급실(사이트-1)에 외상성 뇌 손상(TBI)이 의심되는 환자 또는 뇌졸중이 의심되는 환자(사이트-2)의 임상 사례를 사용하여 전향적 실용적 조사가 수행되었습니다. VIOLA-AI가 새로운 데이터를 접하고 사전 계획된 모델 재훈련을 거치면서 ICH 분류 성능을 평가했습니다. 성능 지표에는 민감도, 특이도, 정확도 및 수신자 작동 특성 곡선 아래 면적(AUC)이 포함되었습니다.  
결과: NeoMedSys는 AI 모델의 반복적인 개선을 용이하게 하여 진단 정확성을 크게 향상시켰습니다. 자동 출혈 감지 및 세분화는 VIOLA-AI의 재훈련을 용이하게 하기 위해 거의 실시간으로 검토되었습니다. 반복적인 개선 과정은 분류 민감도를 79.2%에서 90.3%로, 특이도를 80.7%에서 89.3%로 크게 향상시켰습니다. 전체 샘플에 대한 출혈 감지 ROC 분석은 0.873에서 0.949의 높은 곡선 아래 면적(AUC)을 나타냈습니다. 모델 개선 단계는 실시간 방사선 전문의 피드백의 가치를 강조하며 주목할 만한 이득과 관련이 있었습니다.

## 📝 요약

이 연구는 방사선학에서 AI 도구의 임상 배치를 위한 소프트웨어 플랫폼 NeoMedSys를 소개하고, 이를 통해 AI 모델의 효율적인 배치와 개선을 가능하게 합니다. NeoMedSys는 웹 기반 의료 이미지 뷰어, 주석 시스템, 병원 방사선 정보 시스템과 통합되어 AI 모델을 배포, 테스트 및 최적화합니다. 노르웨이의 응급실에서 3개월간 실험을 통해 두개내 출혈(ICH) 감지를 위한 VIOLA-AI 모델의 성능을 평가했습니다. 연구 결과, NeoMedSys는 AI 모델의 진단 정확도를 크게 향상시켰으며, 민감도는 79.2%에서 90.3%로, 특이도는 80.7%에서 89.3%로 증가했습니다. 또한, ROC 분석에서 AUC가 0.873에서 0.949로 개선되었습니다. 이 과정에서 실시간 방사선 전문의 피드백이 중요한 역할을 했습니다.

## 🎯 주요 포인트

- 1. NeoMedSys는 AI 모델의 효율적인 배포와 개선을 가능하게 하는 방사선학 소프트웨어 플랫폼입니다.

- 2. NeoMedSys는 웹 기반 의료 이미지 뷰어, 주석 시스템, 병원 전체 방사선 정보 시스템과 통합되어 AI 모델의 배포, 테스트, 최적화를 지원합니다.

- 3. VIOLA-AI 모델의 두개내 출혈(ICH) 감지 성능은 새로운 데이터를 통해 90.3%의 민감도와 89.3%의 특이도로 향상되었습니다.

- 4. NeoMedSys는 실시간 방사선 전문의 피드백을 통해 모델의 진단 정확도를 크게 향상시켰습니다.

- 5. 전체 샘플에 대한 출혈 감지 ROC 분석에서 AUC는 0.949로 높은 성능을 보였습니다.

---

*Generated on 2025-09-22 14:47:32*