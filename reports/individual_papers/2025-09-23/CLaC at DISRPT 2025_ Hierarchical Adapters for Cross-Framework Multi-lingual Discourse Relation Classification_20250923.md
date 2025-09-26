---
keywords:
  - Hierarchical Dual-Adapter Contrastive Learning
  - Discourse Relation Classification
  - Large Language Model
  - Few-Shot Learning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16903
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:20:03.768004",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hierarchical Dual-Adapter Contrastive Learning",
    "Discourse Relation Classification",
    "Large Language Model",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hierarchical Dual-Adapter Contrastive Learning": 0.78,
    "Discourse Relation Classification": 0.82,
    "Large Language Model": 0.75,
    "Few-Shot Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hierarchical Dual-Adapter Contrastive learning",
        "canonical": "Hierarchical Dual-Adapter Contrastive Learning",
        "aliases": [
          "HiDAC"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel model introduced in the paper, offering a unique approach to discourse relation classification.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Discourse Relation Classification",
        "canonical": "Discourse Relation Classification",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus, it connects to broader discourse analysis topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Key technology evaluated in the paper, relevant for linking to broader NLP and AI discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Zero-shot and Few-shot settings",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Zero-Shot Learning"
        ],
        "category": "specific_connectable",
        "rationale": "These learning paradigms are significant for understanding model adaptability and performance.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "Task 3",
      "DISRPT 2025",
      "mBERT",
      "XLM-RoBERTa"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hierarchical Dual-Adapter Contrastive learning",
      "resolved_canonical": "Hierarchical Dual-Adapter Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Discourse Relation Classification",
      "resolved_canonical": "Discourse Relation Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Zero-shot and Few-shot settings",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# CLaC at DISRPT 2025: Hierarchical Adapters for Cross-Framework Multi-lingual Discourse Relation Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16903.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16903](https://arxiv.org/abs/2509.16903)

## 🔗 유사한 논문
- [[2025-09-23/CorefInst_ Leveraging LLMs for Multilingual Coreference Resolution_20250923|CorefInst: Leveraging LLMs for Multilingual Coreference Resolution]] (82.7% similar)
- [[2025-09-23/Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification_20250923|Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification]] (81.9% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (81.3% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (81.1% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Discourse Relation Classification|Discourse Relation Classification]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Hierarchical Dual-Adapter Contrastive Learning|Hierarchical Dual-Adapter Contrastive Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16903v1 Announce Type: new 
Abstract: We present our submission to Task 3 (Discourse Relation Classification) of the DISRPT 2025 shared task. Task 3 introduces a unified set of 17 discourse relation labels across 39 corpora in 16 languages and six discourse frameworks, posing significant multilingual and cross-formalism challenges. We first benchmark the task by fine-tuning multilingual BERT-based models (mBERT, XLM-RoBERTa-Base, and XLM-RoBERTa-Large) with two argument-ordering strategies and progressive unfreezing ratios to establish strong baselines. We then evaluate prompt-based large language models (namely Claude Opus 4.0) in zero-shot and few-shot settings to understand how LLMs respond to the newly proposed unified labels. Finally, we introduce HiDAC, a Hierarchical Dual-Adapter Contrastive learning model. Results show that while larger transformer models achieve higher accuracy, the improvements are modest, and that unfreezing the top 75% of encoder layers yields performance comparable to full fine-tuning while training far fewer parameters. Prompt-based models lag significantly behind fine-tuned transformers, and HiDAC achieves the highest overall accuracy (67.5%) while remaining more parameter-efficient than full fine-tuning.

## 📝 요약

이 논문은 DISRPT 2025 공유 과제의 Task 3인 담화 관계 분류에 대한 연구를 다룹니다. 16개 언어와 6개의 담화 체계를 포함한 39개의 코퍼스에서 17개의 담화 관계 레이블을 통합하여 다언어 및 교차 형식 문제를 제시합니다. 연구에서는 다국어 BERT 기반 모델(mBERT, XLM-RoBERTa-Base, XLM-RoBERTa-Large)을 미세 조정하여 강력한 기준선을 설정하고, 프롬프트 기반 대형 언어 모델(Claude Opus 4.0)을 평가하여 새로운 레이블에 대한 반응을 분석합니다. 또한, HiDAC라는 계층적 이중 어댑터 대조 학습 모델을 소개합니다. 결과적으로, 대형 트랜스포머 모델이 더 높은 정확도를 보이지만, 개선 폭은 크지 않으며, 인코더 층의 75%를 해제하는 것이 전체 미세 조정과 유사한 성능을 보이면서도 더 적은 매개변수를 학습합니다. 프롬프트 기반 모델은 미세 조정된 트랜스포머보다 성능이 떨어지며, HiDAC는 전체 미세 조정보다 더 효율적인 매개변수로 최고 정확도(67.5%)를 달성합니다.

## 🎯 주요 포인트

- 1. Task 3에서는 16개 언어와 6개의 담화 프레임워크를 아우르는 17개의 통합 담화 관계 레이블을 도입하여 다국어 및 교차 형식 도전 과제를 제시합니다.
- 2. mBERT, XLM-RoBERTa-Base, XLM-RoBERTa-Large 모델을 미세 조정하여 강력한 기준선을 설정했습니다.
- 3. Claude Opus 4.0과 같은 대형 언어 모델을 제로샷 및 퓨샷 설정에서 평가하여 새로운 통합 레이블에 대한 반응을 분석했습니다.
- 4. HiDAC 모델은 전체 미세 조정보다 더 적은 매개변수를 사용하면서도 67.5%의 최고 정확도를 달성했습니다.
- 5. 프롬프트 기반 모델은 미세 조정된 트랜스포머 모델에 비해 성능이 상당히 뒤처졌습니다.


---

*Generated on 2025-09-24 03:20:03*