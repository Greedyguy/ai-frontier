---
keywords:
  - Deep Learning
  - Domain Shift
  - Clinician-Validated Datasets
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:21:30.904921",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Domain Shift",
    "Clinician-Validated Datasets"
  ],
  "rejected_keywords": [
    "Label Quality",
    "Dataset Bias"
  ],
  "similarity_scores": {
    "Deep Learning": 0.8,
    "Domain Shift": 0.75,
    "Clinician-Validated Datasets": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Limitations of Public Chest Radiography Datasets for Artificial Intelligence: Label Quality, Domain Shift, Bias and Evaluation Challenges

**Korean Title:** 공공 흉부 방사선 촬영 데이터셋의 인공지능 한계: 레이블 품질, 도메인 이동, 편향 및 평가 과제

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Domain Shift|Domain Shift]]
**🚀 Evolved Concepts**: [[keywords/Clinician-Validated Datasets|Clinician-Validated Datasets]]

## 🔗 유사한 논문
- [[Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (81.9% similar)
- [[Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses_20250919|Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses]] (80.1% similar)
- [[MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (79.7% similar)
- [[Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models_20250917|Automated Triaging and Transfer Learning of Incident Learning Safety Reports Using Large Language Representational Models]] (79.5% similar)
- [[Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (79.2% similar)

## 📋 저자 정보

**Authors:** Amy Rafferty, Rishi Ramaesh, Ajitha Rajan

## 📄 Abstract (원문)

Artificial intelligence has shown significant promise in chest radiography,
where deep learning models can approach radiologist-level diagnostic
performance. Progress has been accelerated by large public datasets such as
MIMIC-CXR, ChestX-ray14, PadChest, and CheXpert, which provide hundreds of
thousands of labelled images with pathology annotations. However, these
datasets also present important limitations. Automated label extraction from
radiology reports introduces errors, particularly in handling uncertainty and
negation, and radiologist review frequently disagrees with assigned labels. In
addition, domain shift and population bias restrict model generalisability,
while evaluation practices often overlook clinically meaningful measures. We
conduct a systematic analysis of these challenges, focusing on label quality,
dataset bias, and domain shift. Our cross-dataset domain shift evaluation
across multiple model architectures revealed substantial external performance
degradation, with pronounced reductions in AUPRC and F1 scores relative to
internal testing. To assess dataset bias, we trained a source-classification
model that distinguished datasets with near-perfect accuracy, and performed
subgroup analyses showing reduced performance for minority age and sex groups.
Finally, expert review by two board-certified radiologists identified
significant disagreement with public dataset labels. Our findings highlight
important clinical weaknesses of current benchmarks and emphasise the need for
clinician-validated datasets and fairer evaluation frameworks.

## 🔍 Abstract (한글 번역)

인공지능은 흉부 방사선 촬영에서 상당한 가능성을 보여주었으며, 딥러닝 모델은 방사선 전문의 수준의 진단 성능에 접근할 수 있습니다. MIMIC-CXR, ChestX-ray14, PadChest, CheXpert와 같은 대규모 공공 데이터셋은 병리 주석이 포함된 수십만 개의 라벨링된 이미지를 제공하여 이러한 발전을 가속화했습니다. 그러나 이러한 데이터셋은 중요한 한계도 가지고 있습니다. 방사선 보고서에서 자동으로 라벨을 추출하는 과정에서 불확실성과 부정 처리를 포함한 오류가 발생하며, 방사선 전문의의 검토는 할당된 라벨과 자주 불일치합니다. 또한, 도메인 이동과 인구 편향은 모델의 일반화를 제한하며, 평가 관행은 종종 임상적으로 의미 있는 측정을 간과합니다. 우리는 라벨 품질, 데이터셋 편향, 도메인 이동에 초점을 맞추어 이러한 문제를 체계적으로 분석합니다. 여러 모델 아키텍처에 걸친 교차 데이터셋 도메인 이동 평가에서는 외부 성능 저하가 상당히 나타났으며, 내부 테스트에 비해 AUPRC와 F1 점수가 크게 감소했습니다. 데이터셋 편향을 평가하기 위해, 우리는 데이터셋을 거의 완벽한 정확도로 구별하는 소스 분류 모델을 훈련시켰으며, 소수 연령 및 성별 그룹에서 성능이 저하되는 하위 그룹 분석을 수행했습니다. 마지막으로, 두 명의 보드 인증을 받은 방사선 전문의의 전문가 검토는 공공 데이터셋 라벨과의 상당한 불일치를 확인했습니다. 우리의 연구 결과는 현재 벤치마크의 중요한 임상적 약점을 강조하며, 임상의가 검증한 데이터셋과 공정한 평가 체계의 필요성을 강조합니다.

## 📝 요약

인공지능은 흉부 방사선 사진 진단에서 방사선과 전문의 수준의 성능을 보이고 있으며, MIMIC-CXR, ChestX-ray14, PadChest, CheXpert와 같은 대규모 공개 데이터셋이 발전을 가속화했습니다. 그러나 자동 레이블 추출 과정에서 불확실성 처리와 부정 표현에서 오류가 발생하고, 방사선과 전문의의 검토 결과와 불일치가 자주 발생합니다. 또한, 도메인 이동과 인구 편향이 모델의 일반화 능력을 제한하며, 평가 관행은 임상적으로 의미 있는 지표를 간과합니다. 본 연구는 레이블 품질, 데이터셋 편향, 도메인 이동에 대한 체계적인 분석을 수행했습니다. 여러 모델 아키텍처를 통한 도메인 이동 평가에서 외부 성능 저하가 확인되었고, 데이터셋 편향 평가에서는 소수 연령 및 성별 그룹에서 성능 저하가 나타났습니다. 두 명의 방사선과 전문의가 데이터셋 레이블과의 상당한 불일치를 확인했습니다. 연구 결과는 현재 벤치마크의 임상적 약점을 강조하며, 임상 전문가가 검증한 데이터셋과 공정한 평가 체계의 필요성을 제시합니다.

## 🎯 주요 포인트

- 1. 인공지능은 흉부 방사선 촬영에서 방사선 전문의 수준의 진단 성능을 보일 수 있다.

- 2. 대규모 공개 데이터셋은 진단 모델 개발에 기여하지만, 자동화된 라벨 추출 과정에서 오류가 발생한다.

- 3. 도메인 이동과 인구 편향은 모델의 일반화 능력을 제한하며, 평가 관행은 임상적으로 의미 있는 측정을 간과한다.

- 4. 데이터셋 간 도메인 이동 평가 결과, 외부 성능 저하가 상당하며, 특히 AUPRC 및 F1 점수가 크게 감소한다.

- 5. 전문가 검토 결과, 공개 데이터셋 라벨과의 상당한 불일치가 발견되었으며, 임상적으로 검증된 데이터셋과 공정한 평가 체계의 필요성이 강조된다.

---

*Generated on 2025-09-20 01:01:46*