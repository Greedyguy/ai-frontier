---
keywords:
  - Multimodal Learning
  - Zero-Shot Learning
  - Forgery Detection
  - Reinforcement Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19841
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:07:56.055403",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Zero-Shot Learning",
    "Forgery Detection",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Zero-Shot Learning": 0.79,
    "Forgery Detection": 0.77,
    "Reinforcement Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Model",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLM"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is crucial for integrating visual and textual data, enhancing the detection capabilities of AI systems.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-Shot Generalization",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is essential for models to generalize without task-specific training data, aligning with the paper's focus on generalization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Forgery Reasoning Prompt",
        "canonical": "Forgery Detection",
        "aliases": [
          "Forgery Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Forgery Detection is a unique aspect of the paper, focusing on reasoning-based approaches for identifying AI-generated images.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "GRPO"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational technique used in the paper to optimize the model's reasoning capabilities.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "detection method",
      "structured outputs",
      "extensive experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-Shot Generalization",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Forgery Reasoning Prompt",
      "resolved_canonical": "Forgery Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ThinkFake: Reasoning in Multimodal Large Language Models for AI-Generated Image Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19841.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19841](https://arxiv.org/abs/2509.19841)

## 🔗 유사한 논문
- [[2025-09-22/PRISM_ Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images_20250922|PRISM: Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images]] (86.5% similar)
- [[2025-09-22/Causal Fingerprints of AI Generative Models_20250922|Causal Fingerprints of AI Generative Models]] (85.3% similar)
- [[2025-09-22/Toward Medical Deepfake Detection_ A Comprehensive Dataset and Novel Method_20250922|Toward Medical Deepfake Detection: A Comprehensive Dataset and Novel Method]] (85.0% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (84.8% similar)
- [[2025-09-24/AvatarShield_ Visual Reinforcement Learning for Human-Centric Synthetic Video Detection_20250924|AvatarShield: Visual Reinforcement Learning for Human-Centric Synthetic Video Detection]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Forgery Detection|Forgery Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19841v1 Announce Type: new 
Abstract: The increasing realism of AI-generated images has raised serious concerns about misinformation and privacy violations, highlighting the urgent need for accurate and interpretable detection methods. While existing approaches have made progress, most rely on binary classification without explanations or depend heavily on supervised fine-tuning, resulting in limited generalization. In this paper, we propose ThinkFake, a novel reasoning-based and generalizable framework for AI-generated image detection. Our method leverages a Multimodal Large Language Model (MLLM) equipped with a forgery reasoning prompt and is trained using Group Relative Policy Optimization (GRPO) reinforcement learning with carefully designed reward functions. This design enables the model to perform step-by-step reasoning and produce interpretable, structured outputs. We further introduce a structured detection pipeline to enhance reasoning quality and adaptability. Extensive experiments show that ThinkFake outperforms state-of-the-art methods on the GenImage benchmark and demonstrates strong zero-shot generalization on the challenging LOKI benchmark. These results validate our framework's effectiveness and robustness. Code will be released upon acceptance.

## 📝 요약

AI 생성 이미지의 사실성과 관련된 허위 정보 및 프라이버시 침해 문제가 대두되면서, 정확하고 해석 가능한 탐지 방법의 필요성이 커지고 있습니다. 기존 방법들은 대부분 이진 분류에 의존하거나 감독 학습에 크게 의존하여 일반화에 한계가 있습니다. 본 논문에서는 AI 생성 이미지 탐지를 위한 새로운 추론 기반 프레임워크인 ThinkFake를 제안합니다. 이 방법은 위조 추론 프롬프트가 장착된 다중 모달 대형 언어 모델(MLLM)을 활용하며, 그룹 상대 정책 최적화(GRPO) 강화 학습을 통해 훈련됩니다. 이 설계는 단계별 추론과 해석 가능한 구조적 출력을 가능하게 합니다. 또한, 추론 품질과 적응성을 높이기 위한 구조적 탐지 파이프라인을 도입했습니다. 실험 결과, ThinkFake는 GenImage 벤치마크에서 최첨단 방법들을 능가하며, LOKI 벤치마크에서 강력한 제로샷 일반화를 보여주었습니다. 이러한 결과는 본 프레임워크의 효과성과 견고성을 입증합니다. 코드 공개는 승인 후 진행될 예정입니다.

## 🎯 주요 포인트

- 1. AI 생성 이미지의 사실성 증가로 인한 허위 정보 및 개인정보 침해 문제를 해결하기 위해 정확하고 해석 가능한 탐지 방법이 필요합니다.
- 2. 기존 방법들은 이진 분류에 의존하거나 감독 학습에 크게 의존하여 일반화에 한계가 있습니다.
- 3. ThinkFake는 위조 추론 프롬프트를 갖춘 다중 모달 대형 언어 모델(MLLM)을 활용하여 AI 생성 이미지 탐지를 위한 새로운 추론 기반 프레임워크를 제안합니다.
- 4. 제안된 방법은 그룹 상대 정책 최적화(GRPO) 강화 학습을 통해 단계별 추론과 해석 가능한 구조화된 출력을 생성합니다.
- 5. ThinkFake는 GenImage 및 LOKI 벤치마크에서 최첨단 방법을 능가하며, 코드 공개 예정입니다.


---

*Generated on 2025-09-26 09:07:56*