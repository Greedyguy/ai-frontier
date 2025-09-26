---
keywords:
  - Subspace Identification Methods
  - Finite Sample Analysis
  - Hankel-like Matrix
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2501.16639
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:28:41.339192",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Subspace Identification Methods",
    "Finite Sample Analysis",
    "Hankel-like Matrix"
  ],
  "rejected_keywords": [
    "Model Reduction"
  ],
  "similarity_scores": {
    "Subspace Identification Methods": 0.78,
    "Finite Sample Analysis": 0.75,
    "Hankel-like Matrix": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Finite Sample Analysis of Open-loop Subspace Identification Methods

**Korean Title:** 오픈 루프 부분 공간 식별 방법의 유한 샘플 분석

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Subspace Identification Methods|Subspace Identification Methods]], [[keywords/Finite Sample Analysis|Finite Sample Analysis]], [[keywords/Hankel-like Matrix|Hankel-like Matrix]]

## 🔗 유사한 논문
- [[Post-Hoc_Split-Point_Self-Consistency_Verification_for_Efficient,_Unified_Quantification_of_Aleatoric_and_Epistemic_Uncertainty_in_Deep_Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (77.2% similar)
- [[Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (76.7% similar)
- [[Asymptotic_Boundedness_of_Distributed_Set-Membership_Filtering_20250918|Asymptotic Boundedness of Distributed Set-Membership Filtering]] (76.1% similar)
- [[Robust,_positive_and_exact_model_reduction_via_monotone_matrices_20250918|Robust, positive and exact model reduction via monotone matrices]] (75.6% similar)
- [[Inject, Fork, Compare: Defining an Interaction Vocabulary for Multi-Agent Simulation Platforms]] (74.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.16639v2 Announce Type: replace 
Abstract: Subspace identification methods (SIMs) are known for their simple parameterization for MIMO systems and robust numerical properties. However, a comprehensive statistical analysis of SIMs remains an open problem. Following a three-step procedure generally used in SIMs, this work presents a finite sample analysis for open-loop SIMs. In Step 1 we begin with a parsimonious SIM. Leveraging a recent analysis of an individual ARX model, we obtain a union error bound for a Hankel-like matrix constructed from a bank of ARX models. Step 2 involves model reduction via weighted singular value decomposition (SVD), where we use robustness results for SVD to obtain error bounds on extended controllability and observability matrices, respectively. The final Step 3 focuses on deriving error bounds for system matrices, where two different realization algorithms, the MOESP type and the CVA type, are studied. Our results not only agree with classical asymptotic results, but also show how much data is needed to guarantee a desired error bound with high probability. The proposed method generalizes related finite sample analyses and applies broadly to many variants of SIMs.

## 🔍 Abstract (한글 번역)

arXiv:2501.16639v2 발표 유형: 대체
요약: 부분 공간 식별 방법(SIMs)은 MIMO 시스템에 대한 간단한 매개변수화와 견고한 수치적 특성으로 알려져 있습니다. 그러나 SIMs에 대한 포괄적인 통계 분석은 여전히 열린 문제입니다. SIMs에서 일반적으로 사용되는 세 단계 절차를 따라, 본 연구는 오픈 루프 SIMs에 대한 유한 샘플 분석을 제시합니다. 단계 1에서는 간소화된 SIM으로 시작합니다. 최근 ARX 모델의 개별 분석을 활용하여, ARX 모델의 은행에서 구성된 Hankel과 유사한 행렬에 대한 연합 오차 한계를 얻습니다. 단계 2는 가중 특이값 분해(SVD)를 통한 모델 축소를 포함하며, SVD의 견고성 결과를 사용하여 각각 확장된 제어 가능성 및 관측 가능성 행렬에 대한 오차 한계를 얻습니다. 마지막 단계 3은 시스템 행렬에 대한 오차 한계 유도에 초점을 맞추며, MOESP 유형과 CVA 유형의 두 가지 다른 실현 알고리즘을 연구합니다. 우리의 결과는 고전적인 점근적 결과와 일치뿐만 아니라, 원하는 오차 한계를 확률적으로 보장하기 위해 얼마나 많은 데이터가 필요한지 보여줍니다. 제안된 방법은 관련된 유한 샘플 분석을 일반화하고 SIMs의 여러 변형에 널리 적용됩니다.

## 📝 요약

이 논문은 다변량 입력 다변량 출력 시스템에 대한 부분 공간 식별 방법(SIMs)의 통계적 분석을 다룬다. SIMs는 간단한 모수화와 강력한 수치적 특성으로 알려져 있지만, 종합적인 통계 분석은 여전히 미해결 문제이다. 본 연구는 SIMs에서 일반적으로 사용되는 세 단계 절차를 따라 개방 루프 SIMs에 대한 유한 샘플 분석을 제시한다. 제안된 방법은 고전적인 점근 결과와 일치하며, 원하는 오차 한계를 보장하기 위해 얼마나 많은 데이터가 필요한지 보여준다. 이는 관련 유한 샘플 분석을 일반화하고 SIMs의 여러 변형에 널리 적용될 수 있다.

## 🎯 주요 포인트

- 1. 다변량 시스템에 대한 간단한 모수화와 강력한 수치적 특성으로 알려진 부공간 식별 방법(SIMs)에 대한 통계적 분석이 필요하다.

- 2. 최근 ARX 모델의 분석을 활용하여 ARX 모델의 은행에서 구성된 Hankel과 유사한 행렬에 대한 연합 오차 한계를 얻는다.

- 3. 가중 특이값 분해(SVD)를 통한 모델 축소를 통해 확장된 제어 가능성 및 관측 가능성 행렬에 대한 오차 한계를 얻는다.

---

*Generated on 2025-09-18 17:25:32*