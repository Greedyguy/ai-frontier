
# Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture

**Korean Title:** 블랙 박스 열기: 의미 공명 아키텍처를 통한 해석 가능한 대형 언어 모델(LLM)

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Semantic Routing

## 🔗 유사한 논문
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (84.7% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (84.2% similar)
- [[CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (83.1% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (82.9% similar)
- [[Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary]] (82.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14255v1 Announce Type: cross 
Abstract: Large language models (LLMs) achieve remarkable performance but remain difficult to interpret. Mixture-of-Experts (MoE) models improve efficiency through sparse activation, yet typically rely on opaque, learned gating functions. While similarity-based routing (Cosine Routers) has been explored for training stabilization, its potential for inherent interpretability remains largely untapped. We introduce the Semantic Resonance Architecture (SRA), an MoE approach designed to ensure that routing decisions are inherently interpretable. SRA replaces learned gating with a Chamber of Semantic Resonance (CSR) module, which routes tokens based on cosine similarity with trainable semantic anchors. We also introduce a novel Dispersion Loss that encourages orthogonality among anchors to enforce diverse specialization. Experiments on WikiText-103 demonstrate that SRA achieves a validation perplexity of 13.41, outperforming both a dense baseline (14.13) and a Standard MoE baseline (13.53) under matched active parameter constraints (29.0M). Crucially, SRA exhibits superior expert utilization (1.0% dead experts vs. 14.8% in the Standard MoE) and develops distinct, semantically coherent specialization patterns, unlike the noisy specialization observed in standard MoEs. This work establishes semantic routing as a robust methodology for building more transparent and controllable language models.

## 🔍 Abstract (한글 번역)

arXiv:2509.14255v1 발표 유형: 교차  
초록: 대형 언어 모델(LLMs)은 뛰어난 성능을 발휘하지만 해석하기 어려운 경우가 많습니다. 전문가 혼합(MoE) 모델은 희소 활성화를 통해 효율성을 개선하지만, 일반적으로 불투명한 학습 게이팅 기능에 의존합니다. 유사성 기반 라우팅(코사인 라우터)은 훈련 안정화를 위해 탐구되었지만, 내재적 해석 가능성에 대한 잠재력은 크게 활용되지 않았습니다. 우리는 라우팅 결정이 본질적으로 해석 가능하도록 설계된 MoE 접근 방식인 의미 공명 아키텍처(SRA)를 소개합니다. SRA는 학습된 게이팅을 훈련 가능한 의미 앵커와의 코사인 유사성에 기반하여 토큰을 라우팅하는 의미 공명 챔버(CSR) 모듈로 대체합니다. 또한 앵커 간의 직교성을 장려하여 다양한 전문화를 강화하는 새로운 분산 손실을 도입합니다. WikiText-103에 대한 실험은 SRA가 검증 혼란도 13.41을 달성하여 밀집 기준선(14.13)과 표준 MoE 기준선(13.53)을 능동 매개변수 제약(29.0M) 하에서 능가함을 보여줍니다. 중요한 것은, SRA가 전문가 활용도에서 우수한 성과를 보이며(비활성 전문가 1.0% vs. 표준 MoE의 14.8%) 표준 MoE에서 관찰되는 소음이 많은 전문화와 달리 뚜렷하고 의미론적으로 일관된 전문화 패턴을 개발한다는 것입니다. 이 연구는 보다 투명하고 제어 가능한 언어 모델을 구축하기 위한 강력한 방법론으로 의미 라우팅을 확립합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 해석 가능성을 높이기 위해 혼합 전문가(MoE) 모델의 새로운 접근법인 Semantic Resonance Architecture(SRA)를 제안합니다. SRA는 기존의 불투명한 게이팅 기능을 대체하여, 코사인 유사성을 기반으로 토큰을 라우팅하는 Chamber of Semantic Resonance(CSR) 모듈을 사용합니다. 또한, 앵커 간의 직교성을 촉진하는 Dispersion Loss를 도입하여 다양한 전문화를 유도합니다. WikiText-103 실험 결과, SRA는 검증 퍼플렉시티 13.41을 기록하며, 밀집 및 표준 MoE 모델보다 우수한 성능을 보였습니다. 특히, SRA는 전문가 활용도에서 뛰어난 성과를 보이며, 명확하고 일관된 전문화 패턴을 형성합니다. 이 연구는 언어 모델의 투명성과 제어 가능성을 높이는 데 있어 의미 기반 라우팅의 잠재력을 입증합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 해석 가능성을 높이기 위해 SRA(Semantic Resonance Architecture)를 도입하여 토큰 라우팅을 코사인 유사도 기반으로 수행합니다.

- 2. SRA는 학습된 게이팅 대신 CSR(Chamber of Semantic Resonance) 모듈을 사용하여 해석 가능한 라우팅 결정을 보장합니다.

- 3. 새로운 디스퍼션 손실(Dispersion Loss)을 도입하여 앵커 간의 직교성을 촉진하고 다양한 전문화를 강화합니다.

- 4. WikiText-103 실험에서 SRA는 검증 퍼플렉시티 13.41을 달성하여 밀집 베이스라인(14.13)과 표준 MoE 베이스라인(13.53)을 능가합니다.

- 5. SRA는 전문가 활용도에서 우수한 성능을 보이며, 표준 MoE와 달리 명확하고 의미론적으로 일관된 전문화 패턴을 개발합니다.

---

*Generated on 2025-09-19 14:50:43*