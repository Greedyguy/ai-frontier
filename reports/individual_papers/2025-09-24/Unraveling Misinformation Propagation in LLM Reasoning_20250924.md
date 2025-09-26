<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:52:26.585450",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Misinformation Propagation",
    "Mathematical Reasoning",
    "Factual Corrections"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Misinformation Propagation": 0.88,
    "Mathematical Reasoning": 0.8,
    "Factual Corrections": 0.82
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
        "rationale": "Central to the study, linking to broader discussions on AI models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Misinformation Propagation",
        "canonical": "Misinformation Propagation",
        "aliases": [
          "Misinformation Spread"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, offering a unique angle on LLM challenges.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Mathematical Reasoning",
        "canonical": "Mathematical Reasoning",
        "aliases": [
          "Math Reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Specific application area of LLMs, relevant for linking to reasoning studies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Factual Corrections",
        "canonical": "Factual Corrections",
        "aliases": [
          "Fact Correction"
        ],
        "category": "unique_technical",
        "rationale": "Addresses a specific intervention strategy in LLM reasoning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "reasoning process",
      "accuracy drops"
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
      "candidate_surface": "Misinformation Propagation",
      "resolved_canonical": "Misinformation Propagation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Mathematical Reasoning",
      "resolved_canonical": "Mathematical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Factual Corrections",
      "resolved_canonical": "Factual Corrections",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Unraveling Misinformation Propagation in LLM Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.18555.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2505.18555](https://arxiv.org/abs/2505.18555)

## 🔗 유사한 논문
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (91.1% similar)
- [[2025-09-24/Thinking in a Crowd_ How Auxiliary Information Shapes LLM Reasoning_20250924|Thinking in a Crowd: How Auxiliary Information Shapes LLM Reasoning]] (87.0% similar)
- [[2025-09-23/Neither Stochastic Parroting nor AGI_ LLMs Solve Tasks through Context-Directed Extrapolation from Training Data Priors_20250923|Neither Stochastic Parroting nor AGI: LLMs Solve Tasks through Context-Directed Extrapolation from Training Data Priors]] (86.3% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (85.8% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (85.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Mathematical Reasoning|Mathematical Reasoning]]
**⚡ Unique Technical**: [[keywords/Misinformation Propagation|Misinformation Propagation]], [[keywords/Factual Corrections|Factual Corrections]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18555v2 Announce Type: replace 
Abstract: Large Language Models (LLMs) have demonstrated impressive capabilities in reasoning, positioning them as promising tools for supporting human problem-solving. However, what happens when their performance is affected by misinformation, i.e., incorrect inputs introduced by users due to oversights or gaps in knowledge? Such misinformation is prevalent in real-world interactions with LLMs, yet how it propagates within LLMs' reasoning process remains underexplored. Focusing on mathematical reasoning, we present a comprehensive analysis of how misinformation affects intermediate reasoning steps and final answers. We also examine how effectively LLMs can correct misinformation when explicitly instructed to do so. Even with explicit instructions, LLMs succeed less than half the time in rectifying misinformation, despite possessing correct internal knowledge, leading to significant accuracy drops (10.02% - 72.20%), and the degradation holds with thinking models (4.30% - 19.97%). Further analysis shows that applying factual corrections early in the reasoning process most effectively reduces misinformation propagation, and fine-tuning on synthesized data with early-stage corrections significantly improves reasoning factuality. Our work offers a practical approach to mitigating misinformation propagation.

## 📝 요약

대형 언어 모델(LLM)은 뛰어난 추론 능력을 보이며 인간 문제 해결을 지원하는 도구로 주목받고 있습니다. 그러나 사용자 입력 오류로 인한 잘못된 정보가 모델 성능에 미치는 영향은 충분히 탐구되지 않았습니다. 본 연구는 수학적 추론에서 잘못된 정보가 중간 추론 단계와 최종 답변에 어떻게 영향을 미치는지를 분석하고, LLM이 명시적 지시를 받을 때 잘못된 정보를 얼마나 효과적으로 수정할 수 있는지를 조사했습니다. LLM은 내부적으로 올바른 지식을 가지고 있음에도 불구하고, 명시적 지시에도 불구하고 잘못된 정보를 수정하는 데 절반 이하의 성공률을 보였으며, 이는 정확도에 큰 영향을 미쳤습니다. 초기 단계에서 사실적 수정을 적용하면 잘못된 정보의 전파를 가장 효과적으로 줄일 수 있으며, 초기 단계 수정이 포함된 합성 데이터로 미세 조정하면 추론의 사실성을 크게 향상시킬 수 있음을 발견했습니다. 본 연구는 잘못된 정보 전파를 줄이는 실질적인 접근법을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 인간 문제 해결을 지원하는 유망한 도구로서의 가능성을 보여주고 있지만, 잘못된 정보가 모델의 성능에 미치는 영향은 충분히 탐구되지 않았다.
- 2. 수학적 추론에 초점을 맞춰, 잘못된 정보가 중간 추론 단계와 최종 답변에 미치는 영향을 분석하였다.
- 3. LLMs는 명시적인 지시가 주어져도 잘못된 정보를 수정하는 데 절반 이하의 성공률을 보이며, 이는 정확도에 큰 영향을 미친다.
- 4. 추론 과정 초기에 사실을 교정하는 것이 잘못된 정보의 전파를 가장 효과적으로 줄이며, 초기 단계 교정으로 합성 데이터를 미세 조정하면 추론의 사실성이 크게 향상된다.
- 5. 본 연구는 잘못된 정보 전파를 완화하기 위한 실질적인 접근법을 제시한다.


---

*Generated on 2025-09-24 15:52:26*