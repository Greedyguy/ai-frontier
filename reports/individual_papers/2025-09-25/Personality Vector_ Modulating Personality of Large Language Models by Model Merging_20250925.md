---
keywords:
  - Large Language Model
  - Personality Modulation
  - Model Merging
  - Personality Vectors
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19727
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:44:37.462254",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Personality Modulation",
    "Model Merging",
    "Personality Vectors"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Personality Modulation": 0.78,
    "Model Merging": 0.77,
    "Personality Vectors": 0.82
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
        "rationale": "Large Language Models are central to the paper's discussion and connect to many related concepts in AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Personality Modulation",
        "canonical": "Personality Modulation",
        "aliases": [
          "Personality Adjustment",
          "Trait Modulation"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method proposed in the paper, focusing on modifying LLMs to exhibit personality traits.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Model Merging",
        "canonical": "Model Merging",
        "aliases": [
          "Model Integration",
          "Model Combination"
        ],
        "category": "unique_technical",
        "rationale": "Model Merging is a unique approach discussed in the paper, enabling the integration of personality traits into LLMs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Personality Vectors",
        "canonical": "Personality Vectors",
        "aliases": [
          "Trait Vectors",
          "Personality Embeddings"
        ],
        "category": "unique_technical",
        "rationale": "Personality Vectors are a central innovation in the paper, allowing for the modulation of personality traits in LLMs.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "pre-trained model",
      "fine-tuned model",
      "downstream models"
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
      "candidate_surface": "Personality Modulation",
      "resolved_canonical": "Personality Modulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Model Merging",
      "resolved_canonical": "Model Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Personality Vectors",
      "resolved_canonical": "Personality Vectors",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Personality Vector: Modulating Personality of Large Language Models by Model Merging

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19727.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19727](https://arxiv.org/abs/2509.19727)

## 🔗 유사한 논문
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (88.8% similar)
- [[2025-09-23/Psychometric Personality Shaping Modulates Capabilities and Safety in Language Models_20250923|Psychometric Personality Shaping Modulates Capabilities and Safety in Language Models]] (88.0% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (84.4% similar)
- [[2025-09-23/Probabilistic Token Alignment for Large Language Model Fusion_20250923|Probabilistic Token Alignment for Large Language Model Fusion]] (84.1% similar)
- [[2025-09-22/Beyond Linear Steering_ Unified Multi-Attribute Control for Language Models_20250922|Beyond Linear Steering: Unified Multi-Attribute Control for Language Models]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Personality Modulation|Personality Modulation]], [[keywords/Model Merging|Model Merging]], [[keywords/Personality Vectors|Personality Vectors]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19727v1 Announce Type: new 
Abstract: Driven by the demand for personalized AI systems, there is growing interest in aligning the behavior of large language models (LLMs) with human traits such as personality. Previous attempts to induce personality in LLMs have shown promising results, but they struggle to capture the continuous and multidimensional nature of human traits. In this work, we propose a novel method for personality modulation in LLMs via model merging. Specifically, we construct personality vectors by subtracting the weights of a pre-trained model from those of the fine-tuned model on a given personality trait. By merging personality vectors, we enable LLMs to exhibit desired personality traits without additional training. Extensive experiments show that personality vectors enable continuous control over trait intensity and support the composition of multiple traits. Furthermore, personality vectors transfer across diverse downstream models, suggesting that they encode generalizable representations of personality. Our code is available at here.

## 📝 요약

이 논문은 개인화된 AI 시스템의 필요성에 따라 대형 언어 모델(LLM)의 성격 특성 조정을 위한 새로운 방법을 제안합니다. 기존의 시도들은 인간의 성격을 연속적이고 다차원적으로 반영하는 데 어려움을 겪었습니다. 본 연구에서는 모델 병합을 통해 성격 벡터를 생성하여, 사전 훈련된 모델과 특정 성격 특성으로 미세 조정된 모델의 가중치 차이를 이용합니다. 이를 통해 추가 훈련 없이 LLM이 원하는 성격 특성을 나타낼 수 있습니다. 실험 결과, 성격 벡터는 성격 강도의 연속적 조절 및 다중 특성의 조합을 지원하며, 다양한 모델에 일반화 가능한 성격 표현을 제공함을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 행동을 인간의 성격과 같은 특성에 맞추려는 연구가 증가하고 있습니다.
- 2. 본 연구에서는 모델 병합을 통해 LLM의 성격 조절을 위한 새로운 방법을 제안합니다.
- 3. 성격 벡터를 사용하여 추가 훈련 없이 LLM이 원하는 성격 특성을 나타낼 수 있도록 합니다.
- 4. 실험 결과, 성격 벡터는 특성 강도의 연속적 조절과 다중 특성의 조합을 지원합니다.
- 5. 성격 벡터는 다양한 다운스트림 모델에 걸쳐 전이 가능하며, 일반화 가능한 성격 표현을 인코딩합니다.


---

*Generated on 2025-09-26 08:44:37*