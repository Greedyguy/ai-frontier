---
keywords:
  - Remote Sensing Change Detection
  - Bi-Temporal Deformable Alignment
  - Scale-Sparse Change Amplifier
  - State Space Models
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15563
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:01:19.621272",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Remote Sensing Change Detection",
    "Bi-Temporal Deformable Alignment",
    "Scale-Sparse Change Amplifier",
    "State Space Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Remote Sensing Change Detection": 0.78,
    "Bi-Temporal Deformable Alignment": 0.8,
    "Scale-Sparse Change Amplifier": 0.77,
    "State Space Models": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Remote Sensing Change Detection",
        "canonical": "Remote Sensing Change Detection",
        "aliases": [
          "RSCD"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, offering a unique technical perspective on change detection.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bi-Temporal Deformable Alignment",
        "canonical": "Bi-Temporal Deformable Alignment",
        "aliases": [
          "BTDA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel alignment method crucial for addressing geometric misalignments in change detection.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Scale-Sparse Change Amplifier",
        "canonical": "Scale-Sparse Change Amplifier",
        "aliases": [
          "SSCA"
        ],
        "category": "unique_technical",
        "rationale": "Enhances detection by selectively amplifying change signals, a key innovation in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "State Space Models",
        "canonical": "State Space Models",
        "aliases": [
          "SSMs"
        ],
        "category": "broad_technical",
        "rationale": "Provides a foundational context for the paper's improvements over existing methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
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
      "candidate_surface": "Remote Sensing Change Detection",
      "resolved_canonical": "Remote Sensing Change Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bi-Temporal Deformable Alignment",
      "resolved_canonical": "Bi-Temporal Deformable Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Scale-Sparse Change Amplifier",
      "resolved_canonical": "Scale-Sparse Change Amplifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "State Space Models",
      "resolved_canonical": "State Space Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection

**Korean Title:** DC-Mamba: 원격 감지 변화 탐지를 위한 이중 시간 변형 정렬 및 스케일 희소 강화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15563.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15563](https://arxiv.org/abs/2509.15563)

## 🔗 유사한 논문
- [[2025-09-22/Semantic Change Detection of Roads and Bridges_ A Fine-grained Dataset and Multimodal Frequency-driven Detector_20250922|Semantic Change Detection of Roads and Bridges: A Fine-grained Dataset and Multimodal Frequency-driven Detector]] (85.9% similar)
- [[2025-09-22/FoBa_ A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection_20250922|FoBa: A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection]] (84.9% similar)
- [[2025-09-22/RSCC_ A Large-Scale Remote Sensing Change Caption Dataset for Disaster Events_20250922|RSCC: A Large-Scale Remote Sensing Change Caption Dataset for Disaster Events]] (84.3% similar)
- [[2025-09-22/Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment_20250922|Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment]] (81.7% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/State Space Models|State Space Models]]
**⚡ Unique Technical**: [[keywords/Remote Sensing Change Detection|Remote Sensing Change Detection]], [[keywords/Bi-Temporal Deformable Alignment|Bi-Temporal Deformable Alignment]], [[keywords/Scale-Sparse Change Amplifier|Scale-Sparse Change Amplifier]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15563v1 Announce Type: new 
Abstract: Remote sensing change detection (RSCD) is vital for identifying land-cover changes, yet existing methods, including state-of-the-art State Space Models (SSMs), often lack explicit mechanisms to handle geometric misalignments and struggle to distinguish subtle, true changes from noise.To address this, we introduce DC-Mamba, an "align-then-enhance" framework built upon the ChangeMamba backbone. It integrates two lightweight, plug-and-play modules: (1) Bi-Temporal Deformable Alignment (BTDA), which explicitly introduces geometric awareness to correct spatial misalignments at the semantic feature level; and (2) a Scale-Sparse Change Amplifier(SSCA), which uses multi-source cues to selectively amplify high-confidence change signals while suppressing noise before the final classification. This synergistic design first establishes geometric consistency with BTDA to reduce pseudo-changes, then leverages SSCA to sharpen boundaries and enhance the visibility of small or subtle targets. Experiments show our method significantly improves performance over the strong ChangeMamba baseline, increasing the F1-score from 0.5730 to 0.5903 and IoU from 0.4015 to 0.4187. The results confirm the effectiveness of our "align-then-enhance" strategy, offering a robust and easily deployable solution that transparently addresses both geometric and feature-level challenges in RSCD.

## 🔍 Abstract (한글 번역)

arXiv:2509.15563v1 발표 유형: 신규  
초록: 원격 감지 변화 탐지(RSCD)는 토지 피복 변화 식별에 필수적이지만, 최신 상태 공간 모델(SSM)을 포함한 기존 방법들은 종종 기하학적 불일치를 처리하는 명시적 메커니즘이 부족하고, 미세한 실제 변화를 잡음과 구별하는 데 어려움을 겪습니다. 이를 해결하기 위해, 우리는 ChangeMamba 백본을 기반으로 한 "정렬 후 강화" 프레임워크인 DC-Mamba를 소개합니다. 이 프레임워크는 두 가지 경량의 플러그 앤 플레이 모듈을 통합합니다: (1) Bi-Temporal Deformable Alignment (BTDA)는 의미적 특징 수준에서 공간적 불일치를 수정하기 위해 기하학적 인식을 명시적으로 도입합니다; (2) Scale-Sparse Change Amplifier(SSCA)는 다중 소스 단서를 사용하여 높은 신뢰도의 변화 신호를 선택적으로 증폭하면서 최종 분류 전에 잡음을 억제합니다. 이 시너지적 설계는 먼저 BTDA를 통해 기하학적 일관성을 확립하여 가상 변화를 줄이고, 그 다음 SSCA를 활용하여 경계를 선명하게 하고 작은 또는 미세한 목표의 가시성을 향상시킵니다. 실험 결과, 우리의 방법은 강력한 ChangeMamba 기준선에 비해 성능을 크게 향상시켜 F1 점수를 0.5730에서 0.5903으로, IoU를 0.4015에서 0.4187로 증가시켰습니다. 결과는 우리의 "정렬 후 강화" 전략의 효과를 확인하며, RSCD에서 기하학적 및 특징 수준의 문제를 투명하게 해결하는 강력하고 쉽게 배포 가능한 솔루션을 제공합니다.

## 📝 요약

이 논문은 원격 감지 변화 탐지(RSCD)에서 지리적 불일치와 노이즈로 인한 미세한 변화를 구별하는 문제를 해결하기 위해 DC-Mamba라는 "정렬 후 강화" 프레임워크를 제안합니다. ChangeMamba를 기반으로 한 이 프레임워크는 두 가지 모듈을 통합합니다: (1) Bi-Temporal Deformable Alignment(BTDA)로, 공간적 불일치를 교정하여 기하학적 일관성을 확보하고, (2) Scale-Sparse Change Amplifier(SSCA)로, 다중 소스 단서를 활용해 고신뢰 변화 신호를 선택적으로 증폭합니다. 실험 결과, 이 방법은 F1-score를 0.5730에서 0.5903으로, IoU를 0.4015에서 0.4187로 향상시켜 기존 ChangeMamba보다 성능을 크게 개선했습니다. 이 연구는 RSCD에서 기하학적 및 특징 수준의 문제를 효과적으로 해결하는 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. DC-Mamba는 지리적 불일치를 해결하고 미세한 변화를 감지하기 위해 "align-then-enhance" 프레임워크를 도입했습니다.
- 2. Bi-Temporal Deformable Alignment(BTDA) 모듈은 공간적 불일치를 수정하기 위해 기하학적 인식을 명시적으로 도입합니다.
- 3. Scale-Sparse Change Amplifier(SSCA) 모듈은 다중 소스 단서를 사용하여 고신뢰도 변화 신호를 선택적으로 증폭하고 노이즈를 억제합니다.
- 4. 실험 결과, DC-Mamba는 F1-score를 0.5730에서 0.5903으로, IoU를 0.4015에서 0.4187로 향상시켰습니다.
- 5. 이 연구는 RSCD에서 기하학적 및 특징 수준의 문제를 투명하게 해결하는 강력하고 쉽게 배포 가능한 솔루션을 제공합니다.


---

*Generated on 2025-09-23 12:01:19*