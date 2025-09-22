# GUI-ReWalk: Massive Data Generation for GUI Agent via Stochastic Exploration and Intent-Aware Reasoning

**Korean Title:** GUI-ReWalk: GUI 에이전트를 위한 대규모 데이터 생성: 확률적 탐색 및 의도 인식 추론을 통한 접근

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Intent Aware Reasoning

## 🔗 유사한 논문
- [[2025-09-22/GUI-ARP_ Enhancing Grounding with Adaptive Region Perception for GUI Agents_20250922|GUI-ARP Enhancing Grounding with Adaptive Region Perception for GUI Agents]] (85.3% similar)
- [[2025-09-22/BTL-UI_ Blink-Think-Link Reasoning Model for GUI Agent_20250922|BTL-UI Blink-Think-Link Reasoning Model for GUI Agent]] (82.9% similar)
- [[2025-09-19/ScaleCUA_ Scaling Open-Source Computer Use Agents with Cross-Platform Data_20250919|ScaleCUA Scaling Open-Source Computer Use Agents with Cross-Platform Data]] (81.3% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (80.5% similar)
- [[2025-09-18/InfraMind_ A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management_20250918|InfraMind A Novel Exploration-based GUI Agentic Framework for Mission-critical Industrial Management]] (80.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15738v1 Announce Type: new 
Abstract: Graphical User Interface (GUI) Agents, powered by large language and vision-language models, hold promise for enabling end-to-end automation in digital environments. However, their progress is fundamentally constrained by the scarcity of scalable, high-quality trajectory data. Existing data collection strategies either rely on costly and inconsistent manual annotations or on synthetic generation methods that trade off between diversity and meaningful task coverage. To bridge this gap, we present GUI-ReWalk: a reasoning-enhanced, multi-stage framework for synthesizing realistic and diverse GUI trajectories. GUI-ReWalk begins with a stochastic exploration phase that emulates human trial-and-error behaviors, and progressively transitions into a reasoning-guided phase where inferred goals drive coherent and purposeful interactions. Moreover, it supports multi-stride task generation, enabling the construction of long-horizon workflows across multiple applications. By combining randomness for diversity with goal-aware reasoning for structure, GUI-ReWalk produces data that better reflects the intent-aware, adaptive nature of human-computer interaction. We further train Qwen2.5-VL-7B on the GUI-ReWalk dataset and evaluate it across multiple benchmarks, including Screenspot-Pro, OSWorld-G, UI-Vision, AndroidControl, and GUI-Odyssey. Results demonstrate that GUI-ReWalk enables superior coverage of diverse interaction flows, higher trajectory entropy, and more realistic user intent. These findings establish GUI-ReWalk as a scalable and data-efficient framework for advancing GUI agent research and enabling robust real-world automation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15738v1 발표 유형: 신규  
초록: 대형 언어 및 비전-언어 모델에 의해 구동되는 그래픽 사용자 인터페이스(GUI) 에이전트는 디지털 환경에서의 종단 간 자동화를 가능하게 할 잠재력을 가지고 있습니다. 그러나 이들의 발전은 확장 가능하고 고품질의 궤적 데이터가 부족하다는 근본적인 제약을 받고 있습니다. 기존의 데이터 수집 전략은 비용이 많이 들고 일관성이 없는 수동 주석에 의존하거나 다양성과 의미 있는 작업 범위 사이에서 균형을 이루는 합성 생성 방법에 의존합니다. 이러한 격차를 해소하기 위해, 우리는 현실적이고 다양한 GUI 궤적을 합성하기 위한 추론 강화, 다단계 프레임워크인 GUI-ReWalk를 제시합니다. GUI-ReWalk는 인간의 시행착오 행동을 모방하는 확률적 탐색 단계로 시작하여, 추론된 목표가 일관되고 목적 있는 상호작용을 이끄는 추론 안내 단계로 점진적으로 전환됩니다. 또한, 다단계 작업 생성을 지원하여 여러 애플리케이션에 걸쳐 장기적인 워크플로를 구성할 수 있습니다. 다양성을 위한 무작위성과 구조를 위한 목표 인식 추론을 결합함으로써, GUI-ReWalk는 인간-컴퓨터 상호작용의 의도 인식적이고 적응적인 특성을 더 잘 반영하는 데이터를 생성합니다. 우리는 GUI-ReWalk 데이터셋을 기반으로 Qwen2.5-VL-7B를 추가로 훈련하고, Screenspot-Pro, OSWorld-G, UI-Vision, AndroidControl, GUI-Odyssey를 포함한 여러 벤치마크에서 평가합니다. 결과는 GUI-ReWalk가 다양한 상호작용 흐름의 우수한 커버리지, 높은 궤적 엔트로피, 그리고 더 현실적인 사용자 의도를 가능하게 한다는 것을 보여줍니다. 이러한 발견은 GUI-ReWalk를 GUI 에이전트 연구를 발전시키고 강력한 실제 세계 자동화를 가능하게 하는 확장 가능하고 데이터 효율적인 프레임워크로 확립합니다.

## 📝 요약

GUI 에이전트의 발전은 고품질 경로 데이터의 부족으로 제한됩니다. 이를 해결하기 위해, 우리는 GUI-ReWalk라는 프레임워크를 제안합니다. 이 프레임워크는 인간의 시행착오를 모방하는 탐색 단계와 목표 기반의 상호작용을 유도하는 추론 단계로 구성되어 있습니다. GUI-ReWalk는 다양한 GUI 경로를 생성하며, 여러 애플리케이션에 걸친 장기 작업 흐름을 지원합니다. 이를 통해 인간-컴퓨터 상호작용의 의도 인식과 적응성을 반영하는 데이터를 생성합니다. GUI-ReWalk 데이터셋으로 Qwen2.5-VL-7B를 학습시킨 결과, 다양한 상호작용 흐름의 우수한 커버리지와 현실적인 사용자 의도를 보여주었습니다. 이러한 결과는 GUI-ReWalk가 GUI 에이전트 연구를 발전시키고 실제 자동화를 가능하게 하는 효율적인 프레임워크임을 입증합니다.

## 🎯 주요 포인트

- 1. GUI 에이전트의 발전은 확장 가능한 고품질 궤적 데이터의 부족으로 인해 제한됩니다.

- 2. GUI-ReWalk는 인간의 시행착오 행동을 모방하는 확률적 탐색 단계로 시작하여 목표 지향적 상호작용을 유도하는 추론 단계로 전환합니다.

- 3. GUI-ReWalk는 여러 애플리케이션에 걸쳐 긴 작업 흐름을 생성할 수 있는 다단계 작업 생성을 지원합니다.

- 4. GUI-ReWalk는 다양성을 위한 무작위성과 구조를 위한 목표 인식 추론을 결합하여 인간-컴퓨터 상호작용의 의도 인식적이고 적응적인 특성을 반영하는 데이터를 생성합니다.

- 5. GUI-ReWalk 데이터셋으로 학습된 Qwen2.5-VL-7B는 다양한 벤치마크에서 뛰어난 상호작용 흐름 커버리지와 현실적인 사용자 의도를 보여줍니다.

---

*Generated on 2025-09-22 15:23:06*