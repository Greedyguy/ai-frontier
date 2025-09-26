---
keywords:
  - Multilingual Neural Machine Translation
  - Parallel Corpus
  - Domain Adaptation
  - Cross-Script Transfer Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19941
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:54:14.233969",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multilingual Neural Machine Translation",
    "Parallel Corpus",
    "Domain Adaptation",
    "Cross-Script Transfer Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multilingual Neural Machine Translation": 0.82,
    "Parallel Corpus": 0.75,
    "Domain Adaptation": 0.79,
    "Cross-Script Transfer Learning": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multilingual neural machine translation",
        "canonical": "Multilingual Neural Machine Translation",
        "aliases": [
          "multilingual NMT"
        ],
        "category": "specific_connectable",
        "rationale": "This term is central to the paper's focus on translation across multiple Indian languages, linking it to broader discussions on multilingual models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "parallel corpus",
        "canonical": "Parallel Corpus",
        "aliases": [
          "bi-text corpus"
        ],
        "category": "unique_technical",
        "rationale": "The creation of a parallel corpus is a unique contribution of the paper, essential for training translation models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "domain adaptation",
        "canonical": "Domain Adaptation",
        "aliases": [
          "domain-aware adaptation"
        ],
        "category": "specific_connectable",
        "rationale": "Domain adaptation is crucial for improving translation quality across different subject areas, linking to broader machine learning strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "cross-script transfer learning",
        "canonical": "Cross-Script Transfer Learning",
        "aliases": [
          "script transfer learning"
        ],
        "category": "unique_technical",
        "rationale": "This concept is significant for understanding how models handle different writing systems, a unique aspect of the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "Government",
      "Health",
      "General"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multilingual neural machine translation",
      "resolved_canonical": "Multilingual Neural Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "parallel corpus",
      "resolved_canonical": "Parallel Corpus",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "domain adaptation",
      "resolved_canonical": "Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "cross-script transfer learning",
      "resolved_canonical": "Cross-Script Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# CorIL: Towards Enriching Indian Language to Indian Language Parallel Corpora and Machine Translation Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19941.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19941](https://arxiv.org/abs/2509.19941)

## 🔗 유사한 논문
- [[2025-09-23/Crosslingual Optimized Metric for Translation Assessment of Indian Languages_20250923|Crosslingual Optimized Metric for Translation Assessment of Indian Languages]] (84.1% similar)
- [[2025-09-23/CUTE_ A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages_20250923|CUTE: A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages]] (81.6% similar)
- [[2025-09-22/UPRPRC_ Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations_20250922|UPRPRC: Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations]] (81.4% similar)
- [[2025-09-24/DRISHTIKON_ A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture_20250924|DRISHTIKON: A Multimodal Multilingual Benchmark for Testing Language Models' Understanding on Indian Culture]] (81.2% similar)
- [[2025-09-23/DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India_ Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context_20250923|DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multilingual Neural Machine Translation|Multilingual Neural Machine Translation]], [[keywords/Domain Adaptation|Domain Adaptation]]
**⚡ Unique Technical**: [[keywords/Parallel Corpus|Parallel Corpus]], [[keywords/Cross-Script Transfer Learning|Cross-Script Transfer Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19941v1 Announce Type: cross 
Abstract: India's linguistic landscape is one of the most diverse in the world, comprising over 120 major languages and approximately 1,600 additional languages, with 22 officially recognized as scheduled languages in the Indian Constitution. Despite recent progress in multilingual neural machine translation (NMT), high-quality parallel corpora for Indian languages remain scarce, especially across varied domains. In this paper, we introduce a large-scale, high-quality annotated parallel corpus covering 11 of these languages : English, Telugu, Hindi, Punjabi, Odia, Kashmiri, Sindhi, Dogri, Kannada, Urdu, and Gujarati comprising a total of 772,000 bi-text sentence pairs. The dataset is carefully curated and systematically categorized into three key domains: Government, Health, and General, to enable domain-aware machine translation research and facilitate effective domain adaptation. To demonstrate the utility of CorIL and establish strong benchmarks for future research, we fine-tune and evaluate several state-of-the-art NMT models, including IndicTrans2, NLLB, and BhashaVerse. Our analysis reveals important performance trends and highlights the corpus's value in probing model capabilities. For instance, the results show distinct performance patterns based on language script, with massively multilingual models showing an advantage on Perso-Arabic scripts (Urdu, Sindhi) while other models excel on Indic scripts. This paper provides a detailed domain-wise performance analysis, offering insights into domain sensitivity and cross-script transfer learning. By publicly releasing CorIL, we aim to significantly improve the availability of high-quality training data for Indian languages and provide a valuable resource for the machine translation research community.

## 📝 요약

이 논문은 인도의 다양한 언어 환경을 고려하여 11개 인도 언어에 대한 대규모 고품질 병렬 코퍼스인 CorIL을 소개합니다. 이 데이터셋은 영어, 텔루구어, 힌디어, 펀자브어, 오디아어, 카슈미르어, 신디어, 도그리어, 칸나다어, 우르두어, 구자라트어로 구성된 77만 2천 개의 문장 쌍을 포함하며, 정부, 건강, 일반의 세 가지 주요 도메인으로 체계적으로 분류되었습니다. 이를 통해 도메인 인식 기계 번역 연구와 효과적인 도메인 적응을 가능하게 합니다. 논문에서는 IndicTrans2, NLLB, BhashaVerse 등 최신 NMT 모델을 활용하여 데이터셋의 유용성을 입증하고, 언어 스크립트에 따른 성능 패턴을 분석하여 모델의 능력을 평가했습니다. 특히, 페르소-아라빅 스크립트(우르두어, 신디어)에서는 다중언어 모델이 우위를 보이는 반면, 인도 스크립트에서는 다른 모델이 뛰어난 성능을 보였습니다. CorIL의 공개를 통해 인도 언어에 대한 고품질 학습 데이터의 접근성을 크게 향상시키고, 기계 번역 연구 커뮤니티에 유용한 자원을 제공하고자 합니다.

## 🎯 주요 포인트

- 1. 인도의 언어적 다양성은 세계에서 가장 높은 수준으로, 120개 이상의 주요 언어와 약 1,600개의 추가 언어로 구성되어 있으며, 이 중 22개가 인도 헌법에 공식 언어로 인정받고 있다.
- 2. 본 논문에서는 영어, 텔루구어, 힌디어 등 11개 언어로 구성된 772,000개의 문장 쌍을 포함하는 대규모 고품질 병렬 코퍼스를 소개한다.
- 3. 데이터셋은 정부, 건강, 일반 등 세 가지 주요 도메인으로 체계적으로 분류되어 도메인 인식 기계 번역 연구와 효과적인 도메인 적응을 가능하게 한다.
- 4. 여러 최신 NMT 모델을 미세 조정하고 평가하여, 언어 스크립트에 따른 성능 패턴을 분석하고 모델의 능력을 탐구하는 데 있어 코퍼스의 가치를 강조한다.
- 5. CorIL의 공개를 통해 인도 언어를 위한 고품질 학습 데이터의 가용성을 크게 향상시키고 기계 번역 연구 커뮤니티에 귀중한 자원을 제공하고자 한다.


---

*Generated on 2025-09-25 15:54:14*