# Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework

**Korean Title:** 적응형 사고 과정 압축을 통한 효율적인 추론: 자기 최적화 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Kerui Huang|Kerui Huang]] [[authors/Shuhan Liu|Shuhan Liu]] [[authors/Xing Hu|Xing Hu]] [[authors/Tongtong Xu|Tongtong Xu]] [[authors/Lingfeng Bao|Lingfeng Bao]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Chain-of-Thought Compression

## 🔗 유사한 논문
- [[Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (89.4% similar)
- [[ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (86.0% similar)
- [[Uni-cot_ Towards Unified Chain-of-Thought Reasoning Across Text and Vision_20250918|Uni-cot Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (84.2% similar)
- [[Do Code Semantics Help A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models_20250919|Do Code Semantics Help A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (81.7% similar)
- [[WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (81.5% similar)

## 📋 저자 정보

**Authors:** Kerui Huang, Shuhan Liu, Xing Hu, Tongtong Xu, Lingfeng Bao, Xin Xia

## 📄 Abstract (원문)

Chain-of-Thought (CoT) reasoning enhances Large Language Models (LLMs) by
prompting intermediate steps, improving accuracy and robustness in arithmetic,
logic, and commonsense tasks. However, this benefit comes with high
computational costs: longer outputs increase latency, memory usage, and
KV-cache demands. These issues are especially critical in software engineering
tasks where concise and deterministic outputs are required. To investigate
these trade-offs, we conduct an empirical study based on code generation
benchmarks. The results reveal that longer CoT does not always help. Excessive
reasoning often causes truncation, accuracy drops, and latency up to five times
higher, with failed outputs consistently longer than successful ones. These
findings challenge the assumption that longer reasoning is inherently better
and highlight the need for adaptive CoT control. Motivated by this, we propose
SEER (Self-Enhancing Efficient Reasoning), an adaptive framework that
compresses CoT while preserving accuracy. SEER combines Best-of-N sampling with
task-aware adaptive filtering, dynamically adjusting thresholds based on
pre-inference outputs to reduce verbosity and computational overhead. We then
evaluate SEER on three software engineering tasks and one math task. On
average, SEER shortens CoT by 42.1%, improves accuracy by reducing truncation,
and eliminates most infinite loops. These results demonstrate SEER as a
practical method to make CoT-enhanced LLMs more efficient and robust, even
under resource constraints.

## 🔍 Abstract (한글 번역)

연쇄 사고(Chain-of-Thought, CoT) 추론은 중간 단계를 유도하여 대형 언어 모델(LLM)의 산술, 논리, 상식 작업에서 정확성과 견고성을 향상시킵니다. 그러나 이러한 이점은 높은 계산 비용을 수반합니다. 출력이 길어지면 지연 시간, 메모리 사용량, KV-캐시 요구량이 증가합니다. 이러한 문제는 간결하고 결정론적인 출력이 필요한 소프트웨어 엔지니어링 작업에서 특히 중요합니다. 이러한 상충 관계를 조사하기 위해 코드 생성 벤치마크를 기반으로 실증 연구를 수행했습니다. 결과는 더 긴 CoT가 항상 도움이 되지 않는다는 것을 보여줍니다. 과도한 추론은 종종 잘림, 정확도 저하, 최대 5배 높은 지연 시간을 초래하며, 실패한 출력은 성공한 출력보다 일관되게 더 깁니다. 이러한 발견은 더 긴 추론이 본질적으로 더 낫다는 가정을 도전하며 적응형 CoT 제어의 필요성을 강조합니다. 이에 영감을 받아, 우리는 정확성을 유지하면서 CoT를 압축하는 적응형 프레임워크인 SEER(Self-Enhancing Efficient Reasoning)를 제안합니다. SEER는 Best-of-N 샘플링과 작업 인식 적응형 필터링을 결합하여 사전 추론 출력에 기반한 임계값을 동적으로 조정하여 장황함과 계산 오버헤드를 줄입니다. 그런 다음 SEER를 세 가지 소프트웨어 엔지니어링 작업과 하나의 수학 작업에 대해 평가합니다. 평균적으로 SEER는 CoT를 42.1% 단축하고, 잘림을 줄여 정확성을 개선하며, 대부분의 무한 루프를 제거합니다. 이러한 결과는 SEER가 자원 제약 하에서도 CoT로 강화된 LLM을 보다 효율적이고 견고하게 만드는 실용적인 방법임을 보여줍니다.

## 📝 요약

Chain-of-Thought (CoT) 추론은 대형 언어 모델(LLMs)의 중간 단계 유도를 통해 산술, 논리, 상식 작업의 정확성과 견고성을 향상시킵니다. 그러나 이는 출력 길이 증가로 인한 높은 계산 비용을 수반합니다. 본 연구는 코드 생성 벤치마크를 통해 이러한 비용과 이점의 균형을 조사하였으며, 긴 CoT가 항상 유리하지 않음을 발견했습니다. 과도한 추론은 출력이 잘리거나 정확도가 떨어지며, 지연 시간이 최대 5배 증가하는 문제를 초래합니다. 이러한 문제를 해결하기 위해 SEER(Self-Enhancing Efficient Reasoning)라는 적응형 프레임워크를 제안하였으며, 이는 CoT를 압축하면서도 정확성을 유지합니다. SEER는 Best-of-N 샘플링과 작업 인식 적응형 필터링을 결합하여 불필요한 장황함과 계산 부담을 줄입니다. 세 가지 소프트웨어 엔지니어링 작업과 하나의 수학 작업에 대한 평가 결과, SEER는 CoT 길이를 평균 42.1% 단축하고 정확성을 향상시켜 무한 루프를 대부분 제거했습니다. 이를 통해 SEER는 자원 제약 하에서도 CoT 강화 LLM을 더 효율적이고 견고하게 만드는 실용적인 방법임을 입증했습니다.

## 🎯 주요 포인트

- 1. Chain-of-Thought (CoT) 추론은 대형 언어 모델(LLM)의 정확성과 견고성을 향상시키지만, 높은 계산 비용을 초래합니다.

- 2. CoT의 장황한 출력은 지연, 메모리 사용량 증가, KV-캐시 요구 증가를 야기하며, 특히 소프트웨어 엔지니어링 작업에서 문제가 됩니다.

- 3. 연구 결과, CoT의 길이가 항상 도움이 되는 것은 아니며, 과도한 추론은 정확도 저하와 지연을 초래할 수 있습니다.

- 4. SEER(Self-Enhancing Efficient Reasoning)는 CoT를 압축하여 정확성을 유지하면서 계산 비용을 줄이는 적응형 프레임워크입니다.

- 5. SEER는 CoT 길이를 평균 42.1% 단축하고, 정확성을 개선하며, 대부분의 무한 루프를 제거하여 CoT-강화 LLM의 효율성과 견고성을 향상시킵니다.

---

*Generated on 2025-09-20 07:48:04*