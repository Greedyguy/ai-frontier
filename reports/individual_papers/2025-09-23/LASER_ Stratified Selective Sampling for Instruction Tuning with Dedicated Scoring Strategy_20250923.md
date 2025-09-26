---
keywords:
  - Large Language Model
  - Instruction Tuning
  - Data Selection
  - Embedding Model
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.22157
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:00:38.526489",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Instruction Tuning",
    "Data Selection",
    "Embedding Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Instruction Tuning": 0.82,
    "Data Selection": 0.75,
    "Embedding Model": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion on data selection and fine-tuning, providing a strong link to existing literature.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Instruction Tuning",
        "canonical": "Instruction Tuning",
        "aliases": [
          "Instruction Fine-tuning"
        ],
        "category": "unique_technical",
        "rationale": "Instruction Tuning is a specific technique discussed in the paper, offering a novel approach to model fine-tuning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Data Selection",
        "canonical": "Data Selection",
        "aliases": [
          "Data Sampling",
          "Data Filtering"
        ],
        "category": "specific_connectable",
        "rationale": "Data Selection is a key process in the paper's methodology, linking to broader themes of efficient data usage in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Embedding Models",
        "canonical": "Embedding Model",
        "aliases": [
          "Embedding Techniques"
        ],
        "category": "specific_connectable",
        "rationale": "Embedding Models are used to improve diversity in data selection, connecting to established methods in NLP.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
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
        "connectivity": 0.89,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Instruction Tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Data Selection",
      "resolved_canonical": "Data Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Embedding Models",
      "resolved_canonical": "Embedding Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# LASER: Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.22157.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.22157](https://arxiv.org/abs/2505.22157)

## 🔗 유사한 논문
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (87.9% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (85.2% similar)
- [[2025-09-23/Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning_20250923|Mitigating Forgetting in LLM Fine-Tuning via Low-Perplexity Token Learning]] (85.1% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (85.1% similar)
- [[2025-09-17/Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning_20250917|Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Data Selection|Data Selection]], [[keywords/Embedding Model|Embedding Model]]
**⚡ Unique Technical**: [[keywords/Instruction Tuning|Instruction Tuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22157v2 Announce Type: replace 
Abstract: Recent work shows that post-training datasets for LLMs can be substantially downsampled without noticeably deteriorating performance. However, data selection often incurs high computational costs or is limited to narrow domains. In this paper, we demonstrate that data selection can be both -- efficient and universal -- by using a multi-step pipeline in which we efficiently bin data points into groups, estimate quality using specialized models, and score difficulty with a robust, lightweight method. Task-based categorization allows us to control the composition of our final data -- crucial for finetuning multi-purpose models. To guarantee diversity, we improve upon previous work using embedding models and a clustering algorithm. This integrated strategy enables high-performance fine-tuning with minimal overhead.

## 📝 요약

최근 연구에 따르면 대형 언어 모델(LLM)의 후처리 데이터셋을 크게 축소해도 성능 저하가 거의 없다고 합니다. 그러나 데이터 선택은 높은 계산 비용이 들거나 특정 분야에 제한되는 경우가 많습니다. 본 논문에서는 데이터 선택이 효율적이고 범용적일 수 있음을 보여줍니다. 우리는 데이터를 그룹으로 나누고, 특수 모델로 품질을 추정하며, 경량 방법으로 난이도를 평가하는 다단계 파이프라인을 사용합니다. 작업 기반 분류를 통해 다목적 모델의 최종 데이터 구성을 제어할 수 있습니다. 다양성을 보장하기 위해 임베딩 모델과 클러스터링 알고리즘을 사용하여 이전 연구를 개선했습니다. 이 통합 전략은 최소한의 오버헤드로 고성능 미세 조정을 가능하게 합니다.

## 🎯 주요 포인트

- 1. LLM의 사후 훈련 데이터셋을 성능 저하 없이 크게 다운샘플링할 수 있음이 최근 연구에서 밝혀졌다.
- 2. 데이터 선택은 높은 계산 비용이 들거나 좁은 도메인에 제한되는 경우가 많다.
- 3. 본 논문에서는 데이터를 효율적으로 그룹화하고, 품질을 전문 모델로 추정하며, 경량 방법으로 난이도를 평가하는 다단계 파이프라인을 제안한다.
- 4. 임베딩 모델과 클러스터링 알고리즘을 사용하여 데이터 다양성을 보장하고, 다목적 모델의 미세 조정을 위한 데이터 구성을 제어한다.
- 5. 통합 전략을 통해 최소한의 오버헤드로 고성능 미세 조정을 가능하게 한다.


---

*Generated on 2025-09-24 04:00:38*