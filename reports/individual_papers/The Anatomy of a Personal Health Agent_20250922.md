# The Anatomy of a Personal Health Agent

**Korean Title:** 개인 건강 에이전트의 해부학

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent Framework

## 🔗 유사한 논문
- [[2025-09-18/MAFA_ A multi-agent framework for annotation_20250918|MAFA A multi-agent framework for annotation]] (82.8% similar)
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI Fully Autonomous Research Agent for Health Infomatics]] (81.9% similar)
- [[2025-09-19/Why Johnny Can't Use Agents_ Industry Aspirations vs. User Realities with AI Agent Software_20250919|Why Johnny Can't Use Agents Industry Aspirations vs. User Realities with AI Agent Software]] (81.1% similar)
- [[2025-09-18/Designing AI-Agents with Personalities_ A Psychometric Approach_20250918|Designing AI-Agents with Personalities A Psychometric Approach]] (80.7% similar)
- [[2025-09-22/MICA_ Multi-Agent Industrial Coordination Assistant_20250922|MICA Multi-Agent Industrial Coordination Assistant]] (80.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.20148v2 Announce Type: replace 
Abstract: Health is a fundamental pillar of human wellness, and the rapid advancements in large language models (LLMs) have driven the development of a new generation of health agents. However, the application of health agents to fulfill the diverse needs of individuals in daily non-clinical settings is underexplored. In this work, we aim to build a comprehensive personal health agent that is able to reason about multimodal data from everyday consumer wellness devices and common personal health records, and provide personalized health recommendations. To understand end-users' needs when interacting with such an assistant, we conducted an in-depth analysis of web search and health forum queries, alongside qualitative insights from users and health experts gathered through a user-centered design process. Based on these findings, we identified three major categories of consumer health needs, each of which is supported by a specialist sub-agent: (1) a data science agent that analyzes personal time-series wearable and health record data, (2) a health domain expert agent that integrates users' health and contextual data to generate accurate, personalized insights, and (3) a health coach agent that synthesizes data insights, guiding users using a specified psychological strategy and tracking users' progress. Furthermore, we propose and develop the Personal Health Agent (PHA), a multi-agent framework that enables dynamic, personalized interactions to address individual health needs. To evaluate each sub-agent and the multi-agent system, we conducted automated and human evaluations across 10 benchmark tasks, involving more than 7,000 annotations and 1,100 hours of effort from health experts and end-users. Our work represents the most comprehensive evaluation of a health agent to date and establishes a strong foundation towards the futuristic vision of a personal health agent accessible to everyone.

## 🔍 Abstract (한글 번역)

arXiv:2508.20148v2 발표 유형: 교체  
초록: 건강은 인간 웰빙의 근본적인 기둥이며, 대형 언어 모델(LLM)의 급속한 발전은 새로운 세대의 건강 에이전트 개발을 촉진했습니다. 그러나 일상적인 비임상 환경에서 개인의 다양한 요구를 충족시키기 위한 건강 에이전트의 적용은 충분히 탐구되지 않았습니다. 본 연구에서는 일상적인 소비자 웰니스 기기와 일반적인 개인 건강 기록에서 수집한 다중 모드 데이터를 분석하고 개인 맞춤형 건강 추천을 제공할 수 있는 포괄적인 개인 건강 에이전트를 구축하는 것을 목표로 합니다. 이러한 보조 도구와 상호 작용할 때 최종 사용자의 요구를 이해하기 위해, 웹 검색 및 건강 포럼 쿼리에 대한 심층 분석을 수행하고, 사용자 중심 설계 과정을 통해 수집한 사용자 및 건강 전문가의 질적 통찰을 함께 분석했습니다. 이러한 발견을 바탕으로, 우리는 소비자 건강 요구의 세 가지 주요 범주를 식별했으며, 각각은 전문 하위 에이전트에 의해 지원됩니다: (1) 개인 시계열 웨어러블 및 건강 기록 데이터를 분석하는 데이터 과학 에이전트, (2) 사용자의 건강 및 맥락 데이터를 통합하여 정확하고 개인화된 통찰을 생성하는 건강 도메인 전문가 에이전트, (3) 데이터 통찰을 종합하여 특정 심리적 전략을 사용하여 사용자를 안내하고 사용자의 진행 상황을 추적하는 건강 코치 에이전트. 또한, 우리는 개인 건강 에이전트(PHA)를 제안하고 개발하며, 개별 건강 요구를 해결하기 위한 동적이고 개인화된 상호 작용을 가능하게 하는 다중 에이전트 프레임워크를 제안합니다. 각 하위 에이전트와 다중 에이전트 시스템을 평가하기 위해, 우리는 10개의 벤치마크 작업에 걸쳐 자동 및 인간 평가를 수행했으며, 건강 전문가와 최종 사용자의 7,000개 이상의 주석과 1,100시간 이상의 노력을 포함했습니다. 우리의 연구는 현재까지 가장 포괄적인 건강 에이전트 평가를 나타내며, 모든 사람이 접근할 수 있는 개인 건강 에이전트의 미래적 비전을 위한 강력한 기반을 마련합니다.

## 📝 요약

이 논문은 개인 건강 관리 에이전트의 개발을 목표로 하며, 일상적인 비임상 환경에서 개인의 다양한 건강 요구를 충족시키기 위해 설계되었습니다. 연구팀은 사용자 중심 설계를 통해 웹 검색과 건강 포럼 질의를 분석하고, 사용자 및 건강 전문가의 질적 통찰을 수집했습니다. 이를 통해 세 가지 주요 소비자 건강 요구를 파악하고, 각각을 지원하는 전문 하위 에이전트를 개발했습니다: (1) 개인의 웨어러블 및 건강 기록 데이터를 분석하는 데이터 과학 에이전트, (2) 사용자 건강 및 맥락 데이터를 통합하여 맞춤형 통찰을 제공하는 건강 도메인 전문가 에이전트, (3) 심리 전략을 사용해 사용자에게 가이드를 제공하고 진행 상황을 추적하는 건강 코치 에이전트입니다. 이 연구는 10개의 벤치마크 과제를 통해 자동 및 인간 평가를 수행하여, 7,000개 이상의 주석과 1,100시간 이상의 노력을 통해 각 하위 에이전트와 다중 에이전트 시스템을 평가했습니다. 이 연구는 개인 건강 에이전트의 미래적 비전을 위한 강력한 기초를 마련했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 일상적인 비임상 환경에서 개인의 다양한 건강 요구를 충족시키기 위한 종합적인 개인 건강 에이전트를 구축하는 것을 목표로 한다.

- 2. 사용자 중심 설계 과정을 통해 웹 검색 및 건강 포럼 쿼리와 사용자 및 건강 전문가의 정성적 통찰을 분석하여 소비자 건강 요구를 세 가지 주요 범주로 식별하였다.

- 3. 데이터 과학 에이전트, 건강 도메인 전문가 에이전트, 건강 코치 에이전트로 구성된 전문 하위 에이전트를 통해 개인화된 건강 추천을 제공한다.

- 4. 개인 건강 에이전트(PHA)라는 다중 에이전트 프레임워크를 제안 및 개발하여 개인의 건강 요구를 동적으로 해결할 수 있는 상호작용을 가능하게 한다.

- 5. 10개의 벤치마크 과제를 통해 자동화 및 인간 평가를 수행하여, 7,000개 이상의 주석과 1,100시간 이상의 건강 전문가 및 최종 사용자 노력을 통해 종합적인 평가를 진행하였다.

---

*Generated on 2025-09-22 14:33:48*