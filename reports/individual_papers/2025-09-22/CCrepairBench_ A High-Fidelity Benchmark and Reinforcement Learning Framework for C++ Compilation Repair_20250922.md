# CCrepairBench: A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair

**Korean Title:** CCrepairBench: C++ 컴파일 수정을 위한 고충실도 벤치마크 및 강화 학습 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: LLM-as-a-Judge

## 🔗 유사한 논문
- [[2025-09-18/KGCompass_ Knowledge Graph Enhanced Repository-Level Software Repair_20250918|KGCompass Knowledge Graph Enhanced Repository-Level Software Repair]] (82.5% similar)
- [[2025-09-19/RulER_ Automated Rule-Based Semantic Error Localization and Repair for Code Translation_20250919|RulER Automated Rule-Based Semantic Error Localization and Repair for Code Translation]] (82.0% similar)
- [[2025-09-18/Crash Report Enhancement with Large Language Models_ An Empirical Study_20250918|Crash Report Enhancement with Large Language Models An Empirical Study]] (80.9% similar)
- [[2025-09-19/Evolution of Kernels_ Automated RISC-V Kernel Optimization with Large Language Models_20250919|Evolution of Kernels Automated RISC-V Kernel Optimization with Large Language Models]] (80.8% similar)
- [[2025-09-19/Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (80.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15690v1 Announce Type: new 
Abstract: The automated repair of C++ compilation errors presents a significant challenge, the resolution of which is critical for developer productivity. Progress in this domain is constrained by two primary factors: the scarcity of large-scale, high-fidelity datasets and the limitations of conventional supervised methods, which often fail to generate semantically correct patches.This paper addresses these gaps by introducing a comprehensive framework with three core contributions. First, we present CCrepair, a novel, large-scale C++ compilation error dataset constructed through a sophisticated generate-and-verify pipeline. Second, we propose a Reinforcement Learning (RL) paradigm guided by a hybrid reward signal, shifting the focus from mere compilability to the semantic quality of the fix. Finally, we establish the robust, two-stage evaluation system providing this signal, centered on an LLM-as-a-Judge whose reliability has been rigorously validated against the collective judgments of a panel of human experts. This integrated approach aligns the training objective with generating high-quality, non-trivial patches that are both syntactically and semantically correct. The effectiveness of our approach was demonstrated experimentally. Our RL-trained Qwen2.5-1.5B-Instruct model achieved performance comparable to a Qwen2.5-14B-Instruct model, validating the efficiency of our training paradigm. Our work provides the research community with a valuable new dataset and a more effective paradigm for training and evaluating robust compilation repair models, paving the way for more practical and reliable automated programming assistants.

## 🔍 Abstract (한글 번역)

arXiv:2509.15690v1 발표 유형: 신규  
초록: C++ 컴파일 오류의 자동 수정을 위한 연구는 개발자의 생산성에 중요한 영향을 미치는 도전 과제입니다. 이 분야의 발전은 두 가지 주요 요인에 의해 제한됩니다: 대규모 고품질 데이터셋의 부족과 전통적인 지도 학습 방법의 한계로, 이는 종종 의미적으로 올바른 패치를 생성하는 데 실패합니다. 본 논문은 이러한 격차를 해결하기 위해 세 가지 핵심 기여를 포함한 포괄적인 프레임워크를 소개합니다. 첫째, 우리는 정교한 생성 및 검증 파이프라인을 통해 구축된 새로운 대규모 C++ 컴파일 오류 데이터셋인 CCrepair를 제시합니다. 둘째, 단순한 컴파일 가능성에서 벗어나 수정의 의미적 품질에 중점을 두는 하이브리드 보상 신호에 의해 안내되는 강화 학습(RL) 패러다임을 제안합니다. 마지막으로, 이 신호를 제공하는 강력한 2단계 평가 시스템을 구축하며, 이는 인간 전문가 패널의 집단적 판단에 대해 엄격하게 검증된 LLM-as-a-Judge를 중심으로 합니다. 이 통합 접근 방식은 교육 목표를 문법적으로나 의미적으로 올바른 고품질의 비평범한 패치를 생성하는 것과 일치시킵니다. 우리의 접근 방식의 효과는 실험적으로 입증되었습니다. RL로 훈련된 Qwen2.5-1.5B-Instruct 모델은 Qwen2.5-14B-Instruct 모델과 유사한 성능을 달성하여 우리의 훈련 패러다임의 효율성을 입증했습니다. 우리의 연구는 연구 커뮤니티에 귀중한 새로운 데이터셋과 강력한 컴파일 수리 모델을 훈련하고 평가하기 위한 보다 효과적인 패러다임을 제공하여 더 실용적이고 신뢰할 수 있는 자동 프로그래밍 보조 도구의 길을 열어줍니다.

## 📝 요약

이 논문은 C++ 컴파일 오류의 자동 수정을 위한 새로운 접근 방식을 제안합니다. 주요 기여는 다음과 같습니다. 첫째, C++ 컴파일 오류를 다루는 대규모 데이터셋인 CCrepair를 소개합니다. 둘째, 보상 신호를 통해 수정의 의미적 품질을 향상시키는 강화 학습(RL) 패러다임을 제안합니다. 셋째, 인간 전문가의 판단과 비교하여 검증된 LLM-as-a-Judge를 중심으로 한 평가 시스템을 구축합니다. 실험 결과, RL로 훈련된 모델이 기존의 대형 모델과 유사한 성능을 보이며, 제안된 접근 방식의 효율성을 입증했습니다. 이 연구는 데이터셋과 새로운 학습 및 평가 패러다임을 제공하여 자동화된 프로그래밍 도우미의 발전에 기여합니다.

## 🎯 주요 포인트

- 1. CCrepair라는 대규모 C++ 컴파일 오류 데이터셋을 생성하여 자동 수정을 위한 새로운 프레임워크를 제안합니다.

- 2. 보상 신호를 하이브리드 방식으로 제공하는 강화 학습(RL) 패러다임을 도입하여 수정의 의미적 품질을 강조합니다.

- 3. LLM-as-a-Judge를 중심으로 한 신뢰성 높은 평가 시스템을 구축하여 인간 전문가의 판단과 비교 검증하였습니다.

- 4. RL로 훈련된 Qwen2.5-1.5B-Instruct 모델이 Qwen2.5-14B-Instruct 모델과 유사한 성능을 보여, 효율적인 훈련 패러다임을 입증했습니다.

- 5. 본 연구는 연구 커뮤니티에 가치 있는 데이터셋과 견고한 컴파일 수리 모델을 위한 효과적인 훈련 및 평가 패러다임을 제공합니다.

---

*Generated on 2025-09-22 13:45:08*