---
keywords:
  - Few-Shot Learning
  - Large Language Model
  - Weak Supervision
  - Pseudo-Label Correction
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2410.01508
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:16:16.185455",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Large Language Model",
    "Weak Supervision",
    "Pseudo-Label Correction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.85,
    "Large Language Model": 0.8,
    "Weak Supervision": 0.78,
    "Pseudo-Label Correction": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "In-Context Learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "ICL"
        ],
        "category": "specific_connectable",
        "rationale": "In-Context Learning is a form of Few-Shot Learning, which is crucial for linking to related concepts in learning paradigms.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and application of In-Context Learning, providing a strong link to related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Weak Supervision",
        "canonical": "Weak Supervision",
        "aliases": [
          "Weakly Supervised Learning"
        ],
        "category": "unique_technical",
        "rationale": "Weak Supervision is a key concept in the paper's methodology, offering a unique perspective on learning paradigms.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pseudo-Label Correction",
        "canonical": "Pseudo-Label Correction",
        "aliases": [
          "Pseudo-Labeling"
        ],
        "category": "unique_technical",
        "rationale": "Pseudo-Label Correction is a novel approach in the paper, enhancing the understanding of label refinement processes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "In-Context Learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Weak Supervision",
      "resolved_canonical": "Weak Supervision",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pseudo-Label Correction",
      "resolved_canonical": "Pseudo-Label Correction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Disentangling Latent Shifts of In-Context Learning with Weak Supervision

**Korean Title:** 맥락 내 학습의 잠재적 변화 분리를 약한 감독으로 해결하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2410.01508.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2410.01508](https://arxiv.org/abs/2410.01508)

## 🔗 유사한 논문
- [[2025-09-22/KITE_ Kernelized and Information Theoretic Exemplars for In-Context Learning_20250922|KITE: Kernelized and Information Theoretic Exemplars for In-Context Learning]] (85.6% similar)
- [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL: Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (81.4% similar)
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (81.2% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (80.9% similar)
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Weak Supervision|Weak Supervision]], [[keywords/Pseudo-Label Correction|Pseudo-Label Correction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.01508v2 Announce Type: replace-cross 
Abstract: In-context learning (ICL) enables large language models to perform few-shot learning by conditioning on labeled examples in the prompt. Despite its flexibility, ICL suffers from instability -- especially as prompt length increases with more demonstrations. To address this, we treat ICL as a source of weak supervision and propose a parameter-efficient method that disentangles demonstration-induced latent shifts from those of the query. An ICL-based teacher generates pseudo-labels on unlabeled queries, while a student predicts them using only the query input, updating a lightweight adapter. This captures demonstration effects in a compact, reusable form, enabling efficient inference while remaining composable with new demonstrations. Although trained on noisy teacher outputs, the student often outperforms its teacher through pseudo-label correction and coverage expansion, consistent with the weak-to-strong generalization effect. Empirically, our method improves generalization, stability, and efficiency across both in-domain and out-of-domain tasks, surpassing standard ICL and prior disentanglement methods.

## 🔍 Abstract (한글 번역)

arXiv:2410.01508v2 발표 유형: 교차 대체  
초록: 맥락 내 학습(ICL)은 대형 언어 모델이 프롬프트에서 레이블이 있는 예시를 조건으로 하여 몇 가지 샷 학습을 수행할 수 있게 합니다. 그 유연성에도 불구하고, ICL은 불안정성 문제를 겪습니다. 특히, 더 많은 데모가 포함되어 프롬프트 길이가 길어질수록 이러한 문제가 두드러집니다. 이를 해결하기 위해, 우리는 ICL을 약한 감독의 원천으로 간주하고, 데모에 의해 유도된 잠재적 변화를 쿼리의 변화와 분리하는 파라미터 효율적인 방법을 제안합니다. ICL 기반의 교사는 레이블이 없는 쿼리에 대해 가짜 레이블을 생성하고, 학생은 쿼리 입력만을 사용하여 이를 예측하며, 경량 어댑터를 업데이트합니다. 이는 데모 효과를 간결하고 재사용 가능한 형태로 포착하여, 새로운 데모와 조합 가능하면서도 효율적인 추론을 가능하게 합니다. 비록 교사의 출력이 노이즈가 많더라도, 학생은 종종 가짜 레이블 수정과 범위 확장을 통해 교사를 능가하며, 이는 약한 감독에서 강한 일반화로의 효과와 일치합니다. 실증적으로, 우리의 방법은 도메인 내 및 도메인 외 과제 전반에서 일반화, 안정성 및 효율성을 향상시켜, 표준 ICL 및 이전의 분리 방법을 능가합니다.

## 📝 요약

이 논문은 대형 언어 모델의 불안정성을 해결하기 위해 ICL(문맥 내 학습)을 약한 감독의 원천으로 활용하는 방법을 제안합니다. 제안된 방법은 시연으로 인한 잠재적 변화를 질의로부터 분리하여 처리하며, ICL 기반 교사가 비표시된 질의에 대해 생성한 가짜 레이블을 학생 모델이 경량 어댑터를 통해 예측합니다. 이 과정에서 학생 모델은 교사의 출력보다 더 나은 성능을 보이며, 이는 약한 감독에서 강한 일반화로의 전환 효과를 반영합니다. 실험 결과, 제안된 방법은 기존 ICL 및 이전 분리 방법보다 더 나은 일반화, 안정성, 효율성을 제공합니다.

## 🎯 주요 포인트

- 1. ICL(문맥 학습)은 레이블이 있는 예제를 프롬프트에 조건으로 사용하여 대형 언어 모델이 소수의 샷 학습을 수행할 수 있게 합니다.
- 2. ICL은 유연성에도 불구하고 프롬프트 길이가 증가할수록 불안정성이 커지는 문제를 겪습니다.
- 3. 제안된 방법은 ICL을 약한 감독의 원천으로 보고, 시연으로 인한 잠재적 변화를 쿼리의 변화와 분리하는 파라미터 효율적인 방법을 제안합니다.
- 4. ICL 기반 교사는 레이블이 없는 쿼리에 대해 가짜 레이블을 생성하고, 학생은 쿼리 입력만으로 이를 예측하여 경량 어댑터를 업데이트합니다.
- 5. 제안된 방법은 일반화, 안정성, 효율성을 개선하며, 표준 ICL 및 이전의 분리 방법을 능가합니다.


---

*Generated on 2025-09-23 11:16:16*