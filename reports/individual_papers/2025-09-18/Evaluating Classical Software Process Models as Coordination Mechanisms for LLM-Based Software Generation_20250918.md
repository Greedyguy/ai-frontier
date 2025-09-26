---
keywords:
  - Large Language Models
  - Multi-Agent Systems
  - Agile Software Development
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13942
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:29:49.232876",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Multi-Agent Systems",
    "Agile Software Development"
  ],
  "rejected_keywords": [
    "Waterfall Model",
    "V-Model"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Multi-Agent Systems": 0.75,
    "Agile Software Development": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation

**Korean Title:** LLM 기반 소프트웨어 생성을 위한 조정 메커니즘으로서 고전적인 소프트웨어 프로세스 모델을 평가하기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-Agent Systems|multi-agent systems]]
**⚡ Unique Technical**: [[keywords/Agile Software Development|Agile]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Model]]

## 🔗 유사한 논문
- [[An_LLM_Agentic_Approach_for_Legal-Critical_Software_A_Case_Study_for_Tax_Prep_Software_20250918|An LLM Agentic Approach for Legal-Critical Software: A Case Study for Tax Prep Software]] (82.7% similar)
- [[LLM_Agents_for_Interactive_Workflow_Provenance_Reference_Architecture_and_Evaluation_Methodology_20250918|LLM Agents for Interactive Workflow Provenance: Reference Architecture and Evaluation Methodology]] (81.5% similar)
- [[LLM Chatbot-Creation Approaches]] (80.7% similar)
- [[Semantic_Alignment-Enhanced_Code_Translation_via_an_LLM-Based_Multi-Agent_System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (79.4% similar)
- [[Using LLMs in Generating Design Rationale for Software Architecture Decisions]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13942v1 Announce Type: new 
Abstract: [Background] Large Language Model (LLM)-based multi-agent systems (MAS) are transforming software development by enabling autonomous collaboration. Classical software processes such asWaterfall, V-Model, and Agile offer structured coordination patterns that can be repurposed to guide these agent interactions. [Aims] This study explores how traditional software development processes can be adapted as coordination scaffolds for LLM based MAS and examines their impact on code quality, cost, and productivity. [Method] We executed 11 diverse software projects under three process models and four GPT variants, totaling 132 runs. Each output was evaluated using standardized metrics for size (files, LOC), cost (execution time, token usage), and quality (code smells, AI- and human detected bugs). [Results] Both process model and LLM choice significantly affected system performance. Waterfall was most efficient, V-Model produced the most verbose code, and Agile achieved the highest code quality, albeit at higher computational cost. [Conclusions] Classical software processes can be effectively instantiated in LLM-based MAS, but each entails trade-offs across quality, cost, and adaptability. Process selection should reflect project goals, whether prioritizing efficiency, robustness, or structured validation.

## 🔍 Abstract (한글 번역)

arXiv:2509.13942v1 발표 유형: 새로운
요약: [배경] 대규모 언어 모델(LLM) 기반의 다중 에이전트 시스템(MAS)은 자율 협업을 가능하게 함으로써 소프트웨어 개발을 변혁하고 있다. 폭포수, V-모델 및 애자일과 같은 고전적인 소프트웨어 프로세스는 이러한 에이전트 상호작용을 안내하기 위해 재활용할 수 있는 구조화된 조정 패턴을 제공한다. [목표] 본 연구는 전통적인 소프트웨어 개발 프로세스가 LLM 기반 MAS를 위한 조정 틀로 어떻게 적응될 수 있는지 탐구하고, 코드 품질, 비용 및 생산성에 미치는 영향을 조사한다. [방법] 우리는 3가지 프로세스 모델과 4가지 GPT 변형을 사용하여 총 132회 실행한 11가지 다양한 소프트웨어 프로젝트를 실행했다. 각 결과물은 크기(파일, LOC), 비용(실행 시간, 토큰 사용량), 품질(코드 냄새, AI 및 인간이 감지한 버그)에 대한 표준화된 측정 항목을 사용하여 평가되었다. [결과] 프로세스 모델과 LLM 선택이 시스템 성능에 유의미하게 영향을 미쳤다. 폭포수가 가장 효율적이었고, V-모델은 가장 말이 많은 코드를 생성했으며, 애자일은 높은 코드 품질을 달성했지만 높은 계산 비용이 발생했다. [결론] 고전적인 소프트웨어 프로세스는 LLM 기반 MAS에서 효과적으로 구현될 수 있지만, 각각은 품질, 비용 및 적응성 측면에서 상충관계를 가지고 있다. 프로세스 선택은 효율성, 견고성 또는 구조화된 검증을 우선시하는 프로젝트 목표를 반영해야 한다.

## 📝 요약

이 연구는 대형 언어 모델(LLM) 기반의 다중 에이전트 시스템(MAS)이 소프트웨어 개발을 자율적인 협업으로 변화시키고 있는데, 이를 위해 전통적인 소프트웨어 개발 프로세스가 LLM 기반 MAS에 조정되어 상호작용을 안내하는 데 어떻게 활용될 수 있는지 탐구한다. 11가지 다양한 소프트웨어 프로젝트를 세 가지 프로세스 모델과 네 가지 GPT 변형을 사용하여 실행하고, 각 결과물을 크기(파일, LOC), 비용(실행 시간, 토큰 사용량), 품질(코드 냄새, AI 및 인간이 감지한 버그)에 대한 표준화된 지표로 평가했다. 결과적으로 프로세스 모델과 LLM 선택이 시스템 성능에 유의미한 영향을 미치는 것으로 나타났다. 워터폴이 가장 효율적이었고, V-모델은 가장 많은 코드를 생성했으며, 애자일은 높은 코드 품질을 달성했지만 높은 계산 비용이 들었다. 전통적인 소프트웨어 프로세스는 LLM 기반 MAS에서 효과적으로 구현될 수 있지만, 각각은 품질, 비용 및 적응성 측면에서 트레이드오프가 필요하다. 프로세스 선택은 프로젝트 목표를 반영해야 하며, 효율성, 견고성 또는 구조적 검증을 우선시해야 한다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM) 기반 다중 에이전트 시스템(MAS)은 소프트웨어 개발을 자율적인 협업을 통해 변화시키고 있다.

- 2. 전통적인 소프트웨어 개발 프로세스는 LLM 기반 MAS에서 조정 뼈대로 적응될 수 있으며 코드 품질, 비용 및 생산성에 영향을 미친다.

- 3. 워터폴이 가장 효율적이며, V-모델은 가장 많은 코드를 생성하며, 애자일은 높은 코드 품질을 달성하지만 높은 계산 비용이 든다.

- 4. 전통적인 소프트웨어 프로세스는 LLM 기반 MAS에서 효과적으로 구현될 수 있지만 각각은 품질, 비용 및 적응성 측면에서 트레이드 오프가 있다.

- 5. 프로세스 선택은 프로젝트 목표를 반영해야 하며, 효율성, 견고성 또는 구조화된 검증을 우선시해야 한다.

---

*Generated on 2025-09-18 17:23:03*