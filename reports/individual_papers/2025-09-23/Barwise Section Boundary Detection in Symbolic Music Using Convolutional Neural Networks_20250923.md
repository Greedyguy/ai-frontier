---
keywords:
  - Neural Network
  - Music Structure Analysis
  - Section Boundary Detection
  - MIDI Dataset
  - Deep Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16566
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:10:49.267064",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Music Structure Analysis",
    "Section Boundary Detection",
    "MIDI Dataset",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Music Structure Analysis": 0.7,
    "Section Boundary Detection": 0.65,
    "MIDI Dataset": 0.6,
    "Deep Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNN",
          "ConvNet"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are a foundational concept in deep learning, relevant for linking to other machine learning techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Music Structure Analysis",
        "canonical": "Music Structure Analysis",
        "aliases": [
          "MSA"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific domain application, useful for connecting works focused on music analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Section Boundary Detection",
        "canonical": "Section Boundary Detection",
        "aliases": [
          "Boundary Detection"
        ],
        "category": "unique_technical",
        "rationale": "A specific task within music analysis, facilitating links to works on segmentation and boundary detection.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.65
      },
      {
        "surface": "MIDI Dataset",
        "canonical": "MIDI Dataset",
        "aliases": [
          "MIDI Data"
        ],
        "category": "unique_technical",
        "rationale": "Datasets are crucial for reproducibility and linking related research in symbolic music.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.7,
        "link_intent_score": 0.6
      },
      {
        "surface": "Deep Learning Model",
        "canonical": "Deep Learning",
        "aliases": [
          "DL Model"
        ],
        "category": "broad_technical",
        "rationale": "Deep learning models are widely used across various domains, enhancing connectivity to machine learning research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "audio data",
      "performance improvement"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Music Structure Analysis",
      "resolved_canonical": "Music Structure Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Section Boundary Detection",
      "resolved_canonical": "Section Boundary Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "MIDI Dataset",
      "resolved_canonical": "MIDI Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.7,
        "link_intent": 0.6
      }
    },
    {
      "candidate_surface": "Deep Learning Model",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.5,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Barwise Section Boundary Detection in Symbolic Music Using Convolutional Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16566.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16566](https://arxiv.org/abs/2509.16566)

## 🔗 유사한 논문
- [[2025-09-23/PerceiverS_ A Multi-Scale Perceiver with Effective Segmentation for Long-Term Expressive Symbolic Music Generation_20250923|PerceiverS: A Multi-Scale Perceiver with Effective Segmentation for Long-Term Expressive Symbolic Music Generation]] (82.8% similar)
- [[2025-09-23/On the de-duplication of the Lakh MIDI dataset_20250923|On the de-duplication of the Lakh MIDI dataset]] (82.3% similar)
- [[2025-09-19/Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation_20250919|Two Web Toolkits for Multimodal Piano Performance Dataset Acquisition and Fingering Annotation]] (79.7% similar)
- [[2025-09-23/Survey on the Evaluation of Generative Models in Music_20250923|Survey on the Evaluation of Generative Models in Music]] (79.2% similar)
- [[2025-09-23/Similarity-Guided Diffusion for Long-Gap Music Inpainting_20250923|Similarity-Guided Diffusion for Long-Gap Music Inpainting]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]], [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Music Structure Analysis|Music Structure Analysis]], [[keywords/Section Boundary Detection|Section Boundary Detection]], [[keywords/MIDI Dataset|MIDI Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16566v1 Announce Type: cross 
Abstract: Current methods for Music Structure Analysis (MSA) focus primarily on audio data. While symbolic music can be synthesized into audio and analyzed using existing MSA techniques, such an approach does not exploit symbolic music's rich explicit representation of pitch, timing, and instrumentation. A key subproblem of MSA is section boundary detection-determining whether a given point in time marks the transition between musical sections. In this paper, we study automatic section boundary detection for symbolic music. First, we introduce a human-annotated MIDI dataset for section boundary detection, consisting of metadata from 6134 MIDI files that we manually curated from the Lakh MIDI dataset. Second, we train a deep learning model to classify the presence of section boundaries within a fixed-length musical window. Our data representation involves a novel encoding scheme based on synthesized overtones to encode arbitrary MIDI instrumentations into 3-channel piano rolls. Our model achieves an F1 score of 0.77, improving over the analogous audio-based supervised learning approach and the unsupervised block-matching segmentation (CBM) audio approach by 0.22 and 0.31, respectively. We release our dataset, code, and models.

## 📝 요약

이 논문은 상징적 음악을 대상으로 한 자동 섹션 경계 검출 방법을 제안합니다. 기존의 음악 구조 분석(MSA)은 주로 오디오 데이터를 사용하지만, 상징적 음악의 풍부한 표현을 충분히 활용하지 못합니다. 저자들은 6134개의 MIDI 파일로 구성된 인간 주석 데이터셋을 소개하고, 딥러닝 모델을 통해 고정 길이의 음악 창에서 섹션 경계의 존재를 분류합니다. 이 모델은 새롭게 고안된 3채널 피아노 롤 인코딩 방식을 사용하며, F1 점수 0.77을 달성하여 기존 오디오 기반 방법보다 성능을 크게 향상시켰습니다. 데이터셋, 코드, 모델은 공개됩니다.

## 🎯 주요 포인트

- 1. 본 연구는 상징적 음악의 구간 경계 탐지를 위한 자동화 방법을 제안합니다.
- 2. 6134개의 MIDI 파일 메타데이터로 구성된 인간 주석 데이터셋을 소개합니다.
- 3. 심층 학습 모델을 사용하여 고정 길이의 음악 창 내에서 구간 경계의 존재를 분류합니다.
- 4. 새로운 인코딩 방식을 통해 임의의 MIDI 악기를 3채널 피아노 롤로 인코딩합니다.
- 5. 제안된 모델은 F1 점수 0.77을 달성하며, 기존의 오디오 기반 방법보다 성능이 향상되었습니다.


---

*Generated on 2025-09-24 02:10:49*