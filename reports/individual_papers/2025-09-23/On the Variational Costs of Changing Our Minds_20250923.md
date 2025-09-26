---
keywords:
  - Belief Updating
  - Confirmation Bias
  - Kullback-Leibler Divergence
  - Motivated Variational Decision
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17957
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:04:44.417930",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Belief Updating",
    "Confirmation Bias",
    "Kullback-Leibler Divergence",
    "Motivated Variational Decision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Belief Updating": 0.85,
    "Confirmation Bias": 0.78,
    "Kullback-Leibler Divergence": 0.88,
    "Motivated Variational Decision": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "belief updating",
        "canonical": "Belief Updating",
        "aliases": [
          "belief revision",
          "belief change"
        ],
        "category": "unique_technical",
        "rationale": "Belief updating is central to the paper's framework and offers a unique perspective on cognitive processes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "confirmation bias",
        "canonical": "Confirmation Bias",
        "aliases": [
          "cognitive bias",
          "bias"
        ],
        "category": "specific_connectable",
        "rationale": "Confirmation bias is a well-studied phenomenon that connects to broader discussions on cognitive biases.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Kullback-Leibler divergence",
        "canonical": "Kullback-Leibler Divergence",
        "aliases": [
          "KL divergence",
          "information divergence"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in information theory that is crucial for the paper's mathematical framework.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.88
      },
      {
        "surface": "motivated variational decision",
        "canonical": "Motivated Variational Decision",
        "aliases": [
          "variational decision-making",
          "motivated decision"
        ],
        "category": "unique_technical",
        "rationale": "This concept is a novel approach introduced in the paper, linking decision-making with variational principles.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "human mind",
      "pragmatic costs",
      "cognitive costs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "belief updating",
      "resolved_canonical": "Belief Updating",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "confirmation bias",
      "resolved_canonical": "Confirmation Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Kullback-Leibler divergence",
      "resolved_canonical": "Kullback-Leibler Divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "motivated variational decision",
      "resolved_canonical": "Motivated Variational Decision",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# On the Variational Costs of Changing Our Minds

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17957.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17957](https://arxiv.org/abs/2509.17957)

## 🔗 유사한 논문
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (80.2% similar)
- [[2025-09-22/The Psychology of Falsehood_ A Human-Centric Survey of Misinformation Detection_20250922|The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection]] (79.7% similar)
- [[2025-09-22/Assessing invariance to affine transformations in image quality metrics_20250922|Assessing invariance to affine transformations in image quality metrics]] (79.3% similar)
- [[2025-09-18/How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations_20250918|How Does Cognitive Bias Affect Large Language Models? A Case Study on the Anchoring Effect in Price Negotiation Simulations]] (78.9% similar)
- [[2025-09-19/How Bad Is Forming Your Own Multidimensional Opinion?_20250919|How Bad Is Forming Your Own Multidimensional Opinion?]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Kullback-Leibler Divergence|Kullback-Leibler Divergence]]
**🔗 Specific Connectable**: [[keywords/Confirmation Bias|Confirmation Bias]]
**⚡ Unique Technical**: [[keywords/Belief Updating|Belief Updating]], [[keywords/Motivated Variational Decision|Motivated Variational Decision]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17957v1 Announce Type: new 
Abstract: The human mind is capable of extraordinary achievements, yet it often appears to work against itself. It actively defends its cherished beliefs even in the face of contradictory evidence, conveniently interprets information to conform to desired narratives, and selectively searches for or avoids information to suit its various purposes. Despite these behaviours deviating from common normative standards for belief updating, we argue that such 'biases' are not inherently cognitive flaws, but rather an adaptive response to the significant pragmatic and cognitive costs associated with revising one's beliefs. This paper introduces a formal framework that aims to model the influence of these costs on our belief updating mechanisms.
  We treat belief updating as a motivated variational decision, where agents weigh the perceived 'utility' of a belief against the informational cost required to adopt a new belief state, quantified by the Kullback-Leibler divergence from the prior to the variational posterior. We perform computational experiments to demonstrate that simple instantiations of this resource-rational model can be used to qualitatively emulate commonplace human behaviours, including confirmation bias and attitude polarisation. In doing so, we suggest that this framework makes steps toward a more holistic account of the motivated Bayesian mechanics of belief change and provides practical insights for predicting, compensating for, and correcting deviations from desired belief updating processes.

## 📝 요약

이 논문은 인간의 신념 갱신 과정에서 나타나는 편향이 단순한 인지적 결함이 아니라, 신념 수정에 따르는 실용적 및 인지적 비용에 대한 적응적 반응임을 주장합니다. 이를 위해, 신념 갱신을 동기화된 변분 결정으로 모델링하는 형식적 틀을 제시합니다. 이 모델은 신념의 '효용'과 새로운 신념 상태 채택에 필요한 정보 비용을 저울질하며, Kullback-Leibler 발산을 통해 비용을 정량화합니다. 컴퓨터 실험을 통해 이 모델이 확인 편향과 태도 양극화 같은 인간 행동을 모방할 수 있음을 보여줍니다. 이 연구는 신념 변화의 동기화된 베이지안 메커니즘에 대한 포괄적 설명을 제안하고, 바람직한 신념 갱신 과정에서의 편차를 예측하고 보완하는 데 실질적인 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 인간의 신념 갱신 과정에서 나타나는 편향은 인지적 결함이 아니라 신념 수정의 실용적 및 인지적 비용에 대한 적응적 반응으로 설명됩니다.
- 2. 본 논문은 이러한 비용이 신념 갱신 메커니즘에 미치는 영향을 모델링하기 위한 형식적 프레임워크를 제안합니다.
- 3. 신념 갱신을 동기화된 변분적 결정으로 간주하여, 신념의 '효용'과 새로운 신념 상태를 채택하는 데 필요한 정보 비용을 비교합니다.
- 4. 컴퓨터 실험을 통해 이 모델이 확증 편향 및 태도 양극화와 같은 인간 행동을 질적으로 모방할 수 있음을 보여줍니다.
- 5. 이 프레임워크는 신념 변화의 동기화된 베이지안 메커니즘에 대한 보다 포괄적인 설명을 제공하고, 신념 갱신 과정의 편향을 예측하고 보정하는 데 실질적인 통찰을 제공합니다.


---

*Generated on 2025-09-23 23:04:44*