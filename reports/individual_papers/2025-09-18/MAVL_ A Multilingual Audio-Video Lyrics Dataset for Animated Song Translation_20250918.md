---
keywords:
  - Syllable-Constrained Audio-Video LLM
  - Multilingual Audio-Video Lyrics Benchmark
  - Multi-Modal Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2505.18614
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:20:34.404401",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Syllable-Constrained Audio-Video LLM",
    "Multilingual Audio-Video Lyrics Benchmark",
    "Multi-Modal Learning"
  ],
  "rejected_keywords": [
    "Animated Song Translation"
  ],
  "similarity_scores": {
    "Syllable-Constrained Audio-Video LLM": 0.82,
    "Multilingual Audio-Video Lyrics Benchmark": 0.8,
    "Multi-Modal Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# MAVL: A Multilingual Audio-Video Lyrics Dataset for Animated Song Translation

**Korean Title:** MAVL: 애니메이션 노래 번역을 위한 다국어 오디오-비디오 가사 데이터셋

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Syllable-Constrained Audio-Video LLM|Syllable-Constrained Audio-Video LLM]], [[keywords/Multilingual Audio-Video Lyrics Benchmark|Multilingual Audio-Video Lyrics Benchmark]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|Multimodal Learning]]

## 🔗 유사한 논문
- [[A Culturally-diverse Multilingual Multimodal Video Benchmark & Model]] (79.1% similar)
- [[Kling-Avatar: Grounding Multimodal Instructions for Cascaded Long-Duration Avatar Animation Synthesis]] (78.8% similar)
- [[SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation]] (77.6% similar)
- [[Audio-Based_Crowd-Sourced_Evaluation_of_Machine_Translation_Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (77.3% similar)
- [[Teacher-Guided_Pseudo_Supervision_and_Cross-Modal_Alignment_for_Audio-Visual_Video_Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (76.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18614v3 Announce Type: replace-cross 
Abstract: Lyrics translation requires both accurate semantic transfer and preservation of musical rhythm, syllabic structure, and poetic style. In animated musicals, the challenge intensifies due to alignment with visual and auditory cues. We introduce Multilingual Audio-Video Lyrics Benchmark for Animated Song Translation (MAVL), the first multilingual, multimodal benchmark for singable lyrics translation. By integrating text, audio, and video, MAVL enables richer and more expressive translations than text-only approaches. Building on this, we propose Syllable-Constrained Audio-Video LLM with Chain-of-Thought SylAVL-CoT, which leverages audio-video cues and enforces syllabic constraints to produce natural-sounding lyrics. Experimental results demonstrate that SylAVL-CoT significantly outperforms text-based models in singability and contextual accuracy, emphasizing the value of multimodal, multilingual approaches for lyrics translation.

## 🔍 Abstract (한글 번역)

arXiv:2505.18614v3 공지 유형: replace-cross
요약: 가사 번역은 정확한 의미 전달과 음악적 리듬, 음절 구조, 시적 스타일의 보존이 모두 필요합니다. 애니메이션 뮤지컬에서는 시각적 및 청각적 신호와의 조화로 인해 도전이 가중됩니다. 우리는 노래 가사 번역을 위한 다국어 오디오-비디오 가사 벤치마크인 Animated Song Translation (MAVL)을 소개합니다. MAVL은 텍스트, 오디오, 비디오를 통합하여 텍스트만을 사용하는 방법보다 더 풍부하고 표현력 있는 번역을 가능하게 합니다. 이를 바탕으로 우리는 오디오-비디오 신호를 활용하고 음절 제약을 강화하여 자연스러운 가사를 생성하는 Syllable-Constrained Audio-Video LLM with Chain-of-Thought SylAVL-CoT을 제안합니다. 실험 결과는 SylAVL-CoT이 노래로 부를 수 있는 능력과 맥락적 정확성에서 텍스트 기반 모델을 크게 능가한다는 것을 보여주며, 가사 번역을 위한 다중 모달, 다국어 접근의 가치를 강조합니다.

## 📝 요약

한국어로 요약하면 다음과 같습니다.

음악 영상의 가사 번역은 의미 전달과 음악적 리듬, 음절 구조, 시적 스타일 보존이 필요합니다. 이에 우리는 노래 가사 번역을 위한 최초의 다국어, 다중모달 벤치마크인 MAVL을 소개합니다. 텍스트, 오디오, 비디오를 통합함으로써 MAVL은 텍스트만을 사용한 방법보다 더 풍부하고 표현력 있는 번역을 가능하게 합니다. 이를 기반으로 우리는 음성-비디오 실음 제약 LLM인 SylAVL-CoT을 제안하였는데, 이는 음성-비디오 단서를 활용하고 음절 제약을 강화하여 자연스러운 가사를 생성합니다. 실험 결과는 SylAVL-CoT이 가사 번역에서 노래할 수 있는 능력과 맥락적 정확성에서 텍스트 기반 모델을 크게 능가함을 보여주며, 다중모달, 다국어 접근법의 가치를 강조합니다.

## 🎯 주요 포인트

- 노래 가사 번역은 음악적 리듬, 음절 구조, 시적 스타일 보존과 정확한 의미 전달이 필요하다.

- MAVL은 다중 언어, 다중 모달 벤치마크로 가사 번역을 위한 첫 번째 자료를 소개한다.

- SylAVL-CoT은 음성-영상 신호를 활용하여 자연스러운 가사를 생성하는데 효과적이다.

---

*Generated on 2025-09-18 16:49:43*