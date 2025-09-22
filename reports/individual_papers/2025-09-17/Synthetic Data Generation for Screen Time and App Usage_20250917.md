# Synthetic Data Generation for Screen Time and App Usage

**Korean Title:** 스크린 타임 및 앱 사용에 대한 합성 데이터 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Gustavo Kruger|Gustavo Kruger]] [[authors/Nikhil Sachdeva|Nikhil Sachdeva]] [[authors/Michael Sobolev|Michael Sobolev]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Use Case Specific Evaluation Metrics

## 🔗 유사한 논문
- [[Single- vs. Dual-Prompt Dialogue Generation with LLMs for Job Interviews in Human Resources_20250919|Single- vs. Dual-Prompt Dialogue Generation with LLMs for Job Interviews in Human Resources]] (81.6% similar)
- [[Catch Me If You Can Not Yet_ LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors_20250918|Catch Me If You Can Not Yet LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors]] (80.6% similar)
- [[JU-NLP at Touch'e_ Covert Advertisement in Conversational AI-Generation and Detection Strategies_20250919|JU-NLP at Touch'e Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (79.9% similar)
- [[On the Use of Agentic Coding_ An Empirical Study of Pull Requests on GitHub_20250919|On the Use of Agentic Coding An Empirical Study of Pull Requests on GitHub]] (79.2% similar)
- [[Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (79.1% similar)

## 📋 저자 정보

**Authors:** Gustavo Kruger, Nikhil Sachdeva, Michael Sobolev

## 📄 Abstract (원문)

Smartphone usage data can provide valuable insights for understanding
interaction with technology and human behavior. However, collecting
large-scale, in-the-wild smartphone usage logs is challenging due to high
costs, privacy concerns, under representative user samples and biases like
non-response that can skew results. These challenges call for exploring
alternative approaches to obtain smartphone usage datasets. In this context,
large language models (LLMs) such as Open AI's ChatGPT present a novel approach
for synthetic smartphone usage data generation, addressing limitations of
real-world data collection. We describe a case study on how four prompt
strategies influenced the quality of generated smartphone usage data. We
contribute with insights on prompt design and measures of data quality,
reporting a prompting strategy comparison combining two factors, prompt level
of detail (describing a user persona, describing the expected results
characteristics) and seed data inclusion (with versus without an initial real
usage example). Our findings suggest that using LLMs to generate structured and
behaviorally plausible smartphone use datasets is feasible for some use cases,
especially when using detailed prompts. Challenges remain in capturing diverse
nuances of human behavioral patterns in a single synthetic dataset, and
evaluating tradeoffs between data fidelity and diversity, suggesting the need
for use-case-specific evaluation metrics and future research with more diverse
seed data and different LLM models.

## 🔍 Abstract (한글 번역)

스마트폰 사용 데이터는 기술과의 상호작용 및 인간 행동을 이해하는 데 있어 귀중한 통찰력을 제공할 수 있습니다. 그러나 대규모의 자연 상태에서의 스마트폰 사용 로그를 수집하는 것은 높은 비용, 프라이버시 문제, 대표성이 부족한 사용자 샘플, 그리고 결과를 왜곡할 수 있는 무응답과 같은 편향 때문에 어려움을 겪고 있습니다. 이러한 도전 과제는 스마트폰 사용 데이터셋을 얻기 위한 대체 접근 방식을 탐색할 필요성을 제기합니다. 이와 같은 맥락에서, Open AI의 ChatGPT와 같은 대형 언어 모델(LLM)은 실제 데이터 수집의 한계를 해결하는 합성 스마트폰 사용 데이터 생성의 새로운 접근 방식을 제시합니다. 우리는 네 가지 프롬프트 전략이 생성된 스마트폰 사용 데이터의 품질에 어떻게 영향을 미쳤는지에 대한 사례 연구를 설명합니다. 우리는 프롬프트 설계와 데이터 품질 측정에 대한 통찰력을 제공하며, 사용자 페르소나 설명, 예상 결과 특성 설명과 같은 프롬프트의 세부 수준과 초기 실제 사용 예시 포함 여부(포함 대 미포함)를 결합한 프롬프트 전략 비교를 보고합니다. 우리의 연구 결과는 LLM을 사용하여 구조적이고 행동적으로 그럴듯한 스마트폰 사용 데이터셋을 생성하는 것이 일부 사용 사례에서 특히 상세한 프롬프트를 사용할 때 가능하다는 것을 시사합니다. 단일 합성 데이터셋에서 인간 행동 패턴의 다양한 뉘앙스를 포착하는 데 여전히 어려움이 있으며, 데이터 충실도와 다양성 간의 균형을 평가하는 데 있어 사용 사례별 평가 지표와 더 다양한 시드 데이터 및 다른 LLM 모델을 활용한 향후 연구의 필요성을 제안합니다.

## 📝 요약

이 논문은 스마트폰 사용 데이터를 대규모로 수집하는 어려움을 해결하기 위해 대형 언어 모델(LLM)을 활용한 합성 데이터 생성 방법을 제안합니다. 연구는 Open AI의 ChatGPT를 사용하여 네 가지 프롬프트 전략이 데이터 품질에 미치는 영향을 분석했습니다. 프롬프트의 세부 수준과 초기 실제 사용 예시의 포함 여부가 데이터 생성에 어떻게 영향을 미치는지를 비교했습니다. 연구 결과, 상세한 프롬프트를 사용할 경우 LLM을 통해 구조적이고 행동적으로 타당한 스마트폰 사용 데이터를 생성할 수 있음을 발견했습니다. 그러나 인간 행동 패턴의 다양한 뉘앙스를 포착하는 데는 여전히 한계가 있으며, 데이터의 정확성과 다양성 간의 균형을 평가하기 위한 구체적인 평가 지표가 필요함을 시사합니다.

## 🎯 주요 포인트

- 1. 스마트폰 사용 데이터 수집은 비용, 프라이버시 문제, 대표성 부족 등으로 인해 어려움이 존재합니다.

- 2. 대규모 언어 모델(LLM)인 ChatGPT를 활용하여 합성 스마트폰 사용 데이터를 생성하는 새로운 접근법을 제시합니다.

- 3. 네 가지 프롬프트 전략이 생성된 스마트폰 사용 데이터의 품질에 미치는 영향을 사례 연구를 통해 분석했습니다.

- 4. 프롬프트의 세부 수준과 초기 실사용 예시 포함 여부에 따른 프롬프트 전략 비교 결과를 보고합니다.

- 5. LLM을 사용하여 구조적이고 행동적으로 그럴듯한 스마트폰 사용 데이터를 생성하는 것이 일부 사용 사례에서 가능함을 발견했습니다.

---

*Generated on 2025-09-20 09:25:59*