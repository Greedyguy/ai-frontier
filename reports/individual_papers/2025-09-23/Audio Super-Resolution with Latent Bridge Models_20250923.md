---
keywords:
  - Audio Super-Resolution
  - Latent Bridge Models
  - Frequency-aware Latent Bridge Models
  - Diffusion Models
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17609
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:24:30.965666",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Audio Super-Resolution",
    "Latent Bridge Models",
    "Frequency-aware Latent Bridge Models",
    "Diffusion Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Audio Super-Resolution": 0.78,
    "Latent Bridge Models": 0.82,
    "Frequency-aware Latent Bridge Models": 0.75,
    "Diffusion Models": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Audio Super-Resolution",
        "canonical": "Audio Super-Resolution",
        "aliases": [
          "Audio SR",
          "Upsampling"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specific audio processing technique central to the paper's contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Latent Bridge Models",
        "canonical": "Latent Bridge Models",
        "aliases": [
          "LBM"
        ],
        "category": "unique_technical",
        "rationale": "A novel model introduced in the paper, crucial for understanding the proposed methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Frequency-aware LBMs",
        "canonical": "Frequency-aware Latent Bridge Models",
        "aliases": [
          "Frequency-aware LBMs"
        ],
        "category": "unique_technical",
        "rationale": "An enhancement of the LBM concept, adding specificity to the model's application.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion"
        ],
        "category": "broad_technical",
        "rationale": "A well-known method in machine learning, relevant for connecting to broader diffusion-based techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "system",
      "process",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Audio Super-Resolution",
      "resolved_canonical": "Audio Super-Resolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Latent Bridge Models",
      "resolved_canonical": "Latent Bridge Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Frequency-aware LBMs",
      "resolved_canonical": "Frequency-aware Latent Bridge Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Audio Super-Resolution with Latent Bridge Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17609.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17609](https://arxiv.org/abs/2509.17609)

## 🔗 유사한 논문
- [[2025-09-22/Generating Moving 3D Soundscapes with Latent Diffusion Models_20250922|Generating Moving 3D Soundscapes with Latent Diffusion Models]] (82.1% similar)
- [[2025-09-22/SightSound-R1_ Cross-Modal Reasoning Distillation from Vision to Audio Language Models_20250922|SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models]] (80.4% similar)
- [[2025-09-23/Virtual Consistency for Audio Editing_20250923|Virtual Consistency for Audio Editing]] (80.1% similar)
- [[2025-09-19/Listening, Imagining \& Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining \& Refining: A Heuristic Optimized ASR Correction Framework with LLMs]] (79.6% similar)
- [[2025-09-18/Back to Ear_ Perceptually Driven High Fidelity Music Reconstruction_20250918|Back to Ear: Perceptually Driven High Fidelity Music Reconstruction]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**⚡ Unique Technical**: [[keywords/Audio Super-Resolution|Audio Super-Resolution]], [[keywords/Latent Bridge Models|Latent Bridge Models]], [[keywords/Frequency-aware Latent Bridge Models|Frequency-aware Latent Bridge Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17609v1 Announce Type: cross 
Abstract: Audio super-resolution (SR), i.e., upsampling the low-resolution (LR) waveform to the high-resolution (HR) version, has recently been explored with diffusion and bridge models, while previous methods often suffer from sub-optimal upsampling quality due to their uninformative generation prior. Towards high-quality audio super-resolution, we present a new system with latent bridge models (LBMs), where we compress the audio waveform into a continuous latent space and design an LBM to enable a latent-to-latent generation process that naturally matches the LR-toHR upsampling process, thereby fully exploiting the instructive prior information contained in the LR waveform. To further enhance the training results despite the limited availability of HR samples, we introduce frequency-aware LBMs, where the prior and target frequency are taken as model input, enabling LBMs to explicitly learn an any-to-any upsampling process at the training stage. Furthermore, we design cascaded LBMs and present two prior augmentation strategies, where we make the first attempt to unlock the audio upsampling beyond 48 kHz and empower a seamless cascaded SR process, providing higher flexibility for audio post-production. Comprehensive experimental results evaluated on the VCTK, ESC-50, Song-Describer benchmark datasets and two internal testsets demonstrate that we achieve state-of-the-art objective and perceptual quality for any-to-48kHz SR across speech, audio, and music signals, as well as setting the first record for any-to-192kHz audio SR. Demo at https://AudioLBM.github.io/.

## 📝 요약

이 논문은 오디오 초해상도(SR) 기술을 개선하기 위해 잠재 브리지 모델(LBM)을 제안합니다. 기존 방법들이 정보가 부족한 생성 사전으로 인해 최적의 업샘플링 품질을 달성하지 못하는 문제를 해결하고자, 오디오 파형을 연속적인 잠재 공간으로 압축하고, LR에서 HR로의 업샘플링 과정을 자연스럽게 연결하는 LBM을 설계했습니다. 또한, 주파수 인식 LBM을 도입하여 제한된 HR 샘플로도 효과적인 학습이 가능하도록 했습니다. 이 연구는 48kHz를 넘어서는 오디오 업샘플링을 최초로 시도하고, 오디오 후처리에 유연성을 제공합니다. VCTK, ESC-50, Song-Describer 데이터셋과 내부 테스트셋에서의 실험 결과, 제안된 방법이 최첨단의 객관적 및 지각적 품질을 달성했으며, 192kHz 오디오 SR에서도 최초의 기록을 세웠습니다.

## 🎯 주요 포인트

- 1. 새로운 시스템은 잠재 브리지 모델(LBM)을 사용하여 오디오 파형을 연속적인 잠재 공간으로 압축하고, LR에서 HR로의 업샘플링 과정을 자연스럽게 매칭하는 잠재-대-잠재 생성 과정을 가능하게 합니다.
- 2. 주파수 인식 LBM을 도입하여 모델 입력으로 사전 주파수와 목표 주파수를 사용함으로써, 학습 단계에서 모든 주파수 간 업샘플링 과정을 명시적으로 학습할 수 있습니다.
- 3. 48kHz를 초과하는 오디오 업샘플링을 최초로 시도하고, 원활한 계단식 SR 프로세스를 가능하게 하는 두 가지 사전 증강 전략을 설계하였습니다.
- 4. VCTK, ESC-50, Song-Describer 벤치마크 데이터셋 및 두 개의 내부 테스트셋에서의 종합적인 실험 결과는 48kHz까지의 SR에서 최첨단의 객관적 및 지각적 품질을 달성했음을 보여줍니다.
- 5. 192kHz까지의 오디오 SR에 대한 최초의 기록을 세웠으며, 이는 음성, 오디오 및 음악 신호 전반에 걸쳐 적용됩니다.


---

*Generated on 2025-09-24 02:24:30*