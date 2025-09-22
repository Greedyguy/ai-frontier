
# Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity

**Korean Title:** 전략적 다양성을 위한 구성적 갈등 기반 다중 에이전트 강화 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Strategic Diversity

## 🔗 유사한 논문
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (82.3% similar)
- [[Beyond the high score Prosocial ability profiles of multi-agent populations]] (81.3% similar)
- [[HLSMAC A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making]] (80.5% similar)
- [[AI Agents with Human-Like Collaborative Tools Adaptive Strategies for Enhanced Problem-Solving]] (80.2% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (80.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14276v1 Announce Type: cross 
Abstract: In recent years, diversity has emerged as a useful mechanism to enhance the efficiency of multi-agent reinforcement learning (MARL). However, existing methods predominantly focus on designing policies based on individual agent characteristics, often neglecting the interplay and mutual influence among agents during policy formation. To address this gap, we propose Competitive Diversity through Constructive Conflict (CoDiCon), a novel approach that incorporates competitive incentives into cooperative scenarios to encourage policy exchange and foster strategic diversity among agents. Drawing inspiration from sociological research, which highlights the benefits of moderate competition and constructive conflict in group decision-making, we design an intrinsic reward mechanism using ranking features to introduce competitive motivations. A centralized intrinsic reward module generates and distributes varying reward values to agents, ensuring an effective balance between competition and cooperation. By optimizing the parameterized centralized reward module to maximize environmental rewards, we reformulate the constrained bilevel optimization problem to align with the original task objectives. We evaluate our algorithm against state-of-the-art methods in the SMAC and GRF environments. Experimental results demonstrate that CoDiCon achieves superior performance, with competitive intrinsic rewards effectively promoting diverse and adaptive strategies among cooperative agents.

## 🔍 Abstract (한글 번역)

arXiv:2509.14276v1 발표 유형: 교차  
초록: 최근 몇 년간, 다양성은 다중 에이전트 강화 학습(MARL)의 효율성을 향상시키는 유용한 메커니즘으로 부각되었습니다. 그러나 기존 방법들은 주로 개별 에이전트의 특성에 기반하여 정책을 설계하는 데 중점을 두며, 정책 형성 과정에서 에이전트 간의 상호 작용과 상호 영향을 종종 간과합니다. 이러한 격차를 해소하기 위해, 우리는 협력 시나리오에 경쟁적 인센티브를 도입하여 정책 교환을 장려하고 에이전트 간의 전략적 다양성을 촉진하는 새로운 접근법인 건설적 갈등을 통한 경쟁적 다양성(CoDiCon)을 제안합니다. 사회학 연구에서 중간 수준의 경쟁과 건설적 갈등이 그룹 의사 결정에 미치는 이점에 영감을 받아, 우리는 경쟁적 동기를 도입하기 위해 순위 기능을 사용하는 내재적 보상 메커니즘을 설계합니다. 중앙 집중식 내재적 보상 모듈은 에이전트에게 다양한 보상 값을 생성하고 분배하여 경쟁과 협력 간의 효과적인 균형을 보장합니다. 환경 보상을 극대화하기 위해 매개변수화된 중앙 보상 모듈을 최적화함으로써, 우리는 제약된 이중 최적화 문제를 원래의 과제 목표에 맞추어 재구성합니다. 우리는 SMAC 및 GRF 환경에서 최첨단 방법들과 우리의 알고리즘을 비교 평가합니다. 실험 결과, CoDiCon은 협력 에이전트 간의 다양한 적응 전략을 효과적으로 촉진하는 경쟁적 내재적 보상으로 인해 우수한 성능을 달성함을 보여줍니다.

## 📝 요약

최근 다중 에이전트 강화 학습(MARL)에서 다양성은 효율성을 높이는 유용한 메커니즘으로 부각되고 있습니다. 그러나 기존 방법들은 주로 개별 에이전트의 특성에 기반한 정책 설계에 집중하여 에이전트 간 상호작용을 간과하는 경향이 있습니다. 이를 해결하기 위해, 우리는 경쟁적 인센티브를 협력적 시나리오에 도입하여 정책 교환과 전략적 다양성을 촉진하는 CoDiCon(Constructive Conflict)을 제안합니다. 사회학 연구에서 중간 수준의 경쟁과 건설적 갈등이 그룹 의사결정에 유익하다는 점에 착안하여, 랭킹 기능을 활용한 내재적 보상 메커니즘을 설계했습니다. 중앙 집중형 내재적 보상 모듈은 에이전트들에게 다양한 보상 값을 분배하여 경쟁과 협력의 균형을 효과적으로 유지합니다. 환경 보상을 극대화하기 위해 매개변수화된 중앙 보상 모듈을 최적화하여 원래의 과제 목표와 일치하도록 제약된 이중 최적화 문제를 재구성했습니다. SMAC 및 GRF 환경에서 최첨단 방법들과 비교 평가한 결과, CoDiCon이 우수한 성능을 보였으며, 경쟁적 내재적 보상이 협력적 에이전트 간의 다양한 적응 전략을 효과적으로 촉진함을 입증했습니다.

## 🎯 주요 포인트

- 1. 최근 다중 에이전트 강화 학습(MARL)의 효율성을 높이기 위해 다양성이 중요한 메커니즘으로 부상하고 있습니다.

- 2. 기존 방법들은 주로 개별 에이전트의 특성에 기반한 정책 설계에 집중하여 에이전트 간 상호 작용과 영향력을 간과하는 경향이 있습니다.

- 3. CoDiCon은 경쟁적 인센티브를 협력 시나리오에 도입하여 에이전트 간의 전략적 다양성을 촉진하는 새로운 접근 방식입니다.

- 4. 사회학 연구에서 영감을 받아, 중간 수준의 경쟁과 건설적 갈등이 그룹 의사 결정에 유익하다는 점을 활용하여 내재적 보상 메커니즘을 설계했습니다.

- 5. 실험 결과, CoDiCon은 SMAC 및 GRF 환경에서 최첨단 방법들과 비교하여 우수한 성능을 보였으며, 경쟁적 내재 보상이 협력적 에이전트 간의 다양한 적응 전략을 효과적으로 촉진했습니다.

---

*Generated on 2025-09-19 14:52:53*