---
keywords:
  - Mixture of Multicenter Experts
  - Multi-Modal Learning
  - Radiotherapy Target Delineation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2410.00046
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:34:00.709500",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture of Multicenter Experts",
    "Multi-Modal Learning",
    "Radiotherapy Target Delineation"
  ],
  "rejected_keywords": [
    "Few-Shot Learning"
  ],
  "similarity_scores": {
    "Mixture of Multicenter Experts": 0.8,
    "Multi-Modal Learning": 0.82,
    "Radiotherapy Target Delineation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation

**Korean Title:** 다중 모달 AI를 활용한 편향 제거 방사선 치료 표적 윤곽 설정을 위한 다중 센터 전문가의 혼합

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Mixture of Multicenter Experts|Mixture of Multicenter Experts]], [[keywords/Radiotherapy Target Delineation|Radiotherapy Target Delineation]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|Multimodal AI]]

## 🔗 유사한 논문
- [[Semi-MoE Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (83.4% similar)
- [[ModalSurv A Multimodal Deep Survival Framework for Prostate and Bladder Cancer]] (81.8% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (81.6% similar)
- [[CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (81.4% similar)
- [[A_Knowledge-driven_Adaptive_Collaboration_of_LLMs_for_Enhancing_Medical_Decision-making_20250919|A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making]] (81.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.00046v3 Announce Type: replace-cross 
Abstract: Clinical decision-making reflects diverse strategies shaped by regional patient populations and institutional protocols. However, most existing medical artificial intelligence (AI) models are trained on highly prevalent data patterns, which reinforces biases and fails to capture the breadth of clinical expertise. Inspired by the recent advances in Mixture of Experts (MoE), we propose a Mixture of Multicenter Experts (MoME) framework to address AI bias in the medical domain without requiring data sharing across institutions. MoME integrates specialized expertise from diverse clinical strategies to enhance model generalizability and adaptability across medical centers. We validate this framework using a multimodal target volume delineation model for prostate cancer radiotherapy. With few-shot training that combines imaging and clinical notes from each center, the model outperformed baselines, particularly in settings with high inter-center variability or limited data availability. Furthermore, MoME enables model customization to local clinical preferences without cross-institutional data exchange, making it especially suitable for resource-constrained settings while promoting broadly generalizable medical AI.

## 🔍 Abstract (한글 번역)

arXiv:2410.00046v3 발표 유형: 교차 교체  
초록: 임상 의사 결정은 지역 환자 집단과 기관 프로토콜에 의해 형성된 다양한 전략을 반영합니다. 그러나 대부분의 기존 의료 인공지능(AI) 모델은 매우 일반적인 데이터 패턴에 대해 훈련되어 있어 편향을 강화하고 임상 전문 지식의 폭을 포착하지 못합니다. 최근의 전문가 혼합(Mixture of Experts, MoE) 발전에 영감을 받아, 우리는 의료 분야에서 AI 편향을 해결하기 위해 데이터 공유 없이 다기관 전문가 혼합(Mixture of Multicenter Experts, MoME) 프레임워크를 제안합니다. MoME는 다양한 임상 전략에서 전문 지식을 통합하여 의료 센터 전반에서 모델의 일반화 가능성과 적응성을 향상시킵니다. 우리는 전립선암 방사선 치료를 위한 다중 모드 표적 볼륨 윤곽 설정 모델을 사용하여 이 프레임워크를 검증합니다. 각 센터의 영상 및 임상 노트를 결합한 소수 샷 훈련을 통해, 이 모델은 특히 센터 간 변동성이 높거나 데이터 가용성이 제한된 환경에서 기준 모델을 능가했습니다. 또한, MoME는 기관 간 데이터 교환 없이 지역 임상 선호도에 맞춘 모델 맞춤화를 가능하게 하여, 자원이 제한된 환경에서도 특히 적합하며, 널리 일반화 가능한 의료 AI를 촉진합니다.

## 📝 요약

이 논문은 의료 인공지능(AI) 모델의 편향 문제를 해결하기 위해 다중 전문가 혼합(MoME) 프레임워크를 제안합니다. MoME는 다양한 임상 전략의 전문성을 통합하여 모델의 일반화 및 적응성을 향상시킵니다. 전립선암 방사선 치료를 위한 다중 모달 타겟 볼륨 구분 모델을 통해 검증된 결과, MoME는 특히 센터 간 변동성이 크거나 데이터가 제한된 환경에서 우수한 성능을 보였습니다. 또한, 기관 간 데이터 공유 없이도 지역 임상 선호도에 맞춘 모델 맞춤화가 가능하여, 자원이 제한된 환경에서도 활용할 수 있는 일반화된 의료 AI를 촉진합니다.

## 🎯 주요 포인트

- 1. 기존 의료 AI 모델은 주로 일반적인 데이터 패턴에 의존하여 편향을 강화하고 임상 전문성의 다양성을 포착하지 못한다.

- 2. Mixture of Multicenter Experts (MoME) 프레임워크는 기관 간 데이터 공유 없이 의료 분야의 AI 편향을 해결하기 위해 제안되었다.

- 3. MoME는 다양한 임상 전략에서의 전문성을 통합하여 모델의 일반화 가능성과 적응성을 향상시킨다.

- 4. 전립선암 방사선 치료를 위한 다중 모드 목표 부피 구분 모델을 통해 MoME 프레임워크의 유효성이 검증되었다.

- 5. MoME는 자원 제약이 있는 환경에서도 모델을 지역 임상 선호도에 맞게 맞춤화할 수 있어, 광범위하게 일반화 가능한 의료 AI를 촉진한다.

---

*Generated on 2025-09-19 15:42:51*