<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:22:28.066052",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Abduct-Act-Predict Scaffolding",
    "Causal Inference",
    "Failure Attribution",
    "Counterfactual Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Abduct-Act-Predict Scaffolding": 0.8,
    "Causal Inference": 0.85,
    "Failure Attribution": 0.78,
    "Counterfactual Reasoning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Abduct-Act-Predict Scaffolding",
        "canonical": "Abduct-Act-Predict Scaffolding",
        "aliases": [
          "A2P Scaffolding"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper for causal inference in multi-agent systems, making it a unique technical term.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Causal Inference",
        "canonical": "Causal Inference",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Causal inference is a fundamental concept that connects to various methodologies in machine learning and statistics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Failure Attribution",
        "canonical": "Failure Attribution",
        "aliases": [
          "Error Attribution"
        ],
        "category": "specific_connectable",
        "rationale": "This term is central to the paper's focus on identifying errors in multi-agent systems, providing a specific point of connection.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Counterfactual Reasoning",
        "canonical": "Counterfactual Reasoning",
        "aliases": [
          "Counterfactual Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Counterfactual reasoning is crucial for understanding the causal impact of actions, linking to broader causal analysis techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "pattern recognition",
      "conversation logs",
      "step-level accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Abduct-Act-Predict Scaffolding",
      "resolved_canonical": "Abduct-Act-Predict Scaffolding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Causal Inference",
      "resolved_canonical": "Causal Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Failure Attribution",
      "resolved_canonical": "Failure Attribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Counterfactual Reasoning",
      "resolved_canonical": "Counterfactual Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Abduct, Act, Predict: Scaffolding Causal Inference for Automated Failure Attribution in Multi-Agent Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.10401.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.10401](https://arxiv.org/abs/2509.10401)

## 🔗 유사한 논문
- [[2025-09-19/AEGIS_ Automated Error Generation and Identification for Multi-Agent Systems_20250919|AEGIS: Automated Error Generation and Identification for Multi-Agent Systems]] (87.4% similar)
- [[2025-09-17/An Empirical Study on Failures in Automated Issue Solving_20250917|An Empirical Study on Failures in Automated Issue Solving]] (86.6% similar)
- [[2025-09-18/Who is Introducing the Failure? Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis_20250918|Who is Introducing the Failure? Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis]] (85.0% similar)
- [[2025-09-19/Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents_20250919|Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents]] (84.3% similar)
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass: Towards Reliable Evaluation of Agentic Workflows in Production]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Causal Inference|Causal Inference]]
**🔗 Specific Connectable**: [[keywords/Failure Attribution|Failure Attribution]], [[keywords/Counterfactual Reasoning|Counterfactual Reasoning]]
**⚡ Unique Technical**: [[keywords/Abduct-Act-Predict Scaffolding|Abduct-Act-Predict Scaffolding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10401v2 Announce Type: replace 
Abstract: Failure attribution in multi-agent systems -- pinpointing the exact step where a decisive error occurs -- is a critical yet unsolved challenge. Current methods treat this as a pattern recognition task over long conversation logs, leading to critically low step-level accuracy (below 17\%), which renders them impractical for debugging complex systems. Their core weakness is a fundamental inability to perform robust counterfactual reasoning: to determine if correcting a single action would have actually averted the task failure. To bridge this \emph{counterfactual inference gap}, we introduce Abduct-Act-Predict (A2P) Scaffolding, a novel agent framework that transforms failure attribution from pattern recognition into a structured causal inference task. A2P explicitly guides a large language model through a formal three-step reasoning process within a single inference pass: (1) Abduction, to infer the hidden root causes behind an agent's actions; (2) Action, to define a minimal corrective intervention; and (3) Prediction, to simulate the subsequent trajectory and verify if the intervention resolves the failure. This structured approach leverages the holistic context of the entire conversation while imposing a rigorous causal logic on the model's analysis. Our extensive experiments on the Who\&amp;When benchmark demonstrate its efficacy. On the Algorithm-Generated dataset, A2P achieves 47.46\% step-level accuracy, a 2.85$\times$ improvement over the 16.67\% of the baseline. On the more complex Hand-Crafted dataset, it achieves 29.31\% step accuracy, a 2.43$\times$ improvement over the baseline's 12.07\%. By reframing the problem through a causal lens, A2P Scaffolding provides a robust, verifiable, and significantly more accurate solution for automated failure attribution. Ours code are released at https://github.com/ResearAI/A2P.

## 📝 요약

다중 에이전트 시스템에서 오류 발생 지점을 정확히 찾아내는 것은 중요한 과제입니다. 기존 방법은 긴 대화 로그에서 패턴 인식을 통해 이를 해결하려 하지만, 단계별 정확도가 17% 이하로 낮아 실용적이지 않습니다. 이러한 문제를 해결하기 위해, Abduct-Act-Predict (A2P) Scaffolding이라는 새로운 프레임워크를 제안합니다. A2P는 오류 원인을 추론하고, 최소한의 수정 조치를 정의하며, 이를 통해 오류 해결 여부를 예측하는 세 단계의 인과 추론 과정을 거칩니다. 실험 결과, A2P는 기존 방법보다 두 배 이상의 정확도를 보이며, 자동화된 오류 추적에 있어 더욱 정확하고 검증 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. 다중 에이전트 시스템에서 실패 귀속 문제는 결정적 오류가 발생한 정확한 단계를 식별하는데 있어 중요한 도전 과제입니다.
- 2. 현재 방법들은 긴 대화 로그에서 패턴 인식 작업으로 처리되어 단계 수준의 정확도가 매우 낮습니다(17% 미만).
- 3. Abduct-Act-Predict (A2P) Scaffolding은 실패 귀속을 구조화된 인과 추론 작업으로 전환하는 새로운 에이전트 프레임워크입니다.
- 4. A2P는 대형 언어 모델을 통해 세 가지 단계의 추론 과정을 안내하여 실패를 해결할 수 있는지 검증합니다.
- 5. A2P는 Algorithm-Generated 데이터셋에서 47.46%의 단계 수준 정확도를 달성하여 기존 방법보다 2.85배 개선되었습니다.


---

*Generated on 2025-09-24 14:22:28*