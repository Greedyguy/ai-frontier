---
keywords:
  - Transformer
  - Diffusion MRI
  - White Matter Tractography
  - Neural Pathway Mapping
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16429
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:20:33.501375",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Diffusion MRI",
    "White Matter Tractography",
    "Neural Pathway Mapping"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Diffusion MRI": 0.8,
    "White Matter Tractography": 0.78,
    "Neural Pathway Mapping": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer Networks",
        "canonical": "Transformer",
        "aliases": [
          "Transformer Models"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in deep learning, relevant for connecting to broader neural network research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Diffusion MRI",
        "canonical": "Diffusion MRI",
        "aliases": [
          "dMRI"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion MRI is a specialized imaging technique crucial for understanding neural pathways, offering unique insights into neuroimaging.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "White Matter Tractography",
        "canonical": "White Matter Tractography",
        "aliases": [
          "WM Tractography"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application within neuroimaging that directly relates to the paper's focus on neural pathway mapping.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural Pathway Mapping",
        "canonical": "Neural Pathway Mapping",
        "aliases": [
          "Neural Tract Mapping"
        ],
        "category": "unique_technical",
        "rationale": "Mapping neural pathways is central to the paper's contribution and connects to broader neuroimaging research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer Networks",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Diffusion MRI",
      "resolved_canonical": "Diffusion MRI",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "White Matter Tractography",
      "resolved_canonical": "White Matter Tractography",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural Pathway Mapping",
      "resolved_canonical": "Neural Pathway Mapping",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# TractoTransformer: Diffusion MRI Streamline Tractography using CNN and Transformer Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16429.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16429](https://arxiv.org/abs/2509.16429)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (83.3% similar)
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (81.8% similar)
- [[2025-09-23/Automated Labeling of Intracranial Arteries with Uncertainty Quantification Using Deep Learning_20250923|Automated Labeling of Intracranial Arteries with Uncertainty Quantification Using Deep Learning]] (81.7% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (80.6% similar)
- [[2025-09-22/FMD-TransUNet_ Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms_20250922|FMD-TransUNet: Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Diffusion MRI|Diffusion MRI]], [[keywords/White Matter Tractography|White Matter Tractography]], [[keywords/Neural Pathway Mapping|Neural Pathway Mapping]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16429v1 Announce Type: new 
Abstract: White matter tractography is an advanced neuroimaging technique that reconstructs the 3D white matter pathways of the brain from diffusion MRI data. It can be framed as a pathfinding problem aiming to infer neural fiber trajectories from noisy and ambiguous measurements, facing challenges such as crossing, merging, and fanning white-matter configurations. In this paper, we propose a novel tractography method that leverages Transformers to model the sequential nature of white matter streamlines, enabling the prediction of fiber directions by integrating both the trajectory context and current diffusion MRI measurements. To incorporate spatial information, we utilize CNNs that extract microstructural features from local neighborhoods around each voxel. By combining these complementary sources of information, our approach improves the precision and completeness of neural pathway mapping compared to traditional tractography models. We evaluate our method with the Tractometer toolkit, achieving competitive performance against state-of-the-art approaches, and present qualitative results on the TractoInferno dataset, demonstrating strong generalization to real-world data.

## 📝 요약

이 논문은 확산 MRI 데이터를 활용한 백질 경로 추적 기법을 제안합니다. 기존 기법들이 직면한 교차, 합류, 확산 등의 문제를 해결하기 위해, 이 연구는 Transformer를 활용하여 백질 섬유의 방향성을 예측합니다. 또한, CNN을 통해 각 복셀 주변의 미세 구조적 특징을 추출하여 공간 정보를 통합합니다. 이러한 방법론은 기존 모델보다 신경 경로 매핑의 정확성과 완전성을 향상시킵니다. Tractometer 도구를 사용한 평가에서 최첨단 기법과 경쟁력 있는 성능을 보였으며, TractoInferno 데이터셋을 통해 실제 데이터에 대한 강력한 일반화 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. 본 논문은 Transformer를 활용하여 백질 섬유 방향을 예측하는 새로운 트랙토그래피 방법을 제안합니다.
- 2. 제안된 방법은 백질 섬유의 순차적 특성을 모델링하여 경로 문맥과 현재 확산 MRI 측정을 통합합니다.
- 3. CNN을 사용하여 각 복셀 주변의 국소 이웃에서 미세 구조적 특징을 추출하여 공간 정보를 통합합니다.
- 4. 전통적인 트랙토그래피 모델에 비해 신경 경로 매핑의 정밀성과 완전성을 향상시킵니다.
- 5. Tractometer 툴킷으로 평가한 결과, 최신 기법들과 경쟁력 있는 성능을 보였으며, TractoInferno 데이터셋에서 강력한 일반화 능력을 입증했습니다.


---

*Generated on 2025-09-24 04:20:33*