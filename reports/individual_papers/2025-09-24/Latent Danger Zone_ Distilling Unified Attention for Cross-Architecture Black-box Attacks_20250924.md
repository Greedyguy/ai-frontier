<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:59:24.900495",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Latent Diffusion Model",
    "Black-box Adversarial Attacks",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Latent Diffusion Model": 0.72,
    "Black-box Adversarial Attacks": 0.79,
    "Attention Mechanism": 0.81
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Transformers, including Vision Transformers, are pivotal in modern deep learning architectures, enhancing connectivity across various models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "latent diffusion model",
        "canonical": "Latent Diffusion Model",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This model is central to the proposed method, offering a novel approach to adversarial attack generation.",
        "novelty_score": 0.78,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "black-box adversarial attacks",
        "canonical": "Black-box Adversarial Attacks",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper focuses on improving these attacks, making it a key concept for linking related research.",
        "novelty_score": 0.71,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "attention maps",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for understanding model focus areas, enhancing cross-model connectivity.",
        "novelty_score": 0.52,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.81
      }
    ],
    "ban_list_suggestions": [
      "JAD",
      "CNN"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "latent diffusion model",
      "resolved_canonical": "Latent Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "black-box adversarial attacks",
      "resolved_canonical": "Black-box Adversarial Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.71,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "attention maps",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.81
      }
    }
  ]
}
-->

# Latent Danger Zone: Distilling Unified Attention for Cross-Architecture Black-box Attacks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19044.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19044](https://arxiv.org/abs/2509.19044)

## 🔗 유사한 논문
- [[2025-09-18/DiffHash_ Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval_20250918|DiffHash: Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (82.3% similar)
- [[2025-09-17/Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics_20250917|Defending Diffusion Models Against Membership Inference Attacks via Higher-Order Langevin Dynamics]] (81.9% similar)
- [[2025-09-23/Jailbreak-Tuning_ Models Efficiently Learn Jailbreak Susceptibility_20250923|Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility]] (81.4% similar)
- [[2025-09-23/ADVEDM_Fine-grained Adversarial Attack against VLM-based Embodied Agents_20250923|ADVEDM:Fine-grained Adversarial Attack against VLM-based Embodied Agents]] (81.3% similar)
- [[2025-09-24/Backdoor Attack with Invisible Triggers Based on Model Architecture Modification_20250924|Backdoor Attack with Invisible Triggers Based on Model Architecture Modification]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Latent Diffusion Model|Latent Diffusion Model]], [[keywords/Black-box Adversarial Attacks|Black-box Adversarial Attacks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19044v1 Announce Type: new 
Abstract: Black-box adversarial attacks remain challenging due to limited access to model internals. Existing methods often depend on specific network architectures or require numerous queries, resulting in limited cross-architecture transferability and high query costs. To address these limitations, we propose JAD, a latent diffusion model framework for black-box adversarial attacks. JAD generates adversarial examples by leveraging a latent diffusion model guided by attention maps distilled from both a convolutional neural network (CNN) and a Vision Transformer (ViT) models. By focusing on image regions that are commonly sensitive across architectures, this approach crafts adversarial perturbations that transfer effectively between different model types. This joint attention distillation strategy enables JAD to be architecture-agnostic, achieving superior attack generalization across diverse models. Moreover, the generative nature of the diffusion framework yields high adversarial sample generation efficiency by reducing reliance on iterative queries. Experiments demonstrate that JAD offers improved attack generalization, generation efficiency, and cross-architecture transferability compared to existing methods, providing a promising and effective paradigm for black-box adversarial attacks.

## 📝 요약

이 논문에서는 블랙박스 적대적 공격의 한계를 극복하기 위해 JAD라는 잠재 확산 모델 프레임워크를 제안합니다. JAD는 CNN과 비전 트랜스포머(ViT) 모델에서 추출된 주의 맵을 활용하여 잠재 확산 모델을 통해 적대적 예제를 생성합니다. 이 방법은 다양한 모델 간에 효과적으로 전이되는 적대적 교란을 생성하며, 아키텍처에 구애받지 않는 공격 일반화를 달성합니다. 또한, 확산 프레임워크의 생성적 특성 덕분에 반복적인 쿼리에 대한 의존도를 줄여 높은 효율성을 보입니다. 실험 결과, JAD는 기존 방법에 비해 공격 일반화, 생성 효율성, 아키텍처 간 전이 가능성에서 개선된 성능을 보여줍니다.

## 🎯 주요 포인트

- 1. JAD는 CNN과 ViT 모델에서 추출한 주의 맵을 활용하여 잠재 확산 모델을 통해 적대적 예제를 생성합니다.
- 2. 이 접근법은 다양한 모델 유형 간에 효과적으로 전이되는 적대적 교란을 만듭니다.
- 3. JAD는 아키텍처에 구애받지 않으며, 다양한 모델에서 뛰어난 공격 일반화를 달성합니다.
- 4. 확산 프레임워크의 생성적 특성 덕분에 반복적인 쿼리에 대한 의존도를 줄여 높은 효율성으로 적대적 샘플을 생성합니다.
- 5. 실험 결과, JAD는 기존 방법에 비해 공격 일반화, 생성 효율성, 아키텍처 간 전이 가능성에서 향상된 성능을 보여줍니다.


---

*Generated on 2025-09-24 14:59:24*