---
keywords:
  - 3D Gaussian Splatting
  - Contactless Fingerprint Recognition
  - 3D Fingerprint Reconstruction
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15648
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:04:49.415163",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Contactless Fingerprint Recognition",
    "3D Fingerprint Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Contactless Fingerprint Recognition": 0.85,
    "3D Fingerprint Reconstruction": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel technique applied for the first time in fingerprint recognition, offering unique insights into 3D reconstruction.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Contactless Fingerprint Recognition",
        "canonical": "Contactless Fingerprint Recognition",
        "aliases": [
          "Contactless Fingerprint Identification"
        ],
        "category": "specific_connectable",
        "rationale": "This specific application area can connect to broader topics in biometric recognition and security.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "3D Fingerprint Reconstruction",
        "canonical": "3D Fingerprint Reconstruction",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This process is central to the paper's contribution and connects to advancements in 3D modeling and computer vision.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "pose variations",
      "camera parameters"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Contactless Fingerprint Recognition",
      "resolved_canonical": "Contactless Fingerprint Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "3D Fingerprint Reconstruction",
      "resolved_canonical": "3D Fingerprint Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# FingerSplat: Contactless Fingerprint 3D Reconstruction and Generation based on 3D Gaussian Splatting

**Korean Title:** FingerSplat: 3D 가우시안 스플래팅을 기반으로 한 비접촉식 지문 3D 재구성 및 생성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15648.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15648](https://arxiv.org/abs/2509.15648)

## 🔗 유사한 논문
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (82.2% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (80.8% similar)
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (80.5% similar)
- [[2025-09-19/Roll Your Eyes_ Gaze Redirection via Explicit 3D Eyeball Rotation_20250919|Roll Your Eyes: Gaze Redirection via Explicit 3D Eyeball Rotation]] (80.4% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Contactless Fingerprint Recognition|Contactless Fingerprint Recognition]], [[keywords/3D Fingerprint Reconstruction|3D Fingerprint Reconstruction]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15648v1 Announce Type: new 
Abstract: Researchers have conducted many pioneer researches on contactless fingerprints, yet the performance of contactless fingerprint recognition still lags behind contact-based methods primary due to the insufficient contactless fingerprint data with pose variations and lack of the usage of implicit 3D fingerprint representations. In this paper, we introduce a novel contactless fingerprint 3D registration, reconstruction and generation framework by integrating 3D Gaussian Splatting, with the goal of offering a new paradigm for contactless fingerprint recognition that integrates 3D fingerprint reconstruction and generation. To our knowledge, this is the first work to apply 3D Gaussian Splatting to the field of fingerprint recognition, and the first to achieve effective 3D registration and complete reconstruction of contactless fingerprints with sparse input images and without requiring camera parameters information. Experiments on 3D fingerprint registration, reconstruction, and generation prove that our method can accurately align and reconstruct 3D fingerprints from 2D images, and sequentially generates high-quality contactless fingerprints from 3D model, thus increasing the performances for contactless fingerprint recognition.

## 🔍 Abstract (한글 번역)

arXiv:2509.15648v1 발표 유형: 신규  
초록: 연구자들은 비접촉식 지문에 대한 많은 선구적인 연구를 수행했지만, 비접촉식 지문 인식의 성능은 여전히 접촉 기반 방법에 비해 뒤처지고 있습니다. 이는 주로 자세 변형이 있는 비접촉식 지문 데이터의 부족과 암묵적인 3D 지문 표현의 사용 부족 때문입니다. 본 논문에서는 3D 가우시안 스플래팅을 통합하여 비접촉식 지문 3D 등록, 재구성 및 생성 프레임워크를 소개하며, 3D 지문 재구성과 생성을 통합한 새로운 비접촉식 지문 인식 패러다임을 제공하는 것을 목표로 합니다. 우리가 아는 한, 지문 인식 분야에 3D 가우시안 스플래팅을 적용한 것은 이번이 처음이며, 카메라 매개변수 정보 없이도 희소한 입력 이미지로 비접촉식 지문의 효과적인 3D 등록과 완전한 재구성을 달성한 것도 이번이 처음입니다. 3D 지문 등록, 재구성 및 생성에 대한 실험은 우리의 방법이 2D 이미지로부터 3D 지문을 정확하게 정렬하고 재구성할 수 있으며, 순차적으로 3D 모델로부터 고품질의 비접촉식 지문을 생성하여 비접촉식 지문 인식의 성능을 향상시킬 수 있음을 증명합니다.

## 📝 요약

이 논문은 비접촉식 지문 인식의 성능을 개선하기 위해 3D 가우시안 스플래팅을 활용한 새로운 3D 등록, 재구성 및 생성 프레임워크를 제안합니다. 기존의 비접촉식 지문 인식은 자세 변화에 따른 데이터 부족과 3D 지문 표현의 부재로 인해 성능이 저조했습니다. 본 연구는 3D 가우시안 스플래팅을 지문 인식에 최초로 적용하여, 카메라 매개변수 없이도 2D 이미지로부터 3D 지문을 효과적으로 정렬하고 완전하게 재구성합니다. 실험 결과, 제안된 방법이 고품질의 비접촉식 지문을 생성하여 인식 성능을 향상시킴을 확인했습니다.

## 🎯 주요 포인트

- 1. 비접촉식 지문 인식의 성능은 자세 변화가 있는 비접촉식 지문 데이터의 부족과 암묵적 3D 지문 표현의 사용 부족으로 인해 접촉식 방법에 비해 뒤처져 있다.
- 2. 본 논문은 3D Gaussian Splatting을 통합하여 비접촉식 지문 3D 등록, 재구성 및 생성 프레임워크를 제안한다.
- 3. 3D Gaussian Splatting을 지문 인식 분야에 적용한 최초의 연구로, 카메라 매개변수 정보 없이도 드문 입력 이미지로 비접촉식 지문의 효과적인 3D 등록 및 완전한 재구성을 달성했다.
- 4. 실험 결과, 제안된 방법이 2D 이미지로부터 3D 지문을 정확하게 정렬 및 재구성할 수 있으며, 3D 모델로부터 고품질의 비접촉식 지문을 생성하여 비접촉식 지문 인식 성능을 향상시킨다.


---

*Generated on 2025-09-23 12:04:49*