---
keywords:
  - Diffusion Models
  - Sparse-view CT Reconstruction
  - Generative Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14566
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:50:27.562853",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Sparse-view CT Reconstruction",
    "Generative Models"
  ],
  "rejected_keywords": [
    "Consensus Equilibrium"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.8,
    "Sparse-view CT Reconstruction": 0.78,
    "Generative Models": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# DICE: Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction

**Korean Title:** DICE: 희소 뷰 CT 재구성을 위한 확산 합의 평형

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Generative Models|Generative Models]]
**⚡ Unique Technical**: [[keywords/Sparse-view CT Reconstruction|Sparse-view CT Reconstruction]]

## 🔗 유사한 논문
- [[Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (85.5% similar)
- [[PRISM-DP Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (78.9% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (78.6% similar)
- [[ColonCrafter A Depth Estimation Model for Colonoscopy Videos Using Diffusion Priors]] (78.1% similar)
- [[Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (78.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14566v1 Announce Type: new 
Abstract: Sparse-view computed tomography (CT) reconstruction is fundamentally challenging due to undersampling, leading to an ill-posed inverse problem. Traditional iterative methods incorporate handcrafted or learned priors to regularize the solution but struggle to capture the complex structures present in medical images. In contrast, diffusion models (DMs) have recently emerged as powerful generative priors that can accurately model complex image distributions. In this work, we introduce Diffusion Consensus Equilibrium (DICE), a framework that integrates a two-agent consensus equilibrium into the sampling process of a DM. DICE alternates between: (i) a data-consistency agent, implemented through a proximal operator enforcing measurement consistency, and (ii) a prior agent, realized by a DM performing a clean image estimation at each sampling step. By balancing these two complementary agents iteratively, DICE effectively combines strong generative prior capabilities with measurement consistency. Experimental results show that DICE significantly outperforms state-of-the-art baselines in reconstructing high-quality CT images under uniform and non-uniform sparse-view settings of 15, 30, and 60 views (out of a total of 180), demonstrating both its effectiveness and robustness.

## 🔍 Abstract (한글 번역)

arXiv:2509.14566v1 발표 유형: 신규  
초록: 스파스 뷰 컴퓨터 단층 촬영(CT) 재구성은 표본 추출이 부족하여 부정정 역문제가 발생하기 때문에 근본적으로 도전적입니다. 전통적인 반복적 방법은 수작업으로 설계되거나 학습된 사전 정보를 통합하여 솔루션을 정규화하지만, 의료 이미지에 존재하는 복잡한 구조를 포착하는 데 어려움을 겪습니다. 반면, 확산 모델(DMs)은 최근 복잡한 이미지 분포를 정확하게 모델링할 수 있는 강력한 생성 사전으로 부상했습니다. 본 연구에서는 확산 합의 평형(DICE)을 소개합니다. 이는 DM의 샘플링 과정에 두 에이전트 합의 평형을 통합하는 프레임워크입니다. DICE는 다음을 번갈아 수행합니다: (i) 측정 일관성을 강제하는 근접 연산자를 통해 구현된 데이터 일관성 에이전트와 (ii) 각 샘플링 단계에서 깨끗한 이미지 추정을 수행하는 DM에 의해 실현된 사전 에이전트. 이 두 상호 보완적인 에이전트를 반복적으로 균형 있게 조정함으로써, DICE는 강력한 생성 사전 능력과 측정 일관성을 효과적으로 결합합니다. 실험 결과, DICE는 15, 30 및 60 뷰(총 180 뷰 중)에서의 균일 및 비균일 스파스 뷰 설정 하에서 고품질 CT 이미지를 재구성하는 데 있어 최첨단 기준을 크게 능가하며, 그 효과성과 견고성을 입증합니다.

## 📝 요약

이 논문은 희소 뷰 컴퓨터 단층 촬영(CT) 재구성을 위한 새로운 프레임워크인 Diffusion Consensus Equilibrium (DICE)를 제안합니다. DICE는 두 에이전트 간의 합의 균형을 통해 샘플링 과정을 개선합니다. 첫 번째 에이전트는 측정 일관성을 보장하는 데이터 일관성 에이전트이며, 두 번째 에이전트는 복잡한 이미지 분포를 정확하게 모델링하는 확산 모델(DM)입니다. 이 두 에이전트를 반복적으로 균형 있게 조합하여, DICE는 강력한 생성적 사전과 측정 일관성을 효과적으로 결합합니다. 실험 결과, DICE는 15, 30, 60개의 뷰를 사용하는 희소 뷰 설정에서 최첨단 기법보다 뛰어난 CT 이미지 재구성 성능을 보여주었습니다.

## 🎯 주요 포인트

- 1. 희소 뷰 CT 재구성 문제는 샘플링 부족으로 인해 본질적으로 어려운 반전 문제를 형성합니다.

- 2. 전통적인 반복 방법은 수작업 또는 학습된 사전 지식을 사용하여 솔루션을 정규화하지만, 의료 이미지의 복잡한 구조를 포착하는 데 어려움을 겪습니다.

- 3. 본 연구에서는 두 에이전트 합의 균형을 DM 샘플링 과정에 통합한 DICE 프레임워크를 소개합니다.

- 4. DICE는 데이터 일관성 에이전트와 사전 에이전트를 번갈아 사용하여 강력한 생성 사전 능력과 측정 일관성을 효과적으로 결합합니다.

- 5. 실험 결과, DICE는 15, 30, 60개의 뷰 설정에서 최첨단 기준을 크게 능가하여 높은 품질의 CT 이미지를 재구성하는 데 효과적이고 견고함을 입증합니다.

---

*Generated on 2025-09-19 16:04:01*