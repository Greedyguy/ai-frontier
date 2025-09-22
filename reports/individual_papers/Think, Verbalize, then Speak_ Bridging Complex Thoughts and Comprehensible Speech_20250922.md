# Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech

**Korean Title:** 생각하고, 말로 표현한 후, 말하기: 복잡한 사고와 이해 가능한 언어 사이의 다리 놓기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Latency-efficient Verbalizer

## 🔗 유사한 논문
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (85.1% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (85.1% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.9% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (83.9% similar)
- [[2025-09-19/Cross-Modal Knowledge Distillation for Speech Large Language Models_20250919|Cross-Modal Knowledge Distillation for Speech Large Language Models]] (83.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16028v1 Announce Type: cross 
Abstract: Spoken dialogue systems increasingly employ large language models (LLMs) to leverage their advanced reasoning capabilities. However, direct application of LLMs in spoken communication often yield suboptimal results due to mismatches between optimal textual and verbal delivery. While existing approaches adapt LLMs to produce speech-friendly outputs, their impact on reasoning performance remains underexplored. In this work, we propose Think-Verbalize-Speak, a framework that decouples reasoning from spoken delivery to preserve the full reasoning capacity of LLMs. Central to our method is verbalizing, an intermediate step that translates thoughts into natural, speech-ready text. We also introduce ReVerT, a latency-efficient verbalizer based on incremental and asynchronous summarization. Experiments across multiple benchmarks show that our method enhances speech naturalness and conciseness with minimal impact on reasoning. The project page with the dataset and the source code is available at https://yhytoto12.github.io/TVS-ReVerT

## 🔍 Abstract (한글 번역)

arXiv:2509.16028v1 발표 유형: 교차  
초록: 음성 대화 시스템은 점점 더 고급 추론 능력을 활용하기 위해 대형 언어 모델(LLMs)을 사용하고 있습니다. 그러나 LLMs를 음성 통신에 직접 적용할 경우, 최적의 텍스트 전달과 음성 전달 간의 불일치로 인해 종종 최적의 결과를 얻지 못합니다. 기존 접근 방식은 LLMs를 조정하여 음성 친화적인 출력을 생성하도록 하지만, 이러한 조정이 추론 성능에 미치는 영향은 충분히 탐구되지 않았습니다. 본 연구에서는 LLMs의 완전한 추론 능력을 유지하기 위해 추론을 음성 전달과 분리하는 Think-Verbalize-Speak 프레임워크를 제안합니다. 이 방법의 핵심은 생각을 자연스럽고 음성 준비가 된 텍스트로 변환하는 중간 단계인 발화(verbalizing)입니다. 또한, 점진적이고 비동기적인 요약을 기반으로 한 지연 효율적인 발화기인 ReVerT를 소개합니다. 여러 벤치마크에서의 실험 결과, 우리의 방법이 추론에 미치는 영향을 최소화하면서도 음성의 자연스러움과 간결성을 향상시킨다는 것을 보여줍니다. 데이터셋과 소스 코드를 포함한 프로젝트 페이지는 https://yhytoto12.github.io/TVS-ReVerT에서 확인할 수 있습니다.

## 📝 요약

이 연구는 대화 시스템에서 대형 언어 모델(LLM)의 추론 능력을 유지하면서 음성 전달을 최적화하는 새로운 프레임워크인 Think-Verbalize-Speak를 제안합니다. 기존 방법들이 LLM의 음성 친화적 출력을 생성하는 데 집중한 반면, 이 연구는 추론 성능에 미치는 영향을 분석하지 않았습니다. 제안된 방법은 추론과 음성 전달을 분리하여 LLM의 추론 능력을 온전히 보존합니다. 핵심은 생각을 자연스럽고 음성에 적합한 텍스트로 변환하는 중간 단계인 'verbalizing'입니다. 또한, 지연을 최소화하는 비동기 요약 기반의 ReVerT를 도입하여 음성의 자연스러움과 간결성을 향상시킵니다. 여러 벤치마크 실험 결과, 제안된 방법이 추론에 거의 영향을 주지 않으면서도 음성의 자연스러움과 간결성을 개선함을 확인했습니다.

## 🎯 주요 포인트

- 1. 대화형 시스템에서 대형 언어 모델(LLM)의 추론 능력을 활용하기 위해 Think-Verbalize-Speak 프레임워크를 제안합니다.

- 2. 제안된 프레임워크는 추론과 발화를 분리하여 LLM의 추론 능력을 최대한 보존합니다.

- 3. ReVerT는 비동기 요약을 기반으로 한 지연 효율적인 발화 도구로, 자연스러운 발화와 간결성을 향상시킵니다.

- 4. 여러 벤치마크 실험에서 제안된 방법이 추론 성능에 거의 영향을 주지 않으면서 발화의 자연스러움과 간결성을 개선함을 보여줍니다.

- 5. 프로젝트 페이지에서 데이터셋과 소스 코드를 제공합니다: https://yhytoto12.github.io/TVS-ReVerT

---

*Generated on 2025-09-22 14:23:03*