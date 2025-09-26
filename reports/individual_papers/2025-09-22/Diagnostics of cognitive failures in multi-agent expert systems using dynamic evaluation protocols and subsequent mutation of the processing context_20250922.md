---
keywords:
  - Transformer
  - Large Language Model
  - Agent Judge
  - Expert Behaviour Transfer
  - Cognitive Failures
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15366
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:40:56.339559",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Large Language Model",
    "Agent Judge",
    "Expert Behaviour Transfer",
    "Cognitive Failures"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Large Language Model": 0.8,
    "Agent Judge": 0.78,
    "Expert Behaviour Transfer": 0.77,
    "Cognitive Failures": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large-scale Transformer-based models",
        "canonical": "Transformer",
        "aliases": [
          "Transformer-based models",
          "Large Transformer models"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture for modern LLMs, facilitating strong connectivity with other AI concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's focus on agentic behaviors and expert system integration.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Agent Judge",
        "canonical": "Agent Judge",
        "aliases": [
          "LLM-based Agent Judge"
        ],
        "category": "unique_technical",
        "rationale": "The Agent Judge is a novel component of the diagnostic framework, crucial for evaluating and improving agent performance.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Expert behaviour transfer",
        "canonical": "Expert Behaviour Transfer",
        "aliases": [
          "Behaviour transfer",
          "Expert transfer"
        ],
        "category": "unique_technical",
        "rationale": "This concept is key to the paper's contribution in standardizing and reproducing expert behavior in LLM agents.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Cognitive failures",
        "canonical": "Cognitive Failures",
        "aliases": [
          "Latent cognitive failures"
        ],
        "category": "unique_technical",
        "rationale": "Identifying cognitive failures is essential for diagnosing and improving multi-agent systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "evaluation methods",
      "expert systems",
      "multi-agent system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large-scale Transformer-based models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Agent Judge",
      "resolved_canonical": "Agent Judge",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Expert behaviour transfer",
      "resolved_canonical": "Expert Behaviour Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Cognitive failures",
      "resolved_canonical": "Cognitive Failures",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context

**Korean Title:** 다중 에이전트 전문가 시스템에서 인지 실패의 진단: 동적 평가 프로토콜과 후속 처리 맥락의 변이를 활용한 접근법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15366.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15366](https://arxiv.org/abs/2509.15366)

## 🔗 유사한 논문
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass: Towards Reliable Evaluation of Agentic Workflows in Production]] (88.2% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED: A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (87.5% similar)
- [[2025-09-19/Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents_20250919|Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents]] (86.8% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (86.6% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance: Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (85.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Agent Judge|Agent Judge]], [[keywords/Expert Behaviour Transfer|Expert Behaviour Transfer]], [[keywords/Cognitive Failures|Cognitive Failures]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15366v1 Announce Type: new 
Abstract: The rapid evolution of neural architectures - from multilayer perceptrons to large-scale Transformer-based models - has enabled language models (LLMs) to exhibit emergent agentic behaviours when equipped with memory, planning, and external tool use. However, their inherent stochasticity and multi-step decision processes render classical evaluation methods inadequate for diagnosing agentic performance. This work introduces a diagnostic framework for expert systems that not only evaluates but also facilitates the transfer of expert behaviour into LLM-powered agents. The framework integrates (i) curated golden datasets of expert annotations, (ii) silver datasets generated through controlled behavioural mutation, and (iii) an LLM-based Agent Judge that scores and prescribes targeted improvements. These prescriptions are embedded into a vectorized recommendation map, allowing expert interventions to propagate as reusable improvement trajectories across multiple system instances. We demonstrate the framework on a multi-agent recruiter-assistant system, showing that it uncovers latent cognitive failures - such as biased phrasing, extraction drift, and tool misrouting - while simultaneously steering agents toward expert-level reasoning and style. The results establish a foundation for standardized, reproducible expert behaviour transfer in stochastic, tool-augmented LLM agents, moving beyond static evaluation to active expert system refinement.

## 🔍 Abstract (한글 번역)

arXiv:2509.15366v1 발표 유형: 신규  
초록: 다층 퍼셉트론에서 대규모 트랜스포머 기반 모델로의 신경 아키텍처의 급속한 발전은 언어 모델(LLM)이 메모리, 계획 및 외부 도구 사용을 갖추었을 때 새로운 에이전트 행동을 나타낼 수 있도록 했습니다. 그러나 그들의 고유한 확률성과 다단계 의사 결정 과정은 고전적인 평가 방법이 에이전트 성능을 진단하는 데 부적합하게 만듭니다. 본 연구는 전문가 시스템을 위한 진단 프레임워크를 소개하여 LLM 기반 에이전트로의 전문가 행동 전이를 촉진할 뿐만 아니라 평가도 수행합니다. 이 프레임워크는 (i) 전문가 주석으로 구성된 골든 데이터셋, (ii) 통제된 행동 변이를 통해 생성된 실버 데이터셋, (iii) 점수와 목표 개선을 처방하는 LLM 기반 에이전트 판사를 통합합니다. 이러한 처방은 벡터화된 추천 맵에 내장되어 전문가 개입이 여러 시스템 인스턴스에 걸쳐 재사용 가능한 개선 궤적으로 전파될 수 있도록 합니다. 우리는 다중 에이전트 채용 보조 시스템에서 프레임워크를 시연하여, 편향된 표현, 추출 드리프트, 도구 오경로와 같은 잠재적 인지 실패를 발견하는 동시에 에이전트를 전문가 수준의 추론과 스타일로 유도함을 보여줍니다. 결과는 확률적이고 도구가 보강된 LLM 에이전트에서 정적 평가를 넘어 능동적인 전문가 시스템 개선으로 나아가는 표준화되고 재현 가능한 전문가 행동 전이의 기초를 확립합니다.

## 📝 요약

이 논문은 대규모 Transformer 기반 언어 모델(LLM)의 에이전트적 행동을 평가하고 개선하기 위한 진단 프레임워크를 제안합니다. 기존 평가 방법이 LLM의 확률성과 다단계 의사 결정 과정을 충분히 진단하지 못하는 문제를 해결하고자, 이 프레임워크는 전문가 주석이 포함된 골든 데이터셋, 통제된 행동 변이를 통해 생성된 실버 데이터셋, 그리고 LLM 기반 에이전트 평가 시스템을 통합합니다. 이를 통해 전문가의 행동을 LLM 에이전트에 전이시키고, 벡터화된 추천 지도를 통해 개선 경로를 제시합니다. 다중 에이전트 시스템에 적용한 결과, 잠재적인 인지 실패를 발견하고 에이전트를 전문가 수준의 추론과 스타일로 유도하는 데 성공했습니다. 이 연구는 확률적이고 도구가 보강된 LLM 에이전트에서 전문가 행동 전이를 표준화하고 재현 가능하게 만드는 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 신경망 구조의 빠른 발전은 언어 모델이 기억, 계획, 외부 도구 사용을 통해 에이전트적 행동을 보이게 합니다.
- 2. 기존 평가 방법은 이러한 에이전트적 성능을 진단하기에 충분하지 않으며, 이를 해결하기 위한 진단 프레임워크가 제안되었습니다.
- 3. 제안된 프레임워크는 전문가 주석의 골든 데이터셋, 행동 변이를 통한 실버 데이터셋, LLM 기반 에이전트 평가자를 통합하여 전문가 행동을 LLM 에이전트로 전이시킵니다.
- 4. 이 프레임워크는 편향된 표현, 추출 드리프트, 도구 오작동 등의 잠재적 인지 실패를 발견하고 에이전트를 전문가 수준의 추론과 스타일로 유도합니다.
- 5. 결과적으로, 도구가 보강된 LLM 에이전트에서 표준화되고 재현 가능한 전문가 행동 전이를 위한 기초를 마련합니다.


---

*Generated on 2025-09-23 08:40:56*