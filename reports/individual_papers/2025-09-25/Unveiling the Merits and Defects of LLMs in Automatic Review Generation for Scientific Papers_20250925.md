---
keywords:
  - Large Language Model
  - Semantic Similarity Analysis
  - Knowledge Graph Metrics
  - Automated Review Generation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19326
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:23:58.059366",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Semantic Similarity Analysis",
    "Knowledge Graph Metrics",
    "Automated Review Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Semantic Similarity Analysis": 0.78,
    "Knowledge Graph Metrics": 0.8,
    "Automated Review Generation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on automated review generation, linking to existing work on LLMs.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Semantic Similarity Analysis",
        "canonical": "Semantic Similarity Analysis",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key component of the proposed evaluation framework, offering a unique angle for linking.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Structured Knowledge Graph Metrics",
        "canonical": "Knowledge Graph Metrics",
        "aliases": [
          "Structured Knowledge Graph"
        ],
        "category": "specific_connectable",
        "rationale": "Provides a structured approach to evaluate LLMs, connecting to broader knowledge graph research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Automated Review Generation",
        "canonical": "Automated Review Generation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Core application of LLMs in the paper, facilitating connections to similar automation studies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "peer-review process",
      "human-written counterparts",
      "ICLR",
      "NeurIPS"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Semantic Similarity Analysis",
      "resolved_canonical": "Semantic Similarity Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Structured Knowledge Graph Metrics",
      "resolved_canonical": "Knowledge Graph Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Automated Review Generation",
      "resolved_canonical": "Automated Review Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19326.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19326](https://arxiv.org/abs/2509.19326)

## 🔗 유사한 논문
- [[2025-09-23/Breaking the Reviewer_ Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks_20250923|Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks]] (90.7% similar)
- [[2025-09-23/Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues_20250923|Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues]] (88.9% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (88.4% similar)
- [[2025-09-23/Challenging the Evaluator_ LLM Sycophancy Under User Rebuttal_20250923|Challenging the Evaluator: LLM Sycophancy Under User Rebuttal]] (87.7% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (87.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Knowledge Graph Metrics|Knowledge Graph Metrics]]
**⚡ Unique Technical**: [[keywords/Semantic Similarity Analysis|Semantic Similarity Analysis]], [[keywords/Automated Review Generation|Automated Review Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19326v1 Announce Type: cross 
Abstract: The surge in scientific submissions has placed increasing strain on the traditional peer-review process, prompting the exploration of large language models (LLMs) for automated review generation. While LLMs demonstrate competence in producing structured and coherent feedback, their capacity for critical reasoning, contextual grounding, and quality sensitivity remains limited. To systematically evaluate these aspects, we propose a comprehensive evaluation framework that integrates semantic similarity analysis and structured knowledge graph metrics to assess LLM-generated reviews against human-written counterparts. We construct a large-scale benchmark of 1,683 papers and 6,495 expert reviews from ICLR and NeurIPS in multiple years, and generate reviews using five LLMs. Our findings show that LLMs perform well in descriptive and affirmational content, capturing the main contributions and methodologies of the original work, with GPT-4o highlighted as an illustrative example, generating 15.74% more entities than human reviewers in the strengths section of good papers in ICLR 2025. However, they consistently underperform in identifying weaknesses, raising substantive questions, and adjusting feedback based on paper quality. GPT-4o produces 59.42% fewer entities than real reviewers in the weaknesses and increases node count by only 5.7% from good to weak papers, compared to 50% in human reviews. Similar trends are observed across all conferences, years, and models, providing empirical foundations for understanding the merits and defects of LLM-generated reviews and informing the development of future LLM-assisted reviewing tools. Data, code, and more detailed results are publicly available at https://github.com/RichardLRC/Peer-Review.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용한 자동 리뷰 생성의 가능성을 탐구합니다. 전통적인 동료 평가 과정의 부담을 덜기 위해 LLM의 활용이 제안되었지만, 비판적 사고와 맥락적 이해, 품질 감수성에서 한계가 있습니다. 이를 평가하기 위해, 저자들은 LLM이 생성한 리뷰와 인간 리뷰를 비교하는 평가 프레임워크를 제안했습니다. ICLR과 NeurIPS의 1,683개 논문과 6,495개의 전문가 리뷰를 바탕으로 LLM 리뷰를 생성한 결과, LLM은 주로 기술적 내용과 긍정적 피드백에서 우수한 성과를 보였으나, 약점 식별과 비판적 질문 제기에서는 부족함을 드러냈습니다. 특히, GPT-4o는 강점 부분에서 인간 리뷰어보다 더 많은 엔티티를 생성했지만, 약점 식별에서는 부족했습니다. 이러한 결과는 LLM 기반 리뷰 도구 개발에 중요한 통찰을 제공합니다. 데이터와 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 과학 논문 제출 증가로 전통적인 동료 평가 과정에 부담이 가중되면서 대형 언어 모델(LLMs)을 활용한 자동 리뷰 생성이 탐구되고 있다.
- 2. LLMs는 구조적이고 일관된 피드백을 생성하는 데 능숙하지만, 비판적 사고, 맥락적 기반, 품질 민감도에서는 한계가 있다.
- 3. LLMs는 논문의 주요 기여와 방법론을 잘 포착하지만, 약점을 식별하고 실질적인 질문을 제기하며 논문 품질에 따라 피드백을 조정하는 데는 미흡하다.
- 4. 연구 결과, LLMs는 ICLR 2025에서 좋은 논문의 강점 부분에서 인간 리뷰어보다 15.74% 더 많은 엔티티를 생성했지만, 약점 식별에서는 59.42% 적은 엔티티를 생성했다.
- 5. 모든 회의, 연도, 모델에서 유사한 경향이 관찰되며, 이는 LLM 기반 리뷰의 장단점을 이해하고 미래의 LLM 지원 리뷰 도구 개발에 정보를 제공한다.


---

*Generated on 2025-09-25 15:23:58*