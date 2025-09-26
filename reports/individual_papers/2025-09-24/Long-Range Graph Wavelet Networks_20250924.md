<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:40:16.776885",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Wavelet Networks",
    "Long-Range Interactions",
    "Spectral-Domain Parameterization",
    "Graph Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Wavelet Networks": 0.8,
    "Long-Range Interactions": 0.75,
    "Spectral-Domain Parameterization": 0.7,
    "Graph Neural Network": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Wavelet Networks",
        "canonical": "Graph Wavelet Networks",
        "aliases": [
          "GWN"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach in graph neural networks by integrating wavelet theory, enhancing long-range information propagation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Long-Range Interactions",
        "canonical": "Long-Range Interactions",
        "aliases": [
          "Long-Range Propagation"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for understanding the paper's focus on improving information flow across distant graph nodes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Spectral-Domain Parameterization",
        "canonical": "Spectral-Domain Parameterization",
        "aliases": [
          "Spectral Parameterization"
        ],
        "category": "unique_technical",
        "rationale": "Describes a method for capturing long-range interactions, crucial for the paper's proposed model.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's context, linking it to broader discussions in graph-based machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
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
      "candidate_surface": "Graph Wavelet Networks",
      "resolved_canonical": "Graph Wavelet Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Long-Range Interactions",
      "resolved_canonical": "Long-Range Interactions",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Spectral-Domain Parameterization",
      "resolved_canonical": "Spectral-Domain Parameterization",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Long-Range Graph Wavelet Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.06743.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.06743](https://arxiv.org/abs/2509.06743)

## 🔗 유사한 논문
- [[2025-09-23/Word2VecGD_ Neural Graph Drawing with Cosine-Stress Optimization_20250923|Word2VecGD: Neural Graph Drawing with Cosine-Stress Optimization]] (83.2% similar)
- [[2025-09-23/ScaleGNN_ Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion_20250923|ScaleGNN: Towards Scalable Graph Neural Networks via Adaptive High-order Neighboring Feature Fusion]] (83.1% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (82.7% similar)
- [[2025-09-22/DiRW_ Path-Aware Digraph Learning for Heterophily_20250922|DiRW: Path-Aware Digraph Learning for Heterophily]] (82.7% similar)
- [[2025-09-23/Wavelet-Space Representations for Neural Super-Resolution in Rendering Pipelines_20250923|Wavelet-Space Representations for Neural Super-Resolution in Rendering Pipelines]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Graph Wavelet Networks|Graph Wavelet Networks]], [[keywords/Long-Range Interactions|Long-Range Interactions]], [[keywords/Spectral-Domain Parameterization|Spectral-Domain Parameterization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06743v2 Announce Type: replace-cross 
Abstract: Modeling long-range interactions, the propagation of information across distant parts of a graph, is a central challenge in graph machine learning. Graph wavelets, inspired by multi-resolution signal processing, provide a principled way to capture both local and global structures. However, existing wavelet-based graph neural networks rely on finite-order polynomial approximations, which limit their receptive fields and hinder long-range propagation. We propose Long-Range Graph Wavelet Networks (LR-GWN), which decompose wavelet filters into complementary local and global components. Local aggregation is handled with efficient low-order polynomials, while long-range interactions are captured through a flexible spectral-domain parameterization. This hybrid design unifies short- and long-distance information flow within a principled wavelet framework. Experiments show that LR-GWN achieves state-of-the-art performance among wavelet-based methods on long-range benchmarks, while remaining competitive on short-range datasets.

## 📝 요약

이 논문은 그래프 머신러닝에서 장거리 상호작용을 효과적으로 모델링하기 위한 새로운 방법론을 제안합니다. 기존의 웨이블릿 기반 그래프 신경망은 유한 차수 다항식 근사에 의존하여 수용 범위가 제한적이었으나, 제안된 Long-Range Graph Wavelet Networks(LR-GWN)는 웨이블릿 필터를 지역 및 전역 구성 요소로 분해하여 이를 극복합니다. 지역 집계는 저차 다항식으로 처리하고, 장거리 상호작용은 유연한 스펙트럼 도메인 매개변수화를 통해 포착합니다. 이 하이브리드 설계는 단거리와 장거리 정보 흐름을 통합하며, 실험 결과 장거리 벤치마크에서 최첨단 성능을 달성하고 단거리 데이터셋에서도 경쟁력을 유지함을 보여줍니다.

## 🎯 주요 포인트

- 1. 그래프 머신 러닝에서 장거리 상호작용 모델링은 중요한 도전 과제입니다.
- 2. 기존의 웨이블릿 기반 그래프 신경망은 유한 차수 다항식 근사에 의존하여 수용 범위가 제한됩니다.
- 3. LR-GWN은 웨이블릿 필터를 지역 및 글로벌 구성 요소로 분해하여 장거리 상호작용을 효과적으로 캡처합니다.
- 4. 실험 결과, LR-GWN은 장거리 벤치마크에서 최첨단 성능을 달성하며, 단거리 데이터셋에서도 경쟁력을 유지합니다.
- 5. 이 하이브리드 설계는 웨이블릿 프레임워크 내에서 단거리 및 장거리 정보 흐름을 통합합니다.


---

*Generated on 2025-09-24 14:40:16*