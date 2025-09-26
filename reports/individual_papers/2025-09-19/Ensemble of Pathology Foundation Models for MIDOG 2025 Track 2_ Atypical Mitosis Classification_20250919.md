---
keywords:
  - Foundation Models
  - Convolutional Neural Networks
  - Fourier Domain Adaptation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.02591
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:46:11.407767",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Foundation Models",
    "Convolutional Neural Networks",
    "Fourier Domain Adaptation"
  ],
  "rejected_keywords": [
    "Mitotic Figures"
  ],
  "similarity_scores": {
    "Foundation Models": 0.8,
    "Convolutional Neural Networks": 0.78,
    "Fourier Domain Adaptation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification

**Korean Title:** 병리학 기초 모델 앙상블을 활용한 MIDOG 2025 트랙 2: 비정형 유사분열 분류

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Convolutional Neural Networks|Convolutional Neural Network]]
**⚡ Unique Technical**: [[keywords/Fourier Domain Adaptation|Fourier Domain Adaptation]]
**🚀 Evolved Concepts**: [[keywords/Foundation Models|Pathology Foundation Models]]

## 🔗 유사한 논문
- [[Generative_AI_for_Misalignment-Resistant_Virtual_Staining_to_Accelerate_Histopathology_Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (81.3% similar)
- [[Taylor-Series_Expanded_Kolmogorov-Arnold_Network_for_Medical_Imaging_Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (80.8% similar)
- [[Superpose_Task-specific_Features_for_Model_Merging_20250919|Superpose Task-specific Features for Model Merging]] (80.7% similar)
- [[Fine-tuning_Vision_Language_Models_with_Graph-based_Knowledge_for_Explainable_Medical_Image_Analysis_20250919|Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis]] (80.4% similar)
- [[ModalSurv A Multimodal Deep Survival Framework for Prostate and Bladder Cancer]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.02591v3 Announce Type: replace-cross 
Abstract: Mitotic figures are classified into typical and atypical variants, with atypical counts correlating strongly with tumor aggressiveness. Accurate differentiation is therefore essential for patient prognostication and resource allocation, yet remains challenging even for expert pathologists. Here, we leveraged Pathology Foundation Models (PFMs) pre-trained on large histopathology datasets and applied parameter-efficient fine-tuning via low-rank adaptation. In addition, we incorporated ConvNeXt V2, a state-of-the-art convolutional neural network architecture, to complement PFMs. During training, we employed a fisheye transform to emphasize mitoses and Fourier Domain Adaptation using ImageNet target images. Finally, we ensembled multiple PFMs to integrate complementary morphological insights, achieving competitive balanced accuracy on the Preliminary Evaluation Phase dataset.

## 🔍 Abstract (한글 번역)

arXiv:2509.02591v3 발표 유형: 교차 교체  
초록: 유사 분열 상은 전형적 및 비전형적 변종으로 분류되며, 비전형적 수치는 종양의 공격성과 강하게 상관관계가 있습니다. 따라서 정확한 구분은 환자의 예후 평가와 자원 할당에 필수적이지만, 전문가 병리학자에게도 여전히 어려운 과제입니다. 본 연구에서는 대규모 조직병리 데이터셋으로 사전 학습된 병리학 기초 모델(Pathology Foundation Models, PFMs)을 활용하고, 저순위 적응을 통한 파라미터 효율적 미세 조정을 적용했습니다. 또한, PFMs를 보완하기 위해 최첨단 합성곱 신경망 구조인 ConvNeXt V2를 도입했습니다. 훈련 과정에서 우리는 유사 분열을 강조하기 위해 어안 변환을 사용하고, ImageNet 목표 이미지를 사용한 푸리에 도메인 적응을 적용했습니다. 마지막으로, 여러 PFMs를 앙상블하여 상호 보완적인 형태학적 통찰을 통합하여 예비 평가 단계 데이터셋에서 경쟁력 있는 균형 정확도를 달성했습니다.

## 📝 요약

이 논문은 전형적 및 비전형적 유사분열을 분류하는 방법을 제안합니다. 비전형적 유사분열은 종양의 공격성과 강하게 연관되어 있어 정확한 분류가 중요합니다. 연구진은 대규모 병리학 데이터셋으로 사전 학습된 병리학 기초 모델(PFMs)을 활용하고, 저랭크 적응을 통한 효율적인 미세 조정을 적용했습니다. 또한, 최신 컨볼루션 신경망 구조인 ConvNeXt V2를 사용하여 PFMs를 보완했습니다. 학습 과정에서 유사분열을 강조하기 위해 어안 변환과 ImageNet 타겟 이미지를 사용한 푸리에 도메인 적응을 사용했습니다. 여러 PFMs를 앙상블하여 보완적인 형태학적 통찰을 통합함으로써, 예비 평가 단계 데이터셋에서 경쟁력 있는 균형 정확도를 달성했습니다.

## 🎯 주요 포인트

- 1. 비정형 유사분열 수는 종양의 공격성과 강하게 상관관계가 있으며, 정확한 구분이 환자 예후와 자원 배분에 필수적이다.

- 2. 대규모 병리학 데이터셋으로 사전 학습된 병리학 기초 모델(PFMs)을 활용하고, 저순위 적응을 통해 매개변수 효율적인 미세 조정을 수행했다.

- 3. 최첨단 합성곱 신경망 아키텍처인 ConvNeXt V2를 PFMs와 결합하여 성능을 보완했다.

- 4. 훈련 과정에서 유사분열을 강조하기 위해 어안 변환과 ImageNet 대상 이미지를 사용한 푸리에 도메인 적응을 적용했다.

- 5. 여러 PFMs를 앙상블하여 상호 보완적인 형태학적 통찰을 통합하여, Preliminary Evaluation Phase 데이터셋에서 경쟁력 있는 균형 정확도를 달성했다.

---

*Generated on 2025-09-19 15:21:14*