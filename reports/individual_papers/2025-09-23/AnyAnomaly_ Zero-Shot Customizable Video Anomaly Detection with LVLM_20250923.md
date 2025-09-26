---
keywords:
  - Zero-Shot Learning
  - Vision-Language Model
  - Video Anomaly Detection
  - Context-Aware Visual Question Answering
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2503.04504
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:18:25.258062",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Vision-Language Model",
    "Video Anomaly Detection",
    "Context-Aware Visual Question Answering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.78,
    "Vision-Language Model": 0.82,
    "Video Anomaly Detection": 0.77,
    "Context-Aware Visual Question Answering": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is crucial for understanding the model's ability to generalize without retraining, a key aspect of the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLM"
        ],
        "category": "evolved_concepts",
        "rationale": "The use of a Vision-Language Model is central to the AnyAnomaly approach, linking it to recent advancements in multimodal AI.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Video Anomaly Detection",
        "canonical": "Video Anomaly Detection",
        "aliases": [
          "VAD"
        ],
        "category": "unique_technical",
        "rationale": "Video Anomaly Detection is the primary application of the study, providing a unique context for the proposed model.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Context-Aware Visual Question Answering",
        "canonical": "Context-Aware Visual Question Answering",
        "aliases": [
          "C-VQA"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel aspect of the model's implementation, enhancing its adaptability and customization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "model",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-Shot",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Video Anomaly Detection",
      "resolved_canonical": "Video Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Context-Aware Visual Question Answering",
      "resolved_canonical": "Context-Aware Visual Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# AnyAnomaly: Zero-Shot Customizable Video Anomaly Detection with LVLM

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.04504.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2503.04504](https://arxiv.org/abs/2503.04504)

## 🔗 유사한 논문
- [[2025-09-18/AD-DINOv3_ Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration_20250918|AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (82.9% similar)
- [[2025-09-23/From Benchmarks to Reality_ Advancing Visual Anomaly Detection by the VAND 3.0 Challenge_20250923|From Benchmarks to Reality: Advancing Visual Anomaly Detection by the VAND 3.0 Challenge]] (82.4% similar)
- [[2025-09-23/VCE_ Safe Autoregressive Image Generation via Visual Contrast Exploitation_20250923|VCE: Safe Autoregressive Image Generation via Visual Contrast Exploitation]] (80.8% similar)
- [[2025-09-23/When Big Models Train Small Ones_ Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs_20250923|When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs]] (80.7% similar)
- [[2025-09-23/ADVEDM_Fine-grained Adversarial Attack against VLM-based Embodied Agents_20250923|ADVEDM:Fine-grained Adversarial Attack against VLM-based Embodied Agents]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Video Anomaly Detection|Video Anomaly Detection]], [[keywords/Context-Aware Visual Question Answering|Context-Aware Visual Question Answering]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.04504v3 Announce Type: replace 
Abstract: Video anomaly detection (VAD) is crucial for video analysis and surveillance in computer vision. However, existing VAD models rely on learned normal patterns, which makes them difficult to apply to diverse environments. Consequently, users should retrain models or develop separate AI models for new environments, which requires expertise in machine learning, high-performance hardware, and extensive data collection, limiting the practical usability of VAD. To address these challenges, this study proposes customizable video anomaly detection (C-VAD) technique and the AnyAnomaly model. C-VAD considers user-defined text as an abnormal event and detects frames containing a specified event in a video. We effectively implemented AnyAnomaly using a context-aware visual question answering without fine-tuning the large vision language model. To validate the effectiveness of the proposed model, we constructed C-VAD datasets and demonstrated the superiority of AnyAnomaly. Furthermore, our approach showed competitive results on VAD benchmarks, achieving state-of-the-art performance on UBnormal and UCF-Crime and surpassing other methods in generalization across all datasets. Our code is available online at github.com/SkiddieAhn/Paper-AnyAnomaly.

## 📝 요약

이 연구는 다양한 환경에 적용하기 어려운 기존 영상 이상 탐지(VAD) 모델의 한계를 극복하기 위해 사용자 정의 가능한 영상 이상 탐지(C-VAD) 기술과 AnyAnomaly 모델을 제안합니다. C-VAD는 사용자가 정의한 텍스트를 이상 이벤트로 간주하여 해당 이벤트가 포함된 프레임을 탐지합니다. AnyAnomaly는 대형 비전 언어 모델의 미세 조정 없이 문맥 인식 시각적 질문 응답을 활용하여 구현되었습니다. 제안된 모델의 효과를 검증하기 위해 C-VAD 데이터셋을 구축하고, UBnormal 및 UCF-Crime 벤치마크에서 최첨단 성능을 달성하며 모든 데이터셋에서 일반화 능력에서 경쟁력을 입증했습니다. 코드와 데이터는 온라인에서 제공됩니다.

## 🎯 주요 포인트

- 1. 기존의 비디오 이상 탐지(VAD) 모델은 학습된 정상 패턴에 의존하여 다양한 환경에 적용하기 어렵다.
- 2. 사용자가 정의한 텍스트를 비정상 이벤트로 간주하여 특정 이벤트가 포함된 프레임을 탐지하는 맞춤형 비디오 이상 탐지(C-VAD) 기법을 제안한다.
- 3. AnyAnomaly 모델은 대형 비전 언어 모델을 미세 조정하지 않고 맥락 인식 시각적 질문 응답을 통해 효과적으로 구현되었다.
- 4. 제안된 모델의 효과성을 검증하기 위해 C-VAD 데이터셋을 구축하고 AnyAnomaly의 우수성을 입증하였다.
- 5. AnyAnomaly는 UBnormal 및 UCF-Crime에서 최첨단 성능을 달성하고, 모든 데이터셋에서 일반화 측면에서 다른 방법들을 능가하였다.


---

*Generated on 2025-09-24 05:18:25*