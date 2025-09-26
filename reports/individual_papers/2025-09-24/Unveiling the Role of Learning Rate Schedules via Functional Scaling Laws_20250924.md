<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:01:29.297709",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Learning Rate Schedule",
    "Functional Scaling Law",
    "Stochastic Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Learning Rate Schedule": 0.78,
    "Functional Scaling Law": 0.8,
    "Stochastic Gradient Descent": 0.72
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
        "rationale": "Central to the paper, linking to existing knowledge on large-scale model training.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Learning Rate Schedule",
        "canonical": "Learning Rate Schedule",
        "aliases": [
          "LRS",
          "Learning Rate Schedules"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the study, providing insights into training dynamics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Functional Scaling Law",
        "canonical": "Functional Scaling Law",
        "aliases": [
          "FSL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept for understanding training processes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Stochastic Gradient Descent",
        "canonical": "Stochastic Gradient Descent",
        "aliases": [
          "SGD"
        ],
        "category": "specific_connectable",
        "rationale": "Common optimization method, relevant for linking training methodologies.",
        "novelty_score": 0.2,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "scaling laws",
      "teacher-student kernel regression",
      "population risk"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Learning Rate Schedule",
      "resolved_canonical": "Learning Rate Schedule",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Functional Scaling Law",
      "resolved_canonical": "Functional Scaling Law",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Stochastic Gradient Descent",
      "resolved_canonical": "Stochastic Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Unveiling the Role of Learning Rate Schedules via Functional Scaling Laws

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19189.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19189](https://arxiv.org/abs/2509.19189)

## 🔗 유사한 논문
- [[2025-09-23/Temporal Scaling Law for Large Language Models_20250923|Temporal Scaling Law for Large Language Models]] (90.0% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (83.6% similar)
- [[2025-09-23/Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling_20250923|Mitigating Strategy-Selection Bias in Reasoning for More Effective Test-Time Scaling]] (83.3% similar)
- [[2025-09-23/Bayesian scaling laws for in-context learning_20250923|Bayesian scaling laws for in-context learning]] (83.1% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Stochastic Gradient Descent|Stochastic Gradient Descent]]
**⚡ Unique Technical**: [[keywords/Learning Rate Schedule|Learning Rate Schedule]], [[keywords/Functional Scaling Law|Functional Scaling Law]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19189v1 Announce Type: new 
Abstract: Scaling laws have played a cornerstone role in guiding the training of large language models (LLMs). However, most existing works on scaling laws primarily focus on the final-step loss, overlooking the loss dynamics during the training process and, crucially, the impact of learning rate schedule (LRS). In this paper, we aim to bridge this gap by studying a teacher-student kernel regression setup trained via online stochastic gradient descent (SGD). Leveraging a novel intrinsic time viewpoint and stochastic differential equation (SDE) modeling of SGD, we introduce the Functional Scaling Law (FSL), which characterizes the evolution of population risk during the training process for general LRSs. Remarkably, the impact of the LRSs is captured through an explicit convolution-type functional term, making their effects fully tractable. To illustrate the utility of FSL, we analyze three widely used LRSs -- constant, exponential decay, and warmup-stable-decay (WSD) -- under both data-limited and compute-limited regimes. We provide theoretical justification for widely adopted empirical practices in LLMs pre-training such as (i) higher-capacity models are more data- and compute-efficient; (ii) learning rate decay can improve training efficiency; (iii) WSD-like schedules can outperform direct-decay schedules. Lastly, we explore the practical relevance of FSL as a surrogate model for fitting, predicting and optimizing the loss curves in LLM pre-training, with experiments conducted across model sizes ranging from 0.1B to 1B parameters. We hope our FSL framework can deepen the understanding of LLM pre-training dynamics and provide insights for improving large-scale model training.

## 📝 요약

이 논문은 대형 언어 모델(LLM) 훈련에서 중요한 역할을 하는 스케일링 법칙의 한계를 극복하고자 한다. 기존 연구들은 최종 손실에 집중했으나, 이 논문은 학습률 스케줄(LRS)의 영향을 포함한 손실 동태를 분석한다. 저자들은 온라인 확률적 경사 하강법(SGD)을 사용한 교사-학생 커널 회귀 설정을 통해, 인구 위험의 변화를 설명하는 기능적 스케일링 법칙(FSL)을 제안한다. FSL은 LRS의 영향을 명시적 컨볼루션 형태로 설명하여, 이들의 효과를 명확히 파악할 수 있게 한다. 세 가지 LRS(상수, 지수적 감소, 워밍업-안정-감소)를 분석하고, 이론적으로 대형 모델의 데이터 및 계산 효율성, 학습률 감소의 효율성, WSD 스케줄의 우수성을 설명한다. FSL은 LLM 사전 훈련의 손실 곡선을 예측하고 최적화하는 데 유용하며, 다양한 모델 크기에서 실험을 통해 그 실용성을 입증한다. 이는 LLM 훈련의 이해를 심화하고 대규모 모델 훈련 개선에 기여할 수 있다.

## 🎯 주요 포인트

- 1. 기존의 스케일링 법칙 연구는 주로 최종 손실에 초점을 맞추었으나, 본 논문은 학습률 스케줄(LRS)의 영향을 포함한 손실 동역학을 연구한다.
- 2. 본 연구에서는 온라인 확률적 경사 하강법(SGD)을 통한 교사-학생 커널 회귀 설정을 사용하여, 학습 과정 중 인구 위험의 진화를 설명하는 기능적 스케일링 법칙(FSL)을 도입한다.
- 3. FSL은 학습률 스케줄의 영향을 명시적인 컨볼루션 형태의 기능적 항으로 포착하여 그 효과를 완전히 추적 가능하게 한다.
- 4. 이론적 분석을 통해 높은 용량의 모델이 데이터 및 계산 효율성이 더 높고, 학습률 감소가 훈련 효율성을 향상시킬 수 있음을 설명한다.
- 5. FSL은 LLM 사전 훈련의 손실 곡선을 맞추고 예측하며 최적화하는 대체 모델로서의 실용적 관련성을 탐구한다.


---

*Generated on 2025-09-24 15:01:29*