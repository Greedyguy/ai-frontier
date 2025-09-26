<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:50:10.745562",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Chain-of-Thought",
    "Large Language Model",
    "Continuous Space",
    "Self-Distillation",
    "Implicit Chain-of-Thought"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Chain-of-Thought": 0.82,
    "Large Language Model": 0.88,
    "Continuous Space": 0.78,
    "Self-Distillation": 0.8,
    "Implicit Chain-of-Thought": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Chain-of-Thought",
        "canonical": "Chain-of-Thought",
        "aliases": [
          "CoT"
        ],
        "category": "unique_technical",
        "rationale": "Chain-of-Thought is a unique reasoning framework that enhances LLMs by encouraging step-by-step reasoning, crucial for understanding the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion, providing a basis for the proposed reasoning framework.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "Continuous Space",
        "canonical": "Continuous Space",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Continuous Space is a novel concept in the paper, representing the latent space where reasoning is compressed.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Self-Distillation",
        "canonical": "Self-Distillation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Self-Distillation is a key mechanism in the paper for transferring reasoning ability from explicit to implicit CoT.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      },
      {
        "surface": "Implicit CoT",
        "canonical": "Implicit Chain-of-Thought",
        "aliases": [
          "Implicit CoT"
        ],
        "category": "unique_technical",
        "rationale": "Implicit CoT is a variant of the Chain-of-Thought reasoning that operates in continuous space, central to the paper's innovation.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Chain-of-Thought",
      "resolved_canonical": "Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Continuous Space",
      "resolved_canonical": "Continuous Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Self-Distillation",
      "resolved_canonical": "Self-Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Implicit CoT",
      "resolved_canonical": "Implicit Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# CODI: Compressing Chain-of-Thought into Continuous Space via Self-Distillation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.21074.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2502.21074](https://arxiv.org/abs/2502.21074)

## 🔗 유사한 논문
- [[2025-09-24/Soft Tokens, Hard Truths_20250924|Soft Tokens, Hard Truths]] (84.8% similar)
- [[2025-09-18/Uni-cot_ Towards Unified Chain-of-Thought Reasoning Across Text and Vision_20250918|Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (84.8% similar)
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (84.6% similar)
- [[2025-09-18/Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (84.3% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought|Chain-of-Thought]], [[keywords/Continuous Space|Continuous Space]], [[keywords/Self-Distillation|Self-Distillation]], [[keywords/Implicit Chain-of-Thought|Implicit Chain-of-Thought]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.21074v3 Announce Type: replace 
Abstract: Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by encouraging step-by-step reasoning in natural language. However, leveraging a latent continuous space for reasoning may offer benefits in terms of both efficiency and robustness. Prior implicit CoT methods attempt to bypass language completely by reasoning in continuous space but have consistently underperformed compared to the standard explicit CoT approach. We introduce CODI (Continuous Chain-of-Thought via Self-Distillation), a novel training framework that effectively compresses natural language CoT into continuous space. CODI jointly trains a teacher task (Explicit CoT) and a student task (Implicit CoT), distilling the reasoning ability from language into continuous space by aligning the hidden states of a designated token. Our experiments show that CODI is the first implicit CoT approach to match the performance of explicit CoT on GSM8k at the GPT-2 scale, achieving a 3.1x compression rate and outperforming the previous state-of-the-art by 28.2% in accuracy. CODI also demonstrates robustness, generalizable to complex datasets, and interpretability. These results validate that LLMs can reason effectively not only in natural language, but also in a latent continuous space. Code is available at https://github.com/zhenyi4/codi.

## 📝 요약

Chain-of-Thought (CoT) 추론은 대형 언어 모델(LLM)의 자연어 단계별 추론을 강화하지만, 연속적인 잠재 공간을 활용한 추론은 효율성과 견고성 면에서 이점을 제공할 수 있습니다. 기존의 암묵적 CoT 방법은 연속 공간에서 추론하려 했으나 명시적 CoT 접근법에 비해 성능이 낮았습니다. 본 논문에서는 CODI(Continuous Chain-of-Thought via Self-Distillation)라는 새로운 훈련 프레임워크를 소개합니다. CODI는 자연어 CoT를 연속 공간으로 효과적으로 압축하며, 교사 작업(명시적 CoT)과 학생 작업(암묵적 CoT)을 공동 훈련하여 지정된 토큰의 숨겨진 상태를 정렬함으로써 추론 능력을 증류합니다. 실험 결과, CODI는 GPT-2 규모에서 GSM8k 데이터셋에 대해 명시적 CoT와 동등한 성능을 최초로 달성했으며, 3.1배 압축률과 28.2%의 정확도 향상을 보였습니다. CODI는 복잡한 데이터셋에 대한 일반화 가능성과 해석 가능성도 입증했습니다. 이 결과는 LLM이 자연어뿐만 아니라 잠재 연속 공간에서도 효과적으로 추론할 수 있음을 확인시켜 줍니다.

## 🎯 주요 포인트

- 1. CODI는 자연어 연쇄 사고(CoT)를 연속 공간으로 효과적으로 압축하는 새로운 훈련 프레임워크입니다.
- 2. CODI는 Explicit CoT(교사 작업)와 Implicit CoT(학생 작업)를 공동으로 훈련하여 언어 추론 능력을 연속 공간으로 증류합니다.
- 3. CODI는 GPT-2 규모에서 GSM8k 데이터셋에 대해 Explicit CoT와 동등한 성능을 처음으로 달성하였으며, 3.1배의 압축률과 28.2%의 정확도 향상을 이루었습니다.
- 4. CODI는 복잡한 데이터셋에 대한 일반화 가능성과 해석 가능성을 보여주며, 연속 공간에서도 효과적인 추론이 가능함을 입증합니다.
- 5. 연구 결과는 대형 언어 모델이 자연어뿐만 아니라 잠재 연속 공간에서도 효과적으로 추론할 수 있음을 확인합니다.


---

*Generated on 2025-09-24 15:50:10*