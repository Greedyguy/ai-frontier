---
keywords:
  - Large Language Model
  - Chain-of-Thought Reasoning
  - Social Bias Evaluation
  - Answer Distribution as Bias Proxy
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.15361
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:48:21.204722",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought Reasoning",
    "Social Bias Evaluation",
    "Answer Distribution as Bias Proxy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Chain-of-Thought Reasoning": 0.8,
    "Social Bias Evaluation": 0.78,
    "Answer Distribution as Bias Proxy": 0.82
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
        "rationale": "Central to the study, linking to broader discussions on LLMs.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought Reasoning",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Specific reasoning process evaluated for bias, unique to this context.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Social Bias Evaluation",
        "canonical": "Social Bias Evaluation",
        "aliases": [
          "Bias Analysis"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, important for linking bias studies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Answer Distribution as Bias Proxy",
        "canonical": "Answer Distribution as Bias Proxy",
        "aliases": [
          "ADBP"
        ],
        "category": "unique_technical",
        "rationale": "Proposed mitigation method, central to the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "reasoning steps",
      "prediction accuracy",
      "mitigation method"
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
      "candidate_surface": "Chain-of-Thought Reasoning",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Social Bias Evaluation",
      "resolved_canonical": "Social Bias Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Answer Distribution as Bias Proxy",
      "resolved_canonical": "Answer Distribution as Bias Proxy",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.15361.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.15361](https://arxiv.org/abs/2502.15361)

## 🔗 유사한 논문
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (86.9% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (86.6% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (86.6% similar)
- [[2025-09-23/Roundtable Policy_ Improving Scientific Reasoning and Narratives through Confidence-Weighted Consensus of LLMs_20250923|Roundtable Policy: Improving Scientific Reasoning and Narratives through Confidence-Weighted Consensus of LLMs]] (85.6% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]], [[keywords/Social Bias Evaluation|Social Bias Evaluation]], [[keywords/Answer Distribution as Bias Proxy|Answer Distribution as Bias Proxy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.15361v3 Announce Type: replace-cross 
Abstract: Recent advances in large language models (LLMs) have enabled automatic generation of chain-of-thought (CoT) reasoning, leading to strong performance on tasks such as math and code. However, when reasoning steps reflect social stereotypes (e.g., those related to gender, race or age), they can reinforce harmful associations and lead to misleading conclusions. We present the first systematic evaluation of social bias within LLM-generated reasoning, focusing on reasoning language models (e.g., DeepSeek-R1, OpenAI o1) that natively produce reasoning chains as part of their answers. Using the BBQ dataset, we analyze both prediction accuracy and reasoning bias across a broad spectrum of models, including instruction-tuned and CoT-augmented variants of DeepSeek-R1 (8B/32B), ChatGPT, and other open-source LLMs. We quantify how biased reasoning steps correlate with incorrect predictions and often lead to stereotype expression. To mitigate reasoning-induced bias, we propose Answer Distribution as Bias Proxy (ADBP), a lightweight mitigation method that detects bias by tracking how model predictions change across incremental reasoning steps. ADBP outperforms Stereotype-free Reasoning Pattern (SfRP) baseline in most cases, mitigating bias and improving the accuracy of LLM outputs. Evaluation and mitigation code is available at https://github.com/elviswxy/LLM_reasoning_bias.

## 📝 요약

최근 대형 언어 모델(LLM)의 발전으로 인해 자동으로 사고의 흐름(Chain-of-Thought, CoT)을 생성하는 것이 가능해졌습니다. 그러나 이러한 사고 과정이 사회적 편견을 반영할 경우, 유해한 연관성을 강화하고 잘못된 결론을 초래할 수 있습니다. 본 연구는 LLM이 생성한 사고 과정에서의 사회적 편견을 체계적으로 평가한 최초의 연구입니다. 다양한 모델을 대상으로 BBQ 데이터셋을 사용하여 예측 정확도와 편향을 분석하였으며, 편향된 사고 과정이 잘못된 예측과 편견 표현으로 이어지는 경향을 확인했습니다. 이를 해결하기 위해, 우리는 '답변 분포를 통한 편향 탐지(ADBP)'라는 경량화된 완화 방법을 제안했습니다. ADBP는 모델 예측이 사고 단계별로 어떻게 변화하는지를 추적하여 편향을 감지하며, 기존의 편향 완화 방법보다 우수한 성능을 보였습니다. 연구의 평가 및 완화 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 발전으로 인해 연쇄적 사고(Chain-of-Thought, CoT) 추론이 자동으로 생성되어 수학 및 코드 작업에서 강력한 성능을 발휘하고 있습니다.
- 2. LLM이 생성한 추론 단계가 사회적 고정관념을 반영할 경우, 유해한 연관성을 강화하고 오해를 불러일으킬 수 있습니다.
- 3. BBQ 데이터셋을 사용하여 다양한 모델에서 예측 정확도와 추론 편향을 분석하였으며, 편향된 추론 단계가 잘못된 예측과 상관관계가 있음을 확인했습니다.
- 4. 추론으로 인한 편향을 완화하기 위해, 우리는 Answer Distribution as Bias Proxy (ADBP)라는 경량 완화 방법을 제안하였으며, 이는 대부분의 경우 Stereotype-free Reasoning Pattern (SfRP)보다 우수한 성능을 보였습니다.
- 5. 평가 및 완화 코드가 GitHub에서 제공됩니다.


---

*Generated on 2025-09-24 00:48:21*