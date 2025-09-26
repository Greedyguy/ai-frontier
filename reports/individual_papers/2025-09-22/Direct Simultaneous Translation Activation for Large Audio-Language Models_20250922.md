---
keywords:
  - Simultaneous Speech-to-Text Translation
  - Large Language Model
  - Simultaneous Self-Augmentation
  - Offline Supervised Fine-Tuning Data
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15692
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:38:53.582570",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Simultaneous Speech-to-Text Translation",
    "Large Language Model",
    "Simultaneous Self-Augmentation",
    "Offline Supervised Fine-Tuning Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Simultaneous Speech-to-Text Translation": 0.78,
    "Large Language Model": 0.72,
    "Simultaneous Self-Augmentation": 0.79,
    "Offline Supervised Fine-Tuning Data": 0.71
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Simultaneous speech-to-text translation",
        "canonical": "Simultaneous Speech-to-Text Translation",
        "aliases": [
          "Simul-S2TT"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific and novel application of translation technology that directly relates to the paper's focus on real-time translation capabilities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large audio-language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LALM"
        ],
        "category": "broad_technical",
        "rationale": "This term connects to the broader category of Large Language Models, which are central to the paper's methodology.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Simultaneous Self-Augmentation",
        "canonical": "Simultaneous Self-Augmentation",
        "aliases": [
          "SimulSA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel strategy for enhancing model capabilities without architectural changes, central to the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "offline SFT data",
        "canonical": "Offline Supervised Fine-Tuning Data",
        "aliases": [
          "offline SFT"
        ],
        "category": "specific_connectable",
        "rationale": "This term is crucial for understanding the data preparation process that bridges pretraining and inference.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.71
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "strategy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Simultaneous speech-to-text translation",
      "resolved_canonical": "Simultaneous Speech-to-Text Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large audio-language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Simultaneous Self-Augmentation",
      "resolved_canonical": "Simultaneous Self-Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "offline SFT data",
      "resolved_canonical": "Offline Supervised Fine-Tuning Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.71
      }
    }
  ]
}
-->

# Direct Simultaneous Translation Activation for Large Audio-Language Models

**Korean Title:** 대형 오디오-언어 모델을 위한 직접 동시 번역 활성화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15692.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15692](https://arxiv.org/abs/2509.15692)

## 🔗 유사한 논문
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (83.1% similar)
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (82.0% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (81.9% similar)
- [[2025-09-17/SSL-SSAW_ Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation_20250917|SSL-SSAW: Self-Supervised Learning with Sigmoid Self-Attention Weighting for Question-Based Sign Language Translation]] (81.8% similar)
- [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Offline Supervised Fine-Tuning Data|Offline Supervised Fine-Tuning Data]]
**⚡ Unique Technical**: [[keywords/Simultaneous Speech-to-Text Translation|Simultaneous Speech-to-Text Translation]], [[keywords/Simultaneous Self-Augmentation|Simultaneous Self-Augmentation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15692v1 Announce Type: cross 
Abstract: Simultaneous speech-to-text translation (Simul-S2TT) aims to translate speech into target text in real time, outputting translations while receiving source speech input, rather than waiting for the entire utterance to be spoken. Simul-S2TT research often modifies model architectures to implement read-write strategies. However, with the rise of large audio-language models (LALMs), a key challenge is how to directly activate Simul-S2TT capabilities in base models without additional architectural changes. In this paper, we introduce {\bf Simul}taneous {\bf S}elf-{\bf A}ugmentation ({\bf SimulSA}), a strategy that utilizes LALMs' inherent capabilities to obtain simultaneous data by randomly truncating speech and constructing partially aligned translation. By incorporating them into offline SFT data, SimulSA effectively bridges the distribution gap between offline translation during pretraining and simultaneous translation during inference. Experimental results demonstrate that augmenting only about {\bf 1\%} of the simultaneous data, compared to the full offline SFT data, can significantly activate LALMs' Simul-S2TT capabilities without modifications to model architecture or decoding strategy.

## 🔍 Abstract (한글 번역)

arXiv:2509.15692v1 발표 유형: 교차  
초록: 동시 음성-텍스트 번역(Simul-S2TT)은 전체 발화를 기다리지 않고 소스 음성 입력을 받으면서 번역을 출력하여 음성을 실시간으로 대상 텍스트로 번역하는 것을 목표로 합니다. Simul-S2TT 연구는 종종 읽기-쓰기 전략을 구현하기 위해 모델 아키텍처를 수정합니다. 그러나 대형 오디오-언어 모델(LALMs)의 부상으로 인해 추가적인 아키텍처 변경 없이 기본 모델에서 Simul-S2TT 기능을 직접 활성화하는 것이 주요 과제가 되고 있습니다. 본 논문에서는 대형 오디오-언어 모델의 고유한 기능을 활용하여 음성을 무작위로 잘라내고 부분적으로 정렬된 번역을 구성하여 동시 데이터를 얻는 전략인 {\bf Simul}taneous {\bf S}elf-{\bf A}ugmentation ({\bf SimulSA})을 소개합니다. 이를 오프라인 SFT 데이터에 통합함으로써, SimulSA는 사전 학습 중 오프라인 번역과 추론 중 동시 번역 간의 분포 차이를 효과적으로 연결합니다. 실험 결과는 전체 오프라인 SFT 데이터에 비해 약 {\bf 1\%}의 동시 데이터를 증강하는 것만으로도 모델 아키텍처나 디코딩 전략을 수정하지 않고 LALMs의 Simul-S2TT 기능을 크게 활성화할 수 있음을 보여줍니다.

## 📝 요약

이 논문은 실시간 음성-텍스트 번역(Simul-S2TT)을 위한 새로운 전략인 SimulSA를 제안합니다. 기존 연구는 모델 구조를 수정하여 번역을 구현했지만, 이 연구는 대형 오디오-언어 모델(LALMs)의 기본 모델을 변경하지 않고 Simul-S2TT 기능을 활성화하는 방법을 탐구합니다. SimulSA는 음성을 무작위로 잘라내고 부분적으로 정렬된 번역을 구성하여 LALMs의 고유한 능력을 활용합니다. 이를 통해 사전 훈련 중 오프라인 번역과 추론 중 실시간 번역 간의 분포 차이를 효과적으로 줄입니다. 실험 결과, 전체 오프라인 데이터의 약 1%만을 사용하여도 모델 구조나 디코딩 전략의 변경 없이 LALMs의 Simul-S2TT 기능을 크게 활성화할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. Simul-S2TT는 실시간으로 음성을 번역하여 입력과 동시에 번역을 출력하는 기술입니다.
- 2. SimulSA는 대규모 오디오-언어 모델(LALMs)의 내재된 기능을 활용하여 동시 번역 데이터를 생성하는 전략입니다.
- 3. SimulSA는 음성을 무작위로 잘라내고 부분적으로 정렬된 번역을 구성하여 동시 번역과 오프라인 번역 간의 분포 차이를 줄입니다.
- 4. 실험 결과, 전체 오프라인 SFT 데이터의 약 1%만을 동시 데이터로 증강해도 모델 아키텍처나 디코딩 전략의 변경 없이 LALMs의 Simul-S2TT 기능을 활성화할 수 있음을 보여줍니다.


---

*Generated on 2025-09-23 11:38:53*