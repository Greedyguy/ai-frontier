---
keywords:
  - Optimization
  - Large Margin Distribution Machine
  - Low-Rank Decomposition
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14577
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:23:11.707325",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Optimization",
    "Large Margin Distribution Machine",
    "Low-Rank Decomposition"
  ],
  "rejected_keywords": [
    "High-Order Tensor Data",
    "Tucker Decomposition"
  ],
  "similarity_scores": {
    "Optimization": 0.79,
    "Large Margin Distribution Machine": 0.78,
    "Low-Rank Decomposition": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Structure-Preserving Margin Distribution Learning for High-Order Tensor Data with Low-Rank Decomposition

**Korean Title:** 고차원 텐서 데이터의 저순위 분해를 통한 구조 보존 마진 분포 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|Alternating Optimization]]
**🔗 Specific Connectable**: [[keywords/Low-Rank Decomposition|Low-Rank Decomposition]]
**⚡ Unique Technical**: [[keywords/Large Margin Distribution Machine|Large Margin Distribution Machine]]

## 🔗 유사한 논문
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (77.3% similar)
- [[SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (76.9% similar)
- [[Taylor-Series_Expanded_Kolmogorov-Arnold_Network_for_Medical_Imaging_Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (76.5% similar)
- [[Superpose_Task-specific_Features_for_Model_Merging_20250919|Superpose Task-specific Features for Model Merging]] (76.5% similar)
- [[Data-Driven_Distributed_Optimization_via_Aggregative_Tracking_and_Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (76.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14577v1 Announce Type: new 
Abstract: The Large Margin Distribution Machine (LMDM) is a recent advancement in classifier design that optimizes not just the minimum margin (as in SVM) but the entire margin distribution, thereby improving generalization. However, existing LMDM formulations are limited to vectorized inputs and struggle with high-dimensional tensor data due to the need for flattening, which destroys the data's inherent multi-mode structure and increases computational burden. In this paper, we propose a Structure-Preserving Margin Distribution Learning for High-Order Tensor Data with Low-Rank Decomposition (SPMD-LRT) that operates directly on tensor representations without vectorization. The SPMD-LRT preserves multi-dimensional spatial structure by incorporating first-order and second-order tensor statistics (margin mean and variance) into the objective, and it leverages low-rank tensor decomposition techniques including rank-1(CP), higher-rank CP, and Tucker decomposition to parameterize the weight tensor. An alternating optimization (double-gradient descent) algorithm is developed to efficiently solve the SPMD-LRT, iteratively updating factor matrices and core tensor. This approach enables SPMD-LRT to maintain the structural information of high-order data while optimizing margin distribution for improved classification. Extensive experiments on diverse datasets (including MNIST, images and fMRI neuroimaging) demonstrate that SPMD-LRT achieves superior classification accuracy compared to conventional SVM, vector-based LMDM, and prior tensor-based SVM extensions (Support Tensor Machines and Support Tucker Machines). Notably, SPMD-LRT with Tucker decomposition attains the highest accuracy, highlighting the benefit of structure preservation. These results confirm the effectiveness and robustness of SPMD-LRT in handling high-dimensional tensor data for classification.

## 🔍 Abstract (한글 번역)

arXiv:2509.14577v1 발표 유형: 신규  
초록: 대형 마진 분포 기계(LMDM)는 최근 분류기 설계에서의 발전으로, 최소 마진(SVM에서처럼)뿐만 아니라 전체 마진 분포를 최적화하여 일반화를 개선하는 방법입니다. 그러나 기존의 LMDM 공식은 벡터화된 입력에만 제한되며, 고차원 텐서 데이터에 대해서는 평탄화가 필요하여 데이터의 고유한 다중 모드 구조를 파괴하고 계산 부담을 증가시킵니다. 본 논문에서는 벡터화 없이 텐서 표현에서 직접 작동하는 고차원 텐서 데이터를 위한 구조 보존 마진 분포 학습(SPMD-LRT)을 제안합니다. SPMD-LRT는 목적 함수에 1차 및 2차 텐서 통계(마진 평균 및 분산)를 포함하여 다차원 공간 구조를 보존하며, 랭크-1(CP), 고차원 CP, 터커 분해를 포함한 저랭크 텐서 분해 기법을 활용하여 가중치 텐서를 매개변수화합니다. 교대 최적화(이중 경사 하강) 알고리즘이 개발되어 SPMD-LRT를 효율적으로 해결하며, 요소 행렬과 코어 텐서를 반복적으로 업데이트합니다. 이 접근 방식은 SPMD-LRT가 고차원 데이터의 구조적 정보를 유지하면서 마진 분포를 최적화하여 분류 성능을 향상시킬 수 있게 합니다. 다양한 데이터셋(MNIST, 이미지 및 fMRI 신경영상 포함)에 대한 광범위한 실험 결과, SPMD-LRT는 기존 SVM, 벡터 기반 LMDM 및 이전의 텐서 기반 SVM 확장(서포트 텐서 머신 및 서포트 터커 머신)과 비교하여 우수한 분류 정확도를 달성했습니다. 특히, 터커 분해를 사용한 SPMD-LRT는 가장 높은 정확도를 달성하여 구조 보존의 이점을 강조합니다. 이러한 결과는 SPMD-LRT가 고차원 텐서 데이터를 분류하는 데 있어 효과적이고 견고함을 확인시켜 줍니다.

## 📝 요약

이 논문은 고차원 텐서 데이터를 다루는 새로운 분류기 설계법인 구조 보존 마진 분포 학습(SPMD-LRT)을 제안합니다. 기존의 대형 마진 분포 기계(LMDM)는 벡터화된 입력에 한정되어 고차원 텐서 데이터 처리에 한계가 있었으나, SPMD-LRT는 벡터화 없이 텐서 표현을 직접 활용합니다. 이 방법은 텐서의 다차원 구조를 보존하며, 저랭크 텐서 분해 기법을 사용하여 마진 분포를 최적화합니다. 제안된 알고리즘은 다양한 데이터셋에서 기존 방법들보다 우수한 분류 정확도를 보였으며, 특히 Tucker 분해를 사용한 경우 가장 높은 정확도를 기록했습니다. 이는 구조 보존의 이점을 강조하며, SPMD-LRT의 효과성과 강건함을 입증합니다.

## 🎯 주요 포인트

- 1. Large Margin Distribution Machine (LMDM)은 최소 마진뿐만 아니라 전체 마진 분포를 최적화하여 일반화를 개선합니다.

- 2. 기존 LMDM은 벡터화된 입력에 국한되어 고차원 텐서 데이터 처리에 어려움을 겪습니다.

- 3. 제안된 SPMD-LRT는 벡터화를 피하고 텐서 표현을 직접 다루어 다차원 공간 구조를 보존합니다.

- 4. SPMD-LRT는 저랭크 텐서 분해 기법을 활용하여 고차원 데이터의 구조 정보를 유지하면서 마진 분포를 최적화합니다.

- 5. 다양한 데이터셋 실험 결과, SPMD-LRT는 기존 SVM 및 텐서 기반 SVM 확장보다 우수한 분류 정확도를 달성합니다.

---

*Generated on 2025-09-19 15:25:12*