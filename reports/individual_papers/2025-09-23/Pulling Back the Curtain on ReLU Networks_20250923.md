---
keywords:
  - Neural Network
  - Excitation Pullbacks
  - Path Stability Hypothesis
  - Batch Normalization
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2507.22832
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:48:42.276596",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Excitation Pullbacks",
    "Path Stability Hypothesis",
    "Batch Normalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.8,
    "Excitation Pullbacks": 0.78,
    "Path Stability Hypothesis": 0.75,
    "Batch Normalization": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ReLU Networks",
        "canonical": "Neural Network",
        "aliases": [
          "Rectified Linear Unit Networks"
        ],
        "category": "broad_technical",
        "rationale": "ReLU Networks are a fundamental component of many neural network architectures, providing a strong link to general neural network discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "excitation pullbacks",
        "canonical": "Excitation Pullbacks",
        "aliases": [
          "modified gradients"
        ],
        "category": "unique_technical",
        "rationale": "This novel concept introduced in the paper provides a new perspective on gradient alignment and interpretability in neural networks.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "path stability hypothesis",
        "canonical": "Path Stability Hypothesis",
        "aliases": [
          "binary activation pattern stability"
        ],
        "category": "unique_technical",
        "rationale": "The hypothesis offers a theoretical framework that could link to discussions on neural network training dynamics.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Batch Normalization",
        "canonical": "Batch Normalization",
        "aliases": [
          "BN"
        ],
        "category": "specific_connectable",
        "rationale": "Batch Normalization is a widely used technique in deep learning, providing a strong connection to discussions on network training and generalization.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "piecewise affine",
      "intrinsic noise",
      "soft gating"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ReLU Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "excitation pullbacks",
      "resolved_canonical": "Excitation Pullbacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "path stability hypothesis",
      "resolved_canonical": "Path Stability Hypothesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Batch Normalization",
      "resolved_canonical": "Batch Normalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Pulling Back the Curtain on ReLU Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.22832.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2507.22832](https://arxiv.org/abs/2507.22832)

## 🔗 유사한 논문
- [[2025-09-17/Circuit realization and hardware linearization of monotone operator equilibrium networks_20250917|Circuit realization and hardware linearization of monotone operator equilibrium networks]] (83.2% similar)
- [[2025-09-23/Checking extracted rules in Neural Networks_20250923|Checking extracted rules in Neural Networks]] (82.7% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (82.1% similar)
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (82.0% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Batch Normalization|Batch Normalization]]
**⚡ Unique Technical**: [[keywords/Excitation Pullbacks|Excitation Pullbacks]], [[keywords/Path Stability Hypothesis|Path Stability Hypothesis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.22832v4 Announce Type: replace 
Abstract: Since any ReLU network is piecewise affine, its hidden units can be characterized by their pullbacks through the active subnetwork, i.e., by their gradients (up to bias terms). However, gradients of deeper neurons are notoriously misaligned, which obscures the network's internal representations. We posit that models do align gradients with data, yet this is concealed by the intrinsic noise of the ReLU hard gating. We validate this intuition by applying soft gating in the backward pass only, reducing the local impact of weakly excited neurons. The resulting modified gradients, which we call "excitation pullbacks", exhibit striking perceptual alignment on a number of ImageNet-pretrained architectures, while the rudimentary pixel-space gradient ascent quickly produces easily interpretable input- and target-specific features. Inspired by these findings, we formulate the "path stability" hypothesis, claiming that the binary activation patterns largely stabilize during training and get encoded in the pre-activation distribution of the final model. When true, excitation pullbacks become aligned with the gradients of a kernel machine that mainly determines the network's decision. This provides a theoretical justification for the apparent faithfulness of the feature attributions based on excitation pullbacks, potentially even leading to mechanistic interpretability of deep models. Incidentally, we give a possible explanation for the effectiveness of Batch Normalization and Deep Features, together with a novel perspective on the network's internal memory and generalization properties. We release the code and an interactive app for easier exploration of the excitation pullbacks.

## 📝 요약

이 논문은 ReLU 네트워크의 내부 표현을 이해하기 위해 "excitation pullbacks"라는 수정된 그래디언트를 제안합니다. ReLU의 하드 게이팅으로 인해 깊은 층의 그래디언트가 잘못 정렬되는 문제를 해결하기 위해, 역전파 과정에서 소프트 게이팅을 적용하여 약하게 활성화된 뉴런의 영향을 줄였습니다. 이를 통해 ImageNet 사전 학습 모델에서 명확한 시각적 정렬을 확인했습니다. 또한, "경로 안정성" 가설을 제시하여 이진 활성화 패턴이 훈련 중 안정화되며, 최종 모델의 사전 활성화 분포에 인코딩된다고 주장합니다. 이 연구는 Batch Normalization과 딥 피처의 효과성을 설명하고, 네트워크의 내부 메모리 및 일반화 특성에 대한 새로운 관점을 제공합니다. 연구 결과를 탐색할 수 있는 코드와 인터랙티브 앱도 공개했습니다.

## 🎯 주요 포인트

- 1. ReLU 네트워크의 숨겨진 유닛은 활성 서브네트워크를 통한 풀백, 즉 기울기로 특징지어질 수 있습니다.
- 2. 깊은 신경망의 기울기는 잘못 정렬되는 경우가 많아 네트워크의 내부 표현을 모호하게 만듭니다.
- 3. 소프트 게이팅을 역전파에만 적용하여 약하게 활성화된 뉴런의 영향을 줄이고, "흥분 풀백"이라는 수정된 기울기를 통해 이미지넷 사전 학습 아키텍처에서 인지적 정렬을 확인했습니다.
- 4. "경로 안정성" 가설을 제안하여 이진 활성화 패턴이 훈련 중에 안정화되고 최종 모델의 사전 활성화 분포에 인코딩된다고 주장합니다.
- 5. 배치 정규화와 심층 특징의 효과성에 대한 설명을 제공하고, 네트워크의 내부 메모리 및 일반화 특성에 대한 새로운 관점을 제시합니다.


---

*Generated on 2025-09-24 02:48:42*