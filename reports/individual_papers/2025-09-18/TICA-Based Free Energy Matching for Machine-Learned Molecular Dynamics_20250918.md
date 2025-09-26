---
keywords:
  - Multi-Modal Learning
  - Molecular Dynamics
  - Free Energy Surface
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:07:29.504828",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Modal Learning",
    "Molecular Dynamics",
    "Free Energy Surface"
  ],
  "rejected_keywords": [
    "Coarse-Grained Machine Learning",
    "Energy Matching"
  ],
  "similarity_scores": {
    "Multi-Modal Learning": 0.8,
    "Molecular Dynamics": 0.75,
    "Free Energy Surface": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# TICA-Based Free Energy Matching for Machine-Learned Molecular Dynamics

**Korean Title:** TICA 기반 자유 에너지 매칭을 통한 기계 학습 분자동역학

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Molecular Dynamics|Molecular Dynamics]], [[keywords/Free Energy Surface|Free Energy Surface]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|Multi-Modal Loss Formulations]]

## 🔗 유사한 논문
- [[Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (78.1% similar)
- [[Template-Based Cortical Surface Reconstruction with Minimal Energy Deformation_20250918|Template-Based Cortical Surface Reconstruction with Minimal Energy Deformation]] (77.5% similar)
- [[Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (77.5% similar)
- [[Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (76.7% similar)
- [[Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (76.0% similar)

## 📋 저자 정보

**Authors:** Alexander Aghili, Andy Bruce, Daniel Sabo, Razvan Marinescu

## 📄 Abstract (원문)

Molecular dynamics (MD) simulations provide atomistic insight into
biomolecular systems but are often limited by high computational costs required
to access long timescales. Coarse-grained machine learning models offer a
promising avenue for accelerating sampling, yet conventional force matching
approaches often fail to capture the full thermodynamic landscape as fitting a
model on the gradient may not fit the absolute differences between low-energy
conformational states. In this work, we incorporate a complementary energy
matching term into the loss function. We evaluate our framework on the
Chignolin protein using the CGSchNet model, systematically varying the weight
of the energy loss term. While energy matching did not yield statistically
significant improvements in accuracy, it revealed distinct tendencies in how
models generalize the free energy surface. Our results suggest future
opportunities to enhance coarse-grained modeling through improved energy
estimation techniques and multi-modal loss formulations.

## 🔍 Abstract (한글 번역)

분자 동역학(MD) 시뮬레이션은 생체분자 시스템에 대한 원자 수준의 통찰력을 제공하지만, 긴 시간 척도에 접근하기 위해 필요한 높은 계산 비용으로 인해 종종 제한됩니다. 거시적 기계 학습 모델은 샘플링을 가속화할 수 있는 유망한 방법을 제공하지만, 기존의 힘 매칭 접근법은 종종 열역학적 풍경을 완전히 포착하지 못합니다. 이는 모델을 기울기에 맞추는 것이 저에너지 구조 상태 간의 절대적인 차이를 맞추지 못할 수 있기 때문입니다. 본 연구에서는 보완적인 에너지 매칭 항을 손실 함수에 통합하였습니다. 우리는 CGSchNet 모델을 사용하여 Chignolin 단백질에 대한 프레임워크를 평가하고, 에너지 손실 항의 가중치를 체계적으로 변화시켰습니다. 에너지 매칭이 정확성에서 통계적으로 유의미한 개선을 가져오지는 않았지만, 모델이 자유 에너지 표면을 일반화하는 방식에서 뚜렷한 경향을 드러냈습니다. 우리의 결과는 향후 개선된 에너지 추정 기법과 다중 모드 손실 공식화를 통해 거시적 모델링을 향상시킬 수 있는 기회를 제시합니다.

## 📝 요약

이 연구는 분자동역학 시뮬레이션의 계산 비용 문제를 해결하기 위해 머신러닝 기반의 조잡화 모델을 활용하여 샘플링을 가속화하는 방법을 제안합니다. 기존의 힘 맞춤 방식이 저에너지 상태 간의 절대적 차이를 잘 포착하지 못하는 문제를 해결하기 위해, 손실 함수에 에너지 맞춤 항을 추가했습니다. Chignolin 단백질을 대상으로 CGSchNet 모델을 사용해 에너지 손실 항의 가중치를 조정하며 평가한 결과, 에너지 맞춤이 정확성을 통계적으로 유의미하게 개선하지는 않았지만, 모델이 자유 에너지 표면을 일반화하는 경향을 드러냈습니다. 이는 향후 에너지 추정 기법과 다중 모드 손실 공식화를 통해 조잡화 모델링을 개선할 기회를 시사합니다.

## 🎯 주요 포인트

- 1. 분자동역학 시뮬레이션은 생체분자 시스템에 대한 원자 수준의 통찰을 제공하지만, 긴 시간 척도에 접근하기 위한 높은 계산 비용으로 제한된다.

- 2. 기존의 힘 맞춤 접근법은 저에너지 형태 상태 간의 절대 차이를 잘 반영하지 못해 전체 열역학적 풍경을 포착하는 데 실패할 수 있다.

- 3. 본 연구에서는 손실 함수에 보완적인 에너지 맞춤 항을 도입하여 모델의 일반화 경향을 분석하였다.

- 4. 에너지 맞춤은 정확도에서 통계적으로 유의미한 개선을 가져오지 않았지만, 자유 에너지 표면을 일반화하는 모델의 경향성을 드러냈다.

- 5. 본 연구 결과는 향후 에너지 추정 기술과 다중 모드 손실 공식화를 통해 조잡한 모델링을 개선할 기회를 제시한다.

---

*Generated on 2025-09-20 05:50:20*