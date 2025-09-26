<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:20:56.247961",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Layout-to-Image Generation",
    "OverLayScore",
    "OverLayBench",
    "CreatiLayout-AM",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Layout-to-Image Generation": 0.85,
    "OverLayScore": 0.88,
    "OverLayBench": 0.92,
    "CreatiLayout-AM": 0.87,
    "Computer Vision": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "layout-to-image generation",
        "canonical": "Layout-to-Image Generation",
        "aliases": [
          "layout image synthesis",
          "layout-based image generation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task in computer vision that connects to layout understanding and image synthesis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "OverLayScore",
        "canonical": "OverLayScore",
        "aliases": [
          "overlap complexity metric"
        ],
        "category": "unique_technical",
        "rationale": "A novel metric introduced in the paper, crucial for evaluating overlap complexity in layout-to-image tasks.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "OverLayBench",
        "canonical": "OverLayBench",
        "aliases": [
          "overlap benchmark"
        ],
        "category": "unique_technical",
        "rationale": "A new benchmark proposed in the paper, essential for assessing models on complex layout scenarios.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.92
      },
      {
        "surface": "CreatiLayout-AM",
        "canonical": "CreatiLayout-AM",
        "aliases": [
          "amodal mask model"
        ],
        "category": "unique_technical",
        "rationale": "A model introduced for improving performance on complex overlaps, linking to amodal perception.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.87
      },
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "The overarching field relevant to layout-to-image generation and the proposed benchmarks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "quality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "layout-to-image generation",
      "resolved_canonical": "Layout-to-Image Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "OverLayScore",
      "resolved_canonical": "OverLayScore",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "OverLayBench",
      "resolved_canonical": "OverLayBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "CreatiLayout-AM",
      "resolved_canonical": "CreatiLayout-AM",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.87
      }
    },
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# OverLayBench: A Benchmark for Layout-to-Image Generation with Dense Overlaps

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19282.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19282](https://arxiv.org/abs/2509.19282)

## 🔗 유사한 논문
- [[2025-09-23/InstanceAssemble_ Layout-Aware Image Generation via Instance Assembling Attention_20250923|InstanceAssemble: Layout-Aware Image Generation via Instance Assembling Attention]] (86.2% similar)
- [[2025-09-23/Introducing Resizable Region Packing Problem in Image Generation, with a Heuristic Solution_20250923|Introducing Resizable Region Packing Problem in Image Generation, with a Heuristic Solution]] (82.9% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (81.9% similar)
- [[2025-09-19/End4_ End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection_20250919|End4: End-to-end Denoising Diffusion for Diffusion-Based Inpainting Detection]] (81.7% similar)
- [[2025-09-22/OptiScene_ LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization_20250922|OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/Layout-to-Image Generation|Layout-to-Image Generation]], [[keywords/OverLayScore|OverLayScore]], [[keywords/OverLayBench|OverLayBench]], [[keywords/CreatiLayout-AM|CreatiLayout-AM]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19282v1 Announce Type: new 
Abstract: Despite steady progress in layout-to-image generation, current methods still struggle with layouts containing significant overlap between bounding boxes. We identify two primary challenges: (1) large overlapping regions and (2) overlapping instances with minimal semantic distinction. Through both qualitative examples and quantitative analysis, we demonstrate how these factors degrade generation quality. To systematically assess this issue, we introduce OverLayScore, a novel metric that quantifies the complexity of overlapping bounding boxes. Our analysis reveals that existing benchmarks are biased toward simpler cases with low OverLayScore values, limiting their effectiveness in evaluating model performance under more challenging conditions. To bridge this gap, we present OverLayBench, a new benchmark featuring high-quality annotations and a balanced distribution across different levels of OverLayScore. As an initial step toward improving performance on complex overlaps, we also propose CreatiLayout-AM, a model fine-tuned on a curated amodal mask dataset. Together, our contributions lay the groundwork for more robust layout-to-image generation under realistic and challenging scenarios. Project link: https://mlpc-ucsd.github.io/OverLayBench.

## 📝 요약

이 논문은 레이아웃에서 이미지 생성 시 경계 상자가 많이 겹치는 경우의 문제를 다룹니다. 주요 기여는 두 가지 도전 과제를 식별한 것입니다: (1) 큰 겹침 영역, (2) 의미적 구분이 적은 겹침 인스턴스. 이를 해결하기 위해 OverLayScore라는 새로운 지표를 도입하여 겹침의 복잡성을 정량화하고, 기존 벤치마크가 단순한 사례에 치우쳐 있음을 밝혔습니다. 이를 보완하기 위해 다양한 OverLayScore 수준을 포함한 OverLayBench라는 새로운 벤치마크를 제안했습니다. 또한, 복잡한 겹침 문제를 개선하기 위한 CreatiLayout-AM 모델을 소개했습니다. 이 연구는 현실적이고 도전적인 시나리오에서 더 강력한 레이아웃-이미지 생성의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 현재의 레이아웃-이미지 생성 방법은 경계 상자 간의 중첩이 큰 경우에 어려움을 겪고 있습니다.
- 2. 중첩된 경계 상자의 복잡성을 정량화하는 새로운 지표인 OverLayScore를 도입했습니다.
- 3. 기존 벤치마크는 OverLayScore 값이 낮은 간단한 사례에 편향되어 있어, 복잡한 조건에서 모델 성능 평가에 한계가 있습니다.
- 4. 다양한 OverLayScore 수준에 걸쳐 균형 잡힌 분포를 가진 새로운 벤치마크인 OverLayBench를 제시했습니다.
- 5. 복잡한 중첩 문제 해결을 위해 CreatiLayout-AM 모델을 제안하고, 이는 큐레이션된 비가시 마스크 데이터셋으로 미세 조정되었습니다.


---

*Generated on 2025-09-24 16:20:56*