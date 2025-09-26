<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:07:25.159706",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Vision-Language Model",
    "Self-supervised Learning",
    "Pre-trained Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.9,
    "Vision-Language Model": 0.85,
    "Self-supervised Learning": 0.8,
    "Pre-trained Model": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot Image Classification",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Classification"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's approach and connects well with existing discussions on learning paradigms without labeled data.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are pivotal in the proposed framework, linking to multimodal learning discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Self-Learning Cycle",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-Learning"
        ],
        "category": "specific_connectable",
        "rationale": "The self-learning cycle is a key mechanism in the paper, aligning with self-supervised learning techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pre-trained Visual Model",
        "canonical": "Pre-trained Model",
        "aliases": [
          "Pre-trained Visual"
        ],
        "category": "broad_technical",
        "rationale": "Pre-trained models are a foundational element in transfer learning, relevant to the paper's methodology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "deep learning",
      "classification performance",
      "annotated datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-Shot Image Classification",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Self-Learning Cycle",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pre-trained Visual Model",
      "resolved_canonical": "Pre-trained Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# No Labels Needed: Zero-Shot Image Classification with Collaborative Self-Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18938.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18938](https://arxiv.org/abs/2509.18938)

## 🔗 유사한 논문
- [[2025-09-23/ViLReF_ An Expert Knowledge Enabled Vision-Language Retinal Foundation Model_20250923|ViLReF: An Expert Knowledge Enabled Vision-Language Retinal Foundation Model]] (85.9% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (84.9% similar)
- [[2025-09-23/Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification_20250923|Dual-View Alignment Learning with Hierarchical-Prompt for Class-Imbalance Multi-Label Classification]] (84.5% similar)
- [[2025-09-23/Catching the Details_ Self-Distilled RoI Predictors for Fine-Grained MLLM Perception_20250923|Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception]] (84.2% similar)
- [[2025-09-24/VLN-Zero_ Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation_20250924|VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Pre-trained Model|Pre-trained Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18938v1 Announce Type: cross 
Abstract: While deep learning, including Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs), has significantly advanced classification performance, its typical reliance on extensive annotated datasets presents a major obstacle in many practical scenarios where such data is scarce. Vision-language models (VLMs) and transfer learning with pre-trained visual models appear as promising techniques to deal with this problem. This paper proposes a novel zero-shot image classification framework that combines a VLM and a pre-trained visual model within a self-learning cycle. Requiring only the set of class names and no labeled training data, our method utilizes a confidence-based pseudo-labeling strategy to train a lightweight classifier directly on the test data, enabling dynamic adaptation. The VLM identifies high-confidence samples, and the pre-trained visual model enhances their visual representations. These enhanced features then iteratively train the classifier, allowing the system to capture complementary semantic and visual cues without supervision. Notably, our approach avoids VLM fine-tuning and the use of large language models, relying on the visual-only model to reduce the dependence on semantic representation. Experimental evaluations on ten diverse datasets demonstrate that our approach outperforms the baseline zero-shot method.

## 📝 요약

이 논문은 주석이 부족한 데이터셋 문제를 해결하기 위해 새로운 제로샷 이미지 분류 프레임워크를 제안합니다. 이 방법은 비전-언어 모델(VLM)과 사전 학습된 시각 모델을 결합하여 자체 학습 사이클을 형성합니다. 클래스 이름만 필요로 하며, 라벨이 없는 테스트 데이터에 신뢰 기반의 가짜 라벨링 전략을 사용해 경량 분류기를 학습시킵니다. VLM은 높은 신뢰도의 샘플을 식별하고, 사전 학습된 시각 모델은 이들의 시각적 표현을 강화합니다. 이 강화된 특징을 통해 분류기를 반복적으로 학습시켜, 감독 없이 보완적인 의미와 시각적 단서를 포착합니다. VLM의 미세 조정이나 대형 언어 모델을 사용하지 않고, 시각 모델에 의존하여 의미 표현에 대한 의존성을 줄입니다. 실험 결과, 제안된 방법이 10개의 다양한 데이터셋에서 기존 제로샷 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 본 논문은 주석이 부족한 데이터셋 문제를 해결하기 위해 VLM과 사전 학습된 비주얼 모델을 결합한 새로운 제로샷 이미지 분류 프레임워크를 제안합니다.
- 2. 제안된 방법은 클래스 이름만 필요로 하며, 라벨이 없는 테스트 데이터에 대해 경량화된 분류기를 훈련시키는 신뢰 기반의 의사 라벨링 전략을 사용합니다.
- 3. VLM은 높은 신뢰도의 샘플을 식별하고, 사전 학습된 비주얼 모델은 이들의 시각적 표현을 강화하여 분류기를 반복적으로 훈련시킵니다.
- 4. 본 접근법은 VLM의 미세 조정과 대형 언어 모델의 사용을 피하며, 시각적 모델에 의존하여 의미 표현에 대한 의존성을 줄입니다.
- 5. 실험 결과, 제안된 방법은 10개의 다양한 데이터셋에서 기존의 제로샷 방법을 능가하는 성능을 보였습니다.


---

*Generated on 2025-09-24 14:07:25*