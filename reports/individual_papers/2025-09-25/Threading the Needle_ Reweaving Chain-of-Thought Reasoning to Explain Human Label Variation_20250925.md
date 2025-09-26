---
keywords:
  - Large Language Model
  - Chain-of-Thought Reasoning
  - Human Label Variation
  - Discourse Segmenters
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2505.23368
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:55:17.580320",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought Reasoning",
    "Human Label Variation",
    "Discourse Segmenters"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Chain-of-Thought Reasoning": 0.8,
    "Human Label Variation": 0.78,
    "Discourse Segmenters": 0.77
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
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on reasoning and label variation, linking to broader NLP concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought Reasoning",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT Reasoning",
          "Reasoning Chains"
        ],
        "category": "unique_technical",
        "rationale": "A novel reasoning approach that underpins the methodology discussed in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Human Label Variation",
        "canonical": "Human Label Variation",
        "aliases": [
          "Label Variation",
          "HLV"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for understanding the variability in human annotations, central to the paper's evaluation framework.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Discourse Segmenters",
        "canonical": "Discourse Segmenters",
        "aliases": [
          "Linguistic Segmenters"
        ],
        "category": "specific_connectable",
        "rationale": "Important for extracting reasoning components, linking to linguistic processing techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "framework",
      "dataset"
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
      "candidate_surface": "Human Label Variation",
      "resolved_canonical": "Human Label Variation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Discourse Segmenters",
      "resolved_canonical": "Discourse Segmenters",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Threading the Needle: Reweaving Chain-of-Thought Reasoning to Explain Human Label Variation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23368.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2505.23368](https://arxiv.org/abs/2505.23368)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (87.4% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (87.0% similar)
- [[2025-09-25/HoT_ Highlighted Chain of Thought for Referencing Supporting Facts from Inputs_20250925|HoT: Highlighted Chain of Thought for Referencing Supporting Facts from Inputs]] (86.4% similar)
- [[2025-09-24/LiTEx_ A Linguistic Taxonomy of Explanations for Understanding Within-Label Variation in Natural Language Inference_20250924|LiTEx: A Linguistic Taxonomy of Explanations for Understanding Within-Label Variation in Natural Language Inference]] (86.0% similar)
- [[2025-09-24/Please Translate Again_ Two Simple Experiments on Whether Human-Like Reasoning Helps Translation_20250924|Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation]] (85.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Discourse Segmenters|Discourse Segmenters]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]], [[keywords/Human Label Variation|Human Label Variation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23368v3 Announce Type: replace 
Abstract: The recent rise of reasoning-tuned Large Language Models (LLMs)--which generate chains of thought (CoTs) before giving the final answer--has attracted significant attention and offers new opportunities for gaining insights into human label variation, which refers to plausible differences in how multiple annotators label the same data instance. Prior work has shown that LLM-generated explanations can help align model predictions with human label distributions, but typically adopt a reverse paradigm: producing explanations based on given answers. In contrast, CoTs provide a forward reasoning path that may implicitly embed rationales for each answer option, before generating the answers. We thus propose a novel LLM-based pipeline enriched with linguistically-grounded discourse segmenters to extract supporting and opposing statements for each answer option from CoTs with improved accuracy. We also propose a rank-based HLV evaluation framework that prioritizes the ranking of answers over exact scores, which instead favor direct comparison of label distributions. Our method outperforms a direct generation method as well as baselines on three datasets, and shows better alignment of ranking methods with humans, highlighting the effectiveness of our approach.

## 📝 요약

최근 논리 조정된 대형 언어 모델(LLM)이 주목받고 있으며, 이는 최종 답변을 제시하기 전에 사고의 흐름(CoTs)을 생성하여 인간의 라벨 변이를 이해하는 데 새로운 기회를 제공합니다. 기존 연구는 LLM이 생성한 설명이 모델 예측을 인간 라벨 분포와 맞추는 데 도움이 될 수 있음을 보여주었지만, 일반적으로 주어진 답변을 기반으로 설명을 생성하는 역방향 접근 방식을 채택했습니다. 이에 반해 CoTs는 각 답변 옵션에 대한 이유를 암묵적으로 포함할 수 있는 순방향 추론 경로를 제공합니다. 우리는 CoTs에서 각 답변 옵션에 대한 지지 및 반대 진술을 추출하기 위해 언어적으로 기반을 둔 담화 분할기를 활용한 새로운 LLM 기반 파이프라인을 제안합니다. 또한, 답변의 순위를 우선시하는 순위 기반 HLV 평가 프레임워크를 제안하여 라벨 분포의 직접 비교를 선호합니다. 우리의 방법은 세 가지 데이터셋에서 직접 생성 방법 및 기준선을 능가하며, 인간과의 순위 방법 정렬에서 더 나은 성능을 보여줍니다.

## 🎯 주요 포인트

- 1. 최근의 추론 조정 대형 언어 모델(LLM)은 답변을 생성하기 전에 사고의 연쇄(CoTs)를 생성하여 인간의 레이블 변동에 대한 통찰력을 제공한다.
- 2. CoTs는 각 답변 옵션에 대한 근거를 암묵적으로 포함할 수 있는 순방향 추론 경로를 제공한다.
- 3. 우리는 CoTs에서 각 답변 옵션에 대한 지지 및 반대 진술을 추출하기 위해 언어적으로 기반을 둔 담화 분할기를 활용한 새로운 LLM 기반 파이프라인을 제안한다.
- 4. 제안된 방법은 세 가지 데이터셋에서 직접 생성 방법 및 기준선을 능가하며, 인간과의 순위 방법 정렬에서 더 나은 성능을 보여준다.
- 5. 랭크 기반 HLV 평가 프레임워크를 제안하여 정확한 점수보다 레이블 분포의 직접 비교를 우선시한다.


---

*Generated on 2025-09-26 08:55:17*