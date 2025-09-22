# DebFlow: Automating Agent Creation via Agent Debate

**Korean Title:** DebFlow: 에이전트 토론을 통한 에이전트 생성 자동화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Debate Mechanism

## 🔗 유사한 논문
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (84.7% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (81.6% similar)
- [[2025-09-19/FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL Matching Reward Distributions for LLM Reasoning]] (81.6% similar)
- [[2025-09-19/Judging with Many Minds_ Do More Perspectives Mean Less Prejudice On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge_20250919|Judging with Many Minds Do More Perspectives Mean Less Prejudice On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge]] (81.4% similar)
- [[2025-09-22/FLARE_ Faithful Logic-Aided Reasoning and Exploration_20250922|FLARE Faithful Logic-Aided Reasoning and Exploration]] (81.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.23781v3 Announce Type: replace 
Abstract: Large language models (LLMs) have demonstrated strong potential and impressive performance in automating the generation and optimization of workflows. However, existing approaches are marked by limited reasoning capabilities, high computational demands, and significant resource requirements. To address these issues, we propose DebFlow, a framework that employs a debate mechanism to optimize workflows and integrates reflexion to improve based on previous experiences. We evaluated our method across six benchmark datasets, including HotpotQA, MATH, and ALFWorld. Our approach achieved a 3\% average performance improvement over the latest baselines, demonstrating its effectiveness in diverse problem domains. In particular, during training, our framework reduces resource consumption by 37\% compared to the state-of-the-art baselines. Additionally, we performed ablation studies. Removing the Debate component resulted in a 4\% performance drop across two benchmark datasets, significantly greater than the 2\% drop observed when the Reflection component was removed. These findings strongly demonstrate the critical role of Debate in enhancing framework performance, while also highlighting the auxiliary contribution of reflexion to overall optimization.

## 🔍 Abstract (한글 번역)

arXiv:2503.23781v3 발표 유형: 교체  
초록: 대형 언어 모델(LLMs)은 워크플로우 생성 및 최적화 자동화에서 강력한 잠재력과 인상적인 성능을 보여주었습니다. 그러나 기존 접근 방식은 제한된 추론 능력, 높은 계산 요구 사항, 상당한 자원 요구 사항으로 특징지어집니다. 이러한 문제를 해결하기 위해 우리는 워크플로우를 최적화하기 위해 토론 메커니즘을 활용하고 이전 경험을 기반으로 개선하기 위해 반성을 통합하는 프레임워크인 DebFlow를 제안합니다. 우리는 HotpotQA, MATH, ALFWorld를 포함한 여섯 개의 벤치마크 데이터셋에서 우리의 방법을 평가했습니다. 우리의 접근 방식은 최신 기준선 대비 평균 3%의 성능 향상을 달성하여 다양한 문제 영역에서 그 효과를 입증했습니다. 특히, 훈련 중에 우리의 프레임워크는 최첨단 기준선에 비해 자원 소비를 37% 줄입니다. 또한, 우리는 제거 연구를 수행했습니다. 토론 구성 요소를 제거하면 두 개의 벤치마크 데이터셋에서 4%의 성능 저하가 발생했으며, 이는 반사 구성 요소를 제거했을 때 관찰된 2%의 저하보다 훨씬 큽니다. 이러한 발견은 프레임워크 성능을 향상시키는 데 있어 토론의 중요한 역할을 강력히 입증하며, 또한 전체 최적화에 대한 반사의 보조적 기여를 강조합니다.

## 📝 요약

대형 언어 모델(LLM)은 워크플로우 자동화에서 뛰어난 잠재력을 보이지만, 기존 접근법은 제한된 추론 능력과 높은 자원 요구량이 문제입니다. 이를 해결하기 위해 우리는 DebFlow라는 프레임워크를 제안합니다. 이 프레임워크는 토론 메커니즘을 통해 워크플로우를 최적화하고, 이전 경험을 반영하여 개선합니다. HotpotQA, MATH, ALFWorld 등 6개의 벤치마크 데이터셋에서 평가한 결과, 최신 기준선 대비 평균 3%의 성능 향상을 보였습니다. 특히, 훈련 시 자원 소비를 37% 줄였습니다. 토론 요소를 제거하면 성능이 4% 하락했으며, 반성 요소 제거 시 2% 하락했습니다. 이는 토론의 중요성과 반성의 보조적 기여를 강조합니다.

## 🎯 주요 포인트

- 1. DebFlow는 워크플로우 최적화를 위해 토론 메커니즘을 활용하고, 이전 경험을 기반으로 개선하기 위해 반성을 통합한 프레임워크입니다.

- 2. DebFlow는 최신 기준선 대비 평균 3%의 성능 향상을 달성하며, 다양한 문제 도메인에서의 효과성을 입증했습니다.

- 3. 훈련 중 DebFlow는 최첨단 기준선에 비해 자원 소비를 37% 줄였습니다.

- 4. 토론 구성 요소를 제거하면 두 개의 벤치마크 데이터셋에서 성능이 4% 감소하여, 토론의 중요성을 강조합니다.

- 5. 반성 구성 요소의 제거는 2%의 성능 감소를 초래하여, 반성이 전체 최적화에 기여함을 보여줍니다.

---

*Generated on 2025-09-22 14:31:01*