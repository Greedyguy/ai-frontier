---
keywords:
  - Large Language Model
  - Mixed-Precision Quantization
  - Shapley-based Progressive Quantization Estimation
  - Interaction-aware Mixed-Precision Quantization
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15455
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:25:06.297474",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Mixed-Precision Quantization",
    "Shapley-based Progressive Quantization Estimation",
    "Interaction-aware Mixed-Precision Quantization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Mixed-Precision Quantization": 0.88,
    "Shapley-based Progressive Quantization Estimation": 0.92,
    "Interaction-aware Mixed-Precision Quantization": 0.9
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
        "rationale": "Large Language Models are central to the paper's focus on quantization techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Mixed-Precision Quantization",
        "canonical": "Mixed-Precision Quantization",
        "aliases": [
          "MPQ"
        ],
        "category": "unique_technical",
        "rationale": "This is a core technique discussed in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Shapley-based Progressive Quantization Estimation",
        "canonical": "Shapley-based Progressive Quantization Estimation",
        "aliases": [
          "SPQE"
        ],
        "category": "unique_technical",
        "rationale": "A novel method introduced in the paper, important for linking to quantization strategies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.92
      },
      {
        "surface": "Interaction-aware Mixed-Precision Quantization",
        "canonical": "Interaction-aware Mixed-Precision Quantization",
        "aliases": [
          "IMPQ"
        ],
        "category": "unique_technical",
        "rationale": "The main contribution of the paper, essential for understanding the proposed optimization approach.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
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
      "candidate_surface": "Mixed-Precision Quantization",
      "resolved_canonical": "Mixed-Precision Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Shapley-based Progressive Quantization Estimation",
      "resolved_canonical": "Shapley-based Progressive Quantization Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Interaction-aware Mixed-Precision Quantization",
      "resolved_canonical": "Interaction-aware Mixed-Precision Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    }
  ]
}
-->

# IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs

**Korean Title:** IMPQ: 대형 언어 모델(LLM)을 위한 상호작용 인식 계층별 혼합 정밀도 양자화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15455.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15455](https://arxiv.org/abs/2509.15455)

## 🔗 유사한 논문
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (86.3% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.6% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (83.9% similar)
- [[2025-09-22/IGD_ Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation_20250922|IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation]] (83.6% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Mixed-Precision Quantization|Mixed-Precision Quantization]], [[keywords/Shapley-based Progressive Quantization Estimation|Shapley-based Progressive Quantization Estimation]], [[keywords/Interaction-aware Mixed-Precision Quantization|Interaction-aware Mixed-Precision Quantization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15455v1 Announce Type: new 
Abstract: Large Language Models (LLMs) promise impressive capabilities, yet their multi-billion-parameter scale makes on-device or low-resource deployment prohibitive. Mixed-precision quantization offers a compelling solution, but existing methods struggle when the average precision drops below four bits, as they rely on isolated, layer-specific metrics that overlook critical inter-layer interactions affecting overall performance. In this paper, we propose two innovations to address these limitations. First, we frame the mixed-precision quantization problem as a cooperative game among layers and introduce Shapley-based Progressive Quantization Estimation (SPQE) to efficiently obtain accurate Shapley estimates of layer sensitivities and inter-layer interactions. Second, building upon SPQE, we propose Interaction-aware Mixed-Precision Quantization (IMPQ) which translates these Shapley estimates into a binary quadratic optimization formulation, assigning either 2 or 4-bit precision to layers under strict memory constraints. Comprehensive experiments conducted on Llama-3, Gemma-2, and Qwen-3 models across three independent PTQ backends (Quanto, HQQ, GPTQ) demonstrate IMPQ's scalability and consistently superior performance compared to methods relying solely on isolated metrics. Across average precisions spanning 4 bit down to 2 bit, IMPQ cuts Perplexity by 20 to 80 percent relative to the best baseline, with the margin growing as the bit-width tightens.

## 🔍 Abstract (한글 번역)

arXiv:2509.15455v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)은 인상적인 능력을 약속하지만, 수십억 개의 매개변수 규모로 인해 장치 내 또는 저자원 환경에서의 배포가 어렵습니다. 혼합 정밀도 양자화는 매력적인 해결책을 제공하지만, 기존 방법은 평균 정밀도가 4비트 이하로 떨어질 때 어려움을 겪습니다. 이는 개별적이고 계층별 메트릭에 의존하여 전체 성능에 영향을 미치는 중요한 계층 간 상호작용을 간과하기 때문입니다. 본 논문에서는 이러한 제한을 해결하기 위한 두 가지 혁신을 제안합니다. 첫째, 혼합 정밀도 양자화 문제를 계층 간의 협력 게임으로 프레임화하고, 계층 민감도와 계층 간 상호작용에 대한 정확한 샤플리 추정치를 효율적으로 얻기 위해 샤플리 기반 점진적 양자화 추정(SPQE)을 도입합니다. 둘째, SPQE를 기반으로 하여, 이러한 샤플리 추정치를 이진 이차 최적화 공식으로 변환하여 엄격한 메모리 제약 하에 계층에 2비트 또는 4비트 정밀도를 할당하는 상호작용 인식 혼합 정밀도 양자화(IMPQ)를 제안합니다. Llama-3, Gemma-2, Qwen-3 모델에서 세 가지 독립적인 PTQ 백엔드(Quanto, HQQ, GPTQ)를 통해 수행된 포괄적인 실험은 IMPQ의 확장성과 고립된 메트릭에만 의존하는 방법에 비해 일관되게 우수한 성능을 보여줍니다. 평균 정밀도가 4비트에서 2비트로 감소하는 동안, IMPQ는 최상의 기준선에 비해 당혹도를 20%에서 80%까지 줄이며, 비트 폭이 좁아질수록 그 차이는 더욱 커집니다.

## 📝 요약

대형 언어 모델(LLM)의 효율적인 배포를 위해 혼합 정밀도 양자화가 유망하지만, 기존 방법은 평균 정밀도가 4비트 이하로 떨어질 때 성능 저하를 겪습니다. 본 논문에서는 이러한 한계를 극복하기 위해 두 가지 혁신을 제안합니다. 첫째, 혼합 정밀도 양자화 문제를 계층 간 협력 게임으로 보고, Shapley 기반의 점진적 양자화 추정(SPQE)을 도입하여 계층 민감도와 상호작용을 정확히 추정합니다. 둘째, SPQE를 기반으로 상호작용 인식 혼합 정밀도 양자화(IMPQ)를 제안하여, 이를 이진 이차 최적화 문제로 변환하여 메모리 제약 하에 2비트 또는 4비트 정밀도를 할당합니다. Llama-3, Gemma-2, Qwen-3 모델에 대한 실험 결과, IMPQ는 기존 방법보다 우수한 성능을 보이며, 평균 정밀도가 4비트에서 2비트로 줄어들수록 Perplexity를 20%에서 80%까지 감소시켰습니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)의 기기 내 또는 저자원 환경 배포를 위해 혼합 정밀도 양자화가 중요한 해결책으로 제시됩니다.
- 2. 기존 방법들이 평균 정밀도가 4비트 이하로 떨어질 때 성능 저하를 겪는 문제를 해결하기 위해, 본 논문은 Shapley 기반의 점진적 양자화 추정(SPQE)을 도입하여 레이어 민감도와 상호작용을 효율적으로 추정합니다.
- 3. SPQE를 기반으로, 상호작용을 고려한 혼합 정밀도 양자화(IMPQ)를 제안하여, 2비트 또는 4비트 정밀도를 레이어에 할당하는 이진 이차 최적화 문제로 변환합니다.
- 4. 다양한 모델과 PTQ 백엔드에서의 실험 결과, IMPQ는 기존의 고립된 메트릭에 의존하는 방법들보다 일관되게 우수한 성능을 보이며, 비트 폭이 줄어들수록 Perplexity를 20%에서 80%까지 감소시킵니다.


---

*Generated on 2025-09-23 10:25:06*