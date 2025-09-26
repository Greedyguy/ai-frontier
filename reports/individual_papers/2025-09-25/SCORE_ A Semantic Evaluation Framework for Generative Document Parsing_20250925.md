---
keywords:
  - Generative Document Parsing
  - SCORE Framework
  - Semantic Alignment
  - Interpretive Diversity
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19345
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:27:44.315408",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Document Parsing",
    "SCORE Framework",
    "Semantic Alignment",
    "Interpretive Diversity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generative Document Parsing": 0.78,
    "SCORE Framework": 0.82,
    "Semantic Alignment": 0.77,
    "Interpretive Diversity": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "generative document parsing",
        "canonical": "Generative Document Parsing",
        "aliases": [
          "document parsing",
          "generative parsing"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specialized approach in document analysis, linking to discussions on generative models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "SCORE",
        "canonical": "SCORE Framework",
        "aliases": [
          "Structural and Content Robust Evaluation"
        ],
        "category": "unique_technical",
        "rationale": "As a new evaluation framework, it provides a unique perspective on document parsing, linking to evaluation methodologies.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "semantic alignment",
        "canonical": "Semantic Alignment",
        "aliases": [
          "alignment",
          "semantic matching"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding how different document interpretations can be evaluated for semantic consistency.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "interpretive diversity",
        "canonical": "Interpretive Diversity",
        "aliases": [
          "interpretation diversity",
          "diverse interpretations"
        ],
        "category": "unique_technical",
        "rationale": "This term highlights the variability in document parsing outputs, linking to discussions on evaluation challenges.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "performance",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "generative document parsing",
      "resolved_canonical": "Generative Document Parsing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SCORE",
      "resolved_canonical": "SCORE Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "semantic alignment",
      "resolved_canonical": "Semantic Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "interpretive diversity",
      "resolved_canonical": "Interpretive Diversity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SCORE: A Semantic Evaluation Framework for Generative Document Parsing

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19345.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19345](https://arxiv.org/abs/2509.19345)

## 🔗 유사한 논문
- [[2025-09-23/RadEval_ A framework for radiology text evaluation_20250923|RadEval: A framework for radiology text evaluation]] (82.6% similar)
- [[2025-09-24/HSGM_ Hierarchical Segment-Graph Memory for Scalable Long-Text Semantics_20250924|HSGM: Hierarchical Segment-Graph Memory for Scalable Long-Text Semantics]] (81.2% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (80.7% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (80.7% similar)
- [[2025-09-25/Score the Steps, Not Just the Goal_ VLM-Based Subgoal Evaluation for Robotic Manipulation_20250925|Score the Steps, Not Just the Goal: VLM-Based Subgoal Evaluation for Robotic Manipulation]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic Alignment|Semantic Alignment]]
**⚡ Unique Technical**: [[keywords/Generative Document Parsing|Generative Document Parsing]], [[keywords/SCORE Framework|SCORE Framework]], [[keywords/Interpretive Diversity|Interpretive Diversity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19345v1 Announce Type: cross 
Abstract: Multi-modal generative document parsing systems challenge traditional evaluation: unlike deterministic OCR or layout models, they often produce semantically correct yet structurally divergent outputs. Conventional metrics-CER, WER, IoU, or TEDS-misclassify such diversity as error, penalizing valid interpretations and obscuring system behavior.
  We introduce SCORE (Structural and COntent Robust Evaluation), an interpretation-agnostic framework that integrates (i) adjusted edit distance for robust content fidelity, (ii) token-level diagnostics to distinguish hallucinations from omissions, (iii) table evaluation with spatial tolerance and semantic alignment, and (iv) hierarchy-aware consistency checks. Together, these dimensions enable evaluation that embraces representational diversity while enforcing semantic rigor.
  Across 1,114 pages spanning a holistic benchmark and a field dataset, SCORE consistently revealed cross-dataset performance patterns missed by standard metrics. In 2-5% of pages with ambiguous table structures, traditional metrics penalized systems by 12-25% on average, leading to distorted rankings. SCORE corrected these cases, recovering equivalence between alternative but valid interpretations. Moreover, by normalizing generative outputs into a format-agnostic representation, SCORE reproduces traditional scores (e.g., table F1 up to 0.93) without requiring object-detection pipelines, demonstrating that generative parsing alone suffices for comprehensive evaluation.
  By exposing how interpretive diversity impacts evaluation outcomes and providing multi-dimensional, interpretable diagnostics, SCORE establishes foundational principles for semantically grounded, fair, and practical benchmarking of modern document parsing systems.

## 📝 요약

이 논문은 전통적인 평가 방식이 아닌, 다중 모달 생성 문서 파싱 시스템을 위한 새로운 평가 프레임워크인 SCORE를 제안합니다. 기존의 평가 지표는 다양한 해석을 오류로 간주하여 시스템의 성능을 왜곡할 수 있습니다. SCORE는 조정된 편집 거리, 토큰 수준 진단, 공간적 관용성을 고려한 표 평가, 계층 인식 일관성 검사를 통합하여 이러한 문제를 해결합니다. 1,114페이지에 걸친 실험에서 SCORE는 기존 지표가 놓친 성능 패턴을 발견했으며, 모호한 구조를 가진 페이지에서의 왜곡된 평가를 수정했습니다. 이로써 SCORE는 현대 문서 파싱 시스템의 공정하고 실용적인 벤치마킹을 위한 기본 원칙을 확립합니다.

## 🎯 주요 포인트

- 1. SCORE는 전통적인 평가 방식이 간과하는 해석적 다양성을 포용하면서도 의미적 엄격성을 유지하는 평가 프레임워크를 제공합니다.
- 2. SCORE는 조정된 편집 거리, 토큰 수준 진단, 공간적 관용과 의미적 정렬을 갖춘 테이블 평가, 계층 인식 일관성 검사를 통합합니다.
- 3. SCORE는 1,114페이지에 걸친 벤치마크와 필드 데이터셋에서 전통적인 메트릭이 놓친 성능 패턴을 일관되게 드러냈습니다.
- 4. SCORE는 포맷에 구애받지 않는 표현으로 생성된 출력을 정규화하여 전통적인 점수를 재현하며, 객체 탐지 파이프라인 없이도 포괄적인 평가가 가능함을 보여줍니다.
- 5. SCORE는 현대 문서 파싱 시스템의 의미적으로 기반을 둔 공정하고 실용적인 벤치마킹을 위한 기초 원칙을 확립합니다.


---

*Generated on 2025-09-25 15:27:44*