---
keywords:
  - Decomposed Criteria-Based Evaluation
  - Large Language Model
  - Precision in LLM Evaluation
  - Recall in LLM Evaluation
  - Multi-Jurisdictional Reasoning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16093
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:28:41.075807",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Decomposed Criteria-Based Evaluation",
    "Large Language Model",
    "Precision in LLM Evaluation",
    "Recall in LLM Evaluation",
    "Multi-Jurisdictional Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Decomposed Criteria-Based Evaluation": 0.78,
    "Large Language Model": 0.85,
    "Precision in LLM Evaluation": 0.7,
    "Recall in LLM Evaluation": 0.7,
    "Multi-Jurisdictional Reasoning": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DeCE",
        "canonical": "Decomposed Criteria-Based Evaluation",
        "aliases": [
          "DeCE"
        ],
        "category": "unique_technical",
        "rationale": "DeCE is a novel evaluation framework introduced in the paper, offering a new approach to LLM evaluation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "LLM",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion, providing a broad technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "precision",
        "canonical": "Precision in LLM Evaluation",
        "aliases": [
          "factual accuracy",
          "relevance"
        ],
        "category": "specific_connectable",
        "rationale": "Precision is a key component of the DeCE framework, crucial for understanding LLM evaluation.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "recall",
        "canonical": "Recall in LLM Evaluation",
        "aliases": [
          "coverage of required concepts"
        ],
        "category": "specific_connectable",
        "rationale": "Recall complements precision in the DeCE framework, essential for comprehensive LLM evaluation.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "multi-jurisdictional reasoning",
        "canonical": "Multi-Jurisdictional Reasoning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is specific to the legal QA task discussed, highlighting the complexity of the evaluation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "BLEU",
      "ROUGE",
      "model-agnostic",
      "domain-general"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DeCE",
      "resolved_canonical": "Decomposed Criteria-Based Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LLM",
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
      "candidate_surface": "precision",
      "resolved_canonical": "Precision in LLM Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "recall",
      "resolved_canonical": "Recall in LLM Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "multi-jurisdictional reasoning",
      "resolved_canonical": "Multi-Jurisdictional Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses

**Korean Title:** 포인트와이즈 점수를 넘어서: LLM 응답의 분해된 기준 기반 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16093.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16093](https://arxiv.org/abs/2509.16093)

## 🔗 유사한 논문
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (83.5% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (83.3% similar)
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (83.0% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (82.2% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Precision in LLM Evaluation|Precision in LLM Evaluation]], [[keywords/Recall in LLM Evaluation|Recall in LLM Evaluation]]
**⚡ Unique Technical**: [[keywords/Decomposed Criteria-Based Evaluation|Decomposed Criteria-Based Evaluation]], [[keywords/Multi-Jurisdictional Reasoning|Multi-Jurisdictional Reasoning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16093v1 Announce Type: cross 
Abstract: Evaluating long-form answers in high-stakes domains such as law or medicine remains a fundamental challenge. Standard metrics like BLEU and ROUGE fail to capture semantic correctness, and current LLM-based evaluators often reduce nuanced aspects of answer quality into a single undifferentiated score. We introduce DeCE, a decomposed LLM evaluation framework that separates precision (factual accuracy and relevance) and recall (coverage of required concepts), using instance-specific criteria automatically extracted from gold answer requirements. DeCE is model-agnostic and domain-general, requiring no predefined taxonomies or handcrafted rubrics. We instantiate DeCE to evaluate different LLMs on a real-world legal QA task involving multi-jurisdictional reasoning and citation grounding. DeCE achieves substantially stronger correlation with expert judgments ($r=0.78$), compared to traditional metrics ($r=0.12$), pointwise LLM scoring ($r=0.35$), and modern multidimensional evaluators ($r=0.48$). It also reveals interpretable trade-offs: generalist models favor recall, while specialized models favor precision. Importantly, only 11.95% of LLM-generated criteria required expert revision, underscoring DeCE's scalability. DeCE offers an interpretable and actionable LLM evaluation framework in expert domains.

## 🔍 Abstract (한글 번역)

arXiv:2509.16093v1 발표 유형: 교차  
초록: 법률이나 의학과 같은 고위험 분야에서 장문의 답변을 평가하는 것은 여전히 근본적인 도전 과제로 남아 있습니다. BLEU 및 ROUGE와 같은 표준 지표는 의미적 정확성을 포착하지 못하며, 현재의 LLM 기반 평가자들은 종종 답변 품질의 미묘한 측면을 단일한 비차별적 점수로 축소합니다. 우리는 정밀도(사실적 정확성과 관련성)와 재현율(필요한 개념의 포괄성)을 분리하여, 골드 답변 요구사항에서 자동으로 추출한 사례별 기준을 사용하는 분해된 LLM 평가 프레임워크인 DeCE를 소개합니다. DeCE는 사전 정의된 분류 체계나 수작업으로 작성된 루브릭이 필요 없는 모델 불가지론적이며 도메인 일반적입니다. 우리는 다중 관할권적 추론과 인용 근거를 포함하는 실제 법률 QA 작업에서 다양한 LLM을 평가하기 위해 DeCE를 구현합니다. DeCE는 전통적인 지표($r=0.12$), 점별 LLM 점수($r=0.35$), 현대 다차원 평가자($r=0.48$)에 비해 전문가 판단과의 상관관계가 상당히 강합니다($r=0.78$). 또한 해석 가능한 절충점을 드러냅니다: 일반 모델은 재현율을 선호하는 반면, 전문 모델은 정밀도를 선호합니다. 중요한 점은, LLM이 생성한 기준 중 전문가 수정이 필요한 것은 단 11.95%에 불과하여 DeCE의 확장 가능성을 강조합니다. DeCE는 전문가 도메인에서 해석 가능하고 실행 가능한 LLM 평가 프레임워크를 제공합니다.

## 📝 요약

이 논문은 법률 및 의학과 같은 고위험 분야에서 장문의 답변을 평가하는 데 있어 기존의 BLEU 및 ROUGE와 같은 지표가 의미적 정확성을 포착하지 못하는 문제를 해결하기 위해 DeCE라는 평가 프레임워크를 제안합니다. DeCE는 정밀도(사실 정확성과 관련성)와 재현율(필요한 개념의 포괄성)을 분리하여 평가하며, 이는 금 답변 요구사항에서 자동으로 추출된 기준을 사용합니다. 이 프레임워크는 특정 모델이나 분야에 구애받지 않으며, 사전 정의된 분류 체계나 수작업으로 작성된 기준이 필요하지 않습니다. 실제 법률 QA 작업에 적용한 결과, DeCE는 전문가 판단과의 상관관계가 기존 지표보다 훨씬 높았으며, 해석 가능한 평가 결과를 제공합니다. DeCE는 전문가 도메인에서 해석 가능하고 실행 가능한 평가 프레임워크로서의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. DeCE는 정밀도와 재현율을 분리하여 평가하는 LLM 평가 프레임워크로, 사실적 정확성과 관련성을 측정합니다.
- 2. DeCE는 특정 모델이나 도메인에 구애받지 않으며, 사전 정의된 분류 체계나 수작업으로 작성된 기준이 필요하지 않습니다.
- 3. 법률 분야의 실제 QA 작업에서 DeCE는 전문가 판단과의 상관관계가 매우 높아 기존 평가 지표보다 우수한 성능을 보였습니다.
- 4. 일반 모델은 재현율을, 전문 모델은 정밀도를 중시하는 경향을 보여주는 해석 가능한 트레이드오프를 드러냅니다.
- 5. LLM이 생성한 기준 중 전문가 수정이 필요한 경우는 11.95%에 불과하여 DeCE의 확장 가능성을 강조합니다.


---

*Generated on 2025-09-23 09:28:41*