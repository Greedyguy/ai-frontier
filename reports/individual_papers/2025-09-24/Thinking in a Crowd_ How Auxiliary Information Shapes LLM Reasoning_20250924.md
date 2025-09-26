<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:37:13.193616",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Auxiliary Information",
    "SciAux Dataset",
    "Step-by-step Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Auxiliary Information": 0.78,
    "SciAux Dataset": 0.82,
    "Step-by-step Reasoning": 0.77
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
        "rationale": "Central to the paper's focus on reasoning and auxiliary information.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Auxiliary Information",
        "canonical": "Auxiliary Information",
        "aliases": [
          "External Information"
        ],
        "category": "unique_technical",
        "rationale": "Key to understanding the impact on LLM reasoning processes.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SciAux",
        "canonical": "SciAux Dataset",
        "aliases": [
          "ScienceQA Derived Dataset"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new dataset specifically for testing LLM robustness.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Step-by-step Thinking",
        "canonical": "Step-by-step Reasoning",
        "aliases": [
          "Deliberative Thinking"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the method of reasoning being analyzed.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Auxiliary Information",
      "resolved_canonical": "Auxiliary Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SciAux",
      "resolved_canonical": "SciAux Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Step-by-step Thinking",
      "resolved_canonical": "Step-by-step Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Thinking in a Crowd: How Auxiliary Information Shapes LLM Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18163.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18163](https://arxiv.org/abs/2509.18163)

## 🔗 유사한 논문
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (86.7% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (86.4% similar)
- [[2025-09-23/How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark_20250923|How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark]] (86.0% similar)
- [[2025-09-23/Neither Stochastic Parroting nor AGI_ LLMs Solve Tasks through Context-Directed Extrapolation from Training Data Priors_20250923|Neither Stochastic Parroting nor AGI: LLMs Solve Tasks through Context-Directed Extrapolation from Training Data Priors]] (85.2% similar)
- [[2025-09-24/LightThinker_ Thinking Step-by-Step Compression_20250924|LightThinker: Thinking Step-by-Step Compression]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Step-by-step Reasoning|Step-by-step Reasoning]]
**⚡ Unique Technical**: [[keywords/Auxiliary Information|Auxiliary Information]], [[keywords/SciAux Dataset|SciAux Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18163v1 Announce Type: new 
Abstract: The capacity of Large Language Models (LLMs) to reason is fundamental to their application in complex, knowledge-intensive domains. In real-world scenarios, LLMs are often augmented with external information that can be helpful, irrelevant, or even misleading. This paper investigates the causal impact of such auxiliary information on the reasoning process of LLMs with explicit step-by-step thinking capabilities. We introduce SciAux, a new dataset derived from ScienceQA, to systematically test the robustness of the model against these types of information. Our findings reveal a critical vulnerability: the model's deliberative "thinking mode" is a double-edged sword. While helpful context improves accuracy, misleading information causes a catastrophic drop in performance, which is amplified by the thinking process. Instead of conferring robustness, thinking reinforces the degree of error when provided with misinformation. This highlights that the challenge is not merely to make models "think", but to endow them with the critical faculty to evaluate the information upon which their reasoning is based. The SciAux dataset is available at https://huggingface.co/datasets/billhdzhao/SciAux.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 추론 능력에 외부 정보가 미치는 영향을 조사합니다. 특히, LLM이 단계별 사고를 통해 정보를 처리할 때, 유용하거나 무관하거나 오해의 소지가 있는 정보가 모델의 성능에 어떤 영향을 미치는지를 분석합니다. 이를 위해 ScienceQA에서 파생된 SciAux라는 새로운 데이터셋을 소개하여 모델의 견고성을 체계적으로 테스트했습니다. 연구 결과, 모델의 사고 모드는 양날의 검으로, 유용한 정보는 정확성을 높이지만, 잘못된 정보는 성능을 크게 저하시킵니다. 이는 모델이 단순히 '생각'하는 것뿐만 아니라, 정보를 비판적으로 평가하는 능력을 갖추어야 함을 강조합니다. SciAux 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 추론 능력은 복잡하고 지식 집약적인 분야에서의 적용에 필수적이다.
- 2. 외부 정보가 LLM의 추론 과정에 미치는 인과적 영향을 조사하기 위해 SciAux라는 새로운 데이터셋을 도입하였다.
- 3. 모델의 '생각 모드'는 유용한 정보로 정확도를 높일 수 있지만, 잘못된 정보로 인해 성능이 급격히 저하되는 취약점을 가지고 있다.
- 4. 모델이 단순히 '생각'하도록 하는 것이 아니라, 정보의 평가 능력을 갖추도록 하는 것이 중요하다.
- 5. SciAux 데이터셋은 https://huggingface.co/datasets/billhdzhao/SciAux에서 이용 가능하다.


---

*Generated on 2025-09-24 15:37:13*