---
keywords:
  - Large Language Model
  - Software Defined Networking
  - Network Function Virtualization
  - Intent-Based Translation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2501.08760
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:43:11.078585",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Software Defined Networking",
    "Network Function Virtualization",
    "Intent-Based Translation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.88,
    "Software Defined Networking": 0.82,
    "Network Function Virtualization": 0.8,
    "Intent-Based Translation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the proposed framework, linking to broader AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "Software Defined Networking",
        "canonical": "Software Defined Networking",
        "aliases": [
          "SDN"
        ],
        "category": "specific_connectable",
        "rationale": "SDN is a key paradigm shift in network configuration that the framework addresses.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Network Function Virtualization",
        "canonical": "Network Function Virtualization",
        "aliases": [
          "NFV"
        ],
        "category": "specific_connectable",
        "rationale": "NFV is another emerging paradigm relevant to the framework's application.",
        "novelty_score": 0.58,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Intent-Based Translation",
        "canonical": "Intent-Based Translation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is the novel approach proposed by the paper, crucial for understanding its contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "configuration",
      "translation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Software Defined Networking",
      "resolved_canonical": "Software Defined Networking",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Network Function Virtualization",
      "resolved_canonical": "Network Function Virtualization",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Intent-Based Translation",
      "resolved_canonical": "Intent-Based Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# INTA: Intent-Based Translation for Network Configuration with LLM Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.08760.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2501.08760](https://arxiv.org/abs/2501.08760)

## 🔗 유사한 논문
- [[2025-09-18/Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (83.0% similar)
- [[2025-09-22/MatchFixAgent_ Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair_20250922|MatchFixAgent: Language-Agnostic Autonomous Repository-Level Code Translation Validation and Repair]] (80.4% similar)
- [[2025-09-23/XAgents_ A Framework for Interpretable Rule-Based Multi-Agents Cooperation_20250923|XAgents: A Framework for Interpretable Rule-Based Multi-Agents Cooperation]] (80.1% similar)
- [[2025-09-19/T-araVLN_ Translator for Agricultural Robotic Agents on Vision-and-Language Navigation_20250919|T-araVLN: Translator for Agricultural Robotic Agents on Vision-and-Language Navigation]] (79.6% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance: Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Software Defined Networking|Software Defined Networking]], [[keywords/Network Function Virtualization|Network Function Virtualization]]
**⚡ Unique Technical**: [[keywords/Intent-Based Translation|Intent-Based Translation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.08760v2 Announce Type: replace-cross 
Abstract: Translating configurations between different network devices is a common yet challenging task in modern network operations. This challenge arises in typical scenarios such as replacing obsolete hardware and adapting configurations to emerging paradigms like Software Defined Networking (SDN) and Network Function Virtualization (NFV). Engineers need to thoroughly understand both source and target configuration models, which requires considerable effort due to the complexity and evolving nature of these specifications. To promote automation in network configuration translation, we propose INTA, an intent-based translation framework that leverages Large Language Model (LLM) agents. The key idea of INTA is to use configuration intent as an intermediate representation for translation. It first employs LLMs to decompose configuration files and extract fine-grained intents for each configuration fragment. These intents are then used to retrieve relevant manuals of the target device. Guided by a syntax checker, INTA incrementally generates target configurations. The translated configurations are further verified and refined for semantic consistency. We implement INTA and evaluate it on real-world configuration datasets from the industry. Our approach outperforms state-of-the-art methods in translation accuracy and exhibits strong generalizability. INTA achieves an accuracy of 98.15% in terms of both syntactic and view correctness, and a command recall rate of 84.72% for the target configuration. The semantic consistency report of the translated configuration further demonstrates its practical value in real-world network operations.

## 📝 요약

현대 네트워크 운영에서 다양한 네트워크 장치 간의 설정을 번역하는 것은 일반적인 과제지만 복잡합니다. 이를 해결하기 위해 INTA라는 의도 기반 번역 프레임워크를 제안합니다. INTA는 대형 언어 모델(LLM)을 활용하여 설정 파일을 세분화하고 각 부분의 의도를 추출한 후, 이를 기반으로 대상 장치의 관련 매뉴얼을 참조하여 설정을 생성합니다. 구문 검사기를 통해 점진적으로 대상 설정을 생성하고, 번역된 설정의 의미적 일관성을 검증 및 개선합니다. 실제 산업 데이터셋을 통해 평가한 결과, INTA는 번역 정확도에서 최첨단 방법들을 능가하며 98.15%의 정확도와 84.72%의 명령 회수율을 기록했습니다. 이는 실제 네트워크 운영에서의 실용성을 입증합니다.

## 🎯 주요 포인트

- 1. 네트워크 장치 간의 구성 변환은 현대 네트워크 운영에서 일반적이지만 도전적인 과제입니다.
- 2. INTA는 구성 의도를 중간 표현으로 활용하여 번역을 수행하는 의도 기반 번역 프레임워크입니다.
- 3. INTA는 대규모 언어 모델(LLM)을 사용하여 구성 파일을 분해하고 세밀한 의도를 추출합니다.
- 4. INTA는 번역 정확도에서 최첨단 방법을 능가하며 강력한 일반화 능력을 보여줍니다.
- 5. INTA는 구문 및 보기 정확성에서 98.15%의 정확도를 달성하고, 명령 회수율은 84.72%입니다.


---

*Generated on 2025-09-24 00:43:11*