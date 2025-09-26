---
keywords:
  - Test-time Scaling
  - Large Language Model
  - Tensor Parallelism
  - Speculative Decoding
  - System-driven Perspective
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19645
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:40:44.899159",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Test-time Scaling",
    "Large Language Model",
    "Tensor Parallelism",
    "Speculative Decoding",
    "System-driven Perspective"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Test-time Scaling": 0.78,
    "Large Language Model": 0.85,
    "Tensor Parallelism": 0.72,
    "Speculative Decoding": 0.74,
    "System-driven Perspective": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Test-time scaling",
        "canonical": "Test-time Scaling",
        "aliases": [
          "TTS"
        ],
        "category": "unique_technical",
        "rationale": "Test-time scaling is a novel concept focusing on optimizing inference time performance, which is crucial for linking system performance discussions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are central to the discussion of scaling and optimization, providing a strong link to existing research in language processing.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Tensor parallelism",
        "canonical": "Tensor Parallelism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Tensor parallelism is a specific optimization technique relevant to scaling discussions, enhancing connectivity with parallel computing research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Speculative decoding",
        "canonical": "Speculative Decoding",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Speculative decoding is an emerging technique in model inference, offering new insights into efficiency improvements.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.74
      },
      {
        "surface": "System-driven perspective",
        "canonical": "System-driven Perspective",
        "aliases": [
          "System Perspective"
        ],
        "category": "unique_technical",
        "rationale": "A system-driven perspective introduces a holistic view on optimization, linking to broader system performance evaluations.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.72,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "compute-optimal",
      "system-optimal",
      "paradigm shift"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Test-time scaling",
      "resolved_canonical": "Test-time Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Tensor parallelism",
      "resolved_canonical": "Tensor Parallelism",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Speculative decoding",
      "resolved_canonical": "Speculative Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "System-driven perspective",
      "resolved_canonical": "System-driven Perspective",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.72,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Are We Scaling the Right Thing? A System Perspective on Test-Time Scaling

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19645.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19645](https://arxiv.org/abs/2509.19645)

## 🔗 유사한 논문
- [[2025-09-23/Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling_20250923|Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling]] (89.9% similar)
- [[2025-09-24/Investigating Test-Time Scaling with Reranking for Machine Translation_20250924|Investigating Test-Time Scaling with Reranking for Machine Translation]] (87.6% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (85.8% similar)
- [[2025-09-17/Slim-SC_ Thought Pruning for Efficient Scaling with Self-Consistency_20250917|Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency]] (85.4% similar)
- [[2025-09-23/Temporal Scaling Law for Large Language Models_20250923|Temporal Scaling Law for Large Language Models]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Tensor Parallelism|Tensor Parallelism]]
**⚡ Unique Technical**: [[keywords/Test-time Scaling|Test-time Scaling]], [[keywords/Speculative Decoding|Speculative Decoding]], [[keywords/System-driven Perspective|System-driven Perspective]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19645v1 Announce Type: cross 
Abstract: Test-time scaling (TTS) has recently emerged as a promising direction to exploit the hidden reasoning capabilities of pre-trained large language models (LLMs). However, existing scaling methods narrowly focus on the compute-optimal Pareto-frontier, ignoring the simple fact that compute-optimal is not always system-optimal. In this work, we propose a system-driven perspective on TTS, analyzing how reasoning models scale against practical metrics, such as latency and cost-per-token. By evaluating the impact of popular optimizations such as tensor parallelism and speculative decoding, our preliminary analysis reveals the limitations of current methods and calls for a paradigm shift toward holistic, system-aware evaluations that capture the true essence of scaling laws at inference time.

## 📝 요약

이 논문은 테스트 시 확장(TTS) 방법론을 통해 사전 학습된 대형 언어 모델(LLM)의 잠재적 추론 능력을 활용하는 새로운 접근을 제안합니다. 기존 방법들이 주로 계산 최적화에 집중하는 반면, 이 연구는 시스템 최적화를 고려하여 지연 시간 및 토큰당 비용과 같은 실용적 지표에 대한 모델의 확장성을 분석합니다. 텐서 병렬 처리와 추측 디코딩 등의 최적화 기법이 미치는 영향을 평가한 결과, 현재 방법의 한계를 드러내며, 추론 시 확장 법칙의 본질을 포착하기 위한 시스템 인식 평가의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 테스트 시 스케일링(TTS)은 사전 학습된 대형 언어 모델의 숨겨진 추론 능력을 활용하는 유망한 방향으로 주목받고 있다.
- 2. 기존의 스케일링 방법은 계산 최적의 파레토 경계에만 집중하여 시스템 최적이 항상 계산 최적과 일치하지 않는다는 점을 간과하고 있다.
- 3. 본 연구에서는 지연 시간 및 토큰당 비용과 같은 실용적인 지표에 대한 추론 모델의 스케일링을 분석하는 시스템 중심의 관점을 제안한다.
- 4. 텐서 병렬 처리 및 추측 디코딩과 같은 최적화의 영향을 평가한 결과, 현재 방법의 한계를 드러내고 추론 시 스케일링 법칙의 본질을 포착하는 전체적이고 시스템 인식적인 평가로의 패러다임 전환이 필요함을 강조한다.


---

*Generated on 2025-09-25 15:40:44*