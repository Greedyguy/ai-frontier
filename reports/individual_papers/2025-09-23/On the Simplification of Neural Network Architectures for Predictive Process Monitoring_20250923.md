---
keywords:
  - Predictive Process Monitoring
  - Transformer
  - Long Short-Term Memory
  - Model Simplification
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17145
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:47:22.114787",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Predictive Process Monitoring",
    "Transformer",
    "Long Short-Term Memory",
    "Model Simplification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Predictive Process Monitoring": 0.78,
    "Transformer": 0.85,
    "Long Short-Term Memory": 0.82,
    "Model Simplification": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Predictive Process Monitoring",
        "canonical": "Predictive Process Monitoring",
        "aliases": [
          "PPM"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized application area that can connect to various process mining and monitoring studies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model in deep learning, relevant to the simplification study discussed.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "LSTM",
        "canonical": "Long Short-Term Memory",
        "aliases": [
          "LSTM"
        ],
        "category": "specific_connectable",
        "rationale": "LSTMs are a key model type in predictive tasks and their simplification is central to the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "model simplification",
        "canonical": "Model Simplification",
        "aliases": [
          "simplifying models"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on simplifying neural network architectures, making this a unique technical focus.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "deep learning models",
      "event logs",
      "predictive performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Predictive Process Monitoring",
      "resolved_canonical": "Predictive Process Monitoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "LSTM",
      "resolved_canonical": "Long Short-Term Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "model simplification",
      "resolved_canonical": "Model Simplification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# On the Simplification of Neural Network Architectures for Predictive Process Monitoring

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17145.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17145](https://arxiv.org/abs/2509.17145)

## 🔗 유사한 논문
- [[2025-09-23/SCAN_ Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning_20250923|SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning]] (82.0% similar)
- [[2025-09-23/Less is More_ Unlocking Specialization of Time Series Foundation Models via Structured Pruning_20250923|Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning]] (81.9% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (81.9% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (81.8% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Long Short-Term Memory|Long Short-Term Memory]]
**⚡ Unique Technical**: [[keywords/Predictive Process Monitoring|Predictive Process Monitoring]], [[keywords/Model Simplification|Model Simplification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17145v1 Announce Type: new 
Abstract: Predictive Process Monitoring (PPM) aims to forecast the future behavior of ongoing process instances using historical event data, enabling proactive decision-making. While recent advances rely heavily on deep learning models such as LSTMs and Transformers, their high computational cost hinders practical adoption. Prior work has explored data reduction techniques and alternative feature encodings, but the effect of simplifying model architectures themselves remains underexplored. In this paper, we analyze how reducing model complexity, both in terms of parameter count and architectural depth, impacts predictive performance, using two established PPM approaches. Across five diverse event logs, we show that shrinking the Transformer model by 85% results in only a 2-3% drop in performance across various PPM tasks, while the LSTM proves slightly more sensitive, particularly for waiting time prediction. Overall, our findings suggest that substantial model simplification can preserve predictive accuracy, paving the way for more efficient and scalable PPM solutions.

## 📝 요약

이 논문은 예측 프로세스 모니터링(PPM)에서 모델의 복잡성을 줄이는 것이 예측 성능에 미치는 영향을 분석합니다. 기존의 LSTM과 Transformer 모델의 높은 계산 비용 문제를 해결하기 위해, 모델의 매개변수 수와 구조적 깊이를 줄이는 방법을 탐구했습니다. 다섯 개의 다양한 이벤트 로그를 통해 실험한 결과, Transformer 모델의 크기를 85% 줄여도 성능 저하가 2-3%에 불과했으며, LSTM은 대기 시간 예측에서 더 민감한 반응을 보였습니다. 이 연구는 모델 단순화가 예측 정확성을 유지하면서도 효율적이고 확장 가능한 PPM 솔루션을 가능하게 할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 예측 프로세스 모니터링(PPM)은 과거 이벤트 데이터를 활용하여 현재 진행 중인 프로세스의 미래 행동을 예측하는 것을 목표로 한다.
- 2. 최근의 PPM 연구는 LSTM과 Transformer 같은 딥러닝 모델에 의존하지만, 높은 계산 비용이 실용적인 채택을 방해한다.
- 3. 본 논문은 모델의 파라미터 수와 구조적 깊이를 줄이는 것이 예측 성능에 미치는 영향을 분석하였다.
- 4. Transformer 모델의 크기를 85% 줄여도 다양한 PPM 작업에서 성능이 2-3%만 감소하는 것으로 나타났다.
- 5. 모델 단순화가 예측 정확성을 유지하면서도 더 효율적이고 확장 가능한 PPM 솔루션을 가능하게 할 수 있음을 시사한다.


---

*Generated on 2025-09-24 01:47:22*