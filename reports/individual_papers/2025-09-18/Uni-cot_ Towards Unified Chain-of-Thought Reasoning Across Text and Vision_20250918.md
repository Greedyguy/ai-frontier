
# Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision

**Korean Title:** 유니-코트: 텍스트와 비전을 통한 통합된 사고 연쇄 추론을 향하여

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language Reasoning

## 🔗 유사한 논문
- [[Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (85.9% similar)
- [[Early_Stopping_Chain-of-thoughts_in_Large_Language_Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (84.8% similar)
- [[THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (80.9% similar)
- [[MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (80.5% similar)
- [[Humanoid_Agent_via_Embodied_Chain-of-Action_Reasoning_with_Multimodal_Foundation_Models_for_Zero-Shot_Loco-Manipulation_20250918|Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.05606v2 Announce Type: replace-cross 
Abstract: Chain-of-Thought (CoT) reasoning has been widely adopted to enhance Large Language Models (LLMs) by decomposing complex tasks into simpler, sequential subtasks. However, extending CoT to vision-language reasoning tasks remains challenging, as it often requires interpreting transitions of visual states to support reasoning. Existing methods often struggle with this due to limited capacity of modeling visual state transitions or incoherent visual trajectories caused by fragmented architectures.
  To overcome these limitations, we propose Uni-CoT, a Unified Chain-of-Thought framework that enables coherent and grounded multimodal reasoning within a single unified model. The key idea is to leverage a model capable of both image understanding and generation to reason over visual content and model evolving visual states. However, empowering a unified model to achieve that is non-trivial, given the high computational cost and the burden of training. To address this, Uni-CoT introduces a novel two-level reasoning paradigm: A Macro-Level CoT for high-level task planning and A Micro-Level CoT for subtask execution. This design significantly reduces the computational overhead. Furthermore, we introduce a structured training paradigm that combines interleaved image-text supervision for macro-level CoT with multi-task objectives for micro-level CoT. Together, these innovations allow Uni-CoT to perform scalable and coherent multi-modal reasoning. Furthermore, thanks to our design, all experiments can be efficiently completed using only 8 A100 GPUs with 80GB VRAM each. Experimental results on reasoning-driven image generation benchmark (WISE) and editing benchmarks (RISE and KRIS) indicates that Uni-CoT demonstrates SOTA performance and strong generalization, establishing Uni-CoT as a promising solution for multi-modal reasoning. Project Page and Code: https://sais-fuxi.github.io/projects/uni-cot/

## 🔍 Abstract (한글 번역)

arXiv:2508.05606v2 발표 유형: 대체-교차
요약: Chain-of-Thought (CoT) 추론은 복잡한 작업을 더 간단하고 순차적인 하위 작업으로 분해하여 대형 언어 모델 (LLMs)을 강화하는 데 널리 채택되었습니다. 그러나 CoT를 시각-언어 추론 작업으로 확장하는 것은 종종 추론을 지원하기 위해 시각적 상태의 전이를 해석하는 것을 필요로 하기 때문에 도전적입니다. 기존 방법들은 종종 시각적 상태 전이를 모델링하는 능력의 한계나 단편화된 아키텍처로 인한 일관성 없는 시각적 궤적으로 인해 이에 어려움을 겪습니다.
이러한 제한을 극복하기 위해 우리는 단일 통합 모델 내에서 일관되고 기반을 둔 다중 모달 추론을 가능하게 하는 통합 Chain-of-Thought 프레임워크인 Uni-CoT를 제안합니다. 핵심 아이디어는 이미지 이해와 생성 능력을 모두 갖춘 모델을 활용하여 시각적 콘텐츠를 추론하고 진화하는 시각적 상태를 모델링하는 것입니다. 그러나 통합 모델이 그것을 달성하는 것은 높은 계산 비용과 훈련 부담으로 인해 비닝입니다. 이를 해결하기 위해 Uni-CoT는 고수준 작업 계획을 위한 Macro-Level CoT와 하위 작업 실행을 위한 Micro-Level CoT의 혁신적인 두 수준 추론 패러다임을 소개합니다. 이 설계는 계산 오버헤드를 크게 줄입니다. 더 나아가, 우리는 Macro-Level CoT를 위한 교차 이미지-텍스트 감독 및 Micro-Level CoT를 위한 다중 작업 목표를 결합하는 구조화된 훈련 패러다임을 소개합니다. 이러한 혁신들은 Uni-CoT가 확장 가능하고 일관된 다중 모달 추론을 수행할 수 있도록 합니다. 또한, 우리의 설계 덕분에 모든 실험은 각각 80GB VRAM을 갖춘 8대의 A100 GPU만을 사용하여 효율적으로 완료될 수 있습니다. 추론 주도 이미지 생성 벤치마크 (WISE) 및 편집 벤치마크 (RISE 및 KRIS)에서의 실험 결과는 Uni-CoT가 SOTA 성능과 강력한 일반화를 보여주며, 다중 모달 추론을 위한 유망한 솔루션으로 Uni-CoT를 확립합니다. 프로젝트 페이지 및 코드: https://sais-fuxi.github.io/projects/uni-cot/

## 📝 요약

이 논문은 시각-언어 추론 작업에 대한 Chain-of-Thought (CoT) 추론을 개선하기 위한 Uni-CoT 프레임워크를 제안한다. Uni-CoT는 이미지 이해와 생성을 모두 수행할 수 있는 모델을 활용하여 시각적 콘텐츠를 추론하고 변화하는 시각적 상태를 모델링하는 것을 목표로 한다. 이를 위해 매크로-레벨 CoT와 마이크로-레벨 CoT를 결합한 두 수준의 추론 패러다임을 도입하여 연산 부담을 줄였다. 실험 결과는 Uni-CoT가 SOTA 성능과 강력한 일반화 능력을 보여주며, 다중 모달 추론에 대한 유망한 해결책으로 자리매김하고 있다.

## 🎯 주요 포인트

- 1. Chain-of-Thought (CoT) reasoning을 확장하여 시각-언어 추론 작업에 대한 도전을 극복하기 위해 Uni-CoT를 제안함.

- 2. Uni-CoT는 이미지 이해 및 생성 기능을 결합하여 시각적 콘텐츠를 추론하고 진화하는 시각적 상태를 모델링하는 통합된 모델을 구현함.

- 3. 높은 계산 비용과 훈련 부담으로 인해 Uni-CoT는 새로운 두 수준의 추론 패러다임을 도입하여 계산 오버헤드를 크게 줄임.

- 4. Uni-CoT는 WISE 및 RISE, KRIS 벤치마크에서 SOTA 성능과 강력한 일반화 능력을 보여주며, 다중 모달 추론에 대한 유망한 솔루션으로 자리매김함.

---

*Generated on 2025-09-18 16:57:56*