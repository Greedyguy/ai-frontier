<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:20:12.229113",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Explainable AI",
    "Rule Extraction",
    "SHAP",
    "RuleSHAP"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Explainable AI": 0.8,
    "Rule Extraction": 0.78,
    "SHAP": 0.82,
    "RuleSHAP": 0.88
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
        "rationale": "Central to the study, linking to a broad technical concept widely used in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Explainable AI",
        "canonical": "Explainable AI",
        "aliases": [
          "XAI"
        ],
        "category": "specific_connectable",
        "rationale": "Key to understanding and linking methods for bias detection in AI models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Rule Extraction",
        "canonical": "Rule Extraction",
        "aliases": [
          "Rule Induction"
        ],
        "category": "unique_technical",
        "rationale": "A unique method proposed in the paper for bias detection, enhancing specificity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SHAP",
        "canonical": "SHAP",
        "aliases": [
          "Shapley Additive Explanations"
        ],
        "category": "specific_connectable",
        "rationale": "A specific method for model explanation, relevant for linking to explainability techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "RuleSHAP",
        "canonical": "RuleSHAP",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel algorithm introduced in the paper, crucial for understanding the proposed solution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "misinformation",
      "heuristics",
      "bias"
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
      "candidate_surface": "Explainable AI",
      "resolved_canonical": "Explainable AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Rule Extraction",
      "resolved_canonical": "Rule Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SHAP",
      "resolved_canonical": "SHAP",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "RuleSHAP",
      "resolved_canonical": "RuleSHAP",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# Can Global XAI Methods Reveal Injected Bias in LLMs? SHAP vs Rule Extraction vs RuleSHAP

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11189.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.11189](https://arxiv.org/abs/2505.11189)

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (84.7% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (84.7% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (84.3% similar)
- [[2025-09-23/Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM_20250923|Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM]] (84.2% similar)
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Explainable AI|Explainable AI]], [[keywords/SHAP|SHAP]]
**⚡ Unique Technical**: [[keywords/Rule Extraction|Rule Extraction]], [[keywords/RuleSHAP|RuleSHAP]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11189v2 Announce Type: replace 
Abstract: Large language models (LLMs) can amplify misinformation, undermining societal goals like the UN SDGs. We study three documented drivers of misinformation (valence framing, information overload, and oversimplification) which are often shaped by one's default beliefs. Building on evidence that LLMs encode such defaults (e.g., "joy is positive," "math is complex") and can act as "bags of heuristics," we ask: can general belief-driven heuristics behind misinformative behaviour be recovered from LLMs as clear rules? A key obstacle is that global rule-extraction methods in explainable AI (XAI) are built for numerical inputs/outputs, not text. We address this by eliciting global LLM beliefs and mapping them to numerical scores via statistically reliable abstractions, thereby enabling off-the-shelf global XAI to detect belief-related heuristics in LLMs. To obtain ground truth, we hard-code bias-inducing nonlinear heuristics of increasing complexity (univariate, conjunctive, nonconvex) into popular LLMs (ChatGPT and Llama) via system instructions. This way, we find that RuleFit under-detects non-univariate biases, while global SHAP better approximates conjunctive ones but does not yield actionable rules. To bridge this gap, we propose RuleSHAP, a rule-extraction algorithm that couples global SHAP-value aggregations with rule induction to better capture non-univariate bias, improving heuristics detection over RuleFit by +94% (MRR@1) on average. Our results provide a practical pathway for revealing belief-driven biases in LLMs.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 잘못된 정보를 증폭시켜 사회적 목표를 저해할 수 있음을 지적합니다. 연구는 잘못된 정보의 주요 원인인 감정적 틀, 정보 과부하, 과도한 단순화를 조사합니다. LLM이 이러한 기본 신념을 인코딩하고 '휴리스틱의 집합'으로 작용할 수 있다는 점에 착안하여, 이러한 휴리스틱을 명확한 규칙으로 추출할 수 있는지를 탐구합니다. 기존 설명 가능한 AI(XAI) 방법은 텍스트가 아닌 수치 입력/출력에 맞춰져 있어 이를 극복하기 위해 LLM의 글로벌 신념을 수치 점수로 매핑하는 방법을 제안합니다. 이를 통해 LLM의 신념 관련 휴리스틱을 탐지할 수 있습니다. 연구는 ChatGPT와 Llama에 편향을 유도하는 비선형 휴리스틱을 하드코딩하여, RuleFit과 SHAP의 성능을 비교합니다. RuleFit은 비단일 변수 편향을 잘 감지하지 못하지만, SHAP는 결합적 편향을 더 잘 포착합니다. 이를 개선하기 위해 RuleSHAP 알고리즘을 제안하여 비단일 변수 편향 감지 성능을 평균 94% 향상시켰습니다. 이 결과는 LLM의 신념 기반 편향을 드러내는 실용적 경로를 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 잘못된 정보를 증폭시켜 UN 지속 가능한 개발 목표(SDGs)와 같은 사회적 목표를 저해할 수 있다.
- 2. 잘못된 정보의 주요 원인으로는 감정적 틀, 정보 과부하, 과도한 단순화가 있으며, 이는 개인의 기본 신념에 의해 형성된다.
- 3. LLM의 전역 설명 가능 인공지능(XAI) 방법은 텍스트가 아닌 수치 입력/출력에 맞춰져 있어, 신념 관련 휴리스틱을 감지하는 데 한계가 있다.
- 4. RuleSHAP 알고리즘은 전역 SHAP 값 집계와 규칙 유도를 결합하여 비단일변량 편향을 더 잘 포착하고, RuleFit보다 평균 94% 향상된 휴리스틱 감지를 제공한다.
- 5. 연구 결과는 LLM에서 신념에 기반한 편향을 드러내는 실질적인 경로를 제시한다.


---

*Generated on 2025-09-24 14:20:12*