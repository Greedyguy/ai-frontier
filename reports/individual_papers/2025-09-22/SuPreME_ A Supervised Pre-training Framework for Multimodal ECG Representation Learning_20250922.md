---
keywords:
  - Multimodal Learning
  - Zero-Shot Learning
  - Supervised Learning
  - Large Language Model
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2502.19668
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:51:45.978191",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Zero-Shot Learning",
    "Supervised Learning",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Zero-Shot Learning": 0.85,
    "Supervised Learning": 0.78,
    "Large Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal ECG Representation Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal ECG"
        ],
        "category": "specific_connectable",
        "rationale": "Connects the concept of using multiple data types in ECG analysis, aligning with existing multimodal frameworks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-Shot Classification",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot ECG"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the ability to classify new conditions without additional training, a key feature of the proposed method.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Supervised Pre-training",
        "canonical": "Supervised Learning",
        "aliases": [
          "Supervised Pre-training Framework"
        ],
        "category": "broad_technical",
        "rationale": "Links to the foundational concept of using labeled data to enhance model performance.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Essential for understanding the method's use of language models in extracting structured diagnostic labels.",
        "novelty_score": 0.5,
        "connectivity_score": 0.92,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "ECG",
      "Cardiac Health"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal ECG Representation Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-Shot Classification",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Supervised Pre-training",
      "resolved_canonical": "Supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.92,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# SuPreME: A Supervised Pre-training Framework for Multimodal ECG Representation Learning

**Korean Title:** SuPreME: 다중 모달 ECG 표현 학습을 위한 지도 사전 학습 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.19668.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2502.19668](https://arxiv.org/abs/2502.19668)

## 🔗 유사한 논문
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (82.4% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (81.2% similar)
- [[2025-09-22/Channel-Imposed Fusion_ A Simple yet Effective Method for Medical Time Series Classification_20250922|Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification]] (80.3% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget: Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (80.1% similar)
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Supervised Learning|Supervised Learning]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.19668v4 Announce Type: replace-cross 
Abstract: Cardiovascular diseases are a leading cause of death and disability worldwide. Electrocardiogram (ECG) is critical for diagnosing and monitoring cardiac health, but obtaining large-scale annotated ECG datasets is labor-intensive and time-consuming. Recent ECG Self-Supervised Learning (eSSL) methods mitigate this by learning features without extensive labels but fail to capture fine-grained clinical semantics and require extensive task-specific fine-tuning. To address these challenges, we propose $\textbf{SuPreME}$, a $\textbf{Su}$pervised $\textbf{Pre}$-training framework for $\textbf{M}$ultimodal $\textbf{E}$CG representation learning. SuPreME is pre-trained using structured diagnostic labels derived from ECG report entities through a one-time offline extraction with Large Language Models (LLMs), which help denoise, standardize cardiac concepts, and improve clinical representation learning. By fusing ECG signals with textual cardiac queries instead of fixed labels, SuPreME enables zero-shot classification of unseen conditions without further fine-tuning. We evaluate SuPreME on six downstream datasets covering 106 cardiac conditions, achieving superior zero-shot AUC performance of $77.20\%$, surpassing state-of-the-art eSSLs by $4.98\%$. Results demonstrate SuPreME's effectiveness in leveraging structured, clinically relevant knowledge for high-quality ECG representations.

## 🔍 Abstract (한글 번역)

arXiv:2502.19668v4 발표 유형: 교차 대체  
초록: 심혈관 질환은 전 세계적으로 주요 사망 및 장애 원인입니다. 심전도(ECG)는 심장 건강을 진단하고 모니터링하는 데 필수적이지만, 대규모 주석이 달린 심전도 데이터 세트를 얻는 것은 노동 집약적이고 시간이 많이 소요됩니다. 최근의 심전도 자기 지도 학습(eSSL) 방법은 광범위한 레이블 없이 특징을 학습하여 이를 완화하지만, 세밀한 임상 의미를 포착하지 못하고 광범위한 작업별 미세 조정이 필요합니다. 이러한 문제를 해결하기 위해, 우리는 다중 모달 심전도 표현 학습을 위한 감독된 사전 훈련 프레임워크인 $\textbf{SuPreME}$를 제안합니다. SuPreME는 대형 언어 모델(LLM)을 통해 심전도 보고서 엔티티에서 파생된 구조화된 진단 레이블을 사용하여 사전 훈련되며, 이는 심장 개념을 정규화하고 표준화하여 임상 표현 학습을 개선합니다. 고정된 레이블 대신 심전도 신호와 텍스트 심장 질의를 융합함으로써, SuPreME는 추가 미세 조정 없이 보지 못한 상태에 대한 제로샷 분류를 가능하게 합니다. 우리는 106개의 심장 상태를 다루는 6개의 다운스트림 데이터 세트에서 SuPreME를 평가하여, 최첨단 eSSL을 $4.98\%$ 초과하는 $77.20\%$의 우수한 제로샷 AUC 성능을 달성했습니다. 결과는 고품질 심전도 표현을 위한 구조화된 임상 관련 지식을 활용하는 SuPreME의 효과를 입증합니다.

## 📝 요약

이 논문은 심혈관 질환 진단에 중요한 ECG 데이터의 대규모 주석 작업의 어려움을 해결하기 위해 SuPreME라는 새로운 프레임워크를 제안합니다. SuPreME는 대형 언어 모델을 활용하여 ECG 보고서에서 진단 레이블을 추출하고 이를 통해 ECG 신호와 텍스트 질의를 융합하여 학습합니다. 이를 통해 새로운 심장 질환을 추가 학습 없이 분류할 수 있는 제로샷 분류가 가능해집니다. SuPreME는 106개의 심장 질환을 포함한 6개의 데이터셋에서 테스트되었으며, 기존의 방법보다 4.98% 높은 77.20%의 AUC 성능을 보여주었습니다. 이 연구는 구조화된 임상 지식을 활용하여 ECG 표현 학습의 질을 향상시켰음을 입증합니다.

## 🎯 주요 포인트

- 1. 심혈관 질환 진단 및 모니터링에 중요한 ECG 데이터셋의 대규모 주석 작업은 시간과 노력이 많이 소요됩니다.
- 2. SuPreME는 ECG 보고서에서 추출한 구조화된 진단 레이블을 사용하여 사전 학습된 다중 모드 ECG 표현 학습 프레임워크입니다.
- 3. SuPreME는 고정된 레이블 대신 ECG 신호와 텍스트 심장 질의의 융합을 통해 추가 미세 조정 없이도 새로운 상태에 대한 제로샷 분류를 가능하게 합니다.
- 4. SuPreME는 106개의 심장 상태를 다루는 6개의 다운스트림 데이터셋에서 테스트되어, 최첨단 eSSL을 4.98% 초과하는 77.20%의 제로샷 AUC 성능을 달성했습니다.
- 5. 연구 결과는 SuPreME가 구조화된 임상 지식을 활용하여 고품질 ECG 표현을 학습하는 데 효과적임을 보여줍니다.


---

*Generated on 2025-09-23 09:51:45*