---
keywords:
  - Large Language Model
  - Contextual Robustness
  - Adaptive Distraction
  - Tree Search
  - Post-Training Optimization
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2502.01609
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:47:48.117236",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Contextual Robustness",
    "Adaptive Distraction",
    "Tree Search",
    "Post-Training Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Contextual Robustness": 0.8,
    "Adaptive Distraction": 0.78,
    "Tree Search": 0.77,
    "Post-Training Optimization": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "This is a central concept in the paper, linking it to the broader field of language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "contextual robustness",
        "canonical": "Contextual Robustness",
        "aliases": [
          "context robustness"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical term introduced in the paper, crucial for understanding the model's performance under distraction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "adaptive distraction",
        "canonical": "Adaptive Distraction",
        "aliases": [
          "dynamic distraction"
        ],
        "category": "unique_technical",
        "rationale": "This term describes the novel method proposed in the paper, essential for linking to the methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "tree search",
        "canonical": "Tree Search",
        "aliases": [
          "automated tree search"
        ],
        "category": "specific_connectable",
        "rationale": "Tree search is a key technique used in the paper, linking it to algorithmic strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "post-training approaches",
        "canonical": "Post-Training Optimization",
        "aliases": [
          "post-training methods",
          "DPO"
        ],
        "category": "specific_connectable",
        "rationale": "This connects to strategies for improving model robustness, which is a significant focus of the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
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
      "candidate_surface": "contextual robustness",
      "resolved_canonical": "Contextual Robustness",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "adaptive distraction",
      "resolved_canonical": "Adaptive Distraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "tree search",
      "resolved_canonical": "Tree Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "post-training approaches",
      "resolved_canonical": "Post-Training Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.01609.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2502.01609](https://arxiv.org/abs/2502.01609)

## 🔗 유사한 논문
- [[2025-09-23/How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark_20250923|How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark]] (89.7% similar)
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (87.0% similar)
- [[2025-09-22/From Judgment to Interference_ Early Stopping LLM Harmful Outputs via Streaming Content Monitoring_20250922|From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring]] (86.2% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (86.2% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (86.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Tree Search|Tree Search]], [[keywords/Post-Training Optimization|Post-Training Optimization]]
**⚡ Unique Technical**: [[keywords/Contextual Robustness|Contextual Robustness]], [[keywords/Adaptive Distraction|Adaptive Distraction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.01609v2 Announce Type: replace 
Abstract: Large Language Models (LLMs) often struggle to maintain their original performance when faced with semantically coherent but task-irrelevant contextual information. Although prior studies have explored this issue using fixed-template or retrieval-based distractions, such static methods show limited effectiveness against contemporary models. To address this problem, we propose a dynamic distraction generation framework based on tree search, where the generation process is guided by model behavior. Without modifying the original question or answer, the method efficiently produces challenging adaptive distractions across multiple datasets, enabling systematic stress testing of LLMs' contextual robustness. Experiments on four benchmarks demonstrate that the generated distractions lead to an average performance drop of over 45\% for mainstream models. Further comparisons of mitigation strategies show that prompt-based optimization methods yield limited gains, whereas post-training approaches (e.g., DPO) significantly enhance the model's contextual robustness. The results indicate that these issues do not stem from knowledge deficits in LLMs, but from a fundamental inability to maintain consistent reasoning under contextual distraction, posing a major challenge to the reliability of LLMs in real-world applications. The code is publicly available at https://github.com/wyf23187/Adaptive_Distractions.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 의미적으로 일관되지만 과제와 무관한 문맥 정보에 직면했을 때 성능을 유지하기 어려운 문제를 다룹니다. 이를 해결하기 위해, 모델의 행동을 기반으로 하는 트리 탐색을 활용한 동적 방해 요소 생성 프레임워크를 제안합니다. 이 방법은 원래의 질문이나 답변을 수정하지 않고도 다양한 데이터셋에서 적응적인 방해 요소를 생성하여 LLM의 문맥적 강인성을 체계적으로 테스트할 수 있습니다. 실험 결과, 생성된 방해 요소가 주류 모델의 성능을 평균 45% 이상 감소시켰으며, 후속 학습 방법(DPO 등)이 문맥적 강인성을 크게 향상시킴을 보여줍니다. 이는 LLM의 지식 부족이 아닌, 문맥적 방해 요소 하에서 일관된 추론을 유지하는 데 근본적인 어려움이 있음을 시사합니다. 코드가 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 의미적으로 일관되지만 작업과 무관한 맥락 정보에 직면했을 때 원래 성능을 유지하는 데 어려움을 겪습니다.
- 2. 본 연구는 모델의 행동에 의해 유도되는 트리 탐색 기반의 동적 방해 요소 생성 프레임워크를 제안합니다.
- 3. 생성된 방해 요소는 주류 모델의 평균 성능을 45% 이상 감소시켰으며, 이는 LLM의 맥락적 강건성을 체계적으로 테스트할 수 있게 합니다.
- 4. 프롬프트 기반 최적화 방법은 제한된 성과를 보였으나, 후속 훈련 접근법(DPO 등)은 모델의 맥락적 강건성을 크게 향상시켰습니다.
- 5. 이러한 문제는 LLM의 지식 결핍에서 기인한 것이 아니라, 맥락적 방해 요소 하에서 일관된 추론을 유지하지 못하는 근본적인 한계에서 비롯됩니다.


---

*Generated on 2025-09-24 03:47:48*