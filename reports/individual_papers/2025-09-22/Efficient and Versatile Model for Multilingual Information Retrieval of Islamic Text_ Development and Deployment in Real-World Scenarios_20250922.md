---
keywords:
  - Multilingual Information Retrieval
  - Quranic Multilingual Corpus
  - Cross-Lingual Techniques
  - Embedding Space
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15380
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:55:01.323759",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multilingual Information Retrieval",
    "Quranic Multilingual Corpus",
    "Cross-Lingual Techniques",
    "Embedding Space"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multilingual Information Retrieval": 0.85,
    "Quranic Multilingual Corpus": 0.8,
    "Cross-Lingual Techniques": 0.79,
    "Embedding Space": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multilingual Information Retrieval",
        "canonical": "Multilingual Information Retrieval",
        "aliases": [
          "MLIR"
        ],
        "category": "unique_technical",
        "rationale": "This is a central theme of the paper, focusing on retrieving information across multiple languages, which is crucial for linking multilingual datasets.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Quranic multilingual corpus",
        "canonical": "Quranic Multilingual Corpus",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This specific dataset is pivotal for the study and offers unique insights into multilingual retrieval in the Islamic domain.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "cross-lingual techniques",
        "canonical": "Cross-Lingual Techniques",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "These techniques are essential for linking different language datasets and improving retrieval effectiveness.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
      },
      {
        "surface": "embedding space",
        "canonical": "Embedding Space",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Understanding the embedding space is crucial for improving retrieval models and linking related research in NLP.",
        "novelty_score": 0.54,
        "connectivity_score": 0.87,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "real-world scenarios",
      "deployment considerations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multilingual Information Retrieval",
      "resolved_canonical": "Multilingual Information Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Quranic multilingual corpus",
      "resolved_canonical": "Quranic Multilingual Corpus",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "cross-lingual techniques",
      "resolved_canonical": "Cross-Lingual Techniques",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "embedding space",
      "resolved_canonical": "Embedding Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.54,
        "connectivity": 0.87,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Efficient and Versatile Model for Multilingual Information Retrieval of Islamic Text: Development and Deployment in Real-World Scenarios

**Korean Title:** 다국어 이슬람 텍스트 정보 검색을 위한 효율적이고 다재다능한 모델: 실제 시나리오에서의 개발 및 배포

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15380.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15380](https://arxiv.org/abs/2509.15380)

## 🔗 유사한 논문
- [[2025-09-18/Large Language Models for Information Retrieval_ A Survey_20250918|Large Language Models for Information Retrieval: A Survey]] (83.6% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (82.7% similar)
- [[2025-09-22/KITE_ Kernelized and Information Theoretic Exemplars for In-Context Learning_20250922|KITE: Kernelized and Information Theoretic Exemplars for In-Context Learning]] (81.6% similar)
- [[2025-09-22/Language Mixing in Reasoning Language Models_ Patterns, Impact, and Internal Causes_20250922|Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes]] (81.2% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Embedding Space|Embedding Space]]
**🔗 Specific Connectable**: [[keywords/Cross-Lingual Techniques|Cross-Lingual Techniques]]
**⚡ Unique Technical**: [[keywords/Multilingual Information Retrieval|Multilingual Information Retrieval]], [[keywords/Quranic Multilingual Corpus|Quranic Multilingual Corpus]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15380v1 Announce Type: cross 
Abstract: Despite recent advancements in Multilingual Information Retrieval (MLIR), a significant gap remains between research and practical deployment. Many studies assess MLIR performance in isolated settings, limiting their applicability to real-world scenarios. In this work, we leverage the unique characteristics of the Quranic multilingual corpus to examine the optimal strategies to develop an ad-hoc IR system for the Islamic domain that is designed to satisfy users' information needs in multiple languages. We prepared eleven retrieval models employing four training approaches: monolingual, cross-lingual, translate-train-all, and a novel mixed method combining cross-lingual and monolingual techniques. Evaluation on an in-domain dataset demonstrates that the mixed approach achieves promising results across diverse retrieval scenarios. Furthermore, we provide a detailed analysis of how different training configurations affect the embedding space and their implications for multilingual retrieval effectiveness. Finally, we discuss deployment considerations, emphasizing the cost-efficiency of deploying a single versatile, lightweight model for real-world MLIR applications.

## 🔍 Abstract (한글 번역)

arXiv:2509.15380v1 발표 유형: 교차  
초록: 다국어 정보 검색(MLIR) 분야에서 최근의 발전에도 불구하고, 연구와 실제 배포 사이에는 여전히 상당한 격차가 존재합니다. 많은 연구들이 MLIR 성능을 고립된 환경에서 평가하여 실제 시나리오에의 적용 가능성을 제한하고 있습니다. 본 연구에서는 꾸란 다국어 코퍼스의 독특한 특성을 활용하여, 이슬람 분야에서 다국어로 사용자의 정보 요구를 충족시키기 위해 설계된 임시 정보 검색(IR) 시스템을 개발하기 위한 최적의 전략을 조사합니다. 우리는 단일 언어, 교차 언어, 번역-전체 학습, 그리고 교차 언어와 단일 언어 기법을 결합한 새로운 혼합 방법 등 네 가지 학습 접근 방식을 사용하여 11개의 검색 모델을 준비했습니다. 도메인 내 데이터셋에 대한 평가 결과, 혼합 접근 방식이 다양한 검색 시나리오에서 유망한 결과를 달성함을 보여줍니다. 또한, 다양한 학습 구성 방식이 임베딩 공간에 미치는 영향과 다국어 검색 효율성에 대한 함의를 상세히 분석합니다. 마지막으로, 단일의 다재다능하고 경량화된 모델을 실제 MLIR 응용 프로그램에 배포하는 것이 비용 효율적임을 강조하며 배포 고려 사항을 논의합니다.

## 📝 요약

이 연구는 다국어 정보 검색(MLIR) 분야에서 연구와 실제 적용 간의 격차를 줄이기 위해 코란 다국어 코퍼스를 활용하여 이슬람 분야에 적합한 맞춤형 정보 검색 시스템을 개발하는 최적의 전략을 탐구합니다. 연구에서는 단일 언어, 교차 언어, 번역-훈련-전체, 그리고 교차 언어와 단일 언어 기법을 결합한 새로운 혼합 방법을 포함한 네 가지 훈련 접근법을 사용하여 11개의 검색 모델을 준비했습니다. 도메인 내 데이터셋 평가 결과, 혼합 방법이 다양한 검색 시나리오에서 유망한 결과를 보였습니다. 또한, 다양한 훈련 구성 방식이 임베딩 공간에 미치는 영향과 다국어 검색 효율성에 대한 분석을 제공합니다. 마지막으로, 실제 MLIR 응용을 위한 비용 효율적인 단일 경량 모델 배포의 중요성을 논의합니다.

## 🎯 주요 포인트

- 1. MLIR 연구와 실제 적용 간의 격차가 여전히 존재하며, 많은 연구가 고립된 환경에서 성능을 평가하여 실제 시나리오에의 적용성이 제한적이다.
- 2. 이 연구는 꾸란 다국어 코퍼스를 활용하여 이슬람 도메인에 적합한 다국어 정보 검색 시스템 개발을 위한 최적의 전략을 탐구한다.
- 3. 네 가지 학습 접근법을 사용하여 열한 개의 검색 모델을 준비했으며, 특히 교차 언어 및 단일 언어 기법을 결합한 새로운 혼합 방법이 다양한 검색 시나리오에서 유망한 결과를 보였다.
- 4. 다양한 학습 구성 방식이 임베딩 공간에 미치는 영향과 다국어 검색 효율성에 대한 함의를 상세히 분석하였다.
- 5. 실제 MLIR 응용 프로그램을 위한 단일의 다재다능하고 경량화된 모델 배포의 비용 효율성을 강조하며 배포 고려 사항을 논의하였다.


---

*Generated on 2025-09-23 08:55:01*