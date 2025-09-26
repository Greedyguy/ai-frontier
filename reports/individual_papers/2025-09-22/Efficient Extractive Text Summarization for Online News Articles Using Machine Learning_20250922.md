---
keywords:
  - Extractive Summarization
  - Transformer
  - Neural Network
  - Cornell Newsroom Dataset
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15614
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:31:48.594130",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Extractive Summarization",
    "Transformer",
    "Neural Network",
    "Cornell Newsroom Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Extractive Summarization": 0.79,
    "Transformer": 0.8,
    "Neural Network": 0.77,
    "Cornell Newsroom Dataset": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "extractive text summarization",
        "canonical": "Extractive Summarization",
        "aliases": [
          "text summarization",
          "extractive summarization"
        ],
        "category": "specific_connectable",
        "rationale": "Extractive summarization is a key technique in NLP for condensing information, linking to broader themes in content management.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "BERT embeddings",
        "canonical": "Transformer",
        "aliases": [
          "BERT",
          "BERT model"
        ],
        "category": "broad_technical",
        "rationale": "BERT is a foundational model in NLP, facilitating connections to other Transformer-based techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "LSTM networks",
        "canonical": "Neural Network",
        "aliases": [
          "LSTM",
          "Long Short-Term Memory"
        ],
        "category": "broad_technical",
        "rationale": "LSTM networks are a type of neural network crucial for tasks involving sequential data, enhancing connections in temporal data processing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Cornell Newsroom dataset",
        "canonical": "Cornell Newsroom Dataset",
        "aliases": [
          "Newsroom dataset"
        ],
        "category": "unique_technical",
        "rationale": "This dataset is specific to the domain of news summarization, providing a unique link to empirical studies in the field.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "content management",
      "user engagement"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "extractive text summarization",
      "resolved_canonical": "Extractive Summarization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "BERT embeddings",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "LSTM networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Cornell Newsroom dataset",
      "resolved_canonical": "Cornell Newsroom Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Efficient Extractive Text Summarization for Online News Articles Using Machine Learning

**Korean Title:** 온라인 뉴스 기사를 위한 기계 학습 기반의 효율적인 추출적 텍스트 요약

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15614.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15614](https://arxiv.org/abs/2509.15614)

## 🔗 유사한 논문
- [[2025-09-22/Re-FRAME the Meeting Summarization SCOPE_ Fact-Based Summarization and Personalization via Questions_20250922|Re-FRAME the Meeting Summarization SCOPE: Fact-Based Summarization and Personalization via Questions]] (81.1% similar)
- [[2025-09-22/Deep learning and abstractive summarisation for radiological reports_ an empirical study for adapting the PEGASUS models' family with scarce data_20250922|Deep learning and abstractive summarisation for radiological reports: an empirical study for adapting the PEGASUS models' family with scarce data]] (80.7% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (80.6% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (80.4% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Extractive Summarization|Extractive Summarization]]
**⚡ Unique Technical**: [[keywords/Cornell Newsroom Dataset|Cornell Newsroom Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15614v1 Announce Type: new 
Abstract: In the age of information overload, content management for online news articles relies on efficient summarization to enhance accessibility and user engagement. This article addresses the challenge of extractive text summarization by employing advanced machine learning techniques to generate concise and coherent summaries while preserving the original meaning. Using the Cornell Newsroom dataset, comprising 1.3 million article-summary pairs, we developed a pipeline leveraging BERT embeddings to transform textual data into numerical representations. By framing the task as a binary classification problem, we explored various models, including logistic regression, feed-forward neural networks, and long short-term memory (LSTM) networks. Our findings demonstrate that LSTM networks, with their ability to capture sequential dependencies, outperform baseline methods like Lede-3 and simpler models in F1 score and ROUGE-1 metrics. This study underscores the potential of automated summarization in improving content management systems for online news platforms, enabling more efficient content organization and enhanced user experiences.

## 🔍 Abstract (한글 번역)

arXiv:2509.15614v1 발표 유형: 신규  
초록: 정보 과부하의 시대에 온라인 뉴스 기사에 대한 콘텐츠 관리는 접근성 향상과 사용자 참여를 위해 효율적인 요약에 의존합니다. 이 논문은 원래의 의미를 유지하면서 간결하고 일관된 요약을 생성하기 위해 고급 기계 학습 기법을 활용하여 추출적 텍스트 요약의 도전을 다룹니다. 130만 개의 기사-요약 쌍으로 구성된 Cornell Newsroom 데이터셋을 사용하여, 우리는 BERT 임베딩을 활용하여 텍스트 데이터를 수치적 표현으로 변환하는 파이프라인을 개발했습니다. 이 작업을 이진 분류 문제로 설정하여 로지스틱 회귀, 피드포워드 신경망, 장단기 메모리(LSTM) 네트워크를 포함한 다양한 모델을 탐색했습니다. 우리의 연구 결과는 순차적 의존성을 포착할 수 있는 LSTM 네트워크가 Lede-3와 같은 기준 방법 및 더 간단한 모델보다 F1 점수와 ROUGE-1 지표에서 우수한 성능을 보인다는 것을 보여줍니다. 이 연구는 온라인 뉴스 플랫폼의 콘텐츠 관리 시스템을 개선하여 더 효율적인 콘텐츠 조직과 향상된 사용자 경험을 가능하게 하는 자동 요약의 잠재력을 강조합니다.

## 📝 요약

이 논문은 정보 과부하 시대에 온라인 뉴스 기사의 효율적인 요약을 통해 접근성과 사용자 참여를 높이는 방법을 제시합니다. Cornell Newsroom 데이터셋을 활용하여 BERT 임베딩을 통해 텍스트 데이터를 수치화하고, 이를 이진 분류 문제로 접근했습니다. 로지스틱 회귀, 피드포워드 신경망, LSTM 네트워크 등 다양한 모델을 탐색한 결과, LSTM 네트워크가 순차적 의존성을 잘 포착하여 F1 점수와 ROUGE-1 지표에서 Lede-3 등 기존 방법보다 뛰어난 성능을 보였습니다. 이 연구는 자동 요약이 온라인 뉴스 플랫폼의 콘텐츠 관리 시스템을 개선할 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. 정보 과부하 시대에 온라인 뉴스 기사 요약은 접근성과 사용자 참여를 높이기 위해 중요합니다.
- 2. 본 연구는 BERT 임베딩을 활용하여 텍스트 데이터를 수치화하고, 이를 이진 분류 문제로 설정하여 요약을 생성합니다.
- 3. LSTM 네트워크는 순차적 의존성을 포착하는 능력 덕분에 F1 점수와 ROUGE-1 지표에서 기본 방법보다 우수한 성능을 보였습니다.
- 4. 자동 요약은 온라인 뉴스 플랫폼의 콘텐츠 관리 시스템을 개선하고 사용자 경험을 향상시킬 수 있는 잠재력을 가지고 있습니다.


---

*Generated on 2025-09-23 10:31:48*