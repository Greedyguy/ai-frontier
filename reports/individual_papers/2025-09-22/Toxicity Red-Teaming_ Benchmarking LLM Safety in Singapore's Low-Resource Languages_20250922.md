---
keywords:
  - Large Language Model
  - SGToxicGuard
  - Multilingual Learning
  - Red-Teaming
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15260
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:26:06.022200",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "SGToxicGuard",
    "Multilingual Learning",
    "Red-Teaming"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.9,
    "SGToxicGuard": 0.85,
    "Multilingual Learning": 0.8,
    "Red-Teaming": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Connects to a broad range of discussions on language model advancements.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.9
      },
      {
        "surface": "SGToxicGuard",
        "canonical": "SGToxicGuard",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a new dataset and framework specific to the paper's focus on safety in multilingual settings.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "multilingual settings",
        "canonical": "Multilingual Learning",
        "aliases": [
          "multilingual environments"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the focus on language diversity, crucial for linking to multilingual AI research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "red-teaming approach",
        "canonical": "Red-Teaming",
        "aliases": [
          "red teaming"
        ],
        "category": "unique_technical",
        "rationale": "Describes a specific method for probing vulnerabilities, relevant for safety and security discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "sensitive content",
      "real-world scenarios"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "SGToxicGuard",
      "resolved_canonical": "SGToxicGuard",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "multilingual settings",
      "resolved_canonical": "Multilingual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "red-teaming approach",
      "resolved_canonical": "Red-Teaming",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages

**Korean Title:** 독성 레드팀: 싱가포르의 저자원 언어에서 LLM 안전성 벤치마킹

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15260.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15260](https://arxiv.org/abs/2509.15260)

## 🔗 유사한 논문
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (85.2% similar)
- [[2025-09-22/From Judgment to Interference_ Early Stopping LLM Harmful Outputs via Streaming Content Monitoring_20250922|From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring]] (85.1% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.7% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (84.7% similar)
- [[2025-09-22/Red Teaming Multimodal Language Models_ Evaluating Harm Across Prompt Modalities and Models_20250922|Red Teaming Multimodal Language Models: Evaluating Harm Across Prompt Modalities and Models]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multilingual Learning|Multilingual Learning]]
**⚡ Unique Technical**: [[keywords/SGToxicGuard|SGToxicGuard]], [[keywords/Red-Teaming|Red-Teaming]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15260v1 Announce Type: new 
Abstract: The advancement of Large Language Models (LLMs) has transformed natural language processing; however, their safety mechanisms remain under-explored in low-resource, multilingual settings. Here, we aim to bridge this gap. In particular, we introduce \textsf{SGToxicGuard}, a novel dataset and evaluation framework for benchmarking LLM safety in Singapore's diverse linguistic context, including Singlish, Chinese, Malay, and Tamil. SGToxicGuard adopts a red-teaming approach to systematically probe LLM vulnerabilities in three real-world scenarios: \textit{conversation}, \textit{question-answering}, and \textit{content composition}. We conduct extensive experiments with state-of-the-art multilingual LLMs, and the results uncover critical gaps in their safety guardrails. By offering actionable insights into cultural sensitivity and toxicity mitigation, we lay the foundation for safer and more inclusive AI systems in linguistically diverse environments.\footnote{Link to the dataset: https://github.com/Social-AI-Studio/SGToxicGuard.} \textcolor{red}{Disclaimer: This paper contains sensitive content that may be disturbing to some readers.}

## 🔍 Abstract (한글 번역)

arXiv:2509.15260v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)의 발전은 자연어 처리 분야에 혁신을 가져왔으나, 저자원, 다언어 환경에서의 안전 메커니즘은 여전히 충분히 탐구되지 않았습니다. 본 연구에서는 이러한 격차를 해소하고자 합니다. 특히, 싱가포르의 다양한 언어적 맥락(싱글리시, 중국어, 말레이어, 타밀어 포함)에서 LLM 안전성을 평가하기 위한 새로운 데이터셋 및 평가 프레임워크인 \textsf{SGToxicGuard}를 소개합니다. SGToxicGuard는 레드 팀 접근 방식을 채택하여 세 가지 실제 시나리오인 \textit{대화}, \textit{질문-응답}, \textit{콘텐츠 구성}에서 LLM의 취약점을 체계적으로 탐색합니다. 최첨단 다언어 LLM을 사용하여 광범위한 실험을 수행한 결과, 이들의 안전 장치에 중요한 격차가 있음을 밝혀냈습니다. 문화적 민감성과 독성 완화에 대한 실행 가능한 통찰력을 제공함으로써, 언어적으로 다양한 환경에서 더 안전하고 포용적인 AI 시스템을 위한 기초를 마련하고자 합니다.\footnote{데이터셋 링크: https://github.com/Social-AI-Studio/SGToxicGuard.} \textcolor{red}{면책 조항: 이 논문에는 일부 독자에게 불쾌감을 줄 수 있는 민감한 내용이 포함되어 있습니다.}

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 안전 메커니즘이 저자원 다언어 환경에서 충분히 탐구되지 않았음을 지적하며, 이를 해결하기 위해 싱가포르의 다양한 언어적 맥락을 반영한 새로운 데이터셋과 평가 프레임워크인 \textsf{SGToxicGuard}를 소개합니다. 이 프레임워크는 대화, 질문-응답, 콘텐츠 작성의 세 가지 실제 시나리오에서 LLM의 취약성을 체계적으로 조사합니다. 최신 다언어 LLM을 대상으로 한 실험 결과, 이들의 안전 장치에 중요한 결함이 있음을 발견하였습니다. 이 연구는 문화적 민감성과 독성 완화에 대한 실행 가능한 통찰을 제공하여, 언어적으로 다양한 환경에서 더 안전하고 포용적인 AI 시스템 개발의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 안전 메커니즘이 저자원, 다언어 환경에서 충분히 탐구되지 않았음을 지적하고 이를 해결하기 위한 연구를 수행합니다.
- 2. 싱가포르의 다양한 언어적 맥락을 반영한 새로운 데이터셋 및 평가 프레임워크인 SGToxicGuard를 소개합니다.
- 3. SGToxicGuard는 대화, 질문-응답, 콘텐츠 구성의 세 가지 실제 시나리오에서 LLM의 취약점을 체계적으로 탐색합니다.
- 4. 최신 다언어 LLM을 대상으로 한 실험 결과, 안전성의 중요한 결함이 드러났으며, 문화적 민감성과 독성 완화에 대한 실행 가능한 통찰을 제공합니다.
- 5. 이 연구는 언어적으로 다양한 환경에서 더 안전하고 포용적인 AI 시스템을 구축하기 위한 기초를 마련합니다.


---

*Generated on 2025-09-23 11:26:06*