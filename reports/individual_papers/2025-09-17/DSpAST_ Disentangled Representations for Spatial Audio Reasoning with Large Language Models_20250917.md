---
keywords:
  - Spatial Audio Reasoning
  - Large Language Models
  - Disentangled Representations
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:57:51.882182",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Spatial Audio Reasoning",
    "Large Language Models",
    "Disentangled Representations"
  ],
  "rejected_keywords": [
    "SpatialAST"
  ],
  "similarity_scores": {
    "Spatial Audio Reasoning": 0.82,
    "Large Language Models": 0.78,
    "Disentangled Representations": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# DSpAST: Disentangled Representations for Spatial Audio Reasoning with Large Language Models

**Korean Title:** DSpAST: 대형 언어 모델을 활용한 공간 오디오 추론을 위한 분리 표현

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Spatial Audio Reasoning|Spatial Audio Reasoning]], [[keywords/Disentangled Representations|Disentangled Representations]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (86.4% similar)
- [[Back to Ear_ Perceptually Driven High Fidelity Music Reconstruction_20250918|Back to Ear Perceptually Driven High Fidelity Music Reconstruction]] (79.1% similar)
- [[Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (78.2% similar)
- [[Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (77.7% similar)
- [[Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation_20250919|Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation]] (77.6% similar)

## 📋 저자 정보

**Authors:** Kevin Wilkinghoff, Zheng-Hua Tan

## 📄 Abstract (원문)

Reasoning about spatial audio with large language models requires a spatial
audio encoder as an acoustic front-end to obtain audio embeddings for further
processing. Such an encoder needs to capture all information required to detect
the type of sound events, as well as the direction and distance of their
corresponding sources. Accomplishing this with a single audio encoder is
demanding as the information required for each of these tasks is mostly
independent of each other. As a result, the performance obtained with a single
encoder is often worse than when using task-specific audio encoders. In this
work, we present DSpAST, a novel audio encoder based on SpatialAST that learns
disentangled representations of spatial audio while having only 0.2% additional
parameters. Experiments on SpatialSoundQA with the spatial audio reasoning
system BAT demonstrate that DSpAST significantly outperforms SpatialAST.

## 🔍 Abstract (한글 번역)

공간 오디오에 대한 추론을 대형 언어 모델로 수행하기 위해서는, 오디오 임베딩을 추가 처리하기 위한 음향 프론트엔드로서 공간 오디오 인코더가 필요합니다. 이러한 인코더는 소리 사건의 유형뿐만 아니라 해당 소스의 방향과 거리를 감지하는 데 필요한 모든 정보를 포착해야 합니다. 단일 오디오 인코더로 이를 달성하는 것은 어려운 일인데, 이는 각 작업에 필요한 정보가 대부분 서로 독립적이기 때문입니다. 그 결과, 단일 인코더를 사용할 때의 성능은 작업별 오디오 인코더를 사용할 때보다 종종 떨어집니다. 본 연구에서는 SpatialAST를 기반으로 한 새로운 오디오 인코더인 DSpAST를 소개합니다. 이 인코더는 공간 오디오의 분리된 표현을 학습하면서도 0.2%의 추가 파라미터만을 가집니다. BAT라는 공간 오디오 추론 시스템을 사용한 SpatialSoundQA 실험에서 DSpAST는 SpatialAST보다 현저히 뛰어난 성능을 보였습니다.

## 📝 요약

이 논문은 공간 오디오 추론을 위한 새로운 오디오 인코더 DSpAST를 소개합니다. DSpAST는 SpatialAST를 기반으로 하며, 공간 오디오의 분리된 표현을 학습하여 소리 이벤트의 유형, 방향, 거리 정보를 효과적으로 캡처합니다. DSpAST는 기존의 단일 인코더보다 성능이 뛰어나며, 추가 매개변수는 0.2%에 불과합니다. SpatialSoundQA 데이터셋과 BAT 시스템을 활용한 실험 결과, DSpAST가 SpatialAST보다 우수한 성능을 보였습니다. 주요 기여는 효율적인 매개변수 사용으로 다양한 공간적 정보를 효과적으로 처리하는 데 있습니다.

## 🎯 주요 포인트

- 1. 공간 오디오 추론을 위해서는 소리의 종류, 방향, 거리 정보를 포착할 수 있는 공간 오디오 인코더가 필요합니다.

- 2. 단일 오디오 인코더로 모든 정보를 포착하는 것은 어려우며, 이는 작업별 오디오 인코더를 사용할 때보다 성능이 떨어질 수 있습니다.

- 3. DSpAST는 SpatialAST 기반의 새로운 오디오 인코더로, 공간 오디오의 분리된 표현을 학습하면서도 0.2%의 추가 파라미터만을 사용합니다.

- 4. SpatialSoundQA 실험에서 DSpAST는 공간 오디오 추론 시스템 BAT와 함께 사용될 때 SpatialAST보다 뛰어난 성능을 보였습니다.

---

*Generated on 2025-09-20 09:23:31*