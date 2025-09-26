---
keywords:
  - AI-assisted Software Development
  - Code Generation
  - Automated Code Review
  - Developer Productivity
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19708
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:46:06.800684",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "AI-assisted Software Development",
    "Code Generation",
    "Automated Code Review",
    "Developer Productivity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "AI-assisted Software Development": 0.78,
    "Code Generation": 0.75,
    "Automated Code Review": 0.77,
    "Developer Productivity": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AI-assisted software development",
        "canonical": "AI-assisted Software Development",
        "aliases": [
          "AI-driven software development",
          "AI-enhanced coding"
        ],
        "category": "unique_technical",
        "rationale": "This term captures the specific integration of AI in software development, which is central to the paper's findings.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "code generation",
        "canonical": "Code Generation",
        "aliases": [
          "automated code creation"
        ],
        "category": "specific_connectable",
        "rationale": "Code generation is a key feature of AI tools discussed, linking to broader AI capabilities.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "automated review capabilities",
        "canonical": "Automated Code Review",
        "aliases": [
          "AI code review",
          "automated code assessment"
        ],
        "category": "specific_connectable",
        "rationale": "Automated review is a critical component of the AI platform, enhancing developer productivity.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "developer productivity",
        "canonical": "Developer Productivity",
        "aliases": [
          "programmer efficiency",
          "coding productivity"
        ],
        "category": "broad_technical",
        "rationale": "The paper's primary focus is on measuring the impact of AI on developer productivity.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "enterprise scale",
      "cohort analysis",
      "production environments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AI-assisted software development",
      "resolved_canonical": "AI-assisted Software Development",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "code generation",
      "resolved_canonical": "Code Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "automated review capabilities",
      "resolved_canonical": "Automated Code Review",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "developer productivity",
      "resolved_canonical": "Developer Productivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Intuition to Evidence: Measuring AI's True Impact on Developer Productivity

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19708.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19708](https://arxiv.org/abs/2509.19708)

## 🔗 유사한 논문
- [[2025-09-19/On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub]] (85.5% similar)
- [[2025-09-23/Agentic AI for Software_ thoughts from Software Engineering community_20250923|Agentic AI for Software: thoughts from Software Engineering community]] (82.4% similar)
- [[2025-09-24/Reading Between the Lines_ Scalable User Feedback via Implicit Sentiment in Developer Prompts_20250924|Reading Between the Lines: Scalable User Feedback via Implicit Sentiment in Developer Prompts]] (82.1% similar)
- [[2025-09-19/Why Johnny Can't Use Agents_ Industry Aspirations vs. User Realities with AI Agent Software_20250919|Why Johnny Can't Use Agents: Industry Aspirations vs. User Realities with AI Agent Software]] (82.1% similar)
- [[2025-09-22/From Development to Deployment of AI-assisted Telehealth and Screening for Vision- and Hearing-threatening diseases in resource-constrained settings_ Field Observations, Challenges and Way Forward_20250922|From Development to Deployment of AI-assisted Telehealth and Screening for Vision- and Hearing-threatening diseases in resource-constrained settings: Field Observations, Challenges and Way Forward]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Developer Productivity|Developer Productivity]]
**🔗 Specific Connectable**: [[keywords/Code Generation|Code Generation]], [[keywords/Automated Code Review|Automated Code Review]]
**⚡ Unique Technical**: [[keywords/AI-assisted Software Development|AI-assisted Software Development]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19708v1 Announce Type: cross 
Abstract: We present a comprehensive real-world evaluation of AI-assisted software development tools deployed at enterprise scale. Over one year, 300 engineers across multiple teams integrated an in-house AI platform (DeputyDev) that combines code generation and automated review capabilities into their daily workflows. Through rigorous cohort analysis, our study demonstrates statistically significant productivity improvements, including an overall 31.8% reduction in PR review cycle time.
  Developer adoption was strong, with 85% satisfaction for code review features and 93% expressing a desire to continue using the platform. Adoption patterns showed systematic scaling from 4% engagement in month 1 to 83% peak usage by month 6, stabilizing at 60% active engagement. Top adopters achieved a 61% increase in code volume pushed to production, contributing to approximately 30 to 40% of code shipped to production through this tool, accounting for an overall 28% increase in code shipment volume.
  Unlike controlled benchmark evaluations, our longitudinal analysis provides empirical evidence from production environments, revealing both the transformative potential and practical deployment challenges of integrating AI into enterprise software development workflows.

## 📝 요약

이 논문은 기업 규모에서 AI 지원 소프트웨어 개발 도구의 실사용 평가를 다룹니다. 1년간 300명의 엔지니어가 코드 생성 및 자동 리뷰 기능을 갖춘 자체 AI 플랫폼 'DeputyDev'를 사용하여 생산성을 개선했습니다. 연구 결과, PR 리뷰 사이클 시간이 31.8% 단축되었고, 코드 리뷰 기능에 대한 만족도는 85%, 플랫폼 지속 사용 의사는 93%로 나타났습니다. 사용률은 1개월 차 4%에서 6개월 차 83%로 증가 후 60%로 안정화되었습니다. 주요 사용자들은 코드 생산량이 61% 증가했으며, 전체 코드 배포량이 28% 증가했습니다. 이 연구는 실제 환경에서 AI 통합의 잠재력과 도전 과제를 실증적으로 보여줍니다.

## 🎯 주요 포인트

- 1. AI 보조 소프트웨어 개발 도구의 도입으로 PR 리뷰 사이클 시간이 31.8% 감소하는 등 생산성이 크게 향상되었습니다.
- 2. 코드 리뷰 기능에 대한 만족도가 85%에 달하며, 93%의 개발자가 플랫폼 사용을 지속하고 싶다고 응답했습니다.
- 3. 도입 초기 4%의 참여율에서 시작하여 6개월 차에 83%의 사용률을 기록한 후, 60%의 안정적인 활성 참여율을 유지했습니다.
- 4. 상위 사용자들은 코드 생산량이 61% 증가했으며, 전체 코드 배포량이 28% 증가했습니다.
- 5. 본 연구는 AI 통합의 변혁적 잠재력과 실질적 배포 과제를 실증적으로 보여줍니다.


---

*Generated on 2025-09-25 15:46:06*