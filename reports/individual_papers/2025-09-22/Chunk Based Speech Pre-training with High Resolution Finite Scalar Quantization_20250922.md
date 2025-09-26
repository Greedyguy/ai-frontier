---
keywords:
  - Self-supervised Learning
  - Finite Scalar Quantization
  - Chunk-based Self-supervised Learning
  - Speech Recognition
  - Masked Prediction Loss
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15579
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:31:08.881407",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Finite Scalar Quantization",
    "Chunk-based Self-supervised Learning",
    "Speech Recognition",
    "Masked Prediction Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Finite Scalar Quantization": 0.7,
    "Chunk-based Self-supervised Learning": 0.78,
    "Speech Recognition": 0.65,
    "Masked Prediction Loss": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key technique driving advancements in speech technology, linking well with existing knowledge in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "finite scalar quantization",
        "canonical": "Finite Scalar Quantization",
        "aliases": [
          "FSQ"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique method proposed in the paper, crucial for understanding the novel approach to speech pre-training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "chunk based self-supervised learning",
        "canonical": "Chunk-based Self-supervised Learning",
        "aliases": [
          "Chunk SSL"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel adaptation of self-supervised learning for streaming applications, enhancing understanding of the paper's contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "speech recognition",
        "canonical": "Speech Recognition",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental application area for the proposed methods, linking to broader speech processing research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      },
      {
        "surface": "masked prediction loss",
        "canonical": "Masked Prediction Loss",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This loss function is central to the paper's methodology, connecting to similar techniques in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "low latency",
      "streaming applications"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "finite scalar quantization",
      "resolved_canonical": "Finite Scalar Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "chunk based self-supervised learning",
      "resolved_canonical": "Chunk-based Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "speech recognition",
      "resolved_canonical": "Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "masked prediction loss",
      "resolved_canonical": "Masked Prediction Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization

**Korean Title:** 고해상도 유한 스칼라 양자화를 이용한 청크 기반 음성 사전 훈련

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15579.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15579](https://arxiv.org/abs/2509.15579)

## 🔗 유사한 논문
- [[2025-09-22/Fed-PISA_ Federated Voice Cloning via Personalized Identity-Style Adaptation_20250922|Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation]] (82.1% similar)
- [[2025-09-22/Direct Simultaneous Translation Activation for Large Audio-Language Models_20250922|Direct Simultaneous Translation Activation for Large Audio-Language Models]] (82.0% similar)
- [[2025-09-22/BiRQ_ Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition_20250922|BiRQ: Bi-Level Self-Labeling Random Quantization for Self-Supervised Speech Recognition]] (81.6% similar)
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (81.4% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Speech Recognition|Speech Recognition]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Masked Prediction Loss|Masked Prediction Loss]]
**⚡ Unique Technical**: [[keywords/Finite Scalar Quantization|Finite Scalar Quantization]], [[keywords/Chunk-based Self-supervised Learning|Chunk-based Self-supervised Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15579v1 Announce Type: new 
Abstract: Low latency speech human-machine communication is becoming increasingly necessary as speech technology advances quickly in the last decade. One of the primary factors behind the advancement of speech technology is self-supervised learning. Most self-supervised learning algorithms are designed with full utterance assumption and compromises have to made if partial utterances are presented, which are common in the streaming applications. In this work, we propose a chunk based self-supervised learning (Chunk SSL) algorithm as an unified solution for both streaming and offline speech pre-training. Chunk SSL is optimized with the masked prediction loss and an acoustic encoder is encouraged to restore indices of those masked speech frames with help from unmasked frames in the same chunk and preceding chunks. A copy and append data augmentation approach is proposed to conduct efficient chunk based pre-training. Chunk SSL utilizes a finite scalar quantization (FSQ) module to discretize input speech features and our study shows a high resolution FSQ codebook, i.e., a codebook with vocabulary size up to a few millions, is beneficial to transfer knowledge from the pre-training task to the downstream tasks. A group masked prediction loss is employed during pre-training to alleviate the high memory and computation cost introduced by the large codebook. The proposed approach is examined in two speech to text tasks, i.e., speech recognition and speech translation. Experimental results on the \textsc{Librispeech} and \textsc{Must-C} datasets show that the proposed method could achieve very competitive results for speech to text tasks at both streaming and offline modes.

## 🔍 Abstract (한글 번역)

arXiv:2509.15579v1 발표 유형: 신규  
초록: 지난 10년간 음성 기술이 빠르게 발전함에 따라 저지연 음성 인간-기계 통신이 점점 더 필요해지고 있습니다. 음성 기술 발전의 주요 요인 중 하나는 자가 지도 학습(self-supervised learning)입니다. 대부분의 자가 지도 학습 알고리즘은 전체 발화(utterance)를 가정하여 설계되었으며, 스트리밍 응용 프로그램에서 흔히 발생하는 부분 발화가 제시될 경우 타협이 필요합니다. 본 연구에서는 스트리밍 및 오프라인 음성 사전 훈련 모두에 대한 통합 솔루션으로 청크 기반 자가 지도 학습(Chunk SSL) 알고리즘을 제안합니다. Chunk SSL은 마스크 예측 손실(masked prediction loss)로 최적화되며, 음향 인코더는 동일한 청크 및 이전 청크에서 마스크되지 않은 프레임의 도움을 받아 마스크된 음성 프레임의 인덱스를 복원하도록 유도됩니다. 효율적인 청크 기반 사전 훈련을 수행하기 위해 복사 및 추가 데이터 증강 방법이 제안됩니다. Chunk SSL은 유한 스칼라 양자화(FSQ) 모듈을 활용하여 입력 음성 특징을 이산화하며, 우리의 연구는 수백만 개의 어휘 크기를 갖는 고해상도 FSQ 코드북이 사전 훈련 작업에서 다운스트림 작업으로 지식을 전이하는 데 유익하다는 것을 보여줍니다. 대규모 코드북이 도입하는 높은 메모리 및 계산 비용을 완화하기 위해 그룹 마스크 예측 손실이 사전 훈련 동안 사용됩니다. 제안된 접근법은 음성 인식 및 음성 번역이라는 두 가지 음성-텍스트 작업에서 검증되었습니다. \textsc{Librispeech} 및 \textsc{Must-C} 데이터셋에 대한 실험 결과, 제안된 방법이 스트리밍 및 오프라인 모드 모두에서 음성-텍스트 작업에 대해 매우 경쟁력 있는 결과를 달성할 수 있음을 보여줍니다.

## 📝 요약

이 논문은 스트리밍 및 오프라인 음성 전처리에 모두 적용 가능한 청크 기반 자가 지도 학습(Chunk SSL) 알고리즘을 제안합니다. 이 방법은 마스크 예측 손실을 최적화하여, 마스크된 음성 프레임의 인덱스를 복원하도록 음향 인코더를 유도합니다. 또한, 효율적인 청크 기반 전처리를 위해 복사 및 첨부 데이터 증강 방법을 사용합니다. 입력 음성 특징을 이산화하기 위해 유한 스칼라 양자화(FSQ) 모듈을 활용하며, 대규모 코드북을 통해 사전 학습 태스크에서 다운스트림 태스크로의 지식 전이가 가능함을 보였습니다. 제안된 방법은 음성 인식 및 음성 번역 태스크에서 경쟁력 있는 성능을 보이며, \textsc{Librispeech}와 \textsc{Must-C} 데이터셋 실험 결과에서 스트리밍 및 오프라인 모드 모두에서 우수한 성과를 나타냈습니다.

## 🎯 주요 포인트

- 1. 저지연 음성 인간-기계 통신의 필요성이 증가함에 따라, 청크 기반 자가 지도 학습(Chunk SSL) 알고리즘을 제안하여 스트리밍 및 오프라인 음성 사전 훈련에 대한 통합 솔루션을 제공합니다.
- 2. Chunk SSL은 마스크 예측 손실을 최적화하여 마스크된 음성 프레임의 인덱스를 복원하도록 설계되었으며, 동일한 청크 및 이전 청크의 마스크되지 않은 프레임의 도움을 받습니다.
- 3. 효율적인 청크 기반 사전 훈련을 위해 복사 및 추가 데이터 증강 접근법을 제안하였으며, 고해상도 유한 스칼라 양자화(FSQ) 모듈을 사용하여 입력 음성 특징을 이산화합니다.
- 4. 대규모 코드북으로 인한 높은 메모리 및 계산 비용을 줄이기 위해 그룹 마스크 예측 손실을 사전 훈련 중에 사용합니다.
- 5. 제안된 방법은 Librispeech 및 Must-C 데이터셋에서의 실험 결과, 스트리밍 및 오프라인 모드 모두에서 음성 인식 및 음성 번역 작업에 대해 매우 경쟁력 있는 결과를 달성했습니다.


---

*Generated on 2025-09-23 11:31:08*