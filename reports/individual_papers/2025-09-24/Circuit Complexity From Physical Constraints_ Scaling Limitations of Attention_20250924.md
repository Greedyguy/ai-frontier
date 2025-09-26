<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:17:24.953798",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Circuit Complexity",
    "Transformer Expressivity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.85,
    "Circuit Complexity": 0.78,
    "Transformer Expressivity": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "attention mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for understanding the scaling limitations discussed in the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "circuit complexity",
        "canonical": "Circuit Complexity",
        "aliases": [
          "complexity of circuits"
        ],
        "category": "unique_technical",
        "rationale": "Circuit complexity is central to the paper's argument about physical constraints.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "transformer expressivity",
        "canonical": "Transformer Expressivity",
        "aliases": [
          "expressivity of transformers"
        ],
        "category": "unique_technical",
        "rationale": "Understanding transformer expressivity is key to evaluating model limitations.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "model expressivity",
      "scaling physical circuits"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "attention mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "circuit complexity",
      "resolved_canonical": "Circuit Complexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "transformer expressivity",
      "resolved_canonical": "Transformer Expressivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Circuit Complexity From Physical Constraints: Scaling Limitations of Attention

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19161.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19161](https://arxiv.org/abs/2509.19161)

## 🔗 유사한 논문
- [[2025-09-23/Towards Interpretable and Efficient Attention_ Compressing All by Contracting a Few_20250923|Towards Interpretable and Efficient Attention: Compressing All by Contracting a Few]] (82.5% similar)
- [[2025-09-22/Hierarchical Self-Attention_ Generalizing Neural Attention Mechanics to Multi-Scale Problems_20250922|Hierarchical Self-Attention: Generalizing Neural Attention Mechanics to Multi-Scale Problems]] (82.3% similar)
- [[2025-09-22/AttentionDrop_ A Novel Regularization Method for Transformer Models_20250922|AttentionDrop: A Novel Regularization Method for Transformer Models]] (80.6% similar)
- [[2025-09-23/Inceptive Transformers_ Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages_20250923|Inceptive Transformers: Enhancing Contextual Representations through Multi-Scale Feature Learning Across Domains and Languages]] (80.1% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Circuit Complexity|Circuit Complexity]], [[keywords/Transformer Expressivity|Transformer Expressivity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19161v1 Announce Type: cross 
Abstract: We argue that the standard circuit complexity measures derived from $NC, AC, TC$ provide limited practical information and are now insufficient to further differentiate model expressivity. To address these new limitations, we define a novel notion of local uniformity and a family of circuit complexity classes $RC(\cdot)$ that capture the fundamental constraints of scaling physical circuits. Through the lens of $RC(\cdot)$, we show that attention mechanisms with $\omega(n^{3/2})$ runtime cannot scale to accommodate the entropy of increasingly complex datasets. Our results simultaneously provide a methodology for defining meaningful bounds on transformer expressivity and naturally expose the restricted viability of attention.

## 📝 요약

이 논문은 기존의 회로 복잡도 측정 방법($NC, AC, TC$)이 모델의 표현력을 구별하는 데 한계가 있음을 지적합니다. 이를 해결하기 위해 새로운 지역적 균일성 개념과 $RC(\cdot)$라는 회로 복잡도 클래스 가족을 정의합니다. $RC(\cdot)$를 통해 $\omega(n^{3/2})$ 실행 시간을 갖는 어텐션 메커니즘이 복잡한 데이터셋의 엔트로피를 처리할 수 없음을 보여줍니다. 이 연구는 트랜스포머의 표현력에 대한 유의미한 경계를 정의하는 방법론을 제공하며, 어텐션의 제한된 가능성을 자연스럽게 드러냅니다.

## 🎯 주요 포인트

- 1. 기존의 회로 복잡도 측정 방법인 $NC, AC, TC$는 모델의 표현력을 구분하는 데 한계가 있다.
- 2. 새로운 개념인 지역적 균일성(local uniformity)과 회로 복잡도 클래스 $RC(\cdot)$를 정의하여 물리적 회로의 확장 제약을 포착한다.
- 3. $RC(\cdot)$를 통해 $\omega(n^{3/2})$ 런타임을 가진 주의 메커니즘(attention mechanisms)은 복잡한 데이터셋의 엔트로피를 처리할 수 없음을 보인다.
- 4. 연구 결과는 트랜스포머의 표현력에 대한 의미 있는 경계를 정의하는 방법론을 제공한다.
- 5. 주의 메커니즘의 제한된 실행 가능성을 자연스럽게 드러낸다.


---

*Generated on 2025-09-24 15:17:24*