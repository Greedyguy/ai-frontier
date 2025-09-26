---
keywords:
  - Self-supervised Learning
  - Multimodal Learning
  - Joint Embedding Predictive Architecture
  - Pulmonary Nodule Diagnosis
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15470
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:00:09.485527",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Multimodal Learning",
    "Joint Embedding Predictive Architecture",
    "Pulmonary Nodule Diagnosis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Multimodal Learning": 0.82,
    "Joint Embedding Predictive Architecture": 0.78,
    "Pulmonary Nodule Diagnosis": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervision"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing concepts in machine learning that focus on learning from unlabeled data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multimodal",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal models"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the growing field of integrating multiple data types in model training.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Joint embedding predictive architecture",
        "canonical": "Joint Embedding Predictive Architecture",
        "aliases": [
          "JEPA"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach specific to the paper, offering a unique linking opportunity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pulmonary nodule diagnosis",
        "canonical": "Pulmonary Nodule Diagnosis",
        "aliases": [
          "lung nodule diagnosis"
        ],
        "category": "unique_technical",
        "rationale": "Specific medical application that provides context for the model's use case.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "model",
      "approach",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multimodal",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Joint embedding predictive architecture",
      "resolved_canonical": "Joint Embedding Predictive Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pulmonary nodule diagnosis",
      "resolved_canonical": "Pulmonary Nodule Diagnosis",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture

**Korean Title:** 이미지 및 임상 서명을 자기 지도 학습하는 다중 모달 공동 임베딩 예측 아키텍처

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15470.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15470](https://arxiv.org/abs/2509.15470)

## 🔗 유사한 논문
- [[2025-09-19/Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (83.7% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (83.0% similar)
- [[2025-09-22/DAFTED_ Decoupled Asymmetric Fusion of Tabular and Echocardiographic Data for Cardiac Hypertension Diagnosis_20250922|DAFTED: Decoupled Asymmetric Fusion of Tabular and Echocardiographic Data for Cardiac Hypertension Diagnosis]] (83.0% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (82.7% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Joint Embedding Predictive Architecture|Joint Embedding Predictive Architecture]], [[keywords/Pulmonary Nodule Diagnosis|Pulmonary Nodule Diagnosis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15470v1 Announce Type: cross 
Abstract: The development of multimodal models for pulmonary nodule diagnosis is limited by the scarcity of labeled data and the tendency for these models to overfit on the training distribution. In this work, we leverage self-supervised learning from longitudinal and multimodal archives to address these challenges. We curate an unlabeled set of patients with CT scans and linked electronic health records from our home institution to power joint embedding predictive architecture (JEPA) pretraining. After supervised finetuning, we show that our approach outperforms an unregularized multimodal model and imaging-only model in an internal cohort (ours: 0.91, multimodal: 0.88, imaging-only: 0.73 AUC), but underperforms in an external cohort (ours: 0.72, imaging-only: 0.75 AUC). We develop a synthetic environment that characterizes the context in which JEPA may underperform. This work innovates an approach that leverages unlabeled multimodal medical archives to improve predictive models and demonstrates its advantages and limitations in pulmonary nodule diagnosis.

## 🔍 Abstract (한글 번역)

arXiv:2509.15470v1 발표 유형: 교차  
초록: 폐 결절 진단을 위한 다중 모달 모델의 개발은 라벨이 지정된 데이터의 부족과 이러한 모델이 훈련 분포에 과적합되는 경향으로 인해 제한됩니다. 본 연구에서는 이러한 문제를 해결하기 위해 종단적 및 다중 모달 아카이브로부터의 자가 지도 학습을 활용합니다. 우리는 공동 임베딩 예측 아키텍처(JEPA) 사전 훈련을 위해 본 기관의 CT 스캔과 연결된 전자 건강 기록을 가진 라벨이 없는 환자 세트를 큐레이션합니다. 지도 학습 후, 우리의 접근 방식이 내부 코호트에서 비정규화된 다중 모달 모델과 이미징 전용 모델을 능가함을 보여줍니다(우리의 모델: 0.91, 다중 모달: 0.88, 이미징 전용: 0.73 AUC), 그러나 외부 코호트에서는 성능이 떨어집니다(우리의 모델: 0.72, 이미징 전용: 0.75 AUC). 우리는 JEPA가 성능이 떨어질 수 있는 맥락을 특성화하는 합성 환경을 개발합니다. 이 연구는 라벨이 없는 다중 모달 의료 아카이브를 활용하여 예측 모델을 개선하는 접근 방식을 혁신하고, 폐 결절 진단에서의 장점과 한계를 입증합니다.

## 📝 요약

이 연구는 폐 결절 진단을 위한 다중 모달 모델 개발의 어려움을 해결하기 위해 자기 지도 학습을 활용했습니다. 연구진은 CT 스캔과 전자의료기록을 포함한 비라벨링 환자 데이터를 사용하여 공동 임베딩 예측 아키텍처(JEPA)를 사전 학습했습니다. 그 결과, 내부 코호트에서는 기존 다중 모달 모델과 영상 전용 모델보다 우수한 성능을 보였으나, 외부 코호트에서는 다소 저조한 성능을 나타냈습니다. 이 연구는 비라벨링 다중 모달 의료 데이터를 활용하여 예측 모델의 성능을 향상시키는 방법론을 제시하고, 그 장점과 한계를 보여주었습니다.

## 🎯 주요 포인트

- 1. 폐 결절 진단을 위한 다중 모달 모델 개발은 라벨링된 데이터의 부족과 훈련 분포에 대한 과적합 경향으로 제한됩니다.
- 2. 본 연구는 자가 지도 학습을 활용하여 이러한 문제를 해결하고자 하며, CT 스캔과 전자 건강 기록을 활용한 무라벨 환자 데이터를 사용합니다.
- 3. 제안된 방법은 내부 코호트에서 기존의 비정규화 다중 모달 모델과 영상 전용 모델을 능가하지만, 외부 코호트에서는 성능이 떨어집니다.
- 4. JEPA가 성능이 저하될 수 있는 맥락을 특성화하는 합성 환경을 개발하였습니다.
- 5. 본 연구는 무라벨 다중 모달 의료 아카이브를 활용하여 예측 모델을 개선하는 접근법을 혁신적으로 제시하고, 폐 결절 진단에서의 장점과 한계를 보여줍니다.


---

*Generated on 2025-09-23 09:00:09*