---
keywords:
  - Large Language Model
  - Watermarking
  - Medical Factuality
  - Factuality-Weighted Score
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.07755
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:11:11.185943",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Watermarking",
    "Medical Factuality",
    "Factuality-Weighted Score"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Watermarking": 0.78,
    "Medical Factuality": 0.8,
    "Factuality-Weighted Score": 0.77
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
        "rationale": "Essential for linking discussions about AI applications in sensitive domains like medicine.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Watermarking",
        "canonical": "Watermarking",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus on ensuring text integrity and accountability in medical applications.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Medical Factuality",
        "canonical": "Medical Factuality",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Highlights the specific challenge of maintaining factual accuracy in medical texts.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Factuality-Weighted Score",
        "canonical": "Factuality-Weighted Score",
        "aliases": [
          "FWS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel metric for evaluating watermarking effectiveness in medical texts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "evaluation",
      "workflow"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Watermarking",
      "resolved_canonical": "Watermarking",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Medical Factuality",
      "resolved_canonical": "Medical Factuality",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Factuality-Weighted Score",
      "resolved_canonical": "Factuality-Weighted Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Factuality Beyond Coherence: Evaluating LLM Watermarking Methods for Medical Texts

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.07755.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.07755](https://arxiv.org/abs/2509.07755)

## 🔗 유사한 논문
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (84.3% similar)
- [[2025-09-22/VLA-Mark_ A cross modal watermark for large vision-language alignment model_20250922|VLA-Mark: A cross modal watermark for large vision-language alignment model]] (83.6% similar)
- [[2025-09-19/MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1: Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (83.5% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (83.1% similar)
- [[2025-09-23/MedFact_ A Large-scale Chinese Dataset for Evidence-based Medical Fact-checking of LLM Responses_20250923|MedFact: A Large-scale Chinese Dataset for Evidence-based Medical Fact-checking of LLM Responses]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Watermarking|Watermarking]], [[keywords/Medical Factuality|Medical Factuality]], [[keywords/Factuality-Weighted Score|Factuality-Weighted Score]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07755v2 Announce Type: replace 
Abstract: As large language models (LLMs) are adapted to sensitive domains such as medicine, their fluency raises safety risks, particularly regarding provenance and accountability. Watermarking embeds detectable patterns to mitigate these risks, yet its reliability in medical contexts remains untested. Existing benchmarks focus on detection-quality tradeoffs and overlook factual risks. In medical text, watermarking often reweights low-entropy tokens, which are highly predictable and often carry critical medical terminology. Shifting these tokens can cause inaccuracy and hallucinations, risks that prior general-domain benchmarks fail to capture.
  We propose a medical-focused evaluation workflow that jointly assesses factual accuracy and coherence. Using GPT-Judger and further human validation, we introduce the Factuality-Weighted Score (FWS), a composite metric prioritizing factual accuracy beyond coherence to guide watermarking deployment in medical domains. Our evaluation shows current watermarking methods substantially compromise medical factuality, with entropy shifts degrading medical entity representation. These findings underscore the need for domain-aware watermarking approaches that preserve the integrity of medical content.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 의료 분야에 적용될 때 발생할 수 있는 안전성 문제를 다룹니다. 특히, 워터마킹 기법이 의료 분야에서의 신뢰성을 검증받지 못한 상황에서, 이 기법이 의료 텍스트의 정확성과 일관성을 저해할 수 있음을 지적합니다. 기존 벤치마크는 사실적 위험을 간과하고 있으며, 워터마킹이 낮은 엔트로피를 가진 예측 가능한 의료 용어를 재조정함으로써 부정확성과 환각을 초래할 수 있음을 강조합니다. 이를 해결하기 위해, 사실적 정확성과 일관성을 동시에 평가하는 의료 중심의 평가 워크플로우를 제안하며, 사실적 정확성을 우선시하는 Factuality-Weighted Score(FWS)를 도입했습니다. 연구 결과, 현재의 워터마킹 방법이 의료 정보의 정확성을 크게 저해함을 보여주며, 의료 콘텐츠의 무결성을 보존하기 위한 도메인 인식 워터마킹 접근법의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 의료 분야 적용 시, 유창성으로 인해 출처 및 책임 문제와 같은 안전 위험이 발생할 수 있다.
- 2. 워터마킹은 이러한 위험을 완화하기 위해 탐지 가능한 패턴을 삽입하지만, 의료 분야에서의 신뢰성은 검증되지 않았다.
- 3. 기존 벤치마크는 탐지 품질의 트레이드오프에 중점을 두며 사실적 위험을 간과한다.
- 4. 의료 텍스트에서 워터마킹은 종종 낮은 엔트로피 토큰을 재배치하여 중요한 의료 용어의 부정확성과 환각을 초래할 수 있다.
- 5. 제안된 평가 워크플로우는 사실적 정확성과 일관성을 함께 평가하며, 현재 워터마킹 방법이 의료 사실성을 크게 훼손함을 보여준다.


---

*Generated on 2025-09-24 04:11:11*