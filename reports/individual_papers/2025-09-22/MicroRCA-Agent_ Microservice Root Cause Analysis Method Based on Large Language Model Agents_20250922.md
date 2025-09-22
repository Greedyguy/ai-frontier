# MicroRCA-Agent: Microservice Root Cause Analysis Method Based on Large Language Model Agents

**Korean Title:** 마이크로RCA-에이전트: 대형 언어 모델 에이전트를 기반으로 한 마이크로서비스 근본 원인 분석 방법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-modal Reasoning

## 🔗 유사한 논문
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (82.8% similar)
- [[2025-09-19/Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents_20250919|Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents]] (81.9% similar)
- [[2025-09-22/MICA_ Multi-Agent Industrial Coordination Assistant_20250922|MICA Multi-Agent Industrial Coordination Assistant]] (81.7% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (81.1% similar)
- [[2025-09-19/RationAnomaly_ Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning_20250919|RationAnomaly Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning]] (80.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15635v1 Announce Type: new 
Abstract: This paper presents MicroRCA-Agent, an innovative solution for microservice root cause analysis based on large language model agents, which constructs an intelligent fault root cause localization system with multimodal data fusion. The technical innovations are embodied in three key aspects: First, we combine the pre-trained Drain log parsing algorithm with multi-level data filtering mechanism to efficiently compress massive logs into high-quality fault features. Second, we employ a dual anomaly detection approach that integrates Isolation Forest unsupervised learning algorithms with status code validation to achieve comprehensive trace anomaly identification. Third, we design a statistical symmetry ratio filtering mechanism coupled with a two-stage LLM analysis strategy to enable full-stack phenomenon summarization across node-service-pod hierarchies. The multimodal root cause analysis module leverages carefully designed cross-modal prompts to deeply integrate multimodal anomaly information, fully exploiting the cross-modal understanding and logical reasoning capabilities of large language models to generate structured analysis results encompassing fault components, root cause descriptions, and reasoning trace. Comprehensive ablation studies validate the complementary value of each modal data and the effectiveness of the system architecture. The proposed solution demonstrates superior performance in complex microservice fault scenarios, achieving a final score of 50.71. The code has been released at: https://github.com/tangpan360/MicroRCA-Agent.

## 🔍 Abstract (한글 번역)

arXiv:2509.15635v1 발표 유형: 신규  
초록: 이 논문은 대형 언어 모델 에이전트를 기반으로 한 마이크로서비스 근본 원인 분석을 위한 혁신적인 솔루션인 MicroRCA-Agent를 제시하며, 다중 모달 데이터 융합을 통해 지능형 결함 근본 원인 위치 시스템을 구축합니다. 기술적 혁신은 세 가지 주요 측면에서 구현됩니다. 첫째, 사전 학습된 Drain 로그 파싱 알고리즘과 다중 레벨 데이터 필터링 메커니즘을 결합하여 대량의 로그를 효율적으로 압축하여 고품질의 결함 특징을 도출합니다. 둘째, Isolation Forest 비지도 학습 알고리즘과 상태 코드 검증을 통합한 이중 이상 탐지 접근 방식을 사용하여 포괄적인 추적 이상 식별을 달성합니다. 셋째, 통계적 대칭 비율 필터링 메커니즘과 2단계 LLM 분석 전략을 설계하여 노드-서비스-포드 계층 전반에 걸친 전체 스택 현상 요약을 가능하게 합니다. 다중 모달 근본 원인 분석 모듈은 신중하게 설계된 교차 모달 프롬프트를 활용하여 다중 모달 이상 정보를 깊이 통합하며, 대형 언어 모델의 교차 모달 이해 및 논리적 추론 능력을 최대한 활용하여 결함 구성 요소, 근본 원인 설명 및 추론 추적을 포함하는 구조화된 분석 결과를 생성합니다. 종합적인 소거 연구는 각 모달 데이터의 상호 보완적 가치를 검증하고 시스템 아키텍처의 효과성을 입증합니다. 제안된 솔루션은 복잡한 마이크로서비스 결함 시나리오에서 우수한 성능을 보여주며, 최종 점수 50.71을 달성했습니다. 코드는 다음에서 공개되었습니다: https://github.com/tangpan360/MicroRCA-Agent.

## 📝 요약

이 논문은 대규모 언어 모델 에이전트를 기반으로 한 마이크로서비스 근본 원인 분석 솔루션인 MicroRCA-Agent를 제안합니다. 주요 기여는 세 가지로 요약됩니다. 첫째, Drain 로그 파싱 알고리즘과 다단계 데이터 필터링을 결합하여 대량의 로그를 고품질의 결함 특징으로 압축합니다. 둘째, Isolation Forest 비지도 학습 알고리즘과 상태 코드 검증을 통합한 이중 이상 탐지 방법을 통해 포괄적인 추적 이상 식별을 수행합니다. 셋째, 통계적 대칭 비율 필터링 메커니즘과 2단계 LLM 분석 전략을 설계하여 노드-서비스-포드 계층 전반에 걸친 현상 요약을 가능하게 합니다. 이 시스템은 복잡한 마이크로서비스 결함 시나리오에서 우수한 성능을 보이며, 최종 점수 50.71을 기록했습니다. 코드는 GitHub에서 공개되었습니다.

## 🎯 주요 포인트

- 1. MicroRCA-Agent는 대형 언어 모델 에이전트를 기반으로 한 마이크로서비스 근본 원인 분석 솔루션으로, 멀티모달 데이터 융합을 통해 지능형 고장 원인 위치 시스템을 구축합니다.

- 2. Drain 로그 파싱 알고리즘과 다단계 데이터 필터링 메커니즘을 결합하여 대량의 로그를 고품질 고장 특징으로 효율적으로 압축합니다.

- 3. Isolation Forest 비지도 학습 알고리즘과 상태 코드 검증을 통합한 이중 이상 탐지 접근 방식을 사용하여 포괄적인 추적 이상 식별을 달성합니다.

- 4. 통계적 대칭 비율 필터링 메커니즘과 2단계 LLM 분석 전략을 설계하여 노드-서비스-포드 계층 전반에 걸쳐 현상 요약을 가능하게 합니다.

- 5. 제안된 솔루션은 복잡한 마이크로서비스 고장 시나리오에서 우수한 성능을 보여주며, 최종 점수 50.71을 달성했습니다.

---

*Generated on 2025-09-22 13:44:49*