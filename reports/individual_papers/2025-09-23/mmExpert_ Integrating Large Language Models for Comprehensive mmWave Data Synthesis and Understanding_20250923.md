---
keywords:
  - Large Language Model
  - mmWave Sensing Technology
  - Zero-Shot Learning
  - Synthetic mmWave Radar Datasets
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16521
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:39:20.806962",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "mmWave Sensing Technology",
    "Zero-Shot Learning",
    "Synthetic mmWave Radar Datasets"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "mmWave Sensing Technology": 0.78,
    "Zero-Shot Learning": 0.81,
    "Synthetic mmWave Radar Datasets": 0.75
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
        "rationale": "Large Language Models are central to the framework's data generation process, linking to existing knowledge on LLMs.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "mmWave sensing technology",
        "canonical": "mmWave Sensing Technology",
        "aliases": [
          "mmWave",
          "Millimeter-wave sensing"
        ],
        "category": "unique_technical",
        "rationale": "This is a core technology discussed in the paper, essential for understanding the application context.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-shot generalization",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot generalization"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot generalization is a key outcome of the framework, connecting to broader discussions on learning paradigms.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.77,
        "link_intent_score": 0.81
      },
      {
        "surface": "Synthetic mmWave radar datasets",
        "canonical": "Synthetic mmWave Radar Datasets",
        "aliases": [
          "Synthetic datasets",
          "mmWave datasets"
        ],
        "category": "unique_technical",
        "rationale": "The creation of synthetic datasets is a novel contribution of the paper, enhancing data availability for model training.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "data acquisition",
      "performance",
      "experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "mmWave sensing technology",
      "resolved_canonical": "mmWave Sensing Technology",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-shot generalization",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.77,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Synthetic mmWave radar datasets",
      "resolved_canonical": "Synthetic mmWave Radar Datasets",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# mmExpert: Integrating Large Language Models for Comprehensive mmWave Data Synthesis and Understanding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16521.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16521](https://arxiv.org/abs/2509.16521)

## 🔗 유사한 논문
- [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (84.7% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.2% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (84.2% similar)
- [[2025-09-23/SignalLLM_ A General-Purpose LLM Agent Framework for Automated Signal Processing_20250923|SignalLLM: A General-Purpose LLM Agent Framework for Automated Signal Processing]] (83.5% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/mmWave Sensing Technology|mmWave Sensing Technology]], [[keywords/Synthetic mmWave Radar Datasets|Synthetic mmWave Radar Datasets]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16521v1 Announce Type: new 
Abstract: Millimeter-wave (mmWave) sensing technology holds significant value in human-centric applications, yet the high costs associated with data acquisition and annotation limit its widespread adoption in our daily lives. Concurrently, the rapid evolution of large language models (LLMs) has opened up opportunities for addressing complex human needs. This paper presents mmExpert, an innovative mmWave understanding framework consisting of a data generation flywheel that leverages LLMs to automate the generation of synthetic mmWave radar datasets for specific application scenarios, thereby training models capable of zero-shot generalization in real-world environments. Extensive experiments demonstrate that the data synthesized by mmExpert significantly enhances the performance of downstream models and facilitates the successful deployment of large models for mmWave understanding.

## 📝 요약

이 논문은 mmWave 센싱 기술의 활용을 촉진하기 위해 mmExpert라는 프레임워크를 제안합니다. 이 프레임워크는 대형 언어 모델(LLM)을 활용하여 특정 응용 시나리오에 맞춘 합성 mmWave 레이더 데이터셋을 자동으로 생성합니다. 이를 통해 실제 환경에서 제로샷 일반화가 가능한 모델을 훈련할 수 있습니다. 실험 결과, mmExpert가 생성한 데이터가 하위 모델의 성능을 크게 향상시키고, 대형 모델의 mmWave 이해를 성공적으로 지원함을 보여줍니다.

## 🎯 주요 포인트

- 1. mmWave 센싱 기술은 인간 중심의 응용 분야에서 중요한 가치를 지니지만, 데이터 획득 및 주석의 높은 비용이 일상적인 활용을 제한한다.
- 2. 대형 언어 모델(LLM)의 빠른 발전은 복잡한 인간의 요구를 해결할 수 있는 기회를 제공한다.
- 3. mmExpert는 LLM을 활용하여 특정 응용 시나리오에 맞춘 합성 mmWave 레이더 데이터셋을 자동 생성하는 데이터 생성 플라이휠을 포함한 혁신적인 mmWave 이해 프레임워크이다.
- 4. mmExpert가 생성한 데이터는 다운스트림 모델의 성능을 크게 향상시키고, 대형 모델의 mmWave 이해를 위한 성공적인 배포를 촉진한다.
- 5. 제로샷 일반화가 가능한 모델을 훈련하여 실제 환경에서의 적용을 가능하게 한다.


---

*Generated on 2025-09-24 01:39:20*