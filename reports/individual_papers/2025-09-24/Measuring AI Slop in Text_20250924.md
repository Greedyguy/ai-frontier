<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:45:13.547657",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "AI Slop",
    "Natural Language Processing",
    "Coherence",
    "Relevance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "AI Slop": 0.78,
    "Natural Language Processing": 0.85,
    "Coherence": 0.8,
    "Relevance": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AI slop",
        "canonical": "AI Slop",
        "aliases": [
          "low-quality AI-generated text"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel concept in evaluating AI-generated text quality, which is central to the paper's focus.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "NLP is a foundational field relevant to the study of AI-generated text and its quality assessment.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "coherence",
        "canonical": "Coherence",
        "aliases": [
          "text coherence"
        ],
        "category": "specific_connectable",
        "rationale": "Coherence is a critical dimension for evaluating text quality, directly linked to the paper's assessment framework.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "relevance",
        "canonical": "Relevance",
        "aliases": [
          "text relevance"
        ],
        "category": "specific_connectable",
        "rationale": "Relevance is another key dimension in assessing AI-generated text, facilitating connections to quality evaluation.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "taxonomy",
      "framework",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AI slop",
      "resolved_canonical": "AI Slop",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "coherence",
      "resolved_canonical": "Coherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "relevance",
      "resolved_canonical": "Relevance",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Measuring AI "Slop" in Text

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19163.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19163](https://arxiv.org/abs/2509.19163)

## 🔗 유사한 논문
- [[2025-09-23/Fine-Grained Detection of AI-Generated Text Using Sentence-Level Segmentation_20250923|Fine-Grained Detection of AI-Generated Text Using Sentence-Level Segmentation]] (81.7% similar)
- [[2025-09-24/Trace Is In Sentences_ Unbiased Lightweight ChatGPT-Generated Text Detector_20250924|Trace Is In Sentences: Unbiased Lightweight ChatGPT-Generated Text Detector]] (81.4% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (80.0% similar)
- [[2025-09-22/The Great AI Witch Hunt_ Reviewers Perception and (Mis)Conception of Generative AI in Research Writing_20250922|The Great AI Witch Hunt: Reviewers Perception and (Mis)Conception of Generative AI in Research Writing]] (79.0% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Coherence|Coherence]], [[keywords/Relevance|Relevance]]
**⚡ Unique Technical**: [[keywords/AI Slop|AI Slop]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19163v1 Announce Type: new 
Abstract: AI "slop" is an increasingly popular term used to describe low-quality AI-generated text, but there is currently no agreed upon definition of this term nor a means to measure its occurrence. In this work, we develop a taxonomy of "slop" through interviews with experts in NLP, writing, and philosophy, and propose a set of interpretable dimensions for its assessment in text. Through span-level annotation, we find that binary "slop" judgments are (somewhat) subjective, but such determinations nonetheless correlate with latent dimensions such as coherence and relevance. Our framework can be used to evaluate AI-generated text in both detection and binary preference tasks, potentially offering new insights into the linguistic and stylistic factors that contribute to quality judgments.

## 📝 요약

이 논문은 AI가 생성한 저품질 텍스트를 의미하는 "slop"의 정의와 측정 방법이 부재한 상황에서, 이를 체계화하기 위해 NLP, 작문, 철학 전문가와의 인터뷰를 통해 "slop"의 분류 체계를 개발했습니다. 텍스트 평가를 위한 해석 가능한 차원을 제안하며, span-level 주석을 통해 이진 "slop" 판단이 다소 주관적이지만, 일관성과 관련성과 같은 잠재적 차원과 상관관계가 있음을 발견했습니다. 이 프레임워크는 AI 생성 텍스트의 탐지 및 이진 선호 과제에서 평가 도구로 활용될 수 있으며, 품질 판단에 기여하는 언어적, 스타일적 요소에 대한 새로운 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. AI "slop"은 저품질의 AI 생성 텍스트를 설명하는 용어로, 현재까지 명확한 정의나 측정 방법이 없다.
- 2. 본 연구에서는 NLP, 글쓰기, 철학 전문가와의 인터뷰를 통해 "slop"의 분류 체계를 개발하고, 이를 평가할 수 있는 해석 가능한 차원을 제안한다.
- 3. 스팬 수준의 주석을 통해 이진 "slop" 판단이 다소 주관적임을 발견했지만, 이러한 판단은 일관성과 관련성과 같은 잠재적 차원과 상관관계가 있다.
- 4. 제안된 프레임워크는 AI 생성 텍스트의 탐지 및 이진 선호 과제에서 평가 도구로 사용될 수 있으며, 품질 판단에 기여하는 언어적 및 스타일적 요인에 대한 새로운 통찰을 제공할 수 있다.


---

*Generated on 2025-09-24 15:45:13*