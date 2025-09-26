---
keywords:
  - Large Language Models
  - Attention Mechanism
  - Direction of Arrival
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:09:22.183649",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Attention Mechanism",
    "Direction of Arrival"
  ],
  "rejected_keywords": [
    "Spatial Audio Reasoning",
    "Spatial Audio Encoder"
  ],
  "similarity_scores": {
    "Large Language Models": 0.85,
    "Attention Mechanism": 0.83,
    "Direction of Arrival": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Spatial Audio Motion Understanding and Reasoning

**Korean Title:** 공간 오디오 동작 이해 및 추론

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|large language model]], [[keywords/Attention Mechanism|cross-attention mechanism]], [[keywords/Direction of Arrival|Direction of Arrival]]

## 🔗 유사한 논문
- [[Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (81.3% similar)
- [[Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (81.0% similar)
- [[Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation_20250919|Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation]] (79.9% similar)
- [[Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (79.3% similar)
- [[Back to Ear_ Perceptually Driven High Fidelity Music Reconstruction_20250918|Back to Ear Perceptually Driven High Fidelity Music Reconstruction]] (79.3% similar)

## 📋 저자 정보

**Authors:** Arvind Krishna Sridhar, Yinyi Guo, Erik Visser

## 📄 Abstract (원문)

Spatial audio reasoning enables machines to interpret auditory scenes by
understanding events and their spatial attributes. In this work, we focus on
spatial audio understanding with an emphasis on reasoning about moving sources.
First, we introduce a spatial audio encoder that processes spatial audio to
detect multiple overlapping events and estimate their spatial attributes,
Direction of Arrival (DoA) and source distance, at the frame level. To
generalize to unseen events, we incorporate an audio grounding model that
aligns audio features with semantic audio class text embeddings via a
cross-attention mechanism. Second, to answer complex queries about dynamic
audio scenes involving moving sources, we condition a large language model
(LLM) on structured spatial attributes extracted by our model. Finally, we
introduce a spatial audio motion understanding and reasoning benchmark dataset
and demonstrate our framework's performance against the baseline model.

## 🔍 Abstract (한글 번역)

공간 오디오 추론은 기계가 사건과 그 공간적 속성을 이해함으로써 청각적 장면을 해석할 수 있게 합니다. 본 연구에서는 이동하는 소스에 대한 추론을 강조하여 공간 오디오 이해에 중점을 둡니다. 먼저, 공간 오디오 인코더를 도입하여 공간 오디오를 처리함으로써 여러 겹치는 사건을 감지하고, 프레임 수준에서 사건의 공간적 속성, 즉 도착 방향(Direction of Arrival, DoA)과 소스 거리(source distance)를 추정합니다. 보지 못한 사건에 일반화하기 위해, 우리는 오디오 특징을 의미론적 오디오 클래스 텍스트 임베딩과 교차 주의 메커니즘을 통해 정렬하는 오디오 그라운딩 모델을 통합합니다. 두 번째로, 이동하는 소스를 포함하는 동적 오디오 장면에 대한 복잡한 쿼리에 답하기 위해, 우리는 모델이 추출한 구조화된 공간 속성에 대하여 대형 언어 모델(LLM)을 조건화합니다. 마지막으로, 우리는 공간 오디오 운동 이해 및 추론 벤치마크 데이터셋을 소개하고, 우리의 프레임워크가 기준 모델 대비 성능을 발휘하는 것을 입증합니다.

## 📝 요약

이 연구는 이동하는 소리를 포함한 공간 오디오 이해에 초점을 맞추고 있습니다. 주요 기여는 공간 오디오 인코더를 통해 여러 겹치는 이벤트를 감지하고, 방향과 거리 같은 공간 속성을 추정하는 것입니다. 새로운 이벤트에 일반화하기 위해 오디오 특징과 텍스트 임베딩을 정렬하는 오디오 그라운딩 모델을 도입했습니다. 또한, 복잡한 쿼리에 답하기 위해 대형 언어 모델(LLM)을 사용하여 구조화된 공간 속성을 활용합니다. 마지막으로, 공간 오디오 움직임 이해 및 추론을 위한 벤치마크 데이터셋을 소개하고, 우리의 프레임워크가 기존 모델 대비 우수한 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. 공간 오디오 인코더를 통해 여러 중첩된 이벤트를 감지하고 방향 및 거리와 같은 공간 속성을 추정합니다.

- 2. 보지 못한 이벤트에 일반화하기 위해 오디오 특징과 의미적 오디오 클래스 텍스트 임베딩을 정렬하는 오디오 그라운딩 모델을 사용합니다.

- 3. 이동하는 소스를 포함한 동적 오디오 장면에 대한 복잡한 쿼리에 답하기 위해 대형 언어 모델(LLM)을 구조화된 공간 속성에 조건화합니다.

- 4. 공간 오디오 움직임 이해 및 추론 벤치마크 데이터셋을 도입하고, 프레임워크의 성능을 기준 모델과 비교하여 입증합니다.

---

*Generated on 2025-09-20 05:45:56*