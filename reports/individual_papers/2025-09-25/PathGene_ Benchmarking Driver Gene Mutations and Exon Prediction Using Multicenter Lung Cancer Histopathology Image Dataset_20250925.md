---
keywords:
  - Deep Learning
  - PathGene Dataset
  - Tumor Mutational Burden
  - Next-Generation Sequencing
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2506.00096
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:26:20.414672",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "PathGene Dataset",
    "Tumor Mutational Burden",
    "Next-Generation Sequencing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.78,
    "PathGene Dataset": 0.82,
    "Tumor Mutational Burden": 0.79,
    "Next-Generation Sequencing": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is central to the prediction tasks described in the paper, linking it to existing AI methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "PathGene",
        "canonical": "PathGene Dataset",
        "aliases": [
          "PathGene"
        ],
        "category": "unique_technical",
        "rationale": "PathGene is a unique dataset introduced in the paper, crucial for linking to specific research on lung cancer histopathology.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Tumor Mutational Burden",
        "canonical": "Tumor Mutational Burden",
        "aliases": [
          "TMB"
        ],
        "category": "specific_connectable",
        "rationale": "TMB is a specific biomarker discussed in the paper, relevant for linking to cancer genomics and precision oncology.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Next-Generation Sequencing",
        "canonical": "Next-Generation Sequencing",
        "aliases": [
          "NGS"
        ],
        "category": "specific_connectable",
        "rationale": "Next-Generation Sequencing is a key technology used in the dataset, connecting to broader genomic research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "precision therapy",
      "personalized treatment",
      "early genetic screening"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "PathGene",
      "resolved_canonical": "PathGene Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Tumor Mutational Burden",
      "resolved_canonical": "Tumor Mutational Burden",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Next-Generation Sequencing",
      "resolved_canonical": "Next-Generation Sequencing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PathGene: Benchmarking Driver Gene Mutations and Exon Prediction Using Multicenter Lung Cancer Histopathology Image Dataset

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.00096.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2506.00096](https://arxiv.org/abs/2506.00096)

## 🔗 유사한 논문
- [[2025-09-23/Imaging Modalities-Based Classification for Lung Cancer Detection_20250923|Imaging Modalities-Based Classification for Lung Cancer Detection]] (84.1% similar)
- [[2025-09-23/IPGPhormer_ Interpretable Pathology Graph-Transformer for Survival Analysis_20250923|IPGPhormer: Interpretable Pathology Graph-Transformer for Survival Analysis]] (83.9% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (83.0% similar)
- [[2025-09-23/Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images_20250923|Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images]] (83.0% similar)
- [[2025-09-23/A Multimodal and Multi-centric Head and Neck Cancer Dataset for Segmentation, Diagnosis and Outcome Prediction_20250923|A Multimodal and Multi-centric Head and Neck Cancer Dataset for Segmentation, Diagnosis and Outcome Prediction]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Tumor Mutational Burden|Tumor Mutational Burden]], [[keywords/Next-Generation Sequencing|Next-Generation Sequencing]]
**⚡ Unique Technical**: [[keywords/PathGene Dataset|PathGene Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.00096v2 Announce Type: replace-cross 
Abstract: Accurately predicting gene mutations, mutation subtypes and their exons in lung cancer is critical for personalized treatment planning and prognostic assessment. Faced with regional disparities in medical resources and the high cost of genomic assays, using artificial intelligence to infer these mutations and exon variants from routine histopathology images could greatly facilitate precision therapy. Although some prior studies have shown that deep learning can accelerate the prediction of key gene mutations from lung cancer pathology slides, their performance remains suboptimal and has so far been limited mainly to early screening tasks. To address these limitations, we have assembled PathGene, which comprises histopathology images paired with next-generation sequencing reports from 1,576 patients at the Second Xiangya Hospital, Central South University, and 448 TCGA-LUAD patients. This multi-center dataset links whole-slide images to driver gene mutation status, mutation subtypes, exon, and tumor mutational burden (TMB) status, with the goal of leveraging pathology images to predict mutations, subtypes, exon locations, and TMB for early genetic screening and to advance precision oncology. Unlike existing datasets, we provide molecular-level information related to histopathology images in PathGene to facilitate the development of biomarker prediction models. We benchmarked 11 multiple-instance learning methods on PathGene for mutation, subtype, exon, and TMB prediction tasks. These experimental methods provide valuable alternatives for early genetic screening of lung cancer patients and assisting clinicians to quickly develop personalized precision targeted treatment plans for patients. Code and data are available at https://github.com/panliangrui/NIPS2025/.

## 📝 요약

이 논문은 폐암 환자의 유전자 돌연변이와 돌연변이 아형, 엑손을 예측하기 위해 인공지능을 활용하는 방법을 제안합니다. 기존 연구의 한계를 극복하기 위해, 연구팀은 1,576명의 환자와 448명의 TCGA-LUAD 환자로부터 수집한 다기관 데이터셋 PathGene를 구축했습니다. 이 데이터셋은 병리 이미지와 유전자 돌연변이 상태, 돌연변이 아형, 엑손 위치, 종양 돌연변이 부담(TMB) 상태를 연결하여, 병리 이미지를 통해 유전자 예측을 가능하게 합니다. 11개의 다중 인스턴스 학습 방법을 활용하여 돌연변이 및 TMB 예측을 수행하였으며, 이는 폐암 환자의 조기 유전자 스크리닝과 맞춤형 치료 계획 수립에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 폐암에서 유전자 돌연변이와 돌연변이 아형, 엑손을 정확히 예측하는 것은 개인 맞춤형 치료 계획과 예후 평가에 중요합니다.
- 2. 인공지능을 활용하여 일반적인 조직병리 이미지를 통해 돌연변이와 엑손 변이를 추론하면 정밀 치료를 크게 촉진할 수 있습니다.
- 3. PathGene 데이터셋은 1,576명의 환자와 448명의 TCGA-LUAD 환자로부터 수집된 조직병리 이미지와 차세대 시퀀싱 보고서를 포함합니다.
- 4. PathGene는 조직병리 이미지와 분자 수준의 정보를 연결하여 돌연변이, 아형, 엑손 위치, 종양 돌연변이 부담(TMB)을 예측하는 모델 개발을 지원합니다.
- 5. PathGene에서 11개의 다중 인스턴스 학습 방법을 벤치마킹하여 폐암 환자의 조기 유전자 스크리닝 및 개인화된 정밀 치료 계획 개발을 지원합니다.


---

*Generated on 2025-09-25 16:26:20*