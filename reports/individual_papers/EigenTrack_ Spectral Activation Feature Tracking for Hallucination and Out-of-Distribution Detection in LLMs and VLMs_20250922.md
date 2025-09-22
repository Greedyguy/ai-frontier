# EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs

**Korean Title:** EigenTrack: LLM 및 VLM에서 환각 및 분포 외 탐지를 위한 스펙트럼 활성화 특징 추적

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretable Real-time Detection

## 🔗 유사한 논문
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (80.9% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (80.1% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (79.5% similar)
- [[2025-09-18/LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (79.4% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15735v1 Announce Type: new 
Abstract: Large language models (LLMs) offer broad utility but remain prone to hallucination and out-of-distribution (OOD) errors. We propose EigenTrack, an interpretable real-time detector that uses the spectral geometry of hidden activations, a compact global signature of model dynamics. By streaming covariance-spectrum statistics such as entropy, eigenvalue gaps, and KL divergence from random baselines into a lightweight recurrent classifier, EigenTrack tracks temporal shifts in representation structure that signal hallucination and OOD drift before surface errors appear. Unlike black- and grey-box methods, it needs only a single forward pass without resampling. Unlike existing white-box detectors, it preserves temporal context, aggregates global signals, and offers interpretable accuracy-latency trade-offs.

## 🔍 Abstract (한글 번역)

arXiv:2509.15735v1 발표 유형: 신규  
초록: 대형 언어 모델(LLM)은 광범위한 유용성을 제공하지만, 여전히 환각 및 분포 외(OOD) 오류에 취약합니다. 우리는 숨겨진 활성화의 스펙트럼 기하학, 즉 모델 동역학의 압축된 전역 서명을 사용하는 해석 가능한 실시간 탐지기인 EigenTrack을 제안합니다. 엔트로피, 고유값 간격, 무작위 기준선으로부터의 KL 발산과 같은 공분산-스펙트럼 통계를 가벼운 순환 분류기에 스트리밍함으로써, EigenTrack은 표면 오류가 나타나기 전에 환각 및 OOD 드리프트를 신호하는 표현 구조의 시간적 변화를 추적합니다. 블랙박스 및 그레이박스 방법과 달리, 재샘플링 없이 단일 순방향 패스만 필요합니다. 기존의 화이트박스 탐지기와 달리, 시간적 맥락을 보존하고, 전역 신호를 집계하며, 해석 가능한 정확도-지연 트레이드오프를 제공합니다.

## 📝 요약

EigenTrack은 대형 언어 모델(LLM)의 환각 및 분포 외 오류를 실시간으로 탐지하는 해석 가능한 도구입니다. 이 방법은 모델의 숨겨진 활성화의 스펙트럼 기하학을 활용하여, 엔트로피, 고유값 차이, KL 발산과 같은 통계치를 경량의 순환 분류기에 스트리밍합니다. 이를 통해 표면 오류가 나타나기 전에 환각 및 분포 외 드리프트를 감지합니다. EigenTrack은 단일 전방 패스만 필요로 하며, 기존의 흑-회색 상자 방법과 달리 시간적 맥락을 보존하고 글로벌 신호를 집계하여 해석 가능한 정확도-지연 트레이드오프를 제공합니다.

## 🎯 주요 포인트

- 1. EigenTrack는 대형 언어 모델(LLMs)의 환각 및 분포 외 오류(OOD)를 실시간으로 탐지하는 해석 가능한 도구입니다.

- 2. 이 도구는 숨겨진 활성화의 스펙트럼 기하학을 사용하여 모델의 동적 특성을 압축된 글로벌 서명으로 추적합니다.

- 3. EigenTrack은 엔트로피, 고유값 간격, KL 발산 등의 공분산 스펙트럼 통계를 경량의 순환 분류기에 스트리밍하여 표면 오류가 나타나기 전에 환각 및 OOD 드리프트를 감지합니다.

- 4. 기존의 블랙박스 및 그레이박스 방법과 달리, 단일 전방 패스만으로도 작동하며 재샘플링이 필요하지 않습니다.

- 5. EigenTrack은 시간적 문맥을 보존하고 글로벌 신호를 집계하며, 해석 가능한 정확도-지연 시간의 균형을 제공합니다.

---

*Generated on 2025-09-22 15:22:19*