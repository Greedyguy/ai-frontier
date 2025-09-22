
# Judging with Many Minds: Do More Perspectives Mean Less Prejudice? On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge

**Korean Title:** 다수의 관점으로 판단하기: 더 많은 관점이 편견을 줄이는가? 다중 에이전트 기반 LLM-as-Judge에서의 편향 증폭과 저항에 관하여

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Bias Mitigation Strategies

## 🔗 유사한 논문
- [[How Does Cognitive Bias Affect Large Language Models_ A Case Study on the Anchoring Effect in Price Negotiation Simulations_20250918|How Does Cognitive Bias Affect Large Language Models A Case Study on the Anchoring Effect in Price Negotiation Simulations]] (83.5% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (82.3% similar)
- [[Programmable_Cognitive_Bias_in_Social_Agents_20250918|Programmable Cognitive Bias in Social Agents]] (82.1% similar)
- [[The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (82.0% similar)
- [[AgentCompass Towards Reliable Evaluation of Agentic Workflows in Production]] (81.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19477v3 Announce Type: replace 
Abstract: LLM-as-Judge has emerged as a scalable alternative to human evaluation, enabling large language models (LLMs) to provide reward signals in trainings. While recent work has explored multi-agent extensions such as multi-agent debate and meta-judging to enhance evaluation quality, the question of how intrinsic biases manifest in these settings remains underexplored. In this study, we conduct a systematic analysis of four diverse bias types: position bias, verbosity bias, chain-of-thought bias, and bandwagon bias. We evaluate these biases across two widely adopted multi-agent LLM-as-Judge frameworks: Multi-Agent-Debate and LLM-as-Meta-Judge. Our results show that debate framework amplifies biases sharply after the initial debate, and this increased bias is sustained in subsequent rounds, while meta-judge approaches exhibit greater resistance. We further investigate the incorporation of PINE, a leading single-agent debiasing method, as a bias-free agent within these systems. The results reveal that this bias-free agent effectively reduces biases in debate settings but provides less benefit in meta-judge scenarios. Our work provides a comprehensive study of bias behavior in multi-agent LLM-as-Judge systems and highlights the need for targeted bias mitigation strategies in collaborative evaluation settings.

## 🔍 Abstract (한글 번역)

arXiv:2505.19477v3 발표 유형: 교체  
초록: LLM-as-Judge는 인간 평가에 대한 확장 가능한 대안으로 부상하여 대형 언어 모델(LLM)이 훈련에서 보상 신호를 제공할 수 있게 합니다. 최근 연구에서는 평가 품질을 향상시키기 위해 다중 에이전트 토론 및 메타-판단과 같은 다중 에이전트 확장을 탐구했지만, 이러한 설정에서 내재된 편향이 어떻게 나타나는지는 충분히 탐구되지 않았습니다. 본 연구에서는 위치 편향, 장황함 편향, 사고의 연쇄 편향, 밴드왜건 편향 등 네 가지 다양한 편향 유형에 대한 체계적인 분석을 수행합니다. 우리는 Multi-Agent-Debate 및 LLM-as-Meta-Judge라는 두 가지 널리 채택된 다중 에이전트 LLM-as-Judge 프레임워크에서 이러한 편향을 평가합니다. 우리의 결과는 토론 프레임워크가 초기 토론 이후 편향을 급격히 증폭시키고, 이러한 증가된 편향이 후속 라운드에서도 지속되는 반면, 메타-판단 접근법은 더 큰 저항을 나타낸다는 것을 보여줍니다. 우리는 또한 이러한 시스템 내에서 편향 없는 에이전트로서 선도적인 단일 에이전트 편향 제거 방법인 PINE의 통합을 조사합니다. 결과는 이 편향 없는 에이전트가 토론 설정에서 편향을 효과적으로 줄이지만 메타-판단 시나리오에서는 덜 유익하다는 것을 보여줍니다. 우리의 연구는 다중 에이전트 LLM-as-Judge 시스템에서의 편향 행동에 대한 포괄적인 연구를 제공하며, 협력적 평가 설정에서의 목표 편향 완화 전략의 필요성을 강조합니다.

## 📝 요약

이 연구는 LLM-as-Judge 시스템에서 발생하는 내재적 편향을 분석하여 인간 평가의 대안으로서의 가능성을 탐구합니다. 특히, 다중 에이전트 토론과 메타-판단 프레임워크에서 위치 편향, 장황함 편향, 사고의 흐름 편향, 밴드왜건 편향 등 네 가지 편향을 체계적으로 분석했습니다. 연구 결과, 토론 프레임워크는 초기 토론 이후 편향을 크게 증폭시키며, 이러한 편향은 이후 라운드에서도 지속됩니다. 반면, 메타-판단 접근법은 편향에 더 강한 저항성을 보였습니다. 또한, PINE라는 단일 에이전트 편향 완화 방법을 도입하여 편향 없는 에이전트로 활용한 결과, 토론 환경에서는 편향을 효과적으로 줄였지만 메타-판단 시나리오에서는 그 효과가 덜했습니다. 이 연구는 다중 에이전트 LLM-as-Judge 시스템에서의 편향 행동을 포괄적으로 분석하고, 협업 평가 환경에서의 편향 완화 전략의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. LLM-as-Judge는 인간 평가의 대안으로, 대규모 언어 모델이 보상 신호를 제공할 수 있도록 한다.

- 2. 본 연구는 위치 편향, 장황함 편향, 사고의 흐름 편향, 밴드왜건 편향 등 네 가지 다양한 편향 유형을 체계적으로 분석한다.

- 3. Multi-Agent-Debate 프레임워크는 초기 토론 후 편향을 크게 증폭시키고, 이러한 편향은 후속 라운드에서도 지속된다.

- 4. PINE라는 단일 에이전트 디바이싱 방법을 도입하여 편향 없는 에이전트로서의 효과를 평가한 결과, 토론 설정에서 편향을 효과적으로 줄이는 반면, 메타-판단 시나리오에서는 덜 효과적이다.

- 5. 본 연구는 다중 에이전트 LLM-as-Judge 시스템에서의 편향 행동을 포괄적으로 연구하고, 협력적 평가 환경에서의 편향 완화 전략의 필요성을 강조한다.

---

*Generated on 2025-09-19 15:09:33*