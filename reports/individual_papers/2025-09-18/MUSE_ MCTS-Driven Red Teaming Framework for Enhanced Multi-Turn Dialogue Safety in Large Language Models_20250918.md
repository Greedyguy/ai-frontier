# MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models

**Korean Title:** MUSE: 대규모 언어 모델에서 다중 턴 대화 안전성을 향상시키기 위한 MCTS 기반 레드 팀 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Siyu Yan|Siyu Yan]] [[authors/Long Zeng|Long Zeng]] [[authors/Xuecheng Wu|Xuecheng Wu]] [[authors/Chengcheng Han|Chengcheng Han]] [[authors/Kongcheng Zhang|Kongcheng Zhang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-turn Dialogue Safety

## 🔗 유사한 논문
- [[Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (84.7% similar)
- [[The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (83.5% similar)
- [[A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (83.1% similar)
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (81.4% similar)
- [[Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (81.3% similar)

## 📋 저자 정보

**Authors:** Siyu Yan, Long Zeng, Xuecheng Wu, Chengcheng Han, Kongcheng Zhang, Chong Peng, Xuezhi Cao, Xunliang Cai, Chenjuan Guo

## 📄 Abstract (원문)

As large language models~(LLMs) become widely adopted, ensuring their
alignment with human values is crucial to prevent jailbreaks where adversaries
manipulate models to produce harmful content. While most defenses target
single-turn attacks, real-world usage often involves multi-turn dialogues,
exposing models to attacks that exploit conversational context to bypass safety
measures. We introduce MUSE, a comprehensive framework tackling multi-turn
jailbreaks from both attack and defense angles. For attacks, we propose MUSE-A,
a method that uses frame semantics and heuristic tree search to explore diverse
semantic trajectories. For defense, we present MUSE-D, a fine-grained safety
alignment approach that intervenes early in dialogues to reduce
vulnerabilities. Extensive experiments on various models show that MUSE
effectively identifies and mitigates multi-turn vulnerabilities. Code is
available at
\href{https://github.com/yansiyu02/MUSE}{https://github.com/yansiyu02/MUSE}.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)이 널리 채택됨에 따라, 적대자가 모델을 조작하여 유해한 콘텐츠를 생성하는 탈옥(jailbreak)을 방지하기 위해 인간의 가치와의 정렬을 보장하는 것이 중요합니다. 대부분의 방어는 단일 턴 공격을 목표로 하지만, 실제 사용에서는 다중 턴 대화가 자주 발생하여 대화의 맥락을 악용하여 안전 조치를 우회하는 공격에 모델이 노출됩니다. 우리는 MUSE라는 포괄적인 프레임워크를 소개하여 다중 턴 탈옥을 공격과 방어 양측에서 해결합니다. 공격 측면에서는 다양한 의미적 경로를 탐색하기 위해 프레임 의미론과 휴리스틱 트리 탐색을 사용하는 MUSE-A 방법을 제안합니다. 방어 측면에서는 대화 초기에 개입하여 취약성을 줄이는 세분화된 안전 정렬 접근법인 MUSE-D를 제시합니다. 다양한 모델에 대한 광범위한 실험은 MUSE가 다중 턴 취약성을 효과적으로 식별하고 완화함을 보여줍니다. 코드는 \href{https://github.com/yansiyu02/MUSE}{https://github.com/yansiyu02/MUSE}에서 확인할 수 있습니다.

## 📝 요약

대형 언어 모델(LLM)의 사용이 증가함에 따라, 인간의 가치와의 정렬을 보장하는 것이 중요합니다. 이는 모델이 유해한 콘텐츠를 생성하지 않도록 하는 데 필수적입니다. 기존 방어책은 주로 단일 턴 공격에 초점을 맞추지만, 실제 사용에서는 다중 턴 대화가 일반적이며, 이는 대화 맥락을 이용한 공격에 취약합니다. 본 연구에서는 다중 턴 공격과 방어를 모두 다루는 MUSE 프레임워크를 제안합니다. 공격 측면에서는 프레임 의미론과 휴리스틱 트리 탐색을 활용한 MUSE-A 방법을, 방어 측면에서는 대화 초기에 개입하여 취약성을 줄이는 MUSE-D 방법을 제시합니다. 다양한 모델에 대한 실험 결과, MUSE가 다중 턴 취약성을 효과적으로 식별하고 완화함을 확인했습니다. 코드와 관련 자료는 [이곳](https://github.com/yansiyu02/MUSE)에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 인간 가치 정렬은 유해한 콘텐츠 생성을 방지하기 위해 중요합니다.

- 2. MUSE는 다중 턴 대화에서 발생하는 공격과 방어를 모두 다루는 포괄적인 프레임워크입니다.

- 3. MUSE-A는 프레임 의미론과 휴리스틱 트리 탐색을 사용하여 다양한 의미적 경로를 탐색하는 공격 방법입니다.

- 4. MUSE-D는 대화 초기에 개입하여 취약성을 줄이는 세밀한 안전 정렬 방어 방법입니다.

- 5. 다양한 모델에 대한 실험 결과, MUSE는 다중 턴 취약성을 효과적으로 식별하고 완화합니다.

---

*Generated on 2025-09-20 05:47:07*