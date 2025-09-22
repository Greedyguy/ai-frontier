# SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data

**Korean Title:** SyGra: 합성 데이터의 확장 가능한 생성, 품질 태깅 및 관리에 대한 통합 그래프 기반 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Supervised Fine Tuning, Direct Preference Optimization

## 🔗 유사한 논문
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (85.6% similar)
- [[2025-09-17/Synthetic Data Generation for Screen Time and App Usage_20250917|Synthetic Data Generation for Screen Time and App Usage]] (83.9% similar)
- [[2025-09-22/LiteLong_ Resource-Efficient Long-Context Data Synthesis for LLMs_20250922|LiteLong Resource-Efficient Long-Context Data Synthesis for LLMs]] (83.1% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (82.6% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (82.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15432v2 Announce Type: replace 
Abstract: The advancement of large language models (LLMs) is critically dependent on the availability of high-quality datasets for Supervised Fine-Tuning (SFT), alignment tasks like Direct Preference Optimization (DPO), etc. In this work, we present a comprehensive synthetic data generation framework that facilitates scalable, configurable, and high-fidelity generation of synthetic data tailored for these training paradigms. Our approach employs a modular and configuration-based pipeline capable of modeling complex dialogue flows with minimal manual intervention. This framework uses a dual-stage quality tagging mechanism, combining heuristic rules and LLM-based evaluations, to automatically filter and score data extracted from OASST-formatted conversations, ensuring the curation of high-quality dialogue samples. The resulting datasets are structured under a flexible schema supporting both SFT and DPO use cases, enabling seamless integration into diverse training workflows. Together, these innovations offer a robust solution for generating and managing synthetic conversational data at scale, significantly reducing the overhead of data preparation in LLM training pipelines.

## 🔍 Abstract (한글 번역)

arXiv:2508.15432v2 발표 유형: 교체  
초록: 대형 언어 모델(LLM)의 발전은 감독된 미세 조정(SFT), 직접 선호 최적화(DPO)와 같은 정렬 작업을 위한 고품질 데이터셋의 가용성에 크게 의존합니다. 본 연구에서는 이러한 훈련 패러다임에 맞춘 합성 데이터를 확장 가능하고 구성 가능하며 고충실도로 생성할 수 있는 포괄적인 합성 데이터 생성 프레임워크를 제시합니다. 우리의 접근 방식은 최소한의 수작업 개입으로 복잡한 대화 흐름을 모델링할 수 있는 모듈식 및 구성 기반 파이프라인을 사용합니다. 이 프레임워크는 휴리스틱 규칙과 LLM 기반 평가를 결합한 이중 단계 품질 태그 메커니즘을 사용하여 OASST 형식의 대화에서 추출한 데이터를 자동으로 필터링하고 점수를 매겨 고품질 대화 샘플을 선별합니다. 결과 데이터셋은 SFT와 DPO 사용 사례 모두를 지원하는 유연한 스키마로 구조화되어 다양한 훈련 워크플로에 원활하게 통합될 수 있습니다. 이러한 혁신들은 대규모 합성 대화 데이터를 생성하고 관리하는 강력한 솔루션을 제공하여 LLM 훈련 파이프라인의 데이터 준비에 대한 부담을 크게 줄여줍니다.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 발전을 위한 고품질 데이터셋 생성 프레임워크를 제안합니다. 이 프레임워크는 대화 흐름을 모델링하는 모듈형 파이프라인을 통해 최소한의 수작업으로 대규모 합성 데이터를 생성합니다. 또한, 이중 단계의 품질 태깅 메커니즘을 사용하여 대화 데이터를 자동으로 필터링하고 평가합니다. 생성된 데이터셋은 SFT와 DPO에 모두 활용 가능하며, 다양한 훈련 워크플로우에 쉽게 통합될 수 있습니다. 이로써 LLM 훈련에서 데이터 준비의 부담을 크게 줄입니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)의 발전은 고품질 데이터셋의 가용성에 크게 의존하며, 이를 위한 종합적인 합성 데이터 생성 프레임워크를 제시합니다.

- 2. 이 프레임워크는 최소한의 수작업 개입으로 복잡한 대화 흐름을 모델링할 수 있는 모듈식 및 구성 기반 파이프라인을 사용합니다.

- 3. 이중 단계 품질 태그 메커니즘을 통해 OASST 형식의 대화에서 추출된 데이터를 자동으로 필터링하고 평가하여 고품질 대화 샘플을 선별합니다.

- 4. 생성된 데이터셋은 SFT 및 DPO 사용 사례를 지원하는 유연한 스키마로 구조화되어 다양한 훈련 워크플로우에 원활하게 통합될 수 있습니다.

- 5. 이 혁신은 대규모 합성 대화 데이터를 생성 및 관리하는 강력한 솔루션을 제공하여 LLM 훈련 파이프라인의 데이터 준비 부담을 크게 줄입니다.

---

*Generated on 2025-09-22 14:33:09*