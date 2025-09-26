---
keywords:
  - Neural Network
  - Self-supervised Learning
  - Focal Modulation
  - Streamable Codecs
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16195
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:31:40.911701",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Self-supervised Learning",
    "Focal Modulation",
    "Streamable Codecs"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Self-supervised Learning": 0.82,
    "Focal Modulation": 0.7,
    "Streamable Codecs": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural audio codecs",
        "canonical": "Neural Network",
        "aliases": [
          "Neural codecs",
          "Audio neural networks"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are a foundational technology for audio processing, linking to broader machine learning contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.55,
        "link_intent_score": 0.78
      },
      {
        "surface": "Causal distillation",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Causal learning",
          "Causal inference"
        ],
        "category": "specific_connectable",
        "rationale": "Causal distillation is a specific technique within self-supervised learning, enhancing connectivity to related learning paradigms.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Focal modulation",
        "canonical": "Focal Modulation",
        "aliases": [
          "Focal processing",
          "Modulation techniques"
        ],
        "category": "unique_technical",
        "rationale": "Focal modulation is a novel technique specific to this paper, offering unique insights into speech coding.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Streamable codecs",
        "canonical": "Streamable Codecs",
        "aliases": [
          "Real-time codecs",
          "Streaming audio codecs"
        ],
        "category": "unique_technical",
        "rationale": "Streamable codecs are crucial for real-time applications, providing a unique angle on codec technology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
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
      "candidate_surface": "Neural audio codecs",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.55,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Causal distillation",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Focal modulation",
      "resolved_canonical": "Focal Modulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Streamable codecs",
      "resolved_canonical": "Streamable Codecs",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# FocalCodec-Stream: Streaming Low-Bitrate Speech Coding via Causal Distillation

**Korean Title:** FocalCodec-Stream: 인과적 증류를 통한 스트리밍 저비트율 음성 코딩

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16195.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16195](https://arxiv.org/abs/2509.16195)

## 🔗 유사한 논문
- [[2025-09-22/VoXtream_ Full-Stream Text-to-Speech with Extremely Low Latency_20250922|VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency]] (83.3% similar)
- [[2025-09-22/Compose Yourself_ Average-Velocity Flow Matching for One-Step Speech Enhancement_20250922|Compose Yourself: Average-Velocity Flow Matching for One-Step Speech Enhancement]] (80.3% similar)
- [[2025-09-18/Real-Time Streaming Mel Vocoding with Generative Flow Matching_20250918|Real-Time Streaming Mel Vocoding with Generative Flow Matching]] (80.2% similar)
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (78.8% similar)
- [[2025-09-22/Generating Moving 3D Soundscapes with Latent Diffusion Models_20250922|Generating Moving 3D Soundscapes with Latent Diffusion Models]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Focal Modulation|Focal Modulation]], [[keywords/Streamable Codecs|Streamable Codecs]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16195v1 Announce Type: cross 
Abstract: Neural audio codecs are a fundamental component of modern generative audio pipelines. Although recent codecs achieve strong low-bitrate reconstruction and provide powerful representations for downstream tasks, most are non-streamable, limiting their use in real-time applications. We present FocalCodec-Stream, a hybrid codec based on focal modulation that compresses speech into a single binary codebook at 0.55 - 0.80 kbps with a theoretical latency of 80 ms. Our approach combines multi-stage causal distillation of WavLM with targeted architectural improvements, including a lightweight refiner module that enhances quality under latency constraints. Experiments show that FocalCodec-Stream outperforms existing streamable codecs at comparable bitrates, while preserving both semantic and acoustic information. The result is a favorable trade-off between reconstruction quality, downstream task performance, latency, and efficiency. Code and checkpoints will be released at https://github.com/lucadellalib/focalcodec.

## 🔍 Abstract (한글 번역)

arXiv:2509.16195v1 발표 유형: 교차  
초록: 신경 오디오 코덱은 현대 생성 오디오 파이프라인의 기본 구성 요소입니다. 최근의 코덱들은 낮은 비트레이트에서 강력한 재구성을 달성하고, 다운스트림 작업을 위한 강력한 표현을 제공하지만, 대부분은 스트리밍이 불가능하여 실시간 응용 프로그램에서의 사용이 제한됩니다. 우리는 FocalCodec-Stream을 소개합니다. 이는 초점 변조에 기반한 하이브리드 코덱으로, 이론적으로 80ms의 지연 시간을 가지면서 0.55 - 0.80 kbps의 단일 이진 코드북으로 음성을 압축합니다. 우리의 접근 방식은 WavLM의 다단계 인과 증류와 지연 제약 하에서 품질을 향상시키는 경량의 정제 모듈을 포함한 목표 지향적 아키텍처 개선을 결합합니다. 실험 결과, FocalCodec-Stream은 유사한 비트레이트에서 기존의 스트리밍 가능한 코덱을 능가하며, 의미적 및 음향적 정보를 모두 보존합니다. 그 결과는 재구성 품질, 다운스트림 작업 성능, 지연 시간, 효율성 간의 유리한 균형을 제공합니다. 코드와 체크포인트는 https://github.com/lucadellalib/focalcodec에서 공개될 예정입니다.

## 📝 요약

FocalCodec-Stream은 실시간 응용 프로그램에 적합한 스트리밍 가능한 신경 오디오 코덱으로, 초점 변조를 기반으로 하여 0.55 - 0.80 kbps의 비트레이트로 음성을 단일 이진 코드북으로 압축합니다. 이 코덱은 WavLM의 다단계 인과 증류와 경량화된 정제 모듈을 결합하여 80ms의 이론적 지연 시간 내에서 높은 품질을 유지합니다. 실험 결과, FocalCodec-Stream은 유사한 비트레이트에서 기존 스트리밍 코덱보다 뛰어난 성능을 보이며, 의미적 및 음향적 정보를 잘 보존합니다. 이 연구는 재구성 품질, 다운스트림 작업 성능, 지연 시간 및 효율성 간의 균형을 효과적으로 달성했습니다. 코드와 체크포인트는 GitHub에서 제공될 예정입니다.

## 🎯 주요 포인트

- 1. FocalCodec-Stream은 초점 변조 기반의 하이브리드 코덱으로, 0.55 - 0.80 kbps의 비트레이트에서 이진 코드북으로 음성을 압축하며 이론적 지연 시간은 80 ms입니다.
- 2. 이 코덱은 WavLM의 다단계 인과적 증류와 경량화된 리파이너 모듈을 포함한 아키텍처 개선을 결합하여 지연 시간 제약 하에서도 품질을 향상시킵니다.
- 3. 실험 결과, FocalCodec-Stream은 기존의 스트리밍 가능한 코덱보다 유사한 비트레이트에서 더 나은 성능을 보이며, 의미적 및 음향적 정보를 모두 보존합니다.
- 4. 이 연구는 재구성 품질, 다운스트림 작업 성능, 지연 시간 및 효율성 간의 유리한 균형을 제공합니다.
- 5. 코드와 체크포인트는 https://github.com/lucadellalib/focalcodec에서 공개될 예정입니다.


---

*Generated on 2025-09-23 09:31:40*