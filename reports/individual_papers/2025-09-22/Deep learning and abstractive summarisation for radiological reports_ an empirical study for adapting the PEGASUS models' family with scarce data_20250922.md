---
keywords:
  - Deep Learning
  - Abstractive Summarization
  - PEGASUS Model
  - Model Fine-Tuning
  - Radiological Reports
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15419
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:56:05.341344",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Abstractive Summarization",
    "PEGASUS Model",
    "Model Fine-Tuning",
    "Radiological Reports"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Abstractive Summarization": 0.88,
    "PEGASUS Model": 0.8,
    "Model Fine-Tuning": 0.82,
    "Radiological Reports": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational concept that connects to numerous advancements in AI and summarization models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "abstractive summarisation",
        "canonical": "Abstractive Summarization",
        "aliases": [
          "abstractive summarization"
        ],
        "category": "specific_connectable",
        "rationale": "Abstractive Summarization is a key technique in NLP that directly relates to the paper's focus on summarizing radiological reports.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "PEGASUS",
        "canonical": "PEGASUS Model",
        "aliases": [
          "PEGASUS-X"
        ],
        "category": "unique_technical",
        "rationale": "The PEGASUS Model is central to the study and represents a specific application of deep learning in summarization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "fine-tuning",
        "canonical": "Model Fine-Tuning",
        "aliases": [
          "fine tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Model Fine-Tuning is a critical process in adapting models to specific domains, which is a major theme of the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "radiological reports",
        "canonical": "Radiological Reports",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Radiological Reports are the specific domain of application for the summarization models discussed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "model",
      "performance",
      "training data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "abstractive summarisation",
      "resolved_canonical": "Abstractive Summarization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "PEGASUS",
      "resolved_canonical": "PEGASUS Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "fine-tuning",
      "resolved_canonical": "Model Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "radiological reports",
      "resolved_canonical": "Radiological Reports",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Deep learning and abstractive summarisation for radiological reports: an empirical study for adapting the PEGASUS models' family with scarce data

**Korean Title:** 심층 학습과 추상적 요약을 통한 방사선 보고서: 제한된 데이터로 PEGASUS 모델 계열을 적응시키기 위한 실증적 연구

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15419.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15419](https://arxiv.org/abs/2509.15419)

## 🔗 유사한 논문
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (82.5% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence: Label Quality, Domain Shift, Bias and Evaluation Challenges]] (82.5% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (81.7% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (81.6% similar)
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Abstractive Summarization|Abstractive Summarization]], [[keywords/Model Fine-Tuning|Model Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/PEGASUS Model|PEGASUS Model]], [[keywords/Radiological Reports|Radiological Reports]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15419v1 Announce Type: cross 
Abstract: Regardless of the rapid development of artificial intelligence, abstractive summarisation is still challenging for sensitive and data-restrictive domains like medicine. With the increasing number of imaging, the relevance of automated tools for complex medical text summarisation is expected to become highly relevant. In this paper, we investigated the adaptation via fine-tuning process of a non-domain-specific abstractive summarisation encoder-decoder model family, and gave insights to practitioners on how to avoid over- and underfitting. We used PEGASUS and PEGASUS-X, on a medium-sized radiological reports public dataset. For each model, we comprehensively evaluated two different checkpoints with varying sizes of the same training data. We monitored the models' performances with lexical and semantic metrics during the training history on the fixed-size validation set. PEGASUS exhibited different phases, which can be related to epoch-wise double-descent, or peak-drop-recovery behaviour. For PEGASUS-X, we found that using a larger checkpoint led to a performance detriment. This work highlights the challenges and risks of fine-tuning models with high expressivity when dealing with scarce training data, and lays the groundwork for future investigations into more robust fine-tuning strategies for summarisation models in specialised domains.

## 🔍 Abstract (한글 번역)

arXiv:2509.15419v1 발표 유형: 교차  
초록: 인공지능의 급속한 발전에도 불구하고, 의학과 같은 민감하고 데이터 제한적인 분야에서는 추상적 요약이 여전히 도전 과제로 남아 있습니다. 이미지의 증가와 함께 복잡한 의학 텍스트 요약을 위한 자동화 도구의 중요성이 더욱 커질 것으로 예상됩니다. 본 논문에서는 비전문 분야 추상적 요약 인코더-디코더 모델 계열의 적응을 미세 조정 과정을 통해 조사하고, 과적합과 과소적합을 피하는 방법에 대한 통찰을 실무자에게 제공했습니다. 중간 규모의 방사선 보고서 공개 데이터셋에서 PEGASUS와 PEGASUS-X를 사용했습니다. 각 모델에 대해 동일한 훈련 데이터의 크기를 달리하여 두 개의 다른 체크포인트를 종합적으로 평가했습니다. 고정 크기의 검증 세트에서 훈련 기록 동안 어휘 및 의미적 지표로 모델의 성능을 모니터링했습니다. PEGASUS는 에포크별 이중 하강 또는 피크-드롭-회복 행동과 관련될 수 있는 다양한 단계를 보였습니다. PEGASUS-X의 경우, 더 큰 체크포인트를 사용하는 것이 성능 저하로 이어진다는 것을 발견했습니다. 이 연구는 훈련 데이터가 부족한 상황에서 높은 표현력을 가진 모델을 미세 조정할 때의 도전과 위험을 강조하고, 전문 분야에서 요약 모델을 위한 보다 견고한 미세 조정 전략에 대한 향후 연구의 기초를 마련합니다.

## 📝 요약

이 논문은 의료 분야와 같은 민감하고 데이터가 제한적인 영역에서 추상적 요약의 어려움을 다룹니다. 저자들은 비전문 분야의 추상적 요약 모델인 PEGASUS와 PEGASUS-X를 방사선 보고서 데이터셋에 맞춰 미세 조정하여 적용했습니다. 두 모델의 성능을 다양한 데이터 크기에서 평가했으며, 특히 PEGASUS는 학습 과정에서 이중 하강 및 회복 패턴을 보였습니다. PEGASUS-X는 큰 체크포인트 사용 시 성능 저하가 발생했습니다. 이 연구는 제한된 데이터로 고성능 모델을 미세 조정할 때의 위험성을 강조하며, 전문 분야 요약 모델의 향후 연구 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 인공지능의 급속한 발전에도 불구하고, 의학과 같은 민감하고 데이터 제한적인 분야에서의 추상적 요약은 여전히 도전적이다.
- 2. 본 연구는 비도메인 특화 추상적 요약 인코더-디코더 모델의 미세 조정을 통해 적응을 조사하고, 과적합 및 과소적합을 피하는 방법에 대한 통찰을 제공하였다.
- 3. PEGASUS와 PEGASUS-X 모델을 사용하여 중간 크기의 방사선 보고서 공개 데이터셋에서 두 가지 다른 체크포인트를 평가하였다.
- 4. PEGASUS는 에포크별 더블 디센트 또는 피크-드롭-회복 행동과 관련된 다양한 단계를 보였다.
- 5. PEGASUS-X의 경우, 더 큰 체크포인트를 사용할 때 성능 저하가 발생함을 발견하였다.


---

*Generated on 2025-09-23 08:56:05*