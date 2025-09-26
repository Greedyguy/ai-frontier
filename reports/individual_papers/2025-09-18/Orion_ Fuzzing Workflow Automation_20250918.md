---
keywords:
  - Large Language Models
  - Orion Framework
  - Fuzz Testing
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:17:02.951410",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Orion Framework",
    "Fuzz Testing"
  ],
  "rejected_keywords": [
    "Software Vulnerabilities"
  ],
  "similarity_scores": {
    "Large Language Models": 0.9,
    "Orion Framework": 0.85,
    "Fuzz Testing": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Orion: Fuzzing Workflow Automation

**Korean Title:** 오리온: 퍼징 워크플로 자동화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Orion Framework|Orion]], [[keywords/Fuzz Testing|fuzz testing]]

## 📋 저자 정보

**Authors:** Max Bazalii, Marius Fleischer

## 📄 Abstract (원문)

Fuzz testing is one of the most effective techniques for finding software
vulnerabilities. While modern fuzzers can generate inputs and monitor
executions automatically, the overall workflow, from analyzing a codebase, to
configuring harnesses, to triaging results, still requires substantial manual
effort. Prior attempts focused on single stages such as harness synthesis or
input minimization, leaving researchers to manually connect the pieces into a
complete fuzzing campaign.
  We introduce Orion, a framework that automates the the manual bottlenecks of
fuzzing by integrating LLM reasoning with traditional tools, allowing campaigns
to scale to settings where human effort alone was impractical. Orion uses LLMs
for code reasoning and semantic guidance, while relying on deterministic tools
for verification, iterative refinement, and tasks that require precision.
Across our benchmark suite, Orion reduces human effort by 46-204x depending on
the workflow stage, and we demonstrate its effectiveness through the discovery
of two previously unknown vulnerabilities in the widely used open-source clib
library.

## 🔍 Abstract (한글 번역)

퍼즈 테스트는 소프트웨어 취약점을 발견하는 데 가장 효과적인 기법 중 하나입니다. 현대의 퍼저는 입력을 생성하고 실행을 자동으로 모니터링할 수 있지만, 코드베이스 분석에서 하네스 구성, 결과 분류에 이르는 전체 워크플로우는 여전히 상당한 수작업을 필요로 합니다. 이전 시도들은 하네스 합성이나 입력 최소화와 같은 단일 단계에 초점을 맞췄으며, 연구자들은 이를 완전한 퍼징 캠페인으로 수동으로 연결해야 했습니다.

우리는 퍼징의 수작업 병목 현상을 자동화하는 프레임워크인 Orion을 소개합니다. Orion은 LLM 추론을 전통적인 도구와 통합하여, 인간의 노력만으로는 실현 불가능했던 환경에서도 캠페인을 확장할 수 있도록 합니다. Orion은 코드 추론과 의미적 안내를 위해 LLM을 사용하며, 검증, 반복적 개선, 정밀도가 필요한 작업에는 결정론적 도구에 의존합니다. 우리의 벤치마크 스위트에서 Orion은 워크플로우 단계에 따라 인간의 노력을 46배에서 204배까지 줄이며, 널리 사용되는 오픈 소스 clib 라이브러리에서 이전에 알려지지 않은 두 가지 취약점을 발견함으로써 그 효과를 입증합니다.

## 📝 요약

이 논문은 소프트웨어 취약점을 찾는 효과적인 기법인 퍼즈 테스트의 자동화를 목표로 하는 Orion 프레임워크를 소개합니다. 기존 퍼즈 테스트는 코드 분석, 하니스 구성, 결과 분류 등에서 많은 수작업이 필요했으나, Orion은 LLM(대형 언어 모델)과 전통적 도구를 결합하여 이러한 수작업을 자동화합니다. LLM은 코드 추론과 의미적 지침을 제공하고, 결정론적 도구는 검증과 정밀한 작업을 수행합니다. 이를 통해 퍼즈 테스트 캠페인의 확장성을 높이며, 인간의 노력을 46-204배 줄였습니다. 또한, Orion은 널리 사용되는 오픈 소스 clib 라이브러리에서 두 개의 새로운 취약점을 발견하는 데 성공했습니다.

## 🎯 주요 포인트

- 1. Fuzz 테스트는 소프트웨어 취약점을 찾는 데 가장 효과적인 기법 중 하나입니다.

- 2. Orion은 LLM 추론과 전통적인 도구를 통합하여 퍼징의 수작업 병목을 자동화하는 프레임워크입니다.

- 3. Orion은 코드 추론과 의미적 안내를 위해 LLM을 사용하고, 검증과 정밀성이 필요한 작업에는 결정론적 도구를 활용합니다.

- 4. Orion은 워크플로우 단계에 따라 인간의 노력을 46-204배 줄여줍니다.

- 5. Orion은 널리 사용되는 오픈 소스 clib 라이브러리에서 두 개의 새로운 취약점을 발견하여 그 효과를 입증했습니다.

---

*Generated on 2025-09-19 17:05:14*