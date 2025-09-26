---
keywords:
  - Implicit Neural Representations
  - Wavelet-Informed Implicit Neural Representation
  - Neural Network
  - Multi-Scale Enhancement
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15494
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:26:59.138394",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Implicit Neural Representations",
    "Wavelet-Informed Implicit Neural Representation",
    "Neural Network",
    "Multi-Scale Enhancement"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Implicit Neural Representations": 0.78,
    "Wavelet-Informed Implicit Neural Representation": 0.8,
    "Neural Network": 0.7,
    "Multi-Scale Enhancement": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Implicit Neural Representations",
        "canonical": "Implicit Neural Representations",
        "aliases": [
          "INR"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a specific approach to neural representation that is distinct from traditional methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Wavelet-Informed Implicit Neural Representation",
        "canonical": "Wavelet-Informed Implicit Neural Representation",
        "aliases": [
          "WIEN-INR"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method proposed in the paper, offering a new approach to multi-scale neural representation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Neural networks are the foundational technology for the discussed representations, providing a broad technical link.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multi-Scale Enhancement",
        "canonical": "Multi-Scale Enhancement",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for improving the representation of complex data structures, enhancing connectivity with related methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "resolution-independent representation",
      "training efficiency",
      "storage cost"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Implicit Neural Representations",
      "resolved_canonical": "Implicit Neural Representations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Wavelet-Informed Implicit Neural Representation",
      "resolved_canonical": "Wavelet-Informed Implicit Neural Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multi-Scale Enhancement",
      "resolved_canonical": "Multi-Scale Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Detail Across Scales: Multi-Scale Enhancement for Full Spectrum Neural Representations

**Korean Title:** 스케일 전반의 세부사항: 전체 스펙트럼 신경 표현을 위한 다중 스케일 향상

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15494.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15494](https://arxiv.org/abs/2509.15494)

## 🔗 유사한 논문
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (79.9% similar)
- [[2025-09-22/A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction_20250922|A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction]] (79.2% similar)
- [[2025-09-17/Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems_20250917|Data Denoising and Derivative Estimation for Data-Driven Modeling of Nonlinear Dynamical Systems]] (78.9% similar)
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (78.7% similar)
- [[2025-09-18/Task-Aware Image Signal Processor for Advanced Visual Perception_20250918|Task-Aware Image Signal Processor for Advanced Visual Perception]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Multi-Scale Enhancement|Multi-Scale Enhancement]]
**⚡ Unique Technical**: [[keywords/Implicit Neural Representations|Implicit Neural Representations]], [[keywords/Wavelet-Informed Implicit Neural Representation|Wavelet-Informed Implicit Neural Representation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15494v1 Announce Type: new 
Abstract: Implicit neural representations (INRs) have emerged as a compact and parametric alternative to discrete array-based data representations, encoding information directly in neural network weights to enable resolution-independent representation and memory efficiency. However, existing INR approaches, when constrained to compact network sizes, struggle to faithfully represent the multi-scale structures, high-frequency information, and fine textures that characterize the majority of scientific datasets. To address this limitation, we propose WIEN-INR, a wavelet-informed implicit neural representation that distributes modeling across different resolution scales and employs a specialized kernel network at the finest scale to recover subtle details. This multi-scale architecture allows for the use of smaller networks to retain the full spectrum of information while preserving the training efficiency and reducing storage cost. Through extensive experiments on diverse scientific datasets spanning different scales and structural complexities, WIEN-INR achieves superior reconstruction fidelity while maintaining a compact model size. These results demonstrate WIEN-INR as a practical neural representation framework for high-fidelity scientific data encoding, extending the applicability of INRs to domains where efficient preservation of fine detail is essential.

## 🔍 Abstract (한글 번역)

arXiv:2509.15494v1 발표 유형: 신규  
초록: 암시적 신경 표현(INRs)은 불연속 배열 기반 데이터 표현에 대한 압축적이고 매개변수화된 대안으로 부상하여, 정보가 신경망 가중치에 직접 인코딩되어 해상도 독립적인 표현과 메모리 효율성을 가능하게 합니다. 그러나 기존의 INR 접근 방식은 네트워크 크기가 작을 때 다중 스케일 구조, 고주파 정보 및 대부분의 과학 데이터셋을 특징짓는 세밀한 질감을 충실히 표현하는 데 어려움을 겪습니다. 이러한 제한점을 해결하기 위해, 우리는 다양한 해상도 스케일에 걸쳐 모델링을 분배하고 가장 세밀한 스케일에서 미세한 세부 사항을 복원하기 위해 특수화된 커널 네트워크를 사용하는 파동 기반 암시적 신경 표현인 WIEN-INR을 제안합니다. 이 다중 스케일 아키텍처는 더 작은 네트워크를 사용하여 전체 정보 스펙트럼을 유지하면서도 훈련 효율성을 보존하고 저장 비용을 줄일 수 있게 합니다. 다양한 스케일과 구조적 복잡성을 아우르는 다양한 과학 데이터셋에 대한 광범위한 실험을 통해 WIEN-INR은 컴팩트한 모델 크기를 유지하면서도 우수한 재구성 충실도를 달성합니다. 이러한 결과는 WIEN-INR이 세부 사항의 효율적인 보존이 필수적인 분야에서 INRs의 적용 가능성을 확장하는 고충실도 과학 데이터 인코딩을 위한 실용적인 신경 표현 프레임워크임을 입증합니다.

## 📝 요약

WIEN-INR은 기존의 암묵적 신경 표현(INR)이 작은 네트워크 크기에서 다중 스케일 구조와 고주파 정보를 충실히 표현하지 못하는 문제를 해결하기 위해 제안된 방법입니다. 이 방법은 웨이블릿 정보를 활용하여 다양한 해상도 스케일에서 모델링을 분산시키고, 가장 세밀한 스케일에서는 특수한 커널 네트워크를 사용하여 미세한 디테일을 복원합니다. 이를 통해 작은 네트워크로도 전체 정보를 유지하면서 훈련 효율성과 저장 비용을 줄일 수 있습니다. 다양한 과학 데이터셋에 대한 실험 결과, WIEN-INR은 높은 재구성 정확도를 유지하면서도 모델 크기를 작게 유지하는 데 성공했습니다. 이는 세부 정보의 효율적 보존이 중요한 분야에서 INR의 적용 가능성을 확장하는 실용적인 신경 표현 프레임워크임을 입증합니다.

## 🎯 주요 포인트

- 1. 암묵적 신경 표현(INRs)은 해상도 독립적인 표현과 메모리 효율성을 제공하는 데이터 표현 방식이다.
- 2. 기존 INR 방법은 네트워크 크기가 작을 때 다중 스케일 구조와 고주파 정보를 충실히 표현하는 데 한계가 있다.
- 3. WIEN-INR은 다양한 해상도 스케일에 걸쳐 모델링을 분배하고, 가장 세밀한 스케일에서 특수 커널 네트워크를 사용하여 미세한 세부 사항을 복원한다.
- 4. WIEN-INR은 작은 네트워크로도 전체 정보 스펙트럼을 유지하면서 훈련 효율성과 저장 비용을 줄일 수 있다.
- 5. 다양한 과학 데이터셋 실험에서 WIEN-INR은 높은 재구성 충실도를 달성하며, 세부 정보 보존이 중요한 분야에서 실용적인 신경 표현 프레임워크로 입증되었다.


---

*Generated on 2025-09-23 10:26:59*