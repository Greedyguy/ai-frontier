
# Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue

**Korean Title:** 명확히 묻기: 다중 회차 대화를 통한 지시 모호성 해결

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Collaborative Embodied Agents

## 🔗 유사한 논문
- [[CollabVLA Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (88.4% similar)
- [[ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (85.0% similar)
- [[AI Agents with Human-Like Collaborative Tools Adaptive Strategies for Enhanced Problem-Solving]] (83.9% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (83.2% similar)
- [[Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery_20250919|Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery]] (82.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15061v1 Announce Type: new 
Abstract: The ultimate goal of embodied agents is to create collaborators that can interact with humans, not mere executors that passively follow instructions. This requires agents to communicate, coordinate, and adapt their actions based on human feedback. Recently, advances in VLAs have offered a path toward this goal. However, most current VLA-based embodied agents operate in a one-way mode: they receive an instruction and execute it without feedback. This approach fails in real-world scenarios where instructions are often ambiguous. In this paper, we address this problem with the Ask-to-Clarify framework. Our framework first resolves ambiguous instructions by asking questions in a multi-turn dialogue. Then it generates low-level actions end-to-end. Specifically, the Ask-to-Clarify framework consists of two components, one VLM for collaboration and one diffusion for action. We also introduce a connection module that generates conditions for the diffusion based on the output of the VLM. This module adjusts the observation by instructions to create reliable conditions. We train our framework with a two-stage knowledge-insulation strategy. First, we fine-tune the collaboration component using ambiguity-solving dialogue data to handle ambiguity. Then, we integrate the action component while freezing the collaboration one. This preserves the interaction abilities while fine-tuning the diffusion to generate actions. The training strategy guarantees our framework can first ask questions, then generate actions. During inference, a signal detector functions as a router that helps our framework switch between asking questions and taking actions. We evaluate the Ask-to-Clarify framework in 8 real-world tasks, where it outperforms existing state-of-the-art VLAs. The results suggest that our proposed framework, along with the training strategy, provides a path toward collaborative embodied agents.

## 🔍 Abstract (한글 번역)

arXiv:2509.15061v1 발표 유형: 신규  
초록: 구현된 에이전트의 궁극적인 목표는 단순히 지시를 수동적으로 따르는 실행자가 아닌 인간과 상호작용할 수 있는 협력자를 만드는 것입니다. 이를 위해 에이전트는 인간의 피드백을 기반으로 의사소통하고, 조정하며, 행동을 적응시켜야 합니다. 최근 VLA의 발전은 이 목표를 향한 경로를 제공했습니다. 그러나 대부분의 현재 VLA 기반 구현 에이전트는 일방적인 방식으로 작동합니다: 지시를 받고 피드백 없이 이를 실행합니다. 이 접근 방식은 지시가 종종 모호한 실제 시나리오에서 실패합니다. 본 논문에서는 Ask-to-Clarify 프레임워크로 이 문제를 해결합니다. 우리의 프레임워크는 먼저 다중 회차 대화에서 질문을 통해 모호한 지시를 해결합니다. 그런 다음 저수준 행동을 종단 간 생성합니다. 구체적으로, Ask-to-Clarify 프레임워크는 협업을 위한 하나의 VLM과 행동을 위한 하나의 확산으로 구성됩니다. 우리는 또한 VLM의 출력을 기반으로 확산 조건을 생성하는 연결 모듈을 소개합니다. 이 모듈은 신뢰할 수 있는 조건을 생성하기 위해 지시에 따라 관찰을 조정합니다. 우리는 두 단계의 지식 절연 전략으로 프레임워크를 훈련합니다. 먼저, 모호성을 해결하는 대화 데이터를 사용하여 협업 구성 요소를 미세 조정하여 모호성을 처리합니다. 그런 다음, 협업 구성 요소를 고정한 상태에서 행동 구성 요소를 통합합니다. 이는 상호작용 능력을 유지하면서 확산을 미세 조정하여 행동을 생성하도록 합니다. 훈련 전략은 우리의 프레임워크가 먼저 질문을 하고, 그 다음 행동을 생성할 수 있도록 보장합니다. 추론 중에는 신호 탐지기가 라우터로 작동하여 프레임워크가 질문을 하는 것과 행동을 취하는 것 사이를 전환하도록 돕습니다. 우리는 8개의 실제 과제에서 Ask-to-Clarify 프레임워크를 평가했으며, 기존의 최첨단 VLA를 능가했습니다. 결과는 제안된 프레임워크와 훈련 전략이 협력적인 구현 에이전트로 가는 경로를 제공함을 시사합니다.

## 📝 요약

이 논문은 인간과 상호작용할 수 있는 협력적 구현 에이전트를 목표로 하는 연구로, 모호한 지시를 해결하기 위해 질문을 통해 명확히 하고, 저수준 행동을 생성하는 Ask-to-Clarify 프레임워크를 제안합니다. 이 프레임워크는 협업을 위한 VLM과 행동 생성을 위한 확산 모듈로 구성되며, 두 모듈 간 연결을 통해 조건을 생성합니다. 두 단계의 지식 격리 전략을 사용하여 모호성을 해결하는 대화 데이터를 통해 협업 모듈을 미세 조정하고, 행동 모듈을 통합하여 행동 생성을 최적화합니다. 8개의 실제 과제에서 기존 최첨단 VLA를 능가하는 성능을 보이며, 제안된 프레임워크와 훈련 전략이 협력적 구현 에이전트 개발에 기여할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 본 연구는 인간과 상호작용할 수 있는 협력형 구현 에이전트를 목표로 하며, 이를 위해 Ask-to-Clarify 프레임워크를 제안합니다.

- 2. 제안된 프레임워크는 모호한 지시를 해결하기 위해 다중 회차 대화를 통해 질문을 하고, 저수준의 행동을 생성합니다.

- 3. Ask-to-Clarify 프레임워크는 협업을 위한 VLM과 행동 생성을 위한 확산 모듈로 구성되며, 연결 모듈을 통해 두 컴포넌트를 조정합니다.

- 4. 두 단계의 지식 절연 전략을 통해 협업 컴포넌트를 미세 조정하고, 행동 컴포넌트를 통합하여 프레임워크의 상호작용 능력을 유지합니다.

- 5. 8개의 실제 과제에서 프레임워크를 평가한 결과, 기존 최첨단 VLA를 능가하는 성능을 보여 협력형 구현 에이전트 개발에 기여할 수 있음을 시사합니다.

---

*Generated on 2025-09-19 16:36:23*