---
keywords:
  - Retrieval Augmented Generation
  - Refusal Post-Training
  - In-Context Fine-Tuning
  - Over-Refusal Behavior
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.01476
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:10:59.764842",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Refusal Post-Training",
    "In-Context Fine-Tuning",
    "Over-Refusal Behavior"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.79,
    "Refusal Post-Training": 0.81,
    "In-Context Fine-Tuning": 0.77,
    "Over-Refusal Behavior": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval Augmented Language Models",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RALMs"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the concept of enhancing language models with retrieval mechanisms, which is a trending topic.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Refusal Post-Training",
        "canonical": "Refusal Post-Training",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to improve model responses by training them to refuse uncertain answers.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "In-Context Fine-Tuning",
        "canonical": "In-Context Fine-Tuning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specific method of fine-tuning models using contextual information, enhancing model adaptability.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Over-Refusal Behavior",
        "canonical": "Over-Refusal Behavior",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Highlights a specific issue in model behavior that affects the balance between refusal and answer quality.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "hallucinations",
      "evaluation",
      "influence"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval Augmented Language Models",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Refusal Post-Training",
      "resolved_canonical": "Refusal Post-Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "In-Context Fine-Tuning",
      "resolved_canonical": "In-Context Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Over-Refusal Behavior",
      "resolved_canonical": "Over-Refusal Behavior",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Do Retrieval Augmented Language Models Know When They Don't Know?

**Korean Title:** 회수 증강 언어 모델은 자신이 모를 때를 알고 있는가?

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.01476.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.01476](https://arxiv.org/abs/2509.01476)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (86.5% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (85.1% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (84.7% similar)
- [[2025-09-22/Pointing to a Llama and Call it a Camel_ On the Sycophancy of Multimodal Large Language Models_20250922|Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models]] (84.7% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (84.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Refusal Post-Training|Refusal Post-Training]], [[keywords/In-Context Fine-Tuning|In-Context Fine-Tuning]], [[keywords/Over-Refusal Behavior|Over-Refusal Behavior]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01476v2 Announce Type: replace-cross 
Abstract: Existing Large Language Models (LLMs) occasionally generate plausible yet factually incorrect responses, known as hallucinations. Researchers are primarily using two approaches to mitigate hallucinations, namely Retrieval Augmented Language Models (RALMs) and refusal post-training. However, current research predominantly emphasizes their individual effectiveness while overlooking the evaluation of the refusal capability of RALMs. In this study, we ask the fundamental question: Do RALMs know when they don't know? Specifically, we ask three questions. First, are RALMs well-calibrated regarding different internal and external knowledge states? We examine the influence of various factors. Contrary to expectations, we find that LLMs exhibit significant \textbf{over-refusal} behavior. Then, how does refusal post-training affect the over-refusal issue? We investigate the Refusal-aware Instruction Tuning and In-Context Fine-tuning methods. Our results show that the over-refusal problem is mitigated by In-context fine-tuning. but magnified by R-tuning. However, we also find that the refusal ability may conflict with the quality of the answer. Finally, we develop a simple yet effective refusal method for refusal post-trained models to improve their overall answer quality in terms of refusal and correct answers. Our study provides a more comprehensive understanding of the influence of important factors on RALM systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.01476v2 발표 유형: 교차 교체  
초록: 기존의 대형 언어 모델(LLM)은 때때로 그럴듯하지만 사실과 다른 응답을 생성하는데, 이를 환각(hallucinations)이라고 합니다. 연구자들은 주로 환각을 줄이기 위해 검색 증강 언어 모델(RALM)과 거부 후 학습이라는 두 가지 접근 방식을 사용하고 있습니다. 그러나 현재 연구는 주로 이들의 개별적인 효과에 중점을 두고 있으며, RALM의 거부 능력 평가를 간과하고 있습니다. 이 연구에서는 기본적인 질문을 제기합니다: RALM은 자신이 모를 때를 알 수 있을까요? 구체적으로 세 가지 질문을 던집니다. 첫째, RALM은 다양한 내부 및 외부 지식 상태에 대해 잘 보정되어 있는가? 여러 요인의 영향을 조사합니다. 기대와 달리, LLM은 상당한 \textbf{과도한 거부} 행동을 보인다는 것을 발견했습니다. 그렇다면 거부 후 학습은 과도한 거부 문제에 어떻게 영향을 미칠까요? 우리는 거부 인식 지시 조정과 맥락 내 미세 조정 방법을 조사합니다. 우리의 결과는 맥락 내 미세 조정이 과도한 거부 문제를 완화하지만, R-튜닝에 의해 확대된다는 것을 보여줍니다. 그러나 우리는 또한 거부 능력이 답변의 질과 충돌할 수 있음을 발견했습니다. 마지막으로, 우리는 거부 후 학습된 모델의 전반적인 답변 품질을 거부와 올바른 답변 측면에서 향상시키기 위한 간단하면서도 효과적인 거부 방법을 개발했습니다. 우리의 연구는 RALM 시스템에 중요한 요인이 미치는 영향을 보다 포괄적으로 이해할 수 있도록 합니다.

## 📝 요약

이 연구는 대형 언어 모델(LLM)의 환각 문제를 해결하기 위한 두 가지 접근법, 즉 검색 증강 언어 모델(RALM)과 거부 후 학습에 대해 다룹니다. 연구는 RALM의 거부 능력을 평가하는 데 중점을 두며, RALM이 자신의 지식 한계를 인지하는지를 조사합니다. 연구 결과, LLM이 과도한 거부 행동을 보이며, 이는 In-context 미세 조정으로 완화되지만 R-튜닝으로는 악화됩니다. 또한, 거부 능력이 답변의 질과 충돌할 수 있음을 발견했습니다. 마지막으로, 연구는 거부 후 학습된 모델의 전반적인 답변 품질을 향상시키기 위한 간단하면서도 효과적인 거부 방법을 제안합니다. 이 연구는 RALM 시스템에 영향을 미치는 주요 요인에 대한 포괄적인 이해를 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 종종 사실과 다른 응답을 생성하는 환각(hallucinations) 문제를 겪으며, 이를 완화하기 위해 검색 증강 언어 모델(RALMs)과 거부 후 훈련 방법이 사용된다.
- 2. 연구에서는 RALMs의 거부 능력 평가를 간과한 기존 연구와 달리, RALMs가 자신이 모르는 것을 인지할 수 있는지를 탐구한다.
- 3. RALMs는 내부 및 외부 지식 상태에 대한 과잉 거부(over-refusal) 행동을 보이며, 이는 In-context fine-tuning으로 완화되지만 R-tuning으로는 악화된다.
- 4. 거부 능력은 응답의 질과 상충할 수 있으며, 이를 개선하기 위해 간단하지만 효과적인 거부 방법을 개발하였다.
- 5. 본 연구는 RALM 시스템에 영향을 미치는 중요한 요소들에 대한 포괄적인 이해를 제공한다.


---

*Generated on 2025-09-23 10:10:59*