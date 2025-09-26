---
keywords:
  - Large Language Model
  - Queer Slang
  - Sense Disambiguation
  - Inter-annotator Agreement
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17449
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:27:55.157957",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Queer Slang",
    "Sense Disambiguation",
    "Inter-annotator Agreement"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Queer Slang": 0.9,
    "Sense Disambiguation": 0.8,
    "Inter-annotator Agreement": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion on slang processing.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Queer Slang",
        "canonical": "Queer Slang",
        "aliases": [
          "LGBTQ+ Slang"
        ],
        "category": "unique_technical",
        "rationale": "Queer Slang is the primary focus of the dataset and analysis in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Sense Disambiguation",
        "canonical": "Sense Disambiguation",
        "aliases": [
          "Word Sense Disambiguation"
        ],
        "category": "specific_connectable",
        "rationale": "Sense Disambiguation is a key task evaluated in the paper using the dataset.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Inter-annotator Agreement",
        "canonical": "Inter-annotator Agreement",
        "aliases": [
          "Annotation Agreement"
        ],
        "category": "unique_technical",
        "rationale": "Inter-annotator Agreement is crucial for evaluating the quality of the dataset annotations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "hate speech",
      "user interaction",
      "data curation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Queer Slang",
      "resolved_canonical": "Queer Slang",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Sense Disambiguation",
      "resolved_canonical": "Sense Disambiguation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Inter-annotator Agreement",
      "resolved_canonical": "Inter-annotator Agreement",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# SLAyiNG: Towards Queer Language Processing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17449.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17449](https://arxiv.org/abs/2509.17449)

## 🔗 유사한 논문
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (83.4% similar)
- [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (82.5% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (80.8% similar)
- [[2025-09-23/MIST_ Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning_20250923|MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning]] (80.8% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Sense Disambiguation|Sense Disambiguation]]
**⚡ Unique Technical**: [[keywords/Queer Slang|Queer Slang]], [[keywords/Inter-annotator Agreement|Inter-annotator Agreement]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17449v1 Announce Type: new 
Abstract: Knowledge of slang is a desirable feature of LLMs in the context of user interaction, as slang often reflects an individual's social identity. Several works on informal language processing have defined and curated benchmarks for tasks such as detection and identification of slang. In this paper, we focus on queer slang. Queer slang can be mistakenly flagged as hate speech or can evoke negative responses from LLMs during user interaction. Research efforts so far have not focused explicitly on queer slang. In particular, detection and processing of queer slang have not been thoroughly evaluated due to the lack of a high-quality annotated benchmark. To address this gap, we curate SLAyiNG, the first dataset containing annotated queer slang derived from subtitles, social media posts, and podcasts, reflecting real-world usage. We describe our data curation process, including the collection of slang terms and definitions, scraping sources for examples that reflect usage of these terms, and our ongoing annotation process. As preliminary results, we calculate inter-annotator agreement for human annotators and OpenAI's model o3-mini, evaluating performance on the task of sense disambiguation. Reaching an average Krippendorff's alpha of 0.746, we argue that state-of-the-art reasoning models can serve as tools for pre-filtering, but the complex and often sensitive nature of queer language data requires expert and community-driven annotation efforts.

## 📝 요약

이 논문은 사용자 상호작용에서 LLMs(대형 언어 모델)의 슬랭 이해 능력을 강조하며, 특히 퀴어 슬랭에 초점을 맞추고 있습니다. 퀴어 슬랭은 종종 혐오 발언으로 잘못 인식되거나 부정적인 반응을 유발할 수 있습니다. 기존 연구는 퀴어 슬랭에 대한 명확한 평가가 부족했으며, 이를 해결하기 위해 SLAyiNG이라는 최초의 퀴어 슬랭 주석 데이터셋을 제작했습니다. 이 데이터셋은 자막, 소셜 미디어 게시물, 팟캐스트 등에서 실제 사용 사례를 반영합니다. 데이터 수집 및 주석 과정에서 인간 주석자와 OpenAI 모델의 상호 주석자 일치도를 평가한 결과, 평균 Krippendorff's alpha가 0.746로 나타났습니다. 이는 최신 모델이 예비 필터링 도구로 활용될 수 있음을 시사하지만, 퀴어 언어 데이터의 복잡성과 민감성 때문에 전문가와 커뮤니티 주도의 주석 작업이 필요함을 강조합니다.

## 🎯 주요 포인트

- 1. 사용자 상호작용 맥락에서 LLM의 슬랭 이해는 개인의 사회적 정체성을 반영하기 때문에 중요하다.
- 2. 기존 연구들은 슬랭 탐지 및 식별에 대한 벤치마크를 정의했지만, 퀴어 슬랭에 대한 연구는 부족했다.
- 3. 퀴어 슬랭은 증오 발언으로 오인되거나 부정적인 반응을 유발할 수 있어, 이를 탐지하고 처리하는 데 어려움이 있었다.
- 4. SLAyiNG은 자막, 소셜 미디어 게시물, 팟캐스트에서 수집한 퀴어 슬랭을 포함한 최초의 주석 데이터셋이다.
- 5. 연구 결과, Krippendorff의 알파 값이 0.746로 나타나, 최첨단 모델이 사전 필터링 도구로 사용될 수 있지만, 퀴어 언어 데이터의 복잡성과 민감성 때문에 전문가와 커뮤니티 주도의 주석 작업이 필요하다.


---

*Generated on 2025-09-24 03:27:55*