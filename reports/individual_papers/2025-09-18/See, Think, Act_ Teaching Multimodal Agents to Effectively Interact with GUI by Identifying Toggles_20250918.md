
# See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI by Identifying Toggles

**Korean Title:** 보기, 생각하기, 행동하기: 토글 식별을 통해 멀티모달 에이전트가 GUI와 효과적으로 상호작용하도록 교육하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Toggle Instruction Execution

## 🔗 유사한 논문
- [[VeriOS Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents]] (81.4% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (80.4% similar)
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (79.9% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (79.6% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13615v1 Announce Type: new 
Abstract: The advent of multimodal agents facilitates effective interaction within graphical user interface (GUI), especially in ubiquitous GUI control. However, their inability to reliably execute toggle control instructions remains a key bottleneck. To investigate this, we construct a state control benchmark with binary toggle instructions from public datasets. Evaluations of existing agents demonstrate their unreliability, particularly when the current toggle state already matches the desired state. To address the challenge, we propose State-aware Reasoning (StaR), a training method that teaches agents to perceive the current toggle state, analyze the desired state from the instruction, and act accordingly. Experiments on three multimodal agents demonstrate that StaR can improve toggle instruction execution accuracy by over 30\%. Further evaluations on three public benchmarks show that StaR also enhances general task performance. Finally, evaluations on a dynamic environment highlight the potential of StaR for real-world applications. Code, benchmark, and StaR-enhanced agents are available at https://github.com/ZrW00/StaR.

## 🔍 Abstract (한글 번역)

arXiv:2509.13615v1 발표 유형: 신규
초록: 멀티모달 에이전트의 등장은 그래픽 사용자 인터페이스(GUI) 내에서의 효과적인 상호작용을 촉진하며, 특히 유비쿼터스 GUI 제어에서 그러하다. 그러나 토글 제어 명령을 안정적으로 실행하지 못하는 능력 부족이 주요 병목지점으로 남아있다. 이를 조사하기 위해, 우리는 공개 데이터셋으로부터 이진 토글 명령을 포함한 상태 제어 벤치마크를 구축하였다. 기존 에이전트들에 대한 평가는 특히 현재 토글 상태가 이미 원하는 상태와 일치할 때 그들의 불안정성을 보여준다. 이러한 도전과제를 해결하기 위해, 우리는 에이전트가 현재 토글 상태를 인식하고, 명령으로부터 원하는 상태를 분석하며, 그에 따라 행동하도록 가르치는 훈련 방법인 상태 인식 추론(StaR)을 제안한다. 세 개의 멀티모달 에이전트에 대한 실험은 StaR이 토글 명령 실행 정확도를 30% 이상 향상시킬 수 있음을 보여준다. 세 개의 공개 벤치마크에 대한 추가 평가는 StaR이 일반적인 작업 성능 또한 향상시킴을 보여준다. 마지막으로, 동적 환경에서의 평가는 실제 응용을 위한 StaR의 잠재력을 강조한다. 코드, 벤치마크, 그리고 StaR이 향상된 에이전트들은 https://github.com/ZrW00/StaR 에서 이용 가능하다.

## 📝 요약

다중 모달 에이전트는 그래픽 사용자 인터페이스(GUI)와의 상호작용을 촉진하지만, 토글 제어 명령을 신뢰성 있게 수행하지 못하는 문제가 있습니다. 이를 해결하기 위해, 우리는 공개 데이터셋에서 이진 토글 명령을 사용한 상태 제어 벤치마크를 구축했습니다. 기존 에이전트의 평가 결과, 현재 토글 상태가 원하는 상태와 일치할 때 특히 신뢰성이 떨어지는 것으로 나타났습니다. 이를 개선하기 위해, 우리는 State-aware Reasoning (StaR)이라는 훈련 방법을 제안하여 에이전트가 현재 토글 상태를 인식하고, 명령에서 원하는 상태를 분석하여 적절히 행동하도록 가르칩니다. 세 가지 다중 모달 에이전트에 대한 실험 결과, StaR은 토글 명령 수행 정확도를 30% 이상 향상시켰습니다. 또한, 세 가지 공개 벤치마크에서 StaR은 일반적인 작업 성능도 향상시켰으며, 동적 환경에서의 평가를 통해 실세계 응용 가능성을 확인했습니다. 코드와 벤치마크, StaR로 강화된 에이전트는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 멀티모달 에이전트는 GUI 내 상호작용을 촉진하지만, 토글 제어 명령 실행의 신뢰성 부족이 문제점으로 지적됩니다.

- 2. 이 문제를 해결하기 위해 이진 토글 명령을 포함한 상태 제어 벤치마크를 구축하고, 기존 에이전트의 신뢰성을 평가했습니다.

- 3. StaR(State-aware Reasoning)라는 훈련 방법을 제안하여 에이전트가 현재 토글 상태를 인식하고 원하는 상태를 분석하여 적절히 행동하도록 가르칩니다.

- 4. StaR는 세 가지 멀티모달 에이전트의 토글 명령 실행 정확성을 30% 이상 향상시켰습니다.

- 5. StaR는 세 가지 공개 벤치마크에서 일반적인 작업 성능을 향상시키며, 동적 환경에서의 평가를 통해 실제 응용 가능성을 보여줍니다.

---

*Generated on 2025-09-19 10:29:27*