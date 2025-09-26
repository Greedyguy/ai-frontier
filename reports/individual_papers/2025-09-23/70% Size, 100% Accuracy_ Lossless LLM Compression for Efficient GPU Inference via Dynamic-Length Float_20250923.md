---
keywords:
  - Large Language Model
  - Dynamic-Length Float
  - Transformer
  - Entropy Coding
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2504.11651
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:40:59.386519",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Dynamic-Length Float",
    "Transformer",
    "Entropy Coding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "Dynamic-Length Float": 0.78,
    "Transformer": 0.77,
    "Entropy Coding": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large-Scale AI Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on compression and efficiency, linking to broader discussions on AI model scaling.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.68,
        "link_intent_score": 0.82
      },
      {
        "surface": "Dynamic-Length Float",
        "canonical": "Dynamic-Length Float",
        "aliases": [
          "DFloat11"
        ],
        "category": "unique_technical",
        "rationale": "Dynamic-Length Float is a unique technical contribution of the paper, essential for understanding the proposed compression method.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer-block-level decompression",
        "canonical": "Transformer",
        "aliases": [
          "Transformer-block"
        ],
        "category": "specific_connectable",
        "rationale": "Transformer-block-level decompression is a specific technique that enhances the efficiency of the compression method, linking to Transformer architecture.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Entropy coding",
        "canonical": "Entropy Coding",
        "aliases": [
          "Entropy-based compression"
        ],
        "category": "specific_connectable",
        "rationale": "Entropy coding is a key technique used in the compression framework, relevant to discussions on data compression in AI models.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.75,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "efficient inference",
      "custom GPU kernel",
      "memory constraints"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.68,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Dynamic-Length Float",
      "resolved_canonical": "Dynamic-Length Float",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer-block-level decompression",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Entropy coding",
      "resolved_canonical": "Entropy Coding",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.75,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# 70% Size, 100% Accuracy: Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.11651.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2504.11651](https://arxiv.org/abs/2504.11651)

## 🔗 유사한 논문
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (83.6% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (83.2% similar)
- [[2025-09-22/LowDiff_ Efficient Diffusion Sampling with Low-Resolution Condition_20250922|LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition]] (82.9% similar)
- [[2025-09-19/{\lambda}Scale_ Enabling Fast Scaling for Serverless Large Language Model Inference_20250919|{\lambda}Scale: Enabling Fast Scaling for Serverless Large Language Model Inference]] (82.8% similar)
- [[2025-09-23/Spiffy_ Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding_20250923|Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Transformer|Transformer]], [[keywords/Entropy Coding|Entropy Coding]]
**⚡ Unique Technical**: [[keywords/Dynamic-Length Float|Dynamic-Length Float]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.11651v2 Announce Type: replace 
Abstract: Large-scale AI models, such as Large Language Models (LLMs) and Diffusion Models (DMs), have grown rapidly in size, creating significant challenges for efficient deployment on resource-constrained hardware. In this paper, we introduce Dynamic-Length Float (DFloat11), a lossless compression framework that reduces LLM and DM size by 30% while preserving outputs that are bit-for-bit identical to the original model. DFloat11 is motivated by the low entropy in the BFloat16 weight representation of LLMs, which reveals significant inefficiency in the existing storage format. By applying entropy coding, DFloat11 assigns dynamic-length encodings to weights based on frequency, achieving near information-optimal compression without any loss of precision. To facilitate efficient inference with dynamic-length encodings, we develop a custom GPU kernel for fast online decompression. Our design incorporates the following: (i) compact, hierarchical lookup tables (LUTs) that fit within GPU SRAM for efficient decoding, (ii) a two-phase GPU kernel for coordinating thread read/write positions using lightweight auxiliary variables, and (iii) transformer-block-level decompression to minimize latency. Experiments on Llama 3.3, Qwen 3, Mistral 3, FLUX.1, and others validate our hypothesis that DFloat11 achieves around 30% model size reduction while preserving bit-for-bit identical outputs. Compared to a potential alternative of offloading parts of an uncompressed model to the CPU to meet memory constraints, DFloat11 achieves 2.3--46.2x higher throughput in token generation. With a fixed GPU memory budget, DFloat11 enables 5.7--14.9x longer generation lengths than uncompressed models. Notably, our method enables lossless inference of Llama 3.1 405B, an 810GB model, on a single node equipped with 8x80GB GPUs. Our code is available at https://github.com/LeanModels/DFloat11.

## 📝 요약

이 논문은 대규모 AI 모델의 효율적인 배포를 위해 DFloat11이라는 무손실 압축 프레임워크를 제안합니다. DFloat11은 LLM과 DM의 크기를 30% 줄이면서도 원본 모델과 비트 단위로 동일한 출력을 유지합니다. 이는 LLM의 BFloat16 가중치 표현의 낮은 엔트로피를 활용하여, 빈도에 기반한 동적 길이 인코딩을 통해 정보 최적의 압축을 실현합니다. 효율적인 추론을 위해 GPU 내에서 빠른 온라인 압축 해제를 지원하는 맞춤형 커널을 개발하였으며, 실험 결과 DFloat11은 모델 크기를 30% 줄이고, 비압축 모델 대비 최대 46.2배 높은 처리량을 달성했습니다. 이 방법은 810GB 크기의 Llama 3.1 모델을 단일 노드에서 실행 가능하게 합니다.

## 🎯 주요 포인트

- 1. DFloat11은 LLM과 DM의 크기를 30% 줄이면서 원본 모델과 동일한 출력을 유지하는 무손실 압축 프레임워크입니다.
- 2. DFloat11은 LLM의 BFloat16 가중치 표현의 낮은 엔트로피를 활용하여 정보 최적의 압축을 달성합니다.
- 3. 효율적인 추론을 위해 DFloat11은 GPU SRAM에 적합한 계층적 조회 테이블과 두 단계의 GPU 커널을 사용하여 빠른 온라인 압축 해제를 지원합니다.
- 4. DFloat11은 메모리 제약을 해결하기 위해 모델의 일부를 CPU로 오프로드하는 대안보다 2.3~46.2배 높은 처리량을 제공합니다.
- 5. DFloat11은 고정된 GPU 메모리 예산 내에서 비압축 모델보다 5.7~14.9배 긴 생성 길이를 가능하게 합니다.


---

*Generated on 2025-09-24 02:40:59*