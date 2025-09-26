---
keywords:
  - Coreference Resolution
  - Large Language Model
  - Multilingual Coreference Resolution
  - Instruction Tuning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17505
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:00:17.854716",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Coreference Resolution",
    "Large Language Model",
    "Multilingual Coreference Resolution",
    "Instruction Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Coreference Resolution": 0.78,
    "Large Language Model": 0.8,
    "Multilingual Coreference Resolution": 0.77,
    "Instruction Tuning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Coreference Resolution",
        "canonical": "Coreference Resolution",
        "aliases": [
          "CR"
        ],
        "category": "unique_technical",
        "rationale": "Coreference Resolution is a specific task within NLP that this paper aims to improve, making it a key concept for linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's methodology, offering broad connections to existing NLP research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multilingual Coreference Resolution",
        "canonical": "Multilingual Coreference Resolution",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This specific application of Coreference Resolution across multiple languages is a novel contribution of the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Instruction Tuning",
        "canonical": "Instruction Tuning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Instruction Tuning is a specific technique used in the paper to enhance LLM performance, relevant for linking to related methodologies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "methodology",
      "task-specific architectures"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Coreference Resolution",
      "resolved_canonical": "Coreference Resolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multilingual Coreference Resolution",
      "resolved_canonical": "Multilingual Coreference Resolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Instruction Tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# CorefInst: Leveraging LLMs for Multilingual Coreference Resolution

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17505.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17505](https://arxiv.org/abs/2509.17505)

## 🔗 유사한 논문
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (84.5% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.3% similar)
- [[2025-09-23/Reasoning Core_ A Scalable RL Environment for LLM Symbolic Reasoning_20250923|Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning]] (83.9% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (83.5% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Instruction Tuning|Instruction Tuning]]
**⚡ Unique Technical**: [[keywords/Coreference Resolution|Coreference Resolution]], [[keywords/Multilingual Coreference Resolution|Multilingual Coreference Resolution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17505v1 Announce Type: cross 
Abstract: Coreference Resolution (CR) is a crucial yet challenging task in natural language understanding, often constrained by task-specific architectures and encoder-based language models that demand extensive training and lack adaptability. This study introduces the first multilingual CR methodology which leverages decoder-only LLMs to handle both overt and zero mentions. The article explores how to model the CR task for LLMs via five different instruction sets using a controlled inference method. The approach is evaluated across three LLMs; Llama 3.1, Gemma 2, and Mistral 0.3. The results indicate that LLMs, when instruction-tuned with a suitable instruction set, can surpass state-of-the-art task-specific architectures. Specifically, our best model, a fully fine-tuned Llama 3.1 for multilingual CR, outperforms the leading multilingual CR model (i.e., Corpipe 24 single stage variant) by 2 pp on average across all languages in the CorefUD v1.2 dataset collection.

## 📝 요약

이 연구는 자연어 이해에서 중요한 과제인 언급 해소(CR)를 다루며, 기존의 과제 특화 아키텍처와 인코더 기반 언어 모델의 한계를 극복하기 위해 디코더 전용 대규모 언어 모델(LLM)을 활용한 최초의 다국어 CR 방법론을 제안합니다. 연구는 LLM을 위한 CR 과제를 다섯 가지 명령어 세트를 통해 모델링하고, 이를 제어된 추론 방법으로 평가합니다. Llama 3.1, Gemma 2, Mistral 0.3 세 가지 LLM을 대상으로 평가한 결과, 적절한 명령어 세트로 조정된 LLM이 최첨단 과제 특화 아키텍처를 능가할 수 있음을 보여줍니다. 특히, 완전히 미세 조정된 Llama 3.1 모델은 CorefUD v1.2 데이터셋에서 모든 언어에 대해 평균 2pp 향상된 성능을 보이며, 기존의 선도적인 다국어 CR 모델을 능가했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 디코더 전용 대형 언어 모델(LLM)을 활용하여 다국어 대명사 해소(CR) 방법론을 처음으로 제안합니다.
- 2. 다섯 가지 다른 명령 세트를 사용하여 LLM을 위한 CR 작업을 모델링하는 방법을 탐구합니다.
- 3. Llama 3.1, Gemma 2, Mistral 0.3의 세 가지 LLM을 통해 접근 방식을 평가합니다.
- 4. 적절한 명령 세트로 조정된 LLM이 최첨단 작업별 아키텍처를 능가할 수 있음을 보여줍니다.
- 5. 완전히 미세 조정된 Llama 3.1 모델이 CorefUD v1.2 데이터셋에서 평균 2 pp 더 나은 성능을 보였습니다.


---

*Generated on 2025-09-24 00:00:17*