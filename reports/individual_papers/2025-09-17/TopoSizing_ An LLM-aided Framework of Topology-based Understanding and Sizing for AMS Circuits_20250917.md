---
keywords:
  - Large Language Models
  - Graph Neural Networks
  - Hypothesis-verification-refinement loop
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:44:02.330599",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Graph Neural Networks",
    "Hypothesis-verification-refinement loop"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "Large Language Models": 0.85,
    "Graph Neural Networks": 0.82,
    "Hypothesis-verification-refinement loop": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# TopoSizing: An LLM-aided Framework of Topology-based Understanding and Sizing for AMS Circuits

**Korean Title:** 토포사이징: AMS 회로의 위상 기반 이해 및 크기 조정을 위한 LLM 지원 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Graph Neural Networks|Graph algorithms]]
**⚡ Unique Technical**: [[keywords/Hypothesis-verification-refinement loop|Hypothesis-verification-refinement loop]]

## 🔗 유사한 논문
- [[Evolution of Kernels_ Automated RISC-V Kernel Optimization with Large Language Models_20250919|Evolution of Kernels Automated RISC-V Kernel Optimization with Large Language Models]] (80.0% similar)
- [[Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (79.4% similar)
- [[Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (78.7% similar)
- [[The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (78.2% similar)
- [[CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (78.0% similar)

## 📋 저자 정보

**Authors:** Ziming Wei, Zichen Kong, Yuan Wang, David Z. Pan, Xiyuan Tang

## 📄 Abstract (원문)

Analog and mixed-signal circuit design remains challenging due to the
shortage of high-quality data and the difficulty of embedding domain knowledge
into automated flows. Traditional black-box optimization achieves sampling
efficiency but lacks circuit understanding, which often causes evaluations to
be wasted in low-value regions of the design space. In contrast, learning-based
methods embed structural knowledge but are case-specific and costly to retrain.
Recent attempts with large language models show potential, yet they often rely
on manual intervention, limiting generality and transparency. We propose
TopoSizing, an end-to-end framework that performs robust circuit understanding
directly from raw netlists and translates this knowledge into optimization
gains. Our approach first applies graph algorithms to organize circuits into a
hierarchical device-module-stage representation. LLM agents then execute an
iterative hypothesis-verification-refinement loop with built-in consistency
checks, producing explicit annotations. Verified insights are integrated into
Bayesian optimization through LLM-guided initial sampling and
stagnation-triggered trust-region updates, improving efficiency while
preserving feasibility.

## 🔍 Abstract (한글 번역)

아날로그 및 혼합 신호 회로 설계는 고품질 데이터의 부족과 자동화 흐름에 도메인 지식을 내재화하는 어려움 때문에 여전히 도전적입니다. 전통적인 블랙박스 최적화는 샘플링 효율성을 달성하지만 회로 이해가 부족하여 종종 설계 공간의 저가치 영역에서 평가가 낭비됩니다. 반면에 학습 기반 방법은 구조적 지식을 내재화하지만 사례별로 특화되어 있으며 재학습 비용이 많이 듭니다. 대형 언어 모델을 활용한 최근 시도들은 잠재력을 보여주지만, 종종 수동 개입에 의존하여 일반성과 투명성을 제한합니다. 우리는 원시 넷리스트로부터 직접 강력한 회로 이해를 수행하고 이 지식을 최적화 이득으로 번역하는 종단 간 프레임워크인 TopoSizing을 제안합니다. 우리의 접근 방식은 먼저 그래프 알고리즘을 적용하여 회로를 계층적 장치-모듈-단계 표현으로 조직합니다. LLM 에이전트는 내장된 일관성 검사를 통해 가설-검증-개선 루프를 반복적으로 실행하여 명시적인 주석을 생성합니다. 검증된 통찰력은 LLM이 안내하는 초기 샘플링과 정체 상태에서의 신뢰 영역 업데이트를 통해 베이지안 최적화에 통합되어 효율성을 개선하면서도 실현 가능성을 유지합니다.

## 📝 요약

이 논문은 아날로그 및 혼합 신호 회로 설계의 어려움을 해결하기 위해 TopoSizing이라는 새로운 프레임워크를 제안합니다. 기존의 블랙박스 최적화는 샘플링 효율성은 높지만 회로 이해가 부족하고, 학습 기반 방법은 특정 사례에만 적용 가능하며 비용이 많이 듭니다. TopoSizing은 원시 넷리스트로부터 회로를 이해하고 이를 최적화로 전환합니다. 그래프 알고리즘을 통해 회로를 계층적으로 구성하고, 대형 언어 모델(LLM) 에이전트가 가설 검증 및 개선 과정을 통해 명시적 주석을 생성합니다. 이 통찰은 LLM이 안내하는 초기 샘플링과 신뢰 영역 업데이트를 통해 베이지안 최적화에 통합되어 효율성을 높입니다.

## 🎯 주요 포인트

- 1. 아날로그 및 혼합 신호 회로 설계는 고품질 데이터 부족과 자동화 흐름에 도메인 지식을 내재화하는 어려움 때문에 여전히 도전적입니다.

- 2. 전통적인 블랙박스 최적화는 샘플링 효율성을 달성하지만 회로 이해가 부족하여 설계 공간의 저가치 영역에서 평가가 낭비되는 경우가 많습니다.

- 3. TopoSizing은 원시 넷리스트에서 직접 회로 이해를 수행하고 이를 최적화 이득으로 변환하는 종단 간 프레임워크를 제안합니다.

- 4. 제안된 접근법은 그래프 알고리즘을 사용하여 회로를 계층적 장치-모듈-단계 표현으로 조직화하고, LLM 에이전트가 일관성 검사를 내장한 가설-검증-개선 루프를 실행하여 명시적 주석을 생성합니다.

- 5. 검증된 통찰력은 LLM이 안내하는 초기 샘플링과 정체 유발 신뢰 영역 업데이트를 통해 베이지안 최적화에 통합되어 효율성을 개선하면서도 실행 가능성을 유지합니다.

---

*Generated on 2025-09-20 07:44:54*