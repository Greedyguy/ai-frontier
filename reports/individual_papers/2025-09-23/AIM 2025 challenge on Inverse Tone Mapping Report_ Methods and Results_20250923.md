---
keywords:
  - Inverse Tone Mapping
  - HDR Image Reconstruction
  - Perceptual Fidelity
  - Numerical Consistency
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2508.13479
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:29:44.262906",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Inverse Tone Mapping",
    "HDR Image Reconstruction",
    "Perceptual Fidelity",
    "Numerical Consistency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Inverse Tone Mapping": 0.78,
    "HDR Image Reconstruction": 0.77,
    "Perceptual Fidelity": 0.75,
    "Numerical Consistency": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Inverse Tone Mapping",
        "canonical": "Inverse Tone Mapping",
        "aliases": [
          "ITM"
        ],
        "category": "unique_technical",
        "rationale": "Inverse Tone Mapping is a specialized technique crucial for HDR image reconstruction, offering unique insights into image processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "HDR Image Reconstruction",
        "canonical": "HDR Image Reconstruction",
        "aliases": [
          "High Dynamic Range Image Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "HDR Image Reconstruction is a key process in image processing, directly related to the challenge's focus.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Perceptual Fidelity",
        "canonical": "Perceptual Fidelity",
        "aliases": [
          "Visual Fidelity"
        ],
        "category": "unique_technical",
        "rationale": "Perceptual Fidelity is critical for assessing the quality of HDR reconstructions, linking to perceptual metrics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Numerical Consistency",
        "canonical": "Numerical Consistency",
        "aliases": [
          "Quantitative Consistency"
        ],
        "category": "unique_technical",
        "rationale": "Numerical Consistency ensures the quantitative accuracy of HDR reconstructions, relevant to algorithm evaluation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.68,
        "specificity_score": 0.76,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "AIM 2025 Challenge",
      "PU21-PSNR"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Inverse Tone Mapping",
      "resolved_canonical": "Inverse Tone Mapping",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "HDR Image Reconstruction",
      "resolved_canonical": "HDR Image Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Perceptual Fidelity",
      "resolved_canonical": "Perceptual Fidelity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Numerical Consistency",
      "resolved_canonical": "Numerical Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.68,
        "specificity": 0.76,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# AIM 2025 challenge on Inverse Tone Mapping Report: Methods and Results

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2508.13479.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2508.13479](https://arxiv.org/abs/2508.13479)

## 🔗 유사한 논문
- [[2025-09-23/PhysHDR_ When Lighting Meets Materials and Scene Geometry in HDR Reconstruction_20250923|PhysHDR: When Lighting Meets Materials and Scene Geometry in HDR Reconstruction]] (80.1% similar)
- [[2025-09-18/Task-Aware Image Signal Processor for Advanced Visual Perception_20250918|Task-Aware Image Signal Processor for Advanced Visual Perception]] (77.8% similar)
- [[2025-09-23/Rethinking Evaluation of Infrared Small Target Detection_20250923|Rethinking Evaluation of Infrared Small Target Detection]] (77.8% similar)
- [[2025-09-23/AISTAT lab system for DCASE2025 Task6_ Language-based audio retrieval_20250923|AISTAT lab system for DCASE2025 Task6: Language-based audio retrieval]] (77.7% similar)
- [[2025-09-22/USCTNet_ A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction_20250922|USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction]] (77.5% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Inverse Tone Mapping|Inverse Tone Mapping]], [[keywords/HDR Image Reconstruction|HDR Image Reconstruction]], [[keywords/Perceptual Fidelity|Perceptual Fidelity]], [[keywords/Numerical Consistency|Numerical Consistency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.13479v2 Announce Type: replace 
Abstract: This paper presents a comprehensive review of the AIM 2025 Challenge on Inverse Tone Mapping (ITM). The challenge aimed to push forward the development of effective ITM algorithms for HDR image reconstruction from single LDR inputs, focusing on perceptual fidelity and numerical consistency. A total of \textbf{67} participants submitted \textbf{319} valid results, from which the best five teams were selected for detailed analysis. This report consolidates their methodologies and performance, with the lowest PU21-PSNR among the top entries reaching 29.22 dB. The analysis highlights innovative strategies for enhancing HDR reconstruction quality and establishes strong benchmarks to guide future research in inverse tone mapping.

## 📝 요약

이 논문은 AIM 2025 챌린지의 일환으로 진행된 역 톤 매핑(ITM) 연구를 종합적으로 검토합니다. 이 챌린지는 단일 LDR 입력으로부터 HDR 이미지를 재구성하는 효과적인 ITM 알고리즘 개발을 목표로 하였으며, 지각적 충실도와 수치적 일관성에 중점을 두었습니다. 총 67명의 참가자가 319개의 유효 결과를 제출했으며, 상위 5개 팀의 방법론과 성과를 상세히 분석했습니다. 분석 결과, HDR 재구성 품질을 향상시키기 위한 혁신적인 전략이 강조되었으며, 향후 연구를 위한 강력한 기준점을 마련했습니다.

## 🎯 주요 포인트

- 1. AIM 2025 챌린지는 단일 LDR 입력으로부터 HDR 이미지 복원을 위한 효과적인 ITM 알고리즘 개발을 목표로 했다.
- 2. 총 67명의 참가자가 319개의 유효한 결과를 제출했으며, 그 중 상위 5개 팀이 자세한 분석을 위해 선정되었다.
- 3. 보고서는 상위 팀들의 방법론과 성능을 통합하여, HDR 복원 품질을 향상시키기 위한 혁신적인 전략을 강조한다.
- 4. 최상위 결과 중 최저 PU21-PSNR은 29.22 dB에 도달했다.
- 5. 이 분석은 역 톤 매핑 연구의 미래를 위한 강력한 벤치마크를 확립한다.


---

*Generated on 2025-09-24 05:29:44*