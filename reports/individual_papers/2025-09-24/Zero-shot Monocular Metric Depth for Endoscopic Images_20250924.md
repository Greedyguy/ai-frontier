<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:05:10.543473",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Transformer",
    "EndoSynth Dataset",
    "Monocular Depth Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.78,
    "Transformer": 0.82,
    "EndoSynth Dataset": 0.8,
    "Monocular Depth Estimation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-shot",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is crucial for understanding the model's ability to generalize to unseen data, which is a key aspect of the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer based networks",
        "canonical": "Transformer",
        "aliases": [
          "Transformer networks"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are foundational to the depth estimation models discussed, linking to broader advancements in machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "EndoSynth dataset",
        "canonical": "EndoSynth Dataset",
        "aliases": [
          "EndoSynth"
        ],
        "category": "unique_technical",
        "rationale": "The EndoSynth dataset is a novel contribution of the paper, providing a unique resource for future research in endoscopic image analysis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Monocular metric depth estimation",
        "canonical": "Monocular Depth Estimation",
        "aliases": [
          "Monocular metric depth"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific focus of the paper, addressing a niche area within computer vision that is essential for the study's context.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "depth estimation models",
      "synthetic dataset",
      "real data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-shot",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer based networks",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "EndoSynth dataset",
      "resolved_canonical": "EndoSynth Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Monocular metric depth estimation",
      "resolved_canonical": "Monocular Depth Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Zero-shot Monocular Metric Depth for Endoscopic Images

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18642.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18642](https://arxiv.org/abs/2509.18642)

## 🔗 유사한 논문
- [[2025-09-22/Towards Sharper Object Boundaries in Self-Supervised Depth Estimation_20250922|Towards Sharper Object Boundaries in Self-Supervised Depth Estimation]] (84.3% similar)
- [[2025-09-23/BaseBoostDepth_ Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation_20250923|BaseBoostDepth: Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation]] (84.1% similar)
- [[2025-09-23/Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views_20250923|Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views]] (84.1% similar)
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (83.4% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/EndoSynth Dataset|EndoSynth Dataset]], [[keywords/Monocular Depth Estimation|Monocular Depth Estimation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18642v1 Announce Type: new 
Abstract: Monocular relative and metric depth estimation has seen a tremendous boost in the last few years due to the sharp advancements in foundation models and in particular transformer based networks. As we start to see applications to the domain of endoscopic images, there is still a lack of robust benchmarks and high-quality datasets in that area. This paper addresses these limitations by presenting a comprehensive benchmark of state-of-the-art (metric and relative) depth estimation models evaluated on real, unseen endoscopic images, providing critical insights into their generalisation and performance in clinical scenarios. Additionally, we introduce and publish a novel synthetic dataset (EndoSynth) of endoscopic surgical instruments paired with ground truth metric depth and segmentation masks, designed to bridge the gap between synthetic and real-world data. We demonstrate that fine-tuning depth foundation models using our synthetic dataset boosts accuracy on most unseen real data by a significant margin. By providing both a benchmark and a synthetic dataset, this work advances the field of depth estimation for endoscopic images and serves as an important resource for future research. Project page, EndoSynth dataset and trained weights are available at https://github.com/TouchSurgery/EndoSynth.

## 📝 요약

이 논문은 내시경 이미지에서의 단안 상대 및 절대 깊이 추정의 한계를 극복하기 위해, 최신 모델들을 실제 내시경 이미지에서 평가한 포괄적인 벤치마크를 제시합니다. 또한, 새로운 합성 데이터셋인 EndoSynth를 소개하여, 내시경 수술 도구의 깊이 및 분할 마스크 정보를 제공합니다. 이 데이터셋을 활용한 모델 미세 조정은 실제 데이터에서의 정확도를 크게 향상시킵니다. 이 연구는 내시경 이미지 깊이 추정 분야를 발전시키고, 향후 연구에 중요한 자원을 제공합니다.

## 🎯 주요 포인트

- 1. 최근 몇 년간 단안 상대 및 절대 깊이 추정은 기초 모델과 특히 트랜스포머 기반 네트워크의 발전으로 인해 큰 발전을 이루었다.
- 2. 내시경 이미지 분야에서는 아직 견고한 벤치마크와 고품질 데이터셋이 부족하다.
- 3. 본 논문은 실제 보지 못한 내시경 이미지에서 최첨단 깊이 추정 모델을 평가하여 임상 시나리오에서의 일반화 및 성능에 대한 중요한 통찰을 제공한다.
- 4. 새로운 합성 데이터셋인 EndoSynth를 도입하여 합성 및 실제 데이터 간의 격차를 줄이고, 이를 통해 대부분의 보지 못한 실제 데이터에서 정확도를 크게 향상시킨다.
- 5. 이 연구는 내시경 이미지의 깊이 추정 분야를 발전시키고, 향후 연구를 위한 중요한 자원을 제공한다.


---

*Generated on 2025-09-24 16:05:10*