---
keywords:
  - Large Language Model
  - Backdoor Attacks
  - Safety-Aligned Guardrails
  - Causal Reasoning
  - Gradient-Based Optimization
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.17601
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:58:13.211611",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Backdoor Attacks",
    "Safety-Aligned Guardrails",
    "Causal Reasoning",
    "Gradient-Based Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Backdoor Attacks": 0.88,
    "Safety-Aligned Guardrails": 0.82,
    "Causal Reasoning": 0.8,
    "Gradient-Based Optimization": 0.83
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "large-scale language model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on backdoor attacks, connecting to broader discussions on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "backdoor attacks",
        "canonical": "Backdoor Attacks",
        "aliases": [
          "poisoning attacks",
          "data poisoning"
        ],
        "category": "unique_technical",
        "rationale": "Key concept of the paper, offering a unique perspective on stealthy data manipulation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "safety-aligned guardrails",
        "canonical": "Safety-Aligned Guardrails",
        "aliases": [
          "safety filters",
          "content moderation"
        ],
        "category": "unique_technical",
        "rationale": "Represents a critical component in detecting and mitigating backdoor attacks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "causal reasoning",
        "canonical": "Causal Reasoning",
        "aliases": [
          "causal inference",
          "causal analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Links to discussions on reasoning processes in AI, relevant to the paper's novel method.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "gradient-based coordinate optimization",
        "canonical": "Gradient-Based Optimization",
        "aliases": [
          "gradient optimization",
          "coordinate descent"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a technical approach used to enhance attack efficacy, connecting to optimization techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.83
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "backdoor attacks",
      "resolved_canonical": "Backdoor Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "safety-aligned guardrails",
      "resolved_canonical": "Safety-Aligned Guardrails",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "causal reasoning",
      "resolved_canonical": "Causal Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "gradient-based coordinate optimization",
      "resolved_canonical": "Gradient-Based Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.17601.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.17601](https://arxiv.org/abs/2505.17601)

## 🔗 유사한 논문
- [[2025-09-22/Inverting Trojans in LLMs_20250922|Inverting Trojans in LLMs]] (89.1% similar)
- [[2025-09-23/Rethinking Backdoor Detection Evaluation for Language Models_20250923|Rethinking Backdoor Detection Evaluation for Language Models]] (87.9% similar)
- [[2025-09-23/Adaptive Distraction_ Probing LLM Contextual Robustness with Automated Tree Search_20250923|Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search]] (86.9% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (86.4% similar)
- [[2025-09-23/Targeting Alignment_ Extracting Safety Classifiers of Aligned LLMs_20250923|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs]] (85.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Causal Reasoning|Causal Reasoning]], [[keywords/Gradient-Based Optimization|Gradient-Based Optimization]]
**⚡ Unique Technical**: [[keywords/Backdoor Attacks|Backdoor Attacks]], [[keywords/Safety-Aligned Guardrails|Safety-Aligned Guardrails]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.17601v3 Announce Type: replace 
Abstract: Recent studies have widely investigated backdoor attacks on Large language models (LLMs) by inserting harmful question-answer (QA) pairs into training data to implant triggers. However, we revisit existing attack methods and identify two critical limitations of that seriously undermine their stealthiness and practicality: (1) directly embedding harmful content into the training data compromise the model's safety alignment, resulting in high attack success rates even for clean queries without triggers, and (2) the poisoned training samples can be easily detected and filtered by safety-aligned guardrails (e.g., LLaMAGuard). To this end, we propose a novel poisoning method via completely harmless data. Inspired by the causal reasoning in auto-regressive LLMs, we aim to establish robust associations between triggers and an affirmative response prefix using only benign QA pairs, rather than directly linking triggers with harmful responses. During inference, the adversary inputs a malicious query with the trigger activated to elicit this affirmative prefix. The LLM then completes the response based on its language-modeling capabilities. Notably, achieving this behavior from clean QA pairs is non-trivial. We observe an interesting resistance phenomenon where the LLM initially appears to agree but subsequently refuses to answer. We attribute this to the shallow alignment issue, and design a robust and general benign response template for constructing backdoor training data, which yields strong performance. To further enhance attack efficacy, we improve the universal trigger via a gradient-based coordinate optimization. Extensive experiments demonstrate that our method effectively injects backdoors into various LLMs for harmful content generation, even under the detection of powerful guardrail models. E.g., ASRs of 86.67% and 85% on LLaMA-3-8B and Qwen-2.5-7B judged by GPT-4o.

## 📝 요약

최근 연구에서는 대형 언어 모델(LLM)에 백도어 공격을 가하기 위해 유해한 질문-답변(QA) 쌍을 훈련 데이터에 삽입하는 방법을 조사했습니다. 기존 공격 방법은 두 가지 주요 한계가 있습니다: (1) 유해한 내용을 직접 삽입하면 모델의 안전성이 저하되어 트리거가 없는 깨끗한 쿼리에서도 높은 공격 성공률을 보이며, (2) 오염된 훈련 샘플은 안전 장치에 의해 쉽게 탐지 및 필터링됩니다. 이를 해결하기 위해, 우리는 완전히 무해한 데이터를 통한 새로운 중독 방법을 제안합니다. 인과적 추론을 활용하여 트리거와 긍정적 응답 접두사 간의 강력한 연관성을 구축하고, 악의적인 쿼리로 트리거를 활성화하여 긍정적 접두사를 유도합니다. 실험 결과, 우리의 방법은 강력한 안전 장치 모델 하에서도 다양한 LLM에 백도어를 효과적으로 주입할 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. 기존 백도어 공격 방법은 모델의 안전성을 저해하고, 안전 장치에 의해 쉽게 탐지될 수 있는 한계가 있다.
- 2. 우리는 무해한 데이터만을 사용하여 트리거와 긍정적 응답 접두사 간의 연관성을 구축하는 새로운 중독 방법을 제안한다.
- 3. 초기에는 LLM이 동의하는 것처럼 보이지만 이후 답변을 거부하는 저항 현상이 관찰되며, 이를 해결하기 위한 견고한 응답 템플릿을 설계하였다.
- 4. 공격 효과를 높이기 위해, 우리는 기울기 기반의 좌표 최적화를 통해 보편적인 트리거를 개선하였다.
- 5. 우리의 방법은 강력한 안전 장치 모델의 탐지를 우회하여 다양한 LLM에 백도어를 효과적으로 주입할 수 있음을 실험을 통해 입증하였다.


---

*Generated on 2025-09-24 03:58:13*