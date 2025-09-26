---
keywords:
  - Low-bit Quantization
  - Large Language Model
  - Residual Stream
  - Activation Patching
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2506.12044
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:28:10.329170",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-bit Quantization",
    "Large Language Model",
    "Residual Stream",
    "Activation Patching"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-bit Quantization": 0.78,
    "Large Language Model": 0.85,
    "Residual Stream": 0.77,
    "Activation Patching": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Low-bit weight-only quantization",
        "canonical": "Low-bit Quantization",
        "aliases": [
          "Low-bit Quantization",
          "Weight-only Quantization"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's analysis of memory reduction in large language models and is not covered by existing canonical terms.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in the paper, linking to the broader field of language model research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Residual stream magnitudes",
        "canonical": "Residual Stream",
        "aliases": [
          "Residual Magnitudes",
          "Residual Stream Magnitudes"
        ],
        "category": "unique_technical",
        "rationale": "This term is crucial for understanding the error analysis and model behavior discussed in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Activation patching",
        "canonical": "Activation Patching",
        "aliases": [
          "Activation Patching"
        ],
        "category": "unique_technical",
        "rationale": "This technique is highlighted as a key method for analyzing quantization errors, offering a unique perspective.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "examples"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Low-bit weight-only quantization",
      "resolved_canonical": "Low-bit Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
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
      "candidate_surface": "Residual stream magnitudes",
      "resolved_canonical": "Residual Stream",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Activation patching",
      "resolved_canonical": "Activation Patching",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Why Do Some Inputs Break Low-Bit LLM Quantization?

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.12044.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2506.12044](https://arxiv.org/abs/2506.12044)

## 🔗 유사한 논문
- [[2025-09-23/Does quantization affect models' performance on long-context tasks?_20250923|Does quantization affect models' performance on long-context tasks?]] (88.0% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (86.3% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (86.0% similar)
- [[2025-09-24/Speculate Deep and Accurate_ Lossless and Training-Free Acceleration for Offloaded LLMs via Substitute Speculative Decoding_20250924|Speculate Deep and Accurate: Lossless and Training-Free Acceleration for Offloaded LLMs via Substitute Speculative Decoding]] (85.8% similar)
- [[2025-09-24/SBVR_ Summation of BitVector Representation for Efficient LLM Quantization_20250924|SBVR: Summation of BitVector Representation for Efficient LLM Quantization]] (85.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Low-bit Quantization|Low-bit Quantization]], [[keywords/Residual Stream|Residual Stream]], [[keywords/Activation Patching|Activation Patching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.12044v2 Announce Type: replace-cross 
Abstract: Low-bit weight-only quantization significantly reduces the memory footprint of large language models (LLMs), but disproportionately affects certain examples. We analyze diverse 3-4 bit methods on LLMs ranging from 7B-70B in size and find that the quantization errors of 50 pairs of methods are strongly correlated (avg. 0.82) on FineWeb examples. Moreover, the residual stream magnitudes of full-precision models are indicative of future quantization errors. We further establish a hypothesis that relates the residual stream magnitudes to error amplification and accumulation over layers. Using LLM localization techniques, early exiting, and activation patching, we show that examples with large errors rely on precise residual activations in the late layers, and that the outputs of MLP gates play a crucial role in maintaining the perplexity. Our work reveals why certain examples result in large quantization errors and which model components are most critical for performance preservation.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 메모리 사용량을 크게 줄이는 저비트 가중치 양자화가 특정 예제에 불균형적으로 영향을 미친다는 점을 분석합니다. 7B에서 70B 크기의 LLM에 대해 다양한 3-4비트 양자화 방법을 분석한 결과, 50쌍의 방법에서 양자화 오류가 강하게 상관되어 있음(평균 0.82)을 발견했습니다. 또한, 완전 정밀 모델의 잔여 스트림 크기가 미래의 양자화 오류를 예측할 수 있음을 밝혔습니다. 잔여 스트림 크기와 오류 증폭 및 누적 간의 관계를 설명하는 가설을 세웠으며, LLM 로컬라이제이션 기법, 조기 종료, 활성화 패칭을 통해 큰 오류를 가진 예제는 후반 레이어에서 정확한 잔여 활성화에 의존하며, MLP 게이트의 출력이 혼란도를 유지하는 데 중요한 역할을 한다는 것을 보여주었습니다. 이 연구는 특정 예제가 큰 양자화 오류를 발생시키는 이유와 성능 유지에 가장 중요한 모델 구성 요소를 밝혀냅니다.

## 🎯 주요 포인트

- 1. 저비트 가중치 전용 양자화는 대형 언어 모델의 메모리 사용량을 크게 줄이지만 특정 예제에 불균형적인 영향을 미칩니다.
- 2. 50쌍의 3-4비트 양자화 방법의 오류가 FineWeb 예제에서 강하게 상관되어 있음(avg. 0.82)을 발견했습니다.
- 3. 전체 정밀도 모델의 잔여 스트림 크기는 미래의 양자화 오류를 예측하는 지표가 됩니다.
- 4. 잔여 스트림 크기가 오류 증폭 및 누적과 관련이 있다는 가설을 수립했습니다.
- 5. MLP 게이트의 출력이 당혹도를 유지하는 데 중요한 역할을 하며, 큰 오류를 가진 예제는 후반 레이어에서 정확한 잔여 활성화에 의존한다는 것을 보여주었습니다.


---

*Generated on 2025-09-25 16:28:10*