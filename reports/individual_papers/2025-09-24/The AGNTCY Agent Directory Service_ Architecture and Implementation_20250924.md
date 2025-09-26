<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:28:21.926032",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Agent Systems",
    "Open Agentic Schema Framework",
    "Distributed Hash Table",
    "Content-Addressed Storage",
    "Agent Directory Service"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-Agent Systems": 0.78,
    "Open Agentic Schema Framework": 0.72,
    "Distributed Hash Table": 0.68,
    "Content-Addressed Storage": 0.7,
    "Agent Directory Service": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Agent Systems",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "MAS"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-Agent Systems are central to the paper's focus on agent capabilities and interoperability.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Open Agentic Schema Framework",
        "canonical": "Open Agentic Schema Framework",
        "aliases": [
          "OASF"
        ],
        "category": "unique_technical",
        "rationale": "This framework is a unique aspect of the paper's architecture and implementation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.72
      },
      {
        "surface": "Distributed Hash Table",
        "canonical": "Distributed Hash Table",
        "aliases": [
          "DHT"
        ],
        "category": "broad_technical",
        "rationale": "Distributed Hash Tables are fundamental to the architecture described in the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.68
      },
      {
        "surface": "Content-Addressed Storage",
        "canonical": "Content-Addressed Storage",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Content-Addressed Storage is a specific technical component of the system's architecture.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Agent Directory Service",
        "canonical": "Agent Directory Service",
        "aliases": [
          "ADS"
        ],
        "category": "unique_technical",
        "rationale": "The Agent Directory Service is the primary subject of the paper, offering unique insights into agent discovery.",
        "novelty_score": 0.8,
        "connectivity_score": 0.75,
        "specificity_score": 0.95,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "architecture",
      "implementation",
      "discovery",
      "security",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Agent Systems",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Open Agentic Schema Framework",
      "resolved_canonical": "Open Agentic Schema Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Distributed Hash Table",
      "resolved_canonical": "Distributed Hash Table",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "Content-Addressed Storage",
      "resolved_canonical": "Content-Addressed Storage",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Agent Directory Service",
      "resolved_canonical": "Agent Directory Service",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.75,
        "specificity": 0.95,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# The AGNTCY Agent Directory Service: Architecture and Implementation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18787.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18787](https://arxiv.org/abs/2509.18787)

## 🔗 유사한 논문
- [[2025-09-19/Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (80.2% similar)
- [[2025-09-23/BlockA2A_ Towards Secure and Verifiable Agent-to-Agent Interoperability_20250923|BlockA2A: Towards Secure and Verifiable Agent-to-Agent Interoperability]] (79.8% similar)
- [[2025-09-18/Agentic JWT_ A Secure Delegation Protocol for Autonomous AI Agents_20250918|Agentic JWT: A Secure Delegation Protocol for Autonomous AI Agents]] (79.3% similar)
- [[2025-09-24/Autonomous Data Agents_ A New Opportunity for Smart Data_20250924|Autonomous Data Agents: A New Opportunity for Smart Data]] (79.1% similar)
- [[2025-09-23/XAgents_ A Framework for Interpretable Rule-Based Multi-Agents Cooperation_20250923|XAgents: A Framework for Interpretable Rule-Based Multi-Agents Cooperation]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Distributed Hash Table|Distributed Hash Table]]
**🔗 Specific Connectable**: [[keywords/Multi-Agent Systems|Multi-Agent Systems]]
**⚡ Unique Technical**: [[keywords/Open Agentic Schema Framework|Open Agentic Schema Framework]], [[keywords/Content-Addressed Storage|Content-Addressed Storage]], [[keywords/Agent Directory Service|Agent Directory Service]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18787v1 Announce Type: new 
Abstract: The Agent Directory Service (ADS) is a distributed directory for the discovery of AI agent capabilities, metadata, and provenance. It leverages content-addressed storage, hierarchical taxonomies, and cryptographic signing to enable efficient, verifiable, and multi-dimensional discovery across heterogeneous Multi-Agent Systems (MAS). Built on the Open Agentic Schema Framework (OASF), ADS decouples capability indexing from content location through a two-level mapping realized over a Kademlia-based Distributed Hash Table (DHT). It reuses mature OCI / ORAS infrastructure for artifact distribution, integrates Sigstore for provenance, and supports schema-driven extensibility for emerging agent modalities (LLM prompt agents, MCP servers, A2A-enabled components). This paper formalizes the architectural model, describes storage and discovery layers, explains security and performance properties, and positions ADS within the broader landscape of emerging agent registry and interoperability initiatives.

## 📝 요약

Agent Directory Service (ADS)는 AI 에이전트의 기능, 메타데이터, 출처를 발견하기 위한 분산 디렉토리입니다. 이 시스템은 콘텐츠 주소 지정 저장소, 계층적 분류 체계, 암호 서명을 활용하여 이질적인 다중 에이전트 시스템(MAS)에서 효율적이고 검증 가능한 다차원 검색을 가능하게 합니다. ADS는 Open Agentic Schema Framework(OASF)를 기반으로 하며, Kademlia 기반의 분산 해시 테이블(DHT)을 통해 기능 색인과 콘텐츠 위치를 분리합니다. 또한, 성숙한 OCI/ORAS 인프라를 재사용하고, Sigstore를 통합하여 출처를 관리하며, 새로운 에이전트 모달리티를 위한 스키마 기반 확장성을 지원합니다. 이 논문은 ADS의 아키텍처 모델을 공식화하고, 저장 및 검색 계층을 설명하며, 보안 및 성능 특성을 설명하고, 에이전트 레지스트리 및 상호 운용성 이니셔티브의 맥락에서 ADS의 위치를 제시합니다.

## 🎯 주요 포인트

- 1. Agent Directory Service (ADS)는 AI 에이전트의 기능, 메타데이터, 출처를 발견하기 위한 분산 디렉토리입니다.
- 2. ADS는 Kademlia 기반의 분산 해시 테이블을 통해 기능 색인을 콘텐츠 위치와 분리하여 효율적인 검색을 지원합니다.
- 3. 성숙한 OCI / ORAS 인프라를 재사용하고, Sigstore를 통합하여 출처를 관리하며, 새로운 에이전트 모달리티를 위한 스키마 기반 확장성을 지원합니다.
- 4. 이 논문은 ADS의 아키텍처 모델을 공식화하고, 저장 및 검색 계층을 설명하며, 보안 및 성능 속성을 분석합니다.
- 5. ADS는 에이전트 레지스트리 및 상호운용성 이니셔티브의 발전된 환경 내에서의 위치를 설명합니다.


---

*Generated on 2025-09-24 13:28:21*