---
keywords:
  - Wavelet Fourier Diffuser
  - Discrete Wavelet Transform
  - Short-Time Fourier Transform
  - Attention Mechanism
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19305
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:21:24.532929",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Wavelet Fourier Diffuser",
    "Discrete Wavelet Transform",
    "Short-Time Fourier Transform",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Wavelet Fourier Diffuser": 0.88,
    "Discrete Wavelet Transform": 0.82,
    "Short-Time Fourier Transform": 0.85,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Wavelet Fourier Diffuser",
        "canonical": "Wavelet Fourier Diffuser",
        "aliases": [
          "WFDiffuser"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework integrating frequency-domain techniques for reinforcement learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Discrete Wavelet Transform",
        "canonical": "Discrete Wavelet Transform",
        "aliases": [
          "DWT"
        ],
        "category": "broad_technical",
        "rationale": "Key technique for decomposing trajectories into frequency components, relevant across multiple domains.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Short-Time Fourier Transform",
        "canonical": "Short-Time Fourier Transform",
        "aliases": [
          "STFT"
        ],
        "category": "specific_connectable",
        "rationale": "Enhances frequency-domain feature extraction, crucial for cross-frequency interaction in the model.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "cross attention mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "cross attention"
        ],
        "category": "specific_connectable",
        "rationale": "Facilitates cross-frequency interaction, linking to broader attention mechanism concepts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "frequency shift",
      "trajectory instability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Wavelet Fourier Diffuser",
      "resolved_canonical": "Wavelet Fourier Diffuser",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Discrete Wavelet Transform",
      "resolved_canonical": "Discrete Wavelet Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Short-Time Fourier Transform",
      "resolved_canonical": "Short-Time Fourier Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "cross attention mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Wavelet Fourier Diffuser: Frequency-Aware Diffusion Model for Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19305.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19305](https://arxiv.org/abs/2509.19305)

## 🔗 유사한 논문
- [[2025-09-22/DiffusionNFT_ Online Diffusion Reinforcement with Forward Process_20250922|DiffusionNFT: Online Diffusion Reinforcement with Forward Process]] (86.1% similar)
- [[2025-09-24/World4RL_ Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation_20250924|World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation]] (83.0% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.4% similar)
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (82.0% similar)
- [[2025-09-24/APRIL_ Active Partial Rollouts in Reinforcement Learning to tame long-tail generation_20250924|APRIL: Active Partial Rollouts in Reinforcement Learning to tame long-tail generation]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Discrete Wavelet Transform|Discrete Wavelet Transform]]
**🔗 Specific Connectable**: [[keywords/Short-Time Fourier Transform|Short-Time Fourier Transform]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Wavelet Fourier Diffuser|Wavelet Fourier Diffuser]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19305v1 Announce Type: cross 
Abstract: Diffusion probability models have shown significant promise in offline reinforcement learning by directly modeling trajectory sequences. However, existing approaches primarily focus on time-domain features while overlooking frequency-domain features, leading to frequency shift and degraded performance according to our observation. In this paper, we investigate the RL problem from a new perspective of the frequency domain. We first observe that time-domain-only approaches inadvertently introduce shifts in the low-frequency components of the frequency domain, which results in trajectory instability and degraded performance. To address this issue, we propose Wavelet Fourier Diffuser (WFDiffuser), a novel diffusion-based RL framework that integrates Discrete Wavelet Transform to decompose trajectories into low- and high-frequency components. To further enhance diffusion modeling for each component, WFDiffuser employs Short-Time Fourier Transform and cross attention mechanisms to extract frequency-domain features and facilitate cross-frequency interaction. Extensive experiment results on the D4RL benchmark demonstrate that WFDiffuser effectively mitigates frequency shift, leading to smoother, more stable trajectories and improved decision-making performance over existing methods.

## 📝 요약

이 논문은 오프라인 강화 학습에서 주파수 영역의 중요성을 강조하며, 기존의 시간 영역 중심 접근법이 저주파수 성분의 변화를 초래해 성능 저하를 유발한다고 지적합니다. 이를 해결하기 위해, 저자들은 Wavelet Fourier Diffuser(WFDiffuser)라는 새로운 강화 학습 프레임워크를 제안합니다. 이 방법은 이산 웨이블릿 변환을 사용해 경로를 저주파와 고주파 성분으로 분해하고, 단시간 푸리에 변환과 교차 주의 메커니즘을 통해 주파수 영역의 특징을 추출하여 주파수 간 상호작용을 촉진합니다. D4RL 벤치마크 실험 결과, WFDiffuser는 주파수 변화를 효과적으로 완화하여 기존 방법보다 더 안정적이고 향상된 의사결정 성능을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 강화 학습 접근법은 주로 시간 영역의 특징에 집중하여 주파수 이동과 성능 저하를 초래합니다.
- 2. 본 논문은 주파수 영역에서 강화 학습 문제를 새롭게 탐구하며, 시간 영역만을 고려할 경우 저주파수 성분의 이동이 발생함을 관찰했습니다.
- 3. 제안된 Wavelet Fourier Diffuser(WFDiffuser)는 이산 웨이블릿 변환을 사용하여 궤적을 저주파와 고주파 성분으로 분해합니다.
- 4. WFDiffuser는 단시간 푸리에 변환과 교차 주의 메커니즘을 활용하여 주파수 영역의 특징을 추출하고 주파수 간 상호작용을 촉진합니다.
- 5. D4RL 벤치마크 실험 결과, WFDiffuser는 주파수 이동을 효과적으로 완화하여 더 부드럽고 안정적인 궤적과 향상된 의사결정 성능을 보여줍니다.


---

*Generated on 2025-09-25 15:21:24*