# Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling

**Korean Title:** 지식 기반 환각 현상: 대규모 언어 모델에서의 프로세스 모델링에 관한 실증적 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Automated Process Modeling

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.8% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.2% similar)
- [[2025-09-18/From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy A Survey on Large Language Models in Scientific Discovery]] (84.6% similar)
- [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (84.3% similar)
- [[2025-09-17/Do Large Language Models Understand Word Senses_20250917|Do Large Language Models Understand Word Senses]] (83.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15336v1 Announce Type: new 
Abstract: The utility of Large Language Models (LLMs) in analytical tasks is rooted in their vast pre-trained knowledge, which allows them to interpret ambiguous inputs and infer missing information. However, this same capability introduces a critical risk of what we term knowledge-driven hallucination: a phenomenon where the model's output contradicts explicit source evidence because it is overridden by the model's generalized internal knowledge. This paper investigates this phenomenon by evaluating LLMs on the task of automated process modeling, where the goal is to generate a formal business process model from a given source artifact. The domain of Business Process Management (BPM) provides an ideal context for this study, as many core business processes follow standardized patterns, making it likely that LLMs possess strong pre-trained schemas for them. We conduct a controlled experiment designed to create scenarios with deliberate conflict between provided evidence and the LLM's background knowledge. We use inputs describing both standard and deliberately atypical process structures to measure the LLM's fidelity to the provided evidence. Our work provides a methodology for assessing this critical reliability issue and raises awareness of the need for rigorous validation of AI-generated artifacts in any evidence-based domain.

## 🔍 Abstract (한글 번역)

arXiv:2509.15336v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)의 분석 작업에서의 유용성은 방대한 사전 학습된 지식에 뿌리를 두고 있으며, 이를 통해 모호한 입력을 해석하고 누락된 정보를 추론할 수 있습니다. 그러나 이러한 능력은 모델의 일반화된 내부 지식에 의해 명시적인 출처 증거가 무시되어 모델의 출력이 이를 모순되게 하는 지식 기반 환각이라는 중요한 위험을 초래합니다. 본 논문은 주어진 소스 아티팩트로부터 형식적인 비즈니스 프로세스 모델을 생성하는 자동화된 프로세스 모델링 작업에서 LLM을 평가하여 이 현상을 조사합니다. 비즈니스 프로세스 관리(BPM) 분야는 많은 핵심 비즈니스 프로세스가 표준화된 패턴을 따르기 때문에 LLM이 이에 대한 강력한 사전 학습된 스키마를 보유할 가능성이 높아 본 연구에 이상적인 맥락을 제공합니다. 우리는 제공된 증거와 LLM의 배경 지식 간의 의도적인 충돌을 포함하는 시나리오를 생성하기 위해 설계된 통제된 실험을 수행합니다. 표준 및 의도적으로 비정형적인 프로세스 구조를 설명하는 입력을 사용하여 제공된 증거에 대한 LLM의 충실도를 측정합니다. 우리의 연구는 이 중요한 신뢰성 문제를 평가하기 위한 방법론을 제공하며, 증거 기반 도메인에서 AI 생성 아티팩트의 엄격한 검증 필요성에 대한 인식을 제고합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 분석 작업에서 유용하지만, 모델의 일반화된 내부 지식이 명시적 증거를 덮어쓰는 '지식 기반 환각' 현상을 초래할 수 있음을 지적합니다. 연구는 자동 프로세스 모델링 과제를 통해 이 현상을 조사하며, 비즈니스 프로세스 관리(BPM) 분야를 배경으로 삼아 실험을 진행했습니다. 실험은 제공된 증거와 LLM의 배경 지식 간의 충돌을 의도적으로 조성하여, 모델이 증거에 얼마나 충실한지를 평가했습니다. 이 연구는 AI 생성 산출물의 신뢰성을 평가하는 방법론을 제시하고, 증거 기반 분야에서의 엄격한 검증 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 광범위한 사전 학습 지식을 통해 모호한 입력을 해석하고 누락된 정보를 추론할 수 있지만, 이는 모델의 일반화된 내부 지식이 명시적 출처 증거를 덮어쓰는 지식 기반 환각의 위험을 초래할 수 있다.

- 2. 본 논문은 자동화된 프로세스 모델링 작업에서 LLM의 지식 기반 환각 현상을 조사하며, 이는 주어진 소스 아티팩트로부터 공식적인 비즈니스 프로세스 모델을 생성하는 것을 목표로 한다.

- 3. 비즈니스 프로세스 관리(BPM) 분야는 많은 핵심 비즈니스 프로세스가 표준화된 패턴을 따르기 때문에 LLM이 강력한 사전 학습 스키마를 가질 가능성이 높아 본 연구에 이상적인 맥락을 제공한다.

- 4. 제공된 증거와 LLM의 배경 지식 간의 의도적인 충돌을 포함한 시나리오를 만들기 위한 통제된 실험을 수행하여, LLM이 제공된 증거에 얼마나 충실한지를 측정한다.

- 5. 본 연구는 AI 생성 아티팩트의 엄격한 검증 필요성을 인식시키고, 증거 기반 도메인에서의 중요한 신뢰성 문제를 평가하기 위한 방법론을 제공한다.

---

*Generated on 2025-09-22 13:43:23*