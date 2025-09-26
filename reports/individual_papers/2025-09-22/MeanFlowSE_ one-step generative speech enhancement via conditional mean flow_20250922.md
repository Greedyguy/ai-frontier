---
keywords:
  - MeanFlowSE
  - Generative Speech Enhancement
  - Flow-Based Systems
  - Jacobian-Vector Product
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.14858
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:17:05.581304",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MeanFlowSE",
    "Generative Speech Enhancement",
    "Flow-Based Systems",
    "Jacobian-Vector Product"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MeanFlowSE": 0.8,
    "Generative Speech Enhancement": 0.78,
    "Flow-Based Systems": 0.72,
    "Jacobian-Vector Product": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MeanFlowSE",
        "canonical": "MeanFlowSE",
        "aliases": [
          "Mean Flow Speech Enhancement"
        ],
        "category": "unique_technical",
        "rationale": "MeanFlowSE is a novel approach in generative speech enhancement, offering a unique method for real-time applications.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "generative speech enhancement",
        "canonical": "Generative Speech Enhancement",
        "aliases": [
          "speech enhancement",
          "generative enhancement"
        ],
        "category": "specific_connectable",
        "rationale": "This term directly relates to the core application of the paper, connecting it to broader speech processing research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "flow-based systems",
        "canonical": "Flow-Based Systems",
        "aliases": [
          "flow systems"
        ],
        "category": "specific_connectable",
        "rationale": "Flow-based systems are a key component in the methodology, linking to other flow-related research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Jacobian-vector product",
        "canonical": "Jacobian-Vector Product",
        "aliases": [
          "JVP"
        ],
        "category": "specific_connectable",
        "rationale": "The Jacobian-vector product is crucial for the proposed method, connecting to mathematical optimization techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MeanFlowSE",
      "resolved_canonical": "MeanFlowSE",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "generative speech enhancement",
      "resolved_canonical": "Generative Speech Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "flow-based systems",
      "resolved_canonical": "Flow-Based Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Jacobian-vector product",
      "resolved_canonical": "Jacobian-Vector Product",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MeanFlowSE: one-step generative speech enhancement via conditional mean flow

**Korean Title:** MeanFlowSE: 조건부 평균 흐름을 통한 일단계 생성적 음성 향상

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14858.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.14858](https://arxiv.org/abs/2509.14858)

## 🔗 유사한 논문
- [[2025-09-22/Compose Yourself_ Average-Velocity Flow Matching for One-Step Speech Enhancement_20250922|Compose Yourself: Average-Velocity Flow Matching for One-Step Speech Enhancement]] (89.3% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (83.5% similar)
- [[2025-09-19/Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (81.1% similar)
- [[2025-09-22/FLOAT_ Generative Motion Latent Flow Matching for Audio-driven Talking Portrait_20250922|FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait]] (81.0% similar)
- [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Generative Speech Enhancement|Generative Speech Enhancement]], [[keywords/Flow-Based Systems|Flow-Based Systems]], [[keywords/Jacobian-Vector Product|Jacobian-Vector Product]]
**⚡ Unique Technical**: [[keywords/MeanFlowSE|MeanFlowSE]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14858v2 Announce Type: replace-cross 
Abstract: Multistep inference is a bottleneck for real-time generative speech enhancement because flow- and diffusion-based systems learn an instantaneous velocity field and therefore rely on iterative ordinary differential equation (ODE) solvers. We introduce MeanFlowSE, a conditional generative model that learns the average velocity over finite intervals along a trajectory. Using a Jacobian-vector product (JVP) to instantiate the MeanFlow identity, we derive a local training objective that directly supervises finite-interval displacement while remaining consistent with the instantaneous-field constraint on the diagonal. At inference, MeanFlowSE performs single-step generation via a backward-in-time displacement, removing the need for multistep solvers; an optional few-step variant offers additional refinement. On VoiceBank-DEMAND, the single-step model achieves strong intelligibility, fidelity, and perceptual quality with substantially lower computational cost than multistep baselines. The method requires no knowledge distillation or external teachers, providing an efficient, high-fidelity framework for real-time generative speech enhancement. The proposed method is open-sourced at https://github.com/liduojia1/MeanFlowSE.

## 🔍 Abstract (한글 번역)

arXiv:2509.14858v2 발표 유형: 교차 대체  
초록: 다단계 추론은 실시간 생성 음성 향상에 있어 병목 현상으로 작용합니다. 이는 흐름 및 확산 기반 시스템이 순간 속도장을 학습하고, 따라서 반복적인 상미분방정식(ODE) 해석기에 의존하기 때문입니다. 우리는 경로를 따라 유한 구간 동안 평균 속도를 학습하는 조건부 생성 모델인 MeanFlowSE를 소개합니다. MeanFlow 정체성을 구현하기 위해 야코비안-벡터 곱(JVP)을 사용하여, 대각선에서 순간 필드 제약 조건과 일치하면서 유한 구간 변위를 직접 감독하는 지역 학습 목표를 도출합니다. 추론 시, MeanFlowSE는 시간 역방향 변위를 통해 단일 단계 생성을 수행하여 다단계 해석기의 필요성을 제거합니다. 선택적으로 몇 단계의 변형을 통해 추가적인 정제를 제공합니다. VoiceBank-DEMAND 데이터셋에서 단일 단계 모델은 다단계 기준선보다 훨씬 낮은 계산 비용으로 강력한 명료성, 충실도 및 지각적 품질을 달성합니다. 이 방법은 지식 증류나 외부 교사가 필요하지 않으며, 실시간 생성 음성 향상을 위한 효율적이고 고충실도의 프레임워크를 제공합니다. 제안된 방법은 https://github.com/liduojia1/MeanFlowSE에서 오픈 소스로 제공됩니다.

## 📝 요약

MeanFlowSE는 실시간 생성 음성 향상을 위한 조건부 생성 모델로, 다단계 추론의 병목 문제를 해결합니다. 이 모델은 경로를 따라 유한 구간의 평균 속도를 학습하며, Jacobian-벡터 곱을 활용해 유한 구간 변위를 직접 감독하는 지역 학습 목표를 도출합니다. 추론 시, MeanFlowSE는 시간 역방향 변위를 통해 단일 단계로 생성하여 다단계 해석기를 제거하며, 선택적으로 몇 단계의 추가 정제를 제공합니다. VoiceBank-DEMAND 데이터셋에서 단일 단계 모델은 높은 명료도, 충실도, 지각적 품질을 유지하면서도 다단계 기준보다 계산 비용이 현저히 낮습니다. 이 방법은 지식 증류나 외부 교사가 필요 없으며, 효율적이고 고품질의 실시간 생성 음성 향상 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. MeanFlowSE는 실시간 생성 음성 향상을 위한 다단계 추론의 병목 현상을 해결하는 조건부 생성 모델입니다.
- 2. 이 모델은 경로를 따라 유한 구간 동안 평균 속도를 학습하여 단일 단계 생성이 가능하며, 다단계 해석기가 필요하지 않습니다.
- 3. VoiceBank-DEMAND 데이터셋에서 단일 단계 모델은 높은 명료도, 충실도 및 지각적 품질을 달성하면서도 다단계 기준보다 계산 비용이 현저히 낮습니다.
- 4. MeanFlowSE는 지식 증류나 외부 교사가 필요하지 않으며, 실시간 생성 음성 향상을 위한 효율적이고 고충실도의 프레임워크를 제공합니다.
- 5. 제안된 방법은 오픈 소스로 제공되며, GitHub에서 확인할 수 있습니다.


---

*Generated on 2025-09-23 10:17:05*