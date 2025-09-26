<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:03:02.280185",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Natural Language Processing",
    "Inter-firm Risk Relations",
    "Form 10-K Filings",
    "Unsupervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Natural Language Processing": 0.88,
    "Inter-firm Risk Relations": 0.8,
    "Form 10-K Filings": 0.75,
    "Unsupervised Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "This is a key technology used in the proposed method, linking it to a wide range of related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "inter-firm risk relations",
        "canonical": "Inter-firm Risk Relations",
        "aliases": [
          "corporate risk connections"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, this term describes the specific risk connections being analyzed.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Form 10-K filings",
        "canonical": "Form 10-K Filings",
        "aliases": [
          "10-K reports"
        ],
        "category": "unique_technical",
        "rationale": "These documents are the primary data source for the method, linking to financial document analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "unsupervised fine-tuning",
        "canonical": "Unsupervised Learning",
        "aliases": [
          "unsupervised adaptation"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for adapting models to new data without labeled examples, enhancing connectivity to machine learning methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "inter-firm risk relations",
      "resolved_canonical": "Inter-firm Risk Relations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Form 10-K filings",
      "resolved_canonical": "Form 10-K Filings",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "unsupervised fine-tuning",
      "resolved_canonical": "Unsupervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Financial Risk Relation Identification through Dual-view Adaptation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18775.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18775](https://arxiv.org/abs/2509.18775)

## 🔗 유사한 논문
- [[2025-09-23/Robust Reinforcement Learning with Dynamic Distortion Risk Measures_20250923|Robust Reinforcement Learning with Dynamic Distortion Risk Measures]] (79.1% similar)
- [[2025-09-23/Enhancing Financial RAG with Agentic AI and Multi-HyDE_ A Novel Approach to Knowledge Retrieval and Hallucination Reduction_20250923|Enhancing Financial RAG with Agentic AI and Multi-HyDE: A Novel Approach to Knowledge Retrieval and Hallucination Reduction]] (78.9% similar)
- [[2025-09-23/Adaptive Graph Convolution and Semantic-Guided Attention for Multimodal Risk Detection in Social Networks_20250923|Adaptive Graph Convolution and Semantic-Guided Attention for Multimodal Risk Detection in Social Networks]] (78.6% similar)
- [[2025-09-23/Intrinsic Meets Extrinsic Fairness_ Assessing the Downstream Impact of Bias Mitigation in Large Language Models_20250923|Intrinsic Meets Extrinsic Fairness: Assessing the Downstream Impact of Bias Mitigation in Large Language Models]] (78.3% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Unsupervised Learning|Unsupervised Learning]]
**⚡ Unique Technical**: [[keywords/Inter-firm Risk Relations|Inter-firm Risk Relations]], [[keywords/Form 10-K Filings|Form 10-K Filings]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18775v1 Announce Type: cross 
Abstract: A multitude of interconnected risk events -- ranging from regulatory changes to geopolitical tensions -- can trigger ripple effects across firms. Identifying inter-firm risk relations is thus crucial for applications like portfolio management and investment strategy. Traditionally, such assessments rely on expert judgment and manual analysis, which are, however, subjective, labor-intensive, and difficult to scale. To address this, we propose a systematic method for extracting inter-firm risk relations using Form 10-K filings -- authoritative, standardized financial documents -- as our data source. Leveraging recent advances in natural language processing, our approach captures implicit and abstract risk connections through unsupervised fine-tuning based on chronological and lexical patterns in the filings. This enables the development of a domain-specific financial encoder with a deeper contextual understanding and introduces a quantitative risk relation score for transparency, interpretable analysis. Extensive experiments demonstrate that our method outperforms strong baselines across multiple evaluation settings.

## 📝 요약

이 논문은 기업 간 리스크 관계를 식별하기 위한 체계적인 방법을 제안합니다. 전통적으로 전문가의 판단과 수작업 분석에 의존하던 것을 개선하기 위해, 연구진은 Form 10-K 보고서를 데이터 소스로 활용하여 자연어 처리 기술을 적용했습니다. 이 방법은 보고서의 시간적 및 어휘적 패턴을 기반으로 비지도 학습을 통해 암묵적이고 추상적인 리스크 연결을 포착합니다. 이를 통해 도메인 특화된 금융 인코더를 개발하고, 투명하고 해석 가능한 정량적 리스크 관계 점수를 도입했습니다. 실험 결과, 제안된 방법이 여러 평가 환경에서 기존의 강력한 기준선을 능가함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기업 간의 리스크 관계를 식별하는 것은 포트폴리오 관리 및 투자 전략에 중요하다.
- 2. 기존의 리스크 평가 방법은 주관적이고 노동 집약적이며 확장하기 어렵다.
- 3. Form 10-K 서류를 활용하여 기업 간 리스크 관계를 체계적으로 추출하는 방법을 제안한다.
- 4. 자연어 처리 기술을 활용하여 암시적이고 추상적인 리스크 연결을 포착한다.
- 5. 제안된 방법은 여러 평가 설정에서 기존의 강력한 기준을 능가하는 성능을 보인다.


---

*Generated on 2025-09-24 14:03:02*