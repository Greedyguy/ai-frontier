
# HLSMAC: A New StarCraft Multi-Agent Challenge for High-Level Strategic Decision-Making

**Korean Title:** HLSMAC: 고수준 전략 결정을 위한 새로운 스타크래프트 멀티 에이전트 도전.

## 📋 메타데이터

**Links**: [[daily/2025-09-16|2025-09-16]] [[authors/Xingxing Hong|Xingxing Hong]] [[authors/Yungong Wang|Yungong Wang]] [[authors/Dexin Jin|Dexin Jin]] [[authors/Ye Yuan|Ye Yuan]] [[authors/Ximing Huang|Ximing Huang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Thirty-Six Stratagems

## 🔗 유사한 논문
- [[OpenHA_A_Series_of_Open-Source_Hierarchical_Agentic_Models_in_Minecraft_20250918|OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft]] (78.4% similar)
- [[$Agent^2$_An_Agent-Generates-Agent_Framework_for_Reinforcement_Learning_Automation_20250918|$Agent^2$: An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (78.3% similar)
- [[Inject, Fork, Compare: Defining an Interaction Vocabulary for Multi-Agent Simulation Platforms]] (77.7% similar)
- [[MARS2 2025 Challenge on Multimodal Reasoning: Datasets, Methods, Results, Discussion, and Outlook]] (77.6% similar)
- [[MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (77.6% similar)

## 📋 저자 정보

**Authors:** Xingxing Hong, Yungong Wang, Dexin Jin, Ye Yuan, Ximing Huang, Zijian Wu, Wenxin Li

## 📄 Abstract (원문)

Benchmarks are crucial for assessing multi-agent reinforcement learning
(MARL) algorithms. While StarCraft II-related environments have driven
significant advances in MARL, existing benchmarks like SMAC focus primarily on
micromanagement, limiting comprehensive evaluation of high-level strategic
intelligence. To address this, we introduce HLSMAC, a new cooperative MARL
benchmark with 12 carefully designed StarCraft II scenarios based on classical
stratagems from the Thirty-Six Stratagems. Each scenario corresponds to a
specific stratagem and is designed to challenge agents with diverse strategic
elements, including tactical maneuvering, timing coordination, and deception,
thereby opening up avenues for evaluating high-level strategic decision-making
capabilities. We also propose novel metrics across multiple dimensions beyond
conventional win rate, such as ability utilization and advancement efficiency,
to assess agents' overall performance within the HLSMAC environment. We
integrate state-of-the-art MARL algorithms and LLM-based agents with our
benchmark and conduct comprehensive experiments. The results demonstrate that
HLSMAC serves as a robust testbed for advancing multi-agent strategic
decision-making.

## 🔍 Abstract (한글 번역)

벤치마크는 다중 에이전트 강화 학습(MARL) 알고리즘을 평가하는 데 중요합니다. 스타크래프트 II 관련 환경은 MARL에서 중요한 발전을 이끌어내었지만, SMAC와 같은 기존의 벤치마크는 주로 미세 관리에 초점을 맞추어 고수준 전략 지능의 포괄적인 평가를 제한합니다. 이를 해결하기 위해, 우리는 고전 전략인 서육전 중 12가지 정교하게 설계된 스타크래프트 II 시나리오를 기반으로 한 새로운 협력 MARL 벤치마크인 HLSMAC을 소개합니다. 각 시나리오는 특정 전략에 해당하며, 전술적 조작, 시기 조정, 속임수를 포함한 다양한 전략적 요소로 에이전트를 도전하도록 설계되어 있어 고수준 전략적 의사 결정 능력을 평가할 수 있는 길을 열어줍니다. 또한 HLSMAC 환경 내에서 에이전트의 전반적인 성능을 평가하기 위해 승률 이외의 능력 활용 및 진보 효율성과 같은 새로운 측정 항목을 제안합니다. 우리는 최신 MARL 알고리즘과 LLM 기반 에이전트를 우리의 벤치마크와 통합하고 포괄적인 실험을 수행합니다. 결과는 HLSMAC이 다중 에이전트 전략적 의사 결정을 발전시키는 견고한 실험대로 작용함을 보여줍니다.

## 📝 요약

본 연구는 다중 에이전트 강화학습 알고리즘을 평가하는 데 중요한 기준인 벤치마크에 대해 다룬다. 기존의 SMAC과 같은 벤치마크는 주로 미세한 관리에 초점을 맞춰 왔지만, 본 연구에서는 고수준 전략 지능을 포괄적으로 평가하기 위해 Thirty-Six Stratagems에서 영감을 받은 12가지 StarCraft II 시나리오를 기반으로 한 새로운 협력적 MARL 벤치마크인 HLSMAC을 제안한다. 각 시나리오는 특정 전략을 반영하며, 전술적 조작, 타이밍 조정, 속임수 등 다양한 전략 요소에 대한 에이전트의 도전을 의도하였다. 또한 이를 통해 이기는 비율 이외에 능력 활용 및 진보 효율성과 같은 새로운 메트릭을 제안하여 HLSMAC 환경에서 에이전트의 전반적인 성능을 평가한다. 최신 MARL 알고리즘과 LLM 기반 에이전트를 통합하고 포괄적인 실험을 수행한 결과, HLSMAC은 다중 에이전트 전략적 의사 결정을 발전시키는 견고한 실험 대상으로서의 역할을 한다는 것을 입증하였다.

## 🎯 주요 포인트

- StarCraft II 관련 환경에 기반한 HLSMAC는 고전 전략에서 영감을 받은 12가지 StarCraft II 시나리오를 제공한다.

- HLSMAC는 전술적 기동, 타이밍 조정, 속임수 등 다양한 전략적 요소를 포함하여 에이전트들을 도전한다.

- 이러한 측면을 평가하기 위해 전통적인 승률 이외에 능력 활용 및 진보 효율성과 같은 새로운 메트릭을 제안한다.

---

*Generated on 2025-09-18 16:06:16*