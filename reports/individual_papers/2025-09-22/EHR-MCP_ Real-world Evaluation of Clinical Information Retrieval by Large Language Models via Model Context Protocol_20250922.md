# EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol

**Korean Title:** EHR-MCP: 모델 컨텍스트 프로토콜을 통한 대형 언어 모델에 의한 임상 정보 검색의 실제 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Model Context Protocol, LangGraph ReAct Agent

## 🔗 유사한 논문
- [[2025-09-18/Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes_20250918|Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes]] (85.4% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (83.9% similar)
- [[2025-09-19/Position_ Thematic Analysis of Unstructured Clinical Transcripts with Large Language Models_20250919|Position Thematic Analysis of Unstructured Clinical Transcripts with Large Language Models]] (82.6% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (82.3% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15957v1 Announce Type: new 
Abstract: Background: Large language models (LLMs) show promise in medicine, but their deployment in hospitals is limited by restricted access to electronic health record (EHR) systems. The Model Context Protocol (MCP) enables integration between LLMs and external tools.
  Objective: To evaluate whether an LLM connected to an EHR database via MCP can autonomously retrieve clinically relevant information in a real hospital setting.
  Methods: We developed EHR-MCP, a framework of custom MCP tools integrated with the hospital EHR database, and used GPT-4.1 through a LangGraph ReAct agent to interact with it. Six tasks were tested, derived from use cases of the infection control team (ICT). Eight patients discussed at ICT conferences were retrospectively analyzed. Agreement with physician-generated gold standards was measured.
  Results: The LLM consistently selected and executed the correct MCP tools. Except for two tasks, all tasks achieved near-perfect accuracy. Performance was lower in the complex task requiring time-dependent calculations. Most errors arose from incorrect arguments or misinterpretation of tool results. Responses from EHR-MCP were reliable, though long and repetitive data risked exceeding the context window.
  Conclusions: LLMs can retrieve clinical data from an EHR via MCP tools in a real hospital setting, achieving near-perfect performance in simple tasks while highlighting challenges in complex ones. EHR-MCP provides an infrastructure for secure, consistent data access and may serve as a foundation for hospital AI agents. Future work should extend beyond retrieval to reasoning, generation, and clinical impact assessment, paving the way for effective integration of generative AI into clinical practice.

## 🔍 Abstract (한글 번역)

arXiv:2509.15957v1 발표 유형: 신규  
초록: 배경: 대형 언어 모델(LLM)은 의학 분야에서 가능성을 보여주고 있지만, 전자 건강 기록(EHR) 시스템에 대한 제한된 접근으로 인해 병원에서의 배포가 제한되고 있습니다. 모델 컨텍스트 프로토콜(MCP)은 LLM과 외부 도구 간의 통합을 가능하게 합니다.  
목적: MCP를 통해 EHR 데이터베이스에 연결된 LLM이 실제 병원 환경에서 임상적으로 관련된 정보를 자율적으로 검색할 수 있는지를 평가하는 것입니다.  
방법: 우리는 병원 EHR 데이터베이스와 통합된 맞춤형 MCP 도구 프레임워크인 EHR-MCP를 개발하고, LangGraph ReAct 에이전트를 통해 GPT-4.1을 사용하여 상호작용을 수행했습니다. 감염 통제 팀(ICT)의 사용 사례에서 파생된 여섯 가지 작업을 테스트했습니다. ICT 회의에서 논의된 여덟 명의 환자를 회고적으로 분석했습니다. 의사가 생성한 골드 스탠다드와의 일치를 측정했습니다.  
결과: LLM은 일관되게 올바른 MCP 도구를 선택하고 실행했습니다. 두 가지 작업을 제외하고 모든 작업은 거의 완벽한 정확도를 달성했습니다. 시간에 의존하는 계산이 필요한 복잡한 작업에서 성능이 낮았습니다. 대부분의 오류는 잘못된 인수 또는 도구 결과의 오해에서 발생했습니다. EHR-MCP의 응답은 신뢰할 수 있었지만, 긴 반복적인 데이터는 컨텍스트 창을 초과할 위험이 있었습니다.  
결론: LLM은 실제 병원 환경에서 MCP 도구를 통해 EHR에서 임상 데이터를 검색할 수 있으며, 간단한 작업에서 거의 완벽한 성능을 달성하면서 복잡한 작업에서의 도전 과제를 강조합니다. EHR-MCP는 안전하고 일관된 데이터 접근을 위한 인프라를 제공하며, 병원 AI 에이전트의 기초로 활용될 수 있습니다. 향후 연구는 검색을 넘어 추론, 생성 및 임상적 영향 평가로 확장되어, 생성적 AI의 임상 실무 통합을 위한 효과적인 길을 열어야 합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 병원의 전자 건강 기록(EHR) 시스템과 통합하여 임상적으로 중요한 정보를 자동으로 검색할 수 있는지 평가합니다. 연구진은 EHR-MCP라는 프레임워크를 개발하여 GPT-4.1을 통해 병원 EHR 데이터베이스와 상호작용하도록 했습니다. 감염 통제 팀의 사례에서 파생된 6가지 과제를 테스트한 결과, 대부분의 과제에서 거의 완벽한 정확도를 보였으나, 시간 의존적 계산이 필요한 복잡한 과제에서는 성능이 떨어졌습니다. LLM은 간단한 작업에서 높은 성능을 보였으며, EHR-MCP는 안전하고 일관된 데이터 접근을 위한 기반을 제공할 수 있습니다. 향후 연구는 데이터 검색을 넘어 추론, 생성 및 임상적 영향 평가로 확장되어야 합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 병원 내 배치는 전자 건강 기록(EHR) 시스템 접근 제한으로 제한되고 있다.

- 2. 모델 컨텍스트 프로토콜(MCP)은 LLM과 외부 도구 간의 통합을 가능하게 한다.

- 3. EHR-MCP는 병원 EHR 데이터베이스와 통합된 맞춤형 MCP 도구 프레임워크로, GPT-4.1을 사용하여 상호작용한다.

- 4. LLM은 단순한 작업에서 거의 완벽한 성능을 보였으나, 시간 의존적 계산이 필요한 복잡한 작업에서는 성능이 저하되었다.

- 5. EHR-MCP는 안전하고 일관된 데이터 접근을 위한 인프라를 제공하며, 병원 AI 에이전트의 기반이 될 수 있다.

---

*Generated on 2025-09-22 13:46:39*