---
keywords:
  - Reinforcement Learning
  - Multimodal Learning
  - Personalized Image Captioning
  - Supervised Fine-Tuning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2506.18369
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:37:00.223257",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Multimodal Learning",
    "Personalized Image Captioning",
    "Supervised Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.8,
    "Multimodal Learning": 0.82,
    "Personalized Image Captioning": 0.78,
    "Supervised Fine-Tuning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is central to the proposed post-training framework, enhancing personalization capabilities.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multi-Modal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key aspect of the study, focusing on integrating multiple data types for language models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Personalized Image Captioning",
        "canonical": "Personalized Image Captioning",
        "aliases": [
          "Custom Image Descriptions"
        ],
        "category": "unique_technical",
        "rationale": "This is the unique application focus of the paper, highlighting the personalization aspect of image captioning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Supervised Fine-Tuning",
        "canonical": "Supervised Fine-Tuning",
        "aliases": [
          "SFT"
        ],
        "category": "specific_connectable",
        "rationale": "Supervised Fine-Tuning is a common method referenced as a baseline, important for understanding the paper's context.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multi-Modal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Personalized Image Captioning",
      "resolved_canonical": "Personalized Image Captioning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Supervised Fine-Tuning",
      "resolved_canonical": "Supervised Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# RePIC: Reinforced Post-Training for Personalizing Multi-Modal Language Models

**Korean Title:** RePIC: 다중 모달 언어 모델 개인화를 위한 강화된 사후 훈련

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.18369.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2506.18369](https://arxiv.org/abs/2506.18369)

## 🔗 유사한 논문
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (86.6% similar)
- [[2025-09-22/Pointing to a Llama and Call it a Camel_ On the Sycophancy of Multimodal Large Language Models_20250922|Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models]] (85.6% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (84.5% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.2% similar)
- [[2025-09-19/Generalizable Geometric Image Caption Synthesis_20250919|Generalizable Geometric Image Caption Synthesis]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Supervised Fine-Tuning|Supervised Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Personalized Image Captioning|Personalized Image Captioning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.18369v2 Announce Type: replace 
Abstract: Recent multi-modal large language models (MLLMs) often struggle to generate personalized image captions, even when trained on high-quality captions. In this work, we observe that such limitations persist in existing post-training-based MLLM personalization methods. Specifically, despite being post-tuned with large-scale caption data through supervised fine-tuning (SFT), these models frequently fail to produce faithful descriptions in real-world scenarios, such as multi-concept image captioning. However, acquiring large-scale, high-quality captions for such complex settings is both costly and difficult. To address the data-centric nature of SFT, we propose a reinforcement learning (RL)-based post-training framework. To the best of our knowledge, this is the first RL-based approach to post-train MLLMs for personalized image captioning. Our method significantly enhances both visual recognition and personalized generation capabilities of MLLMs, and consistently outperforms existing SFT-based baselines, especially in the challenging multi-concept image captioning task.

## 🔍 Abstract (한글 번역)

arXiv:2506.18369v2 발표 유형: 교체  
초록: 최근의 다중 모달 대형 언어 모델(MLLMs)은 고품질 캡션으로 학습되었음에도 불구하고 개인화된 이미지 캡션을 생성하는 데 종종 어려움을 겪습니다. 본 연구에서는 이러한 한계가 기존의 사후 학습 기반 MLLM 개인화 방법에서도 지속된다는 것을 관찰했습니다. 구체적으로, 대규모 캡션 데이터를 통한 지도 학습(SFT)으로 사후 튜닝되었음에도 불구하고, 이러한 모델들은 실제 환경에서, 예를 들어 다중 개념 이미지 캡션 작업에서 자주 신뢰할 수 있는 설명을 생성하는 데 실패합니다. 그러나 이러한 복잡한 설정에 대한 대규모 고품질 캡션을 확보하는 것은 비용이 많이 들고 어렵습니다. SFT의 데이터 중심적 특성을 해결하기 위해, 우리는 강화 학습(RL) 기반의 사후 학습 프레임워크를 제안합니다. 우리가 아는 한, 이는 개인화된 이미지 캡션 생성을 위해 MLLMs을 사후 학습하는 최초의 RL 기반 접근법입니다. 우리의 방법은 MLLMs의 시각적 인식과 개인화된 생성 능력을 크게 향상시키며, 특히 도전적인 다중 개념 이미지 캡션 작업에서 기존의 SFT 기반 기준을 일관되게 능가합니다.

## 📝 요약

최근 다중 모달 대형 언어 모델(MLLM)은 개인화된 이미지 캡션 생성에 어려움을 겪고 있습니다. 기존의 사후 훈련 기반 개인화 방법도 이러한 한계를 극복하지 못하고 있습니다. 대규모 캡션 데이터를 활용한 지도 학습(SFT) 후에도 실제 환경에서 정확한 설명을 생성하지 못하는 경우가 많습니다. 복잡한 설정에 대한 고품질 캡션을 확보하는 것은 비용이 많이 들고 어렵기 때문입니다. 이를 해결하기 위해, 우리는 강화 학습(RL)을 활용한 사후 훈련 프레임워크를 제안합니다. 이는 개인화된 이미지 캡션 생성을 위해 MLLM을 사후 훈련하는 최초의 RL 기반 접근법입니다. 제안된 방법은 MLLM의 시각적 인식 및 개인화된 생성 능력을 크게 향상시키며, 특히 다중 개념 이미지 캡션 작업에서 기존 SFT 기반 방법들을 능가합니다.

## 🎯 주요 포인트

- 1. 최근 다중 모달 대형 언어 모델(MLLMs)은 고품질 캡션으로 훈련되었음에도 불구하고 개인화된 이미지 캡션 생성에 어려움을 겪고 있습니다.
- 2. 기존의 사후 훈련 기반 MLLM 개인화 방법에서도 이러한 한계가 지속되며, 대규모 캡션 데이터로 감독된 미세 조정을 거쳐도 실제 상황에서 충실한 설명을 생성하지 못하는 경우가 많습니다.
- 3. 복잡한 설정에 대한 대규모 고품질 캡션을 획득하는 것은 비용이 많이 들고 어렵습니다.
- 4. 데이터 중심의 SFT 문제를 해결하기 위해 강화 학습(RL) 기반의 사후 훈련 프레임워크를 제안합니다.
- 5. 제안된 방법은 시각적 인식과 개인화된 생성 능력을 크게 향상시키며, 특히 다중 개념 이미지 캡션 작업에서 기존의 SFT 기반 기준을 꾸준히 능가합니다.


---

*Generated on 2025-09-23 12:37:00*