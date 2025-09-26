---
keywords:
  - Diffusion-based Speech Enhancement
  - Generative Artifacts
  - Semantic Consistency
  - Phonetic Accuracy
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19495
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:36:58.905823",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion-based Speech Enhancement",
    "Generative Artifacts",
    "Semantic Consistency",
    "Phonetic Accuracy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion-based Speech Enhancement": 0.78,
    "Generative Artifacts": 0.77,
    "Semantic Consistency": 0.75,
    "Phonetic Accuracy": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion-based Speech Enhancement",
        "canonical": "Diffusion-based Speech Enhancement",
        "aliases": [
          "Diffusion SE",
          "Diffusion Speech Enhancement"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific method discussed in the paper that addresses generative artifacts in speech processing, providing a unique technical focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Generative Artifacts",
        "canonical": "Generative Artifacts",
        "aliases": [
          "Artifacts in Generation",
          "Generative Errors"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on detecting and reducing these artifacts, making it a central theme for linking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Semantic Consistency",
        "canonical": "Semantic Consistency",
        "aliases": [
          "Semantic Coherence"
        ],
        "category": "specific_connectable",
        "rationale": "Semantic consistency is crucial for improving phonetic accuracy and is applicable across various NLP tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      },
      {
        "surface": "Phonetic Accuracy",
        "canonical": "Phonetic Accuracy",
        "aliases": [
          "Phonetic Precision"
        ],
        "category": "specific_connectable",
        "rationale": "Improving phonetic accuracy is a key outcome of the proposed method, relevant for linking to speech processing research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.76,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "inference",
      "analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion-based Speech Enhancement",
      "resolved_canonical": "Diffusion-based Speech Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Generative Artifacts",
      "resolved_canonical": "Generative Artifacts",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Semantic Consistency",
      "resolved_canonical": "Semantic Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Phonetic Accuracy",
      "resolved_canonical": "Phonetic Accuracy",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.76,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# ArtiFree: Detecting and Reducing Generative Artifacts in Diffusion-based Speech Enhancement

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19495.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19495](https://arxiv.org/abs/2509.19495)

## 🔗 유사한 논문
- [[2025-09-23/Extract and Diffuse_ Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement_20250923|Extract and Diffuse: Latent Integration for Improved Diffusion-based Speech and Vocal Enhancement]] (83.4% similar)
- [[2025-09-23/Leveraging Multiple Speech Enhancers for Non-Intrusive Intelligibility Prediction for Hearing-Impaired Listeners_20250923|Leveraging Multiple Speech Enhancers for Non-Intrusive Intelligibility Prediction for Hearing-Impaired Listeners]] (82.9% similar)
- [[2025-09-24/SynSonic_ Augmenting Sound Event Detection through Text-to-Audio Diffusion ControlNet and Effective Sample Filtering_20250924|SynSonic: Augmenting Sound Event Detection through Text-to-Audio Diffusion ControlNet and Effective Sample Filtering]] (82.2% similar)
- [[2025-09-19/Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (81.9% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic Consistency|Semantic Consistency]], [[keywords/Phonetic Accuracy|Phonetic Accuracy]]
**⚡ Unique Technical**: [[keywords/Diffusion-based Speech Enhancement|Diffusion-based Speech Enhancement]], [[keywords/Generative Artifacts|Generative Artifacts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19495v1 Announce Type: cross 
Abstract: Diffusion-based speech enhancement (SE) achieves natural-sounding speech and strong generalization, yet suffers from key limitations like generative artifacts and high inference latency. In this work, we systematically study artifact prediction and reduction in diffusion-based SE. We show that variance in speech embeddings can be used to predict phonetic errors during inference. Building on these findings, we propose an ensemble inference method guided by semantic consistency across multiple diffusion runs. This technique reduces WER by 15% in low-SNR conditions, effectively improving phonetic accuracy and semantic plausibility. Finally, we analyze the effect of the number of diffusion steps, showing that adaptive diffusion steps balance artifact suppression and latency. Our findings highlight semantic priors as a powerful tool to guide generative SE toward artifact-free outputs.

## 📝 요약

이 논문은 확산 기반 음성 향상(SE)의 문제점인 생성 아티팩트와 높은 추론 지연을 해결하기 위해 연구를 진행했습니다. 연구에서는 음성 임베딩의 분산을 통해 추론 시 발생하는 음운 오류를 예측할 수 있음을 보여주었습니다. 이를 바탕으로, 여러 확산 실행 간의 의미적 일관성을 활용한 앙상블 추론 방법을 제안하여, 낮은 신호 대 잡음비(SNR) 조건에서 단어 오류율(WER)을 15% 감소시켰습니다. 또한, 확산 단계 수가 아티팩트 억제와 지연 시간 사이의 균형을 맞추는 데 중요한 역할을 한다는 것을 분석했습니다. 이 연구는 의미적 선행 지식이 생성 SE를 아티팩트 없는 출력으로 유도하는 강력한 도구임을 강조합니다.

## 🎯 주요 포인트

- 1. 확산 기반 음성 향상(SE)은 자연스러운 음성을 생성하지만 생성 아티팩트와 높은 추론 지연이라는 한계를 가집니다.
- 2. 음성 임베딩의 분산을 통해 추론 중 음성 오류를 예측할 수 있음을 보였습니다.
- 3. 여러 확산 실행 간의 의미적 일관성을 활용한 앙상블 추론 방법을 제안하여 낮은 SNR 조건에서 WER을 15% 감소시켰습니다.
- 4. 적응형 확산 단계가 아티팩트 억제와 지연 시간을 균형 있게 조절함을 분석했습니다.
- 5. 의미적 우선순위가 생성 SE를 아티팩트 없는 출력으로 유도하는 강력한 도구임을 강조했습니다.


---

*Generated on 2025-09-25 15:36:58*