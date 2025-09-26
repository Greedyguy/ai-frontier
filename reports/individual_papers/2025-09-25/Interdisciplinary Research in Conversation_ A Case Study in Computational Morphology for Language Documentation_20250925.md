---
keywords:
  - Computational Morphology
  - Interlinear Glossed Text
  - User-Centered Design
  - Natural Language Processing
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.10644
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:57:56.286621",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Computational Morphology",
    "Interlinear Glossed Text",
    "User-Centered Design",
    "Natural Language Processing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Computational Morphology": 0.8,
    "Interlinear Glossed Text": 0.78,
    "User-Centered Design": 0.77,
    "Natural Language Processing": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Computational Morphology",
        "canonical": "Computational Morphology",
        "aliases": [
          "Morphological Analysis"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and connects to language processing tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Interlinear Glossed Text",
        "canonical": "Interlinear Glossed Text",
        "aliases": [
          "IGT"
        ],
        "category": "unique_technical",
        "rationale": "IGT is a specific format used in language documentation, linking to linguistic data representation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "User-Centered Design",
        "canonical": "User-Centered Design",
        "aliases": [
          "UCD"
        ],
        "category": "specific_connectable",
        "rationale": "User-Centered Design is crucial for integrating research outputs into practical applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "NLP is a foundational field related to the paper's discussion on computational morphology.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "language documentation",
      "research agenda"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Computational Morphology",
      "resolved_canonical": "Computational Morphology",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Interlinear Glossed Text",
      "resolved_canonical": "Interlinear Glossed Text",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "User-Centered Design",
      "resolved_canonical": "User-Centered Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Interdisciplinary Research in Conversation: A Case Study in Computational Morphology for Language Documentation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.10644.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.10644](https://arxiv.org/abs/2509.10644)

## 🔗 유사한 논문
- [[2025-09-23/Translation in the Hands of Many_Centering Lay Users in Machine Translation Interactions_20250923|Translation in the Hands of Many:Centering Lay Users in Machine Translation Interactions]] (83.0% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (82.7% similar)
- [[2025-09-24/Anything Goes? A Crosslinguistic Study of (Im)possible Language Learning in LMs_20250924|Anything Goes? A Crosslinguistic Study of (Im)possible Language Learning in LMs]] (82.7% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (82.5% similar)
- [[2025-09-25/Tokenization and Representation Biases in Multilingual Models on Dialectal NLP Tasks_20250925|Tokenization and Representation Biases in Multilingual Models on Dialectal NLP Tasks]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/User-Centered Design|User-Centered Design]]
**⚡ Unique Technical**: [[keywords/Computational Morphology|Computational Morphology]], [[keywords/Interlinear Glossed Text|Interlinear Glossed Text]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.10644v2 Announce Type: replace 
Abstract: Computational morphology has the potential to support language documentation through tasks like morphological segmentation and the generation of Interlinear Glossed Text (IGT). However, our research outputs have seen limited use in real-world language documentation settings. This position paper situates the disconnect between computational morphology and language documentation within a broader misalignment between research and practice in NLP and argues that the field risks becoming decontextualized and ineffectual without systematic integration of User-Centered Design (UCD). To demonstrate how principles from UCD can reshape the research agenda, we present a case study of GlossLM, a state-of-the-art multilingual IGT generation model. Through a small-scale user study with three documentary linguists, we find that despite strong metric based performance, the system fails to meet core usability needs in real documentation contexts. These insights raise new research questions around model constraints, label standardization, segmentation, and personalization. We argue that centering users not only produces more effective tools, but surfaces richer, more relevant research directions

## 📝 요약

이 논문은 컴퓨터 형태론이 언어 문서화에 기여할 수 있는 잠재력을 가지고 있지만, 실제 활용은 제한적이라고 지적합니다. 연구와 실무 간의 불일치를 해결하기 위해 사용자 중심 설계(UCD)의 통합이 필요하다고 주장하며, 이를 통해 연구 방향을 재구성할 수 있음을 보여줍니다. 사례 연구로 다국어 IGT 생성 모델인 GlossLM을 소개하고, 소규모 사용자 연구를 통해 실제 문서화 환경에서의 사용성 문제를 발견합니다. 이러한 통찰은 모델 제약, 라벨 표준화, 세분화 및 개인화와 관련된 새로운 연구 질문을 제기하며, 사용자 중심 접근이 더 효과적인 도구와 관련성 높은 연구 방향을 제시할 수 있음을 강조합니다.

## 🎯 주요 포인트

- 1. 컴퓨팅 형태론은 형태소 분할 및 중간어 주석 텍스트(IGT) 생성과 같은 작업을 통해 언어 문서화를 지원할 수 있는 잠재력을 지니고 있다.
- 2. 연구 결과가 실제 언어 문서화 환경에서 제한적으로 사용되고 있으며, 이는 NLP 연구와 실무 간의 불일치로 인해 발생한다.
- 3. 사용자 중심 설계(UCD)의 체계적인 통합 없이는 컴퓨팅 형태론 분야가 비맥락적이고 비효율적으로 변할 위험이 있다.
- 4. GlossLM 모델 사례 연구를 통해, 강력한 성능에도 불구하고 실제 문서화 환경에서 핵심 사용성 요구를 충족하지 못하는 문제를 발견하였다.
- 5. 사용자 중심 접근은 더 효과적인 도구를 만들 뿐만 아니라, 모델 제약, 레이블 표준화, 분할 및 개인화 등 새로운 연구 질문을 제기한다.


---

*Generated on 2025-09-26 08:57:56*