<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:12:08.358590",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Frequency-Domain Analysis",
    "Cross-Modal Consistency",
    "Iterative Frequency Decomposition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Frequency-Domain Analysis": 0.78,
    "Cross-Modal Consistency": 0.77,
    "Iterative Frequency Decomposition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Audio-Visual Segmentation",
        "canonical": "Multimodal Learning",
        "aliases": [
          "AVS"
        ],
        "category": "specific_connectable",
        "rationale": "Audio-Visual Segmentation is a specific application of Multimodal Learning, linking it to broader multimodal research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Frequency-Domain Decomposition",
        "canonical": "Frequency-Domain Analysis",
        "aliases": [
          "FDD"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's approach, offering a unique perspective on signal processing in AVS.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Synergistic Cross-Modal Consistency",
        "canonical": "Cross-Modal Consistency",
        "aliases": [
          "SCMC"
        ],
        "category": "unique_technical",
        "rationale": "This module enhances semantic consistency across modalities, a novel contribution to AVS.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Residual-based Iterative Frequency Decomposition",
        "canonical": "Iterative Frequency Decomposition",
        "aliases": [
          "RIFD"
        ],
        "category": "unique_technical",
        "rationale": "This method is a key innovation for distinguishing modality-specific features in the AVS framework.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "benchmark datasets",
      "qualitative visualizations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Audio-Visual Segmentation",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Frequency-Domain Decomposition",
      "resolved_canonical": "Frequency-Domain Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Synergistic Cross-Modal Consistency",
      "resolved_canonical": "Cross-Modal Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Residual-based Iterative Frequency Decomposition",
      "resolved_canonical": "Iterative Frequency Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Frequency-Domain Decomposition and Recomposition for Robust Audio-Visual Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18912.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18912](https://arxiv.org/abs/2509.18912)

## 🔗 유사한 논문
- [[2025-09-23/Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation_20250923|Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation]] (87.6% similar)
- [[2025-09-18/Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (85.2% similar)
- [[2025-09-23/VocSegMRI_ Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI_20250923|VocSegMRI: Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI]] (83.8% similar)
- [[2025-09-23/VAInpaint_ Zero-Shot Video-Audio inpainting framework with LLMs-driven Module_20250923|VAInpaint: Zero-Shot Video-Audio inpainting framework with LLMs-driven Module]] (82.9% similar)
- [[2025-09-18/Back to Ear_ Perceptually Driven High Fidelity Music Reconstruction_20250918|Back to Ear: Perceptually Driven High Fidelity Music Reconstruction]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Frequency-Domain Analysis|Frequency-Domain Analysis]], [[keywords/Cross-Modal Consistency|Cross-Modal Consistency]], [[keywords/Iterative Frequency Decomposition|Iterative Frequency Decomposition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18912v1 Announce Type: new 
Abstract: Audio-visual segmentation (AVS) plays a critical role in multimodal machine learning by effectively integrating audio and visual cues to precisely segment objects or regions within visual scenes. Recent AVS methods have demonstrated significant improvements. However, they overlook the inherent frequency-domain contradictions between audio and visual modalities--the pervasively interfering noise in audio high-frequency signals vs. the structurally rich details in visual high-frequency signals. Ignoring these differences can result in suboptimal performance. In this paper, we rethink the AVS task from a deeper perspective by reformulating AVS task as a frequency-domain decomposition and recomposition problem. To this end, we introduce a novel Frequency-Aware Audio-Visual Segmentation (FAVS) framework consisting of two key modules: Frequency-Domain Enhanced Decomposer (FDED) module and Synergistic Cross-Modal Consistency (SCMC) module. FDED module employs a residual-based iterative frequency decomposition to discriminate modality-specific semantics and structural features, and SCMC module leverages a mixture-of-experts architecture to reinforce semantic consistency and modality-specific feature preservation through dynamic expert routing. Extensive experiments demonstrate that our FAVS framework achieves state-of-the-art performance on three benchmark datasets, and abundant qualitative visualizations further verify the effectiveness of the proposed FDED and SCMC modules. The code will be released as open source upon acceptance of the paper.

## 📝 요약

이 논문은 주파수 영역에서의 차이를 고려하여 오디오-비주얼 세분화(AVS) 문제를 재구성하는 새로운 접근법을 제안합니다. 기존 AVS 방법론은 오디오와 비주얼 신호의 주파수 차이를 간과하여 최적의 성능을 발휘하지 못했습니다. 이를 해결하기 위해, 주파수 인식 오디오-비주얼 세분화(FAVS) 프레임워크를 도입하였으며, 이는 주파수 영역 강화 분해 모듈(FDED)과 시너지적 교차 모달 일관성 모듈(SCMC)로 구성됩니다. FDED는 잔차 기반의 반복적 주파수 분해를 통해 모달리티별 의미와 구조적 특징을 구별하고, SCMC는 전문가 혼합 구조를 활용하여 의미 일관성과 모달리티별 특징 보존을 강화합니다. 실험 결과, 제안된 FAVS 프레임워크는 세 가지 벤치마크 데이터셋에서 최첨단 성능을 달성했으며, 다양한 시각적 검증을 통해 FDED와 SCMC 모듈의 효과성을 입증했습니다.

## 🎯 주요 포인트

- 1. 오디오-비주얼 세분화(AVS)는 멀티모달 머신러닝에서 오디오와 비주얼 신호를 효과적으로 통합하여 시각적 장면 내 객체나 영역을 정확히 세분화하는 데 중요한 역할을 한다.
- 2. 기존 AVS 방법들은 오디오와 비주얼 모달리티 간의 주파수 영역의 차이를 간과하여 최적의 성능을 발휘하지 못할 수 있다.
- 3. 본 논문은 AVS 과제를 주파수 영역 분해 및 재구성 문제로 재정의하여 새로운 주파수 인식 오디오-비주얼 세분화(FAVS) 프레임워크를 제안한다.
- 4. FAVS 프레임워크는 주파수-영역 강화 분해 모듈(FDED)과 시너지 교차-모달 일관성 모듈(SCMC)로 구성되어 있으며, 각각 모달리티별 의미와 구조적 특징을 구별하고 의미 일관성을 강화한다.
- 5. 제안된 FAVS 프레임워크는 세 가지 벤치마크 데이터셋에서 최첨단 성능을 달성했으며, 풍부한 정성적 시각화 결과는 FDED 및 SCMC 모듈의 효과성을 입증한다.


---

*Generated on 2025-09-24 16:12:08*