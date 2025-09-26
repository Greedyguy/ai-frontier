<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:59:52.728160",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "RGB-D Salient Object Detection",
    "State Space Model",
    "Transformer",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "RGB-D Salient Object Detection": 0.78,
    "State Space Model": 0.8,
    "Transformer": 0.85,
    "Multimodal Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RGB-D Salient Object Detection",
        "canonical": "RGB-D Salient Object Detection",
        "aliases": [
          "RGB-D SOD"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task in computer vision that involves depth cues, providing a unique link to related research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "State Space Model",
        "canonical": "State Space Model",
        "aliases": [
          "SSM"
        ],
        "category": "specific_connectable",
        "rationale": "State space models are crucial for understanding long-range dependencies in various domains, linking to broader machine learning concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in deep learning, connecting to a wide range of applications and research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cross-Modality Fusion",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Cross-Modality Integration"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to integrating information from different modalities, enhancing links to multimodal research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
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
      "candidate_surface": "RGB-D Salient Object Detection",
      "resolved_canonical": "RGB-D Salient Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "State Space Model",
      "resolved_canonical": "State Space Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cross-Modality Fusion",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# LEAF-Mamba: Local Emphatic and Adaptive Fusion State Space Model for RGB-D Salient Object Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18683.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18683](https://arxiv.org/abs/2509.18683)

## 🔗 유사한 논문
- [[2025-09-23/A Dual-Modulation Framework for RGB-T Crowd Counting via Spatially Modulated Attention and Adaptive Fusion_20250923|A Dual-Modulation Framework for RGB-T Crowd Counting via Spatially Modulated Attention and Adaptive Fusion]] (83.5% similar)
- [[2025-09-22/Towards Size-invariant Salient Object Detection_ A Generic Evaluation and Optimization Approach_20250922|Towards Size-invariant Salient Object Detection: A Generic Evaluation and Optimization Approach]] (83.0% similar)
- [[2025-09-22/DC-Mamba_ Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection_20250922|DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection]] (82.7% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (82.7% similar)
- [[2025-09-22/FoBa_ A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection_20250922|FoBa: A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/State Space Model|State Space Model]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/RGB-D Salient Object Detection|RGB-D Salient Object Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18683v1 Announce Type: cross 
Abstract: RGB-D salient object detection (SOD) aims to identify the most conspicuous objects in a scene with the incorporation of depth cues. Existing methods mainly rely on CNNs, limited by the local receptive fields, or Vision Transformers that suffer from the cost of quadratic complexity, posing a challenge in balancing performance and computational efficiency. Recently, state space models (SSM), Mamba, have shown great potential for modeling long-range dependency with linear complexity. However, directly applying SSM to RGB-D SOD may lead to deficient local semantics as well as the inadequate cross-modality fusion. To address these issues, we propose a Local Emphatic and Adaptive Fusion state space model (LEAF-Mamba) that contains two novel components: 1) a local emphatic state space module (LE-SSM) to capture multi-scale local dependencies for both modalities. 2) an SSM-based adaptive fusion module (AFM) for complementary cross-modality interaction and reliable cross-modality integration. Extensive experiments demonstrate that the LEAF-Mamba consistently outperforms 16 state-of-the-art RGB-D SOD methods in both efficacy and efficiency. Moreover, our method can achieve excellent performance on the RGB-T SOD task, proving a powerful generalization ability.

## 📝 요약

이 논문은 RGB-D 주목 객체 검출(SOD)에서 깊이 정보를 활용하여 가장 두드러진 객체를 식별하는 새로운 방법론을 제안합니다. 기존의 CNN 기반 방법은 국소 수용 영역에 제한되고, 비전 트랜스포머는 계산 복잡성 문제를 겪습니다. 이를 해결하기 위해 제안된 LEAF-Mamba 모델은 두 가지 주요 구성 요소를 포함합니다. 첫째, 다중 스케일의 국소 의존성을 포착하는 '국소 강조 상태 공간 모듈(LE-SSM)'과 둘째, 상호 보완적인 교차 모달리티 상호작용을 위한 '적응형 융합 모듈(AFM)'입니다. 실험 결과, LEAF-Mamba는 16개의 최신 RGB-D SOD 방법보다 뛰어난 성능과 효율성을 보였으며, RGB-T SOD 작업에서도 우수한 일반화 능력을 입증했습니다.

## 🎯 주요 포인트

- 1. RGB-D 주목 객체 탐지는 깊이 단서를 활용하여 장면에서 가장 눈에 띄는 객체를 식별하는 것을 목표로 한다.
- 2. 기존 방법들은 CNN의 국소 수용 영역 한계와 Vision Transformer의 복잡성 문제로 인해 성능과 계산 효율성의 균형을 맞추기 어렵다.
- 3. LEAF-Mamba는 국소 의미 부족과 교차 모달리티 융합 문제를 해결하기 위해 제안된 모델로, LE-SSM과 AFM 두 가지 주요 구성 요소를 포함한다.
- 4. LEAF-Mamba는 16개의 최신 RGB-D SOD 방법들보다 뛰어난 성능과 효율성을 일관되게 보여준다.
- 5. 제안된 방법은 RGB-T SOD 작업에서도 우수한 성능을 발휘하여 강력한 일반화 능력을 입증한다.


---

*Generated on 2025-09-24 13:59:52*