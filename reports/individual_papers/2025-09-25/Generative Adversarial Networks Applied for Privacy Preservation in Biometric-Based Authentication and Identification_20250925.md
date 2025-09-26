---
keywords:
  - Generative Adversarial Network
  - Privacy Preservation
  - Biometric Authentication
  - Visually Private Domain
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20024
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:56:36.590770",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Adversarial Network",
    "Privacy Preservation",
    "Biometric Authentication",
    "Visually Private Domain"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generative Adversarial Network": 0.88,
    "Privacy Preservation": 0.82,
    "Biometric Authentication": 0.8,
    "Visually Private Domain": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Generative Adversarial Network",
        "canonical": "Generative Adversarial Network",
        "aliases": [
          "GAN",
          "Adversarial Network"
        ],
        "category": "broad_technical",
        "rationale": "GANs are a foundational technology in deep learning, relevant for linking to privacy and image transformation topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "Privacy Preservation",
        "canonical": "Privacy Preservation",
        "aliases": [
          "Data Privacy",
          "Privacy Protection"
        ],
        "category": "unique_technical",
        "rationale": "Privacy preservation is a critical aspect of biometric systems, providing a unique angle for linking privacy-focused technologies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Biometric-Based Authentication",
        "canonical": "Biometric Authentication",
        "aliases": [
          "Biometric Security",
          "Biometric Verification"
        ],
        "category": "specific_connectable",
        "rationale": "Biometric authentication is a key application area for GANs, facilitating connections to security and identity verification topics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      },
      {
        "surface": "Visually Private Domain",
        "canonical": "Visually Private Domain",
        "aliases": [
          "Visual Privacy",
          "Image Privacy"
        ],
        "category": "unique_technical",
        "rationale": "The concept of a visually private domain is novel and specific to this method, enhancing links to privacy and image transformation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "authentication method",
      "participating users",
      "meaningful utility"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Generative Adversarial Network",
      "resolved_canonical": "Generative Adversarial Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Privacy Preservation",
      "resolved_canonical": "Privacy Preservation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Biometric-Based Authentication",
      "resolved_canonical": "Biometric Authentication",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Visually Private Domain",
      "resolved_canonical": "Visually Private Domain",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Generative Adversarial Networks Applied for Privacy Preservation in Biometric-Based Authentication and Identification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20024.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20024](https://arxiv.org/abs/2509.20024)

## 🔗 유사한 논문
- [[2025-09-19/Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (84.0% similar)
- [[2025-09-23/Explainable AI for Analyzing Person-Specific Patterns in Facial Recognition Tasks_20250923|Explainable AI for Analyzing Person-Specific Patterns in Facial Recognition Tasks]] (82.2% similar)
- [[2025-09-22/PRISM_ Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images_20250922|PRISM: Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images]] (82.2% similar)
- [[2025-09-22/RaceGAN_ A Framework for Preserving Individuality while Converting Racial Information for Image-to-Image Translation_20250922|RaceGAN: A Framework for Preserving Individuality while Converting Racial Information for Image-to-Image Translation]] (81.7% similar)
- [[2025-09-22/Causal Fingerprints of AI Generative Models_20250922|Causal Fingerprints of AI Generative Models]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generative Adversarial Network|Generative Adversarial Network]]
**🔗 Specific Connectable**: [[keywords/Biometric Authentication|Biometric Authentication]]
**⚡ Unique Technical**: [[keywords/Privacy Preservation|Privacy Preservation]], [[keywords/Visually Private Domain|Visually Private Domain]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20024v1 Announce Type: cross 
Abstract: Biometric-based authentication systems are getting broadly adopted in many areas. However, these systems do not allow participating users to influence the way their data is used. Furthermore, the data may leak and can be misused without the users' knowledge. In this paper, we propose a new authentication method that preserves the privacy of individuals and is based on a generative adversarial network (GAN). Concretely, we suggest using the GAN for translating images of faces to a visually private domain (e.g., flowers or shoes). Classifiers, which are used for authentication purposes, are then trained on the images from the visually private domain. Based on our experiments, the method is robust against attacks and still provides meaningful utility.

## 📝 요약

이 논문은 개인의 프라이버시를 보호하는 새로운 생체 인증 방법을 제안합니다. 제안된 방법은 생성적 적대 신경망(GAN)을 활용하여 얼굴 이미지를 꽃이나 신발과 같은 시각적으로 비공개적인 도메인으로 변환합니다. 인증을 위한 분류기는 이러한 비공개 도메인의 이미지로 학습됩니다. 실험 결과, 이 방법은 공격에 강인하면서도 유의미한 유용성을 제공합니다.

## 🎯 주요 포인트

- 1. 생체 기반 인증 시스템은 사용자 데이터 사용 방식에 대한 통제권이 부족하며 데이터 유출 및 오용 가능성이 있다.
- 2. 본 논문에서는 개인의 프라이버시를 보호하는 새로운 인증 방법을 제안하며, 이는 생성적 적대 신경망(GAN)에 기반한다.
- 3. GAN을 활용하여 얼굴 이미지를 시각적으로 비공개 도메인(예: 꽃이나 신발)으로 변환하는 방식을 제안한다.
- 4. 인증 목적의 분류기는 시각적으로 비공개된 도메인의 이미지로 학습된다.
- 5. 제안된 방법은 공격에 강인하며 여전히 의미 있는 유용성을 제공한다.


---

*Generated on 2025-09-25 15:56:36*