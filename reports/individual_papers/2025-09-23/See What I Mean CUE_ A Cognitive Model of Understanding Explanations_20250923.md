---
keywords:
  - Explainable AI
  - Cognitive Understanding of Explanations
  - Human-centered Explanation
  - Adaptive XAI Interfaces
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.14775
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:07:38.174367",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Explainable AI",
    "Cognitive Understanding of Explanations",
    "Human-centered Explanation",
    "Adaptive XAI Interfaces"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Explainable AI": 0.78,
    "Cognitive Understanding of Explanations": 0.82,
    "Human-centered Explanation": 0.8,
    "Adaptive XAI Interfaces": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Explainable AI",
        "canonical": "Explainable AI",
        "aliases": [
          "XAI"
        ],
        "category": "broad_technical",
        "rationale": "Explainable AI is a critical area in machine learning that connects to various subfields and applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cognitive Understanding of Explanations",
        "canonical": "Cognitive Understanding of Explanations",
        "aliases": [
          "CUE"
        ],
        "category": "unique_technical",
        "rationale": "CUE is a novel model introduced in this paper, providing a unique perspective on explanation understanding.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Human-centered explanation properties",
        "canonical": "Human-centered Explanation",
        "aliases": [
          "User-centered Explanation"
        ],
        "category": "evolved_concepts",
        "rationale": "Human-centered explanation is an evolving concept in AI focusing on user accessibility and understanding.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive XAI interfaces",
        "canonical": "Adaptive XAI Interfaces",
        "aliases": [
          "Adaptive Explainable AI Interfaces"
        ],
        "category": "unique_technical",
        "rationale": "Adaptive XAI interfaces represent a novel approach to making AI explanations more accessible and user-friendly.",
        "novelty_score": 0.78,
        "connectivity_score": 0.68,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "perception",
      "comprehension",
      "interpretation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Explainable AI",
      "resolved_canonical": "Explainable AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cognitive Understanding of Explanations",
      "resolved_canonical": "Cognitive Understanding of Explanations",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Human-centered explanation properties",
      "resolved_canonical": "Human-centered Explanation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive XAI interfaces",
      "resolved_canonical": "Adaptive XAI Interfaces",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.68,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# See What I Mean? CUE: A Cognitive Model of Understanding Explanations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.14775.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.14775](https://arxiv.org/abs/2506.14775)

## 🔗 유사한 논문
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation]] (84.4% similar)
- [[2025-09-18/From Sea to System_ Exploring User-Centered Explainable AI for Maritime Decision Support_20250918|From Sea to System: Exploring User-Centered Explainable AI for Maritime Decision Support]] (82.3% similar)
- [[2025-09-22/Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models_20250922|Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models]] (82.0% similar)
- [[2025-09-22/Generating Part-Based Global Explanations Via Correspondence_20250922|Generating Part-Based Global Explanations Via Correspondence]] (81.6% similar)
- [[2025-09-23/V-CECE_ Visual Counterfactual Explanations via Conceptual Edits_20250923|V-CECE: Visual Counterfactual Explanations via Conceptual Edits]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Explainable AI|Explainable AI]]
**⚡ Unique Technical**: [[keywords/Cognitive Understanding of Explanations|Cognitive Understanding of Explanations]], [[keywords/Adaptive XAI Interfaces|Adaptive XAI Interfaces]]
**🚀 Evolved Concepts**: [[keywords/Human-centered Explanation|Human-centered Explanation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.14775v2 Announce Type: replace-cross 
Abstract: As machine learning systems increasingly inform critical decisions, the need for human-understandable explanations grows. Current evaluations of Explainable AI (XAI) often prioritize technical fidelity over cognitive accessibility which critically affects users, in particular those with visual impairments. We propose CUE, a model for Cognitive Understanding of Explanations, linking explanation properties to cognitive sub-processes: legibility (perception), readability (comprehension), and interpretability (interpretation). In a study (N=455) testing heatmaps with varying colormaps (BWR, Cividis, Coolwarm), we found comparable task performance but lower confidence/effort for visually impaired users. Unlike expected, these gaps were not mitigated and sometimes worsened by accessibility-focused color maps like Cividis. These results challenge assumptions about perceptual optimization and support the need for adaptive XAI interfaces. They also validate CUE by demonstrating that altering explanation legibility affects understandability. We contribute: (1) a formalized cognitive model for explanation understanding, (2) an integrated definition of human-centered explanation properties, and (3) empirical evidence motivating accessible, user-tailored XAI.

## 📝 요약

이 논문은 기계 학습 시스템의 설명 가능성을 높이기 위해 인간이 이해할 수 있는 설명의 중요성을 강조합니다. 저자들은 설명의 인지적 이해를 위한 CUE 모델을 제안하며, 이는 설명의 특성을 인지적 하위 과정인 가독성, 이해도, 해석 가능성과 연결합니다. 455명을 대상으로 다양한 색상 맵을 사용한 히트맵 실험에서 시각 장애 사용자는 유사한 과제 수행을 보였으나 자신감과 노력 면에서 낮은 결과를 보였습니다. 특히, 접근성을 고려한 색상 맵이 예상과 달리 이러한 격차를 줄이지 못했습니다. 이는 설명의 가독성이 이해도에 영향을 미친다는 점을 보여주며, 적응형 XAI 인터페이스의 필요성을 지지합니다. 주요 기여는 (1) 설명 이해를 위한 인지 모델, (2) 인간 중심 설명 속성의 통합 정의, (3) 접근 가능하고 사용자 맞춤형 XAI의 필요성을 뒷받침하는 실증적 증거입니다.

## 🎯 주요 포인트

- 1. 기계 학습 시스템의 설명 가능성(XAI) 평가에서 기술적 정확성보다 인지적 접근성이 중요하며, 이는 특히 시각 장애 사용자에게 큰 영향을 미친다.
- 2. CUE 모델은 설명의 속성을 인지적 하위 과정인 가독성, 이해도, 해석 가능성과 연결하여 설명 이해를 돕는다.
- 3. 연구 결과, 시각 장애 사용자는 색상 지도에 대한 자신감과 노력이 낮았으며, 접근성 중심의 색상 지도(Cividis 등)가 이러한 차이를 줄이지 못했다.
- 4. 설명의 가독성을 변경하면 이해 가능성에 영향을 미친다는 점에서 CUE 모델의 유효성이 입증되었다.
- 5. 본 연구는 설명 이해를 위한 인지 모델, 인간 중심의 설명 속성 정의, 접근 가능한 사용자 맞춤형 XAI의 필요성을 뒷받침하는 실증적 증거를 제공한다.


---

*Generated on 2025-09-24 01:07:38*