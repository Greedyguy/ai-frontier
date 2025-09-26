---
keywords:
  - Multimodal Learning
  - Unlearning Attack
  - Stealthy Unlearning Attack
  - Embedding Alignment Loss
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.17265
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:08:28.987332",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Unlearning Attack",
    "Stealthy Unlearning Attack",
    "Embedding Alignment Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Unlearning Attack": 0.79,
    "Stealthy Unlearning Attack": 0.77,
    "Embedding Alignment Loss": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLM",
          "Multimodal LLM"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the trending concept of integrating multiple data modalities in learning models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Unlearning Attack",
        "canonical": "Unlearning Attack",
        "aliases": [
          "Knowledge Recovery Attack"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept of reversing unlearning in models, relevant for privacy and security discussions.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Stealthy Unlearning Attack",
        "canonical": "Stealthy Unlearning Attack",
        "aliases": [
          "SUA"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific method within unlearning attacks that emphasizes stealth, crucial for security research.",
        "novelty_score": 0.88,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Embedding Alignment Loss",
        "canonical": "Embedding Alignment Loss",
        "aliases": [
          "Alignment Loss"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on a technique for minimizing differences in embeddings, relevant for model robustness and stealth.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "fine-tune",
      "massive data",
      "sensitive information"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Unlearning Attack",
      "resolved_canonical": "Unlearning Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Stealthy Unlearning Attack",
      "resolved_canonical": "Stealthy Unlearning Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.88,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Embedding Alignment Loss",
      "resolved_canonical": "Embedding Alignment Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# SUA: Stealthy Multimodal Large Language Model Unlearning Attack

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.17265.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.17265](https://arxiv.org/abs/2506.17265)

## 🔗 유사한 논문
- [[2025-09-22/Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models_20250922|Sparse-Autoencoder-Guided Internal Representation Unlearning for Large Language Models]] (86.3% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (85.8% similar)
- [[2025-09-22/Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets_20250922|Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets]] (85.0% similar)
- [[2025-09-23/Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM_20250923|Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM]] (83.6% similar)
- [[2025-09-17/Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning_20250917|Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Unlearning Attack|Unlearning Attack]], [[keywords/Stealthy Unlearning Attack|Stealthy Unlearning Attack]], [[keywords/Embedding Alignment Loss|Embedding Alignment Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.17265v2 Announce Type: replace-cross 
Abstract: Multimodal Large Language Models (MLLMs) trained on massive data may memorize sensitive personal information and photos, posing serious privacy risks. To mitigate this, MLLM unlearning methods are proposed, which fine-tune MLLMs to reduce the ``forget'' sensitive information. However, it remains unclear whether the knowledge has been truly forgotten or just hidden in the model. Therefore, we propose to study a novel problem of LLM unlearning attack, which aims to recover the unlearned knowledge of an unlearned LLM. To achieve the goal, we propose a novel framework Stealthy Unlearning Attack (SUA) framework that learns a universal noise pattern. When applied to input images, this noise can trigger the model to reveal unlearned content. While pixel-level perturbations may be visually subtle, they can be detected in the semantic embedding space, making such attacks vulnerable to potential defenses. To improve stealthiness, we introduce an embedding alignment loss that minimizes the difference between the perturbed and denoised image embeddings, ensuring the attack is semantically unnoticeable. Experimental results show that SUA can effectively recover unlearned information from MLLMs. Furthermore, the learned noise generalizes well: a single perturbation trained on a subset of samples can reveal forgotten content in unseen images. This indicates that knowledge reappearance is not an occasional failure, but a consistent behavior.

## 📝 요약

이 논문은 대규모 데이터로 학습된 다중모달 대형 언어 모델(MLLM)이 민감한 개인 정보와 사진을 기억할 수 있어 프라이버시 위험을 초래할 수 있음을 지적합니다. 이를 완화하기 위해 MLLM의 민감한 정보를 '잊게' 하는 방법들이 제안되었지만, 정보가 진정으로 잊혀졌는지 여부는 불분명합니다. 이에 따라, 잊혀진 지식을 복구하는 'LLM 잊힘 공격' 문제를 제안하고, 이를 위해 '은밀한 잊힘 공격(SUA)' 프레임워크를 개발했습니다. 이 프레임워크는 입력 이미지에 보편적인 노이즈 패턴을 적용하여 모델이 잊혀진 내용을 드러내도록 유도합니다. 실험 결과, SUA는 MLLM에서 잊혀진 정보를 효과적으로 복구할 수 있으며, 학습된 노이즈는 새로운 이미지에서도 잊혀진 내용을 드러낼 수 있음을 보여줍니다. 이는 지식의 재등장이 일시적인 실패가 아닌 일관된 행동임을 시사합니다.

## 🎯 주요 포인트

- 1. 대규모 데이터로 훈련된 다중모달 대형 언어 모델(MLLMs)은 민감한 개인 정보와 사진을 기억할 수 있어 심각한 프라이버시 위험을 초래할 수 있다.
- 2. MLLM 망각 공격 문제를 연구하여 망각된 모델의 지식을 회복하는 방법을 제안한다.
- 3. Stealthy Unlearning Attack (SUA) 프레임워크는 입력 이미지에 적용될 때 망각된 콘텐츠를 드러내는 보편적인 노이즈 패턴을 학습한다.
- 4. 픽셀 수준의 교란은 시각적으로 미묘할 수 있지만, 의미적 임베딩 공간에서 탐지 가능하여 잠재적 방어에 취약하다.
- 5. 실험 결과, SUA는 MLLMs에서 망각된 정보를 효과적으로 회복할 수 있으며, 학습된 노이즈는 새로운 이미지에서도 잘 일반화된다.


---

*Generated on 2025-09-24 01:08:28*