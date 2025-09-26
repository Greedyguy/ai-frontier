---
keywords:
  - EigenTrack
  - Large Language Model
  - Vision-Language Model
  - Spectral Geometry
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15735
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:32:45.985961",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "EigenTrack",
    "Large Language Model",
    "Vision-Language Model",
    "Spectral Geometry"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "EigenTrack": 0.85,
    "Large Language Model": 0.8,
    "Vision-Language Model": 0.78,
    "Spectral Geometry": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "EigenTrack",
        "canonical": "EigenTrack",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "EigenTrack is a novel method introduced in the paper, crucial for understanding its contribution to hallucination and OOD detection.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's focus on hallucination and OOD detection, providing a broad technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are critical for understanding the multimodal aspects of the paper's detection approach.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Spectral Geometry",
        "canonical": "Spectral Geometry",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Spectral Geometry is a unique concept used in the paper to analyze model dynamics, crucial for the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "EigenTrack",
      "resolved_canonical": "EigenTrack",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Spectral Geometry",
      "resolved_canonical": "Spectral Geometry",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# EigenTrack: Spectral Activation Feature Tracking for Hallucination and Out-of-Distribution Detection in LLMs and VLMs

**Korean Title:** EigenTrack: 환각 및 분포 외 탐지를 위한 스펙트럼 활성화 특징 추적 기법 - 대형 언어 모델(LLM) 및 비전 언어 모델(VLM)에서의 적용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15735.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15735](https://arxiv.org/abs/2509.15735)

## 🔗 유사한 논문
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (80.9% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (80.1% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (79.5% similar)
- [[2025-09-18/LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking: An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (79.4% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/EigenTrack|EigenTrack]], [[keywords/Spectral Geometry|Spectral Geometry]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15735v1 Announce Type: new 
Abstract: Large language models (LLMs) offer broad utility but remain prone to hallucination and out-of-distribution (OOD) errors. We propose EigenTrack, an interpretable real-time detector that uses the spectral geometry of hidden activations, a compact global signature of model dynamics. By streaming covariance-spectrum statistics such as entropy, eigenvalue gaps, and KL divergence from random baselines into a lightweight recurrent classifier, EigenTrack tracks temporal shifts in representation structure that signal hallucination and OOD drift before surface errors appear. Unlike black- and grey-box methods, it needs only a single forward pass without resampling. Unlike existing white-box detectors, it preserves temporal context, aggregates global signals, and offers interpretable accuracy-latency trade-offs.

## 🔍 Abstract (한글 번역)

arXiv:2509.15735v1 발표 유형: 신규  
초록: 대형 언어 모델(LLM)은 광범위한 유용성을 제공하지만, 여전히 환각과 분포 외(OOD) 오류에 취약합니다. 우리는 숨겨진 활성화의 스펙트럼 기하학, 즉 모델 동작의 압축된 전역 서명을 사용하는 해석 가능한 실시간 탐지기인 EigenTrack을 제안합니다. 엔트로피, 고유값 간격, 무작위 기준선으로부터의 KL 발산과 같은 공분산 스펙트럼 통계를 경량의 순환 분류기로 스트리밍함으로써, EigenTrack은 표면 오류가 나타나기 전에 환각과 OOD 드리프트를 신호하는 표현 구조의 시간적 변화를 추적합니다. 블랙박스 및 그레이박스 방법과 달리, 재샘플링 없이 단일 순방향 패스만 필요합니다. 기존의 화이트박스 탐지기와 달리, 시간적 맥락을 보존하고, 전역 신호를 집계하며, 해석 가능한 정확도-지연 트레이드오프를 제공합니다.

## 📝 요약

EigenTrack는 대형 언어 모델(LLM)의 환각 및 분포 외 오류를 실시간으로 탐지하는 해석 가능한 도구입니다. 이 방법은 숨겨진 활성화의 스펙트럼 기하학을 활용하여 모델 동작의 전역 서명을 생성합니다. EigenTrack은 엔트로피, 고유값 간격, KL 발산 등의 통계 정보를 경량 재귀 분류기에 스트리밍하여, 표면 오류가 나타나기 전에 환각과 분포 외 변화를 감지합니다. 이 방법은 단일 전방 패스만 필요로 하며, 기존의 탐지기와 달리 시간적 맥락을 보존하고 전역 신호를 집계하여 해석 가능한 정확도-지연 트레이드오프를 제공합니다.

## 🎯 주요 포인트

- 1. EigenTrack는 대형 언어 모델(LLM)의 환각 및 분포 외 오류를 감지하기 위한 실시간 해석 가능한 탐지기입니다.
- 2. 이 탐지기는 숨겨진 활성화의 스펙트럼 기하학을 사용하여 모델 동작의 전역 서명을 분석합니다.
- 3. EigenTrack은 엔트로피, 고유값 간격, KL 발산 등의 공분산-스펙트럼 통계를 경량의 순환 분류기에 스트리밍하여 환각 및 OOD 드리프트를 조기에 감지합니다.
- 4. 기존의 블랙박스 및 그레이박스 방법과 달리, EigenTrack은 단일 전방 패스만 필요로 하며 재샘플링이 필요 없습니다.
- 5. EigenTrack은 시간적 맥락을 보존하고 전역 신호를 집계하며 해석 가능한 정확도-지연 시간의 균형을 제공합니다.


---

*Generated on 2025-09-23 10:32:45*