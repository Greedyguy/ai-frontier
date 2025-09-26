<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:29:16.142941",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "LightThinker",
    "Attention Mechanism",
    "Dependency Metric"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "LightThinker": 0.85,
    "Attention Mechanism": 0.78,
    "Dependency Metric": 0.82
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's theme and connect to existing research on model efficiency.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "LightThinker",
        "canonical": "LightThinker",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "LightThinker is the novel method proposed in the paper, offering a new approach to LLM efficiency.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Attention Masks",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Masks"
        ],
        "category": "specific_connectable",
        "rationale": "The use of specialized attention masks is a key technique in the paper, linking to broader attention mechanism research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dependency Metric",
        "canonical": "Dependency Metric",
        "aliases": [
          "Dep Metric"
        ],
        "category": "unique_technical",
        "rationale": "The Dependency Metric is introduced as a novel measure to quantify compression, important for understanding model efficiency.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "compression",
      "efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "LightThinker",
      "resolved_canonical": "LightThinker",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Attention Masks",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dependency Metric",
      "resolved_canonical": "Dependency Metric",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# LightThinker: Thinking Step-by-Step Compression

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.15589.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2502.15589](https://arxiv.org/abs/2502.15589)

## 🔗 유사한 논문
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (87.0% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (86.3% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.9% similar)
- [[2025-09-24/CogniLoad_ A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density_20250924|CogniLoad: A Synthetic Natural Language Reasoning Benchmark With Tunable Length, Intrinsic Difficulty, and Distractor Density]] (85.3% similar)
- [[2025-09-23/LightRetriever_ A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference_20250923|LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/LightThinker|LightThinker]], [[keywords/Dependency Metric|Dependency Metric]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.15589v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) have shown remarkable performance in complex reasoning tasks, but their efficiency is hindered by the substantial memory and computational costs associated with generating lengthy tokens. In this paper, we propose LightThinker, a novel method that enables LLMs to dynamically compress intermediate thoughts during reasoning. Inspired by human cognitive processes, LightThinker compresses verbose thought steps into compact representations and discards the original reasoning chains, thereby significantly reducing the number of tokens stored in the context window. This is achieved by training the model on when and how to perform compression through data construction, mapping hidden states to condensed gist tokens, and creating specialized attention masks. Additionally, we introduce the Dependency (Dep) metric to quantify the degree of compression by measuring the reliance on historical tokens during generation. Extensive experiments on four datasets and two models show that LightThinker reduces peak memory usage and inference time, while maintaining competitive accuracy. Our work provides a new direction for improving the efficiency of LLMs in complex reasoning tasks without sacrificing performance. Code is released at https://github.com/zjunlp/LightThinker.

## 📝 요약

이 논문에서는 대형 언어 모델(LLM)의 효율성을 높이기 위해 LightThinker라는 새로운 방법을 제안합니다. LightThinker는 인간의 인지 과정을 본떠 복잡한 추론 과정에서 중간 사고 단계를 압축하여 간결한 표현으로 변환하고, 원래의 추론 체인을 삭제함으로써 메모리와 계산 비용을 줄입니다. 이를 위해 데이터 구축을 통해 언제, 어떻게 압축할지를 학습시키고, 숨겨진 상태를 간결한 요약 토큰으로 매핑하며, 특수한 주의 마스크를 생성합니다. 또한, 생성 과정에서 과거 토큰에 대한 의존도를 측정하는 Dependency(Dep) 지표를 도입하여 압축 정도를 정량화합니다. 네 가지 데이터셋과 두 가지 모델을 대상으로 한 실험 결과, LightThinker는 메모리 사용량과 추론 시간을 줄이면서도 정확도를 유지하는 것으로 나타났습니다. 이 연구는 LLM의 복잡한 추론 작업에서 성능을 저하시키지 않고 효율성을 개선할 수 있는 새로운 방향을 제시합니다. 코드: https://github.com/zjunlp/LightThinker.

## 🎯 주요 포인트

- 1. LightThinker는 LLM의 중간 사고 과정을 동적으로 압축하여 메모리와 계산 비용을 줄이는 새로운 방법을 제안합니다.
- 2. 인간의 인지 과정을 모방하여 장황한 사고 단계를 간결한 표현으로 압축하고 원래의 추론 체인을 버립니다.
- 3. 데이터 구축을 통해 압축 수행 시기와 방법을 학습시키고, 숨겨진 상태를 간결한 요약 토큰으로 매핑하며, 특수한 주의 마스크를 생성합니다.
- 4. 의존성(Dep) 메트릭을 도입하여 생성 중 역사적 토큰에 대한 의존도를 측정함으로써 압축 정도를 정량화합니다.
- 5. 네 개의 데이터셋과 두 개의 모델에 대한 실험 결과, LightThinker는 메모리 사용량과 추론 시간을 줄이면서도 경쟁력 있는 정확도를 유지합니다.


---

*Generated on 2025-09-24 14:29:16*