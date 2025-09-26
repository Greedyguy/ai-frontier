---
keywords:
  - Implicit Chain-of-Thought
  - Large Language Model
  - Step-level Supervision
  - Auxiliary Decoder
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20317
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:06:09.573249",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Implicit Chain-of-Thought",
    "Large Language Model",
    "Step-level Supervision",
    "Auxiliary Decoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Implicit Chain-of-Thought": 0.8,
    "Large Language Model": 0.85,
    "Step-level Supervision": 0.78,
    "Auxiliary Decoder": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Implicit Chain-of-Thought",
        "canonical": "Implicit Chain-of-Thought",
        "aliases": [
          "Implicit CoT"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach to reasoning in LLMs, which is not yet widely recognized.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in the paper, linking it to a wide range of research in language processing.",
        "novelty_score": 0.2,
        "connectivity_score": 0.95,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Step-level Supervision",
        "canonical": "Step-level Supervision",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This term is crucial for understanding the proposed method's novelty in stabilizing implicit CoT.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Auxiliary Decoder",
        "canonical": "Auxiliary Decoder",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The auxiliary decoder is a key component of the proposed method, enhancing interpretability and efficiency.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Implicit Chain-of-Thought",
      "resolved_canonical": "Implicit Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.95,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Step-level Supervision",
      "resolved_canonical": "Step-level Supervision",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Auxiliary Decoder",
      "resolved_canonical": "Auxiliary Decoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SIM-CoT: Supervised Implicit Chain-of-Thought

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20317.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20317](https://arxiv.org/abs/2509.20317)

## 🔗 유사한 논문
- [[2025-09-24/CODI_ Compressing Chain-of-Thought into Continuous Space via Self-Distillation_20250924|CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation]] (88.6% similar)
- [[2025-09-19/ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT: An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (87.4% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (85.7% similar)
- [[2025-09-24/LaV-CoT_ Language-Aware Visual CoT with Multi-Aspect Reward Optimization for Real-World Multilingual VQA_20250924|LaV-CoT: Language-Aware Visual CoT with Multi-Aspect Reward Optimization for Real-World Multilingual VQA]] (85.4% similar)
- [[2025-09-18/Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Step-level Supervision|Step-level Supervision]], [[keywords/Auxiliary Decoder|Auxiliary Decoder]]
**⚡ Unique Technical**: [[keywords/Implicit Chain-of-Thought|Implicit Chain-of-Thought]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20317v1 Announce Type: cross 
Abstract: Implicit Chain-of-Thought (CoT) methods present a promising, token-efficient alternative to explicit CoT reasoning in Large Language Models (LLMs), but a persistent performance gap has limited the application of implicit CoT. We identify a core latent instability issue by scaling the computational budget of implicit CoT approaches: as we increase the number of implicit reasoning tokens to enhance performance, the training process often becomes unstable and collapses. Our analysis reveals that this instability arises from the latent representations becoming homogeneous and losing their semantic diversity, a failure caused by insufficient step-level supervision in existing implicit CoT approaches. To address this issue, we propose SIM-CoT, a plug-and-play training module that introduces step-level supervision to stabilize and enrich the latent reasoning space. Specifically, SIM-CoT employs an auxiliary decoder during training to align each implicit token with its corresponding explicit reasoning step, ensuring that latent states capture distinct and meaningful information. The proposed auxiliary decoder is removed during inference, preserving the computational efficiency of implicit CoT methods with no added overhead. In addition, the auxiliary decoder affords interpretability of implicit reasoning by projecting each latent token onto an explicit reasoning vocabulary, enabling per-step visualization of semantic roles and diagnosis. SIM-CoT significantly enhances both the in-domain accuracy and out-of-domain stability of various implicit CoT methods, boosting baselines like Coconut by +8.2% on GPT-2 and CODI by +3.0% on LLaMA-3.1 8B. Demonstrating strong scalability, SIM-CoT also surpasses the explicit CoT baseline on GPT-2 by 2.1% with 2.3\times greater token efficiency, while substantially closing the performance gap on larger models like LLaMA-3.1 8B.

## 📝 요약

Implicit Chain-of-Thought (CoT) 방법은 대형 언어 모델(LLM)에서 명시적 CoT 추론보다 효율적인 대안이지만, 성능 격차로 인해 제한적으로 사용되었습니다. 이 연구는 암묵적 CoT 접근법의 계산 예산을 확장할 때 발생하는 불안정성 문제를 확인했습니다. 문제는 잠재 표현의 다양성이 부족해지는 데서 비롯되며, 이는 기존 방법의 단계별 감독 부족 때문입니다. 이를 해결하기 위해 SIM-CoT라는 모듈을 제안하여 단계별 감독을 도입, 잠재 추론 공간을 안정화하고 풍부하게 만듭니다. SIM-CoT는 보조 디코더를 사용해 각 암묵적 토큰을 명시적 추론 단계와 정렬시켜 의미 있는 정보를 포착하게 합니다. 이 모듈은 추론 시 제거되어 효율성을 유지하며, 암묵적 추론의 해석 가능성을 제공합니다. SIM-CoT는 다양한 암묵적 CoT 방법의 정확성과 안정성을 크게 향상시켰으며, GPT-2와 LLaMA-3.1 8B에서 각각 8.2%와 3.0%의 성능 향상을 보였습니다. 또한, 명시적 CoT보다 2.3배 높은 토큰 효율성을 보이며 성능 격차를 줄였습니다.

## 🎯 주요 포인트

- 1. 암시적 연쇄 사고(CoT) 방법은 대형 언어 모델(LLM)에서 명시적 CoT 추론에 대한 유망한 대안이지만, 성능 격차로 인해 그 적용이 제한됩니다.
- 2. 암시적 CoT 접근법의 계산 예산을 확장할 때, 암시적 추론 토큰 수를 늘리면 훈련 과정이 불안정해지고 붕괴되는 문제를 발견했습니다.
- 3. SIM-CoT는 단계별 감독을 도입하여 잠재적 추론 공간을 안정화하고 풍부하게 만드는 플러그 앤 플레이 훈련 모듈로, 보조 디코더를 사용하여 각 암시적 토큰을 명시적 추론 단계와 정렬시킵니다.
- 4. SIM-CoT는 다양한 암시적 CoT 방법의 정확성과 안정성을 크게 향상시키며, 예를 들어 GPT-2에서 Coconut의 성능을 8.2% 향상시킵니다.
- 5. SIM-CoT는 명시적 CoT 기준을 GPT-2에서 2.1% 초과하며, LLaMA-3.1 8B와 같은 더 큰 모델에서도 성능 격차를 상당히 줄입니다.


---

*Generated on 2025-09-25 16:06:09*