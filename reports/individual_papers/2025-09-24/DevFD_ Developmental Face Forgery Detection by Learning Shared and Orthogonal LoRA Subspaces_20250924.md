<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:19:19.451059",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Developmental Mixture of Experts",
    "LoRA models",
    "Face Forgery Detection",
    "Orthogonal Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Developmental Mixture of Experts": 0.78,
    "LoRA models": 0.77,
    "Face Forgery Detection": 0.8,
    "Orthogonal Loss": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Developmental Mixture of Experts",
        "canonical": "Developmental Mixture of Experts",
        "aliases": [
          "Developmental MoE"
        ],
        "category": "unique_technical",
        "rationale": "This concept represents a novel architecture specific to the paper's approach, offering a unique perspective on continual learning in face forgery detection.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "LoRA models",
        "canonical": "LoRA models",
        "aliases": [
          "Low-Rank Adaptation models"
        ],
        "category": "unique_technical",
        "rationale": "LoRA models are central to the paper's methodology, providing a basis for the orthogonal subspace learning approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Face Forgery Detection",
        "canonical": "Face Forgery Detection",
        "aliases": [
          "Deepfake Detection"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key application area of the paper, relevant to ongoing research in digital security and computer vision.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Orthogonal Loss",
        "canonical": "Orthogonal Loss",
        "aliases": [
          "Orthogonal Gradient Loss"
        ],
        "category": "unique_technical",
        "rationale": "Orthogonal Loss is a specific technique used to prevent gradient interference, crucial for the paper's approach.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
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
      "candidate_surface": "Developmental Mixture of Experts",
      "resolved_canonical": "Developmental Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LoRA models",
      "resolved_canonical": "LoRA models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Face Forgery Detection",
      "resolved_canonical": "Face Forgery Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Orthogonal Loss",
      "resolved_canonical": "Orthogonal Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# DevFD: Developmental Face Forgery Detection by Learning Shared and Orthogonal LoRA Subspaces

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19230.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19230](https://arxiv.org/abs/2509.19230)

## 🔗 유사한 논문
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (83.9% similar)
- [[2025-09-19/Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (82.9% similar)
- [[2025-09-23/Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA_20250923|Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA]] (82.7% similar)
- [[2025-09-22/TT-DF_ A Large-Scale Diffusion-Based Dataset and Benchmark for Human Body Forgery Detection_20250922|TT-DF: A Large-Scale Diffusion-Based Dataset and Benchmark for Human Body Forgery Detection]] (82.7% similar)
- [[2025-09-22/TrueMoE_ Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection_20250922|TrueMoE: Dual-Routing Mixture of Discriminative Experts for Synthetic Image Detection]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Face Forgery Detection|Face Forgery Detection]]
**⚡ Unique Technical**: [[keywords/Developmental Mixture of Experts|Developmental Mixture of Experts]], [[keywords/LoRA models|LoRA models]], [[keywords/Orthogonal Loss|Orthogonal Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19230v1 Announce Type: new 
Abstract: The rise of realistic digital face generation and manipulation poses significant social risks. The primary challenge lies in the rapid and diverse evolution of generation techniques, which often outstrip the detection capabilities of existing models. To defend against the ever-evolving new types of forgery, we need to enable our model to quickly adapt to new domains with limited computation and data while avoiding forgetting previously learned forgery types. In this work, we posit that genuine facial samples are abundant and relatively stable in acquisition methods, while forgery faces continuously evolve with the iteration of manipulation techniques. Given the practical infeasibility of exhaustively collecting all forgery variants, we frame face forgery detection as a continual learning problem and allow the model to develop as new forgery types emerge. Specifically, we employ a Developmental Mixture of Experts (MoE) architecture that uses LoRA models as its individual experts. These experts are organized into two groups: a Real-LoRA to learn and refine knowledge of real faces, and multiple Fake-LoRAs to capture incremental information from different forgery types. To prevent catastrophic forgetting, we ensure that the learning direction of Fake-LoRAs is orthogonal to the established subspace. Moreover, we integrate orthogonal gradients into the orthogonal loss of Fake-LoRAs, preventing gradient interference throughout the training process of each task. Experimental results under both the datasets and manipulation types incremental protocols demonstrate the effectiveness of our method.

## 📝 요약

이 논문은 현실적인 디지털 얼굴 생성 및 조작 기술의 발전이 사회적 위험을 초래할 수 있음을 지적하며, 이러한 위조 얼굴을 탐지하는 모델의 한계를 극복하기 위한 방법을 제안합니다. 연구는 얼굴 위조 탐지를 지속적 학습 문제로 정의하고, 새로운 위조 유형이 등장할 때마다 모델이 적응할 수 있도록 합니다. 이를 위해 LoRA 모델을 전문가로 사용하는 개발적 혼합 전문가(MoE) 아키텍처를 활용합니다. Real-LoRA는 실제 얼굴의 지식을 학습하고, 여러 Fake-LoRA는 다양한 위조 유형의 정보를 포착합니다. 위조 유형의 학습 방향이 기존의 학습 공간과 직교하도록 하여 망각을 방지하며, 직교 손실에 직교 그래디언트를 통합하여 각 작업의 훈련 과정에서 그래디언트 간섭을 방지합니다. 실험 결과, 제안된 방법이 데이터셋과 조작 유형의 증분 프로토콜에서 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 현실적인 디지털 얼굴 생성 및 조작 기술의 발전은 사회적 위험을 초래하며, 이러한 기술의 빠른 진화는 기존 모델의 탐지 능력을 초과합니다.
- 2. 새로운 위조 유형에 대처하기 위해 모델이 제한된 계산 및 데이터로 빠르게 적응하면서도 이전에 학습한 위조 유형을 잊지 않도록 해야 합니다.
- 3. 본 연구에서는 얼굴 위조 탐지를 지속 학습 문제로 설정하고, 새로운 위조 유형이 등장할 때마다 모델이 발전할 수 있도록 합니다.
- 4. LoRA 모델을 개별 전문가로 사용하는 Developmental Mixture of Experts (MoE) 아키텍처를 활용하여 진짜 얼굴과 위조 얼굴을 학습합니다.
- 5. 실험 결과, 데이터셋 및 조작 유형 증분 프로토콜에서 제안된 방법의 효과가 입증되었습니다.


---

*Generated on 2025-09-24 16:19:19*