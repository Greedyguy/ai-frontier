---
keywords:
  - Classifier-Free Guidance
  - Dynamic CFG Scheduling
  - Latent-Space Evaluations
  - Human Preference Reward Model
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16131
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:43:36.219267",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Classifier-Free Guidance",
    "Dynamic CFG Scheduling",
    "Latent-Space Evaluations",
    "Human Preference Reward Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Classifier-Free Guidance": 0.78,
    "Dynamic CFG Scheduling": 0.82,
    "Latent-Space Evaluations": 0.77,
    "Human Preference Reward Model": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Classifier-Free Guidance",
        "canonical": "Classifier-Free Guidance",
        "aliases": [
          "CFG"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution and represents a novel approach to diffusion guidance.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dynamic CFG Scheduling",
        "canonical": "Dynamic CFG Scheduling",
        "aliases": [
          "Dynamic Classifier-Free Guidance Scheduling"
        ],
        "category": "unique_technical",
        "rationale": "The dynamic scheduling of CFG is a key innovation of the paper, providing a new method for adaptive guidance.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Latent-Space Evaluations",
        "canonical": "Latent-Space Evaluations",
        "aliases": [
          "Latent Evaluations"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the feedback mechanism used in the paper's method.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Human Preference Reward Model",
        "canonical": "Human Preference Reward Model",
        "aliases": [
          "Human Preference Model"
        ],
        "category": "specific_connectable",
        "rationale": "This model is used to assess generation quality, linking human feedback with technical evaluation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "framework",
      "model",
      "baseline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Classifier-Free Guidance",
      "resolved_canonical": "Classifier-Free Guidance",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dynamic CFG Scheduling",
      "resolved_canonical": "Dynamic CFG Scheduling",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Latent-Space Evaluations",
      "resolved_canonical": "Latent-Space Evaluations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Human Preference Reward Model",
      "resolved_canonical": "Human Preference Reward Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Dynamic Classifier-Free Diffusion Guidance via Online Feedback

**Korean Title:** 온라인 피드백을 통한 동적 분류기-비자유 확산 안내

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16131.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16131](https://arxiv.org/abs/2509.16131)

## 🔗 유사한 논문
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (83.2% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (81.2% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE: Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (81.0% similar)
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (80.9% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Latent-Space Evaluations|Latent-Space Evaluations]], [[keywords/Human Preference Reward Model|Human Preference Reward Model]]
**⚡ Unique Technical**: [[keywords/Classifier-Free Guidance|Classifier-Free Guidance]], [[keywords/Dynamic CFG Scheduling|Dynamic CFG Scheduling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16131v1 Announce Type: new 
Abstract: Classifier-free guidance (CFG) is a cornerstone of text-to-image diffusion models, yet its effectiveness is limited by the use of static guidance scales. This "one-size-fits-all" approach fails to adapt to the diverse requirements of different prompts; moreover, prior solutions like gradient-based correction or fixed heuristic schedules introduce additional complexities and fail to generalize. In this work, we challeng this static paradigm by introducing a framework for dynamic CFG scheduling. Our method leverages online feedback from a suite of general-purpose and specialized small-scale latent-space evaluations, such as CLIP for alignment, a discriminator for fidelity and a human preference reward model, to assess generation quality at each step of the reverse diffusion process. Based on this feedback, we perform a greedy search to select the optimal CFG scale for each timestep, creating a unique guidance schedule tailored to every prompt and sample. We demonstrate the effectiveness of our approach on both small-scale models and the state-of-the-art Imagen 3, showing significant improvements in text alignment, visual quality, text rendering and numerical reasoning. Notably, when compared against the default Imagen 3 baseline, our method achieves up to 53.8% human preference win-rate for overall preference, a figure that increases up to to 55.5% on prompts targeting specific capabilities like text rendering. Our work establishes that the optimal guidance schedule is inherently dynamic and prompt-dependent, and provides an efficient and generalizable framework to achieve it.

## 🔍 Abstract (한글 번역)

arXiv:2509.16131v1 발표 유형: 신규  
초록: 분류기 없는 안내(CFG)는 텍스트-이미지 확산 모델의 핵심 요소이지만, 정적 안내 척도의 사용으로 인해 그 효과가 제한됩니다. 이러한 "일괄 적용" 접근 방식은 다양한 프롬프트의 요구 사항에 적응하지 못하며, 이전의 해결책인 그래디언트 기반 수정이나 고정된 휴리스틱 일정은 추가적인 복잡성을 초래하고 일반화에 실패합니다. 본 연구에서는 동적 CFG 스케줄링을 위한 프레임워크를 도입하여 이러한 정적 패러다임에 도전합니다. 우리의 방법은 CLIP을 통한 정렬, 충실도를 위한 판별기, 인간 선호 보상 모델 등 일반 목적 및 특수 소규모 잠재 공간 평가 도구에서의 온라인 피드백을 활용하여 역 확산 과정의 각 단계에서 생성 품질을 평가합니다. 이 피드백을 기반으로, 우리는 각 시간 단계에 최적의 CFG 척도를 선택하기 위해 탐욕적 검색을 수행하여, 각 프롬프트와 샘플에 맞춘 독특한 안내 일정을 생성합니다. 우리는 소규모 모델과 최첨단 Imagen 3에서 우리의 접근 방식의 효과를 입증하며, 텍스트 정렬, 시각적 품질, 텍스트 렌더링 및 수치적 추론에서 상당한 개선을 보여줍니다. 특히, 기본 Imagen 3 기준선과 비교했을 때, 우리의 방법은 전체 선호도에서 최대 53.8%의 인간 선호 승률을 달성하며, 텍스트 렌더링과 같은 특정 기능을 목표로 하는 프롬프트에서는 최대 55.5%까지 증가합니다. 우리의 연구는 최적의 안내 일정이 본질적으로 동적이며 프롬프트에 의존적임을 확립하고, 이를 달성하기 위한 효율적이고 일반화 가능한 프레임워크를 제공합니다.

## 📝 요약

이 논문은 텍스트-이미지 변환 모델에서 사용되는 정적 분류기-프리 가이던스(CFG)의 한계를 극복하기 위해 동적 CFG 스케줄링 프레임워크를 제안합니다. 기존의 정적 접근 방식은 다양한 프롬프트의 요구에 적절히 대응하지 못하며, 이전의 해결책들은 복잡성을 증가시키고 일반화에 실패했습니다. 제안된 방법은 CLIP, 판별기, 인간 선호 보상 모델 등의 평가를 통해 생성 품질을 실시간으로 피드백 받고, 각 시간 단계에서 최적의 CFG 스케일을 선택하는 탐욕적 검색을 수행합니다. 이를 통해 프롬프트와 샘플에 맞춘 독특한 가이던스 스케줄을 생성합니다. 실험 결과, 제안된 방법은 텍스트 정렬, 시각적 품질, 텍스트 렌더링 및 수치적 추론에서 개선을 보였으며, 특히 Imagen 3와 비교 시 최대 55.5%의 인간 선호도를 기록했습니다. 이 연구는 최적의 가이던스 스케줄이 동적이며 프롬프트에 의존적임을 입증하고, 이를 효율적으로 달성할 수 있는 일반화 가능한 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 텍스트-이미지 변환 모델에서 정적 가이드 스케일의 한계를 극복하기 위해 동적 CFG 스케줄링 프레임워크를 제안합니다.
- 2. 제안된 방법은 CLIP, 판별기, 인간 선호 보상 모델 등을 활용하여 역확산 과정의 각 단계에서 생성 품질을 평가합니다.
- 3. 각 타임스텝에 최적의 CFG 스케일을 선택하여 프롬프트와 샘플에 맞춘 고유한 가이드 스케줄을 생성합니다.
- 4. 제안된 방법은 텍스트 정렬, 시각적 품질, 텍스트 렌더링 및 수치적 추론에서 유의미한 개선을 보여줍니다.
- 5. 기본 Imagen 3와 비교하여, 제안된 방법은 전체 선호도에서 최대 53.8%의 인간 선호 승률을 기록하며, 특정 기능을 목표로 하는 프롬프트에서는 최대 55.5%까지 증가합니다.


---

*Generated on 2025-09-23 10:43:36*