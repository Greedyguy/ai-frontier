---
keywords:
  - Domain Generalization
  - Test-Time Augmentation
  - Deep Learning
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:59:15.113896",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Domain Generalization",
    "Test-Time Augmentation",
    "Deep Learning"
  ],
  "rejected_keywords": [
    "Confidence-Guided Filtering"
  ],
  "similarity_scores": {
    "Domain Generalization": 0.78,
    "Test-Time Augmentation": 0.77,
    "Deep Learning": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Class-invariant Test-Time Augmentation for Domain Generalization

**Korean Title:** 도메인 일반화를 위한 클래스 불변 테스트 시점 증강

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|Deep Models]]
**⚡ Unique Technical**: [[keywords/Domain Generalization|Domain Generalization]], [[keywords/Test-Time Augmentation|Test-Time Augmentation]]

## 🔗 유사한 논문
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (83.1% similar)
- [[DiffGAN_ A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis_20250918|DiffGAN A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis]] (82.5% similar)
- [[Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (82.0% similar)
- [[Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses_20250919|Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses]] (81.7% similar)
- [[TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (80.4% similar)

## 📋 저자 정보

**Authors:** Zhicheng Lin, Xiaolin Wu, Xi Zhang

## 📄 Abstract (원문)

Deep models often suffer significant performance degradation under
distribution shifts. Domain generalization (DG) seeks to mitigate this
challenge by enabling models to generalize to unseen domains. Most prior
approaches rely on multi-domain training or computationally intensive test-time
adaptation. In contrast, we propose a complementary strategy: lightweight
test-time augmentation. Specifically, we develop a novel Class-Invariant
Test-Time Augmentation (CI-TTA) technique. The idea is to generate multiple
variants of each input image through elastic and grid deformations that
nevertheless belong to the same class as the original input. Their predictions
are aggregated through a confidence-guided filtering scheme that remove
unreliable outputs, ensuring the final decision relies on consistent and
trustworthy cues. Extensive Experiments on PACS and Office-Home datasets
demonstrate consistent gains across different DG algorithms and backbones,
highlighting the effectiveness and generality of our approach.

## 🔍 Abstract (한글 번역)

깊은 모델은 종종 분포 변화에 따라 성능이 크게 저하되는 문제를 겪습니다. 도메인 일반화(DG)는 모델이 보지 못한 도메인으로 일반화할 수 있도록 하여 이러한 문제를 완화하려고 합니다. 대부분의 기존 접근 방식은 다중 도메인 훈련이나 계산 집약적인 테스트 시점 적응에 의존합니다. 이에 반해, 우리는 경량 테스트 시점 증강이라는 보완적인 전략을 제안합니다. 구체적으로, 우리는 새로운 클래스 불변 테스트 시점 증강(Class-Invariant Test-Time Augmentation, CI-TTA) 기법을 개발했습니다. 이 기법의 핵심 아이디어는 탄성 및 그리드 변형을 통해 각 입력 이미지의 여러 변형을 생성하되, 여전히 원래 입력과 동일한 클래스에 속하도록 하는 것입니다. 이러한 변형의 예측은 신뢰도 기반 필터링 체계를 통해 집계되어 신뢰할 수 없는 출력을 제거하고, 최종 결정이 일관되고 신뢰할 수 있는 단서에 의존하도록 합니다. PACS 및 Office-Home 데이터셋에 대한 광범위한 실험은 다양한 DG 알고리즘과 백본에서 일관된 성능 향상을 보여주며, 우리의 접근 방식의 효과성과 일반성을 강조합니다.

## 📝 요약

이 논문은 분포 변화에 따른 성능 저하 문제를 해결하기 위해 도메인 일반화(DG)를 연구하며, 기존의 다중 도메인 학습이나 복잡한 테스트 시 적응 대신 경량화된 테스트 시 증강 방법을 제안합니다. 제안된 방법인 클래스 불변 테스트 시 증강(CI-TTA)은 입력 이미지의 변형을 통해 같은 클래스 내 다양한 변형 이미지를 생성하고, 신뢰도 기반 필터링을 통해 일관되고 신뢰할 수 있는 예측을 도출합니다. PACS와 Office-Home 데이터셋에서의 실험 결과, 다양한 DG 알고리즘과 백본에서 일관된 성능 향상을 보여주며, 제안된 방법의 효과성과 일반성을 입증합니다.

## 🎯 주요 포인트

- 1. 딥러닝 모델은 분포 변화에 따라 성능 저하를 겪으며, 도메인 일반화(DG)는 이를 완화하기 위해 보이지 않는 도메인에 일반화하는 것을 목표로 한다.

- 2. 기존 방법들은 다중 도메인 학습이나 계산 집약적인 테스트 시간 적응에 의존하는 반면, 본 연구는 경량화된 테스트 시간 증강 전략을 제안한다.

- 3. 제안된 Class-Invariant Test-Time Augmentation (CI-TTA) 기법은 탄력적 및 격자 변형을 통해 입력 이미지의 다양한 변형을 생성하고, 신뢰도 기반 필터링을 통해 일관되고 신뢰할 수 있는 예측을 보장한다.

- 4. PACS 및 Office-Home 데이터셋에서의 실험 결과, 제안된 방법이 다양한 DG 알고리즘과 백본에서 일관된 성능 향상을 보여주며, 접근법의 효과성과 일반성을 강조한다.

---

*Generated on 2025-09-20 07:35:42*