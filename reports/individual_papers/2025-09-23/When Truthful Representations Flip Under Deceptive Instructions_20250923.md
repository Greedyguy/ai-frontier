---
keywords:
  - Large Language Model
  - Sparse Autoencoder
  - Deceptive Instruction
  - Truthful Representation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2507.22149
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:30:33.578276",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Sparse Autoencoder",
    "Deceptive Instruction",
    "Truthful Representation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Sparse Autoencoder": 0.78,
    "Deceptive Instruction": 0.82,
    "Truthful Representation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, providing a broad technical context for linking.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Sparse Autoencoders",
        "canonical": "Sparse Autoencoder",
        "aliases": [
          "SAE"
        ],
        "category": "specific_connectable",
        "rationale": "Key technique used for detecting representational shifts, offering specific connectivity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deceptive Instructions",
        "canonical": "Deceptive Instruction",
        "aliases": [
          "Malicious Instructions"
        ],
        "category": "unique_technical",
        "rationale": "Unique to the study's focus on how instructions alter model behavior.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Truthful Representations",
        "canonical": "Truthful Representation",
        "aliases": [
          "Honest Representations"
        ],
        "category": "unique_technical",
        "rationale": "Critical for contrasting with deceptive instructions, enhancing specificity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "factual verification task",
      "internal representations",
      "layer-wise"
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
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Sparse Autoencoders",
      "resolved_canonical": "Sparse Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deceptive Instructions",
      "resolved_canonical": "Deceptive Instruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Truthful Representations",
      "resolved_canonical": "Truthful Representation",
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

# When Truthful Representations Flip Under Deceptive Instructions?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.22149.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2507.22149](https://arxiv.org/abs/2507.22149)

## 🔗 유사한 논문
- [[2025-09-23/Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM_20250923|Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM]] (89.3% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (85.7% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.2% similar)
- [[2025-09-22/Natural Fingerprints of Large Language Models_20250922|Natural Fingerprints of Large Language Models]] (84.5% similar)
- [[2025-09-22/Knowledge-Driven Hallucination in Large Language Models_ An Empirical Study on Process Modeling_20250922|Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Sparse Autoencoder|Sparse Autoencoder]]
**⚡ Unique Technical**: [[keywords/Deceptive Instruction|Deceptive Instruction]], [[keywords/Truthful Representation|Truthful Representation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.22149v3 Announce Type: replace 
Abstract: Large language models (LLMs) tend to follow maliciously crafted instructions to generate deceptive responses, posing safety challenges. How deceptive instructions alter the internal representations of LLM compared to truthful ones remains poorly understood beyond output analysis. To bridge this gap, we investigate when and how these representations ``flip'', such as from truthful to deceptive, under deceptive versus truthful/neutral instructions. Analyzing the internal representations of Llama-3.1-8B-Instruct and Gemma-2-9B-Instruct on a factual verification task, we find the model's instructed True/False output is predictable via linear probes across all conditions based on the internal representation. Further, we use Sparse Autoencoders (SAEs) to show that the Deceptive instructions induce significant representational shifts compared to Truthful/Neutral representations (which are similar), concentrated in early-to-mid layers and detectable even on complex datasets. We also identify specific SAE features highly sensitive to deceptive instruction and use targeted visualizations to confirm distinct truthful/deceptive representational subspaces. % Our analysis pinpoints layer-wise and feature-level correlates of instructed dishonesty, offering insights for LLM detection and control. Our findings expose feature- and layer-level signatures of deception, offering new insights for detecting and mitigating instructed dishonesty in LLMs.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 악의적으로 조작된 지시를 따를 때 발생하는 안전 문제를 다룹니다. 연구는 LLM의 내부 표현이 진실한 지시와 비교하여 어떻게 변화하는지를 조사합니다. Llama-3.1-8B-Instruct와 Gemma-2-9B-Instruct 모델을 사용하여 사실 검증 작업에서 내부 표현을 분석한 결과, 모델의 진실/거짓 출력이 내부 표현을 통해 예측 가능함을 발견했습니다. 특히, Sparse Autoencoders(SAEs)를 통해 거짓 지시가 진실/중립 지시보다 초기부터 중간 레이어에 걸쳐 더 큰 표현 변화를 유도한다는 것을 확인했습니다. 또한, 특정 SAE 특징이 거짓 지시에 민감하게 반응하며, 이를 통해 진실과 거짓의 표현적 차이를 시각화했습니다. 이러한 분석은 LLM의 거짓 지시 탐지 및 제어에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 악의적으로 조작된 지시를 따라 기만적인 응답을 생성할 수 있어 안전 문제를 야기한다.
- 2. Llama-3.1-8B-Instruct와 Gemma-2-9B-Instruct 모델의 내부 표현을 분석한 결과, 내부 표현을 기반으로 모델의 True/False 출력이 모든 조건에서 선형 프로브를 통해 예측 가능함을 발견했다.
- 3. Sparse Autoencoders(SAEs)를 사용하여 기만적인 지시가 진실/중립적 표현에 비해 상당한 표현적 변화를 유도하며, 이는 초기부터 중간 레이어에 집중되어 있음을 보여준다.
- 4. 특정 SAE 특징이 기만적인 지시에 매우 민감하며, 이를 통해 진실/기만적 표현 하위 공간을 시각화하여 확인했다.
- 5. 연구 결과는 LLM에서의 기만적 지시 탐지 및 제어를 위한 새로운 통찰을 제공하며, 레이어 및 특징 수준에서의 기만성 서명을 드러낸다.


---

*Generated on 2025-09-24 00:30:33*