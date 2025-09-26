<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:16:25.215656",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Memory Mechanism",
    "Long-term Point Tracking",
    "Synthetic Training Strategies"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Memory Mechanism": 0.82,
    "Long-term Point Tracking": 0.78,
    "Synthetic Training Strategies": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based model",
        "canonical": "Transformer",
        "aliases": [
          "Transformer architecture"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the model's architecture and are a key concept in machine learning, facilitating connections with other works using similar architectures.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Memory mechanism",
        "canonical": "Memory Mechanism",
        "aliases": [
          "Memory module",
          "Memory system"
        ],
        "category": "specific_connectable",
        "rationale": "The memory mechanism is crucial for maintaining temporal coherence, making it a significant point of connection for research on stateful models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Long-term point tracking",
        "canonical": "Long-term Point Tracking",
        "aliases": [
          "Point tracking over time"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that distinguishes the paper's focus, offering unique insights into tracking methodologies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Synthetic training strategies",
        "canonical": "Synthetic Training Strategies",
        "aliases": [
          "Synthetic data training"
        ],
        "category": "specific_connectable",
        "rationale": "The use of synthetic data for training is a growing area of interest, providing a bridge to discussions on data generation and augmentation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "real-time",
      "streaming applications",
      "performance",
      "efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based model",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Memory mechanism",
      "resolved_canonical": "Memory Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Long-term point tracking",
      "resolved_canonical": "Long-term Point Tracking",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Synthetic training strategies",
      "resolved_canonical": "Synthetic Training Strategies",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Track-On2: Enhancing Online Point Tracking with Memory

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19115.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19115](https://arxiv.org/abs/2509.19115)

## 🔗 유사한 논문
- [[2025-09-23/DepTR-MOT_ Unveiling the Potential of Depth-Informed Trajectory Refinement for Multi-Object Tracking_20250923|DepTR-MOT: Unveiling the Potential of Depth-Informed Trajectory Refinement for Multi-Object Tracking]] (82.6% similar)
- [[2025-09-23/ProDyG_ Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos_20250923|ProDyG: Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos]] (81.0% similar)
- [[2025-09-23/AHA -- Predicting What Matters Next_ Online Highlight Detection Without Looking Ahead_20250923|AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead]] (80.6% similar)
- [[2025-09-24/Enhancing Video Object Segmentation in TrackRAD Using XMem Memory Network_20250924|Enhancing Video Object Segmentation in TrackRAD Using XMem Memory Network]] (80.5% similar)
- [[2025-09-24/Live-E2T_ Real-time Threat Monitoring in Video via Deduplicated Event Reasoning and Chain-of-Thought_20250924|Live-E2T: Real-time Threat Monitoring in Video via Deduplicated Event Reasoning and Chain-of-Thought]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Memory Mechanism|Memory Mechanism]], [[keywords/Synthetic Training Strategies|Synthetic Training Strategies]]
**⚡ Unique Technical**: [[keywords/Long-term Point Tracking|Long-term Point Tracking]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19115v1 Announce Type: new 
Abstract: In this paper, we consider the problem of long-term point tracking, which requires consistent identification of points across video frames under significant appearance changes, motion, and occlusion. We target the online setting, i.e. tracking points frame-by-frame, making it suitable for real-time and streaming applications. We extend our prior model Track-On into Track-On2, a simple and efficient transformer-based model for online long-term tracking. Track-On2 improves both performance and efficiency through architectural refinements, more effective use of memory, and improved synthetic training strategies. Unlike prior approaches that rely on full-sequence access or iterative updates, our model processes frames causally and maintains temporal coherence via a memory mechanism, which is key to handling drift and occlusions without requiring future frames. At inference, we perform coarse patch-level classification followed by refinement. Beyond architecture, we systematically study synthetic training setups and their impact on memory behavior, showing how they shape temporal robustness over long sequences. Through comprehensive experiments, Track-On2 achieves state-of-the-art results across five synthetic and real-world benchmarks, surpassing prior online trackers and even strong offline methods that exploit bidirectional context. These results highlight the effectiveness of causal, memory-based architectures trained purely on synthetic data as scalable solutions for real-world point tracking. Project page: https://kuis-ai.github.io/track_on2

## 📝 요약

이 논문은 영상 프레임 간의 일관된 점 추적 문제를 다루며, 특히 외형 변화, 움직임, 가림 현상이 있는 상황에서의 장기 추적을 목표로 합니다. 온라인 환경에서의 프레임별 추적을 위해, 기존 모델 Track-On을 확장한 Track-On2를 제안합니다. 이 모델은 변형된 트랜스포머 기반 구조로, 메모리 사용과 합성 데이터 학습 전략을 개선하여 성능과 효율성을 높였습니다. Track-On2는 인과적 메모리 메커니즘을 통해 드리프트와 가림을 처리하며, 미래 프레임 없이도 일관성을 유지합니다. 실험 결과, Track-On2는 다섯 개의 합성 및 실제 벤치마크에서 최첨단 성능을 보였으며, 이는 합성 데이터로 학습된 인과적 메모리 기반 아키텍처의 효과성을 입증합니다.

## 🎯 주요 포인트

- 1. Track-On2는 온라인 장기 추적을 위한 간단하고 효율적인 트랜스포머 기반 모델로, 실시간 및 스트리밍 애플리케이션에 적합합니다.
- 2. 이 모델은 메모리 메커니즘을 통해 드리프트와 가림 현상을 처리하며, 향후 프레임 없이도 일관된 추적을 유지합니다.
- 3. Track-On2는 합성 데이터로만 훈련된 인과적 메모리 기반 아키텍처의 효과를 입증하며, 실제 세계의 포인트 추적에 대한 확장 가능한 솔루션을 제공합니다.
- 4. 이 모델은 다섯 가지 합성 및 실제 벤치마크에서 최첨단 결과를 달성하며, 이전의 온라인 및 오프라인 추적 방법을 능가합니다.
- 5. 합성 훈련 설정과 메모리 동작에 대한 체계적인 연구를 통해 장기 시퀀스에서의 시간적 견고성을 형성하는 방법을 보여줍니다.


---

*Generated on 2025-09-24 16:16:25*