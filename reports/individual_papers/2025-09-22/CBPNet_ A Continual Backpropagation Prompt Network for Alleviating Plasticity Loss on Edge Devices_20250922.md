---
keywords:
  - CBPNet
  - Plasticity Loss
  - Edge Devices
  - Catastrophic Forgetting
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15785
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:13:14.240671",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "CBPNet",
    "Plasticity Loss",
    "Edge Devices",
    "Catastrophic Forgetting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "CBPNet": 0.78,
    "Plasticity Loss": 0.82,
    "Edge Devices": 0.75,
    "Catastrophic Forgetting": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Continual Backpropagation Prompt Network",
        "canonical": "CBPNet",
        "aliases": [
          "Continual Backpropagation Prompt Network"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel framework specifically designed to address plasticity loss in edge devices.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "plasticity loss",
        "canonical": "Plasticity Loss",
        "aliases": [
          "plasticity decay"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept in continual learning that affects model performance, relevant for linking to other works on model adaptability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "edge devices",
        "canonical": "Edge Devices",
        "aliases": [
          "IoT devices",
          "embedded systems"
        ],
        "category": "broad_technical",
        "rationale": "Common context for deploying machine learning models, useful for linking to discussions on resource constraints.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "catastrophic forgetting",
        "canonical": "Catastrophic Forgetting",
        "aliases": [
          "forgetting in neural networks"
        ],
        "category": "specific_connectable",
        "rationale": "Central issue in continual learning, providing strong links to research on memory retention in neural networks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Continual Backpropagation Prompt Network",
      "resolved_canonical": "CBPNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "plasticity loss",
      "resolved_canonical": "Plasticity Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "edge devices",
      "resolved_canonical": "Edge Devices",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "catastrophic forgetting",
      "resolved_canonical": "Catastrophic Forgetting",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# CBPNet: A Continual Backpropagation Prompt Network for Alleviating Plasticity Loss on Edge Devices

**Korean Title:** CBPNet: 엣지 디바이스에서 가소성 손실을 완화하기 위한 지속적 역전파 프롬프트 네트워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15785.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15785](https://arxiv.org/abs/2509.15785)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.9% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (81.5% similar)
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (81.5% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (81.3% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO: Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Edge Devices|Edge Devices]]
**🔗 Specific Connectable**: [[keywords/Plasticity Loss|Plasticity Loss]], [[keywords/Catastrophic Forgetting|Catastrophic Forgetting]]
**⚡ Unique Technical**: [[keywords/CBPNet|CBPNet]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15785v1 Announce Type: cross 
Abstract: To meet the demands of applications like robotics and autonomous driving that require real-time responses to dynamic environments, efficient continual learning methods suitable for edge devices have attracted increasing attention. In this transition, using frozen pretrained models with prompts has become a mainstream strategy to combat catastrophic forgetting. However, this approach introduces a new critical bottleneck: plasticity loss, where the model's ability to learn new knowledge diminishes due to the frozen backbone and the limited capacity of prompt parameters. We argue that the reduction in plasticity stems from a lack of update vitality in underutilized parameters during the training process. To this end, we propose the Continual Backpropagation Prompt Network (CBPNet), an effective and parameter efficient framework designed to restore the model's learning vitality. We innovatively integrate an Efficient CBP Block that counteracts plasticity decay by adaptively reinitializing these underutilized parameters. Experimental results on edge devices demonstrate CBPNet's effectiveness across multiple benchmarks. On Split CIFAR-100, it improves average accuracy by over 1% against a strong baseline, and on the more challenging Split ImageNet-R, it achieves a state of the art accuracy of 69.41%. This is accomplished by training additional parameters that constitute less than 0.2% of the backbone's size, validating our approach.

## 🔍 Abstract (한글 번역)

arXiv:2509.15785v1 발표 유형: 교차  
초록: 로봇공학 및 자율 주행과 같이 동적 환경에 대한 실시간 응답을 요구하는 애플리케이션의 수요를 충족하기 위해, 엣지 장치에 적합한 효율적인 지속 학습 방법이 점점 더 많은 주목을 받고 있습니다. 이 전환 과정에서, 프롬프트와 함께 고정된 사전 학습 모델을 사용하는 것이 망각 방지의 주류 전략으로 자리 잡았습니다. 그러나 이 접근법은 모델의 새로운 지식을 학습하는 능력이 고정된 백본과 제한된 프롬프트 매개변수 용량으로 인해 감소하는 가소성 손실이라는 새로운 중요한 병목 현상을 초래합니다. 우리는 가소성 감소가 훈련 과정에서 활용되지 않은 매개변수의 업데이트 활력 부족에서 비롯된다고 주장합니다. 이를 위해, 우리는 모델의 학습 활력을 회복하도록 설계된 효과적이고 매개변수 효율적인 프레임워크인 지속 역전파 프롬프트 네트워크(CBPNet)를 제안합니다. 우리는 비효율적으로 사용된 매개변수를 적응적으로 재초기화하여 가소성 감소를 방지하는 효율적인 CBP 블록을 혁신적으로 통합합니다. 엣지 장치에서의 실험 결과는 여러 벤치마크에서 CBPNet의 효과를 입증합니다. Split CIFAR-100에서는 강력한 기준선에 비해 평균 정확도가 1% 이상 향상되었으며, 더 도전적인 Split ImageNet-R에서는 69.41%의 최첨단 정확도를 달성했습니다. 이는 백본 크기의 0.2% 미만을 차지하는 추가 매개변수를 훈련하여 이루어졌으며, 우리의 접근법을 검증합니다.

## 📝 요약

이 논문은 로봇공학 및 자율주행과 같은 실시간 응답이 필요한 응용 분야를 위해 엣지 디바이스에 적합한 효율적인 지속 학습 방법을 제안합니다. 기존의 프리트레인 모델을 사용한 방법은 망각 문제를 해결하지만, 가동성 손실이라는 새로운 문제를 야기합니다. 이를 해결하기 위해, 저자들은 Continual Backpropagation Prompt Network (CBPNet)를 제안하여 모델의 학습 활력을 회복시키고자 합니다. CBPNet은 비효율적으로 사용되는 파라미터를 재초기화하는 Efficient CBP Block을 통합하여 가동성 감소를 방지합니다. 실험 결과, CBPNet은 Split CIFAR-100에서 평균 정확도를 1% 이상 향상시키고, Split ImageNet-R에서 69.41%의 최첨단 정확도를 달성했습니다. 추가로 학습된 파라미터는 백본 크기의 0.2% 미만으로, 제안된 접근법의 효율성을 입증합니다.

## 🎯 주요 포인트

- 1. 로봇 공학 및 자율 주행과 같은 실시간 응답이 필요한 응용 분야를 위해 엣지 디바이스에 적합한 효율적인 지속 학습 방법이 주목받고 있습니다.
- 2. 프롬프트를 사용하는 고정된 사전 학습 모델은 망각 문제를 해결하지만, 플라스틱성 손실이라는 새로운 병목 현상을 초래합니다.
- 3. 플라스틱성 감소는 훈련 과정에서 저활용된 매개변수의 업데이트 활력 부족에서 비롯된다고 주장합니다.
- 4. Continual Backpropagation Prompt Network (CBPNet)는 모델의 학습 활력을 복원하기 위해 설계된 효과적이고 매개변수 효율적인 프레임워크입니다.
- 5. CBPNet는 Split CIFAR-100 및 Split ImageNet-R에서 강력한 성능을 보이며, 백본 크기의 0.2% 미만의 추가 매개변수만을 훈련하여 성과를 입증합니다.


---

*Generated on 2025-09-23 09:13:14*