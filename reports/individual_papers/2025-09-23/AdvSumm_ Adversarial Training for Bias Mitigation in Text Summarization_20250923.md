---
keywords:
  - Large Language Model
  - Adversarial Summarization
  - Bias Mitigation
  - Sequence-to-Sequence Model
  - Gradient-guided Perturbation
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.06273
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:04:08.051603",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Adversarial Summarization",
    "Bias Mitigation",
    "Sequence-to-Sequence Model",
    "Gradient-guided Perturbation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Adversarial Summarization": 0.82,
    "Bias Mitigation": 0.79,
    "Sequence-to-Sequence Model": 0.77,
    "Gradient-guided Perturbation": 0.8
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
        "rationale": "Large Language Models are central to the paper's focus on summarization and bias mitigation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adversarial Summarization",
        "canonical": "Adversarial Summarization",
        "aliases": [
          "AdvSumm"
        ],
        "category": "unique_technical",
        "rationale": "Adversarial Summarization is a novel approach introduced in the paper, crucial for understanding its contribution.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bias Mitigation",
        "canonical": "Bias Mitigation",
        "aliases": [
          "Bias Reduction"
        ],
        "category": "specific_connectable",
        "rationale": "Bias Mitigation is a key theme of the paper, relevant for linking to broader discussions on fairness in AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Sequence-to-Sequence models",
        "canonical": "Sequence-to-Sequence Model",
        "aliases": [
          "Seq2Seq"
        ],
        "category": "specific_connectable",
        "rationale": "Sequence-to-Sequence models are fundamental to the summarization process discussed in the paper.",
        "novelty_score": 0.48,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Gradient-guided perturbations",
        "canonical": "Gradient-guided Perturbation",
        "aliases": [
          "Gradient Perturbation"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel aspect of the paper's methodology, enhancing model robustness.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
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
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adversarial Summarization",
      "resolved_canonical": "Adversarial Summarization",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bias Mitigation",
      "resolved_canonical": "Bias Mitigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Sequence-to-Sequence models",
      "resolved_canonical": "Sequence-to-Sequence Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Gradient-guided perturbations",
      "resolved_canonical": "Gradient-guided Perturbation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# AdvSumm: Adversarial Training for Bias Mitigation in Text Summarization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.06273.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.06273](https://arxiv.org/abs/2506.06273)

## 🔗 유사한 논문
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (85.4% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (84.6% similar)
- [[2025-09-23/QA-prompting_ Improving Summarization with Large Language Models using Question-Answering_20250923|QA-prompting: Improving Summarization with Large Language Models using Question-Answering]] (84.5% similar)
- [[2025-09-22/Re-FRAME the Meeting Summarization SCOPE_ Fact-Based Summarization and Personalization via Questions_20250922|Re-FRAME the Meeting Summarization SCOPE: Fact-Based Summarization and Personalization via Questions]] (83.3% similar)
- [[2025-09-23/Auto-Search and Refinement_ An Automated Framework for Gender Bias Mitigation in Large Language Models_20250923|Auto-Search and Refinement: An Automated Framework for Gender Bias Mitigation in Large Language Models]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Bias Mitigation|Bias Mitigation]], [[keywords/Sequence-to-Sequence Model|Sequence-to-Sequence Model]]
**⚡ Unique Technical**: [[keywords/Adversarial Summarization|Adversarial Summarization]], [[keywords/Gradient-guided Perturbation|Gradient-guided Perturbation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.06273v2 Announce Type: replace 
Abstract: Large Language Models (LLMs) have achieved impressive performance in text summarization and are increasingly deployed in real-world applications. However, these systems often inherit associative and framing biases from pre-training data, leading to inappropriate or unfair outputs in downstream tasks. In this work, we present AdvSumm (Adversarial Summarization), a domain-agnostic training framework designed to mitigate bias in text summarization through improved generalization. Inspired by adversarial robustness, AdvSumm introduces a novel Perturber component that applies gradient-guided perturbations at the embedding level of Sequence-to-Sequence models, enhancing the model's robustness to input variations. We empirically demonstrate that AdvSumm effectively reduces different types of bias in summarization-specifically, name-nationality bias and political framing bias-without compromising summarization quality. Compared to standard transformers and data augmentation techniques like back-translation, AdvSumm achieves stronger bias mitigation performance across benchmark datasets.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 텍스트 요약에서 뛰어난 성능을 보이지만, 사전 학습 데이터로부터 연관 및 프레이밍 편향을 물려받아 부적절하거나 불공정한 결과를 초래할 수 있음을 지적합니다. 이를 해결하기 위해, 저자들은 AdvSumm이라는 편향 완화 훈련 프레임워크를 제안합니다. AdvSumm는 적대적 견고성에서 영감을 받아, 시퀀스-투-시퀀스 모델의 임베딩 단계에서 그래디언트 기반의 변형을 적용하는 Perturber 컴포넌트를 도입하여 모델의 입력 변동에 대한 견고성을 향상시킵니다. 실험 결과, AdvSumm는 요약 품질을 유지하면서 이름-국적 편향과 정치적 프레이밍 편향을 효과적으로 줄이는 것으로 나타났습니다. 이는 기존의 트랜스포머와 데이터 증강 기법보다 뛰어난 편향 완화 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 텍스트 요약에서 뛰어난 성능을 보이지만, 사전 학습 데이터로부터 편향을 물려받아 부적절하거나 불공정한 결과를 초래할 수 있다.
- 2. AdvSumm은 텍스트 요약에서의 편향을 완화하기 위해 설계된 도메인 독립적인 훈련 프레임워크로, 일반화를 개선하여 편향을 줄인다.
- 3. AdvSumm은 시퀀스-투-시퀀스 모델의 임베딩 수준에서 그래디언트 기반의 교란을 적용하는 Perturber 컴포넌트를 도입하여 모델의 입력 변이에 대한 강건성을 향상시킨다.
- 4. AdvSumm은 요약의 질을 저하시키지 않으면서 이름-국적 편향과 정치적 프레이밍 편향을 효과적으로 줄인다.
- 5. AdvSumm은 표준 트랜스포머와 역번역 같은 데이터 증강 기법에 비해 벤치마크 데이터셋에서 더 강력한 편향 완화 성능을 보여준다.


---

*Generated on 2025-09-24 04:04:08*