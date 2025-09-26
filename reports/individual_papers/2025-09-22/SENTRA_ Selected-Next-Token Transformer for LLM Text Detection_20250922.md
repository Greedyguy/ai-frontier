---
keywords:
  - Transformer
  - Large Language Model
  - Contrastive Pre-training
  - Text Detection
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.12385
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:23:57.083258",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Large Language Model",
    "Contrastive Pre-training",
    "Text Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Large Language Model": 0.8,
    "Contrastive Pre-training": 0.78,
    "Text Detection": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in modern NLP, linking to a wide range of related topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's focus and connect to various applications and research in NLP.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Contrastive Pre-training",
        "canonical": "Contrastive Pre-training",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is crucial for the model's training process and links to advanced learning methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Text Detection",
        "canonical": "Text Detection",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Text detection is a specific application area that connects to broader topics in NLP and AI safety.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Contrastive Pre-training",
      "resolved_canonical": "Contrastive Pre-training",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Text Detection",
      "resolved_canonical": "Text Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SENTRA: Selected-Next-Token Transformer for LLM Text Detection

**Korean Title:** SENTRA: LLM 텍스트 탐지를 위한 선택된 다음 토큰 변환기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12385.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.12385](https://arxiv.org/abs/2509.12385)

## 🔗 유사한 논문
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.1% similar)
- [[2025-09-22/Tag&Tab_ Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack_20250922|Tag&Tab: Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack]] (83.8% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.8% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (83.6% similar)
- [[2025-09-22/DynamicNER_ A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition_20250922|DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Text Detection|Text Detection]]
**⚡ Unique Technical**: [[keywords/Contrastive Pre-training|Contrastive Pre-training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12385v2 Announce Type: replace-cross 
Abstract: LLMs are becoming increasingly capable and widespread. Consequently, the potential and reality of their misuse is also growing. In this work, we address the problem of detecting LLM-generated text that is not explicitly declared as such. We present a novel, general-purpose, and supervised LLM text detector, SElected-Next-Token tRAnsformer (SENTRA). SENTRA is a Transformer-based encoder leveraging selected-next-token-probability sequences and utilizing contrastive pre-training on large amounts of unlabeled data. Our experiments on three popular public datasets across 24 domains of text demonstrate SENTRA is a general-purpose classifier that significantly outperforms popular baselines in the out-of-domain setting.

## 🔍 Abstract (한글 번역)

arXiv:2509.12385v2 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLM)은 점점 더 강력해지고 널리 사용되고 있습니다. 그에 따라 이러한 모델의 오용 가능성과 현실도 증가하고 있습니다. 본 연구에서는 LLM이 생성한 텍스트가 명시적으로 선언되지 않은 경우 이를 감지하는 문제를 다룹니다. 우리는 새로운 범용 감독 학습 LLM 텍스트 탐지기인 SElected-Next-Token tRAnsformer (SENTRA)를 제시합니다. SENTRA는 선택된 다음 토큰 확률 시퀀스를 활용하고 대량의 레이블이 없는 데이터에 대한 대조적 사전 학습을 활용하는 트랜스포머 기반 인코더입니다. 24개의 텍스트 도메인에 걸쳐 세 가지 인기 있는 공개 데이터셋에 대한 실험에서 SENTRA는 범용 분류기로서 도메인 외 설정에서 인기 있는 기준 모델을 크게 능가함을 입증합니다.

## 📝 요약

이 논문은 명시되지 않은 LLM(대형 언어 모델) 생성 텍스트를 탐지하는 문제를 다룹니다. 저자들은 새로운 범용 감독 학습 LLM 텍스트 탐지기인 SENTRA를 제안합니다. SENTRA는 선택된 다음 토큰 확률 시퀀스를 활용하는 Transformer 기반 인코더로, 대량의 비라벨 데이터에 대한 대조적 사전 학습을 사용합니다. 24개 텍스트 도메인에 걸친 세 가지 인기 있는 공개 데이터셋에서의 실험 결과, SENTRA는 범용 분류기로서 도메인 외 설정에서 기존의 인기 있는 기준 모델들을 크게 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. LLM의 오용 가능성과 현실이 증가하고 있으며, 이를 탐지하는 문제를 다루고 있다.
- 2. LLM이 생성한 텍스트를 탐지하기 위해 새로운 범용 감독 학습 기반의 탐지기인 SENTRA를 제안한다.
- 3. SENTRA는 선택된 다음 토큰 확률 시퀀스를 활용하는 Transformer 기반의 인코더이다.
- 4. 대량의 비라벨 데이터에 대한 대조적 사전 학습을 통해 성능을 향상시킨다.
- 5. 24개 도메인의 텍스트를 포함한 세 가지 인기 있는 공개 데이터셋에서 SENTRA는 범용 분류기로서 기존의 인기 있는 기준선을 크게 능가한다.


---

*Generated on 2025-09-23 11:23:57*