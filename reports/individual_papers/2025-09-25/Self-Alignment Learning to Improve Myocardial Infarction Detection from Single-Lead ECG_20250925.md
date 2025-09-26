---
keywords:
  - SelfMIS
  - Latent Space Alignment
  - Single-Lead ECG
  - Myocardial Infarction Detection
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19397
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:34:00.761443",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SelfMIS",
    "Latent Space Alignment",
    "Single-Lead ECG",
    "Myocardial Infarction Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "SelfMIS": 0.8,
    "Latent Space Alignment": 0.82,
    "Single-Lead ECG": 0.75,
    "Myocardial Infarction Detection": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SelfMIS",
        "canonical": "SelfMIS",
        "aliases": [
          "Self-Alignment Learning",
          "Self-Alignment Strategy"
        ],
        "category": "unique_technical",
        "rationale": "SelfMIS is a novel framework proposed in the paper, making it a unique technical term with high novelty.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "latent space alignment",
        "canonical": "Latent Space Alignment",
        "aliases": [
          "latent alignment",
          "latent space matching"
        ],
        "category": "specific_connectable",
        "rationale": "Latent space alignment is central to the paper's methodology, offering a specific concept for linking related works.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "single-lead ECG",
        "canonical": "Single-Lead ECG",
        "aliases": [
          "single-lead electrocardiogram"
        ],
        "category": "unique_technical",
        "rationale": "Single-lead ECG is a specific focus of the study, crucial for understanding the paper's context and applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "myocardial infarction detection",
        "canonical": "Myocardial Infarction Detection",
        "aliases": [
          "heart attack detection"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key application area of the study, linking to broader research on cardiac health.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
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
      "candidate_surface": "SelfMIS",
      "resolved_canonical": "SelfMIS",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "latent space alignment",
      "resolved_canonical": "Latent Space Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "single-lead ECG",
      "resolved_canonical": "Single-Lead ECG",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "myocardial infarction detection",
      "resolved_canonical": "Myocardial Infarction Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Self-Alignment Learning to Improve Myocardial Infarction Detection from Single-Lead ECG

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19397.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19397](https://arxiv.org/abs/2509.19397)

## 🔗 유사한 논문
- [[2025-09-22/SuPreME_ A Supervised Pre-training Framework for Multimodal ECG Representation Learning_20250922|SuPreME: A Supervised Pre-training Framework for Multimodal ECG Representation Learning]] (85.1% similar)
- [[2025-09-25/Advancing Few-Shot Pediatric Arrhythmia Classification with a Novel Contrastive Loss and Multimodal Learning_20250925|Advancing Few-Shot Pediatric Arrhythmia Classification with a Novel Contrastive Loss and Multimodal Learning]] (83.7% similar)
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (82.8% similar)
- [[2025-09-23/CardiacCLIP_ Video-based CLIP Adaptation for LVEF Prediction in a Few-shot Manner_20250923|CardiacCLIP: Video-based CLIP Adaptation for LVEF Prediction in a Few-shot Manner]] (82.0% similar)
- [[2025-09-25/Human Activity Recognition Based on Electrocardiogram Data Only_20250925|Human Activity Recognition Based on Electrocardiogram Data Only]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Latent Space Alignment|Latent Space Alignment]], [[keywords/Myocardial Infarction Detection|Myocardial Infarction Detection]]
**⚡ Unique Technical**: [[keywords/SelfMIS|SelfMIS]], [[keywords/Single-Lead ECG|Single-Lead ECG]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19397v1 Announce Type: cross 
Abstract: Myocardial infarction is a critical manifestation of coronary artery disease, yet detecting it from single-lead electrocardiogram (ECG) remains challenging due to limited spatial information. An intuitive idea is to convert single-lead into multiple-lead ECG for classification by pre-trained models, but generative methods optimized at the signal level in most cases leave a large latent space gap, ultimately degrading diagnostic performance. This naturally raises the question of whether latent space alignment could help. However, most prior ECG alignment methods focus on learning transformation invariance, which mismatches the goal of single-lead detection. To address this issue, we propose SelfMIS, a simple yet effective alignment learning framework to improve myocardial infarction detection from single-lead ECG. Discarding manual data augmentations, SelfMIS employs a self-cutting strategy to pair multiple-lead ECG with their corresponding single-lead segments and directly align them in the latent space. This design shifts the learning objective from pursuing transformation invariance to enriching the single-lead representation, explicitly driving the single-lead ECG encoder to learn a representation capable of inferring global cardiac context from the local signal. Experimentally, SelfMIS achieves superior performance over baseline models across nine myocardial infarction types while maintaining a simpler architecture and lower computational overhead, thereby substantiating the efficacy of direct latent space alignment. Our code and checkpoint will be publicly available after acceptance.

## 📝 요약

이 논문은 단일 유도 심전도(ECG)로부터 심근경색을 효과적으로 탐지하기 위한 새로운 방법론인 SelfMIS를 제안합니다. 기존의 다수 유도 ECG로 변환하는 방법은 잠재 공간의 불일치로 인해 진단 성능이 저하되는 문제가 있었습니다. SelfMIS는 다수 유도 ECG와 단일 유도 세그먼트를 직접 잠재 공간에서 정렬하여, 단일 유도 ECG가 전체 심장 맥락을 추론할 수 있는 표현을 학습하도록 합니다. 실험 결과, SelfMIS는 9가지 심근경색 유형에서 기존 모델보다 우수한 성능을 보였으며, 간단한 구조와 낮은 계산 비용을 유지했습니다.

## 🎯 주요 포인트

- 1. 단일 리드 ECG에서 심근경색을 감지하는 것은 제한된 공간 정보로 인해 여전히 어려운 과제입니다.
- 2. 기존의 신호 수준에서 최적화된 생성 방법은 큰 잠재 공간 격차를 남겨 진단 성능을 저하시킵니다.
- 3. SelfMIS는 다중 리드 ECG와 해당 단일 리드 세그먼트를 잠재 공간에서 직접 정렬하여 심근경색 감지를 개선하는 간단하면서도 효과적인 정렬 학습 프레임워크입니다.
- 4. SelfMIS는 변환 불변성을 추구하는 대신 단일 리드 표현을 풍부하게 하여 지역 신호에서 전반적인 심장 맥락을 추론할 수 있는 표현을 학습하도록 유도합니다.
- 5. SelfMIS는 심근경색의 9가지 유형에서 기존 모델보다 우수한 성능을 보여주며, 더 간단한 아키텍처와 낮은 계산 오버헤드를 유지합니다.


---

*Generated on 2025-09-25 15:34:00*