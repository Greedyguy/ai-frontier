---
keywords:
  - Machine Translation
  - Large Language Model
  - Translation Evaluation
  - Model Rotation
  - xCOMET
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19611
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:43:58.287973",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Translation",
    "Large Language Model",
    "Translation Evaluation",
    "Model Rotation",
    "xCOMET"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Translation": 0.82,
    "Large Language Model": 0.8,
    "Translation Evaluation": 0.78,
    "Model Rotation": 0.77,
    "xCOMET": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "machine translation systems",
        "canonical": "Machine Translation",
        "aliases": [
          "MT",
          "translation systems"
        ],
        "category": "specific_connectable",
        "rationale": "Machine Translation is a key area within NLP and connects well with translation evaluation tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "language models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on translation evaluation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "translation evaluation",
        "canonical": "Translation Evaluation",
        "aliases": [
          "evaluation of translation",
          "translation quality assessment"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical concept central to the paper's methodology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "model rotation",
        "canonical": "Model Rotation",
        "aliases": [
          "rotation of models"
        ],
        "category": "unique_technical",
        "rationale": "Model rotation is a specific technique introduced in the paper, relevant for linking novel methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "xCOMET",
        "canonical": "xCOMET",
        "aliases": [
          "COMET",
          "xCOMET evaluation"
        ],
        "category": "unique_technical",
        "rationale": "xCOMET is a specific evaluation system used as a benchmark in the study.",
        "novelty_score": 0.68,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "quality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "machine translation systems",
      "resolved_canonical": "Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "translation evaluation",
      "resolved_canonical": "Translation Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "model rotation",
      "resolved_canonical": "Model Rotation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "xCOMET",
      "resolved_canonical": "xCOMET",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Evaluating Language Translation Models by Playing Telephone

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19611.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19611](https://arxiv.org/abs/2509.19611)

## 🔗 유사한 논문
- [[2025-09-18/Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality_20250918|Audio-Based Crowd-Sourced Evaluation of Machine Translation Quality]] (85.3% similar)
- [[2025-09-23/Extending Automatic Machine Translation Evaluation to Book-Length Documents_20250923|Extending Automatic Machine Translation Evaluation to Book-Length Documents]] (85.0% similar)
- [[2025-09-17/Long-context Reference-based MT Quality Estimation_20250917|Long-context Reference-based MT Quality Estimation]] (84.8% similar)
- [[2025-09-24/Please Translate Again_ Two Simple Experiments on Whether Human-Like Reasoning Helps Translation_20250924|Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation]] (84.4% similar)
- [[2025-09-25/Feeding Two Birds or Favoring One? Adequacy-Fluency Tradeoffs in Evaluation and Meta-Evaluation of Machine Translation_20250925|Feeding Two Birds or Favoring One? Adequacy-Fluency Tradeoffs in Evaluation and Meta-Evaluation of Machine Translation]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Machine Translation|Machine Translation]]
**⚡ Unique Technical**: [[keywords/Translation Evaluation|Translation Evaluation]], [[keywords/Model Rotation|Model Rotation]], [[keywords/xCOMET|xCOMET]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19611v1 Announce Type: new 
Abstract: Our ability to efficiently and accurately evaluate the quality of machine translation systems has been outrun by the effectiveness of current language models--which limits the potential for further improving these models on more challenging tasks like long-form and literary translation. We propose an unsupervised method to generate training data for translation evaluation over different document lengths and application domains by repeated rounds of translation between source and target languages. We evaluate evaluation systems trained on texts mechanically generated using both model rotation and language translation approaches, demonstrating improved performance over a popular translation evaluation system (xCOMET) on two different tasks: (i) scoring the quality of a given translation against a human reference and (ii) selecting which of two translations is generationally closer to an original source document.

## 📝 요약

이 논문은 기계 번역 시스템의 품질 평가를 개선하기 위한 새로운 비지도 학습 방법을 제안합니다. 기존 언어 모델의 효과가 뛰어나지만, 장문 및 문학 번역과 같은 더 어려운 작업에서의 개선 가능성을 제한하고 있습니다. 제안된 방법은 원문과 번역문 간의 반복 번역을 통해 다양한 문서 길이와 응용 분야에 대한 훈련 데이터를 생성합니다. 이 방법은 모델 회전 및 언어 번역 접근법을 사용하여 기계적으로 생성된 텍스트로 훈련된 평가 시스템의 성능을 평가하며, 인기 있는 번역 평가 시스템인 xCOMET보다 두 가지 작업에서 더 나은 성능을 보였습니다: (i) 주어진 번역의 품질을 인간 참조와 비교하여 평가하는 것과 (ii) 두 번역 중 원본 문서에 더 가까운 번역을 선택하는 것입니다.

## 🎯 주요 포인트

- 1. 현재 언어 모델의 효과성은 기계 번역 시스템의 품질 평가 능력을 초과하고 있어, 장문 및 문학 번역과 같은 더 도전적인 작업에서 모델 개선의 잠재력을 제한하고 있다.
- 2. 우리는 소스와 타겟 언어 간의 반복 번역을 통해 다양한 문서 길이와 응용 분야에 대한 번역 평가 훈련 데이터를 생성하는 비지도 학습 방법을 제안한다.
- 3. 모델 회전 및 언어 번역 접근 방식을 사용하여 기계적으로 생성된 텍스트로 훈련된 평가 시스템은 인기 있는 번역 평가 시스템(xCOMET)보다 두 가지 작업에서 향상된 성능을 보여준다.
- 4. 제안된 시스템은 주어진 번역의 품질을 인간 참조와 비교하여 평가하고, 두 번역 중 원본 소스 문서에 더 가까운 번역을 선택하는 작업에서 성능을 입증한다.


---

*Generated on 2025-09-26 08:43:58*