---
keywords:
  - Adversarial Graph Fusion
  - Tensorial Imputation
  - Graph-based Multi-view Learning
  - Low-rank Tensor Learning
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15955
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:39:31.827770",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Adversarial Graph Fusion",
    "Tensorial Imputation",
    "Graph-based Multi-view Learning",
    "Low-rank Tensor Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Adversarial Graph Fusion": 0.78,
    "Tensorial Imputation": 0.75,
    "Graph-based Multi-view Learning": 0.8,
    "Low-rank Tensor Learning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Adversarial Graph Fusion",
        "canonical": "Adversarial Graph Fusion",
        "aliases": [
          "AGF"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, crucial for understanding the proposed solution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Tensorial Imputation",
        "canonical": "Tensorial Imputation",
        "aliases": [
          "TI"
        ],
        "category": "unique_technical",
        "rationale": "A key component of the proposed method, essential for linking to tensor-based techniques.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Graph-based Multi-view Learning",
        "canonical": "Graph-based Multi-view Learning",
        "aliases": [
          "Multi-view Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's context, linking it to multi-view and graph learning literature.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Low-rank Tensor Learning",
        "canonical": "Low-rank Tensor Learning",
        "aliases": [
          "Tensor Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to tensor decomposition techniques widely used in machine learning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
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
      "candidate_surface": "Adversarial Graph Fusion",
      "resolved_canonical": "Adversarial Graph Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Tensorial Imputation",
      "resolved_canonical": "Tensorial Imputation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Graph-based Multi-view Learning",
      "resolved_canonical": "Graph-based Multi-view Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Low-rank Tensor Learning",
      "resolved_canonical": "Low-rank Tensor Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Adversarial Graph Fusion for Incomplete Multi-view Semi-supervised Learning with Tensorial Imputation

**Korean Title:** 불완전한 다중 뷰 반지도 학습을 위한 적대적 그래프 융합과 텐서 보간법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15955.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15955](https://arxiv.org/abs/2509.15955)

## 🔗 유사한 논문
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (81.7% similar)
- [[2025-09-18/Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation: A Robustness Analysis]] (81.3% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (81.2% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (81.1% similar)
- [[2025-09-22/Deep Reinforcement Learning with Gradient Eligibility Traces_20250922|Deep Reinforcement Learning with Gradient Eligibility Traces]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph-based Multi-view Learning|Graph-based Multi-view Learning]], [[keywords/Low-rank Tensor Learning|Low-rank Tensor Learning]]
**⚡ Unique Technical**: [[keywords/Adversarial Graph Fusion|Adversarial Graph Fusion]], [[keywords/Tensorial Imputation|Tensorial Imputation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15955v1 Announce Type: new 
Abstract: View missing remains a significant challenge in graph-based multi-view semi-supervised learning, hindering their real-world applications. To address this issue, traditional methods introduce a missing indicator matrix and focus on mining partial structure among existing samples in each view for label propagation (LP). However, we argue that these disregarded missing samples sometimes induce discontinuous local structures, i.e., sub-clusters, breaking the fundamental smoothness assumption in LP. Consequently, such a Sub-Cluster Problem (SCP) would distort graph fusion and degrade classification performance. To alleviate SCP, we propose a novel incomplete multi-view semi-supervised learning method, termed AGF-TI. Firstly, we design an adversarial graph fusion scheme to learn a robust consensus graph against the distorted local structure through a min-max framework. By stacking all similarity matrices into a tensor, we further recover the incomplete structure from the high-order consistency information based on the low-rank tensor learning. Additionally, the anchor-based strategy is incorporated to reduce the computational complexity. An efficient alternative optimization algorithm combining a reduced gradient descent method is developed to solve the formulated objective, with theoretical convergence. Extensive experimental results on various datasets validate the superiority of our proposed AGF-TI as compared to state-of-the-art methods. Code is available at https://github.com/ZhangqiJiang07/AGF_TI.

## 🔍 Abstract (한글 번역)

arXiv:2509.15955v1 발표 유형: 신규  
초록: 뷰 손실은 그래프 기반 다중 뷰 반지도 학습에서 중요한 도전 과제로 남아 있으며, 이는 실제 응용을 방해합니다. 이 문제를 해결하기 위해 전통적인 방법들은 손실 지표 행렬을 도입하고, 각 뷰에서 존재하는 샘플 간의 부분 구조를 탐색하여 레이블 전파(LP)를 수행하는 데 중점을 둡니다. 그러나 우리는 이러한 무시된 손실 샘플들이 때때로 불연속적인 지역 구조, 즉 하위 클러스터를 유도하여 LP의 기본적인 평활성 가정을 깨뜨린다고 주장합니다. 결과적으로 이러한 하위 클러스터 문제(SCP)는 그래프 융합을 왜곡하고 분류 성능을 저하시킵니다. SCP를 완화하기 위해, 우리는 AGF-TI라는 새로운 불완전 다중 뷰 반지도 학습 방법을 제안합니다. 먼저, 왜곡된 지역 구조에 대항하여 강력한 합의 그래프를 학습하기 위해 적대적 그래프 융합 방식을 설계하였습니다. 모든 유사성 행렬을 텐서로 쌓아, 저차 텐서 학습에 기반하여 고차 일관성 정보를 통해 불완전한 구조를 복원합니다. 추가로, 앵커 기반 전략을 도입하여 계산 복잡성을 줄였습니다. 이론적 수렴성을 갖춘 감소된 경사 하강법을 결합한 효율적인 대안 최적화 알고리즘을 개발하여 수립된 목표를 해결합니다. 다양한 데이터셋에 대한 광범위한 실험 결과는 최신 방법들과 비교하여 제안한 AGF-TI의 우수성을 입증합니다. 코드는 https://github.com/ZhangqiJiang07/AGF_TI에서 이용 가능합니다.

## 📝 요약

이 논문은 그래프 기반 다중 뷰 반지도 학습에서 발생하는 뷰 누락 문제를 해결하기 위해 새로운 방법론인 AGF-TI를 제안합니다. 기존 방법론은 누락된 샘플로 인해 발생하는 불연속적인 지역 구조 문제(SCP)를 간과하여 성능 저하를 초래할 수 있습니다. AGF-TI는 적대적 그래프 융합 방식을 통해 왜곡된 지역 구조에 강인한 합의 그래프를 학습하고, 저차원 텐서 학습을 통해 불완전한 구조를 복구합니다. 또한, 앵커 기반 전략을 도입하여 계산 복잡성을 줄입니다. 다양한 데이터셋에서의 실험 결과, AGF-TI가 기존 최첨단 방법들보다 우수한 성능을 보임을 확인했습니다.

## 🎯 주요 포인트

- 1. 그래프 기반 다중 뷰 반지도 학습에서 누락된 뷰 문제는 실제 응용을 방해하는 주요 과제입니다.
- 2. 기존 방법들은 누락 지표 행렬을 도입하여 각 뷰의 기존 샘플 간 부분 구조를 탐색하지만, 이는 종종 불연속적인 지역 구조를 유발합니다.
- 3. 제안된 AGF-TI 방법은 왜곡된 지역 구조에 대한 강력한 합의 그래프를 학습하기 위해 적대적 그래프 융합 방식을 사용합니다.
- 4. 저차원 텐서 학습을 기반으로 높은 차수의 일관성 정보를 통해 불완전한 구조를 복구합니다.
- 5. 다양한 데이터셋에 대한 실험 결과, AGF-TI가 최신 방법들보다 우수한 성능을 보임을 확인했습니다.


---

*Generated on 2025-09-23 10:39:31*