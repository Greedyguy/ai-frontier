---
keywords:
  - Neural Network
  - Semantic Inference
  - Discriminative Capability Score
  - Model Pruning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2310.01259
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:37:51.878711",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Semantic Inference",
    "Discriminative Capability Score",
    "Model Pruning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Semantic Inference": 0.8,
    "Discriminative Capability Score": 0.79,
    "Model Pruning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "DNN"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are central to the paper's methodology and link to broader machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semantic Inference",
        "canonical": "Semantic Inference",
        "aliases": [
          "SINF"
        ],
        "category": "unique_technical",
        "rationale": "Semantic Inference is a novel approach introduced in the paper, providing a unique linking point.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Discriminative Capability Score",
        "canonical": "Discriminative Capability Score",
        "aliases": [
          "DCS"
        ],
        "category": "unique_technical",
        "rationale": "DCS is a specific metric introduced in the paper, offering a unique technical concept for linking.",
        "novelty_score": 0.89,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Pruning Approaches",
        "canonical": "Model Pruning",
        "aliases": [
          "Pruning Techniques"
        ],
        "category": "specific_connectable",
        "rationale": "Model pruning is a well-known technique in neural networks, enhancing connectivity with existing literature.",
        "novelty_score": 0.55,
        "connectivity_score": 0.84,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "evaluation",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semantic Inference",
      "resolved_canonical": "Semantic Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Discriminative Capability Score",
      "resolved_canonical": "Discriminative Capability Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.89,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Pruning Approaches",
      "resolved_canonical": "Model Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.84,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SINF: Semantic Neural Network Inference with Semantic Subgraphs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2310.01259.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2310.01259](https://arxiv.org/abs/2310.01259)

## 🔗 유사한 논문
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (82.0% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (80.7% similar)
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (80.3% similar)
- [[2025-09-22/SegDINO3D_ 3D Instance Segmentation Empowered by Both Image-Level and Object-Level 2D Features_20250922|SegDINO3D: 3D Instance Segmentation Empowered by Both Image-Level and Object-Level 2D Features]] (80.0% similar)
- [[2025-09-23/A study on Deep Convolutional Neural Networks, transfer learning, and Mnet model for Cervical Cancer Detection_20250923|A study on Deep Convolutional Neural Networks, transfer learning, and Mnet model for Cervical Cancer Detection]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Model Pruning|Model Pruning]]
**⚡ Unique Technical**: [[keywords/Semantic Inference|Semantic Inference]], [[keywords/Discriminative Capability Score|Discriminative Capability Score]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2310.01259v3 Announce Type: replace-cross 
Abstract: This paper proposes Semantic Inference (SINF) that creates semantic subgraphs in a Deep Neural Network(DNN) based on a new Discriminative Capability Score (DCS) to drastically reduce the DNN computational load with limited performance loss.~We evaluate the performance SINF on VGG16, VGG19, and ResNet50 DNNs trained on CIFAR100 and a subset of the ImageNet dataset. Moreover, we compare its performance against 6 state-of-the-art pruning approaches. Our results show that (i) on average, SINF reduces the inference time of VGG16, VGG19, and ResNet50 respectively by up to 29%, 35%, and 15% with only 3.75%, 0.17%, and 6.75% accuracy loss for CIFAR100 while for ImageNet benchmark, the reduction in inference time is 18%, 22%, and 9% for accuracy drop of 3%, 2.5%, and 6%; (ii) DCS achieves respectively up to 3.65%, 4.25%, and 2.36% better accuracy with VGG16, VGG19, and ResNet50 with respect to existing discriminative scores for CIFAR100 and the same for ImageNet is 8.9%, 5.8%, and 5.2% respectively. Through experimental evaluation on Raspberry Pi and NVIDIA Jetson Nano, we show SINF is about 51% and 38% more energy efficient and takes about 25% and 17% less inference time than the base model for CIFAR100 and ImageNet.

## 📝 요약

이 논문은 새로운 판별 능력 점수(DCS)를 기반으로 심층 신경망(DNN)에서 의미론적 부분 그래프를 생성하는 Semantic Inference(SINF)를 제안하여 DNN의 계산 부하를 크게 줄이면서 성능 손실을 최소화합니다. VGG16, VGG19, ResNet50 모델을 CIFAR100 및 ImageNet 데이터셋에서 평가한 결과, SINF는 평균적으로 추론 시간을 최대 29%, 35%, 15%까지 줄이면서도 CIFAR100에서 각각 3.75%, 0.17%, 6.75%의 정확도 손실만 발생시켰습니다. ImageNet에서는 추론 시간이 18%, 22%, 9% 감소하고 정확도 손실은 각각 3%, 2.5%, 6%였습니다. 또한 DCS는 기존의 판별 점수에 비해 CIFAR100에서 VGG16, VGG19, ResNet50 모델의 정확도를 각각 최대 3.65%, 4.25%, 2.36% 향상시켰으며, ImageNet에서는 각각 8.9%, 5.8%, 5.2% 향상시켰습니다. Raspberry Pi와 NVIDIA Jetson Nano에서의 실험 결과, SINF는 에너지 효율성이 약 51%, 38% 더 높고, 추론 시간이 각각 25%, 17% 더 짧았습니다.

## 🎯 주요 포인트

- 1. Semantic Inference(SINF)는 새로운 Discriminative Capability Score(DCS)를 기반으로 DNN의 계산 부하를 크게 줄이면서 성능 손실을 최소화하는 방법을 제안합니다.
- 2. SINF는 VGG16, VGG19, ResNet50에서 CIFAR100과 ImageNet 데이터셋을 사용하여 평균적으로 최대 35%의 추론 시간 단축을 이루었으며, 성능 손실은 6.75% 이하로 유지되었습니다.
- 3. DCS는 기존의 판별 점수와 비교하여 CIFAR100에서 최대 4.25% 더 나은 정확도를, ImageNet에서 최대 8.9% 더 나은 정확도를 달성했습니다.
- 4. Raspberry Pi와 NVIDIA Jetson Nano에서의 실험 결과, SINF는 각각 51%와 38% 더 에너지 효율적이며, 추론 시간은 25%와 17% 더 단축되었습니다.


---

*Generated on 2025-09-24 00:37:51*