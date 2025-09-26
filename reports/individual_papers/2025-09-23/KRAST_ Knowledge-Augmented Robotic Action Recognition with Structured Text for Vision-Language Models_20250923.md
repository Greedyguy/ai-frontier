---
keywords:
  - Vision-Language Model
  - Knowledge-Augmented Prompts
  - Prompt-Learning
  - Robotic Action Recognition
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16452
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:20:32.280610",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Knowledge-Augmented Prompts",
    "Prompt-Learning",
    "Robotic Action Recognition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Knowledge-Augmented Prompts": 0.78,
    "Prompt-Learning": 0.8,
    "Robotic Action Recognition": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's methodology, linking vision and language processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Knowledge-Augmented Prompts",
        "canonical": "Knowledge-Augmented Prompts",
        "aliases": [
          "Knowledge-Enhanced Prompts"
        ],
        "category": "unique_technical",
        "rationale": "This concept is a novel approach in the paper, enhancing model performance with structured knowledge.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Prompt-Learning Framework",
        "canonical": "Prompt-Learning",
        "aliases": [
          "Prompt-Based Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Prompt-Learning is a key technique used in the paper, facilitating the integration of textual descriptions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Robotic Action Recognition",
        "canonical": "Robotic Action Recognition",
        "aliases": [
          "Robot Action Detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application of the research, linking robotics and action recognition.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
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
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Knowledge-Augmented Prompts",
      "resolved_canonical": "Knowledge-Augmented Prompts",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Prompt-Learning Framework",
      "resolved_canonical": "Prompt-Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Robotic Action Recognition",
      "resolved_canonical": "Robotic Action Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# KRAST: Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16452.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16452](https://arxiv.org/abs/2509.16452)

## 🔗 유사한 논문
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (84.6% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (84.5% similar)
- [[2025-09-19/CollabVLA_ Self-Reflective Vision-Language-Action Model Dreaming Together with Human_20250919|CollabVLA: Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (82.8% similar)
- [[2025-09-18/GeoAware-VLA_ Implicit Geometry Aware Vision-Language-Action Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (82.6% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Prompt-Learning|Prompt-Learning]]
**⚡ Unique Technical**: [[keywords/Knowledge-Augmented Prompts|Knowledge-Augmented Prompts]], [[keywords/Robotic Action Recognition|Robotic Action Recognition]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16452v1 Announce Type: cross 
Abstract: Accurate vision-based action recognition is crucial for developing autonomous robots that can operate safely and reliably in complex, real-world environments. In this work, we advance video-based recognition of indoor daily actions for robotic perception by leveraging vision-language models (VLMs) enriched with domain-specific knowledge. We adapt a prompt-learning framework in which class-level textual descriptions of each action are embedded as learnable prompts into a frozen pre-trained VLM backbone. Several strategies for structuring and encoding these textual descriptions are designed and evaluated. Experiments on the ETRI-Activity3D dataset demonstrate that our method, using only RGB video inputs at test time, achieves over 95\% accuracy and outperforms state-of-the-art approaches. These results highlight the effectiveness of knowledge-augmented prompts in enabling robust action recognition with minimal supervision.

## 📝 요약

이 연구는 자율 로봇의 안전하고 신뢰할 수 있는 동작을 위해 실내 일상 행동을 인식하는 비디오 기반 방법을 제안합니다. 비전-언어 모델(VLM)을 사용하여 도메인 특화 지식을 활용하고, 프롬프트 학습 프레임워크를 통해 각 행동에 대한 텍스트 설명을 학습 가능한 프롬프트로 VLM에 삽입합니다. ETRI-Activity3D 데이터셋 실험에서 RGB 비디오 입력만으로 95% 이상의 정확도를 달성하며, 기존 최첨단 방법을 능가했습니다. 이는 지식이 강화된 프롬프트가 최소한의 감독으로도 강력한 행동 인식을 가능하게 함을 보여줍니다.

## 🎯 주요 포인트

- 1. 비전-언어 모델(VLM)을 활용하여 로봇의 실내 일상 행동 인식을 개선하였습니다.
- 2. 프롬프트 학습 프레임워크를 적용하여 각 행동의 텍스트 설명을 학습 가능한 프롬프트로 VLM에 임베딩하였습니다.
- 3. ETRI-Activity3D 데이터셋 실험 결과, RGB 비디오 입력만으로 95% 이상의 정확도를 달성하였습니다.
- 4. 지식이 강화된 프롬프트가 최소한의 감독으로 강력한 행동 인식을 가능하게 함을 입증하였습니다.


---

*Generated on 2025-09-23 23:20:32*