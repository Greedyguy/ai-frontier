<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:44:45.675552",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Named Entity Recognition",
    "Transformer",
    "KyrgyzNER Dataset",
    "Multilingual Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Named Entity Recognition": 0.85,
    "Transformer": 0.9,
    "KyrgyzNER Dataset": 0.78,
    "Multilingual Models": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Named Entity Recognition",
        "canonical": "Named Entity Recognition",
        "aliases": [
          "NER"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental task in Natural Language Processing, crucial for linking language-specific datasets.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "multilingual RoBERTa",
        "canonical": "Transformer",
        "aliases": [
          "mRoBERTa"
        ],
        "category": "broad_technical",
        "rationale": "A specific application of Transformer models, relevant for multilingual NLP tasks.",
        "novelty_score": 0.58,
        "connectivity_score": 0.92,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "KyrgyzNER",
        "canonical": "KyrgyzNER Dataset",
        "aliases": [
          "Kyrgyz NER"
        ],
        "category": "unique_technical",
        "rationale": "A unique dataset for Kyrgyz language, essential for linking language-specific resources.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "multilingual pretrained models",
        "canonical": "Multilingual Models",
        "aliases": [
          "multilingual NLP models"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the use of models trained on multiple languages, important for cross-lingual NLP research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.87,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "model",
      "language"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Named Entity Recognition",
      "resolved_canonical": "Named Entity Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "multilingual RoBERTa",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.92,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "KyrgyzNER",
      "resolved_canonical": "KyrgyzNER Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multilingual pretrained models",
      "resolved_canonical": "Multilingual Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.87,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Human-Annotated NER Dataset for the Kyrgyz Language

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19109.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19109](https://arxiv.org/abs/2509.19109)

## 🔗 유사한 논문
- [[2025-09-22/DynamicNER_ A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition_20250922|DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition]] (81.1% similar)
- [[2025-09-23/Turk-LettuceDetect_ A Hallucination Detection Models for Turkish RAG Applications_20250923|Turk-LettuceDetect: A Hallucination Detection Models for Turkish RAG Applications]] (79.7% similar)
- [[2025-09-23/KuBERT_ Central Kurdish BERT Model and Its Application for Sentiment Analysis_20250923|KuBERT: Central Kurdish BERT Model and Its Application for Sentiment Analysis]] (79.5% similar)
- [[2025-09-23/SciNLP_ A Domain-Specific Benchmark for Full-Text Scientific Entity and Relation Extraction in NLP_20250923|SciNLP: A Domain-Specific Benchmark for Full-Text Scientific Entity and Relation Extraction in NLP]] (79.0% similar)
- [[2025-09-22/Automatic Lexical Simplification for Turkish_20250922|Automatic Lexical Simplification for Turkish]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Named Entity Recognition|Named Entity Recognition]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multilingual Models|Multilingual Models]]
**⚡ Unique Technical**: [[keywords/KyrgyzNER Dataset|KyrgyzNER Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19109v1 Announce Type: new 
Abstract: We introduce KyrgyzNER, the first manually annotated named entity recognition dataset for the Kyrgyz language. Comprising 1,499 news articles from the 24.KG news portal, the dataset contains 10,900 sentences and 39,075 entity mentions across 27 named entity classes. We show our annotation scheme, discuss the challenges encountered in the annotation process, and present the descriptive statistics. We also evaluate several named entity recognition models, including traditional sequence labeling approaches based on conditional random fields and state-of-the-art multilingual transformer-based models fine-tuned on our dataset. While all models show difficulties with rare entity categories, models such as the multilingual RoBERTa variant pretrained on a large corpus across many languages achieve a promising balance between precision and recall. These findings emphasize both the challenges and opportunities of using multilingual pretrained models for processing languages with limited resources. Although the multilingual RoBERTa model performed best, other multilingual models yielded comparable results. This suggests that future work exploring more granular annotation schemes may offer deeper insights for Kyrgyz language processing pipelines evaluation.

## 📝 요약

KyrgyzNER은 키르기스어를 위한 최초의 수작업 명명 개체 인식 데이터셋으로, 24.KG 뉴스 포털의 1,499개 기사에서 10,900개의 문장과 39,075개의 개체 언급을 포함하고 있습니다. 이 연구는 주석 체계를 소개하고, 주석 과정에서의 도전 과제를 논의하며, 기술 통계를 제시합니다. 또한, 조건부 랜덤 필드 기반의 전통적인 시퀀스 라벨링 접근법과 최첨단 다국어 트랜스포머 기반 모델을 평가했습니다. 드문 개체 범주에서는 모든 모델이 어려움을 겪었지만, 다국어 RoBERTa 모델은 정밀도와 재현성 간의 균형을 잘 유지했습니다. 이는 자원이 제한된 언어 처리에 다국어 사전 학습 모델을 활용하는 것의 가능성을 시사합니다. 다국어 RoBERTa 모델이 가장 우수한 성능을 보였으나, 다른 다국어 모델도 유사한 결과를 보여, 향후 연구에서는 더 세분화된 주석 체계를 탐구하는 것이 키르기스어 처리 파이프라인 평가에 유용할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. KyrgyzNER은 키르기스어에 대한 최초의 수작업으로 주석된 개체명 인식 데이터셋입니다.
- 2. 데이터셋은 24.KG 뉴스 포털의 1,499개 기사에서 10,900개의 문장과 39,075개의 개체명을 포함하고 있습니다.
- 3. 다양한 개체명 인식 모델을 평가한 결과, 다국어 RoBERTa 변형 모델이 정밀도와 재현율에서 균형 잡힌 성능을 보였습니다.
- 4. 드문 개체 카테고리에서는 모든 모델이 어려움을 겪었으나, 다국어 사전학습 모델이 유망한 가능성을 보여주었습니다.
- 5. 향후 연구에서는 더 세분화된 주석 체계를 탐구함으로써 키르기스어 처리 파이프라인 평가에 대한 깊은 통찰을 제공할 수 있을 것입니다.


---

*Generated on 2025-09-24 15:44:45*