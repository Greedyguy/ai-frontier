---
keywords:
  - Chain-of-Reaction
  - ReaSyn
  - Reinforcement Learning
  - Synthesizable Projection
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16084
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:42:29.334519",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Chain-of-Reaction",
    "ReaSyn",
    "Reinforcement Learning",
    "Synthesizable Projection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Chain-of-Reaction": 0.78,
    "ReaSyn": 0.8,
    "Reinforcement Learning": 0.75,
    "Synthesizable Projection": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Chain-of-Reaction",
        "canonical": "Chain-of-Reaction",
        "aliases": [
          "CoR"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept analogous to chain-of-thought reasoning, enhancing understanding of chemical pathways.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "ReaSyn",
        "canonical": "ReaSyn",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a new framework specifically designed for synthesizable molecule generation, crucial for linking advancements in chemical synthesis.",
        "novelty_score": 0.88,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "A key method used in the framework to enhance reasoning capability, linking it to broader machine learning techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Synthesizable Projection",
        "canonical": "Synthesizable Projection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific process within ReaSyn that is central to achieving its goal, providing a unique link to chemical synthesis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "molecular generative models",
      "synthetic pathways",
      "goal-directed test-time compute scaling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Chain-of-Reaction",
      "resolved_canonical": "Chain-of-Reaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ReaSyn",
      "resolved_canonical": "ReaSyn",
      "decision": "linked",
      "scores": {
        "novelty": 0.88,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Synthesizable Projection",
      "resolved_canonical": "Synthesizable Projection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Rethinking Molecule Synthesizability with Chain-of-Reaction

**Korean Title:** 반응 사슬을 통한 분자 합성 가능성 재고

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16084.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16084](https://arxiv.org/abs/2509.16084)

## 🔗 유사한 논문
- [[2025-09-22/FragmentRetro_ A Quadratic Retrosynthetic Method Based on Fragmentation Algorithms_20250922|FragmentRetro: A Quadratic Retrosynthetic Method Based on Fragmentation Algorithms]] (81.7% similar)
- [[2025-09-22/DeepMech_ A Machine Learning Framework for Chemical Reaction Mechanism Prediction_20250922|DeepMech: A Machine Learning Framework for Chemical Reaction Mechanism Prediction]] (81.5% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery: Reinforced Distillation of Large Language Model Agents]] (80.3% similar)
- [[2025-09-22/ConCISE_ Confidence-guided Compression in Step-by-step Efficient Reasoning_20250922|ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning]] (79.6% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Chain-of-Reaction|Chain-of-Reaction]], [[keywords/ReaSyn|ReaSyn]], [[keywords/Synthesizable Projection|Synthesizable Projection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16084v1 Announce Type: new 
Abstract: A well-known pitfall of molecular generative models is that they are not guaranteed to generate synthesizable molecules. There have been considerable attempts to address this problem, but given the exponentially large combinatorial space of synthesizable molecules, existing methods have shown limited coverage of the space and poor molecular optimization performance. To tackle these problems, we introduce ReaSyn, a generative framework for synthesizable projection where the model explores the neighborhood of given molecules in the synthesizable space by generating pathways that result in synthesizable analogs. To fully utilize the chemical knowledge contained in the synthetic pathways, we propose a novel perspective that views synthetic pathways akin to reasoning paths in large language models (LLMs). Specifically, inspired by chain-of-thought (CoT) reasoning in LLMs, we introduce the chain-of-reaction (CoR) notation that explicitly states reactants, reaction types, and intermediate products for each step in a pathway. With the CoR notation, ReaSyn can get dense supervision in every reaction step to explicitly learn chemical reaction rules during supervised training and perform step-by-step reasoning. In addition, to further enhance the reasoning capability of ReaSyn, we propose reinforcement learning (RL)-based finetuning and goal-directed test-time compute scaling tailored for synthesizable projection. ReaSyn achieves the highest reconstruction rate and pathway diversity in synthesizable molecule reconstruction and the highest optimization performance in synthesizable goal-directed molecular optimization, and significantly outperforms previous synthesizable projection methods in synthesizable hit expansion. These results highlight ReaSyn's superior ability to navigate combinatorially-large synthesizable chemical space.

## 🔍 Abstract (한글 번역)

arXiv:2509.16084v1 발표 유형: 신규  
초록: 분자 생성 모델의 잘 알려진 함정 중 하나는 합성 가능한 분자를 생성할 보장이 없다는 것입니다. 이 문제를 해결하기 위한 상당한 시도가 있었지만, 합성 가능한 분자의 지수적으로 큰 조합 공간을 고려할 때 기존 방법들은 공간의 제한된 커버리지와 낮은 분자 최적화 성능을 보여주었습니다. 이러한 문제를 해결하기 위해, 우리는 합성 가능한 투영을 위한 생성 프레임워크인 ReaSyn을 소개합니다. 이 모델은 합성 가능한 공간에서 주어진 분자의 이웃을 탐색하여 합성 가능한 유사체를 생성하는 경로를 생성합니다. 합성 경로에 포함된 화학 지식을 완전히 활용하기 위해, 우리는 합성 경로를 대형 언어 모델(LLMs)에서의 추론 경로와 유사하게 보는 새로운 관점을 제안합니다. 구체적으로, LLMs에서의 사고의 흐름(Chain-of-Thought, CoT) 추론에서 영감을 받아, 우리는 경로의 각 단계에서 반응물, 반응 유형 및 중간 생성물을 명시적으로 나타내는 반응의 흐름(Chain-of-Reaction, CoR) 표기법을 도입합니다. CoR 표기법을 통해 ReaSyn은 감독 학습 동안 화학 반응 규칙을 명시적으로 학습하고 단계별 추론을 수행하기 위해 각 반응 단계에서 밀도 높은 감독을 받을 수 있습니다. 또한, ReaSyn의 추론 능력을 더욱 향상시키기 위해, 우리는 합성 가능한 투영에 맞춘 강화 학습(RL) 기반의 미세 조정과 목표 지향적 테스트 시간 계산 확장을 제안합니다. ReaSyn은 합성 가능한 분자 재구성에서 가장 높은 재구성률과 경로 다양성을 달성하고, 합성 가능한 목표 지향적 분자 최적화에서 가장 높은 최적화 성능을 보여주며, 합성 가능한 히트 확장에서 이전의 합성 가능한 투영 방법을 현저히 능가합니다. 이러한 결과는 조합적으로 큰 합성 가능한 화학 공간을 탐색하는 ReaSyn의 뛰어난 능력을 강조합니다.

## 📝 요약

ReaSyn은 합성 가능한 분자를 생성하는 데 중점을 둔 새로운 생성 프레임워크로, 기존 모델의 한계를 극복하고자 합니다. 이 모델은 주어진 분자의 합성 가능한 공간 내 이웃을 탐색하여 합성 가능한 유사체를 생성하는 경로를 만듭니다. ReaSyn은 합성 경로를 대형 언어 모델의 추론 경로와 유사하게 보고, 반응물, 반응 유형, 중간 생성물을 명시하는 '반응의 연쇄(CoR)' 표기법을 도입하여 각 단계에서 화학 반응 규칙을 학습합니다. 또한, 강화 학습 기반의 미세 조정과 목표 지향적 테스트 시간 계산 확장을 통해 합성 가능한 투영을 최적화합니다. ReaSyn은 합성 가능한 분자 재구성과 목표 지향적 분자 최적화에서 높은 성과를 보이며, 기존 방법보다 뛰어난 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. 분자 생성 모델의 한계인 합성 가능한 분자의 생성 보장을 해결하기 위해 ReaSyn이라는 새로운 생성 프레임워크를 제안합니다.
- 2. ReaSyn은 합성 경로를 통해 합성 가능한 유사체를 생성하며, 이는 대형 언어 모델의 추론 경로와 유사한 방식으로 작동합니다.
- 3. CoR 표기법을 도입하여 각 반응 단계에서 반응물, 반응 유형, 중간 생성물을 명시적으로 기술하고, 이를 통해 화학 반응 규칙을 학습합니다.
- 4. ReaSyn은 강화 학습 기반 미세 조정과 목표 지향적 테스트 시점 계산 확장을 통해 합성 가능한 투영의 추론 능력을 향상시킵니다.
- 5. ReaSyn은 합성 가능한 분자 재구성과 목표 지향적 분자 최적화에서 최고 성능을 보이며, 기존 방법을 능가하는 결과를 보여줍니다.


---

*Generated on 2025-09-23 10:42:29*