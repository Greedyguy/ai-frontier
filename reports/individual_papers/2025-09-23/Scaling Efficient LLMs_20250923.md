---
keywords:
  - Recurrent Transformers
  - AI Scaling Law
  - Kullback-Leibler Divergence
  - Efficient Large Language Models
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2402.14746
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:54:52.665718",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Recurrent Transformers",
    "AI Scaling Law",
    "Kullback-Leibler Divergence",
    "Efficient Large Language Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Recurrent Transformers": 0.78,
    "AI Scaling Law": 0.77,
    "Kullback-Leibler Divergence": 0.81,
    "Efficient Large Language Models": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "recurrent transformers",
        "canonical": "Recurrent Transformers",
        "aliases": [
          "recurrent transformer",
          "recurrent transformer networks"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel architecture combining transformers and recurrent networks, enhancing efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "AI scaling law",
        "canonical": "AI Scaling Law",
        "aliases": [
          "scaling law for AI",
          "transformer scaling law"
        ],
        "category": "specific_connectable",
        "rationale": "Describes a fundamental principle affecting the design and efficiency of large language models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Kullback-Liebler divergence",
        "canonical": "Kullback-Leibler Divergence",
        "aliases": [
          "KL divergence"
        ],
        "category": "specific_connectable",
        "rationale": "A key statistical measure used in the paper to derive efficiency metrics for LLMs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "efficient LLMs",
        "canonical": "Efficient Large Language Models",
        "aliases": [
          "efficient LLM",
          "optimized LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Focuses on optimizing large language models for parameter efficiency and performance.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "transformer architecture",
      "training corpus"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "recurrent transformers",
      "resolved_canonical": "Recurrent Transformers",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "AI scaling law",
      "resolved_canonical": "AI Scaling Law",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Kullback-Liebler divergence",
      "resolved_canonical": "Kullback-Leibler Divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "efficient LLMs",
      "resolved_canonical": "Efficient Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Scaling Efficient LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2402.14746.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2402.14746](https://arxiv.org/abs/2402.14746)

## 🔗 유사한 논문
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (86.5% similar)
- [[2025-09-22/Hierarchical Self-Attention_ Generalizing Neural Attention Mechanics to Multi-Scale Problems_20250922|Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems]] (85.0% similar)
- [[2025-09-23/Conv-like Scale-Fusion Time Series Transformer_ A Multi-Scale Representation for Variable-Length Long Time Series_20250923|Conv-like Scale-Fusion Time Series Transformer: A Multi-Scale Representation for Variable-Length Long Time Series]] (84.0% similar)
- [[2025-09-23/Pre-Trained CNN Architecture for Transformer-Based Image Caption Generation Model_20250923|Pre-Trained CNN Architecture for Transformer-Based Image Caption Generation Model]] (83.7% similar)
- [[2025-09-23/How Large Language Models are Designed to Hallucinate_20250923|How Large Language Models are Designed to Hallucinate]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Efficient Large Language Models|Efficient Large Language Models]]
**🔗 Specific Connectable**: [[keywords/AI Scaling Law|AI Scaling Law]], [[keywords/Kullback-Leibler Divergence|Kullback-Leibler Divergence]]
**⚡ Unique Technical**: [[keywords/Recurrent Transformers|Recurrent Transformers]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2402.14746v4 Announce Type: replace-cross 
Abstract: Trained LLMs in the transformer architecture are typically sparse in that most of the parameters are negligible, raising questions on efficiency. Furthermore, the so called "AI scaling law" for transformers suggests that the number of parameters must scale linearly with the size of the data. In response, we inquire into efficient LLMs, i.e. those with the fewest parameters that achieve the desired accuracy on a training corpus. Specifically, by comparing theoretical and empirical estimates of the Kullback-Liebler divergence, we derive a natural AI scaling law that the number of parameters in an efficient LLM scales as $D^{\gamma}$ where $D$ is the size of the training data and $ \gamma \in [0.44, 0.72]$, suggesting the existence of more efficient architectures. Against this backdrop, we propose recurrent transformers, combining the efficacy of transformers with the efficiency of recurrent networks, progressively applying a single transformer layer to a fixed-width sliding window across the input sequence. Recurrent transformers (a) run in linear time in the sequence length, (b) are memory-efficient and amenable to parallel processing in large batches, (c) learn to forget history for language tasks, or accumulate history for long range tasks like copy and selective copy, and (d) are amenable to curriculum training to overcome vanishing gradients. In our experiments, we find that recurrent transformers perform favorably on benchmark tests.

## 📝 요약

이 논문은 효율적인 대형 언어 모델(LLM)의 설계에 대해 연구합니다. 기존의 트랜스포머 구조는 대부분의 매개변수가 중요하지 않아 비효율적이며, AI 스케일링 법칙에 따르면 매개변수 수는 데이터 크기에 비례해야 합니다. 저자들은 효율적인 LLM의 매개변수 수가 데이터 크기 $D$에 대해 $D^{\gamma}$로 스케일링된다는 법칙을 제안하며, $\gamma$는 [0.44, 0.72] 범위에 속합니다. 이를 바탕으로, 트랜스포머와 순환 신경망의 장점을 결합한 '순환 트랜스포머'를 제안합니다. 이 모델은 입력 시퀀스를 슬라이딩 윈도우 방식으로 처리하여 선형 시간 복잡도를 가지며, 메모리 효율적이고 병렬 처리에 적합합니다. 실험 결과, 순환 트랜스포머는 벤치마크 테스트에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 트랜스포머 구조의 LLM은 대부분의 매개변수가 미미하여 효율성에 대한 의문을 제기합니다.
- 2. 효율적인 LLM은 훈련 데이터 크기에 따라 매개변수가 $D^{\gamma}$로 스케일링되며, $\gamma$는 [0.44, 0.72] 범위에 있습니다.
- 3. 반복 트랜스포머는 트랜스포머의 효과와 순환 네트워크의 효율성을 결합하여 입력 시퀀스에 고정 폭 슬라이딩 윈도우를 적용합니다.
- 4. 반복 트랜스포머는 시퀀스 길이에 대해 선형 시간에 실행되며, 메모리 효율적이고 대량 병렬 처리가 가능합니다.
- 5. 반복 트랜스포머는 벤치마크 테스트에서 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 02:54:52*