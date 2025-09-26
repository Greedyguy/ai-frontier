---
keywords:
  - Volume Electron Microscopy
  - Residual U-Net
  - Synapse Detection
  - SimpSyn
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17041
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:42:07.571019",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Volume Electron Microscopy",
    "Residual U-Net",
    "Synapse Detection",
    "SimpSyn"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Volume Electron Microscopy": 0.78,
    "Residual U-Net": 0.79,
    "Synapse Detection": 0.82,
    "SimpSyn": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Volume Electron Microscopy",
        "canonical": "Volume Electron Microscopy",
        "aliases": [
          "Volume EM"
        ],
        "category": "unique_technical",
        "rationale": "This technique is crucial for synapse detection and is a specialized method in connectomics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Residual U-Net",
        "canonical": "Residual U-Net",
        "aliases": [
          "ResUNet"
        ],
        "category": "specific_connectable",
        "rationale": "A specific neural network architecture that enhances synapse detection, linking to broader neural network discussions.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Synapse Detection",
        "canonical": "Synapse Detection",
        "aliases": [
          "Synaptic Detection"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus and connects to broader discussions on neural circuit analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "SimpSyn",
        "canonical": "SimpSyn",
        "aliases": [
          "Simple Synapse Detection"
        ],
        "category": "unique_technical",
        "rationale": "A novel model proposed in the paper, highlighting its contribution to synapse detection.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "neural circuits",
      "benchmark",
      "datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Volume Electron Microscopy",
      "resolved_canonical": "Volume Electron Microscopy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Residual U-Net",
      "resolved_canonical": "Residual U-Net",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Synapse Detection",
      "resolved_canonical": "Synapse Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "SimpSyn",
      "resolved_canonical": "SimpSyn",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Towards Generalized Synapse Detection Across Invertebrate Species

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17041.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17041](https://arxiv.org/abs/2509.17041)

## 🔗 유사한 논문
- [[2025-09-23/Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks_20250923|Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks]] (80.1% similar)
- [[2025-09-23/SPICED_ A Synaptic Homeostasis-Inspired Framework for Unsupervised Continual EEG Decoding_20250923|SPICED: A Synaptic Homeostasis-Inspired Framework for Unsupervised Continual EEG Decoding]] (79.3% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (79.3% similar)
- [[2025-09-23/DPASyn_ Mechanism-Aware Drug Synergy Prediction via Dual Attention and Precision-Aware Quantization_20250923|DPASyn: Mechanism-Aware Drug Synergy Prediction via Dual Attention and Precision-Aware Quantization]] (78.8% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Residual U-Net|Residual U-Net]], [[keywords/Synapse Detection|Synapse Detection]]
**⚡ Unique Technical**: [[keywords/Volume Electron Microscopy|Volume Electron Microscopy]], [[keywords/SimpSyn|SimpSyn]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17041v1 Announce Type: new 
Abstract: Behavioural differences across organisms, whether healthy or pathological, are closely tied to the structure of their neural circuits. Yet, the fine-scale synaptic changes that give rise to these variations remain poorly understood, in part due to persistent challenges in detecting synapses reliably and at scale. Volume electron microscopy (EM) offers the resolution required to capture synaptic architecture, but automated detection remains difficult due to sparse annotations, morphological variability, and cross-dataset domain shifts. To address this, we make three key contributions. First, we curate a diverse EM benchmark spanning four datasets across two invertebrate species: adult and larval Drosophila melanogaster, and Megaphragma viggianii (micro-WASP). Second, we propose SimpSyn, a single-stage Residual U-Net trained to predict dual-channel spherical masks around pre- and post-synaptic sites, designed to prioritize training and inference speeds and annotation efficiency over architectural complexity. Third, we benchmark SimpSyn against Buhmann et al.'s Synful [1], a state-of-the-art multi-task model that jointly infers synaptic pairs. Despite its simplicity, SimpSyn consistently outperforms Synful in F1-score across all volumes for synaptic site detection. While generalization across datasets remains limited, SimpSyn achieves competitive performance when trained on the combined cohort. Finally, ablations reveal that simple post-processing strategies - such as local peak detection and distance-based filtering - yield strong performance without complex test-time heuristics. Taken together, our results suggest that lightweight models, when aligned with task structure, offer a practical and scalable solution for synapse detection in large-scale connectomic pipelines.

## 📝 요약

이 논문은 신경 회로의 구조가 유기체의 행동 차이에 미치는 영향을 연구하며, 시냅스 검출의 어려움을 해결하기 위한 새로운 방법론을 제시합니다. 주요 기여로는 첫째, 두 종류의 무척추동물에서 수집한 네 가지 데이터셋을 포함한 다양한 전자현미경(EM) 벤치마크를 구축했습니다. 둘째, SimpSyn이라는 단일 단계 Residual U-Net 모델을 제안하여 시냅스 부위 검출을 효율적으로 수행합니다. 셋째, SimpSyn은 기존의 Synful 모델보다 모든 데이터셋에서 F1-score가 우수하며, 간단한 후처리 전략을 통해 복잡한 테스트 시간 기법 없이도 높은 성능을 보입니다. 이 연구는 경량 모델이 대규모 연결체학 파이프라인에서 실용적이고 확장 가능한 시냅스 검출 솔루션을 제공할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 신경 회로의 구조는 유기체의 행동 차이와 밀접하게 연결되어 있으며, 이를 이해하기 위해 신경 시냅스의 미세한 변화를 탐구하는 것이 중요합니다.
- 2. 자동화된 시냅스 검출은 여전히 어려운 과제이며, 이를 해결하기 위해 다양한 전자 현미경(EM) 데이터셋을 활용한 벤치마크를 구축했습니다.
- 3. SimpSyn은 단일 단계의 Residual U-Net 모델로, 시냅스 사이트 주변의 구형 마스크를 예측하여 빠른 학습 및 추론 속도를 제공합니다.
- 4. SimpSyn은 기존의 Synful 모델보다 모든 볼륨에서 시냅스 사이트 검출 F1-score가 우수하며, 간단한 후처리 전략을 통해 성능을 향상시킬 수 있습니다.
- 5. 경량 모델이 대규모 연결체 파이프라인에서 실용적이고 확장 가능한 시냅스 검출 솔루션을 제공할 수 있음을 시사합니다.


---

*Generated on 2025-09-24 04:42:07*