<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:08:35.543022",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Geospatial-Temporal Intelligence",
    "Itinerary Reconstruction",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "Geospatial-Temporal Intelligence": 0.78,
    "Itinerary Reconstruction": 0.8,
    "Vision-Language Model": 0.83
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "MLLMs"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader category of language models, enhancing understanding of their application in multimodal contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "Geospatial-Temporal Intelligence",
        "canonical": "Geospatial-Temporal Intelligence",
        "aliases": [
          "Spatial-Temporal Understanding"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the paper's focus on understanding extended spatial and temporal scales.",
        "novelty_score": 0.75,
        "connectivity_score": 0.67,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Travel Video Itinerary Reconstruction",
        "canonical": "Itinerary Reconstruction",
        "aliases": [
          "Travel Itinerary Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's evaluation framework, linking to practical applications in travel planning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents an evolving concept that bridges vision and language processing, relevant to the paper's multimodal focus.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.83
      }
    ],
    "ban_list_suggestions": [
      "video understanding",
      "travel videos",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Geospatial-Temporal Intelligence",
      "resolved_canonical": "Geospatial-Temporal Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.67,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Travel Video Itinerary Reconstruction",
      "resolved_canonical": "Itinerary Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# VIR-Bench: Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19002.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19002](https://arxiv.org/abs/2509.19002)

## 🔗 유사한 논문
- [[2025-09-23/Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?_20250923|Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?]] (84.6% similar)
- [[2025-09-23/From Easy to Hard_ The MIR Benchmark for Progressive Interleaved Multi-Image Reasoning_20250923|From Easy to Hard: The MIR Benchmark for Progressive Interleaved Multi-Image Reasoning]] (84.6% similar)
- [[2025-09-23/InfiniBench_ A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows_20250923|InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows]] (84.3% similar)
- [[2025-09-19/Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (83.6% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Geospatial-Temporal Intelligence|Geospatial-Temporal Intelligence]], [[keywords/Itinerary Reconstruction|Itinerary Reconstruction]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19002v1 Announce Type: cross 
Abstract: Recent advances in multimodal large language models (MLLMs) have significantly enhanced video understanding capabilities, opening new possibilities for practical applications. Yet current video benchmarks focus largely on indoor scenes or short-range outdoor activities, leaving the challenges associated with long-distance travel largely unexplored. Mastering extended geospatial-temporal trajectories is critical for next-generation MLLMs, underpinning real-world tasks such as embodied-AI planning and navigation. To bridge this gap, we present VIR-Bench, a novel benchmark consisting of 200 travel videos that frames itinerary reconstruction as a challenging task designed to evaluate and push forward MLLMs' geospatial-temporal intelligence. Experimental results reveal that state-of-the-art MLLMs, including proprietary ones, struggle to achieve high scores, underscoring the difficulty of handling videos that span extended spatial and temporal scales. Moreover, we conduct an in-depth case study in which we develop a prototype travel-planning agent that leverages the insights gained from VIR-Bench. The agent's markedly improved itinerary recommendations verify that our evaluation protocol not only benchmarks models effectively but also translates into concrete performance gains in user-facing applications.

## 📝 요약

최근 다중 모달 대형 언어 모델(MLLMs)의 발전은 비디오 이해 능력을 크게 향상시켰으나, 현재의 비디오 벤치마크는 주로 실내 장면이나 단거리 야외 활동에 초점을 맞추고 있습니다. 이러한 한계를 극복하고자, 우리는 장거리 여행의 지리적-시간적 경로를 평가할 수 있는 새로운 벤치마크인 VIR-Bench를 제안합니다. 200개의 여행 비디오로 구성된 VIR-Bench는 여정 재구성을 도전 과제로 삼아 MLLMs의 지리적-시간적 지능을 평가합니다. 실험 결과, 최신 MLLMs도 이 과제에서 높은 점수를 얻기 어려움을 보여주었습니다. 또한, VIR-Bench에서 얻은 통찰을 활용해 여행 계획 에이전트를 개발한 사례 연구를 통해, 이 평가 방법이 모델의 성능 향상뿐만 아니라 사용자 애플리케이션에서의 실제 성능 개선으로 이어짐을 확인했습니다.

## 🎯 주요 포인트

- 1. 최근 다중모달 대형 언어 모델(MLLMs)의 발전으로 비디오 이해 능력이 크게 향상되었습니다.
- 2. 기존 비디오 벤치마크는 주로 실내 장면이나 단거리 야외 활동에 집중되어 있어 장거리 여행과 관련된 도전 과제는 거의 탐구되지 않았습니다.
- 3. VIR-Bench는 200개의 여행 비디오로 구성된 새로운 벤치마크로, 일정 재구성을 통해 MLLMs의 지리적-시간적 지능을 평가하고 발전시키기 위한 도전 과제로 설정되었습니다.
- 4. 실험 결과, 최첨단 MLLMs가 확장된 공간 및 시간적 규모를 다루는 데 어려움을 겪고 있음을 보여주었습니다.
- 5. VIR-Bench에서 얻은 통찰력을 활용하여 개발한 여행 계획 에이전트는 일정 추천 성능이 크게 향상되어 사용자 응용 프로그램에서의 구체적인 성능 향상을 입증했습니다.


---

*Generated on 2025-09-24 14:08:35*