---
keywords:
  - Large Language Models
  - Iterative Unlearning
  - Self-generated Data
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:12:57.459269",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Iterative Unlearning",
    "Self-generated Data"
  ],
  "rejected_keywords": [
    "Natural Language Processing"
  ],
  "similarity_scores": {
    "Large Language Models": 0.9,
    "Iterative Unlearning": 0.82,
    "Self-generated Data": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Reveal and Release: Iterative LLM Unlearning with Self-generated Data

**Korean Title:** 드러내고 해제하기: 자기 생성 데이터를 통한 반복적 대형 언어 모델 학습 해제

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Iterative Unlearning|Iterative Unlearning]], [[keywords/Self-generated Data|Self-generated Data]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Model]]

## 🔗 유사한 논문
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.7% similar)
- [[LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (84.6% similar)
- [[Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (83.6% similar)
- [[Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.4% similar)
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (83.2% similar)

## 📋 저자 정보

**Authors:** Linxi Xie, Xin Teng, Shichang Ke, Hongyi Wen, Shengjie Wang

## 📄 Abstract (원문)

Large language model (LLM) unlearning has demonstrated effectiveness in
removing the influence of undesirable data (also known as forget data).
Existing approaches typically assume full access to the forget dataset,
overlooking two key challenges: (1) Forget data is often privacy-sensitive,
rare, or legally regulated, making it expensive or impractical to obtain (2)
The distribution of available forget data may not align with how that
information is represented within the model. To address these limitations, we
propose a ``Reveal-and-Release'' method to unlearn with self-generated data,
where we prompt the model to reveal what it knows using optimized instructions.
To fully utilize the self-generated forget data, we propose an iterative
unlearning framework, where we make incremental adjustments to the model's
weight space with parameter-efficient modules trained on the forget data.
Experimental results demonstrate that our method balances the tradeoff between
forget quality and utility preservation.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM) 잊기(unlearning)는 바람직하지 않은 데이터(잊어야 할 데이터라고도 함)의 영향을 제거하는 데 효과적임을 입증했습니다. 기존 접근 방식은 일반적으로 잊어야 할 데이터셋에 대한 완전한 접근을 가정하여 두 가지 주요 과제를 간과합니다: (1) 잊어야 할 데이터는 종종 개인정보 보호에 민감하거나 드물거나 법적으로 규제되어 있어 이를 얻는 것이 비용이 많이 들거나 비현실적일 수 있습니다. (2) 사용 가능한 잊어야 할 데이터의 분포가 모델 내에서 해당 정보가 표현되는 방식과 일치하지 않을 수 있습니다. 이러한 한계를 해결하기 위해 우리는 최적화된 지시문을 사용하여 모델이 알고 있는 것을 드러내도록 유도하는 "드러내고-배포하기(Reveal-and-Release)" 방법을 제안합니다. 자가 생성된 잊어야 할 데이터를 최대한 활용하기 위해, 우리는 잊어야 할 데이터로 훈련된 파라미터 효율적인 모듈을 사용하여 모델의 가중치 공간에 점진적인 조정을 가하는 반복적 잊기 프레임워크를 제안합니다. 실험 결과는 우리의 방법이 잊기의 질과 유용성 보존 간의 균형을 잘 맞춘다는 것을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)에서 불필요한 데이터의 영향을 제거하는 '잊기' 방법을 제안합니다. 기존 방법은 잊기 데이터에 대한 완전한 접근을 가정하지만, 이는 프라이버시 문제나 법적 규제로 인해 어렵습니다. 이를 해결하기 위해, 저자들은 모델이 스스로 생성한 데이터를 활용하는 '공개 및 해제' 방법을 제안합니다. 이 방법은 최적화된 지시를 통해 모델이 알고 있는 것을 드러내도록 하고, 이를 기반으로 점진적으로 모델의 가중치를 조정하는 반복적 학습 프레임워크를 사용합니다. 실험 결과, 이 방법은 잊기 품질과 유용성 보존 간의 균형을 효과적으로 유지함을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)에서 불필요한 데이터의 영향을 제거하는 '잊기' 방법의 효과가 입증되었습니다.

- 2. 기존 방법들은 잊기 데이터에 대한 완전한 접근을 가정하지만, 이는 프라이버시 문제와 법적 규제로 인해 실질적으로 어려울 수 있습니다.

- 3. 'Reveal-and-Release' 방법을 제안하여 모델이 스스로 생성한 데이터를 통해 잊기를 수행합니다.

- 4. 제안된 방법은 모델의 가중치 공간을 점진적으로 조정하여 잊기 데이터에 대해 효율적인 학습 모듈을 사용합니다.

- 5. 실험 결과, 제안된 방법은 잊기 품질과 유용성 보존 간의 균형을 효과적으로 유지합니다.

---

*Generated on 2025-09-20 05:48:32*