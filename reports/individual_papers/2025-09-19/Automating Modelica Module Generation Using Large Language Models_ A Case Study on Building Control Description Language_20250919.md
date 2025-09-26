---
keywords:
  - Large Language Models
  - Modelica
  - OpenModelica
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14623
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:55:29.035874",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Modelica",
    "OpenModelica"
  ],
  "rejected_keywords": [
    "Control Description Language",
    "Building Modelica Library"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Modelica": 0.75,
    "OpenModelica": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Automating Modelica Module Generation Using Large Language Models: A Case Study on Building Control Description Language

**Korean Title:** Modelica 모듈 생성을 자동화하기 위한 대형 언어 모델 활용: 건물 제어 설명 언어에 대한 사례 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Modelica|Modelica]], [[keywords/OpenModelica|OpenModelica]]

## 🔗 유사한 논문
- [[Evaluating_Classical_Software_Process_Models_as_Coordination_Mechanisms_for_LLM-Based_Software_Generation_20250918|Evaluating Classical Software Process Models as Coordination Mechanisms for LLM-Based Software Generation]] (82.9% similar)
- [[An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (82.6% similar)
- [[From Automation to Autonomy A Survey on Large Language Models in Scientific Discovery]] (82.1% similar)
- [[Pareto-Grid-Guided Large Language Models for Fast and High-Quality Heuristics Design in Multi-Objective Combinatorial Optimization]] (81.6% similar)
- [[Evolution of Kernels Automated RISC-V Kernel Optimization with Large Language Models]] (81.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14623v1 Announce Type: cross 
Abstract: Dynamic energy systems and controls require advanced modeling frameworks to design and test supervisory and fault tolerant strategies. Modelica is a widely used equation based language, but developing control modules is labor intensive and requires specialized expertise. This paper examines the use of large language models (LLMs) to automate the generation of Control Description Language modules in the Building Modelica Library as a case study. We developed a structured workflow that combines standardized prompt scaffolds, library aware grounding, automated compilation with OpenModelica, and human in the loop evaluation. Experiments were carried out on four basic logic tasks (And, Or, Not, and Switch) and five control modules (chiller enable/disable, bypass valve control, cooling tower fan speed, plant requests, and relief damper control). The results showed that GPT 4o failed to produce executable Modelica code in zero shot mode, while Claude Sonnet 4 achieved up to full success for basic logic blocks with carefully engineered prompts. For control modules, success rates reached 83 percent, and failed outputs required medium level human repair (estimated one to eight hours). Retrieval augmented generation often produced mismatches in module selection (for example, And retrieved as Or), while a deterministic hard rule search strategy avoided these errors. Human evaluation also outperformed AI evaluation, since current LLMs cannot assess simulation results or validate behavioral correctness. Despite these limitations, the LLM assisted workflow reduced the average development time from 10 to 20 hours down to 4 to 6 hours per module, corresponding to 40 to 60 percent time savings. These results highlight both the potential and current limitations of LLM assisted Modelica generation, and point to future research in pre simulation validation, stronger grounding, and closed loop evaluation.

## 🔍 Abstract (한글 번역)

arXiv:2509.14623v1 발표 유형: 교차  
초록: 동적 에너지 시스템과 제어는 감독 및 고장 허용 전략을 설계하고 테스트하기 위해 고급 모델링 프레임워크를 필요로 합니다. Modelica는 널리 사용되는 방정식 기반 언어이지만, 제어 모듈을 개발하는 것은 노동 집약적이며 전문적인 전문 지식이 필요합니다. 본 논문은 대형 언어 모델(LLM)을 사용하여 빌딩 Modelica 라이브러리에서 제어 설명 언어 모듈 생성을 자동화하는 사례 연구를 다룹니다. 우리는 표준화된 프롬프트 스캐폴드, 라이브러리 인식 기반, OpenModelica를 통한 자동 컴파일, 인간의 개입 평가를 결합한 구조화된 워크플로를 개발했습니다. 네 가지 기본 논리 작업(And, Or, Not, Switch)과 다섯 가지 제어 모듈(냉각기 활성화/비활성화, 우회 밸브 제어, 냉각탑 팬 속도, 플랜트 요청, 배기 댐퍼 제어)에 대한 실험이 수행되었습니다. 결과는 GPT 4o가 제로 샷 모드에서 실행 가능한 Modelica 코드를 생성하지 못한 반면, Claude Sonnet 4는 신중하게 설계된 프롬프트로 기본 논리 블록에서 최대 완전 성공을 달성했음을 보여주었습니다. 제어 모듈의 경우 성공률은 83%에 도달했으며, 실패한 출력은 중간 수준의 인간 수정을 필요로 했습니다(추정 1~8시간). 검색 증강 생성은 종종 모듈 선택에서 불일치를 초래했으며(예: And가 Or로 검색됨), 결정론적 하드 룰 검색 전략은 이러한 오류를 피했습니다. 인간 평가도 AI 평가를 능가했는데, 이는 현재 LLM이 시뮬레이션 결과를 평가하거나 행동의 정확성을 검증할 수 없기 때문입니다. 이러한 한계에도 불구하고, LLM 지원 워크플로는 모듈당 평균 개발 시간을 10~20시간에서 4~6시간으로 줄여 40~60%의 시간 절감을 달성했습니다. 이러한 결과는 LLM 지원 Modelica 생성의 잠재력과 현재의 한계를 모두 강조하며, 사전 시뮬레이션 검증, 강력한 기반, 폐쇄 루프 평가에 대한 향후 연구를 지적합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용하여 Building Modelica Library의 제어 설명 언어 모듈 생성을 자동화하는 방법을 연구합니다. 표준화된 프롬프트 구조, 라이브러리 인식 기반, OpenModelica를 통한 자동 컴파일, 인간 평가를 결합한 워크플로우를 개발했습니다. 실험 결과, Claude Sonnet 4는 기본 논리 블록에서 높은 성공률을 보였고, 제어 모듈에서는 83%의 성공률을 기록했습니다. LLM을 활용한 워크플로우는 모듈 개발 시간을 40~60% 단축시켰습니다. 그러나 LLM의 한계로 인해 인간 평가가 더 우수했으며, 향후 연구에서는 시뮬레이션 전 검증 및 평가 방법 개선이 필요합니다.

## 🎯 주요 포인트

- 1. Modelica 언어 기반 제어 모듈 개발은 전문 지식이 필요하며, 이를 자동화하기 위해 대형 언어 모델(LLM)의 활용 가능성을 연구했습니다.

- 2. 연구에서는 표준화된 프롬프트 구조, 라이브러리 인식 기반, OpenModelica 자동 컴파일, 인간 평가를 결합한 워크플로우를 개발했습니다.

- 3. 실험 결과, GPT 4o는 기본 논리 블록에서 실행 가능한 Modelica 코드를 생성하지 못했으나, Claude Sonnet 4는 신중하게 설계된 프롬프트로 높은 성공률을 보였습니다.

- 4. LLM 지원 워크플로우는 모듈당 개발 시간을 평균 10~20시간에서 4~6시간으로 단축시켜 40~60%의 시간 절감을 달성했습니다.

- 5. 연구는 LLM 지원 Modelica 생성의 잠재력과 한계를 강조하며, 향후 시뮬레이션 전 검증, 강력한 기반 확립, 폐쇄 루프 평가에 대한 연구 필요성을 제시합니다.

---

*Generated on 2025-09-19 14:59:02*