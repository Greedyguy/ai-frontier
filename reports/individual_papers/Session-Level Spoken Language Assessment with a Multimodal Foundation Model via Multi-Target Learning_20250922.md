# Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning

**Korean Title:** 다중 목표 학습을 통한 다중 모달 기초 모델을 활용한 세션 수준 구어 언어 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Session-Level Evaluation

## 🔗 유사한 논문
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (84.2% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (83.9% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (82.4% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025 Towards Uncertainty Aware Arabic Readability Assessment]] (82.4% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (82.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16025v1 Announce Type: cross 
Abstract: Spoken Language Assessment (SLA) estimates a learner's oral proficiency from spontaneous speech. The growing population of L2 English speakers has intensified the demand for reliable SLA, a critical component of Computer Assisted Language Learning (CALL). Existing efforts often rely on cascaded pipelines, which are prone to error propagation, or end-to-end models that often operate on a short audio window, which might miss discourse-level evidence. This paper introduces a novel multimodal foundation model approach that performs session-level evaluation in a single pass. Our approach couples multi-target learning with a frozen, Whisper ASR model-based speech prior for acoustic-aware calibration, allowing for jointly learning holistic and trait-level objectives of SLA without resorting to handcrafted features. By coherently processing the entire response session of an L2 speaker, the model excels at predicting holistic oral proficiency. Experiments conducted on the Speak & Improve benchmark demonstrate that our proposed approach outperforms the previous state-of-the-art cascaded system and exhibits robust cross-part generalization, producing a compact deployable grader that is tailored for CALL applications.

## 🔍 Abstract (한글 번역)

arXiv:2509.16025v1 발표 유형: 교차  
초록: 구어 평가(SLA)는 학습자의 자발적 발화를 통해 구술 능력을 평가합니다. L2 영어 사용자의 증가로 인해 신뢰할 수 있는 SLA에 대한 수요가 증가했으며, 이는 컴퓨터 보조 언어 학습(CALL)의 중요한 구성 요소입니다. 기존의 노력은 종종 오류 전파에 취약한 단계적 파이프라인이나 담화 수준의 증거를 놓칠 수 있는 짧은 오디오 창에서 작동하는 종단 간 모델에 의존합니다. 본 논문은 세션 수준 평가를 단일 패스로 수행하는 새로운 다중 모드 기초 모델 접근 방식을 소개합니다. 우리의 접근 방식은 다중 목표 학습을 고정된 Whisper ASR 모델 기반의 음성 사전과 결합하여 음향 인식 보정을 수행하며, 수작업으로 만든 특징을 사용하지 않고도 SLA의 전체적 및 특성 수준 목표를 공동으로 학습할 수 있게 합니다. L2 화자의 전체 응답 세션을 일관되게 처리함으로써, 모델은 전체적인 구술 능력을 예측하는 데 뛰어납니다. Speak & Improve 벤치마크에서 수행된 실험은 제안된 접근 방식이 이전 최첨단 단계적 시스템을 능가하며, CALL 응용 프로그램에 맞춰진 컴팩트한 배포 가능한 채점기를 생성하면서 강력한 교차 부분 일반화를 보여준다는 것을 입증합니다.

## 📝 요약

이 논문은 자발적 발화를 통해 학습자의 구어 능력을 평가하는 구어 언어 평가(SLA)를 다룹니다. 기존의 방법론은 오류 전파가 쉬운 연속 파이프라인이나 담화 수준의 증거를 놓칠 수 있는 단일 오디오 창 기반의 종단 간 모델에 의존합니다. 본 연구는 세션 수준 평가를 단일 패스로 수행하는 새로운 다중 모달 기초 모델 접근법을 제안합니다. 이 접근법은 Whisper ASR 모델 기반의 음향 인식 보정을 위한 음성 사전과 다중 목표 학습을 결합하여, 수작업 특징 없이도 SLA의 전체적 및 특성 수준 목표를 공동 학습합니다. 전체 응답 세션을 일관되게 처리하여 총체적인 구어 능력을 예측하는 데 뛰어나며, Speak & Improve 벤치마크 실험에서 기존 최첨단 시스템을 능가하고 CALL 애플리케이션에 적합한 컴팩트한 평가기를 제공합니다.

## 🎯 주요 포인트

- 1. 본 논문은 자발적 발화를 통해 학습자의 구어 능력을 평가하는 새로운 다중 모달 기반 모델을 제안합니다.

- 2. 제안된 모델은 Whisper ASR 모델 기반의 음향 인식 보정과 다중 목표 학습을 결합하여, 수작업 특징 없이도 전체적 및 특성 수준의 구어 능력을 공동 학습합니다.

- 3. 전체 응답 세션을 일관되게 처리함으로써, 모델은 학습자의 전체적인 구어 능력을 예측하는 데 뛰어난 성능을 보입니다.

- 4. Speak & Improve 벤치마크 실험에서 제안된 접근법은 이전 최첨단 계단식 시스템을 능가하며, CALL 응용 프로그램에 적합한 컴팩트한 평가기를 제공합니다.

- 5. 본 연구는 강력한 교차 부분 일반화를 통해 CALL 응용 프로그램에 적합한 평가기를 개발하였습니다.

---

*Generated on 2025-09-22 14:22:42*