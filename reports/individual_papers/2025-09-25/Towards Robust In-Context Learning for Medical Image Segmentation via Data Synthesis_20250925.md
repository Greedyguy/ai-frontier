---
keywords:
  - Few-Shot Learning
  - Medical Image Segmentation
  - Data Synthesis
  - Domain Randomization
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19711
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:03:26.173718",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Medical Image Segmentation",
    "Data Synthesis",
    "Domain Randomization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.82,
    "Medical Image Segmentation": 0.78,
    "Data Synthesis": 0.77,
    "Domain Randomization": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "In-Context Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "ICL"
        ],
        "category": "specific_connectable",
        "rationale": "In-Context Learning is closely related to Few-Shot Learning, enhancing connectivity with existing research on learning with limited data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Medical Image Segmentation",
        "canonical": "Medical Image Segmentation",
        "aliases": [
          "Medical Segmentation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized application area that directly relates to the paper's focus, providing a unique technical link.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Data Synthesis",
        "canonical": "Data Synthesis",
        "aliases": [
          "Synthetic Data Generation"
        ],
        "category": "unique_technical",
        "rationale": "Data synthesis is a key technique discussed in the paper, relevant for generating diverse datasets.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Domain Randomization",
        "canonical": "Domain Randomization",
        "aliases": [
          "Domain Variability"
        ],
        "category": "unique_technical",
        "rationale": "Domain randomization is a novel approach in the context of this paper, enhancing the robustness of models.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "universal",
      "framework",
      "realism"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "In-Context Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Medical Image Segmentation",
      "resolved_canonical": "Medical Image Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Data Synthesis",
      "resolved_canonical": "Data Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Domain Randomization",
      "resolved_canonical": "Domain Randomization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Towards Robust In-Context Learning for Medical Image Segmentation via Data Synthesis

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19711.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19711](https://arxiv.org/abs/2509.19711)

## 🔗 유사한 논문
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (86.6% similar)
- [[2025-09-24/Towards Application Aligned Synthetic Surgical Image Synthesis_20250924|Towards Application Aligned Synthetic Surgical Image Synthesis]] (85.6% similar)
- [[2025-09-24/MediSyn_ A Generalist Text-Guided Latent Diffusion Model For Diverse Medical Image Synthesis_20250924|MediSyn: A Generalist Text-Guided Latent Diffusion Model For Diverse Medical Image Synthesis]] (85.1% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (83.8% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Medical Image Segmentation|Medical Image Segmentation]], [[keywords/Data Synthesis|Data Synthesis]], [[keywords/Domain Randomization|Domain Randomization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19711v1 Announce Type: new 
Abstract: The rise of In-Context Learning (ICL) for universal medical image segmentation has introduced an unprecedented demand for large-scale, diverse datasets for training, exacerbating the long-standing problem of data scarcity. While data synthesis offers a promising solution, existing methods often fail to simultaneously achieve both high data diversity and a domain distribution suitable for medical data. To bridge this gap, we propose \textbf{SynthICL}, a novel data synthesis framework built upon domain randomization. SynthICL ensures realism by leveraging anatomical priors from real-world datasets, generates diverse anatomical structures to cover a broad data distribution, and explicitly models inter-subject variations to create data cohorts suitable for ICL. Extensive experiments on four held-out datasets validate our framework's effectiveness, showing that models trained with our data achieve performance gains of up to 63\% in average Dice and substantially enhanced generalization to unseen anatomical domains. Our work helps mitigate the data bottleneck for ICL-based segmentation, paving the way for robust models. Our code and the generated dataset are publicly available at https://github.com/jiesihu/Neuroverse3D.

## 📝 요약

이 논문은 보편적인 의료 영상 분할을 위한 문맥 내 학습(ICL)의 증가로 인해 대규모, 다양한 데이터셋의 필요성이 커지고 있는 상황에서, 데이터 부족 문제를 해결하기 위한 새로운 데이터 합성 프레임워크인 SynthICL을 제안합니다. SynthICL은 실제 데이터셋의 해부학적 정보를 활용하여 현실성을 보장하고, 다양한 해부학적 구조를 생성하여 폭넓은 데이터 분포를 포괄하며, 개체 간 변이를 명시적으로 모델링하여 ICL에 적합한 데이터 집합을 만듭니다. 네 개의 데이터셋에 대한 실험 결과, SynthICL로 훈련된 모델은 평균 Dice 점수가 최대 63% 향상되었고, 새로운 해부학적 도메인에 대한 일반화 능력이 크게 증가했습니다. 이 연구는 ICL 기반 분할의 데이터 병목 현상을 완화하고, 견고한 모델 개발에 기여합니다. 코드와 생성된 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. In-Context Learning(ICL)의 발전으로 인해 의료 영상 분할을 위한 대규모, 다양한 데이터셋의 필요성이 증가하고 있습니다.
- 2. 기존 데이터 합성 방법은 높은 데이터 다양성과 의료 데이터에 적합한 도메인 분포를 동시에 달성하지 못하는 경우가 많습니다.
- 3. SynthICL은 실제 데이터셋의 해부학적 사전 지식을 활용하여 현실성을 보장하고, 다양한 해부학적 구조를 생성하여 광범위한 데이터 분포를 커버합니다.
- 4. SynthICL은 피험자 간 변동성을 명시적으로 모델링하여 ICL에 적합한 데이터 코호트를 생성합니다.
- 5. SynthICL로 훈련된 모델은 평균 Dice 점수에서 최대 63%의 성능 향상을 보이며, 새로운 해부학적 도메인에 대한 일반화 능력이 크게 향상되었습니다.


---

*Generated on 2025-09-26 09:03:26*