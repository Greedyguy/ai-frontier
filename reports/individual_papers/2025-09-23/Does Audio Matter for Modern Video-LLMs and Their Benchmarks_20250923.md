---
keywords:
  - Vision-Language Model
  - Audio-Sensitive Evaluation
  - Audio Encoder
  - Audio-Visual Question Answering
  - Token Compression
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17901
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:05:26.515976",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Audio-Sensitive Evaluation",
    "Audio Encoder",
    "Audio-Visual Question Answering",
    "Token Compression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Audio-Sensitive Evaluation": 0.78,
    "Audio Encoder": 0.8,
    "Audio-Visual Question Answering": 0.77,
    "Token Compression": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Video-LLMs",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Video Large Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "This term represents a key concept in the paper, linking vision and language processing in multimodal contexts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "audio-sensitive subsets",
        "canonical": "Audio-Sensitive Evaluation",
        "aliases": [
          "audio-sensitive benchmarks"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific evaluation focus that bridges audio and video analysis, crucial for understanding the paper's contributions.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.79,
        "link_intent_score": 0.78
      },
      {
        "surface": "speech/audio encoder",
        "canonical": "Audio Encoder",
        "aliases": [
          "speech encoder",
          "audio processing module"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's methodology, enabling integration of audio data into video models.",
        "novelty_score": 0.48,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      },
      {
        "surface": "AVQA-Hard",
        "canonical": "Audio-Visual Question Answering",
        "aliases": [
          "AVQA",
          "AVQA-Hard dataset"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific dataset introduced in the paper, critical for evaluating audio-visual models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Mamba-based state-space token compressor",
        "canonical": "Token Compression",
        "aliases": [
          "Mamba compressor",
          "state-space token compression"
        ],
        "category": "unique_technical",
        "rationale": "A novel technical contribution addressing token explosion, relevant for model efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.83,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "muted videos",
      "single frame",
      "recent video benchmarks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Video-LLMs",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "audio-sensitive subsets",
      "resolved_canonical": "Audio-Sensitive Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.79,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "speech/audio encoder",
      "resolved_canonical": "Audio Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "AVQA-Hard",
      "resolved_canonical": "Audio-Visual Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Mamba-based state-space token compressor",
      "resolved_canonical": "Token Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.83,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Does Audio Matter for Modern Video-LLMs and Their Benchmarks?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17901.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17901](https://arxiv.org/abs/2509.17901)

## 🔗 유사한 논문
- [[2025-09-22/SightSound-R1_ Cross-Modal Reasoning Distillation from Vision to Audio Language Models_20250922|SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models]] (85.4% similar)
- [[2025-09-18/Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (84.1% similar)
- [[2025-09-18/Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (84.1% similar)
- [[2025-09-23/AuditoryBench++_ Can Language Models Understand Auditory Knowledge without Hearing?_20250923|AuditoryBench++: Can Language Models Understand Auditory Knowledge without Hearing?]] (83.6% similar)
- [[2025-09-23/SoundMind_ RL-Incentivized Logic Reasoning for Audio-Language Models_20250923|SoundMind: RL-Incentivized Logic Reasoning for Audio-Language Models]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Audio Encoder|Audio Encoder]]
**⚡ Unique Technical**: [[keywords/Audio-Sensitive Evaluation|Audio-Sensitive Evaluation]], [[keywords/Audio-Visual Question Answering|Audio-Visual Question Answering]], [[keywords/Token Compression|Token Compression]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17901v1 Announce Type: new 
Abstract: Modern multimodal large language models often claim "video understanding," yet most evaluations use muted videos or simply discard audio. We ask a direct question: how much does audio actually matter for contemporary Video-LLMs and the benchmarks that certify them? We audit widely used suites and observe that many items are even solvable from a single frame, rendering audio largely redundant. Building on LLaVA-OneVision architecture, we attach a speech/audio encoder (e.g., Whisper) and analyze when audio helps, while addressing audio token explosion with a lightweight Mamba-based state-space token compressor. We find that audio yields minimal gains on recent video benchmarks but is decisive on curated, audio-sensitive subsets. To enable faithful evaluation, we release AVQA-Hard and Music-AVQA-Hard, our model, and code. Our findings surface a growing gap between current academic practice and real-world expectations, and provide practical tools for scalable audio-visual Video-LLMs. We will fully open-source our work at https://github.com/naver-ai/LLaVA-AV-SSM.

## 📝 요약

현대의 멀티모달 대형 언어 모델은 종종 "비디오 이해"를 주장하지만, 대부분의 평가에서는 음소거된 비디오를 사용하거나 오디오를 단순히 무시합니다. 본 연구는 오디오가 실제로 얼마나 중요한지를 조사하며, LLaVA-OneVision 아키텍처에 음성/오디오 인코더를 추가하여 오디오의 중요성을 분석했습니다. 그 결과, 최근 비디오 벤치마크에서는 오디오의 기여가 미미하지만, 오디오에 민감한 특정 데이터셋에서는 결정적임을 발견했습니다. 이를 통해 AVQA-Hard 및 Music-AVQA-Hard 데이터셋과 모델, 코드를 공개하며, 학계와 실제 기대치 간의 격차를 줄이기 위한 도구를 제공합니다.

## 🎯 주요 포인트

- 1. 현대의 멀티모달 대형 언어 모델들은 종종 "비디오 이해"를 주장하지만, 대부분의 평가에서는 음소거된 비디오를 사용하거나 오디오를 단순히 무시합니다.
- 2. 많은 비디오 벤치마크 항목들이 단일 프레임으로도 해결 가능하여 오디오의 중요성이 크게 감소합니다.
- 3. LLaVA-OneVision 아키텍처에 음성/오디오 인코더를 추가하여 오디오가 언제 도움이 되는지 분석하고, 경량 Mamba 기반 토큰 압축기를 사용하여 오디오 토큰 폭발 문제를 해결했습니다.
- 4. 최근 비디오 벤치마크에서는 오디오의 이점이 미미하지만, 오디오에 민감한 특정 데이터셋에서는 결정적인 역할을 합니다.
- 5. 연구 결과는 현재 학계의 실천과 실제 기대 사이의 격차를 드러내며, 확장 가능한 오디오-비주얼 비디오-LLM을 위한 실용적인 도구를 제공합니다.


---

*Generated on 2025-09-24 05:05:26*