# ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models

**Korean Title:** ORCA: 시각-언어 모델에서 환각 및 적대적 견고성을 위한 에이전트적 추론

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Agentic Reasoning

## 🔗 유사한 논문
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (83.4% similar)
- [[2025-09-17/MOCHA_ Multi-modal Objects-aware Cross-arcHitecture Alignment_20250917|MOCHA Multi-modal Objects-aware Cross-arcHitecture Alignment]] (83.2% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (82.6% similar)
- [[2025-09-18/VisMoDAl_ Visual Analytics for Evaluating and Improving Corruption Robustness of Vision-Language Models_20250918|VisMoDAl Visual Analytics for Evaluating and Improving Corruption Robustness of Vision-Language Models]] (82.1% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (82.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15435v1 Announce Type: cross 
Abstract: Large Vision-Language Models (LVLMs) exhibit strong multimodal capabilities but remain vulnerable to hallucinations from intrinsic errors and adversarial attacks from external exploitations, limiting their reliability in real-world applications. We present ORCA, an agentic reasoning framework that improves the factual accuracy and adversarial robustness of pretrained LVLMs through test-time structured inference reasoning with a suite of small vision models (less than 3B parameters). ORCA operates via an Observe--Reason--Critique--Act loop, querying multiple visual tools with evidential questions, validating cross-model inconsistencies, and refining predictions iteratively without access to model internals or retraining. ORCA also stores intermediate reasoning traces, which supports auditable decision-making. Though designed primarily to mitigate object-level hallucinations, ORCA also exhibits emergent adversarial robustness without requiring adversarial training or defense mechanisms. We evaluate ORCA across three settings: (1) clean images on hallucination benchmarks, (2) adversarially perturbed images without defense, and (3) adversarially perturbed images with defense applied. On the POPE hallucination benchmark, ORCA improves standalone LVLM performance by +3.64\% to +40.67\% across different subsets. Under adversarial perturbations on POPE, ORCA achieves an average accuracy gain of +20.11\% across LVLMs. When combined with defense techniques on adversarially perturbed AMBER images, ORCA further improves standalone LVLM performance, with gains ranging from +1.20\% to +48.00\% across evaluation metrics. These results demonstrate that ORCA offers a promising path toward building more reliable and robust multimodal systems.

## 🔍 Abstract (한글 번역)

arXiv:2509.15435v1 발표 유형: 교차  
초록: 대형 비전-언어 모델(LVLMs)은 강력한 다중 모드 기능을 보이지만, 내재적 오류로 인한 환각과 외부 악용으로 인한 적대적 공격에 취약하여 실제 응용에서의 신뢰성을 제한합니다. 우리는 사전 훈련된 LVLMs의 사실적 정확성과 적대적 견고성을 개선하기 위해 테스트 시 구조화된 추론을 통해 소형 비전 모델(3B 매개변수 미만) 모음과 함께 작동하는 ORCA라는 에이전트 추론 프레임워크를 제시합니다. ORCA는 관찰-추론-비판-행동 루프를 통해 여러 시각 도구에 증거 기반 질문을 하여 모델 간 불일치를 검증하고, 모델 내부 접근이나 재훈련 없이 예측을 반복적으로 수정합니다. ORCA는 또한 감사 가능한 의사결정을 지원하는 중간 추론 흔적을 저장합니다. 주로 객체 수준의 환각을 완화하도록 설계되었지만, ORCA는 적대적 훈련이나 방어 메커니즘 없이도 발생하는 적대적 견고성을 보여줍니다. 우리는 ORCA를 세 가지 설정에서 평가합니다: (1) 환각 벤치마크에서의 깨끗한 이미지, (2) 방어 없이 적대적으로 변형된 이미지, (3) 방어가 적용된 적대적으로 변형된 이미지. POPE 환각 벤치마크에서 ORCA는 다양한 하위 집합에서 독립형 LVLM 성능을 +3.64%에서 +40.67%까지 향상시킵니다. POPE에서의 적대적 변형 하에서, ORCA는 LVLMs 전반에 걸쳐 평균 정확도 증가 +20.11%를 달성합니다. 적대적으로 변형된 AMBER 이미지에 방어 기술을 결합할 때, ORCA는 평가 지표 전반에 걸쳐 +1.20%에서 +48.00%까지 독립형 LVLM 성능을 더욱 향상시킵니다. 이러한 결과는 ORCA가 보다 신뢰할 수 있고 견고한 다중 모드 시스템을 구축하는 유망한 경로를 제공함을 보여줍니다.

## 📝 요약

대형 비전-언어 모델(LVLM)은 강력한 멀티모달 기능을 가지고 있지만, 내재적 오류와 외부 공격에 취약하여 실제 응용에서의 신뢰성이 제한됩니다. 본 논문에서는 ORCA라는 에이전트적 추론 프레임워크를 제안하여, 사전 학습된 LVLM의 사실 정확성과 적대적 견고성을 개선합니다. ORCA는 작은 비전 모델들을 활용하여 테스트 시 구조화된 추론을 수행하며, 모델 내부 접근이나 재학습 없이 예측을 개선합니다. 주로 객체 수준 환각을 줄이기 위해 설계된 ORCA는 적대적 훈련 없이도 견고성을 보여줍니다. POPE 환각 벤치마크에서 ORCA는 LVLM 성능을 최대 40.67% 향상시켰으며, 적대적 이미지에서도 평균 20.11%의 정확도 증가를 달성했습니다. 이러한 결과는 ORCA가 더 신뢰할 수 있는 멀티모달 시스템 구축에 기여할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. ORCA는 사전 학습된 대형 비전-언어 모델(LVLM)의 사실적 정확성과 적대적 강인성을 개선하는 에이전트 기반 추론 프레임워크입니다.

- 2. ORCA는 Observe--Reason--Critique--Act 루프를 통해 여러 시각 도구를 활용하여 증거 기반 질문을 하고, 모델 간 불일치를 검증하며, 예측을 반복적으로 개선합니다.

- 3. ORCA는 객체 수준 환각을 줄이기 위해 설계되었지만, 적대적 훈련이나 방어 메커니즘 없이도 적대적 강인성을 나타냅니다.

- 4. POPE 환각 벤치마크에서 ORCA는 독립형 LVLM 성능을 +3.64%에서 +40.67%까지 향상시켰습니다.

- 5. 적대적 방어 기법과 결합하여 AMBER 이미지에서 ORCA는 독립형 LVLM 성능을 +1.20%에서 +48.00%까지 추가로 향상시켰습니다.

---

*Generated on 2025-09-22 13:55:37*