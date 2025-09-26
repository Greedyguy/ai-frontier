---
keywords:
  - Stance Detection
  - Recommendation Systems
  - Journalism-guided Agentic In-Context Learning
  - Viewpoint Diversity
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2507.11049
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:07:13.795044",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stance Detection",
    "Recommendation Systems",
    "Journalism-guided Agentic In-Context Learning",
    "Viewpoint Diversity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stance Detection": 0.82,
    "Recommendation Systems": 0.75,
    "Journalism-guided Agentic In-Context Learning": 0.8,
    "Viewpoint Diversity": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "stance detection",
        "canonical": "Stance Detection",
        "aliases": [
          "stance analysis",
          "stance identification"
        ],
        "category": "specific_connectable",
        "rationale": "Stance Detection is crucial for understanding media bias and viewpoint diversity, aligning with the paper's focus on news stance detection.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "personalized recommendation systems",
        "canonical": "Recommendation Systems",
        "aliases": [
          "personalized recommendations"
        ],
        "category": "broad_technical",
        "rationale": "Recommendation Systems are integral to digital journalism, providing a bridge to discussions on filter bubbles and media bias.",
        "novelty_score": 0.48,
        "connectivity_score": 0.79,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      },
      {
        "surface": "JoA-ICL",
        "canonical": "Journalism-guided Agentic In-Context Learning",
        "aliases": [
          "JoA-ICL framework"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, highlighting its unique contribution to stance detection.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "viewpoint diversity",
        "canonical": "Viewpoint Diversity",
        "aliases": [
          "perspective diversity"
        ],
        "category": "evolved_concepts",
        "rationale": "Viewpoint Diversity is a key concept in mitigating filter bubbles and is central to the paper's objectives.",
        "novelty_score": 0.6,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "news consumption",
      "media bias"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "stance detection",
      "resolved_canonical": "Stance Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "personalized recommendation systems",
      "resolved_canonical": "Recommendation Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.79,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "JoA-ICL",
      "resolved_canonical": "Journalism-guided Agentic In-Context Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "viewpoint diversity",
      "resolved_canonical": "Viewpoint Diversity",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Journalism-Guided Agentic In-Context Learning for News Stance Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2507.11049.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2507.11049](https://arxiv.org/abs/2507.11049)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (81.4% similar)
- [[2025-09-23/Multilingual vs Crosslingual Retrieval of Fact-Checked Claims_ A Tale of Two Approaches_20250923|Multilingual vs Crosslingual Retrieval of Fact-Checked Claims: A Tale of Two Approaches]] (78.6% similar)
- [[2025-09-23/KoACD_ The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation_20250923|KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation]] (78.2% similar)
- [[2025-09-19/Judging with Many Minds_ Do More Perspectives Mean Less Prejudice? On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge_20250919|Judging with Many Minds: Do More Perspectives Mean Less Prejudice? On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge]] (78.1% similar)
- [[2025-09-23/Enhancing Live Broadcast Engagement_ A Multi-modal Approach to Short Video Recommendations Using MMGCN and User Preferences_20250923|Enhancing Live Broadcast Engagement: A Multi-modal Approach to Short Video Recommendations Using MMGCN and User Preferences]] (78.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Recommendation Systems|Recommendation Systems]]
**🔗 Specific Connectable**: [[keywords/Stance Detection|Stance Detection]]
**⚡ Unique Technical**: [[keywords/Journalism-guided Agentic In-Context Learning|Journalism-guided Agentic In-Context Learning]]
**🚀 Evolved Concepts**: [[keywords/Viewpoint Diversity|Viewpoint Diversity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.11049v3 Announce Type: replace 
Abstract: As online news consumption grows, personalized recommendation systems have become integral to digital journalism. However, these systems risk reinforcing filter bubbles and political polarization by failing to incorporate diverse perspectives. Stance detection -- identifying a text's position on a target -- can help mitigate this by enabling viewpoint-aware recommendations and data-driven analyses of media bias. Yet, existing stance detection research remains largely limited to short texts and high-resource languages. To address these gaps, we introduce \textsc{K-News-Stance}, the first Korean dataset for article-level stance detection, comprising 2,000 news articles with article-level and 21,650 segment-level stance annotations across 47 societal issues. We also propose \textsc{JoA-ICL}, a \textbf{Jo}urnalism-guided \textbf{A}gentic \textbf{I}n-\textbf{C}ontext \textbf{L}earning framework that employs a language model agent to predict the stances of key structural segments (e.g., leads, quotations), which are then aggregated to infer the overall article stance. Experiments showed that \textsc{JoA-ICL} outperforms existing stance detection methods, highlighting the benefits of segment-level agency in capturing the overall position of long-form news articles. Two case studies further demonstrate its broader utility in promoting viewpoint diversity in news recommendations and uncovering patterns of media bias.

## 📝 요약

이 논문은 온라인 뉴스 소비 증가에 따라 개인화된 추천 시스템이 중요해졌지만, 이러한 시스템이 필터 버블과 정치적 양극화를 강화할 위험이 있음을 지적합니다. 이를 해결하기 위해 입장 탐지 기술이 필요하며, 이는 다양한 관점을 반영한 추천과 미디어 편향에 대한 데이터 기반 분석을 가능하게 합니다. 그러나 기존 연구는 주로 짧은 텍스트와 자원이 풍부한 언어에 국한되어 있습니다. 이를 해결하기 위해 한국어 기사 수준의 입장 탐지를 위한 최초의 데이터셋인 \textsc{K-News-Stance}를 소개합니다. 이 데이터셋은 47개의 사회적 이슈에 대한 2,000개의 뉴스 기사와 21,650개의 세그먼트 수준 입장 주석을 포함합니다. 또한, \textsc{JoA-ICL}이라는 저널리즘 기반의 에이전트 학습 프레임워크를 제안하여, 주요 구조적 세그먼트의 입장을 예측하고 이를 종합하여 전체 기사 입장을 유추합니다. 실험 결과, \textsc{JoA-ICL}은 기존의 입장 탐지 방법보다 우수한 성능을 보였으며, 뉴스 추천에서 관점 다양성을 증진하고 미디어 편향 패턴을 발견하는 데 유용함을 두 가지 사례 연구를 통해 입증했습니다.

## 🎯 주요 포인트

- 1. 온라인 뉴스 소비 증가로 개인화 추천 시스템이 디지털 저널리즘에 필수적이지만, 필터 버블과 정치적 양극화를 강화할 위험이 있다.
- 2. 입장 감지 기술은 다양한 관점을 반영한 추천과 미디어 편향의 데이터 기반 분석을 가능하게 하여 이러한 문제를 완화할 수 있다.
- 3. \textsc{K-News-Stance}는 기사 수준의 입장 감지를 위한 최초의 한국어 데이터셋으로, 47개 사회적 이슈에 대한 2,000개의 뉴스 기사와 21,650개의 세그먼트 수준 입장 주석을 포함한다.
- 4. \textsc{JoA-ICL} 프레임워크는 주요 구조적 세그먼트의 입장을 예측하여 전체 기사 입장을 추론하며, 기존 입장 감지 방법보다 우수한 성능을 보였다.
- 5. 두 가지 사례 연구를 통해 \textsc{JoA-ICL}의 뉴스 추천에서 관점 다양성을 촉진하고 미디어 편향 패턴을 밝혀내는 데 있어 광범위한 유용성을 입증했다.


---

*Generated on 2025-09-24 04:07:13*