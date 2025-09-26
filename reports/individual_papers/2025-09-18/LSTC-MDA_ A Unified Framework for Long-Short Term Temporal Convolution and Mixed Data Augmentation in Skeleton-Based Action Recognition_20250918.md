---
keywords:
  - Long-Short Term Temporal Convolution
  - Convolutional Neural Networks
  - Skeleton-Based Action Recognition
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:23:14.738666",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Long-Short Term Temporal Convolution",
    "Convolutional Neural Networks",
    "Skeleton-Based Action Recognition"
  ],
  "rejected_keywords": [
    "Mixed Data Augmentation"
  ],
  "similarity_scores": {
    "Long-Short Term Temporal Convolution": 0.82,
    "Convolutional Neural Networks": 0.8,
    "Skeleton-Based Action Recognition": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# LSTC-MDA: A Unified Framework for Long-Short Term Temporal Convolution and Mixed Data Augmentation in Skeleton-Based Action Recognition

**Korean Title:** LSTC-MDA: 골격 기반 행동 인식에서 장단기 시계열 컨볼루션과 혼합 데이터 증강을 위한 통합 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Convolutional Neural Networks|Convolutional Neural Networks]]
**⚡ Unique Technical**: [[keywords/Long-Short Term Temporal Convolution|Long-Short Term Temporal Convolution]], [[keywords/Skeleton-Based Action Recognition|Skeleton-Based Action Recognition]]

## 🔗 유사한 논문
- [[Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (81.5% similar)
- [[Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles Acquiring and Accumulating Knowledge from Diverse Datasets]] (81.2% similar)
- [[Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (80.1% similar)
- [[Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (79.9% similar)
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (79.9% similar)

## 📋 저자 정보

**Authors:** Feng Ding, Haisheng Fu, Soroush Oraki, Jie Liang

## 📄 Abstract (원문)

Skeleton-based action recognition faces two longstanding challenges: the
scarcity of labeled training samples and difficulty modeling short- and
long-range temporal dependencies. To address these issues, we propose a unified
framework, LSTC-MDA, which simultaneously improves temporal modeling and data
diversity. We introduce a novel Long-Short Term Temporal Convolution (LSTC)
module with parallel short- and long-term branches, these two feature branches
are then aligned and fused adaptively using learned similarity weights to
preserve critical long-range cues lost by conventional stride-2 temporal
convolutions. We also extend Joint Mixing Data Augmentation (JMDA) with an
Additive Mixup at the input level, diversifying training samples and
restricting mixup operations to the same camera view to avoid distribution
shifts. Ablation studies confirm each component contributes. LSTC-MDA achieves
state-of-the-art results: 94.1% and 97.5% on NTU 60 (X-Sub and X-View), 90.4%
and 92.0% on NTU 120 (X-Sub and X-Set),97.2% on NW-UCLA. Code:
https://github.com/xiaobaoxia/LSTC-MDA.

## 🔍 Abstract (한글 번역)

골격 기반 행동 인식은 두 가지 오랜 과제에 직면해 있습니다: 라벨이 지정된 훈련 샘플의 부족과 단기 및 장기 시간 의존성을 모델링하는 데 어려움이 있다는 점입니다. 이러한 문제를 해결하기 위해, 우리는 시간 모델링과 데이터 다양성을 동시에 개선하는 통합 프레임워크인 LSTC-MDA를 제안합니다. 우리는 병렬 단기 및 장기 분기를 가진 새로운 장단기 시간 컨볼루션(Long-Short Term Temporal Convolution, LSTC) 모듈을 도입하며, 이 두 가지 특징 분기는 학습된 유사성 가중치를 사용하여 적응적으로 정렬되고 융합되어, 기존의 stride-2 시간 컨볼루션에 의해 손실된 중요한 장기 단서를 보존합니다. 또한, 입력 수준에서 Additive Mixup을 통해 Joint Mixing Data Augmentation (JMDA)을 확장하여 훈련 샘플을 다양화하고, 분포 이동을 피하기 위해 동일한 카메라 뷰로 믹스업 작업을 제한합니다. 소거 연구는 각 구성 요소가 기여함을 확인합니다. LSTC-MDA는 최첨단 결과를 달성합니다: NTU 60에서 94.1% 및 97.5% (X-Sub 및 X-View), NTU 120에서 90.4% 및 92.0% (X-Sub 및 X-Set), NW-UCLA에서 97.2%. 코드: https://github.com/xiaobaoxia/LSTC-MDA.

## 📝 요약

이 논문은 골격 기반 행동 인식의 두 가지 주요 문제인 라벨링된 훈련 샘플의 부족과 시간적 의존성 모델링의 어려움을 해결하기 위해 LSTC-MDA라는 통합 프레임워크를 제안합니다. 새로운 장단기 시간 컨볼루션(LSTC) 모듈을 도입하여 장단기 특징을 병렬로 처리하고, 학습된 유사도 가중치를 통해 적응적으로 융합하여 중요한 장기 정보를 보존합니다. 또한, 입력 수준에서의 Additive Mixup을 통해 Joint Mixing Data Augmentation(JMDA)을 확장하여 훈련 샘플의 다양성을 높이고, 동일한 카메라 뷰 내에서만 믹스업을 제한하여 분포 변화를 방지합니다. 각 구성 요소의 기여도를 확인한 결과, LSTC-MDA는 NTU 60 및 NTU 120 데이터셋에서 최첨단 성능을 기록했습니다.

## 🎯 주요 포인트

- 1. LSTC-MDA 프레임워크는 짧고 긴 시간적 의존성을 동시에 모델링하여 골격 기반 행동 인식의 문제를 해결합니다.

- 2. 새로운 LSTC 모듈은 병렬 단기 및 장기 분기를 통해 중요한 장기 단서를 보존합니다.

- 3. JMDA에 입력 수준의 Additive Mixup을 확장하여 데이터 다양성을 높이고 분포 변화를 방지합니다.

- 4. 각 구성 요소의 기여도가 입증되었으며, LSTC-MDA는 NTU 60 및 NTU 120 데이터셋에서 최첨단 성능을 달성합니다.

---

*Generated on 2025-09-20 05:48:54*