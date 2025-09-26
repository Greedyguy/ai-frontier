---
keywords:
  - Deep Learning
  - Spectral Compressive Imaging
  - Self-supervised Learning
  - Test-time Adaptation
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16509
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:25:37.734183",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Spectral Compressive Imaging",
    "Self-supervised Learning",
    "Test-time Adaptation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.8,
    "Spectral Compressive Imaging": 0.78,
    "Self-supervised Learning": 0.85,
    "Test-time Adaptation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Unfolding Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "Deep Unfolding"
        ],
        "category": "broad_technical",
        "rationale": "Deep Unfolding Learning is a specialized approach within Deep Learning, enhancing connectivity with existing deep learning frameworks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Spectral Compressive Imaging",
        "canonical": "Spectral Compressive Imaging",
        "aliases": [
          "SCI"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that benefits from linking due to its unique technical challenges and solutions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-supervision"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised Learning is a key method used in the paper, connecting it to broader trends in machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Test-time Adaptation",
        "canonical": "Test-time Adaptation",
        "aliases": [
          "On-the-fly Adaptation"
        ],
        "category": "unique_technical",
        "rationale": "Test-time Adaptation is a novel approach that enhances model adaptability and is central to the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
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
      "candidate_surface": "Deep Unfolding Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Spectral Compressive Imaging",
      "resolved_canonical": "Spectral Compressive Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Test-time Adaptation",
      "resolved_canonical": "Test-time Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SlowFast-SCI: Slow-Fast Deep Unfolding Learning for Spectral Compressive Imaging

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16509.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16509](https://arxiv.org/abs/2509.16509)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (81.2% similar)
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (80.8% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (80.6% similar)
- [[2025-09-22/USCTNet_ A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction_20250922|USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction]] (79.9% similar)
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Spectral Compressive Imaging|Spectral Compressive Imaging]], [[keywords/Test-time Adaptation|Test-time Adaptation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16509v1 Announce Type: new 
Abstract: Humans learn in two complementary ways: a slow, cumulative process that builds broad, general knowledge, and a fast, on-the-fly process that captures specific experiences. Existing deep-unfolding methods for spectral compressive imaging (SCI) mirror only the slow component-relying on heavy pre-training with many unfolding stages-yet they lack the rapid adaptation needed to handle new optical configurations. As a result, they falter on out-of-distribution cameras, especially in bespoke spectral setups unseen during training. This depth also incurs heavy computation and slow inference. To bridge this gap, we introduce SlowFast-SCI, a dual-speed framework seamlessly integrated into any deep unfolding network beyond SCI systems. During slow learning, we pre-train or reuse a priors-based backbone and distill it via imaging guidance into a compact fast-unfolding model. In the fast learning stage, lightweight adaptation modules are embedded within each block and trained self-supervised at test time via a dual-domain loss-without retraining the backbone. To the best of our knowledge, SlowFast-SCI is the first test-time adaptation-driven deep unfolding framework for efficient, self-adaptive spectral reconstruction. Its dual-stage design unites offline robustness with on-the-fly per-sample calibration-yielding over 70% reduction in parameters and FLOPs, up to 5.79 dB PSNR improvement on out-of-distribution data, preserved cross-domain adaptability, and a 4x faster adaptation speed. In addition, its modularity integrates with any deep-unfolding network, paving the way for self-adaptive, field-deployable imaging and expanded computational imaging modalities. Code and models are available at https://github.com/XuanLu11/SlowFast-SCI.

## 📝 요약

이 논문은 새로운 심층 전개 네트워크 프레임워크인 SlowFast-SCI를 제안합니다. 이는 기존의 스펙트럼 압축 이미징(SCI) 방법이 느린 학습에만 의존하여 새로운 광학 구성을 처리하는 데 어려움을 겪는 문제를 해결합니다. SlowFast-SCI는 느린 학습 단계에서 사전 학습된 백본을 활용하고, 빠른 학습 단계에서 경량화된 적응 모듈을 통해 테스트 시 자가 지도 학습을 수행합니다. 이 접근법은 매개변수와 연산량을 70% 이상 줄이고, 새로운 데이터에서 최대 5.79 dB PSNR 향상을 달성하며, 4배 빠른 적응 속도를 제공합니다. 또한, 이 프레임워크는 모듈화되어 있어 다양한 심층 전개 네트워크에 통합될 수 있습니다.

## 🎯 주요 포인트

- 1. SlowFast-SCI는 두 가지 학습 속도를 결합하여 새로운 광학 구성에 빠르게 적응할 수 있는 프레임워크를 제안합니다.
- 2. 이 프레임워크는 사전 학습된 백본을 활용하여 빠른 적응 모듈을 통합하고, 테스트 시 자가 지도 학습을 통해 적응합니다.
- 3. SlowFast-SCI는 파라미터와 FLOPs를 70% 이상 줄이고, 새로운 데이터에 대해 최대 5.79 dB PSNR 향상을 달성합니다.
- 4. 이 프레임워크는 다양한 딥 언폴딩 네트워크와 통합 가능하여, 자가 적응형 및 현장 배치 가능한 이미징을 지원합니다.
- 5. SlowFast-SCI의 코드는 GitHub에서 공개되어 있어, 연구자들이 쉽게 접근하고 활용할 수 있습니다.


---

*Generated on 2025-09-24 04:25:37*