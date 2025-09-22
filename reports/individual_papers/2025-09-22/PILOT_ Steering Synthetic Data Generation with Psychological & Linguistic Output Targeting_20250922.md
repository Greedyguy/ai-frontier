# PILOT: Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting

**Korean Title:** 파일럿: 심리학적 및 언어학적 출력 목표 설정을 통한 합성 데이터 생성 조정

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hybrid Persona-Schema Steering

## 🔗 유사한 논문
- [[2025-09-18/Designing AI-Agents with Personalities_ A Psychometric Approach_20250918|Designing AI-Agents with Personalities A Psychometric Approach]] (80.3% similar)
- [[2025-09-18/SPAR_ Scalable LLM-based PDDL Domain Generation for Aerial Robotics_20250918|SPAR Scalable LLM-based PDDL Domain Generation for Aerial Robotics]] (79.9% similar)
- [[2025-09-19/Learning in Context_ Personalizing Educational Content with Large Language Models to Enhance Student Learning_20250919|Learning in Context Personalizing Educational Content with Large Language Models to Enhance Student Learning]] (79.9% similar)
- [[2025-09-18/Catch Me If You Can Not Yet_ LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors_20250918|Catch Me If You Can Not Yet LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors]] (79.7% similar)
- [[2025-09-18/$Agent^2$_ An Agent-Generates-Agent Framework for Reinforcement Learning Automation_20250918|$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15447v1 Announce Type: cross 
Abstract: Generative AI applications commonly leverage user personas as a steering mechanism for synthetic data generation, but reliance on natural language representations forces models to make unintended inferences about which attributes to emphasize, limiting precise control over outputs. We introduce PILOT (Psychological and Linguistic Output Targeting), a two-phase framework for steering large language models with structured psycholinguistic profiles. In Phase 1, PILOT translates natural language persona descriptions into multidimensional profiles with normalized scores across linguistic and psychological dimensions. In Phase 2, these profiles guide generation along measurable axes of variation. We evaluate PILOT across three state-of-the-art LLMs (Mistral Large 2, Deepseek-R1, LLaMA 3.3 70B) using 25 synthetic personas under three conditions: Natural-language Persona Steering (NPS), Schema-Based Steering (SBS), and Hybrid Persona-Schema Steering (HPS). Results demonstrate that schema-based approaches significantly reduce artificial-sounding persona repetition while improving output coherence, with silhouette scores increasing from 0.098 to 0.237 and topic purity from 0.773 to 0.957. Our analysis reveals a fundamental trade-off: SBS produces more concise outputs with higher topical consistency, while NPS offers greater lexical diversity but reduced predictability. HPS achieves a balance between these extremes, maintaining output variety while preserving structural consistency. Expert linguistic evaluation confirms that PILOT maintains high response quality across all conditions, with no statistically significant differences between steering approaches.

## 🔍 Abstract (한글 번역)

arXiv:2509.15447v1 발표 유형: 교차  
초록: 생성적 인공지능 애플리케이션은 종종 사용자 페르소나를 합성 데이터 생성의 조정 메커니즘으로 활용하지만, 자연어 표현에 의존함으로써 모델이 강조할 속성에 대해 의도하지 않은 추론을 하게 되어 출력에 대한 정확한 제어가 제한됩니다. 우리는 구조화된 심리언어학적 프로파일을 사용하여 대형 언어 모델을 조정하는 두 단계 프레임워크인 PILOT(Psychological and Linguistic Output Targeting)을 소개합니다. 1단계에서 PILOT는 자연어 페르소나 설명을 언어적 및 심리적 차원에서 정규화된 점수를 가진 다차원 프로파일로 변환합니다. 2단계에서는 이러한 프로파일이 측정 가능한 변동 축을 따라 생성을 안내합니다. 우리는 Mistral Large 2, Deepseek-R1, LLaMA 3.3 70B 세 가지 최첨단 대형 언어 모델을 사용하여 25개의 합성 페르소나를 세 가지 조건(Natural-language Persona Steering, Schema-Based Steering, Hybrid Persona-Schema Steering) 하에서 평가합니다. 결과는 스키마 기반 접근 방식이 인위적인 페르소나 반복을 크게 줄이고 출력 일관성을 향상시킨다는 것을 보여주며, 실루엣 점수는 0.098에서 0.237로, 주제 순도는 0.773에서 0.957로 증가했습니다. 우리의 분석은 근본적인 상충 관계를 드러냅니다: 스키마 기반 조정은 더 높은 주제 일관성을 가진 간결한 출력을 생성하는 반면, 자연어 페르소나 조정은 더 큰 어휘 다양성을 제공하지만 예측 가능성은 감소합니다. 하이브리드 페르소나-스키마 조정은 이러한 극단 사이에서 균형을 이루어 출력 다양성을 유지하면서 구조적 일관성을 보존합니다. 전문가의 언어 평가에 따르면 PILOT는 모든 조건에서 높은 응답 품질을 유지하며, 조정 접근 방식 간에 통계적으로 유의미한 차이는 없습니다.

## 📝 요약

이 논문은 생성 AI 애플리케이션에서 사용자 페르소나를 활용한 데이터 생성의 한계를 극복하기 위해 PILOT라는 프레임워크를 제안합니다. PILOT는 심리언어학적 프로필을 사용하여 대형 언어 모델을 조정하는 두 단계로 구성됩니다. 첫 번째 단계에서는 자연어 페르소나 설명을 다차원 프로필로 변환하고, 두 번째 단계에서는 이 프로필을 바탕으로 생성 과정을 조정합니다. 세 가지 조건(NPS, SBS, HPS)에서 세 가지 최신 LLM을 평가한 결과, SBS는 인위적인 반복을 줄이고 일관성을 개선하며, HPS는 다양성과 일관성의 균형을 유지하는 것으로 나타났습니다. 전문가 평가 결과, 모든 조건에서 높은 응답 품질이 유지되었습니다.

## 🎯 주요 포인트

- 1. PILOT는 자연어 기반 페르소나를 다차원 심리언어학적 프로필로 변환하여 대형 언어 모델을 조정하는 두 단계의 프레임워크입니다.

- 2. PILOT는 구조화된 프로필을 사용하여 생성 결과의 변화를 측정 가능한 축을 따라 유도합니다.

- 3. 연구 결과, Schema-Based Steering(SBS) 접근법은 인공적인 페르소나 반복을 줄이고 출력의 일관성을 향상시킵니다.

- 4. SBS는 주제 일관성이 높은 간결한 출력을 생성하며, Natural-language Persona Steering(NPS)은 어휘 다양성을 제공하지만 예측 가능성이 낮습니다.

- 5. Hybrid Persona-Schema Steering(HPS)는 출력 다양성과 구조적 일관성을 모두 유지하는 균형을 이룹니다.

---

*Generated on 2025-09-22 13:57:25*