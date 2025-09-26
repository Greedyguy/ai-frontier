<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:46:43.825511",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Baseer",
    "Vision-Language Model",
    "Arabic Document OCR",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Baseer": 0.78,
    "Vision-Language Model": 0.85,
    "Arabic Document OCR": 0.8,
    "Multimodal Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Baseer",
        "canonical": "Baseer",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Baseer is a newly introduced vision-language model specifically designed for Arabic OCR, representing a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are a rapidly evolving concept, crucial for linking multimodal learning approaches.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Arabic Document OCR",
        "canonical": "Arabic Document OCR",
        "aliases": [
          "Arabic OCR"
        ],
        "category": "unique_technical",
        "rationale": "The focus on Arabic Document OCR highlights a specific application area, enhancing domain-specific linking.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Large Language Models are central to the paper's methodology, providing a strong basis for connecting related research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "document understanding",
      "performance",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Baseer",
      "resolved_canonical": "Baseer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Arabic Document OCR",
      "resolved_canonical": "Arabic Document OCR",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Baseer: A Vision-Language Model for Arabic Document-to-Markdown OCR

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18174.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18174](https://arxiv.org/abs/2509.18174)

## 🔗 유사한 논문
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment]] (85.6% similar)
- [[2025-09-23/AutoArabic_ A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks_20250923|AutoArabic: A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks]] (84.9% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (83.0% similar)
- [[2025-09-24/Align Where the Words Look_ Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning_20250924|Align Where the Words Look: Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning]] (81.8% similar)
- [[2025-09-17/Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications_20250917|Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Baseer|Baseer]], [[keywords/Arabic Document OCR|Arabic Document OCR]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18174v1 Announce Type: cross 
Abstract: Arabic document OCR remains a challenging task due to the language's cursive script, diverse fonts, diacritics, and right-to-left orientation. While modern Multimodal Large Language Models (MLLMs) have advanced document understanding for high-resource languages, their performance on Arabic remains limited. In this work, we introduce Baseer, a vision-language model fine- tuned specifically for Arabic document OCR. Leveraging a large-scale dataset combining synthetic and real-world documents, Baseer is trained using a decoder-only fine-tuning strategy to adapt a pre-trained MLLM while preserving general visual features. We also present Misraj-DocOCR, a high-quality, expert-verified benchmark designed for rigorous evaluation of Arabic OCR systems. Our experiments show that Baseer significantly outperforms existing open-source and commercial solutions, achieving a WER of 0.25 and establishing a new state-of-the-art in the domain of Arabic document OCR. Our results highlight the benefits of domain-specific adaptation of general-purpose MLLMs and establish a strong baseline for high-accuracy OCR on morphologically rich languages like Arabic.

## 📝 요약

이 연구는 아랍어 문서의 OCR(광학 문자 인식) 문제를 해결하기 위해 Baseer라는 비전-언어 모델을 소개합니다. Baseer는 대규모 합성 및 실제 문서 데이터셋을 활용하여 아랍어에 특화된 파인튜닝을 통해 개발되었습니다. 또한, 아랍어 OCR 시스템의 평가를 위한 고품질 벤치마크인 Misraj-DocOCR를 제시합니다. 실험 결과, Baseer는 기존의 오픈소스 및 상용 솔루션보다 뛰어난 성능을 보였으며, WER 0.25를 기록하며 아랍어 문서 OCR 분야에서 새로운 기준을 세웠습니다. 이 연구는 일반적인 MLLM의 도메인 특화 적응의 이점을 강조하며, 아랍어와 같은 형태적으로 복잡한 언어의 OCR 정확성을 높이는 강력한 기준을 제시합니다.

## 🎯 주요 포인트

- 1. 아랍어 문서 OCR은 언어의 연결된 글자체, 다양한 글꼴, 발음 구별 기호, 오른쪽에서 왼쪽으로의 방향성 때문에 여전히 어려운 과제입니다.
- 2. Baseer는 아랍어 문서 OCR을 위해 특별히 미세 조정된 비전-언어 모델로, 대규모 합성 및 실제 문서 데이터셋을 활용하여 훈련되었습니다.
- 3. Misraj-DocOCR는 아랍어 OCR 시스템의 엄격한 평가를 위해 설계된 고품질의 전문가 검증 벤치마크입니다.
- 4. Baseer는 기존의 오픈 소스 및 상용 솔루션을 능가하며, WER 0.25를 달성하여 아랍어 문서 OCR 분야에서 새로운 최첨단 성과를 세웠습니다.
- 5. 본 연구는 범용 MLLM의 도메인 특화 적응의 이점을 강조하며, 아랍어와 같은 형태적으로 풍부한 언어에 대한 높은 정확도의 OCR을 위한 강력한 기준을 확립합니다.


---

*Generated on 2025-09-24 15:46:43*