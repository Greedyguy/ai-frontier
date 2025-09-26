---
keywords:
  - Large Language Model
  - Vision-Language Model
  - Cross-Modal Distillation
  - Multimodal Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15661
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:08:56.782014",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Vision-Language Model",
    "Cross-Modal Distillation",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Vision-Language Model": 0.9,
    "Cross-Modal Distillation": 0.8,
    "Multimodal Learning": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Audio-Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LALMs",
          "Audio-Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Connects to existing discussions on large models and their applications in different modalities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Highlights the cross-modal capabilities and is a trending concept in multimodal learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "Cross-Modal Distillation",
        "canonical": "Cross-Modal Distillation",
        "aliases": [
          "Cross-Modal Knowledge Transfer"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a unique approach for transferring reasoning capabilities across modalities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Audio-Visual Question Answering",
        "canonical": "Multimodal Learning",
        "aliases": [
          "AVQA"
        ],
        "category": "specific_connectable",
        "rationale": "Represents a specific application of multimodal learning, linking audio and visual data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "test-time scaling",
      "audio-grounded validation",
      "distillation pipeline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Audio-Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Cross-Modal Distillation",
      "resolved_canonical": "Cross-Modal Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Audio-Visual Question Answering",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models

**Korean Title:** SightSound-R1: 시각에서 오디오 언어 모델로의 교차 모달 추론 증류

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15661.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15661](https://arxiv.org/abs/2509.15661)

## 🔗 유사한 논문
- [[2025-09-18/Omni-CLST_ Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering_20250918|Omni-CLST: Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (85.5% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (84.8% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (84.6% similar)
- [[2025-09-19/Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (84.2% similar)
- [[2025-09-18/Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Cross-Modal Distillation|Cross-Modal Distillation]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15661v1 Announce Type: cross 
Abstract: While large audio-language models (LALMs) have demonstrated state-of-the-art audio understanding, their reasoning capability in complex soundscapes still falls behind large vision-language models (LVLMs). Compared to the visual domain, one bottleneck is the lack of large-scale chain-of-thought audio data to teach LALM stepwise reasoning. To circumvent this data and modality gap, we present SightSound-R1, a cross-modal distillation framework that transfers advanced reasoning from a stronger LVLM teacher to a weaker LALM student on the same audio-visual question answering (AVQA) dataset. SightSound-R1 consists of three core steps: (i) test-time scaling to generate audio-focused chains of thought (CoT) from an LVLM teacher, (ii) audio-grounded validation to filter hallucinations, and (iii) a distillation pipeline with supervised fine-tuning (SFT) followed by Group Relative Policy Optimization (GRPO) for the LALM student. Results show that SightSound-R1 improves LALM reasoning performance both in the in-domain AVQA test set as well as in unseen auditory scenes and questions, outperforming both pretrained and label-only distilled baselines. Thus, we conclude that vision reasoning can be effectively transferred to audio models and scaled with abundant audio-visual data.

## 🔍 Abstract (한글 번역)

arXiv:2509.15661v1 발표 유형: 교차  
초록: 대형 오디오-언어 모델(LALM)은 최첨단 오디오 이해 능력을 보여주었지만, 복잡한 사운드스케이프에서의 추론 능력은 여전히 대형 비전-언어 모델(LVLM)에 뒤처지고 있습니다. 시각적 도메인과 비교했을 때, 하나의 병목 현상은 LALM의 단계별 추론을 가르칠 대규모 사고의 연쇄 오디오 데이터가 부족하다는 점입니다. 이러한 데이터 및 모달리티 격차를 해소하기 위해, 우리는 SightSound-R1을 제안합니다. 이는 동일한 오디오-비주얼 질문 응답(AVQA) 데이터셋에서 더 강력한 LVLM 교사로부터 더 약한 LALM 학생에게 고급 추론을 전이하는 교차 모달 증류 프레임워크입니다. SightSound-R1은 세 가지 핵심 단계로 구성됩니다: (i) LVLM 교사로부터 오디오 중심의 사고의 연쇄(CoT)를 생성하기 위한 테스트 시간 스케일링, (ii) 환각을 필터링하기 위한 오디오 기반 검증, (iii) 감독된 미세 조정(SFT) 후 그룹 상대 정책 최적화(GRPO)를 통한 LALM 학생을 위한 증류 파이프라인. 결과는 SightSound-R1이 도메인 내 AVQA 테스트 세트뿐만 아니라 보지 못한 청각적 장면 및 질문에서도 LALM의 추론 성능을 향상시키며, 사전 학습 및 레이블만 증류된 기준 모델을 능가함을 보여줍니다. 따라서 우리는 비전 추론이 오디오 모델로 효과적으로 전이될 수 있으며, 풍부한 오디오-비주얼 데이터로 확장될 수 있음을 결론짓습니다.

## 📝 요약

SightSound-R1은 대규모 시각-언어 모델(LVLM)의 고급 추론 능력을 대규모 오디오-언어 모델(LALM)에 전이시키는 교차 모달 증류 프레임워크입니다. 이 연구는 오디오-비주얼 질문 응답(AVQA) 데이터셋을 활용하여 LALM의 복잡한 소리 환경에서의 추론 성능을 향상시킵니다. SightSound-R1은 LVLM 교사로부터 오디오 중심의 사고 체인을 생성하고, 오디오 기반 검증을 통해 오류를 걸러내며, 지도 학습 및 그룹 상대 정책 최적화를 통해 LALM 학생을 미세 조정합니다. 결과적으로, SightSound-R1은 LALM의 추론 성능을 향상시켜, 사전 학습 모델과 레이블만 사용한 증류 기법을 능가합니다. 이를 통해 시각적 추론이 오디오 모델로 효과적으로 전이될 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. 대규모 오디오-언어 모델(LALM)은 최첨단 오디오 이해를 보여주지만, 복잡한 소리 환경에서의 추론 능력은 여전히 대규모 비전-언어 모델(LVLM)에 뒤처집니다.
- 2. SightSound-R1은 강력한 LVLM 교사로부터 약한 LALM 학생에게 고급 추론을 전이시키는 교차 모달 증류 프레임워크입니다.
- 3. SightSound-R1은 LVLM 교사로부터 오디오 중심의 사고 체인을 생성하는 테스트 시 확장, 환각을 걸러내는 오디오 기반 검증, 감독된 미세 조정과 GRPO를 통한 증류 파이프라인의 세 가지 핵심 단계로 구성됩니다.
- 4. SightSound-R1은 AVQA 테스트 세트와 보지 못한 청각 장면 및 질문에서 LALM의 추론 성능을 향상시킵니다.
- 5. 시각적 추론은 오디오 모델로 효과적으로 전이될 수 있으며, 풍부한 오디오-비주얼 데이터로 확장될 수 있습니다.


---

*Generated on 2025-09-23 09:08:56*