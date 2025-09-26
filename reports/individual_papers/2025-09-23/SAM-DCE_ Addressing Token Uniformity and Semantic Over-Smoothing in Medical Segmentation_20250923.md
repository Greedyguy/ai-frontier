---
keywords:
  - Segment Anything Model
  - Zero-Shot Learning
  - Medical Imaging
  - Semantic Over-Smoothing
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16886
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:37:14.338956",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Segment Anything Model",
    "Zero-Shot Learning",
    "Medical Imaging",
    "Semantic Over-Smoothing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Segment Anything Model": 0.78,
    "Zero-Shot Learning": 0.82,
    "Medical Imaging": 0.79,
    "Semantic Over-Smoothing": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Segment Anything Model",
        "canonical": "Segment Anything Model",
        "aliases": [
          "SAM"
        ],
        "category": "unique_technical",
        "rationale": "This model is central to the paper's contribution and represents a novel approach in segmentation tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Segmentation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot capabilities are crucial for understanding the model's performance without domain-specific training data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Medical Imaging",
        "canonical": "Medical Imaging",
        "aliases": [
          "Medical Image Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "The paper focuses on adapting segmentation models specifically for medical imaging, highlighting domain-specific challenges.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Semantic Over-Smoothing",
        "canonical": "Semantic Over-Smoothing",
        "aliases": [
          "Over-Smoothing"
        ],
        "category": "unique_technical",
        "rationale": "Addressing semantic over-smoothing is a unique challenge in the paper, crucial for improving model performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "domain shifts",
      "anatomical variability",
      "user-provided prompts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Segment Anything Model",
      "resolved_canonical": "Segment Anything Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Segmentation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Medical Imaging",
      "resolved_canonical": "Medical Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Semantic Over-Smoothing",
      "resolved_canonical": "Semantic Over-Smoothing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SAM-DCE: Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16886.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16886](https://arxiv.org/abs/2509.16886)

## 🔗 유사한 논문
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (88.4% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (87.6% similar)
- [[2025-09-22/TASAM_ Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation_20250922|TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation]] (87.3% similar)
- [[2025-09-23/BiPrompt-SAM_ Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts_20250923|BiPrompt-SAM: Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts]] (86.6% similar)
- [[2025-09-23/DescriptorMedSAM_ Language-Image Fusion with Multi-Aspect Text Guidance for Medical Image Segmentation_20250923|DescriptorMedSAM: Language-Image Fusion with Multi-Aspect Text Guidance for Medical Image Segmentation]] (86.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Medical Imaging|Medical Imaging]]
**⚡ Unique Technical**: [[keywords/Segment Anything Model|Segment Anything Model]], [[keywords/Semantic Over-Smoothing|Semantic Over-Smoothing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16886v1 Announce Type: new 
Abstract: The Segment Anything Model (SAM) demonstrates impressive zero-shot segmentation ability on natural images but encounters difficulties in medical imaging due to domain shifts, anatomical variability, and its reliance on user-provided prompts. Recent prompt-free adaptations alleviate the need for expert intervention, yet still suffer from limited robustness and adaptability, often overlooking the issues of semantic over-smoothing and token uniformity. We propose SAM-DCE, which balances local discrimination and global semantics while mitigating token uniformity, enhancing inter-class separability, and enriching mask decoding with fine-grained, consistent representations. Extensive experiments on diverse medical benchmarks validate its effectiveness.

## 📝 요약

Segment Anything Model (SAM)은 자연 이미지에서 뛰어난 제로샷 분할 능력을 보이지만, 의료 영상에서는 도메인 변화와 해부학적 다양성, 사용자 제공 프롬프트 의존성 때문에 어려움을 겪습니다. 최근 프롬프트 없이도 작동하는 방식이 개발되었지만, 여전히 강건성과 적응성이 제한적이며 의미적 과도한 평활화와 토큰 균일성 문제를 간과합니다. 이를 해결하기 위해 우리는 SAM-DCE를 제안합니다. SAM-DCE는 지역적 변별력과 전역적 의미를 균형 있게 유지하며, 토큰 균일성을 완화하고 클래스 간 분리성을 향상시키며, 세밀하고 일관된 표현으로 마스크 디코딩을 풍부하게 합니다. 다양한 의료 벤치마크 실험을 통해 그 효과가 입증되었습니다.

## 🎯 주요 포인트

- 1. Segment Anything Model (SAM)은 자연 이미지에서 뛰어난 zero-shot 분할 능력을 보이지만, 의료 영상에서는 도메인 변화와 해부학적 다양성 때문에 어려움을 겪습니다.
- 2. 최근의 프롬프트 없는 적응 방식은 전문가의 개입 필요성을 줄였지만, 여전히 제한된 견고성과 적응성 문제를 가지고 있습니다.
- 3. SAM-DCE는 지역적 구별성과 전역적 의미를 균형 있게 유지하며, 토큰 균일성을 완화하고 클래스 간 분리성을 향상시킵니다.
- 4. SAM-DCE는 세밀하고 일관된 표현으로 마스크 디코딩을 풍부하게 하여 성능을 개선합니다.
- 5. 다양한 의료 벤치마크에서의 광범위한 실험을 통해 SAM-DCE의 효과가 검증되었습니다.


---

*Generated on 2025-09-24 04:37:14*