<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:42:35.408380",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Automatic Speech Recognition",
    "Nonverbal Vocalizations",
    "Performative Mandarin Dataset",
    "Expressive Automatic Speech Recognition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Automatic Speech Recognition": 0.78,
    "Nonverbal Vocalizations": 0.82,
    "Performative Mandarin Dataset": 0.85,
    "Expressive Automatic Speech Recognition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Automatic Speech Recognition",
        "canonical": "Automatic Speech Recognition",
        "aliases": [
          "ASR"
        ],
        "category": "broad_technical",
        "rationale": "ASR is a foundational technology in speech processing, relevant for linking to broader technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Nonverbal Vocalizations",
        "canonical": "Nonverbal Vocalizations",
        "aliases": [
          "NVs"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on expanding ASR capabilities to include emotional and intentional cues.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Performative Mandarin Dataset",
        "canonical": "Performative Mandarin Dataset",
        "aliases": [
          "MNV-17"
        ],
        "category": "unique_technical",
        "rationale": "The dataset is a novel contribution to the field, offering new opportunities for research in expressive ASR.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Expressive ASR",
        "canonical": "Expressive Automatic Speech Recognition",
        "aliases": [
          "Expressive ASR"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept represents an evolution in ASR technology, focusing on emotional and nonverbal content.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "speech",
      "dataset",
      "model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Automatic Speech Recognition",
      "resolved_canonical": "Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Nonverbal Vocalizations",
      "resolved_canonical": "Nonverbal Vocalizations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Performative Mandarin Dataset",
      "resolved_canonical": "Performative Mandarin Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Expressive ASR",
      "resolved_canonical": "Expressive Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# MNV-17: A High-Quality Performative Mandarin Dataset for Nonverbal Vocalization Recognition in Speech

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18196.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18196](https://arxiv.org/abs/2509.18196)

## 🔗 유사한 논문
- [[2025-09-23/SynParaSpeech_ Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding_20250923|SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding]] (82.8% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (80.3% similar)
- [[2025-09-19/Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech_20250919|Towards Human-like Multimodal Conversational Agent by Generating Engaging Speech]] (79.7% similar)
- [[2025-09-23/Catching the Details_ Self-Distilled RoI Predictors for Fine-Grained MLLM Perception_20250923|Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception]] (79.4% similar)
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automatic Speech Recognition|Automatic Speech Recognition]]
**⚡ Unique Technical**: [[keywords/Nonverbal Vocalizations|Nonverbal Vocalizations]], [[keywords/Performative Mandarin Dataset|Performative Mandarin Dataset]]
**🚀 Evolved Concepts**: [[keywords/Expressive Automatic Speech Recognition|Expressive Automatic Speech Recognition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18196v1 Announce Type: cross 
Abstract: Mainstream Automatic Speech Recognition (ASR) systems excel at transcribing lexical content, but largely fail to recognize nonverbal vocalizations (NVs) embedded in speech, such as sighs, laughs, and coughs. This capability is important for a comprehensive understanding of human communication, as NVs convey crucial emotional and intentional cues. Progress in NV-aware ASR has been hindered by the lack of high-quality, well-annotated datasets. To address this gap, we introduce MNV-17, a 7.55-hour performative Mandarin speech dataset. Unlike most existing corpora that rely on model-based detection, MNV-17's performative nature ensures high-fidelity, clearly articulated NV instances. To the best of our knowledge, MNV-17 provides the most extensive set of nonverbal vocalization categories, comprising 17 distinct and well-balanced classes of common NVs. We benchmarked MNV-17 on four mainstream ASR architectures, evaluating their joint performance on semantic transcription and NV classification. The dataset and the pretrained model checkpoints will be made publicly available to facilitate future research in expressive ASR.

## 📝 요약

본 연구는 기존 음성 인식 시스템이 언어적 내용은 잘 인식하지만, 한숨, 웃음, 기침 등 비언어적 발성을 인식하는 데 한계를 지닌다는 문제를 해결하고자 한다. 이를 위해 7.55시간 분량의 만다린어 비언어적 발성 데이터셋인 MNV-17을 소개한다. MNV-17은 17개의 다양한 비언어적 발성 카테고리를 포함하며, 기존 데이터셋과 달리 명확하게 발음된 고품질 데이터를 제공한다. 연구에서는 네 가지 주요 음성 인식 아키텍처를 통해 MNV-17의 성능을 평가하였으며, 데이터셋과 사전 학습된 모델을 공개하여 향후 연구를 지원할 예정이다.

## 🎯 주요 포인트

- 1. 기존의 자동 음성 인식 시스템은 비언어적 발성을 인식하는 데 한계가 있다.
- 2. 비언어적 발성은 인간 의사소통에서 중요한 정서적, 의도적 단서를 제공한다.
- 3. MNV-17은 7.55시간 분량의 만다린어 연기형 발화 데이터셋으로, 고품질의 명확한 비언어적 발성 사례를 제공한다.
- 4. MNV-17은 17개의 비언어적 발성 카테고리를 포함하며, 이는 가장 광범위한 범주를 제공한다.
- 5. 데이터셋과 사전 학습된 모델 체크포인트는 향후 연구를 지원하기 위해 공개될 예정이다.


---

*Generated on 2025-09-24 13:42:35*