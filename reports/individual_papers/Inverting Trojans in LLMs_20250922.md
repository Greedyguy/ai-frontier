# Inverting Trojans in LLMs

**Korean Title:** LLM에서 트로이 목마 반전

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Implicit Blacklisting

## 🔗 유사한 논문
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (83.6% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.9% similar)
- [[2025-09-18/LLM Jailbreak Detection for (Almost) Free!_20250918|LLM Jailbreak Detection for (Almost) Free!]] (82.7% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (82.4% similar)
- [[2025-09-19/Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System_20250919|Exploit Tool Invocation Prompt for Tool Behavior Hijacking in LLM-Based Agentic System]] (82.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16203v1 Announce Type: new 
Abstract: While effective backdoor detection and inversion schemes have been developed for AIs used e.g. for images, there are challenges in "porting" these methods to LLMs. First, the LLM input space is discrete, which precludes gradient-based search over this space, central to many backdoor inversion methods. Second, there are ~30,000^k k-tuples to consider, k the token-length of a putative trigger. Third, for LLMs there is the need to blacklist tokens that have strong marginal associations with the putative target response (class) of an attack, as such tokens give false detection signals. However, good blacklists may not exist for some domains. We propose a LLM trigger inversion approach with three key components: i) discrete search, with putative triggers greedily accreted, starting from a select list of singletons; ii) implicit blacklisting, achieved by evaluating the average cosine similarity, in activation space, between a candidate trigger and a small clean set of samples from the putative target class; iii) detection when a candidate trigger elicits high misclassifications, and with unusually high decision confidence. Unlike many recent works, we demonstrate that our approach reliably detects and successfully inverts ground-truth backdoor trigger phrases.

## 🔍 Abstract (한글 번역)

arXiv:2509.16203v1 발표 유형: 신규  
초록: 이미지와 같은 AI에 사용되는 효과적인 백도어 탐지 및 반전 기법이 개발되었지만, 이러한 방법을 대형 언어 모델(LLM)로 "이식"하는 데에는 몇 가지 도전 과제가 있습니다. 첫째, LLM 입력 공간은 이산적이어서 많은 백도어 반전 방법의 중심인 이 공간에 대한 그래디언트 기반 탐색을 방해합니다. 둘째, 고려해야 할 k-튜플이 약 30,000^k개 있으며, 여기서 k는 가정된 트리거의 토큰 길이입니다. 셋째, LLM의 경우 공격의 가정된 목표 응답(클래스)과 강한 주변 연관성을 가진 토큰을 블랙리스트에 올려야 하는 필요성이 있습니다. 이러한 토큰은 잘못된 탐지 신호를 제공하기 때문입니다. 그러나 일부 도메인에서는 적절한 블랙리스트가 존재하지 않을 수 있습니다. 우리는 세 가지 주요 구성 요소를 가진 LLM 트리거 반전 접근법을 제안합니다: i) 이산적 탐색, 단일 항목의 선택 목록에서 시작하여 가정된 트리거를 탐욕적으로 축적; ii) 암묵적 블랙리스트, 가정된 목표 클래스의 작은 깨끗한 샘플 집합과 후보 트리거 간의 활성화 공간에서 평균 코사인 유사성을 평가하여 달성; iii) 후보 트리거가 높은 오분류를 유발하고, 비정상적으로 높은 결정 신뢰도를 보일 때 탐지. 많은 최근 연구와 달리, 우리는 우리의 접근법이 신뢰성 있게 탐지하고 실제 백도어 트리거 구문을 성공적으로 반전시킨다는 것을 입증합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)에서 백도어 탐지 및 반전 방법론을 제안합니다. 기존 이미지 기반 AI에서 효과적인 백도어 탐지 방법이 개발되었지만, LLM에 적용하는 데는 어려움이 있습니다. LLM의 입력 공간이 이산적이어서, 많은 백도어 반전 방법에서 중요한 역할을 하는 그래디언트 기반 탐색이 불가능합니다. 또한, LLM에서는 공격의 목표 응답과 강한 연관성을 가진 토큰을 블랙리스트로 처리해야 하지만, 일부 도메인에서는 적절한 블랙리스트가 존재하지 않을 수 있습니다. 본 연구는 세 가지 주요 구성 요소를 포함한 LLM 트리거 반전 접근법을 제안합니다: 1) 단일 토큰 리스트에서 시작하여 탐욕적으로 트리거를 축적하는 이산적 탐색, 2) 후보 트리거와 목표 클래스의 깨끗한 샘플 간의 평균 코사인 유사도를 평가하여 암묵적 블랙리스트 생성, 3) 후보 트리거가 높은 오분류와 비정상적으로 높은 결정 신뢰도를 유발할 때 탐지. 이 방법은 기존 연구와 달리 백도어 트리거 구문을 신뢰성 있게 탐지하고 반전할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. LLM의 입력 공간은 이산적이어서 기존의 기울기 기반 백도어 탐지 방법을 적용하기 어렵습니다.

- 2. LLM에서 백도어 트리거를 탐지하기 위해서는 약 30,000^k의 k-튜플을 고려해야 합니다.

- 3. LLM에서는 공격 대상 클래스와 강한 연관성을 가진 토큰을 블랙리스트 처리해야 하지만, 모든 도메인에 적합한 블랙리스트가 존재하지 않을 수 있습니다.

- 4. 제안된 방법은 이산적 탐색, 암묵적 블랙리스트, 높은 오분류와 높은 결정 신뢰도를 유발하는 트리거 탐지를 통해 LLM 백도어 트리거를 탐지합니다.

- 5. 제안된 방법은 기존 연구와 달리 실제 백도어 트리거 문구를 신뢰성 있게 탐지하고 성공적으로 반전시킵니다.

---

*Generated on 2025-09-22 15:35:01*