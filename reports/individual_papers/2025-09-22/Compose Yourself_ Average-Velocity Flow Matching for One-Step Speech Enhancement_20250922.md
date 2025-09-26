---
keywords:
  - Speech Enhancement
  - Diffusion and Flow Matching
  - MeanFlow
  - One-Step Generative Modeling
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15952
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:22:26.251564",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Speech Enhancement",
    "Diffusion and Flow Matching",
    "MeanFlow",
    "One-Step Generative Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Speech Enhancement": 0.78,
    "Diffusion and Flow Matching": 0.7,
    "MeanFlow": 0.75,
    "One-Step Generative Modeling": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "speech enhancement",
        "canonical": "Speech Enhancement",
        "aliases": [
          "SE"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area that connects with various audio processing and machine learning techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "diffusion and flow matching",
        "canonical": "Diffusion and Flow Matching",
        "aliases": [
          "FM"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific technique in generative modeling relevant to the paper's methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "MeanFlow",
        "canonical": "MeanFlow",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific model referenced in the paper, indicating a novel approach in one-step generative modeling.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "one-step generative modeling",
        "canonical": "One-Step Generative Modeling",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights a significant advancement in generative modeling techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "speech enhancement",
      "resolved_canonical": "Speech Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "diffusion and flow matching",
      "resolved_canonical": "Diffusion and Flow Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "MeanFlow",
      "resolved_canonical": "MeanFlow",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "one-step generative modeling",
      "resolved_canonical": "One-Step Generative Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Compose Yourself: Average-Velocity Flow Matching for One-Step Speech Enhancement

**Korean Title:** "Compose Yourself: Average-Velocity Flow Matching for One-Step Speech Enhancement"의 번역은 다음과 같습니다:

"자신을 구성하라: 일단계 음성 향상을 위한 평균 속도 흐름 매칭"

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15952.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15952](https://arxiv.org/abs/2509.15952)

## 🔗 유사한 논문
- [[2025-09-19/MeanFlowSE_ one-step generative speech enhancement via conditional mean flow_20250919|MeanFlowSE: one-step generative speech enhancement via conditional mean flow]] (89.3% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (81.9% similar)
- [[2025-09-22/FLOAT_ Generative Motion Latent Flow Matching for Audio-driven Talking Portrait_20250922|FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait]] (81.1% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (80.3% similar)
- [[2025-09-22/FocalCodec-Stream_ Streaming Low-Bitrate Speech Coding via Causal Distillation_20250922|FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Speech Enhancement|Speech Enhancement]], [[keywords/One-Step Generative Modeling|One-Step Generative Modeling]]
**⚡ Unique Technical**: [[keywords/Diffusion and Flow Matching|Diffusion and Flow Matching]], [[keywords/MeanFlow|MeanFlow]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15952v1 Announce Type: cross 
Abstract: Diffusion and flow matching (FM) models have achieved remarkable progress in speech enhancement (SE), yet their dependence on multi-step generation is computationally expensive and vulnerable to discretization errors. Recent advances in one-step generative modeling, particularly MeanFlow, provide a promising alternative by reformulating dynamics through average velocity fields. In this work, we present COSE, a one-step FM framework tailored for SE. To address the high training overhead of Jacobian-vector product (JVP) computations in MeanFlow, we introduce a velocity composition identity to compute average velocity efficiently, eliminating expensive computation while preserving theoretical consistency and achieving competitive enhancement quality. Extensive experiments on standard benchmarks show that COSE delivers up to 5x faster sampling and reduces training cost by 40%, all without compromising speech quality. Code is available at https://github.com/ICDM-UESTC/COSE.

## 🔍 Abstract (한글 번역)

arXiv:2509.15952v1 발표 유형: 교차  
초록: 확산 및 흐름 매칭(FM) 모델은 음성 향상(SE) 분야에서 놀라운 발전을 이루었지만, 다단계 생성에 의존하기 때문에 계산 비용이 많이 들고 이산화 오류에 취약합니다. 최근의 일단계 생성 모델링, 특히 MeanFlow의 발전은 평균 속도장을 통해 동역학을 재구성함으로써 유망한 대안을 제공합니다. 이 연구에서는 SE에 맞춘 일단계 FM 프레임워크인 COSE를 제시합니다. MeanFlow에서 야코비안-벡터 곱(JVP) 계산의 높은 훈련 오버헤드를 해결하기 위해, 평균 속도를 효율적으로 계산하는 속도 구성 정체성을 도입하여 비용이 많이 드는 계산을 제거하면서 이론적 일관성을 유지하고 경쟁력 있는 향상 품질을 달성합니다. 표준 벤치마크에 대한 광범위한 실험 결과, COSE는 샘플링 속도를 최대 5배까지 향상시키고 훈련 비용을 40% 절감하며, 음성 품질을 손상시키지 않습니다. 코드는 https://github.com/ICDM-UESTC/COSE에서 제공됩니다.

## 📝 요약

이 논문에서는 COSE라는 새로운 일단계 흐름 맞춤(FM) 프레임워크를 제안하여, 다단계 생성에 의존하는 기존의 방법론보다 더 효율적인 음성 향상을 달성합니다. MeanFlow의 평균 속도장을 활용한 새로운 접근법을 통해, Jacobian-벡터 곱(JVP) 계산의 높은 훈련 비용을 줄이면서도 이론적 일관성을 유지하고 경쟁력 있는 음성 향상 품질을 제공합니다. 실험 결과, COSE는 표준 벤치마크에서 최대 5배 빠른 샘플링 속도와 40%의 훈련 비용 절감을 달성하였으며, 음성 품질을 저하시키지 않았습니다.

## 🎯 주요 포인트

- 1. COSE는 다단계 생성의 계산 비용 문제를 해결하기 위해 설계된 일단계 흐름 매칭(FM) 프레임워크입니다.
- 2. MeanFlow의 고비용 Jacobian-벡터 곱(JVP) 계산 문제를 해결하기 위해 평균 속도를 효율적으로 계산하는 속도 구성 정체성을 도입했습니다.
- 3. COSE는 최대 5배 빠른 샘플링 속도를 제공하며, 훈련 비용을 40% 절감하면서도 음성 품질을 유지합니다.
- 4. COSE의 성능은 표준 벤치마크 실험에서 경쟁력 있는 개선 품질을 보여주었습니다.
- 5. COSE의 코드는 https://github.com/ICDM-UESTC/COSE에서 제공됩니다.


---

*Generated on 2025-09-23 09:22:26*