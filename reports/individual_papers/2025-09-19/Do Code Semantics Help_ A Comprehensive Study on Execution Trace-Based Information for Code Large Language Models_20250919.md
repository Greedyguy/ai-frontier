
# Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models

**Korean Title:** 코드 의미론이 도움이 되는가? 대규모 언어 모델을 위한 실행 추적 기반 정보에 대한 포괄적인 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Semantic Information Integration

## 🔗 유사한 논문
- [[Reasoning Efficiently Through Adaptive Chain-of-Thought Compression A Self-Optimizing Framework]] (82.5% similar)
- [[Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.2% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (81.6% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.1% similar)
- [[An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (81.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11686v2 Announce Type: replace-cross 
Abstract: Code Large Language Models (Code LLMs) have opened a new era in programming with their impressive capabilities. However, recent research has revealed critical limitations in their ability to reason about runtime behavior and understand the actual functionality of programs, which poses significant challenges for their post-training and practical deployment. Specifically, Code LLMs encounter two principal issues: (1) a lack of proficiency in reasoning about program execution behavior, as they struggle to interpret what programs actually do during runtime, and (2) the inconsistent and fragmented representation of semantic information, such as execution traces, across existing methods, which hinders their ability to generalize and reason effectively. These challenges underscore the necessity for more systematic approaches to enhance the reasoning capabilities of Code LLMs. To address these issues, we introduce a generic framework to support integrating semantic information~(e.g., execution trace) to code task-relevant prompts, and conduct a comprehensive study to explore the role of semantic information in enhancing the reasoning ability of Code LLMs accordingly. Specifically, we focus on investigating the usefulness of trace-based semantic information in boosting supervised fine-tuning~(SFT) and post-phase inference of Code LLMs. The experimental results surprisingly disagree with previous works and demonstrate that semantic information has limited usefulness for SFT and test time scaling of Code LLM.

## 🔍 Abstract (한글 번역)

arXiv:2509.11686v2 발표 유형: 교차 교체  
초록: 코드 대형 언어 모델(Code LLMs)은 그들의 인상적인 능력으로 프로그래밍의 새로운 시대를 열었습니다. 그러나 최근 연구는 이들이 런타임 동작에 대한 추론과 프로그램의 실제 기능을 이해하는 데 있어 중요한 한계를 가지고 있음을 밝혀냈습니다. 이는 그들의 사후 훈련 및 실질적인 배포에 상당한 도전을 제기합니다. 구체적으로, 코드 LLMs는 두 가지 주요 문제에 직면합니다: (1) 프로그램 실행 동작에 대한 추론 능력의 부족, 즉 런타임 동안 프로그램이 실제로 무엇을 하는지 해석하는 데 어려움을 겪고 있으며, (2) 실행 추적과 같은 의미 정보의 일관되지 않고 단편적인 표현이 기존 방법 전반에 걸쳐 존재하여 일반화하고 효과적으로 추론하는 능력을 방해합니다. 이러한 문제들은 코드 LLMs의 추론 능력을 향상시키기 위한 보다 체계적인 접근의 필요성을 강조합니다. 이러한 문제를 해결하기 위해, 우리는 코드 작업 관련 프롬프트에 의미 정보를 통합하는 것을 지원하는 일반적인 프레임워크를 소개하고, 코드 LLMs의 추론 능력을 향상시키는 데 있어 의미 정보의 역할을 탐구하기 위한 포괄적인 연구를 수행합니다. 구체적으로, 우리는 코드 LLMs의 감독된 미세 조정(SFT) 및 사후 단계 추론을 향상시키는 데 있어 추적 기반 의미 정보의 유용성을 조사하는 데 중점을 둡니다. 실험 결과는 이전 연구와 놀랍게도 일치하지 않으며, 의미 정보가 SFT 및 코드 LLM의 테스트 시간 확장에 제한적인 유용성을 가진다는 것을 보여줍니다.

## 📝 요약

Code LLMs는 프로그래밍 분야에서 새로운 가능성을 열었지만, 실행 중인 프로그램의 동작을 이해하는 데 한계가 있습니다. 특히, 프로그램 실행 시의 행동을 해석하는 능력이 부족하고, 기존 방법들이 실행 추적과 같은 의미 정보를 일관되게 제공하지 못해 일반화와 추론에 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 의미 정보를 코드 관련 프롬프트에 통합하는 일반적인 프레임워크를 제안하고, 의미 정보가 Code LLMs의 추론 능력을 향상시키는 역할을 탐구했습니다. 실험 결과, 의미 정보가 감독된 미세 조정(SFT)과 테스트 시 확장에 제한적인 유용성을 가진다는 것을 발견했습니다.

## 🎯 주요 포인트

- 1. Code LLMs는 실행 시 프로그램의 실제 기능을 이해하는 데 한계가 있으며, 이는 실질적인 배포에 도전 과제가 된다.

- 2. Code LLMs는 프로그램 실행 행동에 대한 추론 능력이 부족하고, 기존 방법에서의 의미 정보 표현이 일관되지 않고 단편적이다.

- 3. 의미 정보를 코드 작업 관련 프롬프트에 통합하는 일반적인 프레임워크를 제안하여 Code LLMs의 추론 능력을 향상시키고자 한다.

- 4. 실험 결과, 의미 정보는 Code LLMs의 감독된 미세 조정(SFT) 및 테스트 시 확장에 제한적인 유용성을 보였다.

---

*Generated on 2025-09-19 15:23:05*