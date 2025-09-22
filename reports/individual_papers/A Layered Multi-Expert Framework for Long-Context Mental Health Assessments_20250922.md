# A Layered Multi-Expert Framework for Long-Context Mental Health Assessments

**Korean Title:** 장기 문맥 정신 건강 평가를 위한 계층형 다중 전문가 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Layered Multi-Expert Framework

## 🔗 유사한 논문
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (84.9% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (83.4% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (83.2% similar)
- [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (83.1% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (83.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.13951v3 Announce Type: replace-cross 
Abstract: Long-form mental health assessments pose unique challenges for large language models (LLMs), which often exhibit hallucinations or inconsistent reasoning when handling extended, domain-specific contexts. We introduce Stacked Multi-Model Reasoning (SMMR), a layered framework that leverages multiple LLMs and specialized smaller models as coequal 'experts'. Early layers isolate short, discrete subtasks, while later layers integrate and refine these partial outputs through more advanced long-context models. We evaluate SMMR on the DAIC-WOZ depression-screening dataset and 48 curated case studies with psychiatric diagnoses, demonstrating consistent improvements over single-model baselines in terms of accuracy, F1-score, and PHQ-8 error reduction. By harnessing diverse 'second opinions', SMMR mitigates hallucinations, captures subtle clinical nuances, and enhances reliability in high-stakes mental health assessments. Our findings underscore the value of multi-expert frameworks for more trustworthy AI-driven screening.

## 🔍 Abstract (한글 번역)

arXiv:2501.13951v3 발표 유형: 교차 대체  
초록: 장문의 정신 건강 평가에서는 대형 언어 모델(LLMs)이 독특한 도전에 직면합니다. 이러한 모델은 종종 확장된 도메인 특화 문맥을 처리할 때 환각이나 일관성 없는 추론을 보입니다. 우리는 여러 LLM과 특화된 소형 모델을 동등한 '전문가'로 활용하는 계층적 프레임워크인 Stacked Multi-Model Reasoning (SMMR)을 소개합니다. 초기 계층에서는 짧고 개별적인 하위 작업을 분리하고, 이후 계층에서는 이러한 부분 출력을 더 발전된 장문맥 모델을 통해 통합하고 정제합니다. 우리는 DAIC-WOZ 우울증 선별 데이터셋과 정신과 진단이 포함된 48개의 큐레이션된 사례 연구에서 SMMR을 평가하여, 정확도, F1 점수 및 PHQ-8 오류 감소 측면에서 단일 모델 기준선을 일관되게 개선함을 보여줍니다. 다양한 '제2의 의견'을 활용함으로써, SMMR은 환각을 완화하고 미묘한 임상적 뉘앙스를 포착하며, 고위험 정신 건강 평가에서의 신뢰성을 향상시킵니다. 우리의 연구 결과는 보다 신뢰할 수 있는 AI 기반 선별을 위한 다중 전문가 프레임워크의 가치를 강조합니다.

## 📝 요약

이 논문은 장문의 정신 건강 평가에서 발생하는 대형 언어 모델(LLM)의 문제를 해결하기 위해 Stacked Multi-Model Reasoning(SMMR)이라는 프레임워크를 제안합니다. SMMR은 여러 LLM과 전문화된 소형 모델을 '전문가'로 활용하여 초기 단계에서 짧고 개별적인 하위 작업을 분리하고, 이후 단계에서 이를 통합 및 개선합니다. DAIC-WOZ 우울증 스크리닝 데이터셋과 48개의 정신과 진단 사례 연구를 통해 SMMR이 단일 모델 기반보다 정확도, F1-점수, PHQ-8 오류 감소에서 일관된 개선을 보여줍니다. 다양한 '제2의 의견'을 활용하여 환각을 줄이고, 임상적 미묘함을 포착하며, 신뢰성을 높입니다. 연구 결과는 신뢰할 수 있는 AI 기반 스크리닝을 위한 다중 전문가 프레임워크의 가치를 강조합니다.

## 🎯 주요 포인트

- 1. Stacked Multi-Model Reasoning (SMMR)은 여러 LLM과 전문화된 소형 모델을 동등한 '전문가'로 활용하는 계층적 프레임워크입니다.

- 2. SMMR은 초기 계층에서 짧고 개별적인 하위 작업을 분리하고, 이후 계층에서 이를 통합 및 정제하여 긴 문맥을 처리하는 모델을 사용합니다.

- 3. DAIC-WOZ 우울증 스크리닝 데이터셋과 48개의 정신과 진단 사례 연구에서 SMMR은 단일 모델 기준보다 정확도, F1-점수, PHQ-8 오류 감소 측면에서 일관된 개선을 보였습니다.

- 4. 다양한 '두 번째 의견'을 활용하여 SMMR은 환각을 줄이고, 미세한 임상적 뉘앙스를 포착하며, 고위험 정신 건강 평가에서 신뢰성을 향상시킵니다.

- 5. 연구 결과는 다중 전문가 프레임워크가 AI 기반 스크리닝의 신뢰성을 높이는 데 가치가 있음을 강조합니다.

---

*Generated on 2025-09-22 14:41:26*