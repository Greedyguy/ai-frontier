<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:21:47.461602",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Outcome-Based Educational Recommender",
    "Collaborative Filtering",
    "Knowledge-Based Filtering",
    "Mastery Formula"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Outcome-Based Educational Recommender": 0.78,
    "Collaborative Filtering": 0.8,
    "Knowledge-Based Filtering": 0.72,
    "Mastery Formula": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Outcome-Based Educational Recommender",
        "canonical": "Outcome-Based Educational Recommender",
        "aliases": [
          "OBER"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper, integrating learning outcomes into recommender systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Collaborative Filtering",
        "canonical": "Collaborative Filtering",
        "aliases": [
          "CF"
        ],
        "category": "broad_technical",
        "rationale": "Collaborative Filtering is a widely used technique in recommender systems, facilitating connections to other works in the field.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Knowledge-Based Filtering",
        "canonical": "Knowledge-Based Filtering",
        "aliases": [
          "KB Filtering"
        ],
        "category": "specific_connectable",
        "rationale": "Knowledge-Based Filtering is a specific method that can be linked to other knowledge-based systems in educational technology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Mastery Formula",
        "canonical": "Mastery Formula",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The mastery formula is a unique aspect of the system, crucial for evaluating learning outcomes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "e-learning system",
      "randomized split test",
      "fixed expert trajectory"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Outcome-Based Educational Recommender",
      "resolved_canonical": "Outcome-Based Educational Recommender",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Collaborative Filtering",
      "resolved_canonical": "Collaborative Filtering",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Knowledge-Based Filtering",
      "resolved_canonical": "Knowledge-Based Filtering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Mastery Formula",
      "resolved_canonical": "Mastery Formula",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# An Outcome-Based Educational Recommender System

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18186.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18186](https://arxiv.org/abs/2509.18186)

## 🔗 유사한 논문
- [[2025-09-22/Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom_20250922|Learning Analytics from Spoken Discussion Dialogs in Flipped Classroom]] (77.6% similar)
- [[2025-09-19/Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems_20250919|Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems]] (77.5% similar)
- [[2025-09-22/Latent learning_ episodic memory complements parametric learning by enabling flexible reuse of experiences_20250922|Latent learning: episodic memory complements parametric learning by enabling flexible reuse of experiences]] (77.1% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment]] (77.0% similar)
- [[2025-09-19/SMART_ Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction_20250919|SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction]] (76.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Collaborative Filtering|Collaborative Filtering]]
**🔗 Specific Connectable**: [[keywords/Knowledge-Based Filtering|Knowledge-Based Filtering]]
**⚡ Unique Technical**: [[keywords/Outcome-Based Educational Recommender|Outcome-Based Educational Recommender]], [[keywords/Mastery Formula|Mastery Formula]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18186v1 Announce Type: new 
Abstract: Most educational recommender systems are tuned and judged on click- or rating-based relevance, leaving their true pedagogical impact unclear. We introduce OBER-an Outcome-Based Educational Recommender that embeds learning outcomes and assessment items directly into the data schema, so any algorithm can be evaluated on the mastery it fosters. OBER uses a minimalist entity-relation model, a log-driven mastery formula, and a plug-in architecture. Integrated into an e-learning system in non-formal domain, it was evaluated trough a two-week randomized split test with over 5 700 learners across three methods: fixed expert trajectory, collaborative filtering (CF), and knowledge-based (KB) filtering. CF maximized retention, but the fixed path achieved the highest mastery. Because OBER derives business, relevance, and learning metrics from the same logs, it lets practitioners weigh relevance and engagement against outcome mastery with no extra testing overhead. The framework is method-agnostic and readily extensible to future adaptive or context-aware recommenders.

## 📝 요약

이 논문은 교육 추천 시스템의 교육적 효과를 명확히 평가하기 위해 OBER라는 결과 기반 교육 추천 시스템을 소개합니다. OBER는 학습 결과와 평가 항목을 데이터 스키마에 직접 포함시켜 알고리즘이 학습 성취도를 평가할 수 있도록 합니다. 이 시스템은 최소한의 엔티티-관계 모델, 로그 기반 성취도 공식, 플러그인 아키텍처를 사용합니다. 비형식 교육 분야의 e-러닝 시스템에 통합되어 5,700명 이상의 학습자를 대상으로 2주간 무작위 분할 테스트를 통해 평가되었습니다. 고정 경로가 가장 높은 성취도를 보였고, 협업 필터링(CF)은 학습자 유지율을 극대화했습니다. OBER는 동일한 로그에서 비즈니스, 관련성, 학습 지표를 도출하여 추가 테스트 없이 관련성과 참여도를 성취도와 비교할 수 있게 합니다. 이 프레임워크는 방법론에 구애받지 않으며, 향후 적응형 또는 상황 인식 추천 시스템에 쉽게 확장 가능합니다.

## 🎯 주요 포인트

- 1. OBER는 학습 결과와 평가 항목을 데이터 스키마에 직접 포함하여 알고리즘이 학습 성취도를 기반으로 평가될 수 있도록 한다.
- 2. OBER는 최소한의 엔티티-관계 모델, 로그 기반의 성취도 공식, 플러그인 아키텍처를 사용한다.
- 3. OBER는 비형식 교육 분야의 e-러닝 시스템에 통합되어 5,700명 이상의 학습자를 대상으로 한 2주간의 무작위 분할 테스트에서 평가되었다.
- 4. 협업 필터링(CF)은 학습자 유지율을 극대화했지만, 고정 경로가 가장 높은 성취도를 달성했다.
- 5. OBER는 동일한 로그에서 비즈니스, 관련성, 학습 지표를 도출하여 추가 테스트 없이 관련성과 참여도를 성취도와 비교할 수 있게 한다.


---

*Generated on 2025-09-24 13:21:47*