---
keywords:
  - Large Language Model
  - Low-Resource Machine Translation
  - SynOPUS Repository
  - Document-Level Synthetic Corpus
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.14423
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:56:22.170860",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Low-Resource Machine Translation",
    "SynOPUS Repository",
    "Document-Level Synthetic Corpus"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Low-Resource Machine Translation": 0.78,
    "SynOPUS Repository": 0.8,
    "Document-Level Synthetic Corpus": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-generated synthetic data",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "synthetic data from LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Links to existing discussions on the use of Large Language Models in data generation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "low-resource Machine Translation",
        "canonical": "Low-Resource Machine Translation",
        "aliases": [
          "low-resource MT"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on a niche area within Machine Translation, enhancing connectivity with related research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SynOPUS",
        "canonical": "SynOPUS Repository",
        "aliases": [
          "SynOPUS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new resource for synthetic parallel datasets, relevant for future dataset discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "document-level synthetic corpus",
        "canonical": "Document-Level Synthetic Corpus",
        "aliases": [
          "synthetic corpus"
        ],
        "category": "specific_connectable",
        "rationale": "Provides a detailed focus on corpus-level data generation, useful for corpus-based studies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "improving",
      "evaluation",
      "training regimes",
      "effect",
      "utility"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-generated synthetic data",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "low-resource Machine Translation",
      "resolved_canonical": "Low-Resource Machine Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SynOPUS",
      "resolved_canonical": "SynOPUS Repository",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "document-level synthetic corpus",
      "resolved_canonical": "Document-Level Synthetic Corpus",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Scaling Low-Resource MT via Synthetic Data Generation with LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.14423.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.14423](https://arxiv.org/abs/2505.14423)

## 🔗 유사한 논문
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (88.5% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (84.9% similar)
- [[2025-09-22/LiteLong_ Resource-Efficient Long-Context Data Synthesis for LLMs_20250922|LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs]] (83.3% similar)
- [[2025-09-22/Frustratingly Easy Data Augmentation for Low-Resource ASR_20250922|Frustratingly Easy Data Augmentation for Low-Resource ASR]] (83.1% similar)
- [[2025-09-23/XL-Suite_ Cross-Lingual Synthetic Training and Evaluation Data for Open-Ended Generation_20250923|XL-Suite: Cross-Lingual Synthetic Training and Evaluation Data for Open-Ended Generation]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Document-Level Synthetic Corpus|Document-Level Synthetic Corpus]]
**⚡ Unique Technical**: [[keywords/Low-Resource Machine Translation|Low-Resource Machine Translation]], [[keywords/SynOPUS Repository|SynOPUS Repository]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14423v2 Announce Type: replace 
Abstract: We investigate the potential of LLM-generated synthetic data for improving low-resource Machine Translation (MT). Focusing on seven diverse target languages, we construct a document-level synthetic corpus from English Europarl, and extend it via pivoting to 147 additional language pairs. Automatic and human evaluation confirm its overall high quality. We study its practical application by (i) identifying effective training regimes, (ii) comparing our data with the HPLT dataset, (iii) studying the effect of varying training data size, and (iiii) testing its utility beyond English-centric MT. Finally, we introduce SynOPUS, a public repository for synthetic parallel datasets. Our findings show that LLM-generated synthetic data, even when noisy, can substantially improve MT performance for low-resource languages.

## 📝 요약

이 논문은 LLM이 생성한 합성 데이터가 저자원 기계 번역(MT)의 성능을 향상시킬 수 있는 가능성을 조사합니다. 영어 Europarl에서 문서 수준의 합성 코퍼스를 생성하고, 이를 피벗 기법을 통해 147개의 추가 언어 쌍으로 확장했습니다. 자동 및 인간 평가를 통해 데이터의 전반적인 높은 품질을 확인했습니다. 효과적인 훈련 방법 식별, HPLT 데이터셋과의 비교, 훈련 데이터 크기 변화의 영향, 영어 중심이 아닌 MT에서의 유용성을 테스트했습니다. 최종적으로 합성 병렬 데이터셋을 위한 공개 저장소인 SynOPUS를 소개합니다. 연구 결과, LLM이 생성한 합성 데이터는 노이즈가 있더라도 저자원 언어의 MT 성능을 크게 향상시킬 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. LLM이 생성한 합성 데이터는 저자원 기계 번역 성능을 크게 향상시킬 수 있다.
- 2. 영어 Europarl로부터 문서 수준의 합성 코퍼스를 구축하고, 이를 피벗하여 147개의 추가 언어 쌍으로 확장하였다.
- 3. 자동 및 인간 평가를 통해 합성 데이터의 전반적인 높은 품질을 확인하였다.
- 4. 다양한 훈련 데이터 크기의 효과를 연구하고, 영어 중심의 기계 번역을 넘어서 합성 데이터의 유용성을 테스트하였다.
- 5. SynOPUS라는 합성 병렬 데이터셋의 공개 저장소를 소개하였다.


---

*Generated on 2025-09-24 03:56:22*