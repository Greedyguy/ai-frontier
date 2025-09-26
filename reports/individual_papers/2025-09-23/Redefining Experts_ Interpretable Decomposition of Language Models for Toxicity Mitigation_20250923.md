---
keywords:
  - Large Language Model
  - EigenShift
  - Toxicity Mitigation
  - Neuron Activation
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16660
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:15:56.895735",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "EigenShift",
    "Toxicity Mitigation",
    "Neuron Activation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "EigenShift": 0.78,
    "Toxicity Mitigation": 0.81,
    "Neuron Activation": 0.77
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
        "rationale": "Central to the paper's focus on toxicity mitigation, linking to broader discussions on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "EigenShift",
        "canonical": "EigenShift",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel technique specific to the paper, offering unique insights into model intervention.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.89,
        "link_intent_score": 0.78
      },
      {
        "surface": "Toxicity Mitigation",
        "canonical": "Toxicity Mitigation",
        "aliases": [
          "Toxicity Reduction"
        ],
        "category": "specific_connectable",
        "rationale": "Key theme of the paper, relevant to ongoing research in AI safety.",
        "novelty_score": 0.58,
        "connectivity_score": 0.73,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Neuron Activations",
        "canonical": "Neuron Activation",
        "aliases": [
          "Neural Activation"
        ],
        "category": "specific_connectable",
        "rationale": "Discusses a technical aspect of model behavior, useful for linking to neural network studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "EigenShift",
      "resolved_canonical": "EigenShift",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.89,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Toxicity Mitigation",
      "resolved_canonical": "Toxicity Mitigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.73,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Neuron Activations",
      "resolved_canonical": "Neuron Activation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Redefining Experts: Interpretable Decomposition of Language Models for Toxicity Mitigation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16660.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16660](https://arxiv.org/abs/2509.16660)

## 🔗 유사한 논문
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (84.0% similar)
- [[2025-09-19/Translate, then Detect_ Leveraging Machine Translation for Cross-Lingual Toxicity Classification_20250919|Translate, then Detect: Leveraging Machine Translation for Cross-Lingual Toxicity Classification]] (83.1% similar)
- [[2025-09-23/Jailbreak-Tuning_ Models Efficiently Learn Jailbreak Susceptibility_20250923|Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility]] (82.5% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (82.0% similar)
- [[2025-09-22/Red Teaming Multimodal Language Models_ Evaluating Harm Across Prompt Modalities and Models_20250922|Red Teaming Multimodal Language Models: Evaluating Harm Across Prompt Modalities and Models]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Toxicity Mitigation|Toxicity Mitigation]], [[keywords/Neuron Activation|Neuron Activation]]
**⚡ Unique Technical**: [[keywords/EigenShift|EigenShift]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16660v1 Announce Type: new 
Abstract: Large Language Models have demonstrated impressive fluency across diverse tasks, yet their tendency to produce toxic content remains a critical challenge for AI safety and public trust. Existing toxicity mitigation approaches primarily manipulate individual neuron activations, but these methods suffer from instability, context dependence, and often compromise the model's core language abilities. To address these shortcomings, we investigate three key questions: the stability of neuron-level toxicity indicators, the advantages of structural (layer-wise) representations, and the interpretability of mechanisms driving toxic generation. Through extensive experiments on Jigsaw and ToxiCN datasets, we show that aggregated layer-wise features provide more robust signals than single neurons. Moreover, we observe conceptual limitations in prior works that conflate toxicity detection experts and generation experts within neuron-based interventions. To mitigate this, we propose a novel principled intervention technique, EigenShift, based on eigen-decomposition of the language model's final output layer. This method selectively targets generation-aligned components, enabling precise toxicity suppression without impairing linguistic competence. Our method requires no additional training or fine-tuning, incurs minimal computational cost, and is grounded in rigorous theoretical analysis.

## 📝 요약

대형 언어 모델은 다양한 작업에서 뛰어난 유창성을 보이지만, 유해한 콘텐츠를 생성하는 경향은 AI 안전성과 대중의 신뢰에 중요한 도전 과제로 남아 있습니다. 기존의 유해성 완화 방법은 주로 개별 뉴런 활성화를 조작하지만, 이러한 방법은 불안정하고 맥락에 의존하며 모델의 핵심 언어 능력을 손상시킬 수 있습니다. 본 연구는 뉴런 수준의 유해성 지표의 안정성, 계층적 표현의 장점, 유해 생성 메커니즘의 해석 가능성을 조사합니다. Jigsaw와 ToxiCN 데이터셋을 통해, 계층적 특징이 단일 뉴런보다 더 강력한 신호를 제공함을 보여주었습니다. 또한, 기존 연구의 개념적 한계를 지적하며, 새로운 개입 기법인 EigenShift를 제안합니다. 이 방법은 언어 모델의 최종 출력 계층의 고유값 분해를 기반으로 하여, 생성에 맞춰진 요소를 선택적으로 조정함으로써 언어 능력을 손상시키지 않고 유해성을 억제합니다. 추가적인 훈련이나 미세 조정이 필요 없으며, 최소한의 계산 비용으로 이론적 분석에 기반을 두고 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델의 독성 콘텐츠 생성 문제는 AI 안전성과 대중의 신뢰에 중요한 도전 과제로 남아 있다.
- 2. 기존의 독성 완화 방법은 개별 뉴런 활성화를 조작하지만, 이는 불안정성과 문맥 의존성 문제를 겪는다.
- 3. 연구는 뉴런 수준의 독성 지표의 안정성, 층별 구조적 표현의 장점, 독성 생성 메커니즘의 해석 가능성을 조사한다.
- 4. 실험 결과, 층별 특징의 집계가 단일 뉴런보다 더 강력한 신호를 제공함을 보여준다.
- 5. 제안된 EigenShift 기법은 언어 모델의 최종 출력층의 고유 분해를 기반으로 하여, 언어 능력을 손상시키지 않고 독성을 억제한다.


---

*Generated on 2025-09-24 03:15:56*