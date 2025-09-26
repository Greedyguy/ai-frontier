---
keywords:
  - Large Language Models
  - Automated Issue Solving
  - SWE-Bench
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 23:02:01.586834",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Automated Issue Solving",
    "SWE-Bench"
  ],
  "rejected_keywords": [
    "Expert-Executor Framework"
  ],
  "similarity_scores": {
    "Large Language Models": 0.82,
    "Automated Issue Solving": 0.78,
    "SWE-Bench": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# An Empirical Study on Failures in Automated Issue Solving

**Korean Title:** 자동화된 문제 해결의 실패에 관한 실증적 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Automated Issue Solving|Automated Issue Solving]], [[keywords/SWE-Bench|SWE-Bench]]

## 🔗 유사한 논문
- [[Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents_20250919|Detecting Pipeline Failures through Fine-Grained Analysis of Web Agents]] (84.7% similar)
- [[AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (84.6% similar)
- [[SWE-QA_ Can Language Models Answer Repository-level Code Questions_20250919|SWE-QA Can Language Models Answer Repository-level Code Questions]] (82.8% similar)
- [[Who is Introducing the Failure Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis_20250918|Who is Introducing the Failure Automatically Attributing Failures of Multi-Agent Systems via Spectrum Analysis]] (81.9% similar)
- [[AEGIS_ Automated Error Generation and Identification for Multi-Agent Systems_20250919|AEGIS Automated Error Generation and Identification for Multi-Agent Systems]] (81.9% similar)

## 📋 저자 정보

**Authors:** Simiao Liu, Fang Liu, Liehao Li, Xin Tan, Yinghao Zhu, Xiaoli Lian, Li Zhang

## 📄 Abstract (원문)

Automated issue solving seeks to autonomously identify and repair defective
code snippets across an entire codebase. SWE-Bench has emerged as the most
widely adopted benchmark for evaluating progress in this area. While LLM-based
agentic tools show great promise, they still fail on a substantial portion of
tasks. Moreover, current evaluations primarily report aggregate issue-solving
rates, which obscure the underlying causes of success and failure, making it
challenging to diagnose model weaknesses or guide targeted improvements. To
bridge this gap, we first analyze the performance and efficiency of three SOTA
tools, spanning both pipeline-based and agentic architectures, in automated
issue solving tasks of SWE-Bench-Verified under varying task characteristics.
Furthermore, to move from high-level performance metrics to underlying cause
analysis, we conducted a systematic manual analysis of 150 failed instances.
From this analysis, we developed a comprehensive taxonomy of failure modes
comprising 3 primary phases, 9 main categories, and 25 fine-grained
subcategories. Then we systematically analyze the distribution of the
identified failure modes, the results reveal distinct failure fingerprints
between the two architectural paradigms, with the majority of agentic failures
stemming from flawed reasoning and cognitive deadlocks. Motivated by these
insights, we propose a collaborative Expert-Executor framework. It introduces a
supervisory Expert agent tasked with providing strategic oversight and
course-correction for a primary Executor agent. This architecture is designed
to correct flawed reasoning and break the cognitive deadlocks that frequently
lead to failure. Experiments show that our framework solves 22.2% of previously
intractable issues for a leading single agent. These findings pave the way for
building more robust agents through diagnostic evaluation and collaborative
design.

## 🔍 Abstract (한글 번역)

자동화된 문제 해결은 전체 코드베이스에서 결함이 있는 코드 스니펫을 자율적으로 식별하고 수정하는 것을 목표로 합니다. SWE-Bench는 이 분야에서의 발전을 평가하기 위한 가장 널리 채택된 벤치마크로 부상했습니다. 대규모 언어 모델(LLM) 기반의 에이전트 도구들은 큰 잠재력을 보여주지만, 여전히 상당한 부분의 작업에서 실패하고 있습니다. 게다가, 현재의 평가는 주로 총체적인 문제 해결 비율을 보고하여 성공과 실패의 근본적인 원인을 모호하게 하여 모델의 약점을 진단하거나 목표 지향적인 개선을 유도하는 데 어려움을 줍니다. 이러한 격차를 해소하기 위해, 우리는 SWE-Bench-Verified의 자동화된 문제 해결 작업에서 파이프라인 기반 및 에이전트 아키텍처를 아우르는 세 가지 최신 도구의 성능과 효율성을 다양한 작업 특성 하에서 분석했습니다. 또한, 고수준의 성능 지표에서 근본 원인 분석으로 이동하기 위해, 우리는 150개의 실패 사례에 대한 체계적인 수동 분석을 수행했습니다. 이 분석을 통해 3개의 주요 단계, 9개의 주요 범주, 25개의 세부 하위 범주로 구성된 포괄적인 실패 모드 분류 체계를 개발했습니다. 그런 다음, 식별된 실패 모드의 분포를 체계적으로 분석한 결과, 두 아키텍처 패러다임 간의 뚜렷한 실패 지문이 드러났으며, 에이전트 실패의 대부분은 잘못된 추론과 인지적 교착 상태에서 비롯된다는 것을 밝혀냈습니다. 이러한 통찰에 힘입어, 우리는 협력적인 전문가-실행자(Expert-Executor) 프레임워크를 제안합니다. 이는 주된 실행자 에이전트에 대한 전략적 감독 및 경로 수정 역할을 맡은 감독 전문가 에이전트를 도입합니다. 이 아키텍처는 잘못된 추론을 수정하고 자주 실패로 이어지는 인지적 교착 상태를 해소하도록 설계되었습니다. 실험 결과, 우리의 프레임워크는 선도적인 단일 에이전트의 이전에 해결 불가능했던 문제의 22.2%를 해결하는 것으로 나타났습니다. 이러한 발견은 진단 평가와 협력적 설계를 통해 더 견고한 에이전트를 구축하는 길을 열어줍니다.

## 📝 요약

자동화된 문제 해결은 코드베이스 전반에서 결함이 있는 코드 스니펫을 자동으로 식별하고 수정하는 것을 목표로 합니다. SWE-Bench는 이 분야의 발전을 평가하는 가장 널리 사용되는 벤치마크입니다. LLM 기반 도구는 유망하지만 여전히 많은 작업에서 실패하고 있습니다. 현재 평가 방식은 성공과 실패의 근본 원인을 파악하기 어려운 총체적 문제 해결률만 보고합니다. 이를 해결하기 위해, 우리는 SWE-Bench-Verified에서 세 가지 최첨단 도구의 성능과 효율성을 다양한 작업 특성 하에서 분석했습니다. 또한, 150건의 실패 사례를 체계적으로 분석하여 3단계, 9개 주요 범주, 25개 세부 하위 범주로 구성된 포괄적인 실패 모드 분류 체계를 개발했습니다. 분석 결과, 두 가지 아키텍처 패러다임 간의 실패 패턴이 다르며, 주로 에이전트 기반 도구의 실패는 잘못된 추론과 인지적 교착 상태에서 비롯됨을 발견했습니다. 이러한 통찰을 바탕으로, 우리는 주된 실행 에이전트에 전략적 감독과 교정 기능을 제공하는 전문가-실행자 협력 프레임워크를 제안했습니다. 이 프레임워크는 잘못된 추론을 수정하고 인지적 교착 상태를 해결하여 문제 해결률을 22.2% 향상시켰습니다. 이러한 결과는 진단 평가와 협력적 설계를 통해 더 견고한 에이전트를 구축하는 길을 열어줍니다.

## 🎯 주요 포인트

- 1. SWE-Bench는 자동화된 문제 해결 분야에서 가장 널리 채택된 벤치마크입니다.

- 2. LLM 기반 도구들은 유망하지만 여전히 많은 작업에서 실패하고 있습니다.

- 3. 실패 사례를 분석하여 3단계, 9개 주요 범주, 25개 세부 하위 범주로 구성된 포괄적인 실패 모드를 개발했습니다.

- 4. 에이전틱 실패의 주요 원인은 잘못된 추론과 인지적 교착 상태입니다.

- 5. 제안된 Expert-Executor 프레임워크는 전략적 감독과 교정 기능을 통해 문제 해결 능력을 향상시킵니다.

---

*Generated on 2025-09-20 09:22:22*