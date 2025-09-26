---
keywords:
  - Self-supervised Learning
  - Shortcut Learning
  - Hybrid Generative-Discriminative Learning Framework
  - Invariance Pre-training Principle
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.11598
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:09:26.044987",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Shortcut Learning",
    "Hybrid Generative-Discriminative Learning Framework",
    "Invariance Pre-training Principle"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Shortcut Learning": 0.78,
    "Hybrid Generative-Discriminative Learning Framework": 0.8,
    "Invariance Pre-training Principle": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-Supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised Learning is a key paradigm discussed in the paper, crucial for linking with related works on learning frameworks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Shortcut Learning",
        "canonical": "Shortcut Learning",
        "aliases": [
          "Shortcut Bias"
        ],
        "category": "unique_technical",
        "rationale": "Shortcut Learning is identified as a systemic issue in the paper, providing a unique angle for exploring model biases.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hybrid Generative-Discriminative Learning Framework",
        "canonical": "Hybrid Generative-Discriminative Learning Framework",
        "aliases": [
          "HyGDL"
        ],
        "category": "unique_technical",
        "rationale": "This framework is the core contribution of the paper, offering a novel approach to disentangling content from style.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Invariance Pre-training Principle",
        "canonical": "Invariance Pre-training Principle",
        "aliases": [
          "Invariant Learning"
        ],
        "category": "unique_technical",
        "rationale": "The principle underpins the proposed framework, crucial for understanding the paper's methodological innovation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "MAE",
      "domain-specific features",
      "superficial features"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-Supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Shortcut Learning",
      "resolved_canonical": "Shortcut Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hybrid Generative-Discriminative Learning Framework",
      "resolved_canonical": "Hybrid Generative-Discriminative Learning Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Invariance Pre-training Principle",
      "resolved_canonical": "Invariance Pre-training Principle",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Disentangling Content from Style to Overcome Shortcut Learning: A Hybrid Generative-Discriminative Learning Framework

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11598.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.11598](https://arxiv.org/abs/2509.11598)

## 🔗 유사한 논문
- [[2025-09-18/StyleSculptor_ Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance_20250918|StyleSculptor: Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance]] (82.9% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (82.3% similar)
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (81.2% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (81.0% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Shortcut Learning|Shortcut Learning]], [[keywords/Hybrid Generative-Discriminative Learning Framework|Hybrid Generative-Discriminative Learning Framework]], [[keywords/Invariance Pre-training Principle|Invariance Pre-training Principle]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11598v3 Announce Type: replace-cross 
Abstract: Despite the remarkable success of Self-Supervised Learning (SSL), its generalization is fundamentally hindered by Shortcut Learning, where models exploit superficial features like texture instead of intrinsic structure. We experimentally verify this flaw within the generative paradigm (e.g., MAE) and argue it is a systemic issue also affecting discriminative methods, identifying it as the root cause of their failure on unseen domains. While existing methods often tackle this at a surface level by aligning or separating domain-specific features, they fail to alter the underlying learning mechanism that fosters shortcut dependency. To address this at its core, we propose HyGDL (Hybrid Generative-Discriminative Learning Framework), a hybrid framework that achieves explicit content-style disentanglement. Our approach is guided by the Invariance Pre-training Principle: forcing a model to learn an invariant essence by systematically varying a bias (e.g., style) at the input while keeping the supervision signal constant. HyGDL operates on a single encoder and analytically defines style as the component of a representation that is orthogonal to its style-invariant content, derived via vector projection. This is operationalized through a synergistic design: (1) a self-distillation objective learns a stable, style-invariant content direction; (2) an analytical projection then decomposes the representation into orthogonal content and style vectors; and (3) a style-conditioned reconstruction objective uses these vectors to restore the image, providing end-to-end supervision. Unlike prior methods that rely on implicit heuristics, this principled disentanglement allows HyGDL to learn truly robust representations, demonstrating superior performance on benchmarks designed to diagnose shortcut learning.

## 📝 요약

이 논문은 자기 지도 학습(SSL)의 일반화 문제를 다루며, 모델이 본질적 구조 대신 표면적 특징을 이용하는 '지름길 학습'이 그 원인임을 지적합니다. 이를 해결하기 위해 HyGDL이라는 하이브리드 생성-판별 학습 프레임워크를 제안합니다. HyGDL은 불변성 사전 학습 원칙을 기반으로 스타일과 콘텐츠를 명시적으로 분리하여 학습합니다. 단일 인코더를 사용하여 스타일을 콘텐츠와 직교하는 벡터로 정의하고, 자기 증류 목표와 스타일 조건 재구성 목표를 통해 스타일-불변 콘텐츠 방향을 학습합니다. 이 방법은 지름길 학습을 진단하는 벤치마크에서 우수한 성능을 보입니다.

## 🎯 주요 포인트

- 1. 자기 지도 학습(SSL)은 지름길 학습으로 인해 일반화에 한계가 있으며, 이는 모델이 본질적인 구조 대신 표면적인 특징을 활용하는 문제입니다.
- 2. 기존 방법들은 도메인 특화된 특징을 정렬하거나 분리하는 데 집중하지만, 지름길 의존성을 조장하는 학습 메커니즘을 근본적으로 바꾸지 못합니다.
- 3. HyGDL은 명시적인 콘텐츠-스타일 분리를 달성하는 하이브리드 생성-판별 학습 프레임워크로, 불변성 사전 학습 원칙에 따라 스타일 편향을 체계적으로 변화시킵니다.
- 4. HyGDL은 단일 인코더를 사용하여 스타일을 스타일 불변 콘텐츠와 직교하는 표현의 구성 요소로 정의하며, 이를 통해 진정으로 강건한 표현을 학습합니다.
- 5. HyGDL은 지름길 학습을 진단하기 위한 벤치마크에서 뛰어난 성능을 보여, 기존의 암시적 휴리스틱에 의존하는 방법들과 차별화됩니다.


---

*Generated on 2025-09-24 03:09:26*