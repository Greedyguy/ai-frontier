# Autoguided Online Data Curation for Diffusion Model Training

**Korean Title:** 자동화된 온라인 데이터 큐레이션을 통한 확산 모델 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Diffusion Models, Online Data Selection

## 🔗 유사한 논문
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (79.9% similar)
- [[2025-09-19/Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (79.6% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (79.3% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN Layout-guided 3D Indoor Scene Generation]] (79.2% similar)
- [[2025-09-19/A Mutual Information Perspective on Multiple Latent Variable Generative Models for Positive View Generation_20250919|A Mutual Information Perspective on Multiple Latent Variable Generative Models for Positive View Generation]] (79.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15267v1 Announce Type: cross 
Abstract: The costs of generative model compute rekindled promises and hopes for efficient data curation. In this work, we investigate whether recently developed autoguidance and online data selection methods can improve the time and sample efficiency of training generative diffusion models. We integrate joint example selection (JEST) and autoguidance into a unified code base for fast ablation and benchmarking. We evaluate combinations of data curation on a controlled 2-D synthetic data generation task as well as (3x64x64)-D image generation. Our comparisons are made at equal wall-clock time and equal number of samples, explicitly accounting for the overhead of selection. Across experiments, autoguidance consistently improves sample quality and diversity. Early AJEST (applying selection only at the beginning of training) can match or modestly exceed autoguidance alone in data efficiency on both tasks. However, its time overhead and added complexity make autoguidance or uniform random data selection preferable in most situations. These findings suggest that while targeted online selection can yield efficiency gains in early training, robust sample quality improvements are primarily driven by autoguidance. We discuss limitations and scope, and outline when data selection may be beneficial.

## 🔍 Abstract (한글 번역)

arXiv:2509.15267v1 발표 유형: 교차  
초록: 생성 모델 계산 비용은 효율적인 데이터 큐레이션에 대한 약속과 희망을 다시 불러일으켰습니다. 이 연구에서는 최근 개발된 자동 가이던스 및 온라인 데이터 선택 방법이 생성 확산 모델의 훈련 시간과 샘플 효율성을 향상시킬 수 있는지 조사합니다. 우리는 빠른 소거 및 벤치마킹을 위해 공동 예제 선택(JEST)과 자동 가이던스를 통합하여 통합된 코드 기반을 구축했습니다. 우리는 제어된 2차원 합성 데이터 생성 작업과 (3x64x64)-D 이미지 생성에서 데이터 큐레이션 조합을 평가합니다. 비교는 선택의 오버헤드를 명시적으로 고려하여 동일한 실시간 및 동일한 샘플 수에서 이루어집니다. 실험 전반에 걸쳐 자동 가이던스는 샘플의 품질과 다양성을 일관되게 향상시킵니다. 초기 AJEST(훈련 초기에만 선택 적용)는 두 작업 모두에서 데이터 효율성 면에서 자동 가이던스 단독과 비슷하거나 약간 초과할 수 있습니다. 그러나 시간 오버헤드와 추가 복잡성 때문에 대부분의 상황에서는 자동 가이던스나 균일한 무작위 데이터 선택이 더 바람직합니다. 이러한 결과는 목표 지향적 온라인 선택이 초기 훈련에서 효율성을 향상시킬 수 있지만, 견고한 샘플 품질 개선은 주로 자동 가이던스에 의해 주도된다는 것을 시사합니다. 우리는 한계와 범위를 논의하고 데이터 선택이 유익할 수 있는 경우를 개략적으로 설명합니다.

## 📝 요약

이 연구는 생성 모델의 학습 효율성을 높이기 위해 최근 개발된 자동 가이던스와 온라인 데이터 선택 방법의 효과를 조사합니다. 연구에서는 JEST와 자동 가이던스를 통합하여 빠른 실험과 벤치마킹을 수행했습니다. 2차원 합성 데이터 생성과 (3x64x64)-D 이미지 생성 작업에서 데이터 큐레이션 조합을 평가한 결과, 자동 가이던스는 샘플의 품질과 다양성을 꾸준히 향상시키는 것으로 나타났습니다. 초기 AJEST는 데이터 효율성 면에서 자동 가이던스와 비슷하거나 약간 뛰어났으나, 시간 소모와 복잡성 때문에 대부분의 상황에서는 자동 가이던스나 무작위 데이터 선택이 더 바람직합니다. 연구는 초기 훈련에서의 온라인 선택이 효율성을 높일 수 있지만, 샘플 품질 개선은 주로 자동 가이던스에 의해 이루어진다는 점을 시사합니다. 제한점과 데이터 선택의 유용성을 논의합니다.

## 🎯 주요 포인트

- 1. 생성 모델의 계산 비용 문제를 해결하기 위해 데이터 큐레이션의 효율성을 조사했습니다.

- 2. JEST와 autoguidance를 통합하여 생성 확산 모델의 학습 효율성을 평가했습니다.

- 3. autoguidance는 샘플의 품질과 다양성을 일관되게 향상시켰습니다.

- 4. 초기 AJEST는 데이터 효율성 면에서 autoguidance와 비슷하거나 약간 우수할 수 있지만, 시간 소요와 복잡성 때문에 autoguidance가 더 선호됩니다.

- 5. 데이터 선택은 초기 학습 단계에서 효율성을 높일 수 있지만, 샘플 품질 개선은 주로 autoguidance에 의해 이루어집니다.

---

*Generated on 2025-09-22 13:51:20*