
# ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning

**Korean Title:** ThinkAct: 강화된 시각 잠재 계획을 통한 비전-언어-행동 추론

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Multimodal Learning, Few-shot Adaptation

## 🔗 유사한 논문
- [[CLAW A Vision-Language-Action Framework for Weight-Aware Robotic Grasping]] (85.2% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (83.9% similar)
- [[GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (83.5% similar)
- [[FSR-VLN Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (83.0% similar)
- [[OpenHA A Series of Open-Source Hierarchical Agentic Models in Minecraft]] (82.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.16815v2 Announce Type: replace-cross 
Abstract: Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## 🔍 Abstract (한글 번역)

arXiv:2507.16815v2 발표 유형: 교체-교차  
초록: 시각-언어-행동(VLA) 추론 과제는 에이전트가 다중 모달 지시를 해석하고, 장기 계획을 수행하며, 동적 환경에서 적응적으로 행동할 것을 요구합니다. 기존 접근 방식은 일반적으로 VLA 모델을 입력을 행동으로 직접 매핑하는 종단 간 방식으로 훈련하며, 명시적인 추론 없이 작동하여 여러 단계에 걸친 계획 수립이나 복잡한 과제 변형에 적응하는 능력을 저해합니다. 본 논문에서는 강화된 시각 잠재 계획을 통해 고차원 추론과 저차원 행동 실행을 연결하는 이중 시스템 프레임워크인 ThinkAct를 제안합니다. ThinkAct는 목표 달성 및 경로 일관성에 기반한 행동 정렬 시각 보상에 의해 안내되는 구현된 추론 계획을 생성하기 위해 다중 모달 LLM을 훈련합니다. 이러한 추론 계획은 목표 환경에서의 강력한 행동 실행을 위한 하위 행동 모델을 조건화하는 시각 계획 잠재로 압축됩니다. 구현된 추론 및 로봇 조작 벤치마크에 대한 광범위한 실험은 ThinkAct가 복잡한 구현 AI 과제에서 적은 샷 적응, 장기 계획 및 자기 수정 행동을 가능하게 함을 보여줍니다.

## 📝 요약

이 논문에서는 비전-언어-행동(VLA) 추론 과제를 해결하기 위해 ThinkAct라는 이중 시스템 프레임워크를 제안합니다. 기존 방법들은 입력을 행동으로 직접 매핑하여 명시적인 추론 없이 학습하지만, 이는 복잡한 과제 변형에 적응하거나 여러 단계를 계획하는 데 한계를 가집니다. ThinkAct는 강화된 시각적 잠재 계획을 통해 고수준의 추론과 저수준의 행동 실행을 연결합니다. 이 접근법은 멀티모달 대형 언어 모델(LLM)을 훈련시켜 목표 달성 및 경로 일관성을 기반으로 한 시각적 보상을 통해 체화된 추론 계획을 생성합니다. 이러한 계획은 시각적 잠재 계획으로 압축되어 목표 환경에서 강력한 행동 실행을 위한 행동 모델을 조건화합니다. 실험 결과, ThinkAct는 복잡한 체화 AI 과제에서 소수의 샘플로 적응, 장기 계획, 자기 수정 능력을 가능하게 함을 보여줍니다.

## 🎯 주요 포인트

- 1. Vision-language-action (VLA) 추론 과제는 다중 모달 지시를 해석하고, 장기 계획을 수행하며, 동적 환경에서 적응적으로 행동해야 합니다.

- 2. 기존 접근법은 입력을 행동으로 직접 매핑하는 방식으로, 명시적인 추론 없이 VLA 모델을 훈련하여 다단계 계획이나 복잡한 과제 변형에 적응하는 능력을 저해합니다.

- 3. ThinkAct는 강화된 시각 잠재 계획을 통해 고수준 추론과 저수준 행동 실행을 연결하는 이중 시스템 프레임워크를 제안합니다.

- 4. ThinkAct는 목표 달성과 경로 일관성에 기반한 강화된 행동 정렬 시각 보상에 의해 유도된 구현된 추론 계획을 생성하도록 다중 모달 LLM을 훈련합니다.

- 5. ThinkAct는 복잡한 구현 AI 과제에서 몇 샷 적응, 장기 계획 및 자기 수정 행동을 가능하게 함을 입증합니다.

---

*Generated on 2025-09-19 15:19:25*