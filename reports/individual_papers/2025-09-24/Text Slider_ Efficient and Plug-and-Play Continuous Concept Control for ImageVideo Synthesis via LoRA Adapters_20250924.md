<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:04:32.826981",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text Slider",
    "LoRA Adapters",
    "Diffusion Models",
    "Multi-concept Composition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text Slider": 0.78,
    "LoRA Adapters": 0.77,
    "Diffusion Models": 0.85,
    "Multi-concept Composition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Text Slider",
        "canonical": "Text Slider",
        "aliases": [
          "Continuous Concept Control"
        ],
        "category": "unique_technical",
        "rationale": "Text Slider is a novel framework for continuous concept control in image and video synthesis, offering significant improvements in efficiency and flexibility.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "LoRA Adapters",
        "canonical": "LoRA Adapters",
        "aliases": [
          "Low-Rank Adaptation Adapters"
        ],
        "category": "unique_technical",
        "rationale": "LoRA Adapters are a key component in enabling efficient continuous control in pre-trained text encoders, relevant for linking advancements in model adaptation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion-based Synthesis"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion Models are central to recent advancements in image and video synthesis, providing a foundational concept for linking related research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-concept Composition",
        "canonical": "Multi-concept Composition",
        "aliases": [
          "Conceptual Blending"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-concept Composition is crucial for enabling flexible and fine-grained manipulation in synthesis tasks, facilitating connections to multimodal research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "Concept Slider",
      "Attribute Control",
      "training time",
      "GPU memory"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Text Slider",
      "resolved_canonical": "Text Slider",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LoRA Adapters",
      "resolved_canonical": "LoRA Adapters",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-concept Composition",
      "resolved_canonical": "Multi-concept Composition",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Text Slider: Efficient and Plug-and-Play Continuous Concept Control for Image/Video Synthesis via LoRA Adapters

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18831.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18831](https://arxiv.org/abs/2509.18831)

## 🔗 유사한 논문
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (81.4% similar)
- [[2025-09-23/VidCLearn_ A Continual Learning Approach for Text-to-Video Generation_20250923|VidCLearn: A Continual Learning Approach for Text-to-Video Generation]] (81.0% similar)
- [[2025-09-23/CLIP-IN_ Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions_20250923|CLIP-IN: Enhancing Fine-Grained Visual Understanding in CLIP via Instruction Editing Data and Long Captions]] (80.2% similar)
- [[2025-09-23/In-Context Edit_ Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer_20250923|In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer]] (80.2% similar)
- [[2025-09-23/FG-Attn_ Leveraging Fine-Grained Sparsity In Diffusion Transformers_20250923|FG-Attn: Leveraging Fine-Grained Sparsity In Diffusion Transformers]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Multi-concept Composition|Multi-concept Composition]]
**⚡ Unique Technical**: [[keywords/Text Slider|Text Slider]], [[keywords/LoRA Adapters|LoRA Adapters]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18831v1 Announce Type: cross 
Abstract: Recent advances in diffusion models have significantly improved image and video synthesis. In addition, several concept control methods have been proposed to enable fine-grained, continuous, and flexible control over free-form text prompts. However, these methods not only require intensive training time and GPU memory usage to learn the sliders or embeddings but also need to be retrained for different diffusion backbones, limiting their scalability and adaptability. To address these limitations, we introduce Text Slider, a lightweight, efficient and plug-and-play framework that identifies low-rank directions within a pre-trained text encoder, enabling continuous control of visual concepts while significantly reducing training time, GPU memory consumption, and the number of trainable parameters. Furthermore, Text Slider supports multi-concept composition and continuous control, enabling fine-grained and flexible manipulation in both image and video synthesis. We show that Text Slider enables smooth and continuous modulation of specific attributes while preserving the original spatial layout and structure of the input. Text Slider achieves significantly better efficiency: 5$\times$ faster training than Concept Slider and 47$\times$ faster than Attribute Control, while reducing GPU memory usage by nearly 2$\times$ and 4$\times$, respectively.

## 📝 요약

최근 확산 모델의 발전은 이미지와 비디오 합성을 크게 개선했습니다. 그러나 기존의 개념 제어 방법은 많은 훈련 시간과 GPU 메모리를 요구하며, 다양한 확산 백본에 대해 재훈련이 필요해 확장성과 적응성이 제한됩니다. 이를 해결하기 위해, 우리는 사전 훈련된 텍스트 인코더 내에서 저차원 방향을 식별하여 시각적 개념을 연속적으로 제어할 수 있는 경량의 효율적인 프레임워크인 Text Slider를 제안합니다. Text Slider는 훈련 시간과 GPU 메모리 사용량을 크게 줄이고, 다중 개념 구성과 연속 제어를 지원하여 이미지와 비디오 합성에서 세밀하고 유연한 조작을 가능하게 합니다. 실험 결과, Text Slider는 기존 방법보다 훨씬 효율적이며, 훈련 속도는 Concept Slider보다 5배, Attribute Control보다 47배 빠르고, GPU 메모리 사용량도 각각 2배, 4배 줄였습니다.

## 🎯 주요 포인트

- 1. Text Slider는 사전 훈련된 텍스트 인코더 내의 저랭크 방향을 식별하여 시각적 개념의 연속적 제어를 가능하게 하며, 훈련 시간, GPU 메모리 소비, 학습 가능한 매개변수 수를 크게 줄입니다.
- 2. 이 프레임워크는 이미지와 비디오 합성에서 다중 개념 구성 및 연속 제어를 지원하여 세밀하고 유연한 조작을 가능하게 합니다.
- 3. Text Slider는 특정 속성의 부드럽고 연속적인 변조를 가능하게 하면서 입력의 원래 공간 레이아웃과 구조를 보존합니다.
- 4. Text Slider는 Concept Slider보다 5배, Attribute Control보다 47배 빠른 훈련 속도를 달성하며, GPU 메모리 사용량을 각각 거의 2배, 4배 줄입니다.


---

*Generated on 2025-09-24 14:04:32*