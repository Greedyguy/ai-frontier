---
keywords:
  - Complementary-Label Learning
  - Intra-Cluster Mixup
  - Mixup
  - Weakly-Supervised Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17971
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:14:37.753379",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Complementary-Label Learning",
    "Intra-Cluster Mixup",
    "Mixup",
    "Weakly-Supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Complementary-Label Learning": 0.78,
    "Intra-Cluster Mixup": 0.8,
    "Mixup": 0.75,
    "Weakly-Supervised Learning": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Complementary-Label Learning",
        "canonical": "Complementary-Label Learning",
        "aliases": [
          "CLL"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized form of weakly-supervised learning central to the paper's focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Intra-Cluster Mixup",
        "canonical": "Intra-Cluster Mixup",
        "aliases": [
          "ICM"
        ],
        "category": "unique_technical",
        "rationale": "A novel data augmentation technique proposed in the paper, crucial for enhancing CLL.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mixup",
        "canonical": "Mixup",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A widely-used data augmentation technique whose limitations in CLL are explored.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Weakly-Supervised Learning",
        "canonical": "Weakly-Supervised Learning",
        "aliases": [
          "WSL"
        ],
        "category": "broad_technical",
        "rationale": "Provides context for the type of learning under discussion, linking to broader ML concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "data augmentation",
      "performance improvements"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Complementary-Label Learning",
      "resolved_canonical": "Complementary-Label Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Intra-Cluster Mixup",
      "resolved_canonical": "Intra-Cluster Mixup",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mixup",
      "resolved_canonical": "Mixup",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Weakly-Supervised Learning",
      "resolved_canonical": "Weakly-Supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Intra-Cluster Mixup: An Effective Data Augmentation Technique for Complementary-Label Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17971.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17971](https://arxiv.org/abs/2509.17971)

## 🔗 유사한 논문
- [[2025-09-22/Disentangling Latent Shifts of In-Context Learning with Weak Supervision_20250922|Disentangling Latent Shifts of In-Context Learning with Weak Supervision]] (83.4% similar)
- [[2025-09-22/KITE_ Kernelized and Information Theoretic Exemplars for In-Context Learning_20250922|KITE: Kernelized and Information Theoretic Exemplars for In-Context Learning]] (82.4% similar)
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (82.2% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.8% similar)
- [[2025-09-22/PCSR_ Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning_20250922|PCSR: Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Weakly-Supervised Learning|Weakly-Supervised Learning]]
**🔗 Specific Connectable**: [[keywords/Mixup|Mixup]]
**⚡ Unique Technical**: [[keywords/Complementary-Label Learning|Complementary-Label Learning]], [[keywords/Intra-Cluster Mixup|Intra-Cluster Mixup]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17971v1 Announce Type: cross 
Abstract: In this paper, we investigate the challenges of complementary-label learning (CLL), a specialized form of weakly-supervised learning (WSL) where models are trained with labels indicating classes to which instances do not belong, rather than standard ordinary labels. This alternative supervision is appealing because collecting complementary labels is generally cheaper and less labor-intensive. Although most existing research in CLL emphasizes the development of novel loss functions, the potential of data augmentation in this domain remains largely underexplored. In this work, we uncover that the widely-used Mixup data augmentation technique is ineffective when directly applied to CLL. Through in-depth analysis, we identify that the complementary-label noise generated by Mixup negatively impacts the performance of CLL models. We then propose an improved technique called Intra-Cluster Mixup (ICM), which only synthesizes augmented data from nearby examples, to mitigate the noise effect. ICM carries the benefits of encouraging complementary label sharing of nearby examples, and leads to substantial performance improvements across synthetic and real-world labeled datasets. In particular, our wide spectrum of experimental results on both balanced and imbalanced CLL settings justifies the potential of ICM in allying with state-of-the-art CLL algorithms, achieving significant accuracy increases of 30% and 10% on MNIST and CIFAR datasets, respectively.

## 📝 요약

이 논문은 약한 지도 학습의 한 형태인 보완 레이블 학습(CLL)의 도전 과제를 다룹니다. CLL은 인스턴스가 속하지 않는 클래스를 나타내는 레이블로 모델을 학습시키며, 이는 일반적인 레이블 수집보다 비용이 적게 듭니다. 기존 연구는 주로 새로운 손실 함수 개발에 집중했지만, 데이터 증강의 잠재력은 충분히 탐구되지 않았습니다. 본 연구에서는 널리 사용되는 Mixup 데이터 증강 기법이 CLL에 직접 적용될 경우 효과적이지 않음을 발견했습니다. Mixup이 생성하는 보완 레이블 노이즈가 CLL 모델 성능에 부정적 영향을 미치기 때문입니다. 이를 해결하기 위해, 인접한 예제들로부터만 증강 데이터를 생성하는 Intra-Cluster Mixup(ICM) 기법을 제안했습니다. ICM은 인접 예제 간 보완 레이블 공유를 촉진하며, 다양한 데이터셋에서 성능을 크게 향상시켰습니다. 특히, MNIST와 CIFAR 데이터셋에서 각각 30%와 10%의 정확도 향상을 이루며, 최첨단 CLL 알고리즘과 결합할 가능성을 입증했습니다.

## 🎯 주요 포인트

- 1. 보조 라벨 학습(CLL)은 인스턴스가 속하지 않는 클래스를 나타내는 라벨로 모델을 훈련하는 약지도 학습의 한 형태이다.
- 2. Mixup 데이터 증강 기법은 CLL에 직접 적용할 경우 효과가 없으며, 보조 라벨 노이즈가 성능에 부정적인 영향을 미친다.
- 3. Intra-Cluster Mixup(ICM)은 인접한 예제들로부터만 증강 데이터를 생성하여 노이즈 효과를 완화하고 성능을 향상시킨다.
- 4. ICM은 인접한 예제들 간의 보조 라벨 공유를 촉진하여, 다양한 합성 및 실제 데이터셋에서 성능을 크게 개선한다.
- 5. MNIST와 CIFAR 데이터셋에서 ICM을 적용한 결과, 각각 30%와 10%의 정확도 향상을 달성하였다.


---

*Generated on 2025-09-24 00:14:37*