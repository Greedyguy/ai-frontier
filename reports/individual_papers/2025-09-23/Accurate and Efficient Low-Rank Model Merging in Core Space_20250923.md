---
keywords:
  - Low-Rank Adaptation
  - Core Space Merging
  - Computer Vision
  - Natural Language Processing
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17786
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:09:38.219018",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Rank Adaptation",
    "Core Space Merging",
    "Computer Vision",
    "Natural Language Processing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-Rank Adaptation": 0.85,
    "Core Space Merging": 0.88,
    "Computer Vision": 0.78,
    "Natural Language Processing": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "specific_connectable",
        "rationale": "Low-Rank Adaptation is crucial for understanding parameter-efficient techniques in neural networks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Core Space",
        "canonical": "Core Space Merging",
        "aliases": [
          "Core Space"
        ],
        "category": "unique_technical",
        "rationale": "Core Space Merging is a novel framework proposed in the paper, offering significant improvements in model merging.",
        "novelty_score": 0.9,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Vision Tasks",
        "canonical": "Computer Vision",
        "aliases": [
          "Vision Tasks"
        ],
        "category": "broad_technical",
        "rationale": "Computer Vision is a key application area for the proposed merging framework, enhancing its relevance.",
        "novelty_score": 0.4,
        "connectivity_score": 0.92,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Language Tasks",
        "canonical": "Natural Language Processing",
        "aliases": [
          "Language Tasks"
        ],
        "category": "broad_technical",
        "rationale": "Natural Language Processing is another critical domain where the framework shows state-of-the-art results.",
        "novelty_score": 0.42,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "parameter-efficient",
      "model fine-tuning",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Core Space",
      "resolved_canonical": "Core Space Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Vision Tasks",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.92,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Language Tasks",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.42,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Accurate and Efficient Low-Rank Model Merging in Core Space

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17786.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17786](https://arxiv.org/abs/2509.17786)

## 🔗 유사한 논문
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (84.7% similar)
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (82.9% similar)
- [[2025-09-18/FroM_ Frobenius Norm-Based Data-Free Adaptive Model Merging_20250918|FroM: Frobenius Norm-Based Data-Free Adaptive Model Merging]] (81.8% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (81.4% similar)
- [[2025-09-18/Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]], [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]]
**⚡ Unique Technical**: [[keywords/Core Space Merging|Core Space Merging]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17786v1 Announce Type: cross 
Abstract: In this paper, we address the challenges associated with merging low-rank adaptations of large neural networks. With the rise of parameter-efficient adaptation techniques, such as Low-Rank Adaptation (LoRA), model fine-tuning has become more accessible. While fine-tuning models with LoRA is highly efficient, existing merging methods often sacrifice this efficiency by merging fully-sized weight matrices. We propose the Core Space merging framework, which enables the merging of LoRA-adapted models within a common alignment basis, thereby preserving the efficiency of low-rank adaptation while substantially improving accuracy across tasks. We further provide a formal proof that projection into Core Space ensures no loss of information and provide a complexity analysis showing the efficiency gains. Extensive empirical results demonstrate that Core Space significantly improves existing merging techniques and achieves state-of-the-art results on both vision and language tasks while utilizing a fraction of the computational resources. Codebase is available at https://github.com/apanariello4/core-space-merging.

## 📝 요약

이 논문은 대형 신경망의 저랭크 적응을 병합하는 데 있어 발생하는 문제를 다룹니다. 저랭크 적응(LoRA) 기법은 모델의 파라미터 효율성을 높여주지만, 기존 병합 방법은 전체 가중치 행렬을 병합하여 효율성을 저하시킵니다. 이를 해결하기 위해, 저자들은 Core Space 병합 프레임워크를 제안하여 공통 정렬 기반에서 LoRA 적응 모델을 병합함으로써 효율성을 유지하면서도 정확성을 크게 향상시킵니다. 또한, Core Space로의 투영이 정보 손실을 초래하지 않음을 증명하고, 복잡도 분석을 통해 효율성 향상을 입증합니다. 실험 결과, Core Space는 기존 병합 기법을 크게 개선하며, 적은 계산 자원으로도 비전 및 언어 작업에서 최첨단 성능을 달성합니다. 코드베이스는 https://github.com/apanariello4/core-space-merging에서 제공됩니다.

## 🎯 주요 포인트

- 1. Core Space 병합 프레임워크는 LoRA로 적응된 모델을 공통 정렬 기준 내에서 병합하여 효율성을 유지하면서 정확성을 크게 향상시킵니다.
- 2. Core Space로의 투영이 정보 손실을 방지한다는 공식적인 증명을 제공하며, 복잡도 분석을 통해 효율성 향상을 입증합니다.
- 3. 광범위한 실험 결과, Core Space는 기존 병합 기법을 크게 개선하고, 적은 계산 자원으로도 비전 및 언어 작업에서 최첨단 결과를 달성합니다.
- 4. LoRA를 활용한 모델 미세 조정은 매우 효율적이지만, 기존 병합 방법은 완전 크기의 가중치 행렬을 병합하여 이 효율성을 희생하는 경우가 많습니다.
- 5. Core Space 병합 프레임워크의 코드베이스는 https://github.com/apanariello4/core-space-merging에서 제공됩니다.


---

*Generated on 2025-09-24 00:09:38*