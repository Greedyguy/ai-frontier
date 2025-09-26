---
keywords:
  - Large Language Model
  - Membership Inference Attack
  - Natural Language Processing
  - Data Leakage Detection
  - Tag&Tab
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2501.08454
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:51:47.452616",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Membership Inference Attack",
    "Natural Language Processing",
    "Data Leakage Detection",
    "Tag&Tab"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Membership Inference Attack": 0.78,
    "Natural Language Processing": 0.82,
    "Data Leakage Detection": 0.77,
    "Tag&Tab": 0.79
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
        "rationale": "Central to the paper's focus on pretraining data detection and membership inference attacks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Membership Inference Attacks",
        "canonical": "Membership Inference Attack",
        "aliases": [
          "MIA"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for linking discussions on data privacy and security in machine learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "Relevant for connecting to broader discussions on language model applications and techniques.",
        "novelty_score": 0.2,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.82
      },
      {
        "surface": "Data Leakage Detection",
        "canonical": "Data Leakage Detection",
        "aliases": [
          "Data Leak Detection"
        ],
        "category": "unique_technical",
        "rationale": "Unique focus of the paper, highlighting advancements in detecting unauthorized data use.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Tag&Tab",
        "canonical": "Tag&Tab",
        "aliases": [
          "Tag and Tab"
        ],
        "category": "unique_technical",
        "rationale": "Proposed novel method in the paper, crucial for understanding the new approach to data detection.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.79
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Membership Inference Attacks",
      "resolved_canonical": "Membership Inference Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Data Leakage Detection",
      "resolved_canonical": "Data Leakage Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Tag&Tab",
      "resolved_canonical": "Tag&Tab",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Tag&Tab: Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack

**Korean Title:** 태그&탭: 키워드 기반 멤버십 추론 공격을 이용한 대규모 언어 모델의 사전 학습 데이터 탐지

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2501.08454.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2501.08454](https://arxiv.org/abs/2501.08454)

## 🔗 유사한 논문
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.0% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.1% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (84.0% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (83.8% similar)
- [[2025-09-22/SENTRA_ Selected-Next-Token Transformer for LLM Text Detection_20250922|SENTRA: Selected-Next-Token Transformer for LLM Text Detection]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Natural Language Processing|Natural Language Processing]]
**🔗 Specific Connectable**: [[keywords/Membership Inference Attack|Membership Inference Attack]]
**⚡ Unique Technical**: [[keywords/Data Leakage Detection|Data Leakage Detection]], [[keywords/Tag&Tab|Tag&Tab]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.08454v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) have become essential tools for digital task assistance. Their training relies heavily on the collection of vast amounts of data, which may include copyright-protected or sensitive information. Recent studies on detecting pretraining data in LLMs have primarily focused on sentence- or paragraph-level membership inference attacks (MIAs), usually involving probability analysis of the target model's predicted tokens. However, these methods often exhibit poor accuracy, failing to account for the semantic importance of textual content and word significance. To address these shortcomings, we propose Tag&amp;Tab, a novel approach for detecting data used in LLM pretraining. Our method leverages established natural language processing (NLP) techniques to tag keywords in the input text, a process we term Tagging. Then, the LLM is used to obtain probabilities for these keywords and calculate their average log-likelihood to determine input text membership, a process we refer to as Tabbing. Our experiments on four benchmark datasets (BookMIA, MIMIR, PatentMIA, and the Pile) and several open-source LLMs of varying sizes demonstrate an average increase in AUC scores ranging from 5.3% to 17.6% over state-of-the-art methods. Tag&amp;Tab not only sets a new standard for data leakage detection in LLMs, but its outstanding performance is a testament to the importance of words in MIAs on LLMs.

## 🔍 Abstract (한글 번역)

arXiv:2501.08454v2 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLM)은 디지털 작업 지원을 위한 필수 도구가 되었습니다. 이들의 훈련은 주로 방대한 양의 데이터를 수집하는 데 의존하며, 여기에는 저작권 보호 또는 민감한 정보가 포함될 수 있습니다. LLM에서의 사전 훈련 데이터 탐지에 관한 최근 연구는 주로 문장 또는 단락 수준의 멤버십 추론 공격(MIA)에 초점을 맞추고 있으며, 이는 보통 대상 모델의 예측된 토큰에 대한 확률 분석을 포함합니다. 그러나 이러한 방법은 종종 텍스트 내용의 의미적 중요성과 단어의 중요성을 고려하지 않아 정확도가 떨어지는 경향이 있습니다. 이러한 단점을 해결하기 위해, 우리는 LLM 사전 훈련에 사용된 데이터를 탐지하기 위한 새로운 접근 방식인 Tag&amp;Tab을 제안합니다. 우리의 방법은 입력 텍스트에서 키워드를 태그하는 기존의 자연어 처리(NLP) 기술을 활용하는데, 이를 태깅(Tagging)이라고 부릅니다. 그런 다음, LLM을 사용하여 이러한 키워드의 확률을 얻고, 평균 로그 가능성을 계산하여 입력 텍스트의 멤버십을 결정하는데, 이를 태빙(Tabbing)이라고 부릅니다. 네 가지 벤치마크 데이터셋(BookMIA, MIMIR, PatentMIA, 및 the Pile)과 다양한 크기의 여러 오픈 소스 LLM에 대한 우리의 실험은 최첨단 방법에 비해 AUC 점수가 평균 5.3%에서 17.6%까지 증가함을 보여줍니다. Tag&amp;Tab은 LLM에서의 데이터 누출 탐지에 새로운 기준을 세울 뿐만 아니라, LLM에서의 MIA에 있어서 단어의 중요성을 입증하는 뛰어난 성능을 보여줍니다.

## 📝 요약

대형 언어 모델(LLM)의 사전 학습 데이터에서 저작권 보호 또는 민감한 정보가 포함될 수 있어 데이터 유출 감지가 중요합니다. 기존의 문장 또는 단락 수준의 멤버십 추론 공격(MIA)은 정확도가 낮고 텍스트의 의미적 중요성을 고려하지 못하는 한계가 있습니다. 이를 해결하기 위해, 우리는 Tag&Tab이라는 새로운 접근법을 제안합니다. 이 방법은 자연어 처리(NLP) 기술을 활용해 입력 텍스트의 키워드를 태그하고, LLM을 통해 이 키워드의 확률을 계산하여 평균 로그 가능성을 산출함으로써 데이터 사용 여부를 판단합니다. 네 가지 벤치마크 데이터셋과 다양한 오픈 소스 LLM을 대상으로 한 실험에서, 기존 방법 대비 AUC 점수가 평균 5.3%에서 17.6%까지 향상되었습니다. Tag&Tab은 LLM의 데이터 유출 감지에 새로운 기준을 제시하며, 단어의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 사전 훈련 데이터 탐지에 대한 기존 연구는 문장 또는 문단 수준의 멤버십 추론 공격(MIA)에 집중되어 있으며, 이는 종종 정확도가 낮습니다.
- 2. Tag&amp;Tab는 입력 텍스트의 키워드를 태그하고, 이 키워드의 평균 로그 가능성을 계산하여 입력 텍스트의 멤버십을 결정하는 새로운 접근 방식입니다.
- 3. 제안된 방법은 네 가지 벤치마크 데이터셋과 다양한 크기의 오픈 소스 LLM에서 기존 방법 대비 AUC 점수를 평균 5.3%에서 17.6%까지 향상시켰습니다.
- 4. Tag&amp;Tab는 LLM의 데이터 누출 탐지에서 새로운 기준을 설정하며, MIA에서 단어의 중요성을 강조합니다.


---

*Generated on 2025-09-23 11:51:47*