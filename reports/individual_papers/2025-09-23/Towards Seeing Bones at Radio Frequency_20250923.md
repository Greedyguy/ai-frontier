---
keywords:
  - Radio Frequency Imaging
  - Synthetic Aperture Algorithm
  - Machine Learning Pipeline
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17979
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:28:30.264488",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Radio Frequency Imaging",
    "Synthetic Aperture Algorithm",
    "Machine Learning Pipeline"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Radio Frequency Imaging": 0.78,
    "Synthetic Aperture Algorithm": 0.72,
    "Machine Learning Pipeline": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RF-imaging system",
        "canonical": "Radio Frequency Imaging",
        "aliases": [
          "RF imaging",
          "RF-imaging"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specialized imaging technique that is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "synthetic aperture algorithm",
        "canonical": "Synthetic Aperture Algorithm",
        "aliases": [
          "synthetic aperture"
        ],
        "category": "unique_technical",
        "rationale": "The algorithm is a novel aspect of the paper's methodology, enhancing RF imaging capabilities.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "learning-based pipeline",
        "canonical": "Machine Learning Pipeline",
        "aliases": [
          "learning pipeline"
        ],
        "category": "broad_technical",
        "rationale": "This term links to broader machine learning concepts, facilitating connections to related works.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "X-ray image",
      "meat models",
      "resolution improvement"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "RF-imaging system",
      "resolved_canonical": "Radio Frequency Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "synthetic aperture algorithm",
      "resolved_canonical": "Synthetic Aperture Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "learning-based pipeline",
      "resolved_canonical": "Machine Learning Pipeline",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Towards Seeing Bones at Radio Frequency

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17979.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17979](https://arxiv.org/abs/2509.17979)

## 🔗 유사한 논문
- [[2025-09-19/Chameleon_ Integrated Sensing and Communication with Sub-Symbol Beam Switching in mmWave Networks_20250919|Chameleon: Integrated Sensing and Communication with Sub-Symbol Beam Switching in mmWave Networks]] (78.9% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (78.7% similar)
- [[2025-09-19/Object Recognition and Force Estimation with the GelSight Baby Fin Ray_20250919|Object Recognition and Force Estimation with the GelSight Baby Fin Ray]] (78.1% similar)
- [[2025-09-19/CushionCatch_ A Compliant Catching Mechanism for Mobile Manipulators via Combined Optimization and Learning_20250919|CushionCatch: A Compliant Catching Mechanism for Mobile Manipulators via Combined Optimization and Learning]] (77.7% similar)
- [[2025-09-23/On the Detection of Internal Defects in Structured Media_20250923|On the Detection of Internal Defects in Structured Media]] (77.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning Pipeline|Machine Learning Pipeline]]
**⚡ Unique Technical**: [[keywords/Radio Frequency Imaging|Radio Frequency Imaging]], [[keywords/Synthetic Aperture Algorithm|Synthetic Aperture Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17979v1 Announce Type: cross 
Abstract: Wireless sensing literature has long aspired to achieve X-ray-like vision at radio frequencies. Yet, state-of-the-art wireless sensing literature has yet to generate the archetypal X-ray image: one of the bones beneath flesh. In this paper, we explore MCT, a penetration-based RF-imaging system for imaging bones at mm-resolution, one that significantly exceeds prior penetration-based RF imaging literature. Indeed the long wavelength, significant attenuation and complex diffraction that occur as RF propagates through flesh, have long limited imaging resolution (to several centimeters at best). We address these concerns through a novel penetration-based synthetic aperture algorithm, coupled with a learning-based pipeline to correct for diffraction-induced artifacts. A detailed evaluation of meat models demonstrates a resolution improvement from sub-decimeter to sub-centimeter over prior art in RF penetrative imaging.

## 📝 요약

이 논문은 무선 주파수를 이용한 뼈 이미징 시스템인 MCT를 제안하여 기존의 무선 센싱 기술을 뛰어넘는 밀리미터 수준의 해상도를 달성했습니다. 기존 무선 이미징 기술은 긴 파장과 신체 조직을 통한 전파의 감쇠 및 복잡한 회절로 인해 해상도가 제한되었습니다. 본 연구는 새로운 침투 기반 합성 개구 알고리즘과 회절로 인한 왜곡을 보정하는 학습 기반 파이프라인을 통해 이러한 문제를 해결했습니다. 고기 모델을 이용한 평가 결과, 기존 기술 대비 해상도가 수 센티미터에서 센티미터 미만으로 향상되었습니다.

## 🎯 주요 포인트

- 1. 본 논문은 무선 주파수를 이용한 X-ray와 유사한 이미징을 목표로 하는 MCT 시스템을 소개합니다.
- 2. MCT 시스템은 mm-해상도로 뼈를 이미징할 수 있으며, 기존의 RF 이미징 기술을 뛰어넘는 성능을 보입니다.
- 3. 새로운 침투 기반 합성 개구 알고리즘과 학습 기반 파이프라인을 통해 회절로 인한 왜곡을 보정합니다.
- 4. 육류 모델을 통한 평가에서 기존 RF 침투 이미징 기술 대비 해상도가 수 센티미터에서 수 밀리미터로 개선되었습니다.


---

*Generated on 2025-09-24 02:28:30*