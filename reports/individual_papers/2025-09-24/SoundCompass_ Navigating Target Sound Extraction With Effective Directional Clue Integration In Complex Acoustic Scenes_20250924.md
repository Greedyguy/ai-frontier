<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:53:51.417504",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Target Sound Extraction",
    "Direction of Arrival",
    "Spherical Harmonics",
    "Spectral Pairwise Interaction",
    "Chain-of-Inference"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Target Sound Extraction": 0.78,
    "Direction of Arrival": 0.8,
    "Spherical Harmonics": 0.77,
    "Spectral Pairwise Interaction": 0.79,
    "Chain-of-Inference": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "target sound extraction",
        "canonical": "Target Sound Extraction",
        "aliases": [
          "TSE"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized process central to the paper's focus, offering unique insights into sound processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "direction of arrival",
        "canonical": "Direction of Arrival",
        "aliases": [
          "DoA"
        ],
        "category": "specific_connectable",
        "rationale": "A key concept in sound localization, linking to broader spatial audio processing topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "spherical harmonics",
        "canonical": "Spherical Harmonics",
        "aliases": [
          "SH"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for encoding spatial audio features, facilitating connections to mathematical audio processing methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Spectral Pairwise INteraction",
        "canonical": "Spectral Pairwise Interaction",
        "aliases": [
          "SPIN"
        ],
        "category": "unique_technical",
        "rationale": "A novel module introduced in the paper, crucial for understanding the proposed framework.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "chain-of-inference",
        "canonical": "Chain-of-Inference",
        "aliases": [
          "CoI"
        ],
        "category": "unique_technical",
        "rationale": "An iterative refinement strategy that enhances the framework's adaptability and accuracy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.67,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "complex acoustic scenes",
      "multichannel signals"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "target sound extraction",
      "resolved_canonical": "Target Sound Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "direction of arrival",
      "resolved_canonical": "Direction of Arrival",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "spherical harmonics",
      "resolved_canonical": "Spherical Harmonics",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Spectral Pairwise INteraction",
      "resolved_canonical": "Spectral Pairwise Interaction",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "chain-of-inference",
      "resolved_canonical": "Chain-of-Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.67,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# SoundCompass: Navigating Target Sound Extraction With Effective Directional Clue Integration In Complex Acoustic Scenes

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18561.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18561](https://arxiv.org/abs/2509.18561)

## 🔗 유사한 논문
- [[2025-09-23/Brainprint-Modulated Target Speaker Extraction_20250923|Brainprint-Modulated Target Speaker Extraction]] (81.9% similar)
- [[2025-09-18/Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (81.8% similar)
- [[2025-09-22/TISDiSS_ A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation_20250922|TISDiSS: A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation]] (80.3% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (79.6% similar)
- [[2025-09-23/Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation_20250923|Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Direction of Arrival|Direction of Arrival]], [[keywords/Spherical Harmonics|Spherical Harmonics]]
**⚡ Unique Technical**: [[keywords/Target Sound Extraction|Target Sound Extraction]], [[keywords/Spectral Pairwise Interaction|Spectral Pairwise Interaction]], [[keywords/Chain-of-Inference|Chain-of-Inference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18561v1 Announce Type: cross 
Abstract: Recent advances in target sound extraction (TSE) utilize directional clues derived from direction of arrival (DoA), which represent an inherent spatial property of sound available in any acoustic scene. However, previous DoA-based methods rely on hand-crafted features or discrete encodings, which lose fine-grained spatial information and limit adaptability. We propose SoundCompass, an effective directional clue integration framework centered on a Spectral Pairwise INteraction (SPIN) module that captures cross-channel spatial correlations in the complex spectrogram domain to preserve full spatial information in multichannel signals. The input feature expressed in terms of spatial correlations is fused with a DoA clue represented as spherical harmonics (SH) encoding. The fusion is carried out across overlapping frequency subbands, inheriting the benefits reported in the previous band-split architectures. We also incorporate the iterative refinement strategy, chain-of-inference (CoI), in the TSE framework, which recursively fuses DoA with sound event activation estimated from the previous inference stage. Experiments demonstrate that SoundCompass, combining SPIN, SH embedding, and CoI, robustly extracts target sources across diverse signal classes and spatial configurations.

## 📝 요약

최근 표적 음원 추출(TSE) 분야에서는 도착 방향(DoA)으로부터 유도된 방향 단서를 활용하는 연구가 주목받고 있습니다. 기존의 DoA 기반 방법들은 수작업으로 만든 특징이나 이산적 인코딩에 의존하여 세밀한 공간 정보를 잃고 적응성이 제한되었습니다. 본 연구에서는 SoundCompass라는 효과적인 방향 단서 통합 프레임워크를 제안합니다. 이는 복잡한 스펙트로그램 도메인에서 채널 간 공간 상관관계를 포착하는 Spectral Pairwise INteraction (SPIN) 모듈을 중심으로 하며, 다채널 신호의 전체 공간 정보를 보존합니다. 입력 특징은 공간 상관관계로 표현되며, 구면 조화 함수(SH) 인코딩으로 표현된 DoA 단서와 융합됩니다. 융합은 중첩된 주파수 서브밴드에서 수행되어 이전 밴드 분할 아키텍처의 이점을 계승합니다. 또한, TSE 프레임워크에 반복적 개선 전략인 chain-of-inference (CoI)를 도입하여 이전 추론 단계에서 추정된 음원 활성화와 DoA를 재귀적으로 융합합니다. 실험 결과, SPIN, SH 임베딩, CoI를 결합한 SoundCompass는 다양한 신호 클래스와 공간 구성에서 표적 음원을 견고하게 추출함을 보여줍니다.

## 🎯 주요 포인트

- 1. SoundCompass는 복잡한 스펙트로그램 도메인에서 채널 간 공간 상관관계를 포착하여 다채널 신호의 전체 공간 정보를 보존합니다.
- 2. 제안된 프레임워크는 구면 조화(SH) 인코딩으로 표현된 DoA 단서를 공간 상관관계로 표현된 입력 특징과 융합합니다.
- 3. 주파수 서브밴드에 걸쳐 융합이 이루어지며, 이는 이전 밴드 분할 아키텍처에서 보고된 이점을 계승합니다.
- 4. 체인 오브 인퍼런스(CoI)라는 반복적 정제 전략을 도입하여 이전 추론 단계에서 추정된 소리 이벤트 활성화와 DoA를 재귀적으로 융합합니다.
- 5. 실험 결과, SoundCompass는 SPIN, SH 임베딩, CoI를 결합하여 다양한 신호 클래스와 공간 구성에서 목표 소스를 견고하게 추출합니다.


---

*Generated on 2025-09-24 13:53:51*