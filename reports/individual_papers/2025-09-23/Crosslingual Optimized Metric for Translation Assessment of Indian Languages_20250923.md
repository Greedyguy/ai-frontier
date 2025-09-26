---
keywords:
  - COMTAIL
  - Neural Translation Metric
  - Human Evaluation Dataset
  - BLEU
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17667
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:30:44.100935",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "COMTAIL",
    "Neural Translation Metric",
    "Human Evaluation Dataset",
    "BLEU"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "COMTAIL": 0.88,
    "Neural Translation Metric": 0.72,
    "Human Evaluation Dataset": 0.78,
    "BLEU": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cross-lingual Optimized Metric for Translation Assessment of Indian Languages",
        "canonical": "COMTAIL",
        "aliases": [
          "Cross-lingual Optimized Metric",
          "Translation Assessment Metric"
        ],
        "category": "unique_technical",
        "rationale": "COMTAIL is a novel metric specifically designed for evaluating translations involving Indian languages, offering unique insights and connections in multilingual NLP research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "neural translation evaluation metric",
        "canonical": "Neural Translation Metric",
        "aliases": [
          "Neural Evaluation Metric"
        ],
        "category": "broad_technical",
        "rationale": "This connects to broader discussions on neural approaches in translation evaluation, which is a significant area in NLP.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "human evaluation ratings dataset",
        "canonical": "Human Evaluation Dataset",
        "aliases": [
          "Human Ratings Dataset"
        ],
        "category": "specific_connectable",
        "rationale": "Datasets are critical for training and evaluating models, and this specific dataset enhances connectivity in translation evaluation research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "BLEU",
        "canonical": "BLEU",
        "aliases": [
          "BLEU Score"
        ],
        "category": "specific_connectable",
        "rationale": "BLEU is a widely recognized metric in translation evaluation, providing strong connectivity to existing research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "automatic evaluation",
      "translation pairs",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cross-lingual Optimized Metric for Translation Assessment of Indian Languages",
      "resolved_canonical": "COMTAIL",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "neural translation evaluation metric",
      "resolved_canonical": "Neural Translation Metric",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "human evaluation ratings dataset",
      "resolved_canonical": "Human Evaluation Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "BLEU",
      "resolved_canonical": "BLEU",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Crosslingual Optimized Metric for Translation Assessment of Indian Languages

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17667.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17667](https://arxiv.org/abs/2509.17667)

## 🔗 유사한 논문
- [[2025-09-23/DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India_ Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context_20250923|DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context]] (81.1% similar)
- [[2025-09-23/Fluent but Foreign_ Even Regional LLMs Lack Cultural Alignment_20250923|Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment]] (79.8% similar)
- [[2025-09-17/Long-context Reference-based MT Quality Estimation_20250917|Long-context Reference-based MT Quality Estimation]] (79.6% similar)
- [[2025-09-22/Translationese-index_ Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese_20250922|Translationese-index: Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese]] (79.5% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Translation Metric|Neural Translation Metric]]
**🔗 Specific Connectable**: [[keywords/Human Evaluation Dataset|Human Evaluation Dataset]], [[keywords/BLEU|BLEU]]
**⚡ Unique Technical**: [[keywords/COMTAIL|COMTAIL]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17667v1 Announce Type: new 
Abstract: Automatic evaluation of translation remains a challenging task owing to the orthographic, morphological, syntactic and semantic richness and divergence observed across languages. String-based metrics such as BLEU have previously been extensively used for automatic evaluation tasks, but their limitations are now increasingly recognized. Although learned neural metrics have helped mitigate some of the limitations of string-based approaches, they remain constrained by a paucity of gold evaluation data in most languages beyond the usual high-resource pairs. In this present work we address some of these gaps. We create a large human evaluation ratings dataset for 13 Indian languages covering 21 translation directions and then train a neural translation evaluation metric named Cross-lingual Optimized Metric for Translation Assessment of Indian Languages (COMTAIL) on this dataset. The best performing metric variants show significant performance gains over previous state-of-the-art when adjudging translation pairs with at least one Indian language. Furthermore, we conduct a series of ablation studies to highlight the sensitivities of such a metric to changes in domain, translation quality, and language groupings. We release both the COMTAIL dataset and the accompanying metric models.

## 📝 요약

이 연구는 13개의 인도 언어와 21개의 번역 방향을 포함한 대규모 인간 평가 데이터셋을 구축하고, 이를 기반으로 인도 언어 번역 평가를 위한 신경망 기반 평가 지표인 COMTAIL을 개발했습니다. COMTAIL은 기존의 최고 성능 지표보다 인도 언어가 포함된 번역 쌍 평가에서 우수한 성능을 보였습니다. 또한, 도메인, 번역 품질, 언어 그룹 변화에 대한 민감도를 분석하는 소거 연구를 수행했습니다. 연구 결과로 COMTAIL 데이터셋과 모델을 공개했습니다.

## 🎯 주요 포인트

- 1. 번역의 자동 평가에서 BLEU와 같은 문자열 기반 지표의 한계가 인식되고 있으며, 이를 보완하기 위해 신경망 기반 지표가 사용되고 있습니다.
- 2. 대부분의 언어에서 금 평가 데이터의 부족으로 인해 신경망 기반 지표의 제약이 존재합니다.
- 3. 본 연구에서는 13개의 인도 언어와 21개의 번역 방향을 포함하는 대규모 인간 평가 데이터셋을 생성하고, 이를 기반으로 COMTAIL이라는 신경망 번역 평가 지표를 개발했습니다.
- 4. COMTAIL은 최소 하나의 인도 언어가 포함된 번역 쌍 평가에서 이전 최첨단 성능을 능가하는 성과를 보였습니다.
- 5. 도메인, 번역 품질, 언어 그룹의 변화에 대한 민감성을 강조하기 위해 일련의 소거 연구를 수행했습니다.


---

*Generated on 2025-09-24 03:30:44*