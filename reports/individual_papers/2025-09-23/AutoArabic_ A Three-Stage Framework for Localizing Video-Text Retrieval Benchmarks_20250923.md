---
keywords:
  - Large Language Model
  - Vision-Language Model
  - Arabic Localization
  - Error Detection Module
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16438
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:37:41.311317",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Vision-Language Model",
    "Arabic Localization",
    "Error Detection Module"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Vision-Language Model": 0.82,
    "Arabic Localization": 0.7,
    "Error Detection Module": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the framework's translation process, linking to broader NLP and AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Video-to-text retrieval",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Video-text retrieval"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept connects to the growing field of Vision-Language Models, which integrate visual and textual data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Arabic localization",
        "canonical": "Arabic Localization",
        "aliases": [
          "Arabic translation"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical focus of the paper, emphasizing the adaptation of benchmarks to the Arabic language.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Error detection module",
        "canonical": "Error Detection Module",
        "aliases": [
          "Translation error detection"
        ],
        "category": "unique_technical",
        "rationale": "The module is a novel component of the framework, crucial for ensuring translation accuracy.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "performance",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Video-to-text retrieval",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Arabic localization",
      "resolved_canonical": "Arabic Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Error detection module",
      "resolved_canonical": "Error Detection Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# AutoArabic: A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16438.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16438](https://arxiv.org/abs/2509.16438)

## 🔗 유사한 논문
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment]] (84.0% similar)
- [[2025-09-17/Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications_20250917|Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications]] (83.7% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (82.4% similar)
- [[2025-09-17/Hala Technical Report_ Building Arabic-Centric Instruction & Translation Models at Scale_20250917|Hala Technical Report: Building Arabic-Centric Instruction & Translation Models at Scale]] (82.4% similar)
- [[2025-09-23/Make Every Letter Count_ Building Dialect Variation Dictionaries from Monolingual Corpora_20250923|Make Every Letter Count: Building Dialect Variation Dictionaries from Monolingual Corpora]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Arabic Localization|Arabic Localization]], [[keywords/Error Detection Module|Error Detection Module]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16438v1 Announce Type: cross 
Abstract: Video-to-text and text-to-video retrieval are dominated by English benchmarks (e.g. DiDeMo, MSR-VTT) and recent multilingual corpora (e.g. RUDDER), yet Arabic remains underserved, lacking localized evaluation metrics. We introduce a three-stage framework, AutoArabic, utilizing state-of-the-art large language models (LLMs) to translate non-Arabic benchmarks into Modern Standard Arabic, reducing the manual revision required by nearly fourfold. The framework incorporates an error detection module that automatically flags potential translation errors with 97% accuracy. Applying the framework to DiDeMo, a video retrieval benchmark produces DiDeMo-AR, an Arabic variant with 40,144 fluent Arabic descriptions. An analysis of the translation errors is provided and organized into an insightful taxonomy to guide future Arabic localization efforts. We train a CLIP-style baseline with identical hyperparameters on the Arabic and English variants of the benchmark, finding a moderate performance gap (about 3 percentage points at Recall@1), indicating that Arabic localization preserves benchmark difficulty. We evaluate three post-editing budgets (zero/ flagged-only/ full) and find that performance improves monotonically with more post-editing, while the raw LLM output (zero-budget) remains usable. To ensure reproducibility to other languages, we made the code available at https://github.com/Tahaalshatiri/AutoArabic.

## 📝 요약

이 논문은 비디오-텍스트 및 텍스트-비디오 검색 분야에서 아랍어의 부족한 평가 기준을 해결하기 위해 AutoArabic이라는 세 단계 프레임워크를 제안합니다. 최신 대형 언어 모델(LLM)을 활용하여 비아랍어 벤치마크를 현대 표준 아랍어로 번역하며, 번역 오류를 97% 정확도로 자동 감지하는 모듈을 포함합니다. 이를 DiDeMo 벤치마크에 적용하여 40,144개의 유창한 아랍어 설명을 가진 DiDeMo-AR을 생성했습니다. 번역 오류 분석을 통해 아랍어 현지화에 대한 통찰을 제공합니다. CLIP 스타일의 베이스라인을 아랍어와 영어 버전에서 동일한 하이퍼파라미터로 훈련한 결과, 성능 차이는 약 3%포인트로, 아랍어 현지화가 벤치마크 난이도를 유지함을 보여줍니다. 다양한 후편집 예산을 평가한 결과, 후편집이 많을수록 성능이 향상되며, 원시 LLM 출력도 사용 가능함을 확인했습니다. 다른 언어로의 재현성을 위해 코드를 공개했습니다.

## 🎯 주요 포인트

- 1. AutoArabic 프레임워크는 최신 대형 언어 모델을 활용하여 비아랍어 벤치마크를 현대 표준 아랍어로 번역하며, 수작업 수정 필요성을 약 4배 줄입니다.
- 2. 이 프레임워크는 97%의 정확도로 잠재적 번역 오류를 자동으로 감지하는 오류 탐지 모듈을 포함합니다.
- 3. DiDeMo 벤치마크를 아랍어로 변환한 DiDeMo-AR은 40,144개의 유창한 아랍어 설명을 제공합니다.
- 4. 아랍어와 영어 벤치마크 간의 성능 차이는 약 3%포인트로, 아랍어 현지화가 벤치마크의 난이도를 유지함을 나타냅니다.
- 5. 후편집 예산에 따라 성능이 개선되며, 원시 LLM 출력(제로 예산)도 여전히 사용 가능합니다.


---

*Generated on 2025-09-24 03:37:41*