<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:42:28.938986",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multilingual Language Models",
    "Vocabulary Overlap",
    "Cross-Lingual Transfer",
    "Semantic Similarity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multilingual Language Models": 0.82,
    "Vocabulary Overlap": 0.77,
    "Cross-Lingual Transfer": 0.8,
    "Semantic Similarity": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multilingual language models",
        "canonical": "Multilingual Language Models",
        "aliases": [
          "multilingual models",
          "cross-lingual models"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the study and connects well with existing work on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "vocabulary overlap",
        "canonical": "Vocabulary Overlap",
        "aliases": [
          "token overlap",
          "shared vocabulary"
        ],
        "category": "unique_technical",
        "rationale": "A unique aspect of the study, focusing on the impact of shared tokens across languages.",
        "novelty_score": 0.75,
        "connectivity_score": 0.67,
        "specificity_score": 0.79,
        "link_intent_score": 0.77
      },
      {
        "surface": "cross-lingual transfer",
        "canonical": "Cross-Lingual Transfer",
        "aliases": [
          "language transfer",
          "multilingual transfer"
        ],
        "category": "specific_connectable",
        "rationale": "Key to understanding how multilingual models benefit from shared vocabulary.",
        "novelty_score": 0.52,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "semantic similarity",
        "canonical": "Semantic Similarity",
        "aliases": [
          "semantic overlap",
          "meaning similarity"
        ],
        "category": "broad_technical",
        "rationale": "Relates to how models interpret shared tokens, linking to broader semantic analysis.",
        "novelty_score": 0.4,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
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
      "candidate_surface": "multilingual language models",
      "resolved_canonical": "Multilingual Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "vocabulary overlap",
      "resolved_canonical": "Vocabulary Overlap",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.67,
        "specificity": 0.79,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "cross-lingual transfer",
      "resolved_canonical": "Cross-Lingual Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "semantic similarity",
      "resolved_canonical": "Semantic Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# False Friends Are Not Foes: Investigating Vocabulary Overlap in Multilingual Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18750.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18750](https://arxiv.org/abs/2509.18750)

## 🔗 유사한 논문
- [[2025-09-24/Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages_20250924|Linguistic Neuron Overlap Patterns to Facilitate Cross-lingual Transfer on Low-resource Languages]] (81.8% similar)
- [[2025-09-23/Enhancing Cross-Lingual Transfer through Reversible Transliteration_ A Huffman-Based Approach for Low-Resource Languages_20250923|Enhancing Cross-Lingual Transfer through Reversible Transliteration: A Huffman-Based Approach for Low-Resource Languages]] (81.7% similar)
- [[2025-09-17/You Are What You Train_ Effects of Data Composition on Training Context-aware Machine Translation Models_20250917|You Are What You Train: Effects of Data Composition on Training Context-aware Machine Translation Models]] (81.3% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (80.7% similar)
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Semantic Similarity|Semantic Similarity]]
**🔗 Specific Connectable**: [[keywords/Multilingual Language Models|Multilingual Language Models]], [[keywords/Cross-Lingual Transfer|Cross-Lingual Transfer]]
**⚡ Unique Technical**: [[keywords/Vocabulary Overlap|Vocabulary Overlap]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18750v1 Announce Type: new 
Abstract: Subword tokenizers trained on multilingual corpora naturally produce overlapping tokens across languages. Does token overlap facilitate cross-lingual transfer or instead introduce interference between languages? Prior work offers mixed evidence, partly due to varied setups and confounders, such as token frequency or subword segmentation granularity. To address this question, we devise a controlled experiment where we train bilingual autoregressive models on multiple language pairs under systematically varied vocabulary overlap settings. Crucially, we explore a new dimension to understanding how overlap affects transfer: the semantic similarity of tokens shared across languages. We first analyze our models' hidden representations and find that overlap of any kind creates embedding spaces that capture cross-lingual semantic relationships, while this effect is much weaker in models with disjoint vocabularies. On XNLI and XQuAD, we find that models with overlap outperform models with disjoint vocabularies, and that transfer performance generally improves as overlap increases. Overall, our findings highlight the advantages of token overlap in multilingual models and show that substantial shared vocabulary remains a beneficial design choice for multilingual tokenizers.

## 📝 요약

이 논문은 다국어 코퍼스에서 훈련된 서브워드 토크나이저가 언어 간 토큰 중첩을 자연스럽게 생성하는 현상이 언어 간 전이에 미치는 영향을 연구합니다. 저자들은 다양한 언어 쌍에 대해 어휘 중첩 설정을 체계적으로 변화시키며 이중 언어 모델을 훈련하는 실험을 설계했습니다. 특히, 언어 간 공유되는 토큰의 의미적 유사성이 전이에 미치는 영향을 탐구했습니다. 연구 결과, 중첩된 토큰은 교차 언어적 의미 관계를 포착하는 임베딩 공간을 형성하며, 이는 분리된 어휘를 사용하는 모델보다 성능이 뛰어남을 발견했습니다. XNLI와 XQuAD 벤치마크에서 중첩된 어휘를 가진 모델이 더 나은 성능을 보였고, 중첩이 증가할수록 전이 성능이 향상되었습니다. 결론적으로, 토큰 중첩은 다국어 모델에서 유리하며, 공유 어휘를 사용하는 것이 유익한 설계 선택임을 강조합니다.

## 🎯 주요 포인트

- 1. 다국어 코퍼스에서 학습된 서브워드 토크나이저는 자연스럽게 언어 간 중복 토큰을 생성한다.
- 2. 중복 토큰은 교차 언어 전이에 유리하며, 언어 간 의미적 관계를 포착하는 임베딩 공간을 형성한다.
- 3. XNLI와 XQuAD 실험에서 중복 토큰을 가진 모델이 비중복 모델보다 우수한 성능을 보였다.
- 4. 어휘 중복이 증가할수록 전이 성능이 향상되는 경향을 보인다.
- 5. 다국어 모델에서 상당한 공유 어휘는 유리한 설계 선택임을 강조한다.


---

*Generated on 2025-09-24 15:42:28*