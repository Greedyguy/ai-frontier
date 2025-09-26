---
keywords:
  - Electronic Health Applications
  - Privacy Concerns
  - Trust in Applications
  - Machine Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.19268
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:05:29.962543",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Electronic Health Applications",
    "Privacy Concerns",
    "Trust in Applications",
    "Machine Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Electronic Health Applications": 0.78,
    "Privacy Concerns": 0.8,
    "Trust in Applications": 0.82,
    "Machine Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Electronic Health Apps",
        "canonical": "Electronic Health Applications",
        "aliases": [
          "eHealth Apps",
          "Health Apps"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on privacy and trust in digital health, offering a unique domain for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Privacy Concerns",
        "canonical": "Privacy Concerns",
        "aliases": [
          "Data Privacy Issues",
          "Privacy Issues"
        ],
        "category": "specific_connectable",
        "rationale": "Privacy concerns are a key aspect of user trust in digital applications, providing strong links to privacy research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Trust in Applications",
        "canonical": "Trust in Applications",
        "aliases": [
          "Application Trust",
          "App Trust"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding trust in applications is crucial for user acceptance and is a specific focus of the dataset.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Machine Learning Models",
        "canonical": "Machine Learning",
        "aliases": [
          "ML Models",
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine learning models are fundamental to the analysis and benchmarking described in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "user reviews",
      "annotated corpus"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Electronic Health Apps",
      "resolved_canonical": "Electronic Health Applications",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Privacy Concerns",
      "resolved_canonical": "Privacy Concerns",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Trust in Applications",
      "resolved_canonical": "Trust in Applications",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Machine Learning Models",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# HARPT: A Corpus for Analyzing Consumers' Trust and Privacy Concerns in Electronic Health Apps

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.19268.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.19268](https://arxiv.org/abs/2506.19268)

## 🔗 유사한 논문
- [[2025-09-18/Can I Trust This Chatbot? Assessing User Privacy in AI-Healthcare Chatbot Applications_20250918|Can I Trust This Chatbot? Assessing User Privacy in AI-Healthcare Chatbot Applications]] (80.3% similar)
- [[2025-09-23/"What's Up, Doc?"_ Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets_20250923|"What's Up, Doc?": Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets]] (80.1% similar)
- [[2025-09-23/A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents_20250923|A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents]] (78.7% similar)
- [[2025-09-22/The Anatomy of a Personal Health Agent_20250922|The Anatomy of a Personal Health Agent]] (78.5% similar)
- [[2025-09-23/The Good, the Bad and the Constructive_ Automatically Measuring Peer Review's Utility for Authors_20250923|The Good, the Bad and the Constructive: Automatically Measuring Peer Review's Utility for Authors]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Privacy Concerns|Privacy Concerns]], [[keywords/Trust in Applications|Trust in Applications]]
**⚡ Unique Technical**: [[keywords/Electronic Health Applications|Electronic Health Applications]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.19268v3 Announce Type: replace-cross 
Abstract: We present Health App Reviews for Privacy & Trust (HARPT), a large-scale annotated corpus of user reviews from Electronic Health (eHealth) applications (apps) aimed at advancing research in user privacy and trust. The dataset comprises 480K user reviews labeled in seven categories that capture critical aspects of trust in applications (TA), trust in providers (TP), and privacy concerns (PC). Our multistage strategy integrated keyword-based filtering, iterative manual labeling with review, targeted data augmentation, and weak supervision using transformer-based classifiers. In parallel, we manually annotated a curated subset of 7,000 reviews to support the development and evaluation of machine learning models. We benchmarked a broad range of models, providing a baseline for future work. HARPT is released under an open resource license to support reproducible research in usable privacy and trust in digital libraries and health informatics.

## 📝 요약

이 논문은 사용자 프라이버시와 신뢰 연구를 위한 대규모 주석 코퍼스인 HARPT를 소개합니다. 이 데이터셋은 전자 건강 애플리케이션의 사용자 리뷰 48만 건을 7개 범주로 분류하여 애플리케이션 및 제공자에 대한 신뢰와 프라이버시 우려를 다룹니다. 키워드 기반 필터링, 반복적 수동 라벨링, 데이터 증강, 트랜스포머 기반 분류기를 활용한 약한 지도 학습을 통해 구축되었습니다. 또한, 7,000개의 리뷰를 수동으로 주석 처리하여 기계 학습 모델 개발 및 평가를 지원했습니다. 다양한 모델을 벤치마킹하여 향후 연구의 기준을 제시했으며, HARPT는 디지털 라이브러리와 건강 정보학에서 재현 가능한 연구를 지원하기 위해 공개 자원 라이선스로 배포됩니다.

## 🎯 주요 포인트

- 1. HARPT는 전자 건강 애플리케이션의 사용자 리뷰를 분석하여 사용자 프라이버시와 신뢰 연구를 발전시키기 위한 대규모 주석 코퍼스입니다.
- 2. 데이터셋은 애플리케이션 신뢰, 제공자 신뢰, 프라이버시 우려를 포착하는 7개 범주로 레이블링된 48만 개의 사용자 리뷰로 구성되어 있습니다.
- 3. 키워드 기반 필터링, 반복적인 수동 레이블링, 데이터 증강, 트랜스포머 기반 분류기를 활용한 약한 감독을 통합한 다단계 전략을 사용했습니다.
- 4. 기계 학습 모델 개발 및 평가를 지원하기 위해 7,000개의 리뷰를 수동으로 주석 처리했습니다.
- 5. HARPT는 디지털 도서관과 건강 정보학에서 재현 가능한 연구를 지원하기 위해 오픈 리소스 라이선스로 공개되었습니다.


---

*Generated on 2025-09-24 03:05:29*