---
keywords:
  - Large Language Model
  - Gaussian Mixture Model
  - Pre-Generation Adequacy Measure
  - Task-Specific Evaluation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17314
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:21:56.302445",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Gaussian Mixture Model",
    "Pre-Generation Adequacy Measure",
    "Task-Specific Evaluation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Gaussian Mixture Model": 0.78,
    "Pre-Generation Adequacy Measure": 0.79,
    "Task-Specific Evaluation": 0.77
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
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and are a key concept in machine learning, linking to various applications and methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Gaussian Mixture Model",
        "canonical": "Gaussian Mixture Model",
        "aliases": [
          "GMM"
        ],
        "category": "specific_connectable",
        "rationale": "Gaussian Mixture Models are used in the paper for sampling and ranking inputs, providing a specific statistical method that connects to broader statistical learning concepts.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "pre-generation adequacy measure",
        "canonical": "Pre-Generation Adequacy Measure",
        "aliases": [
          "input adequacy measure"
        ],
        "category": "unique_technical",
        "rationale": "This measure is a novel concept introduced in the paper, crucial for assessing input adequacy before output generation, linking to task-specific evaluation techniques.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "task-specific",
        "canonical": "Task-Specific Evaluation",
        "aliases": [
          "task-focused",
          "task-oriented"
        ],
        "category": "unique_technical",
        "rationale": "Task-specific evaluation is a core theme of the paper, emphasizing the need for tailored assessment methods in LLM applications.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Gaussian Mixture Model",
      "resolved_canonical": "Gaussian Mixture Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "pre-generation adequacy measure",
      "resolved_canonical": "Pre-Generation Adequacy Measure",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "task-specific",
      "resolved_canonical": "Task-Specific Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Clotho: Measuring Task-Specific Pre-Generation Test Adequacy for LLM Inputs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17314.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17314](https://arxiv.org/abs/2509.17314)

## 🔗 유사한 논문
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (84.5% similar)
- [[2025-09-22/Creative Preference Optimization_20250922|Creative Preference Optimization]] (83.3% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO: A Framework for Confidence-Aware Routing of Large Language Models]] (83.2% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (83.2% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Gaussian Mixture Model|Gaussian Mixture Model]]
**⚡ Unique Technical**: [[keywords/Pre-Generation Adequacy Measure|Pre-Generation Adequacy Measure]], [[keywords/Task-Specific Evaluation|Task-Specific Evaluation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17314v1 Announce Type: cross 
Abstract: Software increasingly relies on the emergent capabilities of Large Language Models (LLMs), from natural language understanding to program analysis and generation. Yet testing them on specific tasks remains difficult and costly: many prompts lack ground truth, forcing reliance on human judgment, while existing uncertainty and adequacy measures typically require full inference. A key challenge is to assess input adequacy in a way that reflects the demands of the task, ideally before even generating any output. We introduce CLOTHO, a task-specific, pre-generation adequacy measure that estimates input difficulty directly from hidden LLM states. Given a large pool of unlabelled inputs for a specific task, CLOTHO uses a Gaussian Mixture Model (GMM) to adaptively sample the most informative cases for human labelling. Based on this reference set the GMM can then rank unseen inputs by their likelihood of failure. In our empirical evaluation across eight benchmark tasks and three open-weight LLMs, CLOTHO can predict failures with a ROC-AUC of 0.716, after labelling reference sets that are on average only 5.4% of inputs. It does so without generating any outputs, thereby reducing costs compared to existing uncertainty measures. Comparison of CLOTHO and post-generation uncertainty measures shows that the two approaches complement each other. Crucially, we show that adequacy scores learnt from open-weight LLMs transfer effectively to proprietary models, extending the applicability of the approach. When prioritising test inputs for proprietary models, CLOTHO increases the average number of failing inputs from 18.7 to 42.5 out of 100, compared to random prioritisation.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 입력 적합성을 사전 평가하는 CLOTHO라는 새로운 측정 방법을 제안합니다. CLOTHO는 Gaussian Mixture Model(GMM)을 사용하여 특정 작업에 대한 입력의 난이도를 LLM의 숨겨진 상태에서 직접 추정합니다. 이를 통해 가장 정보가 많은 입력을 선택하여 인간이 레이블링하도록 하고, 이를 기반으로 새로운 입력의 실패 가능성을 예측합니다. 실험 결과, CLOTHO는 평균 5.4%의 입력만 레이블링하여도 0.716의 ROC-AUC로 실패를 예측할 수 있으며, 출력 생성 없이 비용을 절감합니다. 또한, 공개된 LLM에서 학습한 적합성 점수가 독점 모델에도 효과적으로 적용됨을 보여줍니다. CLOTHO는 독점 모델의 테스트 입력을 우선순위화할 때 실패 입력 수를 랜덤 우선순위화보다 크게 증가시킵니다.

## 🎯 주요 포인트

- 1. CLOTHO는 대형 언어 모델(LLM)의 숨겨진 상태로부터 입력의 난이도를 직접 추정하여 사전 생성 적합성을 평가하는 방법을 제안합니다.
- 2. CLOTHO는 특정 작업에 대한 레이블이 없는 입력 풀에서 가장 유익한 사례를 적응적으로 샘플링하기 위해 가우시안 혼합 모델(GMM)을 사용합니다.
- 3. CLOTHO는 평균적으로 입력의 5.4%만 레이블링하여 ROC-AUC 0.716의 성능으로 실패를 예측할 수 있습니다.
- 4. CLOTHO는 출력 생성 없이 비용을 절감하며, 기존의 불확실성 측정 방법과 상호 보완적인 관계를 가집니다.
- 5. CLOTHO는 오픈 웨이트 LLM에서 학습한 적합성 점수를 독점 모델로 효과적으로 전이하여, 독점 모델 테스트 입력의 실패율을 증가시킵니다.


---

*Generated on 2025-09-24 02:21:56*