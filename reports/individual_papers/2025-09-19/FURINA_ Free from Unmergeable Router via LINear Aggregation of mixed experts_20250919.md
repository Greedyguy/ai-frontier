
# FURINA: Free from Unmergeable Router via LINear Aggregation of mixed experts

**Korean Title:** FURINA: 혼합 전문가의 선형 집계를 통한 비병합 가능 라우터로부터의 자유

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Router Free MoE

## 🔗 유사한 논문
- [[Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (81.4% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (80.4% similar)
- [[Don't Forget the Nonlinearity Unlocking Activation Functions in Efficient Fine-Tuning]] (78.6% similar)
- [[FroM Frobenius Norm-Based Data-Free Adaptive Model Merging]] (76.9% similar)
- [[CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (76.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14900v1 Announce Type: new 
Abstract: The Mixture of Experts (MoE) paradigm has been successfully integrated into Low-Rank Adaptation (LoRA) for parameter-efficient fine-tuning (PEFT), delivering performance gains with minimal parameter overhead. However, a key limitation of existing MoE-LoRA methods is their reliance on a discrete router, which prevents the integration of the MoE components into the backbone model. To overcome this, we propose FURINA, a novel Free from Unmergeable Router framework based on the LINear Aggregation of experts. FURINA eliminates the router by introducing a Self-Routing mechanism. This is achieved through three core innovations: (1) decoupled learning of the direction and magnitude for LoRA adapters, (2) a shared learnable magnitude vector for consistent activation scaling, and (3) expert selection loss that encourages divergent expert activation. The proposed mechanism leverages the angular similarity between the input and each adapter's directional component to activate experts, which are then scaled by the shared magnitude vector. This design allows the output norm to naturally reflect the importance of each expert, thereby enabling dynamic, router-free routing. The expert selection loss further sharpens this behavior by encouraging sparsity and aligning it with standard MoE activation patterns. We also introduce a shared expert within the MoE-LoRA block that provides stable, foundational knowledge. To the best of our knowledge, FURINA is the first router-free, MoE-enhanced LoRA method that can be fully merged into the backbone model, introducing zero additional inference-time cost or complexity. Extensive experiments demonstrate that FURINA not only significantly outperforms standard LoRA but also matches or surpasses the performance of existing MoE-LoRA methods, while eliminating the extra inference-time overhead of MoE.

## 🔍 Abstract (한글 번역)

arXiv:2509.14900v1 발표 유형: 신규  
초록: 혼합 전문가(Mixture of Experts, MoE) 패러다임은 파라미터 효율적인 미세 조정(PEFT)을 위해 Low-Rank Adaptation (LoRA)에 성공적으로 통합되어, 최소한의 파라미터 오버헤드로 성능 향상을 제공하고 있습니다. 그러나 기존 MoE-LoRA 방법의 주요 한계는 이산 라우터에 의존하여 MoE 구성 요소를 백본 모델에 통합할 수 없다는 점입니다. 이를 극복하기 위해, 우리는 전문가의 선형 집계(LINear Aggregation)를 기반으로 한 새로운 비병합 라우터 프레임워크인 FURINA를 제안합니다. FURINA는 셀프 라우팅 메커니즘을 도입하여 라우터를 제거합니다. 이는 세 가지 핵심 혁신을 통해 달성됩니다: (1) LoRA 어댑터의 방향과 크기를 분리하여 학습, (2) 일관된 활성화 스케일링을 위한 공유 가능한 학습 크기 벡터, (3) 전문가 활성화를 다양하게 유도하는 전문가 선택 손실. 제안된 메커니즘은 입력과 각 어댑터의 방향성 구성 요소 간의 각도 유사성을 활용하여 전문가를 활성화하고, 이는 공유 크기 벡터에 의해 스케일링됩니다. 이 설계는 출력 노름이 각 전문가의 중요성을 자연스럽게 반영할 수 있도록 하여 동적이고 라우터 없는 라우팅을 가능하게 합니다. 전문가 선택 손실은 희소성을 장려하고 표준 MoE 활성화 패턴과의 정렬을 통해 이 행동을 더욱 날카롭게 합니다. 우리는 또한 안정적이고 기초적인 지식을 제공하는 MoE-LoRA 블록 내의 공유 전문가를 소개합니다. 우리가 아는 한, FURINA는 백본 모델에 완전히 통합될 수 있는 최초의 라우터 없는 MoE 강화 LoRA 방법으로, 추가적인 추론 시간 비용이나 복잡성을 도입하지 않습니다. 광범위한 실험을 통해 FURINA는 표준 LoRA를 크게 능가할 뿐만 아니라 기존 MoE-LoRA 방법의 성능을 맞추거나 능가하면서 MoE의 추가 추론 시간 오버헤드를 제거한다는 것을 입증합니다.

## 📝 요약

FURINA는 기존의 MoE-LoRA 방법의 제한 사항인 비연결 라우터 문제를 해결하기 위해 제안된 새로운 프레임워크입니다. FURINA는 라우터를 제거하고 Self-Routing 메커니즘을 도입하여, LoRA 어댑터의 방향성과 크기를 분리하여 학습하고, 일관된 활성화 스케일링을 위한 공유 가능한 크기 벡터를 사용합니다. 또한, 전문가 선택 손실을 통해 전문가 활성화를 다양화합니다. 이 메커니즘은 입력과 각 어댑터의 방향성 간의 각도 유사성을 활용하여 전문가를 활성화하고, 공유 크기 벡터로 스케일링합니다. 이를 통해 동적이고 라우터 없는 라우팅이 가능해지며, MoE-LoRA 블록 내에 공유 전문가를 도입하여 안정적인 기초 지식을 제공합니다. FURINA는 백본 모델에 완전히 통합될 수 있는 최초의 라우터 없는 MoE 강화 LoRA 방법으로, 추가적인 추론 시간 비용이나 복잡성을 초래하지 않습니다. 실험 결과, FURINA는 표준 LoRA를 능가하며 기존 MoE-LoRA 방법의 성능을 맞추거나 초과하면서도 추가적인 추론 시간 오버헤드를 제거합니다.

## 🎯 주요 포인트

- 1. FURINA는 기존 MoE-LoRA 방법의 제한 사항인 비합병 가능한 라우터 문제를 해결하기 위해 제안된 새로운 프레임워크입니다.

- 2. FURINA는 Self-Routing 메커니즘을 도입하여 라우터를 제거하고, 전문가 활성화를 위한 각도 유사성을 활용합니다.

- 3. 세 가지 핵심 혁신은 LoRA 어댑터의 방향과 크기의 분리 학습, 일관된 활성화 스케일링을 위한 공유 가능한 크기 벡터, 전문가 활성화를 유도하는 전문가 선택 손실입니다.

- 4. FURINA는 MoE-LoRA 블록 내에 공유 전문가를 도입하여 안정적인 기초 지식을 제공합니다.

- 5. 실험 결과, FURINA는 기존 LoRA보다 성능이 우수하며, MoE-LoRA 방법의 추가 추론 시간 비용 없이도 동등하거나 더 나은 성능을 제공합니다.

---

*Generated on 2025-09-19 15:53:29*