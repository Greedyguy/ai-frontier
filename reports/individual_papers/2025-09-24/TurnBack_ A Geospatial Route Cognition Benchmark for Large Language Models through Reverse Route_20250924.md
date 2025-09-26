<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:49:41.665443",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Geospatial Cognition",
    "PathBuilder Tool",
    "Route Reversal Task"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Geospatial Cognition": 0.78,
    "PathBuilder Tool": 0.7,
    "Route Reversal Task": 0.72
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
        "rationale": "Central to the study, providing a basis for linking to other language model research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "geospatial route cognition",
        "canonical": "Geospatial Cognition",
        "aliases": [
          "geospatial route cognition",
          "spatial cognition"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the paper, offering a unique angle on cognitive capabilities of models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "PathBuilder",
        "canonical": "PathBuilder Tool",
        "aliases": [
          "PathBuilder",
          "route conversion tool"
        ],
        "category": "unique_technical",
        "rationale": "A novel tool introduced in the paper, crucial for understanding the methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "route reversal",
        "canonical": "Route Reversal Task",
        "aliases": [
          "reverse route task",
          "route reversal"
        ],
        "category": "unique_technical",
        "rationale": "Specific task evaluated in the study, important for linking to related cognitive challenges.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "evaluation framework",
      "state-of-the-art",
      "metropolises"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "geospatial route cognition",
      "resolved_canonical": "Geospatial Cognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "PathBuilder",
      "resolved_canonical": "PathBuilder Tool",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "route reversal",
      "resolved_canonical": "Route Reversal Task",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# TurnBack: A Geospatial Route Cognition Benchmark for Large Language Models through Reverse Route

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18173.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18173](https://arxiv.org/abs/2509.18173)

## 🔗 유사한 논문
- [[2025-09-23/TurnaboutLLM_ A Deductive Reasoning Benchmark from Detective Games_20250923|TurnaboutLLM: A Deductive Reasoning Benchmark from Detective Games]] (85.1% similar)
- [[2025-09-23/LLMsPark_ A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts_20250923|LLMsPark: A Benchmark for Evaluating Large Language Models in Strategic Gaming Contexts]] (84.9% similar)
- [[2025-09-24/VIR-Bench_ Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction_20250924|VIR-Bench: Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction]] (84.6% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (83.9% similar)
- [[2025-09-24/AECBench_ A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field_20250924|AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Geospatial Cognition|Geospatial Cognition]], [[keywords/PathBuilder Tool|PathBuilder Tool]], [[keywords/Route Reversal Task|Route Reversal Task]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18173v1 Announce Type: new 
Abstract: Humans can interpret geospatial information through natural language, while the geospatial cognition capabilities of Large Language Models (LLMs) remain underexplored. Prior research in this domain has been constrained by non-quantifiable metrics, limited evaluation datasets and unclear research hierarchies. Therefore, we propose a large-scale benchmark and conduct a comprehensive evaluation of the geospatial route cognition of LLMs. We create a large-scale evaluation dataset comprised of 36000 routes from 12 metropolises worldwide. Then, we introduce PathBuilder, a novel tool for converting natural language instructions into navigation routes, and vice versa, bridging the gap between geospatial information and natural language. Finally, we propose a new evaluation framework and metrics to rigorously assess 11 state-of-the-art (SOTA) LLMs on the task of route reversal. The benchmark reveals that LLMs exhibit limitation to reverse routes: most reverse routes neither return to the starting point nor are similar to the optimal route. Additionally, LLMs face challenges such as low robustness in route generation and high confidence for their incorrect answers. Code\ \&\ Data available here: \href{https://github.com/bghjmn32/EMNLP2025_Turnback}{TurnBack.}

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 지리적 인지 능력을 평가하기 위한 새로운 벤치마크를 제안합니다. 연구는 12개 대도시에서 수집한 36,000개의 경로 데이터를 활용하여 LLM의 경로 인지 능력을 평가합니다. 이를 위해 자연어 지시를 경로로 변환하는 도구인 PathBuilder를 소개하고, 경로 반전 작업에서 11개의 최신 LLM을 평가하는 새로운 프레임워크와 지표를 제안합니다. 연구 결과, LLM은 경로 반전에서 한계가 있으며, 생성된 경로의 강건성이 낮고 잘못된 답변에 높은 확신을 보이는 문제를 드러냅니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLMs)의 지리적 경로 인식 능력을 평가하기 위한 대규모 벤치마크와 평가 프레임워크를 제안하였습니다.
- 2. 12개 대도시에서 36,000개의 경로로 구성된 대규모 평가 데이터셋을 생성하였습니다.
- 3. 자연어 지침을 내비게이션 경로로 변환하는 도구인 PathBuilder를 소개하여 지리적 정보와 자연어 간의 격차를 해소하였습니다.
- 4. 최신 LLM 11개를 대상으로 경로 역전 작업을 평가한 결과, 대부분의 모델이 경로를 올바르게 역전하지 못하고 시작점으로 돌아가지 못하는 한계를 보였습니다.
- 5. LLMs는 경로 생성에서 낮은 견고성과 잘못된 답변에 대한 높은 확신과 같은 문제에 직면하고 있습니다.


---

*Generated on 2025-09-24 14:49:41*