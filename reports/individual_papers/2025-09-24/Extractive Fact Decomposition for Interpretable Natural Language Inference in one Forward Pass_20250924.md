<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:43:30.040802",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Natural Language Processing",
    "atomic fact decomposition",
    "encoder-only architecture",
    "synthetic rationales"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Natural Language Processing": 0.85,
    "atomic fact decomposition": 0.7,
    "encoder-only architecture": 0.72,
    "synthetic rationales": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Natural Language Inference",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLI"
        ],
        "category": "broad_technical",
        "rationale": "Natural Language Inference is a key task within Natural Language Processing, facilitating strong connections to broader NLP concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "atomic fact decomposition",
        "canonical": "atomic fact decomposition",
        "aliases": [
          "fact decomposition"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method specific to the paper, enhancing interpretability in NLI tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "encoder-only architecture",
        "canonical": "encoder-only architecture",
        "aliases": [
          "encoder architecture"
        ],
        "category": "unique_technical",
        "rationale": "The use of encoder-only architecture is a distinct approach in the context of NLI, differing from typical generative models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "synthetic rationales",
        "canonical": "synthetic rationales",
        "aliases": [
          "generated rationales"
        ],
        "category": "unique_technical",
        "rationale": "Synthetic rationales are a unique aspect of the paper's methodology, aiding in model training and interpretability.",
        "novelty_score": 0.68,
        "connectivity_score": 0.58,
        "specificity_score": 0.75,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Natural Language Inference",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "atomic fact decomposition",
      "resolved_canonical": "atomic fact decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "encoder-only architecture",
      "resolved_canonical": "encoder-only architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "synthetic rationales",
      "resolved_canonical": "synthetic rationales",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.58,
        "specificity": 0.75,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Extractive Fact Decomposition for Interpretable Natural Language Inference in one Forward Pass

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18901.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18901](https://arxiv.org/abs/2509.18901)

## 🔗 유사한 논문
- [[2025-09-23/Robust Native Language Identification through Agentic Decomposition_20250923|Robust Native Language Identification through Agentic Decomposition]] (82.6% similar)
- [[2025-09-24/Automatic coherence-driven inference on arguments_20250924|Automatic coherence-driven inference on arguments]] (81.8% similar)
- [[2025-09-24/CogniLoad_ A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density_20250924|CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density]] (81.1% similar)
- [[2025-09-24/LightThinker_ Thinking Step-by-Step Compression_20250924|LightThinker: Thinking Step-by-Step Compression]] (81.1% similar)
- [[2025-09-24/Anecdoctoring_ Automated Red-Teaming Across Language and Place_20250924|Anecdoctoring: Automated Red-Teaming Across Language and Place]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/atomic fact decomposition|atomic fact decomposition]], [[keywords/encoder-only architecture|encoder-only architecture]], [[keywords/synthetic rationales|synthetic rationales]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18901v1 Announce Type: new 
Abstract: Recent works in Natural Language Inference (NLI) and related tasks, such as automated fact-checking, employ atomic fact decomposition to enhance interpretability and robustness. For this, existing methods rely on resource-intensive generative large language models (LLMs) to perform decomposition. We propose JEDI, an encoder-only architecture that jointly performs extractive atomic fact decomposition and interpretable inference without requiring generative models during inference. To facilitate training, we produce a large corpus of synthetic rationales covering multiple NLI benchmarks. Experimental results demonstrate that JEDI achieves competitive accuracy in distribution and significantly improves robustness out of distribution and in adversarial settings over models based solely on extractive rationale supervision. Our findings show that interpretability and robust generalization in NLI can be realized using encoder-only architectures and synthetic rationales. Code and data available at https://jedi.nicpopovic.com

## 📝 요약

최근 자연어 추론(NLI) 및 관련 작업에서 해석 가능성과 강건성을 높이기 위해 원자적 사실 분해가 사용됩니다. 기존 방법은 자원 집약적인 생성형 대형 언어 모델(LLM)에 의존하지만, 우리는 JEDI라는 인코더 전용 아키텍처를 제안합니다. JEDI는 생성 모델 없이 추론 시 추출적 원자 사실 분해와 해석 가능한 추론을 동시에 수행합니다. 훈련을 위해 다양한 NLI 벤치마크를 포함하는 대규모 합성 근거 코퍼스를 생성했습니다. 실험 결과, JEDI는 분포 내에서 경쟁력 있는 정확성을 보이며, 분포 외 및 적대적 환경에서 기존 추출적 근거 감독 모델보다 강건성을 크게 향상시켰습니다. 우리의 연구는 인코더 전용 아키텍처와 합성 근거를 통해 NLI에서 해석 가능성과 강건한 일반화가 가능함을 보여줍니다. 코드와 데이터는 https://jedi.nicpopovic.com에서 제공됩니다.

## 🎯 주요 포인트

- 1. JEDI는 생성 모델 없이 추출적 원자 사실 분해와 해석 가능한 추론을 동시에 수행하는 인코더 전용 아키텍처입니다.
- 2. JEDI는 여러 NLI 벤치마크를 포함하는 대규모 합성 근거 코퍼스를 활용하여 훈련됩니다.
- 3. 실험 결과, JEDI는 분포 내에서 경쟁력 있는 정확성을 달성하며, 분포 밖 및 적대적 환경에서의 견고성을 크게 향상시킵니다.
- 4. 인코더 전용 아키텍처와 합성 근거를 사용하여 NLI에서 해석 가능성과 견고한 일반화가 가능함을 보여줍니다.


---

*Generated on 2025-09-24 15:43:30*