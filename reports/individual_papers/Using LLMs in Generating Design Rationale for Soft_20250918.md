
# Using LLMs in Generating Design Rationale for Software Architecture Decisions

**Korean Title:** 소프트웨어 아키텍처 결정에 대한 설계 근거 생성에 LLM 사용하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-agent RAG|Multi-agent RAG]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Design Rationale|Design Rationale]] [[keywords/specific/Stack Overflow|Stack Overflow]] [[keywords/unique/Chain of Thought (CoT|Chain of Thought (CoT]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Text Comprehension
**🔬 Broad Technical**: Large Language Models, Design Rationale
**🔗 Specific Connectable**: Stack Overflow
**⭐ Unique Technical**: Chain of Thought (CoT

**ArXiv ID**: [2504.20781](https://arxiv.org/abs/2504.20781)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2504.20781.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Design Rationale` • 

`Stack Overflow` • 

`Chain of Thought (CoT` • 

`LLM-based Agents`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.20781v2 Announce Type: replace-cross 
Abstract: Design Rationale (DR) for software architecture decisions refers to the reasoning underlying architectural choices, which provides valuable insights into the different phases of the architecting process throughout software development. However, in practice, DR is often inadequately documented due to a lack of motivation and effort from developers. With the recent advancements in Large Language Models (LLMs), their capabilities in text comprehension, reasoning, and generation may enable the generation and recovery of DR for architecture decisions. In this study, we evaluated the performance of LLMs in generating DR for architecture decisions. First, we collected 50 Stack Overflow (SO) posts, 25 GitHub issues, and 25 GitHub discussions related to architecture decisions to construct a dataset of 100 architecture-related problems. Then, we selected five LLMs to generate DR for the architecture decisions with three prompting strategies, including zero-shot, chain of thought (CoT), and LLM-based agents. With the DR provided by human experts as ground truth, the Precision of LLM-generated DR with the three prompting strategies ranges from 0.267 to 0.278, Recall from 0.627 to 0.715, and F1-score from 0.351 to 0.389. Additionally, 64.45% to 69.42% of the arguments of DR not mentioned by human experts are also helpful, 4.12% to 4.87% of the arguments have uncertain correctness, and 1.59% to 3.24% of the arguments are potentially misleading. To further understand the trustworthiness and applicability of LLM-generated DR in practice, we conducted semi-structured interviews with six practitioners. Based on the experimental and interview results, we discussed the pros and cons of the three prompting strategies, the strengths and limitations of LLM-generated DR, and the implications for the practical use of LLM-generated DR.

## 🔍 Abstract (한글 번역)

arXiv:2504.20781v2 발표 유형: replace-cross
요약: 소프트웨어 아키텍처 결정에 대한 디자인 근거 (DR)는 아키텍처 선택에 대한 추론을 의미하며, 이는 소프트웨어 개발 과정 전체에서 아키텍처화 프로세스의 다양한 단계에 대한 유용한 통찰력을 제공합니다. 그러나 실제로는 DR이 개발자들의 동기 부여와 노력 부족으로 인해 부적절하게 문서화되는 경우가 많습니다. 최근 대형 언어 모델 (LLM)의 발전으로 인해 텍스트 이해, 추론 및 생성 능력이 향상되어 아키텍처 결정에 대한 DR의 생성 및 복구가 가능해질 수 있습니다. 본 연구에서는 LLM의 성능을 평가하여 아키텍처 결정에 대한 DR을 생성하는 능력을 조사했습니다. 먼저, 아키텍처 관련 문제 100개의 데이터셋을 구축하기 위해 50개의 Stack Overflow (SO) 게시물, 25개의 GitHub 이슈 및 25개의 GitHub 토론을 수집했습니다. 그런 다음, 세 가지 프롬프팅 전략을 사용하여 다섯 가지 LLM을 선택하여 아키텍처 결정에 대한 DR을 생성했습니다. 이때 사용된 프롬프팅 전략은 zero-shot, chain of thought (CoT), LLM 기반 에이전트입니다. 인간 전문가가 제공한 DR을 기준으로, 세 가지 프롬프팅 전략을 사용하여 생성된 LLM의 DR의 정밀도는 0.267에서 0.278, 재현율은 0.627에서 0.715, F1 점수는 0.351에서 0.389로 범위가 있습니다. 또한, 인간 전문가가 언급하지 않은 DR의 주장 중 64.45%에서 69.42%는 도움이 되며, 4.12%에서 4.87%는 불확실한 정확성을 가지고 있고, 1.59%에서 3.24%는 잠재적으로 오도하는 주장입니다. LLM이 생성한 DR의 신뢰성과 적용 가능성을 더 잘 이해하기 위해 우리는 6명의 실무자와 반구조화된 인터뷰를 실시했습니다. 실험 및 인터뷰 결과를 바탕으로, 세 가지 프롬프팅 전략의 장단점, LLM이 생성한 DR의 강점과 한계, 그리고 LLM이 생성한 DR의 실제 사용에 대한 함의에 대해 논의했습니다.

## 📝 요약

본 연구는 소프트웨어 아키텍처 결정에 대한 설계 근거 (DR)가 소프트웨어 개발 과정 전반에 걸쳐 아키텍처 선택에 대한 이유를 제공함으로써 가치 있는 통찰을 제공한다. 그러나 실제로 DR은 개발자들의 동기 부족과 노력 부족으로 인해 부적절하게 문서화되는 경우가 많다. 최근 대형 언어 모델 (LLMs)의 발전으로 인해 텍스트 이해, 추론 및 생성 능력이 향상되어 아키텍처 결정에 대한 DR의 생성 및 복구가 가능해졌다. 본 연구에서는 LLMs의 성능을 평가하고 100개의 아키텍처 관련 문제 데이터 세트를 구축하여 아키텍처 결정에 대한 DR을 생성하는 다양한 전략을 검토하였다. 실험 및 인터뷰 결과를 토대로 LLMs가 생성한 DR의 신뢰성과 적용 가능성을 논의하였다.

## 🎯 주요 포인트


- 1. 소프트웨어 아키텍처 결정에 대한 설계 근거는 소프트웨어 개발 과정의 다양한 단계에 대한 유용한 통찰을 제공한다.

- 2. 대형 언어 모델(LLMs)은 텍스트 이해, 추론 및 생성 능력을 통해 아키텍처 결정에 대한 설계 근거를 생성하고 복구할 수 있다.

- 3. LLMs를 사용하여 생성된 설계 근거의 정밀도는 0.267에서 0.278로 나타났으며, 리콜은 0.627에서 0.715로 나타났다.


---

*Generated on 2025-09-18 16:33:00*