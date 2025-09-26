---
keywords:
  - Autobidding
  - Type-Dependent Smoothness Framework
  - Liquid Welfare Price of Anarchy
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2506.20908
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:30:15.123278",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Autobidding",
    "Type-Dependent Smoothness Framework",
    "Liquid Welfare Price of Anarchy"
  ],
  "rejected_keywords": [
    "Simultaneous First-Price Auctions"
  ],
  "similarity_scores": {
    "Autobidding": 0.78,
    "Type-Dependent Smoothness Framework": 0.79,
    "Liquid Welfare Price of Anarchy": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Optimal Type-Dependent Liquid Welfare Guarantees for Autobidding Agents with Budgets

**Korean Title:** 예산을 가진 자동 입찰 에이전트를 위한 최적의 유형 의존적 유동적 복지 보장

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Autobidding|autobidding]], [[keywords/Type-Dependent Smoothness Framework|type-dependent smoothness framework]], [[keywords/Liquid Welfare Price of Anarchy|liquid welfare price of anarchy]]

## 🔗 유사한 논문
- [[Polynomial-Time Approximation Schemes via Utility Alignment Unit-Demand Pricing and More]] (80.6% similar)
- [[TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (79.5% similar)
- [[Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (78.1% similar)
- [[Delta Matters An Analytically Tractable Model for $beta$-$delta$ Discounting Agents]] (78.0% similar)
- [[JU-NLP at Touch'e Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (78.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.20908v2 Announce Type: replace 
Abstract: Online advertising systems have recently transitioned to autobidding, allowing advertisers to delegate bidding decisions to automated agents. Each advertiser directs their agent to optimize an objective function subject to return-on-investment (ROI) and budget constraints. Given their practical relevance, this shift has spurred a surge of research on the liquid welfare price of anarchy (POA) of fundamental auction formats under autobidding, most notably simultaneous first-price auctions (FPA). One of the main challenges is to understand the efficiency of FPA in the presence of heterogeneous agent types. We introduce {type-dependent smoothness framework that enables a unified analysis of the POA in such complex autobidding environments. In our approach, we derive type-dependent smoothness parameters which we carefully balance to obtain POA bounds. This balancing gives rise to a POA-revealing mathematical program, which we use to determine tight bounds on the POA of coarse correlated equilibria (CCE). Our framework is versatile enough to handle heterogeneous agent types and extends to the general class of fractionally subadditive valuations. Additionally, we develop a novel reduction technique that transforms budget-constrained agents into budget-unconstrained ones. Combining this reduction technique with our smoothness framework enables us to derive tight bounds on the POA of CCE in the general hybrid agent model with both ROI and budget constraints. Among other results, our bounds uncover an intriguing threshold phenomenon showing that the POA depends intricately on the smallest and largest agent types. We also extend our study to FPAs with reserve prices, which can be interpreted as predictions of agents' values, to further improve efficiency guarantees.

## 🔍 Abstract (한글 번역)

arXiv:2506.20908v2 발표 유형: 교체  
초록: 최근 온라인 광고 시스템은 자동 입찰로 전환되어 광고주가 입찰 결정을 자동화된 에이전트에 위임할 수 있게 되었습니다. 각 광고주는 에이전트에게 투자 수익률(ROI) 및 예산 제약 조건을 충족하는 목표 함수를 최적화하도록 지시합니다. 이러한 실질적인 중요성 때문에, 자동 입찰 하에서의 기본적인 경매 형식의 유동적 복지 무질서 가격(POA)에 대한 연구가 급증하였으며, 특히 동시 1차 가격 경매(FPA)가 주목받고 있습니다. 주요 과제 중 하나는 이질적인 에이전트 유형이 존재할 때 FPA의 효율성을 이해하는 것입니다. 우리는 이러한 복잡한 자동 입찰 환경에서 POA의 통합 분석을 가능하게 하는 유형 의존적 매끄러움 프레임워크를 도입합니다. 우리의 접근 방식에서는 POA 경계를 얻기 위해 신중하게 균형을 맞춘 유형 의존적 매끄러움 매개변수를 도출합니다. 이 균형은 POA를 드러내는 수학적 프로그램을 만들어내며, 이를 통해 조잡한 상관 균형(CCE)의 POA에 대한 엄밀한 경계를 결정합니다. 우리의 프레임워크는 이질적인 에이전트 유형을 처리할 만큼 다재다능하며, 부분적으로 가산적인 가치의 일반적인 클래스까지 확장됩니다. 또한, 우리는 예산 제약이 있는 에이전트를 예산 제약이 없는 에이전트로 변환하는 새로운 축소 기법을 개발했습니다. 이 축소 기법을 우리의 매끄러움 프레임워크와 결합함으로써, ROI 및 예산 제약이 있는 일반적인 하이브리드 에이전트 모델에서 CCE의 POA에 대한 엄밀한 경계를 도출할 수 있습니다. 다른 결과들 중에서, 우리의 경계는 POA가 가장 작은 에이전트 유형과 가장 큰 에이전트 유형에 복잡하게 의존하는 흥미로운 임계 현상을 드러냅니다. 우리는 또한 에이전트의 가치를 예측하는 것으로 해석될 수 있는 예비 가격이 있는 FPA로 연구를 확장하여 효율성 보장을 더욱 개선합니다.

## 📝 요약

이 논문은 온라인 광고 시스템에서 자동 입찰로의 전환과 관련된 연구로, 특히 이종 에이전트가 존재하는 상황에서 동시 1차 가격 경매(FPA)의 효율성을 분석합니다. 저자들은 타입 의존적 매끄러움 프레임워크를 도입하여 복잡한 자동 입찰 환경에서 복지의 무질서 가격(POA)을 통합적으로 분석합니다. 이를 통해 조잡한 상관 균형(CCE)의 POA에 대한 엄밀한 경계를 설정하고, ROI 및 예산 제약을 가진 하이브리드 에이전트 모델에서도 적용 가능한 새로운 감소 기법을 개발합니다. 연구 결과, 에이전트 유형의 크기에 따라 POA가 복잡하게 의존하는 임계 현상을 발견하고, 예약 가격이 있는 FPA로 연구를 확장하여 효율성 보장을 개선합니다.

## 🎯 주요 포인트

- 1. 온라인 광고 시스템은 자동 입찰로 전환되어 광고주가 입찰 결정을 자동화된 에이전트에 위임할 수 있게 되었습니다.

- 2. 이 연구는 자동 입찰 환경에서 이종 에이전트 유형의 존재하에 동시 1차 가격 경매(FPA)의 효율성을 이해하는 데 중점을 두고 있습니다.

- 3. 유형 의존적 매끄러움 프레임워크를 도입하여 복잡한 자동 입찰 환경에서 무질서의 가격(POA)을 통합적으로 분석합니다.

- 4. 예산 제약이 있는 에이전트를 예산 제약이 없는 에이전트로 변환하는 새로운 축소 기법을 개발하였습니다.

- 5. 연구 결과, 에이전트 유형의 크기에 따라 POA가 복잡하게 의존하는 임계 현상을 발견하였습니다.

---

*Generated on 2025-09-19 16:50:10*