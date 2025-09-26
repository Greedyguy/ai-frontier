---
keywords:
  - Mixed-Integer Linear Programming
  - Deep Learning
  - Automated Test-Input Validation
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2507.04990
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:31:06.191146",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixed-Integer Linear Programming",
    "Deep Learning",
    "Automated Test-Input Validation"
  ],
  "rejected_keywords": [
    "Computer Vision"
  ],
  "similarity_scores": {
    "Mixed-Integer Linear Programming": 0.8,
    "Deep Learning": 0.85,
    "Automated Test-Input Validation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Effort-Optimized, Accuracy-Driven Labelling and Validation of Test Inputs for DL Systems: A Mixed-Integer Linear Programming Approach

**Korean Title:** 딥러닝 시스템을 위한 노력 최적화, 정확도 중심의 테스트 입력 라벨링 및 유효성 검사: 혼합 정수 선형 프로그래밍 접근 방식

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Mixed-Integer Linear Programming|Mixed-Integer Linear Programming]], [[keywords/Automated Test-Input Validation|Automated Test-Input Validation]]

## 🔗 유사한 논문
- [[MetaSel_A_Test_Selection_Approach_for_Fine-tuned_DNN_Models_20250918|MetaSel: A Test Selection Approach for Fine-tuned DNN Models]] (78.4% similar)
- [[Post-Hoc_Split-Point_Self-Consistency_Verification_for_Efficient,_Unified_Quantification_of_Aleatoric_and_Epistemic_Uncertainty_in_Deep_Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (78.2% similar)
- [[Controllable Pareto Trade-off between Fairness and Accuracy]] (77.8% similar)
- [[Designing_AI-Agents_with_Personalities_A_Psychometric_Approach_20250918|Designing AI-Agents with Personalities: A Psychometric Approach]] (77.4% similar)
- [[Using LLMs in Generating Design Rationale for Software Architecture Decisions]] (77.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.04990v2 Announce Type: replace 
Abstract: Software systems increasingly include AI components based on deep learning (DL). Reliable testing of such systems requires near-perfect test-input validity and label accuracy, with minimal human effort. Yet, the DL community has largely overlooked the need to build highly accurate datasets with minimal effort, since DL training is generally tolerant of labelling errors. This challenge, instead, reflects concerns more familiar to software engineering, where a central goal is to construct high-accuracy test inputs, with accuracy as close to 100% as possible, while keeping associated costs in check. In this article we introduce OPAL, a human-assisted labelling method that can be configured to target a desired accuracy level while minimizing the manual effort required for labelling. The main contribution of OPAL is a mixed-integer linear programming (MILP) formulation that minimizes labelling effort subject to a specified accuracy target. To evaluate OPAL we instantiate it for two tasks in the context of testing vision systems: automatic labelling of test inputs and automated validation of test inputs. Our evaluation, based on more than 2500 experiments performed on seven datasets, comparing OPAL with eight baseline methods, shows that OPAL, relying on its MILP formulation, achieves an average accuracy of 98.8%, while cutting manual labelling by more than half. OPAL significantly outperforms automated labelling baselines in labelling accuracy across all seven datasets, when all methods are provided with the same manual-labelling budget. For automated test-input validation, on average, OPAL reduces manual effort by 28.8% while achieving 4.5% higher accuracy than the SOTA test-input validation baselines. Finally, we show that augmenting OPAL with an active-learning loop leads to an additional 4.5% reduction in required manual labelling, without compromising accuracy.

## 🔍 Abstract (한글 번역)

arXiv:2507.04990v2 발표 유형: 대체
요약: 소프트웨어 시스템은 점점 더 딥 러닝(DL)을 기반으로 한 AI 구성 요소를 포함하고 있습니다. 이러한 시스템의 신뢰성 있는 테스트를 위해서는 거의 완벽한 테스트 입력 유효성과 레이블 정확성이 필요하며, 인간의 노력을 최소화해야 합니다. 그러나 DL 커뮤니티는 일반적으로 레이블링 오류에 관대한 DL 훈련 때문에 최소한의 노력으로 높은 정확도의 데이터셋을 구축해야 한다는 필요성을 대부분 간과해 왔습니다. 이러한 도전 과제는 대신 소프트웨어 공학에서 더 익숙한 우려를 반영하며, 중심적인 목표는 정확도를 가능한 한 100%에 가깝게 유지하면서 관련 비용을 확인하는 것입니다. 본 논문에서는 OPAL이라는 인간 지원 레이블링 방법을 소개하며, 이 방법은 레이블링에 필요한 수동 노력을 최소화하면서 원하는 정확도 수준을 목표로 설정할 수 있습니다. OPAL의 주요 기여는 지정된 정확도 목표에 따라 레이블링 노력을 최소화하는 혼합정수선형프로그래밍(MILP) 공식입니다. OPAL을 평가하기 위해 시각 시스템 테스트의 두 가지 작업에 대해 인스턴스화하였습니다: 테스트 입력의 자동 레이블링 및 테스트 입력의 자동 검증. 7개 데이터셋에서 수행된 2500개 이상의 실험에 기초한 평가 결과, OPAL은 MILP 공식을 통해 평균 정확도 98.8%를 달성하면서 수동 레이블링을 절반 이상으로 줄였습니다. 모든 방법이 동일한 수동 레이블링 예산을 제공받을 때, OPAL은 7개 데이터셋 전체에서 자동 레이블링 기준에 비해 레이블링 정확도가 현저히 뛰어났습니다. 평균적으로 자동 테스트 입력 검증에서 OPAL은 수동 노력을 28.8% 줄이면서 SOTA 테스트 입력 검증 기준보다 4.5% 더 높은 정확도를 달성했습니다. 마지막으로, OPAL에 액티브 러닝 루프를 추가하면 필요한 수동 레이블링이 추가로 4.5% 감소하면서 정확도를 희생하지 않습니다.

## 📝 요약

본 연구는 딥러닝 기반의 AI 구성 요소를 포함하는 소프트웨어 시스템의 신뢰성 있는 테스트를 위해 높은 정확도의 데이터셋을 최소한의 노력으로 구축하는 방법을 제안한다. OPAL이라는 인간 지원 라벨링 방법을 소개하며, 이는 특정 정확도 수준을 목표로 설정하면서 라벨링에 필요한 수동 노력을 최소화하는 MILP 수식을 제공한다. 실험 결과, OPAL은 다양한 데이터셋에서 평균 98.8%의 정확도를 달성하면서 수동 라벨링을 절반 이상으로 줄였으며, 자동 라벨링 및 검증 방법들을 능가하는 성과를 보였다. 또한, OPAL에 적응 학습 루프를 추가하면 추가적인 수동 라벨링 감소와 정확도 유지가 가능함을 보여준다.

## 🎯 주요 포인트

- 1. 딥러닝 기반 AI 구성 요소를 포함하는 소프트웨어 시스템의 신뢰성 있는 테스트를 위해 높은 정확도의 테스트 입력 및 레이블 정확도가 필요하며, 최소한의 인간 노력이 필요하다.

- 2. OPAL은 원하는 정확도 수준을 목표로 설정하고 레이블링에 필요한 수동 노력을 최소화하는 인간 지원 레이블링 방법을 소개한다.

- 3. OPAL은 MILP 공식을 활용하여 평균 정확도 98.8%를 달성하면서 수동 레이블링을 절반 이상으로 줄이는 것으로 나타났다.

---

*Generated on 2025-09-18 17:07:09*