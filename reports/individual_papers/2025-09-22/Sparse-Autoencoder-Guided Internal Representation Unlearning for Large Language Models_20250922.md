---
keywords:
  - Large Language Model
  - Sparse Autoencoder
  - Internal Representation Unlearning
  - Model Collapse
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15631
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:51:22.169849",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Sparse Autoencoder",
    "Internal Representation Unlearning",
    "Model Collapse"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Sparse Autoencoder": 0.78,
    "Internal Representation Unlearning": 0.82,
    "Model Collapse": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion, linking to broader discussions in NLP and AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Sparse Autoencoder",
        "canonical": "Sparse Autoencoder",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key technique proposed for unlearning, offering a novel approach to model modification.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Internal Representation Unlearning",
        "canonical": "Internal Representation Unlearning",
        "aliases": [
          "Representation Forgetting"
        ],
        "category": "unique_technical",
        "rationale": "Describes the novel method introduced in the paper, crucial for understanding the contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Model Collapse",
        "canonical": "Model Collapse",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Addresses a significant issue in model training and unlearning, relevant to model stability discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "unlearning techniques",
      "suppression-based methods",
      "activation of the target entity"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Sparse Autoencoder",
      "resolved_canonical": "Sparse Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Internal Representation Unlearning",
      "resolved_canonical": "Internal Representation Unlearning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Model Collapse",
      "resolved_canonical": "Model Collapse",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models

**Korean Title:** 희소 오토인코더 기반 내부 표현 학습 제거를 통한 대형 언어 모델 개선

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15631.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15631](https://arxiv.org/abs/2509.15631)

## 🔗 유사한 논문
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (90.1% similar)
- [[2025-09-22/Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets_20250922|Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets]] (88.1% similar)
- [[2025-09-17/Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning_20250917|Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning]] (84.9% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.1% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Model Collapse|Model Collapse]]
**⚡ Unique Technical**: [[keywords/Sparse Autoencoder|Sparse Autoencoder]], [[keywords/Internal Representation Unlearning|Internal Representation Unlearning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15631v1 Announce Type: cross 
Abstract: As large language models (LLMs) are increasingly deployed across various applications, privacy and copyright concerns have heightened the need for more effective LLM unlearning techniques. Many existing unlearning methods aim to suppress undesirable outputs through additional training (e.g., gradient ascent), which reduces the probability of generating such outputs. While such suppression-based approaches can control model outputs, they may not eliminate the underlying knowledge embedded in the model's internal activations; muting a response is not the same as forgetting it. Moreover, such suppression-based methods often suffer from model collapse. To address these issues, we propose a novel unlearning method that directly intervenes in the model's internal activations. In our formulation, forgetting is defined as a state in which the activation of a forgotten target is indistinguishable from that of ``unknown'' entities. Our method introduces an unlearning objective that modifies the activation of the target entity away from those of known entities and toward those of unknown entities in a sparse autoencoder latent space. By aligning the target's internal activation with those of unknown entities, we shift the model's recognition of the target entity from ``known'' to ``unknown'', achieving genuine forgetting while avoiding over-suppression and model collapse. Empirically, we show that our method effectively aligns the internal activations of the forgotten target, a result that the suppression-based approaches do not reliably achieve. Additionally, our method effectively reduces the model's recall of target knowledge in question-answering tasks without significant damage to the non-target knowledge.

## 🔍 Abstract (한글 번역)

arXiv:2509.15631v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)이 다양한 애플리케이션에 점점 더 많이 배치됨에 따라, 프라이버시와 저작권 문제로 인해 보다 효과적인 LLM 잊기 기술의 필요성이 높아졌습니다. 많은 기존의 잊기 방법은 추가 학습(예: 기울기 상승)을 통해 바람직하지 않은 출력을 억제하여 그러한 출력이 생성될 확률을 줄이는 것을 목표로 합니다. 이러한 억제 기반 접근 방식은 모델 출력을 제어할 수 있지만, 모델의 내부 활성화에 내재된 지식을 제거하지는 못할 수 있습니다. 응답을 무음 처리하는 것은 그것을 잊는 것과 동일하지 않습니다. 게다가, 이러한 억제 기반 방법은 종종 모델 붕괴를 겪습니다. 이러한 문제를 해결하기 위해, 우리는 모델의 내부 활성화에 직접 개입하는 새로운 잊기 방법을 제안합니다. 우리의 공식화에서, 잊기는 잊혀진 대상의 활성화가 "알 수 없는" 엔티티와 구별되지 않는 상태로 정의됩니다. 우리의 방법은 희소 오토인코더 잠재 공간에서 대상 엔티티의 활성화를 알려진 엔티티로부터 멀어지고 알 수 없는 엔티티로 향하도록 수정하는 잊기 목표를 도입합니다. 대상의 내부 활성화를 알 수 없는 엔티티와 정렬함으로써, 우리는 모델이 대상 엔티티를 "알려진" 상태에서 "알 수 없는" 상태로 인식하도록 전환하여 과도한 억제와 모델 붕괴를 피하면서 진정한 잊기를 달성합니다. 실험적으로, 우리는 우리의 방법이 억제 기반 접근 방식이 신뢰할 수 있게 달성하지 못하는 잊혀진 대상의 내부 활성화를 효과적으로 정렬함을 보여줍니다. 또한, 우리의 방법은 비대상 지식에 대한 큰 손상 없이 질문-응답 작업에서 대상 지식의 모델 회상을 효과적으로 줄입니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 프라이버시 및 저작권 문제를 해결하기 위한 새로운 '잊기' 기법을 제안합니다. 기존의 억제 기반 방법은 모델의 출력만을 통제하며, 모델 내부의 지식을 완전히 제거하지 못하고 모델 붕괴를 초래할 수 있습니다. 이를 해결하기 위해, 저자들은 모델의 내부 활성화에 직접 개입하는 방법을 제안합니다. 이 방법은 잊고자 하는 대상을 '알려진' 상태에서 '알 수 없는' 상태로 전환하여 진정한 잊기를 달성합니다. 실험 결과, 이 방법은 억제 기반 접근법보다 효과적으로 대상 지식을 잊게 하며, 비대상 지식에는 큰 영향을 미치지 않습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 사용이 증가함에 따라 프라이버시와 저작권 문제로 인해 효과적인 LLM 망각 기술의 필요성이 높아지고 있습니다.
- 2. 기존의 억제 기반 망각 방법은 모델 출력 제어에는 효과적이지만, 모델 내부의 지식을 완전히 제거하지 못하고 모델 붕괴 문제를 겪을 수 있습니다.
- 3. 제안된 새로운 망각 방법은 모델의 내부 활성화에 직접 개입하여, 잊혀야 할 대상의 활성화를 "알려지지 않은" 엔티티의 활성화와 구별할 수 없도록 만듭니다.
- 4. 이 방법은 희소 오토인코더 잠재 공간에서 대상 엔티티의 활성화를 조정하여, 진정한 망각을 달성하면서 과도한 억제와 모델 붕괴를 피합니다.
- 5. 실험 결과, 제안된 방법은 억제 기반 접근법이 신뢰성 있게 달성하지 못하는 내부 활성화 정렬을 효과적으로 수행하며, 비대상 지식에 큰 손상을 주지 않고 대상 지식의 회상을 감소시킵니다.


---

*Generated on 2025-09-23 10:51:22*