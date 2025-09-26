---
keywords:
  - Class Incremental Learning
  - Pre-trained Models
  - Mixture of Noise
  - Information Theory
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16738
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:14:53.848116",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Class Incremental Learning",
    "Pre-trained Models",
    "Mixture of Noise",
    "Information Theory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Class Incremental Learning": 0.8,
    "Pre-trained Models": 0.7,
    "Mixture of Noise": 0.85,
    "Information Theory": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Class Incremental Learning",
        "canonical": "Class Incremental Learning",
        "aliases": [
          "CIL"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's focus on learning new categories while retaining old knowledge, which is crucial for linking related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pre-trained Models",
        "canonical": "Pre-trained Models",
        "aliases": [
          "PTMs"
        ],
        "category": "broad_technical",
        "rationale": "Pre-trained models are a foundational concept in the paper, providing a basis for understanding the proposed method.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Mixture of Noise",
        "canonical": "Mixture of Noise",
        "aliases": [
          "Min"
        ],
        "category": "unique_technical",
        "rationale": "This is the novel method proposed by the authors, making it a unique concept for linking within the domain.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Information Theory",
        "canonical": "Information Theory",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Information theory is used to guide the learning of beneficial noise, linking it to a broader theoretical framework.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "parameter drift",
      "visual patterns"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Class Incremental Learning",
      "resolved_canonical": "Class Incremental Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pre-trained Models",
      "resolved_canonical": "Pre-trained Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Mixture of Noise",
      "resolved_canonical": "Mixture of Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Information Theory",
      "resolved_canonical": "Information Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Min: Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16738.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16738](https://arxiv.org/abs/2509.16738)

## 🔗 유사한 논문
- [[2025-09-23/Intra-Cluster Mixup_ An Effective Data Augmentation Technique for Complementary-Label Learning_20250923|Intra-Cluster Mixup: An Effective Data Augmentation Technique for Complementary-Label Learning]] (84.5% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (83.1% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (82.8% similar)
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (81.6% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Pre-trained Models|Pre-trained Models]]
**🔗 Specific Connectable**: [[keywords/Information Theory|Information Theory]]
**⚡ Unique Technical**: [[keywords/Class Incremental Learning|Class Incremental Learning]], [[keywords/Mixture of Noise|Mixture of Noise]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16738v1 Announce Type: cross 
Abstract: Class Incremental Learning (CIL) aims to continuously learn new categories while retaining the knowledge of old ones. Pre-trained models (PTMs) show promising capabilities in CIL. However, existing approaches that apply lightweight fine-tuning to backbones still induce parameter drift, thereby compromising the generalization capability of pre-trained models. Parameter drift can be conceptualized as a form of noise that obscures critical patterns learned for previous tasks. However, recent researches have shown that noise is not always harmful. For example, the large number of visual patterns learned from pre-training can be easily abused by a single task, and introducing appropriate noise can suppress some low-correlation features, thus leaving a margin for future tasks. To this end, we propose learning beneficial noise for CIL guided by information theory and propose Mixture of Noise (Min), aiming to mitigate the degradation of backbone generalization from adapting new tasks. Specifically, task-specific noise is learned from high-dimension features of new tasks. Then, a set of weights is adjusted dynamically for optimal mixture of different task noise. Finally, Min embeds the beneficial noise into the intermediate features to mask the response of inefficient patterns. Extensive experiments on six benchmark datasets demonstrate that Min achieves state-of-the-art performance in most incremental settings, with particularly outstanding results in 50-steps incremental settings. This shows the significant potential for beneficial noise in continual learning.

## 📝 요약

이 논문은 클래스 증분 학습(CIL)에서 사전 학습된 모델(PTM)의 일반화 능력을 저하시키는 파라미터 드리프트 문제를 해결하기 위해 정보 이론에 기반한 유익한 노이즈 학습 방법인 Mixture of Noise (Min)을 제안합니다. Min은 새로운 작업의 고차원 특징에서 작업별 노이즈를 학습하고, 다양한 작업 노이즈의 최적 혼합을 위해 가중치를 동적으로 조정합니다. 이를 통해 비효율적인 패턴의 반응을 억제하여 백본의 일반화 성능 저하를 완화합니다. 여섯 개의 벤치마크 데이터셋에서 수행한 실험 결과, Min은 대부분의 증분 설정에서 최첨단 성능을 달성하며, 특히 50단계 증분 설정에서 뛰어난 성과를 보였습니다. 이는 지속 학습에서 유익한 노이즈의 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. 클래스 증분 학습(CIL)은 새로운 범주를 지속적으로 학습하면서 기존 지식을 유지하는 것을 목표로 한다.
- 2. 사전 학습된 모델(PTM)은 CIL에서 유망한 성능을 보이지만, 경량화된 미세 조정이 파라미터 드리프트를 유발하여 일반화 능력을 저하시킨다.
- 3. 정보 이론을 기반으로 CIL에 유익한 노이즈를 학습하는 Mixture of Noise(Min) 방법을 제안하여 새로운 작업 적응 시 백본의 일반화 저하를 완화한다.
- 4. Min은 새로운 작업의 고차원 특징에서 작업별 노이즈를 학습하고, 다양한 작업 노이즈의 최적 혼합을 위해 가중치를 동적으로 조정한다.
- 5. 여섯 개의 벤치마크 데이터셋에 대한 실험 결과, Min은 대부분의 증분 설정에서 최첨단 성능을 달성하며, 특히 50단계 증분 설정에서 뛰어난 결과를 보인다.


---

*Generated on 2025-09-24 02:14:53*