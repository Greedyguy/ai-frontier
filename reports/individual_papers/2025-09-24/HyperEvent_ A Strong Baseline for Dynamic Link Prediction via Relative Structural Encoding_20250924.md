<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:26:33.800854",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Dynamic Link Prediction",
    "Relative Structural Encoding",
    "Event Sequences"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Dynamic Link Prediction": 0.9,
    "Relative Structural Encoding": 0.7,
    "Event Sequences": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a fundamental model architecture used in various machine learning tasks, including dynamic link prediction.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "dynamic link prediction",
        "canonical": "Dynamic Link Prediction",
        "aliases": [
          "temporal link prediction"
        ],
        "category": "unique_technical",
        "rationale": "Dynamic link prediction is a specific task in graph analysis that focuses on predicting future connections in time-evolving networks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "relative structural encoding",
        "canonical": "Relative Structural Encoding",
        "aliases": [
          "structural encoding"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the proposed method, providing a novel way to capture structural patterns in dynamic graphs.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "event sequences",
        "canonical": "Event Sequences",
        "aliases": [
          "event patterns"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding event sequences is crucial for modeling temporal dynamics in graphs, linking to broader temporal analysis methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "baseline",
      "simple approach",
      "multiple benchmarks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "dynamic link prediction",
      "resolved_canonical": "Dynamic Link Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "relative structural encoding",
      "resolved_canonical": "Relative Structural Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "event sequences",
      "resolved_canonical": "Event Sequences",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# HyperEvent: A Strong Baseline for Dynamic Link Prediction via Relative Structural Encoding

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.11836.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2507.11836](https://arxiv.org/abs/2507.11836)

## 🔗 유사한 논문
- [[2025-09-23/PASS_ Path-selective State Space Model for Event-based Recognition_20250923|PASS: Path-selective State Space Model for Event-based Recognition]] (81.6% similar)
- [[2025-09-24/EventVL_ Understand Event Streams via Multimodal Large Language Model_20250924|EventVL: Understand Event Streams via Multimodal Large Language Model]] (80.9% similar)
- [[2025-09-23/Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning_20250923|Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning]] (80.3% similar)
- [[2025-09-24/HyperNAS_ Enhancing Architecture Representation for NAS Predictor via Hypernetwork_20250924|HyperNAS: Enhancing Architecture Representation for NAS Predictor via Hypernetwork]] (80.2% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Event Sequences|Event Sequences]]
**⚡ Unique Technical**: [[keywords/Dynamic Link Prediction|Dynamic Link Prediction]], [[keywords/Relative Structural Encoding|Relative Structural Encoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.11836v2 Announce Type: replace 
Abstract: Learning representations for continuous-time dynamic graphs is critical for dynamic link prediction. While recent methods have become increasingly complex, the field lacks a strong and informative baseline to reliably gauge progress. This paper proposes HyperEvent, a simple approach that captures relative structural patterns in event sequences through an intuitive encoding mechanism. As a straightforward baseline, HyperEvent leverages relative structural encoding to identify meaningful event sequences without complex parameterization. By combining these interpretable features with a lightweight transformer classifier, HyperEvent reframes link prediction as event structure recognition. Despite its simplicity, HyperEvent achieves competitive results across multiple benchmarks, often matching the performance of more complex models. This work demonstrates that effective modeling can be achieved through simple structural encoding, providing a clear reference point for evaluating future advancements.

## 📝 요약

이 논문은 연속적인 시간의 동적 그래프에서 링크 예측을 위한 단순하면서도 효과적인 방법인 HyperEvent를 제안합니다. HyperEvent는 이벤트 시퀀스의 상대적 구조 패턴을 직관적인 인코딩 메커니즘을 통해 포착하며, 복잡한 매개변수 없이 의미 있는 이벤트 시퀀스를 식별합니다. 이 방법은 해석 가능한 특징을 경량 트랜스포머 분류기와 결합하여 링크 예측을 이벤트 구조 인식으로 재구성합니다. HyperEvent는 단순함에도 불구하고 여러 벤치마크에서 복잡한 모델과 유사한 성능을 보여주며, 향후 발전 평가를 위한 명확한 기준점을 제공합니다.

## 🎯 주요 포인트

- 1. HyperEvent는 이벤트 시퀀스의 상대적 구조 패턴을 포착하는 직관적인 인코딩 메커니즘을 제안합니다.
- 2. HyperEvent는 복잡한 매개변수화 없이 의미 있는 이벤트 시퀀스를 식별하기 위해 상대적 구조 인코딩을 활용합니다.
- 3. 간단한 구조적 인코딩을 통해 효과적인 모델링이 가능하며, 이는 미래 발전 평가를 위한 명확한 기준점을 제공합니다.
- 4. HyperEvent는 가벼운 트랜스포머 분류기를 결합하여 링크 예측을 이벤트 구조 인식으로 재구성합니다.
- 5. HyperEvent는 여러 벤치마크에서 경쟁력 있는 결과를 달성하며, 종종 더 복잡한 모델의 성능과 일치합니다.


---

*Generated on 2025-09-24 15:26:33*