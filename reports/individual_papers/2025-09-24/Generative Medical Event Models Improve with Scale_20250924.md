<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:38:05.875338",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Comet Model",
    "Foundation Model",
    "Medical Event Data",
    "Scaling Law Study",
    "Real-World Tasks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Comet Model": 0.78,
    "Foundation Model": 0.8,
    "Medical Event Data": 0.77,
    "Scaling Law Study": 0.75,
    "Real-World Tasks": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Comet models",
        "canonical": "Comet Model",
        "aliases": [
          "Comet",
          "Comet Models"
        ],
        "category": "unique_technical",
        "rationale": "The Comet Model is a central focus of the paper, representing a novel approach in generative medical event modeling.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Foundation models",
        "canonical": "Foundation Model",
        "aliases": [
          "Foundation Models"
        ],
        "category": "broad_technical",
        "rationale": "Foundation models are a key concept in scaling real-world evidence generation and are widely applicable across various tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Medical event data",
        "canonical": "Medical Event Data",
        "aliases": [
          "Medical Events",
          "Event Data"
        ],
        "category": "specific_connectable",
        "rationale": "Medical event data is crucial for understanding patient journeys and is a foundational element of the study.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Scaling-law study",
        "canonical": "Scaling Law Study",
        "aliases": [
          "Scaling Study",
          "Scaling Laws"
        ],
        "category": "unique_technical",
        "rationale": "The scaling-law study provides insights into the relationships between compute, tokens, and model size, which are pivotal for model optimization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Real-world tasks",
        "canonical": "Real-World Tasks",
        "aliases": [
          "Real World Tasks",
          "Practical Tasks"
        ],
        "category": "specific_connectable",
        "rationale": "Real-world tasks are essential for evaluating the model's performance across diverse applications.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.74
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
      "candidate_surface": "Comet models",
      "resolved_canonical": "Comet Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Foundation models",
      "resolved_canonical": "Foundation Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Medical event data",
      "resolved_canonical": "Medical Event Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Scaling-law study",
      "resolved_canonical": "Scaling Law Study",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Real-world tasks",
      "resolved_canonical": "Real-World Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Generative Medical Event Models Improve with Scale

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.12104.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2508.12104](https://arxiv.org/abs/2508.12104)

## 🔗 유사한 논문
- [[2025-09-23/ReasonMed_ A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning_20250923|ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning]] (80.2% similar)
- [[2025-09-23/Search-Optimized Quantization in Biomedical Ontology Alignment_20250923|Search-Optimized Quantization in Biomedical Ontology Alignment]] (79.6% similar)
- [[2025-09-23/MIRA_ Medical Time Series Foundation Model for Real-World Health Data_20250923|MIRA: Medical Time Series Foundation Model for Real-World Health Data]] (79.4% similar)
- [[2025-09-24/Citrus-V_ Advancing Medical Foundation Models with Unified Medical Image Grounding for Clinical Reasoning_20250924|Citrus-V: Advancing Medical Foundation Models with Unified Medical Image Grounding for Clinical Reasoning]] (78.7% similar)
- [[2025-09-23/Learning Massive-scale Partial Correlation Networks in Clinical Multi-omics Studies with HP-ACCORD_20250923|Learning Massive-scale Partial Correlation Networks in Clinical Multi-omics Studies with HP-ACCORD]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Foundation Model|Foundation Model]]
**🔗 Specific Connectable**: [[keywords/Medical Event Data|Medical Event Data]], [[keywords/Real-World Tasks|Real-World Tasks]]
**⚡ Unique Technical**: [[keywords/Comet Model|Comet Model]], [[keywords/Scaling Law Study|Scaling Law Study]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.12104v2 Announce Type: replace-cross 
Abstract: Realizing personalized medicine at scale calls for methods that distill insights from longitudinal patient journeys, which can be viewed as a sequence of medical events. Foundation models pretrained on large-scale medical event data represent a promising direction for scaling real-world evidence generation and generalizing to diverse downstream tasks. Using Epic Cosmos, a dataset with medical events from de-identified longitudinal health records for 16.3 billion encounters over 300 million unique patient records from 310 health systems, we introduce the Comet models, a family of decoder-only transformer models pretrained on 118 million patients representing 115 billion discrete medical events (151 billion tokens). We present the largest scaling-law study of medical event data, establishing a methodology for pretraining and revealing power-law scaling relationships for compute, tokens, and model size. Consequently, we pretrained a series of compute-optimal models with up to 1 billion parameters. Conditioned on a patient's real-world history, Comet autoregressively predicts the next medical event to simulate patient health timelines. We studied 78 real-world tasks, including diagnosis prediction, disease prognosis, and healthcare operations. Remarkably for a foundation model with generic pretraining and simulation-based inference, Comet generally outperformed or matched task-specific supervised models on these tasks, without requiring task-specific fine-tuning or few-shot examples. Comet's predictive power consistently improves as the model and pretraining scale. Our results show that Comet, a generative medical event foundation model, can effectively capture complex clinical dynamics, providing an extensible and generalizable framework to support clinical decision-making, streamline healthcare operations, and improve patient outcomes.

## 📝 요약

Comet 모델은 310개 건강 시스템에서 3억 명 이상의 환자 기록을 포함한 Epic Cosmos 데이터셋을 활용하여 1150억 개의 의료 이벤트를 학습한 디코더 전용 트랜스포머 모델입니다. 이 연구는 의료 이벤트 데이터의 스케일링 법칙을 연구하여, 컴퓨팅, 토큰, 모델 크기에 대한 멱법칙 관계를 밝혀냈습니다. Comet 모델은 환자의 실제 의료 기록을 기반으로 다음 의료 이벤트를 예측하여 환자의 건강 타임라인을 시뮬레이션합니다. 78개의 실제 과제를 통해 Comet은 진단 예측, 질병 예후, 의료 운영 등에서 특정 과제에 맞춘 모델을 능가하거나 동등한 성능을 보였습니다. Comet은 복잡한 임상 역학을 효과적으로 포착하여 임상 의사결정 지원, 의료 운영 간소화 및 환자 결과 개선에 기여할 수 있는 확장 가능하고 일반화 가능한 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. Comet 모델은 118백만 명의 환자와 1150억 개의 개별 의료 이벤트를 기반으로 사전 훈련된 디코더 전용 트랜스포머 모델로, 환자의 실시간 의료 이력을 바탕으로 다음 의료 이벤트를 예측합니다.
- 2. 이 연구는 의료 이벤트 데이터에 대한 가장 큰 스케일링 법칙 연구를 통해 사전 훈련 방법론을 확립하고, 계산, 토큰 및 모델 크기에 대한 멱법칙 스케일링 관계를 밝혀냈습니다.
- 3. Comet 모델은 진단 예측, 질병 예후, 의료 운영 등 78개의 실제 과제에서 일반적인 사전 훈련과 시뮬레이션 기반 추론을 통해 과제별로 훈련된 모델을 능가하거나 대등한 성능을 보였습니다.
- 4. Comet의 예측력은 모델과 사전 훈련의 규모가 커질수록 지속적으로 향상되며, 복잡한 임상 역학을 효과적으로 포착하여 임상 의사 결정 지원, 의료 운영 간소화 및 환자 결과 개선에 기여할 수 있는 확장 가능하고 일반화 가능한 프레임워크를 제공합니다.


---

*Generated on 2025-09-24 14:38:05*