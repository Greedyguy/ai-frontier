---
keywords:
  - Large Language Model
  - Cross-lingual In-context Pre-training
  - Semantic Retrieval Framework
  - Multilingual Performance
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2504.20484
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:44:27.234495",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cross-lingual In-context Pre-training",
    "Semantic Retrieval Framework",
    "Multilingual Performance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cross-lingual In-context Pre-training": 0.88,
    "Semantic Retrieval Framework": 0.82,
    "Multilingual Performance": 0.8
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
        "rationale": "Large Language Models are central to the paper's methodology and are a key concept in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cross-lingual In-context Pre-training",
        "canonical": "Cross-lingual In-context Pre-training",
        "aliases": [
          "CrossIC-PT"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel method introduced in the paper, crucial for understanding the proposed approach.",
        "novelty_score": 0.95,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Semantic Retrieval Framework",
        "canonical": "Semantic Retrieval Framework",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This framework is essential for constructing training samples, linking to retrieval-based methods.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multilingual Performance",
        "canonical": "Multilingual Performance",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The paper focuses on improving performance across multiple languages, a key outcome of the study.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
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
      "candidate_surface": "Cross-lingual In-context Pre-training",
      "resolved_canonical": "Cross-lingual In-context Pre-training",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Semantic Retrieval Framework",
      "resolved_canonical": "Semantic Retrieval Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multilingual Performance",
      "resolved_canonical": "Multilingual Performance",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training

**Korean Title:** Cross-lingual In-Context 사전 훈련을 통한 LLM 언어 적응 향상

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2504.20484.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2504.20484](https://arxiv.org/abs/2504.20484)

## 🔗 유사한 논문
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (86.4% similar)
- [[2025-09-22/Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation_20250922|Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation]] (86.0% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (83.8% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.7% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Semantic Retrieval Framework|Semantic Retrieval Framework]], [[keywords/Multilingual Performance|Multilingual Performance]]
**⚡ Unique Technical**: [[keywords/Cross-lingual In-context Pre-training|Cross-lingual In-context Pre-training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.20484v2 Announce Type: replace 
Abstract: Large language models (LLMs) exhibit remarkable multilingual capabilities despite English-dominated pre-training, attributed to cross-lingual mechanisms during pre-training. Existing methods for enhancing cross-lingual transfer remain constrained by parallel resources, suffering from limited linguistic and domain coverage. We propose Cross-lingual In-context Pre-training (CrossIC-PT), a simple and scalable approach that enhances cross-lingual transfer by leveraging semantically related bilingual texts via simple next-word prediction. We construct CrossIC-PT samples by interleaving semantic-related bilingual Wikipedia documents into a single context window. To access window size constraints, we implement a systematic segmentation policy to split long bilingual document pairs into chunks while adjusting the sliding window mechanism to preserve contextual coherence. We further extend data availability through a semantic retrieval framework to construct CrossIC-PT samples from web-crawled corpus. Experimental results demonstrate that CrossIC-PT improves multilingual performance on three models (Llama-3.1-8B, Qwen2.5-7B, and Qwen2.5-1.5B) across six target languages, yielding performance gains of 3.79%, 3.99%, and 1.95%, respectively, with additional improvements after data augmentation.

## 🔍 Abstract (한글 번역)

arXiv:2504.20484v2 발표 유형: 교체  
초록: 대형 언어 모델(LLMs)은 영어 중심의 사전 학습에도 불구하고 놀라운 다국어 능력을 보여주며, 이는 사전 학습 중의 언어 간 메커니즘에 기인합니다. 기존의 언어 간 전이 향상 방법은 병렬 자원에 의해 제한되어 있으며, 언어 및 도메인 범위가 제한적입니다. 우리는 Cross-lingual In-context Pre-training (CrossIC-PT)을 제안하며, 이는 간단한 다음 단어 예측을 통해 의미적으로 관련된 이중 언어 텍스트를 활용하여 언어 간 전이를 향상시키는 간단하고 확장 가능한 접근 방식입니다. 우리는 의미적으로 관련된 이중 언어 위키백과 문서를 하나의 컨텍스트 창에 교차 배치하여 CrossIC-PT 샘플을 구성합니다. 창 크기 제한에 접근하기 위해, 우리는 체계적인 분할 정책을 구현하여 긴 이중 언어 문서 쌍을 청크로 나누고, 슬라이딩 윈도우 메커니즘을 조정하여 문맥적 일관성을 유지합니다. 또한, 웹 크롤링된 코퍼스로부터 CrossIC-PT 샘플을 구성하기 위해 의미적 검색 프레임워크를 통해 데이터 가용성을 확장합니다. 실험 결과는 CrossIC-PT가 세 가지 모델(Llama-3.1-8B, Qwen2.5-7B, Qwen2.5-1.5B)에서 여섯 개의 대상 언어에 대한 다국어 성능을 향상시킴을 보여주며, 각각 3.79%, 3.99%, 1.95%의 성능 향상을 가져왔고, 데이터 증강 후 추가적인 개선이 있었습니다.

## 📝 요약

이 논문은 영어 중심의 사전 학습에도 불구하고 뛰어난 다국어 능력을 보이는 대형 언어 모델(LLM)의 교차 언어 전이를 개선하기 위한 새로운 방법인 Cross-lingual In-context Pre-training (CrossIC-PT)을 제안합니다. 기존 방법들이 병렬 자원에 의존하여 언어 및 도메인 범위가 제한적인 문제를 해결하기 위해, CrossIC-PT는 의미적으로 관련된 이중 언어 텍스트를 활용하여 간단한 다음 단어 예측을 통해 교차 언어 전이를 강화합니다. 실험 결과, CrossIC-PT는 Llama-3.1-8B, Qwen2.5-7B, Qwen2.5-1.5B 모델에서 6개 언어에 걸쳐 각각 3.79%, 3.99%, 1.95%의 성능 향상을 보였으며, 데이터 증강 후 추가적인 개선이 있었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 영어 중심의 사전 학습에도 불구하고 뛰어난 다국어 능력을 보여주며, 이는 사전 학습 중 교차 언어 메커니즘 덕분이다.
- 2. CrossIC-PT는 의미적으로 관련된 이중 언어 텍스트를 활용하여 간단한 다음 단어 예측을 통해 교차 언어 전이를 향상시키는 간단하고 확장 가능한 접근법이다.
- 3. CrossIC-PT 샘플은 의미적으로 관련된 이중 언어 위키피디아 문서를 하나의 컨텍스트 창으로 교차 배열하여 구성된다.
- 4. 실험 결과, CrossIC-PT는 세 가지 모델(Llama-3.1-8B, Qwen2.5-7B, Qwen2.5-1.5B)의 다국어 성능을 여섯 개의 대상 언어에서 각각 3.79%, 3.99%, 1.95% 향상시켰다.
- 5. 데이터 증강 후 추가적인 성능 개선이 관찰되었다.


---

*Generated on 2025-09-23 11:44:27*