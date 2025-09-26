---
keywords:
  - Source Separation
  - TISDiSS Framework
  - Dynamic Inference
  - Parameter Sharing
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15666
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:09:16.351099",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Source Separation",
    "TISDiSS Framework",
    "Dynamic Inference",
    "Parameter Sharing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Source Separation": 0.85,
    "TISDiSS Framework": 0.8,
    "Dynamic Inference": 0.78,
    "Parameter Sharing": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "source separation",
        "canonical": "Source Separation",
        "aliases": [
          "audio separation",
          "speech separation"
        ],
        "category": "specific_connectable",
        "rationale": "Source separation is a key task in audio processing, linking to various applications in speech and music.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "TISDiSS",
        "canonical": "TISDiSS Framework",
        "aliases": [
          "Training-Time and Inference-Time Scalable Discriminative Source Separation"
        ],
        "category": "unique_technical",
        "rationale": "TISDiSS is a novel framework introduced in the paper, offering a scalable solution for source separation.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "dynamic inference repetitions",
        "canonical": "Dynamic Inference",
        "aliases": [
          "adaptive inference",
          "scalable inference"
        ],
        "category": "evolved_concepts",
        "rationale": "Dynamic inference is an evolving concept that allows flexible performance adjustments, relevant to adaptive systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.78
      },
      {
        "surface": "shared-parameter design",
        "canonical": "Parameter Sharing",
        "aliases": [
          "shared parameters",
          "parameter reuse"
        ],
        "category": "specific_connectable",
        "rationale": "Parameter sharing is a technique that enhances model efficiency, relevant to network design discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "training",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "source separation",
      "resolved_canonical": "Source Separation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "TISDiSS",
      "resolved_canonical": "TISDiSS Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "dynamic inference repetitions",
      "resolved_canonical": "Dynamic Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "shared-parameter design",
      "resolved_canonical": "Parameter Sharing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# TISDiSS: A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation

**Korean Title:** TISDiSS: 판별적 소스 분리를 위한 학습 시 및 추론 시 확장 가능한 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15666.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15666](https://arxiv.org/abs/2509.15666)

## 🔗 유사한 논문
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (81.8% similar)
- [[2025-09-19/Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (81.6% similar)
- [[2025-09-22/SETrLUSI_ Stochastic Ensemble Multi-Source Transfer Learning Using Statistical Invariant_20250922|SETrLUSI: Stochastic Ensemble Multi-Source Transfer Learning Using Statistical Invariant]] (80.5% similar)
- [[2025-09-22/Time-adaptive SympNets for separable Hamiltonian systems_20250922|Time-adaptive SympNets for separable Hamiltonian systems]] (78.9% similar)
- [[2025-09-17/Slim-SC_ Thought Pruning for Efficient Scaling with Self-Consistency_20250917|Slim-SC: Thought Pruning for Efficient Scaling with Self-Consistency]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Source Separation|Source Separation]], [[keywords/Parameter Sharing|Parameter Sharing]]
**⚡ Unique Technical**: [[keywords/TISDiSS Framework|TISDiSS Framework]]
**🚀 Evolved Concepts**: [[keywords/Dynamic Inference|Dynamic Inference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15666v1 Announce Type: cross 
Abstract: Source separation is a fundamental task in speech, music, and audio processing, and it also provides cleaner and larger data for training generative models. However, improving separation performance in practice often depends on increasingly large networks, inflating training and deployment costs. Motivated by recent advances in inference-time scaling for generative modeling, we propose Training-Time and Inference-Time Scalable Discriminative Source Separation (TISDiSS), a unified framework that integrates early-split multi-loss supervision, shared-parameter design, and dynamic inference repetitions. TISDiSS enables flexible speed-performance trade-offs by adjusting inference depth without retraining additional models. We further provide systematic analyses of architectural and training choices and show that training with more inference repetitions improves shallow-inference performance, benefiting low-latency applications. Experiments on standard speech separation benchmarks demonstrate state-of-the-art performance with a reduced parameter count, establishing TISDiSS as a scalable and practical framework for adaptive source separation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15666v1 발표 유형: 교차  
초록: 소스 분리는 음성, 음악 및 오디오 처리에서 기본적인 작업이며, 생성 모델을 훈련하기 위한 더 깨끗하고 큰 데이터를 제공합니다. 그러나 실제로 분리 성능을 향상시키는 것은 종종 점점 더 큰 네트워크에 의존하게 되어 훈련 및 배포 비용이 증가합니다. 생성 모델링을 위한 추론 시간 확장의 최근 발전에 영감을 받아, 우리는 훈련 시간 및 추론 시간 확장 가능한 판별 소스 분리(TISDiSS)를 제안합니다. 이는 초기 분할 다중 손실 감독, 공유 매개변수 설계 및 동적 추론 반복을 통합하는 통합 프레임워크입니다. TISDiSS는 추가 모델을 재훈련하지 않고도 추론 깊이를 조정하여 유연한 속도-성능 절충을 가능하게 합니다. 우리는 또한 구조적 및 훈련 선택에 대한 체계적인 분석을 제공하고, 더 많은 추론 반복으로 훈련할 때 얕은 추론 성능이 향상되어 저지연 응용 프로그램에 이점을 제공함을 보여줍니다. 표준 음성 분리 벤치마크에 대한 실험은 매개변수 수를 줄이면서 최첨단 성능을 입증하여 TISDiSS를 적응형 소스 분리를 위한 확장 가능하고 실용적인 프레임워크로 확립합니다.

## 📝 요약

이 논문은 음성 및 음악 처리에서의 소스 분리를 개선하기 위한 TISDiSS라는 새로운 프레임워크를 제안합니다. TISDiSS는 훈련 및 추론 시 확장 가능한 구조로, 초기 분할 다중 손실 감독, 파라미터 공유 설계, 동적 추론 반복을 통합합니다. 이를 통해 추가 모델 재훈련 없이 추론 깊이를 조절하여 속도와 성능 간의 유연한 균형을 제공합니다. 실험 결과, TISDiSS는 적은 파라미터로도 최신 성능을 달성하며, 낮은 대기 시간 응용에 유리한 얕은 추론 성능을 향상시킵니다.

## 🎯 주요 포인트

- 1. TISDiSS는 훈련 및 추론 시 확장 가능한 차별적 소스 분리를 위한 통합 프레임워크로, 초기 분할 다중 손실 감독, 공유 매개변수 설계, 동적 추론 반복을 통합합니다.
- 2. TISDiSS는 추가 모델 재훈련 없이 추론 깊이를 조정하여 유연한 속도-성능 절충을 가능하게 합니다.
- 3. 더 많은 추론 반복을 통한 훈련은 얕은 추론 성능을 개선하여 저지연 응용 프로그램에 이점을 제공합니다.
- 4. 표준 음성 분리 벤치마크 실험에서 TISDiSS는 매개변수 수를 줄이면서도 최첨단 성능을 입증했습니다.
- 5. TISDiSS는 적응형 소스 분리를 위한 확장 가능하고 실용적인 프레임워크로 자리 잡았습니다.


---

*Generated on 2025-09-23 09:09:16*