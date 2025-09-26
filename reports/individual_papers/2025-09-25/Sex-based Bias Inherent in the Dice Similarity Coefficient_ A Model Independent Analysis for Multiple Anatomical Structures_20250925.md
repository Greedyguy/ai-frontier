---
keywords:
  - Dice Similarity Coefficient
  - Sex-based Bias
  - Medical Image Analysis
  - Segmentation Error
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19778
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:06:29.062606",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dice Similarity Coefficient",
    "Sex-based Bias",
    "Medical Image Analysis",
    "Segmentation Error"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dice Similarity Coefficient": 0.85,
    "Sex-based Bias": 0.8,
    "Medical Image Analysis": 0.75,
    "Segmentation Error": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dice Similarity Coefficient",
        "canonical": "Dice Similarity Coefficient",
        "aliases": [
          "DSC"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's analysis of bias in segmentation metrics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Sex-based Bias",
        "canonical": "Sex-based Bias",
        "aliases": [
          "Gender Bias"
        ],
        "category": "evolved_concepts",
        "rationale": "Highlights the paper's focus on bias in medical imaging metrics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Medical Image Analysis",
        "canonical": "Medical Image Analysis",
        "aliases": [
          "Medical Imaging"
        ],
        "category": "broad_technical",
        "rationale": "Relevant to the context of segmentation and bias analysis.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Segmentation Error",
        "canonical": "Segmentation Error",
        "aliases": [
          "Segmentation Mistake"
        ],
        "category": "unique_technical",
        "rationale": "Key to understanding the impact of bias in DSC measurements.",
        "novelty_score": 0.6,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "overlap-based metrics",
      "manual MRI annotations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dice Similarity Coefficient",
      "resolved_canonical": "Dice Similarity Coefficient",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Sex-based Bias",
      "resolved_canonical": "Sex-based Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Medical Image Analysis",
      "resolved_canonical": "Medical Image Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Segmentation Error",
      "resolved_canonical": "Segmentation Error",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Sex-based Bias Inherent in the Dice Similarity Coefficient: A Model Independent Analysis for Multiple Anatomical Structures

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19778.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19778](https://arxiv.org/abs/2509.19778)

## 🔗 유사한 논문
- [[2025-09-23/Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge_20250923|Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge]] (80.4% similar)
- [[2025-09-25/Blind Men and the Elephant_ Diverse Perspectives on Gender Stereotypes in Benchmark Datasets_20250925|Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets]] (79.5% similar)
- [[2025-09-24/Individualized Mapping of Aberrant Cortical Thickness via Stochastic Cortical Self-Reconstruction_20250924|Individualized Mapping of Aberrant Cortical Thickness via Stochastic Cortical Self-Reconstruction]] (79.4% similar)
- [[2025-09-24/"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts_20250924|"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts]] (79.1% similar)
- [[2025-09-23/SAM-DCE_ Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation_20250923|SAM-DCE: Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Medical Image Analysis|Medical Image Analysis]]
**⚡ Unique Technical**: [[keywords/Dice Similarity Coefficient|Dice Similarity Coefficient]], [[keywords/Segmentation Error|Segmentation Error]]
**🚀 Evolved Concepts**: [[keywords/Sex-based Bias|Sex-based Bias]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19778v1 Announce Type: new 
Abstract: Overlap-based metrics such as the Dice Similarity Coefficient (DSC) penalize segmentation errors more heavily in smaller structures. As organ size differs by sex, this implies that a segmentation error of equal magnitude may result in lower DSCs in women due to their smaller average organ volumes compared to men. While previous work has examined sex-based differences in models or datasets, no study has yet investigated the potential bias introduced by the DSC itself. This study quantifies sex-based differences of the DSC and the normalized DSC in an idealized setting independent of specific models. We applied equally-sized synthetic errors to manual MRI annotations from 50 participants to ensure sex-based comparability. Even minimal errors (e.g., a 1 mm boundary shift) produced systematic DSC differences between sexes. For small structures, average DSC differences were around 0.03; for medium-sized structures around 0.01. Only large structures (i.e., lungs and liver) were mostly unaffected, with sex-based DSC differences close to zero. These findings underline that fairness studies using the DSC as an evaluation metric should not expect identical scores between men and women, as the metric itself introduces bias. A segmentation model may perform equally well across sexes in terms of error magnitude, even if observed DSC values suggest otherwise. Importantly, our work raises awareness of a previously underexplored source of sex-based differences in segmentation performance. One that arises not from model behavior, but from the metric itself. Recognizing this factor is essential for more accurate and fair evaluations in medical image analysis.

## 📝 요약

이 연구는 Dice 유사도 계수(DSC)와 같은 중첩 기반 지표가 작은 구조에서의 분할 오류를 더 크게 벌점화하며, 이는 성별에 따라 장기 크기가 다르기 때문에 여성의 경우 더 낮은 DSC를 초래할 수 있음을 지적합니다. 50명의 참가자로부터 얻은 MRI 주석에 동등한 크기의 합성 오류를 적용하여 성별 간 비교를 수행한 결과, 작은 구조에서는 평균 DSC 차이가 약 0.03, 중간 크기 구조에서는 약 0.01로 나타났습니다. 큰 구조(폐와 간)는 성별에 따른 DSC 차이가 거의 없었습니다. 이 연구는 DSC 자체가 성별에 따른 편향을 도입할 수 있음을 강조하며, 의료 영상 분석에서 더 정확하고 공정한 평가를 위해 이 요소를 인식하는 것이 중요하다고 제안합니다.

## 🎯 주요 포인트

- 1. Dice Similarity Coefficient (DSC)는 작은 구조에서의 분할 오류를 더 크게 벌점화하며, 이는 성별에 따른 장기 크기 차이로 인해 여성에게 더 낮은 DSC를 초래할 수 있다.
- 2. 본 연구는 특정 모델과 독립적으로 DSC와 정규화된 DSC의 성별 차이를 이상적인 환경에서 정량화하였다.
- 3. 작은 구조에서는 평균 DSC 차이가 약 0.03, 중간 크기 구조에서는 약 0.01로 나타났으며, 큰 구조에서는 성별에 따른 DSC 차이가 거의 없었다.
- 4. DSC를 평가 척도로 사용하는 공정성 연구는 남성과 여성 간 동일한 점수를 기대해서는 안 되며, 이는 척도 자체가 편향을 도입하기 때문이다.
- 5. 본 연구는 모델의 행동이 아닌 척도 자체에서 발생하는 성별 차이의 원인을 인식하는 것이 의료 영상 분석에서 더 정확하고 공정한 평가를 위해 필수적임을 강조한다.


---

*Generated on 2025-09-26 09:06:29*