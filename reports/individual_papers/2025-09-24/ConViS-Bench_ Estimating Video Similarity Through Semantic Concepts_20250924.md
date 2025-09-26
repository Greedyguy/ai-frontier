<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:19:59.590412",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Concept-based Video Similarity",
    "Concept-conditioned Video Retrieval",
    "Semantic Concepts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Concept-based Video Similarity": 0.78,
    "Concept-conditioned Video Retrieval": 0.72,
    "Semantic Concepts": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Multimodal Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "LMMs"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to recent advancements in integrating multiple data types for enhanced video understanding.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Concept-based Video Similarity",
        "canonical": "Concept-based Video Similarity",
        "aliases": [
          "ConViS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to video similarity, emphasizing semantic concepts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "concept-conditioned video retrieval",
        "canonical": "Concept-conditioned Video Retrieval",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a new application enabled by the ConViS framework, enhancing retrieval tasks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.77,
        "link_intent_score": 0.72
      },
      {
        "surface": "semantic concepts",
        "canonical": "Semantic Concepts",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Core to understanding and comparing video content at a conceptual level.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "video similarity",
      "benchmark",
      "state-of-the-art models"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Multimodal Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Concept-based Video Similarity",
      "resolved_canonical": "Concept-based Video Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "concept-conditioned video retrieval",
      "resolved_canonical": "Concept-conditioned Video Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.77,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "semantic concepts",
      "resolved_canonical": "Semantic Concepts",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# ConViS-Bench: Estimating Video Similarity Through Semantic Concepts

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19245.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19245](https://arxiv.org/abs/2509.19245)

## 🔗 유사한 논문
- [[2025-09-24/3rd Place Report of LSVOS 2025 MeViS Track_ Sa2VA-i_ Improving Sa2VA Results with Consistent Training and Inference_20250924|3rd Place Report of LSVOS 2025 MeViS Track: Sa2VA-i: Improving Sa2VA Results with Consistent Training and Inference]] (83.6% similar)
- [[2025-09-23/InfiniBench_ A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows_20250923|InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows]] (82.9% similar)
- [[2025-09-24/VIR-Bench_ Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction_20250924|VIR-Bench: Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction]] (81.7% similar)
- [[2025-09-24/VLDBench Evaluating Multimodal Disinformation with Regulatory Alignment_20250924|VLDBench Evaluating Multimodal Disinformation with Regulatory Alignment]] (81.7% similar)
- [[2025-09-23/Advancing Reference-free Evaluation of Video Captions with Factual Analysis_20250923|Advancing Reference-free Evaluation of Video Captions with Factual Analysis]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Semantic Concepts|Semantic Concepts]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Concept-based Video Similarity|Concept-based Video Similarity]], [[keywords/Concept-conditioned Video Retrieval|Concept-conditioned Video Retrieval]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19245v1 Announce Type: new 
Abstract: What does it mean for two videos to be similar? Videos may appear similar when judged by the actions they depict, yet entirely different if evaluated based on the locations where they were filmed. While humans naturally compare videos by taking different aspects into account, this ability has not been thoroughly studied and presents a challenge for models that often depend on broad global similarity scores. Large Multimodal Models (LMMs) with video understanding capabilities open new opportunities for leveraging natural language in comparative video tasks. We introduce Concept-based Video Similarity estimation (ConViS), a novel task that compares pairs of videos by computing interpretable similarity scores across a predefined set of key semantic concepts. ConViS allows for human-like reasoning about video similarity and enables new applications such as concept-conditioned video retrieval. To support this task, we also introduce ConViS-Bench, a new benchmark comprising carefully annotated video pairs spanning multiple domains. Each pair comes with concept-level similarity scores and textual descriptions of both differences and similarities. Additionally, we benchmark several state-of-the-art models on ConViS, providing insights into their alignment with human judgments. Our results reveal significant performance differences on ConViS, indicating that some concepts present greater challenges for estimating video similarity. We believe that ConViS-Bench will serve as a valuable resource for advancing research in language-driven video understanding.

## 📝 요약

이 논문은 비디오 유사성을 평가하는 새로운 방법론인 개념 기반 비디오 유사성 추정(ConViS)을 소개합니다. ConViS는 사전 정의된 주요 개념을 기준으로 비디오 쌍의 유사성을 해석 가능한 점수로 계산하여 인간과 유사한 방식으로 비디오 유사성을 평가할 수 있게 합니다. 이를 통해 개념 조건부 비디오 검색과 같은 새로운 응용 프로그램이 가능해집니다. 또한, 다양한 도메인의 비디오 쌍을 포함하는 새로운 벤치마크인 ConViS-Bench를 제안하여, 각 쌍에 대해 개념 수준의 유사성 점수와 차이점 및 유사점에 대한 텍스트 설명을 제공합니다. 여러 최신 모델을 ConViS에서 벤치마크한 결과, 일부 개념이 비디오 유사성 추정에 더 큰 도전 과제를 제시함을 발견했습니다. ConViS-Bench는 언어 기반 비디오 이해 연구를 발전시키는 데 중요한 자원이 될 것입니다.

## 🎯 주요 포인트

- 1. ConViS는 사전 정의된 주요 개념을 기반으로 해석 가능한 유사성 점수를 계산하여 비디오 쌍을 비교하는 새로운 작업입니다.
- 2. ConViS-Bench는 여러 도메인에 걸쳐 신중하게 주석이 달린 비디오 쌍을 포함하는 새로운 벤치마크로, 개념 수준의 유사성 점수와 차이점 및 유사성에 대한 텍스트 설명을 제공합니다.
- 3. ConViS는 인간과 유사한 비디오 유사성 추론을 가능하게 하며, 개념 조건부 비디오 검색과 같은 새로운 응용 프로그램을 지원합니다.
- 4. ConViS-Bench는 언어 기반 비디오 이해 연구를 발전시키기 위한 귀중한 자원으로 활용될 것입니다.
- 5. ConViS에 대한 여러 최신 모델의 벤치마크 결과는 비디오 유사성 추정에 있어 일부 개념이 더 큰 도전 과제를 제시함을 나타냅니다.


---

*Generated on 2025-09-24 16:19:59*