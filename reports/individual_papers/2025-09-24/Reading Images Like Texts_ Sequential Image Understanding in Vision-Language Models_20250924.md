<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:17:58.474053",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Dual-Stream Hypothesis",
    "Object Recognition",
    "Spatial Perception",
    "RoPE Scaling Technique"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.9,
    "Dual-Stream Hypothesis": 0.75,
    "Object Recognition": 0.85,
    "Spatial Perception": 0.8,
    "RoPE Scaling Technique": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept is central to the paper and connects with recent trends in multimodal learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "dual-stream hypothesis",
        "canonical": "Dual-Stream Hypothesis",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "It provides a theoretical framework for understanding visual processing in VLMs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "object recognition",
        "canonical": "Object Recognition",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "This is a foundational concept in computer vision and relevant to the paper's focus.",
        "novelty_score": 0.3,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "spatial perception",
        "canonical": "Spatial Perception",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "It is a key component of the paper's analysis of VLMs' internal mechanisms.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "RoPE scaling technique",
        "canonical": "RoPE Scaling Technique",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for enhancing spatial reasoning in VLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "instruction-agnostic token compression",
      "plug-and-play visual decoder"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "dual-stream hypothesis",
      "resolved_canonical": "Dual-Stream Hypothesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "object recognition",
      "resolved_canonical": "Object Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "spatial perception",
      "resolved_canonical": "Spatial Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "RoPE scaling technique",
      "resolved_canonical": "RoPE Scaling Technique",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Reading Images Like Texts: Sequential Image Understanding in Vision-Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19191.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19191](https://arxiv.org/abs/2509.19191)

## 🔗 유사한 논문
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (88.2% similar)
- [[2025-09-23/Eye Gaze Tells You Where to Compute_ Gaze-Driven Efficient VLMs_20250923|Eye Gaze Tells You Where to Compute: Gaze-Driven Efficient VLMs]] (87.8% similar)
- [[2025-09-23/SD-VLM_ Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models_20250923|SD-VLM: Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models]] (87.4% similar)
- [[2025-09-24/How Far are VLMs from Visual Spatial Intelligence? A Benchmark-Driven Perspective_20250924|How Far are VLMs from Visual Spatial Intelligence? A Benchmark-Driven Perspective]] (87.2% similar)
- [[2025-09-23/Evo-0_ Vision-Language-Action Model with Implicit Spatial Understanding_20250923|Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding]] (86.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Object Recognition|Object Recognition]]
**⚡ Unique Technical**: [[keywords/Dual-Stream Hypothesis|Dual-Stream Hypothesis]], [[keywords/Spatial Perception|Spatial Perception]], [[keywords/RoPE Scaling Technique|RoPE Scaling Technique]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19191v1 Announce Type: new 
Abstract: Vision-Language Models (VLMs) have demonstrated remarkable performance across a variety of real-world tasks. However, existing VLMs typically process visual information by serializing images, a method that diverges significantly from the parallel nature of human vision. Moreover, their opaque internal mechanisms hinder both deeper understanding and architectural innovation. Inspired by the dual-stream hypothesis of human vision, which distinguishes the "what" and "where" pathways, we deconstruct the visual processing in VLMs into object recognition and spatial perception for separate study. For object recognition, we convert images into text token maps and find that the model's perception of image content unfolds as a two-stage process from shallow to deep layers, beginning with attribute recognition and culminating in semantic disambiguation. For spatial perception, we theoretically derive and empirically verify the geometric structure underlying the positional representation in VLMs. Based on these findings, we introduce an instruction-agnostic token compression algorithm based on a plug-and-play visual decoder to improve decoding efficiency, and a RoPE scaling technique to enhance spatial reasoning. Through rigorous experiments, our work validates these analyses, offering a deeper understanding of VLM internals and providing clear principles for designing more capable future architectures.

## 📝 요약

이 논문은 Vision-Language Models(VLMs)의 시각 정보 처리 방식을 인간의 시각과 유사한 이중 경로 가설을 기반으로 재구성하여 연구합니다. 기존 VLMs는 이미지 정보를 직렬화하여 처리하는데, 이는 인간의 병렬적 시각 처리와 다릅니다. 연구는 VLMs의 시각 처리를 객체 인식과 공간 인식으로 나누어 분석합니다. 객체 인식에서는 이미지를 텍스트 토큰 맵으로 변환하여, 모델이 얕은 층에서 속성 인식을 시작으로 깊은 층에서 의미적 모호성을 해소하는 2단계 과정을 거친다는 것을 발견했습니다. 공간 인식에서는 VLMs의 위치 표현에 내재된 기하학적 구조를 이론적으로 도출하고 실험적으로 검증했습니다. 이 발견을 바탕으로, 디코딩 효율성을 높이는 토큰 압축 알고리즘과 공간 추론을 강화하는 RoPE 스케일링 기법을 제안합니다. 실험을 통해 이러한 분석을 검증하며, VLMs의 내부 메커니즘에 대한 깊은 이해와 향후 더 발전된 아키텍처 설계를 위한 명확한 원칙을 제공합니다.

## 🎯 주요 포인트

- 1. 기존의 Vision-Language Models(VLMs)는 이미지 정보를 직렬화하여 처리하며, 이는 인간의 병렬적 시각 처리 방식과 다르다.
- 2. 인간 시각의 이중 경로 가설에 영감을 받아, VLM의 시각 처리를 객체 인식과 공간 지각으로 분리하여 연구하였다.
- 3. 객체 인식에서는 이미지를 텍스트 토큰 맵으로 변환하여, 모델이 이미지 콘텐츠를 얕은 층에서 깊은 층으로 인식하는 두 단계 과정을 발견하였다.
- 4. 공간 지각에서는 VLM의 위치 표현에 내재된 기하학적 구조를 이론적으로 도출하고 실증적으로 검증하였다.
- 5. 연구 결과를 바탕으로 디코딩 효율성을 높이는 토큰 압축 알고리즘과 공간 추론을 강화하는 RoPE 스케일링 기법을 제안하였다.


---

*Generated on 2025-09-24 16:17:58*