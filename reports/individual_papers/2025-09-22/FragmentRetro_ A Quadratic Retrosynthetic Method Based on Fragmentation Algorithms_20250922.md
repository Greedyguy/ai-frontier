---
keywords:
  - FragmentRetro
  - Retrosynthesis
  - BRICS Fragmentation
  - Pattern Fingerprint Screening
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15409
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:41:19.822106",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "FragmentRetro",
    "Retrosynthesis",
    "BRICS Fragmentation",
    "Pattern Fingerprint Screening"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "FragmentRetro": 0.85,
    "Retrosynthesis": 0.7,
    "BRICS Fragmentation": 0.78,
    "Pattern Fingerprint Screening": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FragmentRetro",
        "canonical": "FragmentRetro",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "FragmentRetro is a novel method specific to this paper, offering a unique approach to retrosynthesis with quadratic complexity.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "retrosynthesis",
        "canonical": "Retrosynthesis",
        "aliases": [
          "retrosynthetic analysis"
        ],
        "category": "broad_technical",
        "rationale": "Retrosynthesis is a fundamental concept in chemistry that connects various synthesis planning methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "BRICS",
        "canonical": "BRICS Fragmentation",
        "aliases": [
          "BRICS algorithm"
        ],
        "category": "specific_connectable",
        "rationale": "BRICS is a key fragmentation algorithm used in the paper, crucial for understanding the method's approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "pattern fingerprint screening",
        "canonical": "Pattern Fingerprint Screening",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is essential for reducing complexity in FragmentRetro, making it a unique contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "process",
      "solution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "FragmentRetro",
      "resolved_canonical": "FragmentRetro",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "retrosynthesis",
      "resolved_canonical": "Retrosynthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "BRICS",
      "resolved_canonical": "BRICS Fragmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "pattern fingerprint screening",
      "resolved_canonical": "Pattern Fingerprint Screening",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# FragmentRetro: A Quadratic Retrosynthetic Method Based on Fragmentation Algorithms

**Korean Title:** FragmentRetro: 분할 알고리즘에 기반한 이차적 역합성 방법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15409.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15409](https://arxiv.org/abs/2509.15409)

## 🔗 유사한 논문
- [[2025-09-22/Rethinking Molecule Synthesizability with Chain-of-Reaction_20250922|Rethinking Molecule Synthesizability with Chain-of-Reaction]] (81.7% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (78.0% similar)
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (77.2% similar)
- [[2025-09-22/DeepMech_ A Machine Learning Framework for Chemical Reaction Mechanism Prediction_20250922|DeepMech: A Machine Learning Framework for Chemical Reaction Mechanism Prediction]] (77.0% similar)
- [[2025-09-22/Monte Carlo Tree Diffusion with Multiple Experts for Protein Design_20250922|Monte Carlo Tree Diffusion with Multiple Experts for Protein Design]] (76.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Retrosynthesis|Retrosynthesis]]
**🔗 Specific Connectable**: [[keywords/BRICS Fragmentation|BRICS Fragmentation]]
**⚡ Unique Technical**: [[keywords/FragmentRetro|FragmentRetro]], [[keywords/Pattern Fingerprint Screening|Pattern Fingerprint Screening]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15409v1 Announce Type: new 
Abstract: Retrosynthesis, the process of deconstructing a target molecule into simpler precursors, is crucial for computer-aided synthesis planning (CASP). Widely adopted tree-search methods often suffer from exponential computational complexity. In this work, we introduce FragmentRetro, a novel retrosynthetic method that leverages fragmentation algorithms, specifically BRICS and r-BRICS, combined with stock-aware exploration and pattern fingerprint screening to achieve quadratic complexity. FragmentRetro recursively combines molecular fragments and verifies their presence in a building block set, providing sets of fragment combinations as retrosynthetic solutions. We present the first formal computational analysis of retrosynthetic methods, showing that tree search exhibits exponential complexity $O(b^h)$, DirectMultiStep scales as $O(h^6)$, and FragmentRetro achieves $O(h^2)$, where $h$ represents the number of heavy atoms in the target molecule and $b$ is the branching factor for tree search. Evaluations on PaRoutes, USPTO-190, and natural products demonstrate that FragmentRetro achieves high solved rates with competitive runtime, including cases where tree search fails. The method benefits from fingerprint screening, which significantly reduces substructure matching complexity. While FragmentRetro focuses on efficiently identifying fragment-based solutions rather than full reaction pathways, its computational advantages and ability to generate strategic starting candidates establish it as a powerful foundational component for scalable and automated synthesis planning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15409v1 발표 유형: 신규  
초록: 레트로신테시스는 목표 분자를 더 간단한 전구체로 분해하는 과정으로, 컴퓨터 지원 합성 계획(CASP)에 필수적입니다. 널리 채택된 트리 탐색 방법은 종종 지수적 계산 복잡성을 겪습니다. 이 연구에서는 BRICS 및 r-BRICS와 같은 분할 알고리즘을 활용하고, 재고 인식 탐색 및 패턴 지문 스크리닝과 결합하여 이차 복잡성을 달성하는 새로운 레트로신테시스 방법인 FragmentRetro를 소개합니다. FragmentRetro는 분자 조각을 재귀적으로 결합하고, 이들이 빌딩 블록 세트에 존재하는지를 확인하여 조각 조합 세트를 레트로신테시스 솔루션으로 제공합니다. 우리는 레트로신테시스 방법의 첫 번째 공식 계산 분석을 제시하며, 트리 탐색이 지수적 복잡성 $O(b^h)$를 나타내고, DirectMultiStep이 $O(h^6)$로 확장되며, FragmentRetro가 $O(h^2)$를 달성함을 보여줍니다. 여기서 $h$는 목표 분자의 무거운 원자 수를 나타내고, $b$는 트리 탐색의 분기 계수입니다. PaRoutes, USPTO-190 및 천연물에 대한 평가에서 FragmentRetro는 트리 탐색이 실패하는 경우를 포함하여 경쟁력 있는 실행 시간과 높은 해결률을 달성합니다. 이 방법은 지문 스크리닝 덕분에 부분 구조 매칭 복잡성을 크게 줄입니다. FragmentRetro는 전체 반응 경로보다는 조각 기반 솔루션을 효율적으로 식별하는 데 중점을 두지만, 그 계산상의 이점과 전략적 시작 후보를 생성하는 능력은 확장 가능하고 자동화된 합성 계획을 위한 강력한 기초 구성 요소로서의 위치를 확립합니다.

## 📝 요약

이 논문은 복잡한 분자를 더 간단한 전구체로 분해하는 과정인 역합성 계획에서의 새로운 방법론인 FragmentRetro를 소개합니다. 기존의 트리 탐색 방법은 계산 복잡도가 지수적으로 증가하는 문제를 가지고 있지만, FragmentRetro는 BRICS와 r-BRICS 분할 알고리즘을 활용하여 이 문제를 해결하고 있습니다. 이 방법은 분자 조각을 재귀적으로 결합하고, 조각 조합을 검증하여 역합성 솔루션을 제공합니다. FragmentRetro는 목표 분자의 무거운 원자 수에 따라 계산 복잡도를 $O(h^2)$로 줄이며, 이는 기존 트리 탐색의 $O(b^h)$보다 효율적입니다. PaRoutes, USPTO-190, 천연물 데이터셋 평가에서 높은 해결률과 경쟁력 있는 실행 시간을 보였으며, 트리 탐색이 실패하는 경우에도 성능을 발휘합니다. 이 방법은 전체 반응 경로보다는 조각 기반 솔루션을 효율적으로 식별하는 데 중점을 두며, 자동화된 합성 계획의 기초 구성 요소로서의 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. FragmentRetro는 BRICS와 r-BRICS 분할 알고리즘을 활용하여 이차 복잡성을 달성하는 새로운 레트로 합성 방법입니다.
- 2. FragmentRetro는 분자 조각을 재귀적으로 결합하고, 이를 빌딩 블록 세트에서 확인하여 레트로 합성 솔루션을 제공합니다.
- 3. FragmentRetro는 트리 검색의 지수 복잡성을 피하고, $O(h^2)$의 복잡성을 달성하여 효율적인 합성 계획을 가능하게 합니다.
- 4. PaRoutes, USPTO-190, 및 천연물에 대한 평가에서 FragmentRetro는 높은 해결률과 경쟁력 있는 실행 시간을 보여줍니다.
- 5. FragmentRetro는 전체 반응 경로보다는 조각 기반 솔루션을 효율적으로 식별하는 데 중점을 두며, 자동화된 합성 계획의 강력한 기초 구성 요소로 자리 잡습니다.


---

*Generated on 2025-09-23 08:41:19*