<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:13:02.924794",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Universal Head Avatar Prior",
    "Audio-Driven Avatar",
    "Lip Synchronization",
    "Monocular Encoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Universal Head Avatar Prior": 0.8,
    "Audio-Driven Avatar": 0.79,
    "Lip Synchronization": 0.78,
    "Monocular Encoder": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Universal Head Avatar Prior",
        "canonical": "Universal Head Avatar Prior",
        "aliases": [
          "UHAP"
        ],
        "category": "unique_technical",
        "rationale": "UHAP is a novel concept introduced in the paper, crucial for linking to discussions on avatar synthesis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "audio-driven avatar",
        "canonical": "Audio-Driven Avatar",
        "aliases": [
          "audio-based avatar"
        ],
        "category": "specific_connectable",
        "rationale": "This term connects to the broader field of audio-visual synthesis and avatar creation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "lip synchronization",
        "canonical": "Lip Synchronization",
        "aliases": [
          "lip sync"
        ],
        "category": "specific_connectable",
        "rationale": "Lip synchronization is a key feature in avatar realism, linking to speech and animation research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "monocular encoder",
        "canonical": "Monocular Encoder",
        "aliases": [
          "single-view encoder"
        ],
        "category": "unique_technical",
        "rationale": "Monocular encoder is a specific technique used for efficient avatar personalization.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "model",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Universal Head Avatar Prior",
      "resolved_canonical": "Universal Head Avatar Prior",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "audio-driven avatar",
      "resolved_canonical": "Audio-Driven Avatar",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "lip synchronization",
      "resolved_canonical": "Lip Synchronization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "monocular encoder",
      "resolved_canonical": "Monocular Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Audio-Driven Universal Gaussian Head Avatars

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18924.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18924](https://arxiv.org/abs/2509.18924)

## 🔗 유사한 논문
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (84.2% similar)
- [[2025-09-23/Beat on Gaze_ Learning Stylized Generation of Gaze and Head Dynamics_20250923|Beat on Gaze: Learning Stylized Generation of Gaze and Head Dynamics]] (83.7% similar)
- [[2025-09-22/Tiny is not small enough_ High-quality, low-resource facial animation models through hybrid knowledge distillation_20250922|Tiny is not small enough: High-quality, low-resource facial animation models through hybrid knowledge distillation]] (81.8% similar)
- [[2025-09-23/PGSTalker_ Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control_20250923|PGSTalker: Real-Time Audio-Driven Talking Head Generation via 3D Gaussian Splatting with Pixel-Aware Density Control]] (81.2% similar)
- [[2025-09-23/Revisiting Speech-Lip Alignment_ A Phoneme-Aware Speech Encoder for Robust Talking Head Synthesis_20250923|Revisiting Speech-Lip Alignment: A Phoneme-Aware Speech Encoder for Robust Talking Head Synthesis]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Audio-Driven Avatar|Audio-Driven Avatar]], [[keywords/Lip Synchronization|Lip Synchronization]]
**⚡ Unique Technical**: [[keywords/Universal Head Avatar Prior|Universal Head Avatar Prior]], [[keywords/Monocular Encoder|Monocular Encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18924v1 Announce Type: new 
Abstract: We introduce the first method for audio-driven universal photorealistic avatar synthesis, combining a person-agnostic speech model with our novel Universal Head Avatar Prior (UHAP). UHAP is trained on cross-identity multi-view videos. In particular, our UHAP is supervised with neutral scan data, enabling it to capture the identity-specific details at high fidelity. In contrast to previous approaches, which predominantly map audio features to geometric deformations only while ignoring audio-dependent appearance variations, our universal speech model directly maps raw audio inputs into the UHAP latent expression space. This expression space inherently encodes, both, geometric and appearance variations. For efficient personalization to new subjects, we employ a monocular encoder, which enables lightweight regression of dynamic expression variations across video frames. By accounting for these expression-dependent changes, it enables the subsequent model fine-tuning stage to focus exclusively on capturing the subject's global appearance and geometry. Decoding these audio-driven expression codes via UHAP generates highly realistic avatars with precise lip synchronization and nuanced expressive details, such as eyebrow movement, gaze shifts, and realistic mouth interior appearance as well as motion. Extensive evaluations demonstrate that our method is not only the first generalizable audio-driven avatar model that can account for detailed appearance modeling and rendering, but it also outperforms competing (geometry-only) methods across metrics measuring lip-sync accuracy, quantitative image quality, and perceptual realism.

## 📝 요약

이 논문은 오디오 기반의 보편적인 포토리얼리스틱 아바타 생성 방법을 제안합니다. 이 방법은 사람에 구애받지 않는 음성 모델과 새로운 Universal Head Avatar Prior (UHAP)을 결합합니다. UHAP는 다중 시점 비디오로 훈련되며, 중립적인 스캔 데이터를 사용하여 높은 충실도의 정체성 세부 사항을 포착합니다. 기존 방법들이 오디오 특징을 기하학적 변형에만 매핑하는 것과 달리, 이 모델은 원시 오디오 입력을 UHAP의 표현 공간으로 직접 매핑하여 기하학적 및 외관 변화를 모두 인코딩합니다. 새로운 피사체에 대한 효율적인 개인화를 위해 단안 인코더를 사용하여 비디오 프레임 전반에 걸친 동적 표현 변화를 경량으로 회귀합니다. 이를 통해 모델의 미세 조정 단계가 피사체의 전반적인 외관과 기하학을 포착하는 데 집중할 수 있게 합니다. UHAP를 통해 오디오 기반 표현 코드를 디코딩하면 정밀한 입술 동기화와 섬세한 표현 세부 사항을 가진 매우 현실적인 아바타가 생성됩니다. 광범위한 평가 결과, 이 방법이 입술 동기화 정확성, 정량적 이미지 품질, 지각적 현실감을 측정하는 지표에서 경쟁 방법들을 능가함을 보여줍니다.

## 🎯 주요 포인트

- 1. 이 연구는 오디오 기반의 보편적인 포토리얼리스틱 아바타 합성을 위한 첫 번째 방법을 제안합니다.
- 2. Universal Head Avatar Prior (UHAP)는 다중 시점 비디오로 훈련되어 높은 충실도의 정체성 세부 사항을 포착합니다.
- 3. 기존 방법과 달리, 이 모델은 오디오 입력을 UHAP 잠재 표현 공간으로 직접 매핑하여 기하학적 및 외관 변화를 모두 인코딩합니다.
- 4. 경량화된 개인화를 위해 단안 인코더를 사용하여 동적 표현 변화를 회귀 분석합니다.
- 5. 제안된 방법은 입술 동기화 정확성, 이미지 품질, 지각적 사실성 측면에서 기존 방법을 능가합니다.


---

*Generated on 2025-09-24 16:13:02*