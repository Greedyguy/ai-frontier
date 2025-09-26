<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:56:44.399942",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gradient Inversion",
    "Momentum Based Mixing",
    "Large Batch Processing",
    "Label-Free Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gradient Inversion": 0.78,
    "Momentum Based Mixing": 0.72,
    "Large Batch Processing": 0.65,
    "Label-Free Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gradient Inversion",
        "canonical": "Gradient Inversion",
        "aliases": [
          "Gradient Attack",
          "Gradient Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "Gradient inversion is a specific technique discussed in the paper, relevant for linking to topics in privacy and security within machine learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Momentum Based Mixing",
        "canonical": "Momentum Based Mixing",
        "aliases": [
          "Momentum Mixing",
          "Gradient Momentum Mixing"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, offering a new perspective on gradient optimization techniques.",
        "novelty_score": 0.81,
        "connectivity_score": 0.65,
        "specificity_score": 0.79,
        "link_intent_score": 0.72
      },
      {
        "surface": "Large Batch Scenarios",
        "canonical": "Large Batch Processing",
        "aliases": [
          "Batch Processing",
          "Batch Scenarios"
        ],
        "category": "broad_technical",
        "rationale": "Large batch processing is a common concept in machine learning, relevant for linking discussions on computational efficiency.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      },
      {
        "surface": "Label-Inference-Free Framework",
        "canonical": "Label-Free Learning",
        "aliases": [
          "Label-Free Framework",
          "Label-Inference-Free"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's contribution, highlighting a novel approach in learning without label inference.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "computational footprint"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gradient Inversion",
      "resolved_canonical": "Gradient Inversion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Momentum Based Mixing",
      "resolved_canonical": "Momentum Based Mixing",
      "decision": "linked",
      "scores": {
        "novelty": 0.81,
        "connectivity": 0.65,
        "specificity": 0.79,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Large Batch Scenarios",
      "resolved_canonical": "Large Batch Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Label-Inference-Free Framework",
      "resolved_canonical": "Label-Free Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MAGIA: Sensing Per-Image Signals from Single-Round Averaged Gradients for Label-Inference-Free Gradient Inversion

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18170.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18170](https://arxiv.org/abs/2509.18170)

## 🔗 유사한 논문
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (83.1% similar)
- [[2025-09-22/Analysis Plug-and-Play Methods for Imaging Inverse Problems_20250922|Analysis Plug-and-Play Methods for Imaging Inverse Problems]] (81.1% similar)
- [[2025-09-23/Neural-MMGS_ Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction_20250923|Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction]] (80.6% similar)
- [[2025-09-23/Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding_20250923|Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding]] (80.4% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Batch Processing|Large Batch Processing]]
**⚡ Unique Technical**: [[keywords/Gradient Inversion|Gradient Inversion]], [[keywords/Momentum Based Mixing|Momentum Based Mixing]], [[keywords/Label-Free Learning|Label-Free Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18170v1 Announce Type: new 
Abstract: We study gradient inversion in the challenging single round averaged gradient SAG regime where per sample cues are entangled within a single batch mean gradient. We introduce MAGIA a momentum based adaptive correction on gradient inversion attack a novel label inference free framework that senses latent per image signals by probing random data subsets. MAGIA objective integrates two core innovations 1 a closed form combinatorial rescaling that creates a provably tighter optimization bound and 2 a momentum based mixing of whole batch and subset losses to ensure reconstruction robustness. Extensive experiments demonstrate that MAGIA significantly outperforms advanced methods achieving high fidelity multi image reconstruction in large batch scenarios where prior works fail. This is all accomplished with a computational footprint comparable to standard solvers and without requiring any auxiliary information.

## 📝 요약

이 논문은 단일 라운드 평균 그래디언트(SAG) 환경에서의 그래디언트 반전 문제를 다룹니다. 저자들은 MAGIA라는 새로운 프레임워크를 제안하며, 이는 레이블 추론 없이 무작위 데이터 하위 집합을 탐색하여 이미지별 잠재 신호를 감지합니다. MAGIA는 두 가지 핵심 혁신을 통합합니다: 1) 최적화 경계를 강화하는 조합적 재조정의 폐쇄형 해법, 2) 전체 배치와 하위 집합 손실을 혼합하는 모멘텀 기반 접근법입니다. 실험 결과, MAGIA는 대규모 배치 시나리오에서 기존 방법들이 실패하는 다중 이미지 복원을 높은 정확도로 수행하며, 표준 솔버와 유사한 계산 비용으로 추가 정보 없이 이뤄집니다.

## 🎯 주요 포인트

- 1. 본 연구는 단일 라운드 평균 그래디언트(SAG) 환경에서의 그래디언트 역전 문제를 다룹니다.
- 2. MAGIA는 모멘텀 기반의 적응형 보정 기법을 사용하여 레이블 추론 없이 이미지 신호를 감지하는 새로운 프레임워크입니다.
- 3. MAGIA는 조합적 재스케일링과 모멘텀 기반의 손실 혼합을 통해 최적화 경계를 강화하고 복원 견고성을 보장합니다.
- 4. 실험 결과, MAGIA는 대용량 배치 시나리오에서 기존 방법들보다 뛰어난 성능을 보이며, 높은 정확도의 이미지 복원을 달성합니다.
- 5. MAGIA는 표준 솔버와 유사한 계산 자원을 사용하며, 추가적인 보조 정보 없이도 작동합니다.


---

*Generated on 2025-09-24 15:56:44*