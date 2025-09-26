---
keywords:
  - Transformer
  - Vision-Language Model
  - Visual Robustness Learning
  - Visual Instruction Pretraining
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17562
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:55:16.945616",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Vision-Language Model",
    "Visual Robustness Learning",
    "Visual Instruction Pretraining"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Vision-Language Model": 0.9,
    "Visual Robustness Learning": 0.8,
    "Visual Instruction Pretraining": 0.85
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
        "rationale": "Transformers are a foundational technology in modern machine learning, and linking to them helps connect various related concepts.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are increasingly important in multimodal learning, connecting vision and language processing.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Visual Robustness Learning",
        "canonical": "Visual Robustness Learning",
        "aliases": [
          "VRL"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, enhancing the robustness of visual models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Visual Instruction Pretraining",
        "canonical": "Visual Instruction Pretraining",
        "aliases": [
          "ViTP"
        ],
        "category": "unique_technical",
        "rationale": "This is a new pretraining paradigm proposed in the paper, crucial for understanding the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "perception",
      "reasoning",
      "generation",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Visual Robustness Learning",
      "resolved_canonical": "Visual Robustness Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Visual Instruction Pretraining",
      "resolved_canonical": "Visual Instruction Pretraining",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Visual Instruction Pretraining for Domain-Specific Foundation Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17562.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17562](https://arxiv.org/abs/2509.17562)

## 🔗 유사한 논문
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (84.8% similar)
- [[2025-09-23/Agentic Reasoning for Robust Vision Systems via Increased Test-Time Compute_20250923|Agentic Reasoning for Robust Vision Systems via Increased Test-Time Compute]] (84.8% similar)
- [[2025-09-22/Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks_20250922|Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks]] (83.8% similar)
- [[2025-09-23/Interpreting vision transformers via residual replacement model_20250923|Interpreting vision transformers via residual replacement model]] (83.7% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Visual Robustness Learning|Visual Robustness Learning]], [[keywords/Visual Instruction Pretraining|Visual Instruction Pretraining]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17562v1 Announce Type: new 
Abstract: Modern computer vision is converging on a closed loop in which perception, reasoning and generation mutually reinforce each other. However, this loop remains incomplete: the top-down influence of high-level reasoning on the foundational learning of low-level perceptual features is not yet underexplored. This paper addresses this gap by proposing a new paradigm for pretraining foundation models in downstream domains. We introduce Visual insTruction Pretraining (ViTP), a novel approach that directly leverages reasoning to enhance perception. ViTP embeds a Vision Transformer (ViT) backbone within a Vision-Language Model and pretrains it end-to-end using a rich corpus of visual instruction data curated from target downstream domains. ViTP is powered by our proposed Visual Robustness Learning (VRL), which compels the ViT to learn robust and domain-relevant features from a sparse set of visual tokens. Extensive experiments on 16 challenging remote sensing and medical imaging benchmarks demonstrate that ViTP establishes new state-of-the-art performance across a diverse range of downstream tasks. The code is available at github.com/zcablii/ViTP.

## 📝 요약

이 논문은 고차원적 추론이 저차원적 지각 특징 학습에 미치는 영향을 탐구하지 않은 기존의 한계를 극복하고자, 새로운 사전 학습 패러다임인 Visual insTruction Pretraining (ViTP)을 제안합니다. ViTP는 Vision Transformer (ViT)를 비전-언어 모델에 내장하고, 목표 도메인에서 수집한 시각적 지시 데이터를 활용해 종단 간 사전 학습을 수행합니다. 특히, ViTP는 제안된 Visual Robustness Learning (VRL)을 통해 ViT가 도메인 관련 특징을 학습하도록 유도합니다. 16개의 원격 감지 및 의료 영상 벤치마크 실험에서 ViTP는 다양한 다운스트림 작업에서 최신 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 현대 컴퓨터 비전은 인식, 추론, 생성이 서로 강화하는 폐쇄 루프에 수렴하고 있지만, 고차원 추론이 저차원 인식 특징 학습에 미치는 영향은 아직 충분히 탐구되지 않았다.
- 2. ViTP(Visual insTruction Pretraining)는 고차원 추론을 통해 인식을 향상시키는 새로운 사전 학습 패러다임을 제안한다.
- 3. ViTP는 Vision Transformer(ViT) 백본을 비전-언어 모델에 내장하고, 목표 하위 도메인에서 수집한 시각적 지시 데이터로 종단 간 사전 학습을 수행한다.
- 4. ViTP는 제안된 Visual Robustness Learning(VRL)을 통해 소수의 시각적 토큰으로부터 견고하고 도메인 관련 특징을 학습하도록 한다.
- 5. ViTP는 16개의 원격 감지 및 의료 영상 벤치마크에서 새로운 최첨단 성능을 달성했으며, 다양한 하위 작업에서 우수한 성과를 보였다.


---

*Generated on 2025-09-24 04:55:16*