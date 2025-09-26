---
keywords:
  - Multi-Modal Learning
  - Chain of Action
  - Hierarchical Agent Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13347
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:17:10.198095",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-Modal Learning",
    "Chain of Action",
    "Hierarchical Agent Models"
  ],
  "rejected_keywords": [
    "Open Hierarchical Agents"
  ],
  "similarity_scores": {
    "Multi-Modal Learning": 0.78,
    "Chain of Action": 0.72,
    "Hierarchical Agent Models": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft

**Korean Title:** OpenHA: 마인크래프트에서의 오픈소스 계층적 에이전트 모델 시리즈

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-Modal Learning|Vision-Language-Action]]
**⚡ Unique Technical**: [[keywords/Chain of Action|Chain of Action]], [[keywords/Hierarchical Agent Models|Hierarchical Agent Models]]

## 🔗 유사한 논문
- [[Humanoid_Agent_via_Embodied_Chain-of-Action_Reasoning_with_Multimodal_Foundation_Models_for_Zero-Shot_Loco-Manipulation_20250918|Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation]] (83.8% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (82.0% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (80.6% similar)
- [[Imagined Autocurricula]] (80.4% similar)
- [[Agentic UAVs LLM-Driven Autonomy with Integrated Tool-Calling and Cognitive Reasoning]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13347v1 Announce Type: new 
Abstract: The choice of action spaces is a critical yet unresolved challenge in developing capable, end-to-end trainable agents. This paper first presents a large-scale, systematic comparison of prominent abstracted action spaces and tokenizers for Vision-Language-Action (VLA) or hierarchical agent models in the open-ended Minecraft. Our analysis reveals that no single action space is universally optimal; instead, the most effective abstraction is highly task-dependent, creating a dilemma for building generalist agents. To resolve this, we introduce Chain of Action (CoA), a novel framework that unifies high-level planning and low-level control within a single, monolithic VLA model. CoA treats an abstracted action not as a command for a separate policy, but as an intermediate reasoning step--akin to a chain of thought--that guides the generation of the final, executable action. Furthermore, we demonstrate that an All-in-One agent trained on a diverse mixture of action spaces using the CoA paradigm learns a more robust and generalizable policy. This unified agent achieves a new state-of-the-art, improving the overall task success rate over strong, specialized baselines. To foster reproducible research, we release the OpenHA (Open Hierarchical Agents) suite, which includes our comprehensive benchmark of over 800 distinct tasks, curated datasets, source code, and all pretrained model checkpoints at https://github.com/CraftJarvis/OpenHA

## 🔍 Abstract (한글 번역)

arXiv:2509.13347v1 발표 유형: 신규
초록: 행동 공간의 선택은 유능하고 종단 간 훈련 가능한 에이전트를 개발하는 데 있어 중요하면서도 해결되지 않은 과제이다. 본 논문은 먼저 개방형 마인크래프트 환경에서 Vision-Language-Action (VLA) 또는 계층적 에이전트 모델을 위한 주요 추상화된 행동 공간과 토크나이저에 대한 대규모 체계적 비교를 제시한다. 우리의 분석 결과, 단일한 행동 공간이 보편적으로 최적인 경우는 없으며, 대신 가장 효과적인 추상화는 높은 과제 의존성을 보여 범용 에이전트 구축에 딜레마를 야기함을 밝혀냈다. 이를 해결하기 위해 우리는 Chain of Action (CoA)이라는 새로운 프레임워크를 도입하였는데, 이는 단일한 모놀리식 VLA 모델 내에서 고수준 계획과 저수준 제어를 통합한다. CoA는 추상화된 행동을 별도 정책에 대한 명령으로 취급하지 않고, 최종 실행 가능한 행동의 생성을 안내하는 중간 추론 단계—사고 연쇄와 유사한—로 처리한다. 또한 우리는 CoA 패러다임을 사용하여 다양한 행동 공간의 혼합으로 훈련된 All-in-One 에이전트가 더욱 견고하고 일반화 가능한 정책을 학습함을 입증한다. 이 통합 에이전트는 새로운 최고 성능을 달성하여, 강력한 특화 베이스라인 대비 전반적인 과제 성공률을 향상시켰다. 재현 가능한 연구를 촉진하기 위해, 우리는 800개가 넘는 고유 과제로 구성된 포괄적 벤치마크, 큐레이션된 데이터셋, 소스 코드, 그리고 모든 사전 훈련된 모델 체크포인트를 포함하는 OpenHA (Open Hierarchical Agents) 스위트를 https://github.com/CraftJarvis/OpenHA 에서 공개한다.

## 📝 요약

이 논문은 Minecraft 환경에서 Vision-Language-Action(VLA) 모델을 위한 추상화된 행동 공간과 토크나이저를 대규모로 비교 분석합니다. 연구 결과, 단일 행동 공간이 모든 상황에 최적이 아님을 밝혀내며, 일반적인 에이전트를 구축하는 데 어려움이 있음을 지적합니다. 이를 해결하기 위해, 고수준 계획과 저수준 제어를 통합한 Chain of Action(CoA) 프레임워크를 제안합니다. CoA는 추상화된 행동을 최종 실행 가능한 행동을 생성하는 중간 추론 단계로 처리합니다. 다양한 행동 공간에서 학습된 All-in-One 에이전트는 더 강력하고 일반화된 정책을 학습하며, 기존의 강력한 특화된 기준선을 넘어서는 성과를 보입니다. 연구의 재현성을 위해 800개 이상의 태스크를 포함한 OpenHA 스위트를 공개합니다.

## 🎯 주요 포인트

- 1. 다양한 추상화된 행동 공간과 토크나이저를 비교한 결과, 단일 행동 공간이 보편적으로 최적이 아님을 발견했습니다.

- 2. Chain of Action(CoA)라는 새로운 프레임워크를 도입하여 고수준 계획과 저수준 제어를 단일 VLA 모델 내에서 통합했습니다.

- 3. CoA 패러다임을 사용하여 다양한 행동 공간에서 훈련된 All-in-One 에이전트가 더 강력하고 일반화 가능한 정책을 학습했습니다.

- 4. 통합 에이전트가 강력한 특화된 기준선을 넘어 새로운 최첨단 성과를 달성했습니다.

- 5. 재현 가능한 연구를 촉진하기 위해 800개 이상의 다양한 작업을 포함한 OpenHA 스위트를 공개했습니다.

---

*Generated on 2025-09-19 10:25:27*