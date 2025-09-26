<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:09:23.792170",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Robot-assisted Surgery",
    "Multi-task Learning",
    "Optical Flow-based Segmentation",
    "Surgical Instrument Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Robot-assisted Surgery": 0.8,
    "Multi-task Learning": 0.75,
    "Optical Flow-based Segmentation": 0.7,
    "Surgical Instrument Segmentation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Robot-assisted surgery",
        "canonical": "Robot-assisted Surgery",
        "aliases": [
          "RAS"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and connects to advancements in surgical technology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-task learning",
        "canonical": "Multi-task Learning",
        "aliases": [
          "MTL"
        ],
        "category": "broad_technical",
        "rationale": "Multi-task learning is a key approach in the paper, linking to various machine learning applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "optical flow-based segmentation",
        "canonical": "Optical Flow-based Segmentation",
        "aliases": [
          "optical flow segmentation"
        ],
        "category": "unique_technical",
        "rationale": "This technique is pivotal for label interpolation in the paper, offering a unique approach to video analysis.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "surgical instrument segmentation",
        "canonical": "Surgical Instrument Segmentation",
        "aliases": [
          "instrument segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "This task is crucial for understanding surgical scenes and links to computer vision applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "visual data",
      "temporal dynamics",
      "key frames"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Robot-assisted surgery",
      "resolved_canonical": "Robot-assisted Surgery",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-task learning",
      "resolved_canonical": "Multi-task Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "optical flow-based segmentation",
      "resolved_canonical": "Optical Flow-based Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "surgical instrument segmentation",
      "resolved_canonical": "Surgical Instrument Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Surgical Video Understanding with Label Interpolation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18802.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18802](https://arxiv.org/abs/2509.18802)

## 🔗 유사한 논문
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (85.8% similar)
- [[2025-09-19/Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery_20250919|Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery]] (85.3% similar)
- [[2025-09-24/Towards Application Aligned Synthetic Surgical Image Synthesis_20250924|Towards Application Aligned Synthetic Surgical Image Synthesis]] (83.2% similar)
- [[2025-09-23/VocSegMRI_ Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI_20250923|VocSegMRI: Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI]] (83.0% similar)
- [[2025-09-23/Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views_20250923|Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-task Learning|Multi-task Learning]]
**🔗 Specific Connectable**: [[keywords/Surgical Instrument Segmentation|Surgical Instrument Segmentation]]
**⚡ Unique Technical**: [[keywords/Robot-assisted Surgery|Robot-assisted Surgery]], [[keywords/Optical Flow-based Segmentation|Optical Flow-based Segmentation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18802v1 Announce Type: new 
Abstract: Robot-assisted surgery (RAS) has become a critical paradigm in modern surgery, promoting patient recovery and reducing the burden on surgeons through minimally invasive approaches. To fully realize its potential, however, a precise understanding of the visual data generated during surgical procedures is essential. Previous studies have predominantly focused on single-task approaches, but real surgical scenes involve complex temporal dynamics and diverse instrument interactions that limit comprehensive understanding. Moreover, the effective application of multi-task learning (MTL) requires sufficient pixel-level segmentation data, which are difficult to obtain due to the high cost and expertise required for annotation. In particular, long-term annotations such as phases and steps are available for every frame, whereas short-term annotations such as surgical instrument segmentation and action detection are provided only for key frames, resulting in a significant temporal-spatial imbalance. To address these challenges, we propose a novel framework that combines optical flow-based segmentation label interpolation with multi-task learning. optical flow estimated from annotated key frames is used to propagate labels to adjacent unlabeled frames, thereby enriching sparse spatial supervision and balancing temporal and spatial information for training. This integration improves both the accuracy and efficiency of surgical scene understanding and, in turn, enhances the utility of RAS.

## 📝 요약

로봇 보조 수술(RAS)은 최소 침습적 접근을 통해 환자 회복을 촉진하고 외과의사의 부담을 줄이는 중요한 현대 수술 패러다임입니다. 그러나 수술 중 생성되는 시각 데이터의 정확한 이해가 필요합니다. 기존 연구는 주로 단일 작업에 집중했으나, 실제 수술 장면은 복잡한 시간적 역학과 다양한 기구 상호작용을 포함합니다. 또한, 다중 작업 학습(MTL)의 효과적인 적용을 위해서는 픽셀 수준의 세분화 데이터가 필요하지만, 이는 높은 비용과 전문성 때문에 얻기 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 광학 흐름 기반의 세분화 레이블 보간과 다중 작업 학습을 결합한 새로운 프레임워크를 제안합니다. 주석이 달린 주요 프레임에서 추정된 광학 흐름을 사용하여 레이블을 인접한 비주석 프레임으로 전파함으로써, 희소한 공간적 감독을 풍부하게 하고 시간적 및 공간적 정보를 균형 있게 합니다. 이 통합은 수술 장면 이해의 정확성과 효율성을 향상시켜 RAS의 유용성을 높입니다.

## 🎯 주요 포인트

- 1. 로봇 보조 수술(RAS)은 최소 침습 접근법을 통해 환자 회복을 촉진하고 외과의사의 부담을 줄이는 중요한 현대 수술 패러다임입니다.
- 2. 기존 연구는 주로 단일 작업 접근법에 집중했지만, 실제 수술 장면은 복잡한 시간적 역학과 다양한 기구 상호작용을 포함하여 포괄적인 이해에 한계가 있습니다.
- 3. 다중 작업 학습(MTL)의 효과적인 적용을 위해서는 충분한 픽셀 수준의 분할 데이터가 필요하지만, 이는 높은 비용과 전문성 요구로 인해 얻기 어렵습니다.
- 4. 제안된 프레임워크는 주석된 주요 프레임에서 추정된 광학 흐름을 사용하여 레이블을 인접한 비주석 프레임으로 전파함으로써 희소한 공간적 감독을 풍부하게 하고 시간적 및 공간적 정보를 균형 있게 합니다.
- 5. 이 통합은 수술 장면 이해의 정확성과 효율성을 개선하여 RAS의 유용성을 향상시킵니다.


---

*Generated on 2025-09-24 16:09:23*