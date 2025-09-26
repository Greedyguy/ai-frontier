---
keywords:
  - Kolmogorov-Arnold Networks
  - Gradient-weighted Class Activation Mapping
  - Spline-based Function Approximation
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13687
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:06:25.552291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kolmogorov-Arnold Networks",
    "Gradient-weighted Class Activation Mapping",
    "Spline-based Function Approximation"
  ],
  "rejected_keywords": [
    "Medical Image Classification"
  ],
  "similarity_scores": {
    "Kolmogorov-Arnold Networks": 0.8,
    "Gradient-weighted Class Activation Mapping": 0.78,
    "Spline-based Function Approximation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification

**Korean Title:** 의학 영상 분류를 위한 테일러 급수 확장된 콜모고로프-아놀드 네트워크를 유지하십시오.

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Gradient-weighted Class Activation Mapping|Gradient-weighted Class Activation Mapping]]
**⚡ Unique Technical**: [[keywords/Kolmogorov-Arnold Networks|Kolmogorov-Arnold Networks]], [[keywords/Spline-based Function Approximation|Spline-based Function Approximation]]

## 🔗 유사한 논문
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (81.5% similar)
- [[Locally_Explaining_Prediction_Behavior_via_Gradual_Interventions_and_Measuring_Property_Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (79.5% similar)
- [[ModalSurv: A Multimodal Deep Survival Framework for Prostate and Bladder Cancer]] (79.0% similar)
- [[Multimodal_signal_fusion_for_stress_detection_using_deep_neural_networks_a_novel_approach_for_converting_1D_signals_to_unified_2D_images_20250918|Multimodal signal fusion for stress detection using deep neural networks: a novel approach for converting 1D signals to unified 2D images]] (78.5% similar)
- [[Hybrid Quantum-Classical Model for Image Classification]] (77.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13687v1 Announce Type: new 
Abstract: Effective and interpretable classification of medical images is a challenge in computer-aided diagnosis, especially in resource-limited clinical settings. This study introduces spline-based Kolmogorov-Arnold Networks (KANs) for accurate medical image classification with limited, diverse datasets. The models include SBTAYLOR-KAN, integrating B-splines with Taylor series; SBRBF-KAN, combining B-splines with Radial Basis Functions; and SBWAVELET-KAN, embedding B-splines in Morlet wavelet transforms. These approaches leverage spline-based function approximation to capture both local and global nonlinearities. The models were evaluated on brain MRI, chest X-rays, tuberculosis X-rays, and skin lesion images without preprocessing, demonstrating the ability to learn directly from raw data. Extensive experiments, including cross-dataset validation and data reduction analysis, showed strong generalization and stability. SBTAYLOR-KAN achieved up to 98.93% accuracy, with a balanced F1-score, maintaining over 86% accuracy using only 30% of the training data across three datasets. Despite class imbalance in the skin cancer dataset, experiments on both imbalanced and balanced versions showed SBTAYLOR-KAN outperforming other models, achieving 68.22% accuracy. Unlike traditional CNNs, which require millions of parameters (e.g., ResNet50 with 24.18M), SBTAYLOR-KAN achieves comparable performance with just 2,872 trainable parameters, making it more suitable for constrained medical environments. Gradient-weighted Class Activation Mapping (Grad-CAM) was used for interpretability, highlighting relevant regions in medical images. This framework provides a lightweight, interpretable, and generalizable solution for medical image classification, addressing the challenges of limited datasets and data-scarce scenarios in clinical AI applications.

## 🔍 Abstract (한글 번역)

arXiv:2509.13687v1 발표 유형: 새로운
요약: 의료 이미지의 효과적이고 해석 가능한 분류는 특히 자원이 제한된 임상 환경에서 컴퓨터 지원 진단에서의 과제입니다. 본 연구는 제한된 다양한 데이터셋을 활용한 정확한 의료 이미지 분류를 위해 스플라인 기반의 콜모고로프-아놀드 네트워크(KANs)를 소개합니다. 이 모델들은 B-스플라인과 테일러 시리즈를 통합한 SBTAYLOR-KAN, B-스플라인과 방사 기저 함수를 결합한 SBRBF-KAN, 그리고 B-스플라인을 모를레 웨이블릿 변환에 포함시킨 SBWAVELET-KAN을 포함합니다. 이러한 접근 방식은 지역 및 전역 비선형성을 포착하기 위해 스플라인 기반의 함수 근사를 활용합니다. 이 모델들은 전처리 없이 뇌 MRI, 흉부 X-선, 결핵 X-선 및 피부 병변 이미지에서 평가되었으며, 원시 데이터로부터 직접 학습할 수 있는 능력을 보여주었습니다. 교차 데이터셋 유효성 검사 및 데이터 축소 분석을 포함한 광범위한 실험에서 강력한 일반화 및 안정성을 보였습니다. SBTAYLOR-KAN은 3개 데이터셋 전체의 학습 데이터의 30%만 사용하여 98.93%의 정확도를 달성했으며, 균형 잡힌 F1-점수를 유지했습니다. 피부암 데이터셋에서의 클래스 불균형에도 불구하고, 불균형 및 균형 잡힌 버전에서의 실험에서 SBTAYLOR-KAN이 다른 모델들을 능가하며 68.22%의 정확도를 달성했습니다. 수백만 개의 매개변수(예: 24.18M의 ResNet50)가 필요한 전통적인 CNN과 달리, SBTAYLOR-KAN은 단지 2,872개의 학습 가능한 매개변수로 비슷한 성능을 달성하여 제한된 의료 환경에 더 적합합니다. 해석 가능성을 위해 그래디언트 가중치 클래스 활성화 매핑(Grad-CAM)이 사용되었으며, 의료 이미지의 관련 영역을 강조했습니다. 이 프레임워크는 제한된 데이터셋과 임상 AI 응용 프로그램에서의 데이터 부족 시나리오에 대응하는 의료 이미지 분류를 위한 가벼운, 해석 가능하고 일반화된 솔루션을 제공합니다.

## 📝 요약

의료 이미지의 효과적이고 해석 가능한 분류는 컴퓨터 지원 진단에서 중요한 과제이다. 본 연구는 한정된 다양한 데이터셋으로 정확한 의료 이미지 분류를 위해 스플라인 기반 콜모고로프-아놀드 네트워크(KANs)를 제안한다. SBTAYLOR-KAN, SBRBF-KAN, SBWAVELET-KAN 모델은 지역 및 전역 비선형성을 포착하기 위해 스플라인 기반 함수 근사를 활용한다. 이러한 모델은 전처리 없이 뇌 MRI, 흉부 X-선, 결핵 X-선 및 피부 병변 이미지에서 평가되었으며, 원시 데이터로부터 직접 학습하는 능력을 보여주었다. SBTAYLOR-KAN은 30%의 학습 데이터만 사용하여 86% 이상의 정확도를 유지하며, 다른 모델을 능가하는 결과를 얻었다. 이러한 프레임워크는 제한된 데이터셋과 데이터 부족한 임상 AI 응용 프로그램의 도전을 해결하기 위한 가벼우면서 해석 가능하고 일반화된 솔루션을 제공한다.

## 🎯 주요 포인트

- 1. 한정된 다양한 데이터셋으로 정확한 의료 이미지 분류를 위한 스플라인 기반 콜모고로프-아놀드 네트워크(KAN) 도입

- 2. SBTAYLOR-KAN은 학습 데이터의 30%만 사용하여 86% 이상의 정확도를 유지하며 최대 98.93%의 정확도를 달성

- 3. SBTAYLOR-KAN은 2,872개의 학습 가능한 매개변수만 사용하여 ResNet50과 비교 가능한 성능을 보여줌.

---

*Generated on 2025-09-18 16:59:53*