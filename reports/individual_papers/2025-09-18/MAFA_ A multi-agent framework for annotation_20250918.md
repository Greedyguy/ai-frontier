
# MAFA: A multi-agent framework for annotation

**Korean Title:** MAFA: 어노테이션을 위한 멀티 에이전트 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Structured Reasoning Approach

## 🔗 유사한 논문
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (82.8% similar)
- [[CrowdAgent Multi-Agent Managed Multi-Source Annotation System]] (81.3% similar)
- [[Synthesizing Behaviorally-Grounded Reasoning Chains A Data-Generation Framework for Personal Finance LLMs]] (80.8% similar)
- [[Co-Investigator AI The Rise of Agentic AI for Smarter, Trustworthy AML Compliance Narratives]] (80.8% similar)
- [[Inject, Fork, Compare Defining an Interaction Vocabulary for Multi-Agent Simulation Platforms]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.13668v2 Announce Type: replace 
Abstract: Modern consumer banking applications require accurate and efficient retrieval of information in response to user queries. Mapping user utterances to the most relevant Frequently Asked Questions (FAQs) is a crucial component of these systems. Traditional approaches often rely on a single model or technique, which may not capture the nuances of diverse user inquiries. In this paper, we introduce a multi-agent framework for FAQ annotation that combines multiple specialized agents with different approaches and a judge agent that reranks candidates to produce optimal results. Our agents utilize a structured reasoning approach inspired by Attentive Reasoning Queries (ARQs), which guides them through systematic reasoning steps using targeted, task-specific JSON queries. Our framework features a few-shot example strategy, where each agent receives different few-shots, enhancing ensemble diversity and coverage of the query space. We evaluate our framework on a real-world major bank dataset as well as public benchmark datasets (LCQMC and FiQA), demonstrating significant improvements over single-agent approaches across multiple metrics, including a 14% increase in Top-1 accuracy, an 18% increase in Top-5 accuracy, and a 12% improvement in Mean Reciprocal Rank on our dataset, and similar gains on public benchmarks when compared with traditional and single-agent annotation techniques. Our framework is particularly effective at handling ambiguous queries, making it well-suited for deployment in production banking applications while showing strong generalization capabilities across different domains and languages.

## 🔍 Abstract (한글 번역)

arXiv:2505.13668v2 공지 유형: 교체
초록: 현대 소비자 뱅킹 애플리케이션은 사용자 쿼리에 대응하여 정확하고 효율적인 정보 검색을 요구한다. 사용자 발화를 가장 관련성 높은 자주 묻는 질문(FAQs)에 매핑하는 것은 이러한 시스템의 핵심 구성 요소이다. 전통적인 접근법은 종종 단일 모델이나 기법에 의존하는데, 이는 다양한 사용자 문의의 미묘한 차이를 포착하지 못할 수 있다. 본 논문에서는 서로 다른 접근법을 가진 여러 특화된 에이전트와 최적의 결과를 도출하기 위해 후보를 재순위화하는 판정 에이전트를 결합한 FAQ 주석을 위한 멀티 에이전트 프레임워크를 소개한다. 우리의 에이전트들은 주의적 추론 쿼리(Attentive Reasoning Queries, ARQs)에서 영감을 받은 구조화된 추론 접근법을 활용하며, 이는 목표 지향적이고 작업별 특화된 JSON 쿼리를 사용하여 체계적인 추론 단계를 통해 에이전트들을 안내한다. 우리의 프레임워크는 각 에이전트가 서로 다른 few-shot을 받는 few-shot 예시 전략을 특징으로 하며, 이는 앙상블 다양성과 쿼리 공간의 커버리지를 향상시킨다. 우리는 실제 주요 은행 데이터셋과 공개 벤치마크 데이터셋(LCQMC 및 FiQA)에서 우리의 프레임워크를 평가하여, 우리 데이터셋에서 Top-1 정확도 14% 증가, Top-5 정확도 18% 증가, 평균 역순위(Mean Reciprocal Rank) 12% 개선을 포함하여 여러 지표에서 단일 에이전트 접근법 대비 상당한 개선을 보여주었으며, 전통적 및 단일 에이전트 주석 기법과 비교했을 때 공개 벤치마크에서도 유사한 성과를 달성했다. 우리의 프레임워크는 특히 모호한 쿼리 처리에 효과적이어서 프로덕션 뱅킹 애플리케이션에 배포하기에 매우 적합하며, 서로 다른 도메인과 언어에서 강력한 일반화 능력을 보여준다.

## 📝 요약

현대 소비자 은행 애플리케이션에서는 사용자 문의에 대한 정확하고 효율적인 정보 검색이 필수적입니다. 본 논문에서는 FAQ 주석을 위한 다중 에이전트 프레임워크를 제안합니다. 이 프레임워크는 다양한 접근 방식을 가진 여러 전문 에이전트와 후보를 재정렬하는 판정 에이전트를 결합하여 최적의 결과를 도출합니다. 에이전트들은 ARQ(Attentive Reasoning Queries)에서 영감을 받은 구조화된 추론 접근 방식을 사용하며, 이를 통해 체계적인 추론 단계를 수행합니다. 또한, 에이전트마다 다른 예시를 제공하는 몇 샷 전략을 통해 쿼리 공간의 다양성과 범위를 확장합니다. 주요 은행 데이터셋과 공개 벤치마크 데이터셋(LCQMC, FiQA)에서 프레임워크를 평가한 결과, 단일 에이전트 접근법에 비해 여러 지표에서 성능이 크게 향상되었습니다. 특히, 모호한 쿼리 처리에 효과적이며, 다양한 도메인과 언어에서도 강력한 일반화 능력을 보여줍니다.

## 🎯 주요 포인트

- 1. 현대 소비자 은행 애플리케이션에서는 사용자 쿼리에 대한 정확하고 효율적인 정보 검색이 필수적입니다.

- 2. 본 논문에서는 다양한 접근 방식을 결합한 다중 에이전트 프레임워크를 제안하여 FAQ 주석 작업의 최적화를 도모합니다.

- 3. 제안된 프레임워크는 Attentive Reasoning Queries에서 영감을 받은 구조적 추론 접근 방식을 활용하여 체계적인 추론 단계를 수행합니다.

- 4. 몇 가지 샷 예제 전략을 통해 에이전트 간의 다양성과 쿼리 공간의 커버리지를 향상시킵니다.

- 5. 제안된 프레임워크는 주요 은행 데이터셋과 공공 벤치마크 데이터셋에서 전통적 및 단일 에이전트 접근법을 능가하는 성능을 보였습니다.

---

*Generated on 2025-09-19 10:53:00*