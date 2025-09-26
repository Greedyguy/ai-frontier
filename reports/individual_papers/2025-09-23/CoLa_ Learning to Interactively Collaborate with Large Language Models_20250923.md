---
keywords:
  - Large Language Model
  - Self-supervised Learning
  - Automated Guides
  - Human-AI Collaboration
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2504.02965
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:52:59.487964",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Self-supervised Learning",
    "Automated Guides",
    "Human-AI Collaboration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Self-supervised Learning": 0.82,
    "Automated Guides": 0.78,
    "Human-AI Collaboration": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's theme, linking to existing works on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Self-guided Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-guided Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Relates to the methodology of training guides, connecting to self-supervised learning literature.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Automated Guides",
        "canonical": "Automated Guides",
        "aliases": [
          "AI Guides",
          "Automated Guidance"
        ],
        "category": "unique_technical",
        "rationale": "A novel concept introduced in the paper, crucial for understanding the proposed system.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Human-AI Collaboration",
        "canonical": "Human-AI Collaboration",
        "aliases": [
          "Collaborative AI",
          "Human-AI Interaction"
        ],
        "category": "evolved_concepts",
        "rationale": "Key theme of the paper, linking to broader discussions on AI collaboration.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "QA datasets",
      "puzzle-solving task",
      "constrained text generation task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Self-guided Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Automated Guides",
      "resolved_canonical": "Automated Guides",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Human-AI Collaboration",
      "resolved_canonical": "Human-AI Collaboration",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# CoLa: Learning to Interactively Collaborate with Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2504.02965.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2504.02965](https://arxiv.org/abs/2504.02965)

## 🔗 유사한 논문
- [[2025-09-22/Using Natural Language for Human-Robot Collaboration in the Real World_20250922|Using Natural Language for Human-Robot Collaboration in the Real World]] (85.2% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.9% similar)
- [[2025-09-22/Towards Interactive and Learnable Cooperative Driving Automation_ a Large Language Model-Driven Decision-Making Framework_20250922|Towards Interactive and Learnable Cooperative Driving Automation: a Large Language Model-Driven Decision-Making Framework]] (83.5% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (83.5% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Automated Guides|Automated Guides]]
**🚀 Evolved Concepts**: [[keywords/Human-AI Collaboration|Human-AI Collaboration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.02965v3 Announce Type: replace-cross 
Abstract: LLMs' remarkable ability to tackle a wide range of language tasks opened new opportunities for collaborative human-AI problem solving. LLMs can amplify human capabilities by applying their intuitions and reasoning strategies at scale. We explore whether human guides can be simulated, by generalizing from human demonstrations of guiding an AI system to solve complex language problems. We introduce CoLa, a novel self-guided learning paradigm for training automated $\textit{guides}$ and evaluate it on two QA datasets, a puzzle-solving task, and a constrained text generation task. Our empirical results show that CoLa consistently outperforms competitive approaches across all domains. Moreover, a small-sized trained guide outperforms a strong model like GPT-4 when acting as a guide. We compare the strategies employed by humans and automated guides by conducting a human study on a QA dataset. We show that automated guides outperform humans by adapting their strategies to reasoners' capabilities and conduct qualitative analyses highlighting distinct differences in guiding strategies.

## 📝 요약

이 논문은 인간과 AI의 협력적 문제 해결을 위한 새로운 학습 패러다임인 CoLa를 제안합니다. CoLa는 AI 시스템이 복잡한 언어 문제를 해결하도록 인간 가이드를 모방하는 방법을 일반화하여 자동화된 가이드를 훈련합니다. 두 개의 QA 데이터셋, 퍼즐 해결, 제한된 텍스트 생성 작업에서 CoLa의 성능을 평가한 결과, 모든 분야에서 기존 접근법보다 우수한 성능을 보였습니다. 특히, 소형 가이드 모델이 GPT-4와 같은 강력한 모델보다 더 나은 가이드 역할을 수행했습니다. 인간 연구를 통해 자동화된 가이드가 인간보다 더 효과적으로 전략을 조정하고, 가이드 전략의 차이를 질적으로 분석했습니다.

## 🎯 주요 포인트

- 1. LLMs는 다양한 언어 작업을 해결하는 능력으로 인간-AI 협업 문제 해결의 새로운 기회를 열었습니다.
- 2. CoLa는 AI 시스템을 안내하는 인간 시연을 일반화하여 인간 가이드를 시뮬레이션할 수 있는 새로운 자기 주도 학습 패러다임입니다.
- 3. CoLa는 두 개의 QA 데이터셋, 퍼즐 해결 작업 및 제약된 텍스트 생성 작업에서 경쟁 접근 방식을 일관되게 능가합니다.
- 4. 소형 훈련 가이드는 가이드 역할을 할 때 GPT-4와 같은 강력한 모델보다 뛰어난 성능을 보입니다.
- 5. 자동화된 가이드는 인간의 전략을 능가하며, 이들의 전략은 추론자의 능력에 맞춰 적응합니다.


---

*Generated on 2025-09-24 00:52:59*