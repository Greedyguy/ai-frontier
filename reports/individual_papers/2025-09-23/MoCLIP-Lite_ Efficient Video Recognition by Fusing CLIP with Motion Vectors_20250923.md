---
keywords:
  - Video Action Recognition
  - Vision-Language Model
  - Motion Vectors
  - Zero-Shot Learning
  - Two-Stream Late Fusion
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17084
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:44:59.786758",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Video Action Recognition",
    "Vision-Language Model",
    "Motion Vectors",
    "Zero-Shot Learning",
    "Two-Stream Late Fusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Video Action Recognition": 0.7,
    "Vision-Language Model": 0.9,
    "Motion Vectors": 0.8,
    "Zero-Shot Learning": 0.85,
    "Two-Stream Late Fusion": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Video Action Recognition",
        "canonical": "Video Action Recognition",
        "aliases": [
          "Action Recognition"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and connects to the domain of video analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Contrastive Language-Image Pre-training",
        "canonical": "Vision-Language Model",
        "aliases": [
          "CLIP"
        ],
        "category": "evolved_concepts",
        "rationale": "CLIP is a key component in the proposed method and links to the broader vision-language model trend.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "Motion Vectors",
        "canonical": "Motion Vectors",
        "aliases": [
          "MV"
        ],
        "category": "unique_technical",
        "rationale": "Motion vectors are crucial for the proposed method's efficiency and link to video compression techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Zero-Shot Capabilities",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot capabilities are highlighted as a strength of CLIP, connecting to the broader zero-shot learning paradigm.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Two-Stream Late Fusion",
        "canonical": "Two-Stream Late Fusion",
        "aliases": [
          "Late Fusion"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel aspect of the proposed framework, linking to fusion methods in video analysis.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Video Action Recognition",
      "resolved_canonical": "Video Action Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Contrastive Language-Image Pre-training",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Motion Vectors",
      "resolved_canonical": "Motion Vectors",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Zero-Shot Capabilities",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Two-Stream Late Fusion",
      "resolved_canonical": "Two-Stream Late Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MoCLIP-Lite: Efficient Video Recognition by Fusing CLIP with Motion Vectors

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17084.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17084](https://arxiv.org/abs/2509.17084)

## 🔗 유사한 논문
- [[2025-09-23/CardiacCLIP_ Video-based CLIP Adaptation for LVEF Prediction in a Few-shot Manner_20250923|CardiacCLIP: Video-based CLIP Adaptation for LVEF Prediction in a Few-shot Manner]] (85.5% similar)
- [[2025-09-23/MVCL-DAF++_ Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion_20250923|MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion]] (84.5% similar)
- [[2025-09-18/Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (84.1% similar)
- [[2025-09-22/RegionMed-CLIP_ A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding_20250922|RegionMed-CLIP: A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding]] (82.9% similar)
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Video Action Recognition|Video Action Recognition]], [[keywords/Motion Vectors|Motion Vectors]], [[keywords/Two-Stream Late Fusion|Two-Stream Late Fusion]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17084v1 Announce Type: new 
Abstract: Video action recognition is a fundamental task in computer vision, but state-of-the-art models are often computationally expensive and rely on extensive video pre-training. In parallel, large-scale vision-language models like Contrastive Language-Image Pre-training (CLIP) offer powerful zero-shot capabilities on static images, while motion vectors (MV) provide highly efficient temporal information directly from compressed video streams. To synergize the strengths of these paradigms, we propose MoCLIP-Lite, a simple yet powerful two-stream late fusion framework for efficient video recognition. Our approach combines features from a frozen CLIP image encoder with features from a lightweight, supervised network trained on raw MV. During fusion, both backbones are frozen, and only a tiny Multi-Layer Perceptron (MLP) head is trained, ensuring extreme efficiency. Through comprehensive experiments on the UCF101 dataset, our method achieves a remarkable 89.2% Top-1 accuracy, significantly outperforming strong zero-shot (65.0%) and MV-only (66.5%) baselines. Our work provides a new, highly efficient baseline for video understanding that effectively bridges the gap between large static models and dynamic, low-cost motion cues. Our code and models are available at https://github.com/microa/MoCLIP-Lite.

## 📝 요약

비디오 행동 인식은 컴퓨터 비전에서 중요한 과제이지만, 최신 모델들은 계산 비용이 높고 비디오 사전 학습에 의존합니다. 이에 반해, 대규모 비전-언어 모델인 CLIP은 정적 이미지에서 강력한 제로샷 성능을 보이며, 모션 벡터(MV)는 압축된 비디오 스트림에서 효율적인 시간 정보를 제공합니다. 우리는 이러한 장점을 결합하여 MoCLIP-Lite라는 효율적인 비디오 인식을 위한 간단하면서도 강력한 이중 스트림 후반 융합 프레임워크를 제안합니다. 이 방법은 고정된 CLIP 이미지 인코더의 특징과 경량의 감독된 네트워크로부터 학습된 원시 MV의 특징을 결합합니다. 융합 시 두 백본은 고정되고 작은 MLP 헤드만 학습되어 매우 효율적입니다. UCF101 데이터셋에서 89.2%의 Top-1 정확도를 달성하며, 제로샷(65.0%) 및 MV만 사용한(66.5%) 기준을 크게 능가합니다. 이 연구는 정적 모델과 동적 모션 단서를 효과적으로 연결하는 새로운 효율적 기준을 제공합니다.

## 🎯 주요 포인트

- 1. MoCLIP-Lite는 CLIP 이미지 인코더와 경량의 감독된 네트워크를 결합하여 효율적인 비디오 인식을 위한 두 스트림 늦은 융합 프레임워크를 제안합니다.
- 2. 이 방법은 고정된 백본을 사용하고 작은 MLP 헤드만을 훈련하여 극도의 효율성을 보장합니다.
- 3. UCF101 데이터셋에서 MoCLIP-Lite는 89.2%의 Top-1 정확도를 달성하여 강력한 제로샷 및 MV 전용 기준선을 크게 능가합니다.
- 4. 이 연구는 대형 정적 모델과 저비용 동적 모션 큐 사이의 격차를 효과적으로 메우는 새로운 효율적인 비디오 이해 기준선을 제공합니다.


---

*Generated on 2025-09-24 04:44:59*