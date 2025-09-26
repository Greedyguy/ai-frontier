---
keywords:
  - Diffusion-based Large Language Models
  - Automatic Speech Recognition
  - Whisper-LLaMA
  - Audio-conditioned Embeddings
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16622
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:29:07.589726",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion-based Large Language Models",
    "Automatic Speech Recognition",
    "Whisper-LLaMA",
    "Audio-conditioned Embeddings"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion-based Large Language Models": 0.78,
    "Automatic Speech Recognition": 0.82,
    "Whisper-LLaMA": 0.7,
    "Audio-conditioned Embeddings": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion-based Large Language Models",
        "canonical": "Diffusion-based Large Language Models",
        "aliases": [
          "DLLMs",
          "Diffusion LLMs"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel approach in language models, distinct from autoregressive models, and is central to the paper's contributions.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Automatic Speech Recognition",
        "canonical": "Automatic Speech Recognition",
        "aliases": [
          "ASR"
        ],
        "category": "broad_technical",
        "rationale": "ASR is a fundamental application area for language models, providing a key context for linking related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Whisper-LLaMA",
        "canonical": "Whisper-LLaMA",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This specific model is a focal point of the study, making it crucial for understanding the paper's experimental setup.",
        "novelty_score": 0.75,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Audio-conditioned Embeddings",
        "canonical": "Audio-conditioned Embeddings",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "These embeddings are critical for improving ASR accuracy, highlighting the importance of multimodal approaches.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "empirical study",
      "baseline",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion-based Large Language Models",
      "resolved_canonical": "Diffusion-based Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Automatic Speech Recognition",
      "resolved_canonical": "Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Whisper-LLaMA",
      "resolved_canonical": "Whisper-LLaMA",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Audio-conditioned Embeddings",
      "resolved_canonical": "Audio-conditioned Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Audio-Conditioned Diffusion LLMs for ASR and Deliberation Processing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16622.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16622](https://arxiv.org/abs/2509.16622)

## 🔗 유사한 논문
- [[2025-09-22/Discrete Diffusion in Large Language and Multimodal Models_ A Survey_20250922|Discrete Diffusion in Large Language and Multimodal Models: A Survey]] (85.2% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (82.7% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.3% similar)
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (82.2% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automatic Speech Recognition|Automatic Speech Recognition]]
**🔗 Specific Connectable**: [[keywords/Audio-conditioned Embeddings|Audio-conditioned Embeddings]]
**⚡ Unique Technical**: [[keywords/Diffusion-based Large Language Models|Diffusion-based Large Language Models]], [[keywords/Whisper-LLaMA|Whisper-LLaMA]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16622v1 Announce Type: cross 
Abstract: Diffusion-based large language models (DLLMs) have recently attracted growing interest as an alternative to autoregressive decoders. In this work, we present an empirical study on using the diffusion-based large language model LLaDA for automatic speech recognition (ASR). We first investigate its use as an external deliberation-based processing module for Whisper-LLaMA transcripts. By leveraging the bidirectional attention and denoising capabilities of LLaDA, we explore random masking, low-confidence masking, and semi-autoregressive strategies, showing that Whisper-LLaDA substantially reduces WER compared with the baseline. On LibriSpeech, the best cascade system achieves 2.25%/4.94% WER on test-clean/test-other, representing a 12.3% relative improvement over the Whisper-LLaMA baseline on the test-other split. In contrast, a plain-text LLaDA without acoustic features fails to improve accuracy, highlighting the importance of audio-conditioned embeddings. We further evaluate Whisper-LLaDA as a standalone decoder for ASR with diffusion-based and semi-autoregressive decoding. Most experimental configurations achieve faster inference than the Whisper-LLaMA baseline, although recognition accuracy is slightly lower. These findings offer an empirical view of diffusion-based LLMs for ASR and point to promising directions for improvements.

## 📝 요약

이 연구는 확산 기반 대형 언어 모델(DLLM)인 LLaDA를 자동 음성 인식(ASR)에 활용한 실증적 연구를 다룹니다. LLaDA의 양방향 주의 메커니즘과 잡음 제거 기능을 활용하여 Whisper-LLaMA의 성능을 개선하고자 했습니다. 랜덤 마스킹, 저신뢰도 마스킹, 반자기회귀 전략을 통해 WER(단어 오류율)을 크게 줄였으며, LibriSpeech 데이터셋에서 12.3%의 상대적 개선을 이루었습니다. 또한, LLaDA를 독립적인 디코더로 사용했을 때, 인식 속도는 빨라졌지만 정확도는 약간 낮았습니다. 이 연구는 ASR에 대한 확산 기반 LLM의 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 확산 기반 대형 언어 모델(DLLMs)은 자동 회귀 디코더의 대안으로 주목받고 있다.
- 2. LLaDA 모델을 활용하여 Whisper-LLaMA 성능을 개선하고 WER을 크게 줄였다.
- 3. LibriSpeech 데이터셋에서 Whisper-LLaDA는 test-clean/test-other에서 각각 2.25%/4.94%의 WER을 기록하며, test-other에서 12.3%의 상대적 개선을 보였다.
- 4. 오디오 조건 임베딩의 중요성이 강조되며, 음향 특징이 없는 LLaDA는 정확도 향상에 실패했다.
- 5. Whisper-LLaDA는 확산 기반 및 반자동 회귀 디코딩을 통해 독립적인 디코더로서 빠른 추론 속도를 보였으나, 인식 정확도는 약간 낮았다.


---

*Generated on 2025-09-23 23:29:07*