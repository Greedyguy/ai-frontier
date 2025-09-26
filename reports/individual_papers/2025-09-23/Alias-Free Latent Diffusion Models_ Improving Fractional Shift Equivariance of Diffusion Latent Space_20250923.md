---
keywords:
  - Latent Diffusion Models
  - Shift Equivariance
  - Attention Mechanism
  - Alias-Free Latent Diffusion Models
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2503.09419
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:19:16.247493",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Latent Diffusion Models",
    "Shift Equivariance",
    "Attention Mechanism",
    "Alias-Free Latent Diffusion Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Latent Diffusion Models": 0.78,
    "Shift Equivariance": 0.77,
    "Attention Mechanism": 0.8,
    "Alias-Free Latent Diffusion Models": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Latent Diffusion Models",
        "canonical": "Latent Diffusion Models",
        "aliases": [
          "LDMs"
        ],
        "category": "unique_technical",
        "rationale": "Latent Diffusion Models are central to the paper's contributions and represent a unique technical advancement.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Shift Equivariance",
        "canonical": "Shift Equivariance",
        "aliases": [
          "Shift-Equivariant"
        ],
        "category": "unique_technical",
        "rationale": "Shift Equivariance is a key concept in improving the stability of LDMs and is specific to this research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Module"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanisms are redesigned in the paper to achieve shift-equivariance, linking to broader neural network concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Alias-Free LDM",
        "canonical": "Alias-Free Latent Diffusion Models",
        "aliases": [
          "AF-LDM"
        ],
        "category": "unique_technical",
        "rationale": "Alias-Free LDM represents a novel improvement over traditional LDMs, enhancing shift-equivariance.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "VAE",
      "U-Net",
      "self-attention"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Latent Diffusion Models",
      "resolved_canonical": "Latent Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Shift Equivariance",
      "resolved_canonical": "Shift Equivariance",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Alias-Free LDM",
      "resolved_canonical": "Alias-Free Latent Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Alias-Free Latent Diffusion Models: Improving Fractional Shift Equivariance of Diffusion Latent Space

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.09419.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2503.09419](https://arxiv.org/abs/2503.09419)

## 🔗 유사한 논문
- [[2025-09-23/Time Is a Feature_ Exploiting Temporal Dynamics in Diffusion Language Models_20250923|Time Is a Feature: Exploiting Temporal Dynamics in Diffusion Language Models]] (83.1% similar)
- [[2025-09-22/Discrete Diffusion in Large Language and Multimodal Models_ A Survey_20250922|Discrete Diffusion in Large Language and Multimodal Models: A Survey]] (82.4% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.2% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.9% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Latent Diffusion Models|Latent Diffusion Models]], [[keywords/Shift Equivariance|Shift Equivariance]], [[keywords/Alias-Free Latent Diffusion Models|Alias-Free Latent Diffusion Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.09419v2 Announce Type: replace 
Abstract: Latent Diffusion Models (LDMs) are known to have an unstable generation process, where even small perturbations or shifts in the input noise can lead to significantly different outputs. This hinders their applicability in applications requiring consistent results. In this work, we redesign LDMs to enhance consistency by making them shift-equivariant. While introducing anti-aliasing operations can partially improve shift-equivariance, significant aliasing and inconsistency persist due to the unique challenges in LDMs, including 1) aliasing amplification during VAE training and multiple U-Net inferences, and 2) self-attention modules that inherently lack shift-equivariance. To address these issues, we redesign the attention modules to be shift-equivariant and propose an equivariance loss that effectively suppresses the frequency bandwidth of the features in the continuous domain. The resulting alias-free LDM (AF-LDM) achieves strong shift-equivariance and is also robust to irregular warping. Extensive experiments demonstrate that AF-LDM produces significantly more consistent results than vanilla LDM across various applications, including video editing and image-to-image translation.

## 📝 요약

이 논문에서는 잠재 확산 모델(LDM)의 불안정한 생성 과정을 개선하기 위해 모델을 이동 등가적으로 재설계했습니다. 기존 LDM은 입력 노이즈의 작은 변화에도 출력이 크게 달라지는 문제가 있어 일관된 결과가 필요한 응용에 한계가 있었습니다. 이를 해결하기 위해 주의 모듈을 이동 등가적으로 재설계하고, 연속 도메인에서 특징의 주파수 대역을 억제하는 등가 손실을 제안했습니다. 결과적으로, 새로운 모델인 AF-LDM은 강력한 이동 등가성을 가지며 불규칙한 왜곡에도 강인한 성능을 보입니다. 다양한 실험을 통해 AF-LDM이 기존 LDM보다 비디오 편집 및 이미지 변환 등 여러 응용에서 더 일관된 결과를 생성함을 확인했습니다.

## 🎯 주요 포인트

- 1. 잠재 확산 모델(LDM)은 입력 노이즈의 작은 변화에도 출력이 크게 달라지는 불안정한 생성 과정을 가지고 있다.
- 2. 본 연구에서는 LDM의 일관성을 높이기 위해 시프트 등가성을 갖도록 재설계하였다.
- 3. 반대칭 연산을 도입하여 시프트 등가성을 일부 개선할 수 있지만, LDM의 고유한 문제로 인해 여전히 상당한 앨리어싱과 불일치가 존재한다.
- 4. 주의 모듈을 시프트 등가적으로 재설계하고, 연속 도메인에서 특징의 주파수 대역폭을 효과적으로 억제하는 등가 손실을 제안하였다.
- 5. 제안된 앨리어싱 없는 LDM(AF-LDM)은 강력한 시프트 등가성을 달성하며, 비정형 왜곡에도 강건한 성능을 보인다.


---

*Generated on 2025-09-24 05:19:16*