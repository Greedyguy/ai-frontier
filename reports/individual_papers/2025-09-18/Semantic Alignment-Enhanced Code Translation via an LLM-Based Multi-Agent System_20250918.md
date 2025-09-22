
# Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System

**Korean Title:** 의미적 정렬 강화 코드 번역: LLM 기반 다중 에이전트 시스템을 통한 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-agent System

## 🔗 유사한 논문
- [[An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (84.4% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (83.0% similar)
- [[CrowdAgent Multi-Agent Managed Multi-Source Annotation System]] (81.0% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (80.3% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.19894v4 Announce Type: replace-cross 
Abstract: Code translation converts code from one programming language to another while maintaining its original functionality, which is crucial for software migration, system refactoring, and cross-platform development. Traditional rule-based methods rely on manually-written rules, which can be time-consuming and often result in less readable code. To overcome this, learning-based methods have been developed, leveraging parallel data to train models for automated code translation. More recently, the advance of Large Language Models (LLMs) further boosts learning-based code translation. Although promising, LLM-translated program still suffers from diverse quality issues (e.g., syntax errors and semantic errors). In particular, it can be challenging for LLMs to self-debug these errors when simply provided with the corresponding error messages.
  In this work, we propose a novel LLM-based multi-agent system TRANSAGENT, which enhances LLM-based code translation by fixing the syntax errors and semantic errors with the synergy between four LLM-based agents, including Initial Code Translator, Syntax Error Fixer, Code Aligner, and Semantic Error Fixer. The main insight of TRANSAGENT is to first localize the error code block in the target program based on the execution alignment between the target and source program, which can narrow down the fixing space and thus lower down the fixing difficulties. To evaluate TRANSAGENT, we first construct a new benchmark from recent programming tasks to mitigate the potential data leakage issue. On our benchmark, TRANSAGENT outperforms the latest LLM-based code translation technique UniTrans in both translation effectiveness and efficiency; additionally, our evaluation on different LLMs show the generalization of TRANSAGENT and our ablation study shows the contribution of each agent.

## 🔍 Abstract (한글 번역)

arXiv:2409.19894v4 공지 유형: replace-cross
초록: 코드 번역은 원래 기능을 유지하면서 한 프로그래밍 언어에서 다른 언어로 코드를 변환하는 것으로, 소프트웨어 마이그레이션, 시스템 리팩토링, 크로스 플랫폼 개발에 필수적이다. 전통적인 규칙 기반 방법은 수동으로 작성된 규칙에 의존하며, 이는 시간이 많이 소요되고 종종 가독성이 떨어지는 코드를 생성한다. 이를 극복하기 위해 병렬 데이터를 활용하여 자동화된 코드 번역을 위한 모델을 훈련하는 학습 기반 방법이 개발되었다. 최근에는 대규모 언어 모델(LLM)의 발전이 학습 기반 코드 번역을 더욱 향상시켰다. 유망하지만, LLM으로 번역된 프로그램은 여전히 다양한 품질 문제(예: 구문 오류 및 의미 오류)를 겪고 있다. 특히, 단순히 해당 오류 메시지만 제공받았을 때 LLM이 이러한 오류를 자체 디버깅하는 것은 어려울 수 있다.

본 연구에서는 Initial Code Translator, Syntax Error Fixer, Code Aligner, Semantic Error Fixer를 포함한 네 개의 LLM 기반 에이전트 간의 시너지를 통해 구문 오류와 의미 오류를 수정함으로써 LLM 기반 코드 번역을 향상시키는 새로운 LLM 기반 다중 에이전트 시스템 TRANSAGENT를 제안한다. TRANSAGENT의 핵심 통찰은 먼저 타겟 프로그램과 소스 프로그램 간의 실행 정렬을 기반으로 타겟 프로그램에서 오류 코드 블록을 지역화하는 것으로, 이는 수정 공간을 좁혀 수정 난이도를 낮출 수 있다. TRANSAGENT를 평가하기 위해, 잠재적인 데이터 누출 문제를 완화하기 위해 최근 프로그래밍 과제로부터 새로운 벤치마크를 구축했다. 우리의 벤치마크에서 TRANSAGENT는 번역 효과성과 효율성 모두에서 최신 LLM 기반 코드 번역 기법인 UniTrans를 능가했으며, 서로 다른 LLM에 대한 평가는 TRANSAGENT의 일반화 능력을 보여주고, 우리의 절제 연구는 각 에이전트의 기여도를 보여준다.

## 📝 요약

이 논문은 코드 번역의 품질을 향상시키기 위해 LLM(대형 언어 모델)을 기반으로 한 다중 에이전트 시스템인 TRANSAGENT를 제안합니다. 기존의 규칙 기반 방법은 시간이 많이 소요되고 가독성이 떨어지는 문제를 가지고 있으며, LLM을 활용한 번역은 여전히 문법 및 의미 오류가 발생할 수 있습니다. TRANSAGENT는 초기 코드 번역기, 문법 오류 수정기, 코드 정렬기, 의미 오류 수정기 등 네 가지 에이전트를 통해 이러한 오류를 수정합니다. 특히, 소스 프로그램과 타겟 프로그램 간의 실행 정렬을 통해 오류 코드 블록을 국지화하여 수정 난이도를 낮춥니다. 새로운 벤치마크를 통해 평가한 결과, TRANSAGENT는 최신 LLM 기반 코드 번역 기술인 UniTrans보다 번역 효과성과 효율성에서 우수한 성능을 보였으며, 다양한 LLM에 대한 일반화 가능성도 입증되었습니다.

## 🎯 주요 포인트

- 1. 코드 번역은 소프트웨어 마이그레이션, 시스템 리팩토링, 크로스 플랫폼 개발에 필수적이며, 이를 자동화하기 위해 학습 기반 방법이 개발되었습니다.

- 2. 대형 언어 모델(LLM)의 발전은 학습 기반 코드 번역을 더욱 향상시켰으나, 여전히 문법 오류 및 의미 오류와 같은 다양한 품질 문제를 겪고 있습니다.

- 3. TRANSAGENT는 LLM 기반의 다중 에이전트 시스템으로, 문법 및 의미 오류를 수정하여 코드 번역의 품질을 향상시킵니다.

- 4. TRANSAGENT는 대상 프로그램과 소스 프로그램 간의 실행 정렬을 기반으로 오류 코드 블록을 먼저 지역화하여 수정 난이도를 낮춥니다.

- 5. 새로운 벤치마크 평가에서 TRANSAGENT는 최신 LLM 기반 코드 번역 기술인 UniTrans보다 번역 효과성과 효율성에서 우수한 성능을 보였습니다.

---

*Generated on 2025-09-19 10:59:26*