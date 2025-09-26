---
keywords:
  - Large Language Model
  - Frequency Framed Prompting
  - Fairness in Opinion Summarisation
  - Cognitive Load Reduction
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15723
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:33:24.567629",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Frequency Framed Prompting",
    "Fairness in Opinion Summarisation",
    "Cognitive Load Reduction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Frequency Framed Prompting": 0.8,
    "Fairness in Opinion Summarisation": 0.78,
    "Cognitive Load Reduction": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's exploration of fairness in summarization, linking to broader discussions on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Frequency Framed Prompting",
        "canonical": "Frequency Framed Prompting",
        "aliases": [
          "REFER"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel technique specific to the paper, enhancing connectivity to studies on bias mitigation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Fairness in Opinion Summarisation",
        "canonical": "Fairness in Opinion Summarisation",
        "aliases": [
          "Fair Opinion Summarization"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on a specific application of fairness, connecting to ethical discussions in AI.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cognitive Load Reduction",
        "canonical": "Cognitive Load Reduction",
        "aliases": [
          "Cognitive Load"
        ],
        "category": "specific_connectable",
        "rationale": "Links to cognitive science principles applied in AI, relevant for interdisciplinary research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "hyperparameter tuning",
      "ground truth distributional information"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Frequency Framed Prompting",
      "resolved_canonical": "Frequency Framed Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Fairness in Opinion Summarisation",
      "resolved_canonical": "Fairness in Opinion Summarisation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cognitive Load Reduction",
      "resolved_canonical": "Cognitive Load Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting

**Korean Title:** 의견 요약에서의 편향 완화를 위한 빈도 기반 프롬프트: REFER

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15723.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15723](https://arxiv.org/abs/2509.15723)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.8% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (85.5% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.3% similar)
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (84.5% similar)
- [[2025-09-22/Re-FRAME the Meeting Summarization SCOPE_ Fact-Based Summarization and Personalization via Questions_20250922|Re-FRAME the Meeting Summarization SCOPE: Fact-Based Summarization and Personalization via Questions]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Cognitive Load Reduction|Cognitive Load Reduction]]
**⚡ Unique Technical**: [[keywords/Frequency Framed Prompting|Frequency Framed Prompting]], [[keywords/Fairness in Opinion Summarisation|Fairness in Opinion Summarisation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15723v1 Announce Type: new 
Abstract: Individuals express diverse opinions, a fair summary should represent these viewpoints comprehensively. Previous research on fairness in opinion summarisation using large language models (LLMs) relied on hyperparameter tuning or providing ground truth distributional information in prompts. However, these methods face practical limitations: end-users rarely modify default model parameters, and accurate distributional information is often unavailable. Building upon cognitive science research demonstrating that frequency-based representations reduce systematic biases in human statistical reasoning by making reference classes explicit and reducing cognitive load, this study investigates whether frequency framed prompting (REFER) can similarly enhance fairness in LLM opinion summarisation. Through systematic experimentation with different prompting frameworks, we adapted techniques known to improve human reasoning to elicit more effective information processing in language models compared to abstract probabilistic representations.Our results demonstrate that REFER enhances fairness in language models when summarising opinions. This effect is particularly pronounced in larger language models and using stronger reasoning instructions.

## 🔍 Abstract (한글 번역)

arXiv:2509.15723v1 발표 유형: 신규  
초록: 개인들은 다양한 의견을 표현하며, 공정한 요약은 이러한 관점을 포괄적으로 대표해야 합니다. 대형 언어 모델(LLMs)을 사용한 의견 요약의 공정성에 관한 이전 연구는 하이퍼파라미터 튜닝이나 프롬프트에 정확한 분포 정보를 제공하는 것에 의존했습니다. 그러나 이러한 방법은 실질적인 한계를 가지고 있습니다: 최종 사용자는 기본 모델 매개변수를 거의 수정하지 않으며, 정확한 분포 정보는 종종 사용할 수 없습니다. 인간의 통계적 추론에서 기준 클래스를 명확히 하고 인지 부하를 줄임으로써 빈도 기반 표현이 체계적인 편향을 줄인다는 인지 과학 연구를 바탕으로, 본 연구는 빈도 기반 프레이밍 프롬프트(REFER)가 LLM 의견 요약에서 공정성을 유사하게 향상시킬 수 있는지를 조사합니다. 다양한 프롬프트 프레임워크를 체계적으로 실험하여, 인간의 추론을 개선하는 것으로 알려진 기법을 추상적인 확률적 표현보다 언어 모델에서 더 효과적인 정보 처리를 이끌어내도록 조정했습니다. 우리의 결과는 REFER가 의견을 요약할 때 언어 모델의 공정성을 향상시킨다는 것을 보여줍니다. 이 효과는 특히 더 큰 언어 모델과 강력한 추론 지침을 사용할 때 두드러집니다.

## 📝 요약

이 연구는 의견 요약에서 공정성을 향상시키기 위해 빈도 기반 프레이밍(REPER)을 사용하는 방법을 제안합니다. 기존의 대형 언어 모델(LLM)은 하이퍼파라미터 조정이나 정확한 분포 정보를 필요로 했지만, 이는 실용적이지 않습니다. 연구는 인지 과학의 빈도 기반 표현이 인간의 통계적 추론에서 편향을 줄이는 데 효과적임을 바탕으로, 이를 LLM에 적용하여 공정성을 높일 수 있음을 실험적으로 입증했습니다. 특히, 더 큰 언어 모델과 강력한 추론 지침을 사용할 때 효과가 두드러졌습니다.

## 🎯 주요 포인트

- 1. 다양한 의견을 공정하게 요약하기 위해서는 이러한 관점을 포괄적으로 대표해야 한다.
- 2. 기존 연구에서는 대형 언어 모델(LLM)의 공정성을 위해 하이퍼파라미터 튜닝이나 실제 분포 정보를 프롬프트에 제공하는 방법을 사용했으나, 이는 실용적인 한계가 있다.
- 3. 빈도 기반 표현이 인간의 통계적 추론에서 체계적 편향을 줄이는 데 도움이 된다는 인지 과학 연구를 바탕으로, 본 연구는 빈도 기반 프롬프트(REFFER)가 LLM의 의견 요약에서 공정성을 향상시킬 수 있는지를 조사했다.
- 4. 실험 결과, REFER는 특히 더 큰 언어 모델과 강력한 추론 지침을 사용할 때 의견 요약의 공정성을 향상시킨다.


---

*Generated on 2025-09-23 11:33:24*