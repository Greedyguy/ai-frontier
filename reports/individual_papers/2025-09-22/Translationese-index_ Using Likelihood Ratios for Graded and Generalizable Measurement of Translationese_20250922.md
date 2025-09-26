---
keywords:
  - Translationese
  - Translationese-Index
  - Likelihood Ratios
  - Fine-Tuned Language Models
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2507.12260
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:49:30.806422",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Translationese",
    "Translationese-Index",
    "Likelihood Ratios",
    "Fine-Tuned Language Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Translationese": 0.8,
    "Translationese-Index": 0.85,
    "Likelihood Ratios": 0.7,
    "Fine-Tuned Language Models": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "translationese",
        "canonical": "Translationese",
        "aliases": [
          "translated text properties"
        ],
        "category": "unique_technical",
        "rationale": "Translationese is a unique linguistic property relevant to translation studies and not covered by existing metrics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "translationese-index",
        "canonical": "Translationese-Index",
        "aliases": [
          "T-index"
        ],
        "category": "unique_technical",
        "rationale": "The Translationese-Index is a novel metric for measuring translationese, offering a new dimension to translation quality assessment.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "likelihood ratios",
        "canonical": "Likelihood Ratios",
        "aliases": [
          "probability ratios"
        ],
        "category": "broad_technical",
        "rationale": "Likelihood ratios are a fundamental statistical concept used in the computation of the Translationese-Index.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "fine-tuned language models",
        "canonical": "Fine-Tuned Language Models",
        "aliases": [
          "fine-tuned LMs"
        ],
        "category": "specific_connectable",
        "rationale": "Fine-tuned language models are crucial for the computation of the Translationese-Index, linking to broader NLP applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "cross-domain settings",
      "human judgments",
      "synthetic data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "translationese",
      "resolved_canonical": "Translationese",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "translationese-index",
      "resolved_canonical": "Translationese-Index",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "likelihood ratios",
      "resolved_canonical": "Likelihood Ratios",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "fine-tuned language models",
      "resolved_canonical": "Fine-Tuned Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Translationese-index: Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese

**Korean Title:** 번역체 지수: 번역체의 등급화 및 일반화 가능한 측정을 위한 가능도 비율의 사용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2507.12260.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2507.12260](https://arxiv.org/abs/2507.12260)

## 🔗 유사한 논문
- [[2025-09-19/Translate, then Detect_ Leveraging Machine Translation for Cross-Lingual Toxicity Classification_20250919|Translate, then Detect: Leveraging Machine Translation for Cross-Lingual Toxicity Classification]] (80.6% similar)
- [[2025-09-18/Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (80.1% similar)
- [[2025-09-17/Long-context Reference-based MT Quality Estimation_20250917|Long-context Reference-based MT Quality Estimation]] (79.7% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (78.8% similar)
- [[2025-09-22/BBScoreV2_ Learning Time-Evolution and Latent Alignment from Stochastic Representation_20250922|BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Likelihood Ratios|Likelihood Ratios]]
**🔗 Specific Connectable**: [[keywords/Fine-Tuned Language Models|Fine-Tuned Language Models]]
**⚡ Unique Technical**: [[keywords/Translationese|Translationese]], [[keywords/Translationese-Index|Translationese-Index]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.12260v2 Announce Type: replace 
Abstract: Translationese refers to linguistic properties that usually occur in translated texts. Previous works study translationese by framing it as a binary classification between original texts and translated texts. In this paper, we argue that translationese should be graded instead of binary and propose the first measure for translationese -- the translationese-index (T-index), computed from the likelihood ratios of two contrastively fine-tuned language models (LMs). We use synthesized translations and translations in the wild to evaluate T-index's generalizability in cross-domain settings and its validity against human judgments. Our results show that T-index can generalize to unseen genres, authors, and language pairs. Moreover, T-index computed using two 0.5B LMs fine-tuned on only 1-5k pairs of synthetic data can effectively capture translationese, as demonstrated by alignment with human pointwise ratings and pairwise judgments. Additionally, the correlation between T-index and existing machine translation (MT) quality estimation (QE) metrics such as BLEU and COMET is low, suggesting that T-index is not covered by these metrics and can serve as a complementary metric in MT QE.

## 🔍 Abstract (한글 번역)

arXiv:2507.12260v2 발표 유형: 교체  
초록: 번역체는 번역된 텍스트에서 주로 나타나는 언어적 특성을 의미합니다. 이전 연구들은 번역체를 원본 텍스트와 번역된 텍스트 간의 이진 분류로 다루었습니다. 본 논문에서는 번역체를 이진이 아닌 등급화해야 한다고 주장하며, 번역체를 측정하는 첫 번째 지표인 번역체 지수(T-index)를 제안합니다. T-index는 두 개의 대조적으로 미세 조정된 언어 모델(LM)의 가능도 비율로 계산됩니다. 우리는 합성 번역과 실제 번역을 사용하여 T-index의 도메인 간 설정에서의 일반화 가능성과 인간 판단에 대한 유효성을 평가합니다. 우리의 결과는 T-index가 보지 못한 장르, 저자 및 언어 쌍에 일반화될 수 있음을 보여줍니다. 더욱이, 0.5B LMs 두 개를 사용하여 1-5k 쌍의 합성 데이터로 미세 조정한 T-index는 인간의 점별 평가 및 쌍별 판단과의 일치를 통해 번역체를 효과적으로 포착할 수 있음을 보여줍니다. 또한, T-index와 기존의 기계 번역(MT) 품질 평가(QE) 지표인 BLEU 및 COMET 간의 상관관계가 낮아, T-index가 이러한 지표에 의해 포괄되지 않으며 MT QE에서 보완적인 지표로 활용될 수 있음을 시사합니다.

## 📝 요약

이 논문은 번역체의 특성을 이진 분류가 아닌 등급화해야 한다고 주장하며, 번역체를 측정하는 새로운 지표인 번역체 지수(T-index)를 제안합니다. T-index는 대조적으로 미세 조정된 두 개의 언어 모델(LM)의 가능성 비율을 기반으로 계산됩니다. 연구는 합성 번역과 실제 번역을 사용하여 T-index의 범용성과 인간 판단과의 일치성을 평가했습니다. 결과적으로 T-index는 새로운 장르, 저자, 언어 쌍에 일반화될 수 있으며, 인간의 평가와 일치함을 보였습니다. 또한, T-index는 기존의 기계 번역 품질 평가 지표(BLEU, COMET)와 낮은 상관관계를 보여, 이 지표들을 보완할 수 있는 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 번역체는 이진 분류가 아닌 등급화되어야 한다고 주장하며, 이를 측정하기 위한 T-index를 제안한다.
- 2. T-index는 두 개의 대조적 미세 조정된 언어 모델의 가능성 비율을 통해 계산된다.
- 3. T-index는 새로운 장르, 저자, 언어 쌍에 대해 일반화할 수 있으며, 인간의 판단과의 정렬을 통해 번역체를 효과적으로 포착할 수 있다.
- 4. T-index는 기존의 기계 번역 품질 평가 지표인 BLEU 및 COMET과 상관관계가 낮아, 보완적인 지표로 활용될 수 있다.
- 5. T-index는 1-5k 쌍의 합성 데이터를 사용하여 미세 조정된 두 개의 0.5B 언어 모델로도 효과적으로 번역체를 포착할 수 있다.


---

*Generated on 2025-09-23 11:49:30*