---
keywords:
  - Paralinguistic Sounds
  - Speech Generation
  - Paralinguistic Event Detection
  - SynParaSpeech Dataset
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.14946
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:18:38.495874",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Paralinguistic Sounds",
    "Speech Generation",
    "Paralinguistic Event Detection",
    "SynParaSpeech Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Paralinguistic Sounds": 0.78,
    "Speech Generation": 0.8,
    "Paralinguistic Event Detection": 0.77,
    "SynParaSpeech Dataset": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "paralinguistic sounds",
        "canonical": "Paralinguistic Sounds",
        "aliases": [
          "non-verbal sounds",
          "vocal expressions"
        ],
        "category": "unique_technical",
        "rationale": "Paralinguistic sounds are central to the paper's focus on enhancing speech synthesis and understanding.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "speech generation",
        "canonical": "Speech Generation",
        "aliases": [
          "speech synthesis",
          "voice generation"
        ],
        "category": "broad_technical",
        "rationale": "Speech generation is a core component of the study, linking to broader topics in speech technology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "paralinguistic event detection",
        "canonical": "Paralinguistic Event Detection",
        "aliases": [
          "non-verbal event detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task within the paper's framework, crucial for improving speech understanding.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "SynParaSpeech dataset",
        "canonical": "SynParaSpeech Dataset",
        "aliases": [
          "SynParaSpeech corpus"
        ],
        "category": "unique_technical",
        "rationale": "The dataset is a novel contribution of the paper, providing a new resource for the community.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "framework",
      "data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "paralinguistic sounds",
      "resolved_canonical": "Paralinguistic Sounds",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "speech generation",
      "resolved_canonical": "Speech Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "paralinguistic event detection",
      "resolved_canonical": "Paralinguistic Event Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "SynParaSpeech dataset",
      "resolved_canonical": "SynParaSpeech Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14946.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.14946](https://arxiv.org/abs/2509.14946)

## 🔗 유사한 논문
- [[2025-09-19/Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech_20250919|Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech]] (83.3% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (82.4% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (82.4% similar)
- [[2025-09-22/P2VA_ Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech_20250922|P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech]] (80.8% similar)
- [[2025-09-22/Generating Moving 3D Soundscapes with Latent Diffusion Models_20250922|Generating Moving 3D Soundscapes with Latent Diffusion Models]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Speech Generation|Speech Generation]]
**⚡ Unique Technical**: [[keywords/Paralinguistic Sounds|Paralinguistic Sounds]], [[keywords/Paralinguistic Event Detection|Paralinguistic Event Detection]], [[keywords/SynParaSpeech Dataset|SynParaSpeech Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14946v2 Announce Type: replace-cross 
Abstract: Paralinguistic sounds, like laughter and sighs, are crucial for synthesizing more realistic and engaging speech. However, existing methods typically depend on proprietary datasets, while publicly available resources often suffer from incomplete speech, inaccurate or missing timestamps, and limited real-world relevance. To address these problems, we propose an automated framework for generating large-scale paralinguistic data and apply it to construct the SynParaSpeech dataset. The dataset comprises 6 paralinguistic categories with 118.75 hours of data and precise timestamps, all derived from natural conversational speech. Our contributions lie in introducing the first automated method for constructing large-scale paralinguistic datasets and releasing the SynParaSpeech corpus, which advances speech generation through more natural paralinguistic synthesis and enhances speech understanding by improving paralinguistic event detection. The dataset and audio samples are available at https://github.com/ShawnPi233/SynParaSpeech.

## 📝 요약

이 논문은 웃음과 한숨 같은 비언어적 소리를 포함한 자연스러운 음성 합성을 위해 대규모 비언어적 데이터셋을 자동으로 생성하는 프레임워크를 제안합니다. 기존 방법은 제한된 데이터셋에 의존하는 반면, 이 연구는 자연스러운 대화에서 6가지 비언어적 범주와 정확한 타임스탬프를 포함한 118.75시간의 데이터를 제공하는 SynParaSpeech 데이터셋을 구축했습니다. 이는 대규모 비언어적 데이터셋을 자동으로 생성하는 첫 번째 방법론을 제시하고, 자연스러운 비언어적 합성을 통해 음성 생성과 이해를 향상시키는 데 기여합니다. 데이터셋은 GitHub에서 공개됩니다.

## 🎯 주요 포인트

- 1. 웃음과 한숨과 같은 비언어적 소리는 더 현실적이고 매력적인 음성 합성에 중요하다.
- 2. 기존 방법들은 주로 독점 데이터셋에 의존하며, 공개된 자원은 불완전한 음성, 부정확하거나 누락된 타임스탬프, 제한된 현실 세계의 관련성을 가지고 있다.
- 3. 우리는 대규모 비언어적 데이터를 생성하는 자동화된 프레임워크를 제안하고 이를 통해 SynParaSpeech 데이터셋을 구축하였다.
- 4. SynParaSpeech 데이터셋은 자연스러운 대화 음성에서 파생된 6개의 비언어적 범주와 118.75시간의 데이터 및 정확한 타임스탬프를 포함한다.
- 5. 이 연구는 대규모 비언어적 데이터셋을 구축하는 최초의 자동화된 방법을 도입하고, 자연스러운 비언어적 합성을 통해 음성 생성 및 비언어적 이벤트 탐지를 개선한다.


---

*Generated on 2025-09-24 04:18:38*