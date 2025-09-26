---
keywords:
  - SWE-Bench Pro
  - Long-Horizon Tasks
  - Large Language Model
  - Error Patterns in AI Models
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16941
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:40:07.812642",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SWE-Bench Pro",
    "Long-Horizon Tasks",
    "Large Language Model",
    "Error Patterns in AI Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "SWE-Bench Pro": 0.8,
    "Long-Horizon Tasks": 0.82,
    "Large Language Model": 0.78,
    "Error Patterns in AI Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SWE-Bench Pro",
        "canonical": "SWE-Bench Pro",
        "aliases": [
          "SWE-BENCH PRO"
        ],
        "category": "unique_technical",
        "rationale": "Represents a new benchmark specifically designed for evaluating AI agents on complex software engineering tasks.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Long-Horizon Tasks",
        "canonical": "Long-Horizon Tasks",
        "aliases": [
          "Extended Duration Tasks"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights tasks that require extended time and complexity, relevant for evaluating AI capabilities in software engineering.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Coding Models",
        "canonical": "Large Language Model",
        "aliases": [
          "AI Coding Models"
        ],
        "category": "broad_technical",
        "rationale": "Refers to AI models used for coding tasks, aligning with the broader category of large language models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Error Patterns",
        "canonical": "Error Patterns in AI Models",
        "aliases": [
          "Failure Modes"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding error patterns is crucial for improving AI model performance in complex tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "problems",
      "repositories"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "SWE-Bench Pro",
      "resolved_canonical": "SWE-Bench Pro",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Long-Horizon Tasks",
      "resolved_canonical": "Long-Horizon Tasks",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Coding Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Error Patterns",
      "resolved_canonical": "Error Patterns in AI Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16941.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16941](https://arxiv.org/abs/2509.16941)

## 🔗 유사한 논문
- [[2025-09-17/An Empirical Study on Failures in Automated Issue Solving_20250917|An Empirical Study on Failures in Automated Issue Solving]] (84.7% similar)
- [[2025-09-22/SeCodePLT_ A Unified Platform for Evaluating the Security of Code GenAI_20250922|SeCodePLT: A Unified Platform for Evaluating the Security of Code GenAI]] (82.5% similar)
- [[2025-09-19/SWE-QA_ Can Language Models Answer Repository-level Code Questions?_20250919|SWE-QA: Can Language Models Answer Repository-level Code Questions?]] (82.5% similar)
- [[2025-09-22/SWE-Effi_ Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints_20250922|SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints]] (82.0% similar)
- [[2025-09-19/SPICE_ An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation_20250919|SPICE: An Automated SWE-Bench Labeling Pipeline for Issue Clarity, Test Coverage, and Effort Estimation]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Long-Horizon Tasks|Long-Horizon Tasks]], [[keywords/Error Patterns in AI Models|Error Patterns in AI Models]]
**⚡ Unique Technical**: [[keywords/SWE-Bench Pro|SWE-Bench Pro]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16941v1 Announce Type: cross 
Abstract: We introduce SWE-Bench Pro, a substantially more challenging benchmark that builds upon the best practices of SWE-BENCH [25], but is explicitly designed to capture realistic, complex, enterprise-level problems beyond the scope of SWE-BENCH. SWE-BENCH PRO contains 1,865 problems sourced from a diverse set of 41 actively maintained repositories spanning business applications, B2B services, and developer tools. The benchmark is partitioned into a public set with open access to problems sourced from 11 repositories, a held-out set of 12 repositories and a commercial set of 18 proprietary repositories where we have formal partnership agreements with early-stage startups. Problems in the held-out and the commercial set are not publicly accessible, but we release results on the commercial set. Our benchmark features long-horizon tasks that may require hours to days for a professional software engineer to complete, often involving patches across multiple files and substantial code modifications. All tasks are human-verified and augmented with sufficient context to ensure resolvability. In our evaluation of widely used coding models, under a unified scaffold, we observe that their performance on SWE-Bench PRO remains below 25% (Pass@1), with GPT-5 achieving the highest score to date at 23.3%. To better understand these limitations, we cluster the failure modes observed in the collected agent trajectories for a clearer characterization of the error patterns exhibited by current models. Overall, SWE-BENCH PRO provides a contamination-resistant testbed that more faithfully captures the complexity and diversity of real-world software development, advancing the pursuit of truly autonomous software engineering agents at a professional level.

## 📝 요약

SWE-Bench Pro는 기존 SWE-BENCH를 기반으로 하여 현실적이고 복잡한 기업 수준의 문제를 다루는 더 어려운 벤치마크입니다. 이 벤치마크는 41개의 다양한 저장소에서 수집된 1,865개의 문제로 구성되며, 공개 세트, 비공개 세트, 상업적 세트로 나뉩니다. 상업적 세트는 초기 스타트업과의 공식 파트너십을 통해 제공됩니다. 이 벤치마크는 여러 파일에 걸친 패치와 상당한 코드 수정이 필요한 장기 과제를 포함하며, 모든 과제는 해결 가능하도록 충분한 맥락이 제공됩니다. SWE-Bench Pro에서 GPT-5는 23.3%의 최고 점수를 기록했으며, 이는 현재 모델의 한계를 이해하기 위한 오류 패턴 분석을 통해 확인되었습니다. 이 벤치마크는 현실 세계의 소프트웨어 개발의 복잡성과 다양성을 잘 반영하여 자율 소프트웨어 엔지니어링 에이전트 개발을 촉진합니다.

## 🎯 주요 포인트

- 1. SWE-Bench Pro는 기존 SWE-BENCH를 기반으로 하여 현실적이고 복잡한 기업 수준의 문제를 다루기 위해 설계된 더욱 도전적인 벤치마크입니다.
- 2. 이 벤치마크는 41개의 다양한 리포지토리에서 수집된 1,865개의 문제를 포함하며, 공개 세트, 비공개 세트, 상업적 세트로 구분됩니다.
- 3. SWE-Bench Pro의 과제는 여러 파일에 걸친 패치와 상당한 코드 수정이 필요한 장기 과제로, 해결 가능성을 보장하기 위해 충분한 맥락을 제공합니다.
- 4. SWE-Bench Pro에서의 코딩 모델 성능은 25% 미만(Pass@1)이며, GPT-5가 현재까지 가장 높은 23.3%의 점수를 기록했습니다.
- 5. 이 벤치마크는 오염 저항성이 높은 테스트베드로, 실제 소프트웨어 개발의 복잡성과 다양성을 충실히 반영하여 자율 소프트웨어 엔지니어링 에이전트 개발을 촉진합니다.


---

*Generated on 2025-09-24 03:40:07*