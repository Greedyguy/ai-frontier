
# Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning

**Korean Title:** 미도: 폐루프 학습을 통한 향상된 대형 언어 모델(LLM) 미세 조정을 위한 모델 정보 기반 동적 데이터 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Data Optimization

## 🔗 유사한 논문
- [[Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (86.7% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (85.1% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (85.1% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (84.9% similar)
- [[MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (84.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.21589v2 Announce Type: replace-cross 
Abstract: Supervised Fine-Tuning (SFT) Large Language Models (LLM) fundamentally rely on high-quality training data. While data selection and data synthesis are two common strategies to improve data quality, existing approaches often face limitations in static dataset curation that fail to adapt to evolving model capabilities. In this paper, we introduce Middo, a self-evolving Model-informed dynamic data optimization framework that uses model-aware data selection and context-preserving data refinement. Unlike conventional one-off filtering/synthesis methods, our framework establishes a closed-loop optimization system: (1) A self-referential diagnostic module proactively identifies suboptimal samples through tri-axial model signals - loss patterns (complexity), embedding cluster dynamics (diversity), and self-alignment scores (quality); (2) An adaptive optimization engine then transforms suboptimal samples into pedagogically valuable training points while preserving semantic integrity; (3) This optimization process continuously evolves with model capability through dynamic learning principles. Experiments on multiple benchmarks demonstrate that our Middo consistently enhances the quality of seed data and boosts LLM's performance with improving accuracy by 7.15% on average while maintaining the original dataset scale. This work establishes a new paradigm for sustainable LLM training through dynamic human-AI co-evolution of data and models. Our datasets, models, and code are coming soon. Our datasets, models, and code are publicly available at https://github.com/Word2VecT/Middo

## 🔍 Abstract (한글 번역)

arXiv:2508.21589v2 발표 유형: 교차 교체  
초록: 지도 학습 미세 조정(SFT) 대형 언어 모델(LLM)은 본질적으로 고품질의 훈련 데이터에 의존합니다. 데이터 선택과 데이터 합성은 데이터 품질을 향상시키기 위한 두 가지 일반적인 전략이지만, 기존 접근법은 진화하는 모델 능력에 적응하지 못하는 정적 데이터셋 큐레이션의 한계에 직면하곤 합니다. 본 논문에서는 모델 인식 데이터 선택과 문맥 보존 데이터 정제를 사용하는 자가 진화 모델 정보 기반 동적 데이터 최적화 프레임워크인 Middo를 소개합니다. 기존의 일회성 필터링/합성 방법과 달리, 우리의 프레임워크는 폐쇄 루프 최적화 시스템을 구축합니다: (1) 자기 참조 진단 모듈은 손실 패턴(복잡성), 임베딩 클러스터 동역학(다양성), 자기 정렬 점수(품질)라는 삼축 모델 신호를 통해 비최적 샘플을 능동적으로 식별합니다; (2) 적응형 최적화 엔진은 의미적 무결성을 유지하면서 비최적 샘플을 교육적으로 가치 있는 훈련 포인트로 변환합니다; (3) 이 최적화 과정은 동적 학습 원칙을 통해 모델 능력과 함께 지속적으로 진화합니다. 여러 벤치마크 실험에서 우리의 Middo는 시드 데이터의 품질을 지속적으로 향상시키고, 원래 데이터셋 규모를 유지하면서 평균 7.15%의 정확도 향상을 통해 LLM의 성능을 향상시킵니다. 이 연구는 데이터와 모델의 동적 인간-AI 공동 진화를 통한 지속 가능한 LLM 훈련의 새로운 패러다임을 확립합니다. 우리의 데이터셋, 모델 및 코드는 곧 공개될 예정입니다. 우리의 데이터셋, 모델 및 코드는 https://github.com/Word2VecT/Middo에서 공개적으로 이용 가능합니다.

## 📝 요약

이 논문에서는 대규모 언어 모델(LLM)의 지도 학습을 위한 데이터 품질 향상을 위해 Middo라는 동적 데이터 최적화 프레임워크를 제안합니다. Middo는 모델 인식 데이터 선택과 문맥 보존 데이터 정제를 통해 데이터 품질을 개선합니다. 기존의 정적 데이터 필터링/합성 방법과 달리, Middo는 폐쇄형 최적화 시스템을 구축하여 모델 신호를 통해 비효율적인 샘플을 식별하고, 이를 교육적으로 가치 있는 데이터로 변환합니다. 실험 결과, Middo는 데이터 품질을 향상시키고 모델의 정확도를 평균 7.15% 증가시켰습니다. 이 연구는 데이터와 모델의 동적 공동 진화를 통해 지속 가능한 LLM 학습의 새로운 패러다임을 제시합니다.

## 🎯 주요 포인트

- 1. Middo는 모델 인식 데이터 선택과 문맥 보존 데이터 정제를 활용하여 데이터 최적화를 수행하는 자가 진화 프레임워크입니다.

- 2. 기존의 일회성 필터링/합성 방법과 달리, Middo는 손실 패턴, 임베딩 클러스터 동태, 자기 정렬 점수를 활용한 삼축 모델 신호로 비최적 샘플을 식별합니다.

- 3. 적응형 최적화 엔진은 비최적 샘플을 교육적으로 가치 있는 훈련 데이터로 변환하며, 의미적 무결성을 유지합니다.

- 4. Middo는 모델의 능력에 따라 지속적으로 진화하며, 평균 7.15%의 정확도 향상을 달성합니다.

- 5. 이 연구는 동적 인간-AI 공동 진화를 통해 지속 가능한 LLM 훈련의 새로운 패러다임을 제시합니다.

---

*Generated on 2025-09-19 15:20:26*