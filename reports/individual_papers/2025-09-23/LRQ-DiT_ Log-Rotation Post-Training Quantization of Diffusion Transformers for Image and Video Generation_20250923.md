---
keywords:
  - Transformer
  - Post-Training Quantization
  - Twin-Log Quantization
  - Adaptive Rotation Scheme
  - Computer Vision
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2508.03485
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:28:12.336150",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Post-Training Quantization",
    "Twin-Log Quantization",
    "Adaptive Rotation Scheme",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Post-Training Quantization": 0.9,
    "Twin-Log Quantization": 0.88,
    "Adaptive Rotation Scheme": 0.87,
    "Computer Vision": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformers",
        "canonical": "Transformer",
        "aliases": [
          "DiT"
        ],
        "category": "broad_technical",
        "rationale": "As a variant of Transformers, it connects well with existing Transformer-based models and methods.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Post-Training Quantization",
        "canonical": "Post-Training Quantization",
        "aliases": [
          "PTQ"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's contribution and connects to model compression discussions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Twin-Log Quantization",
        "canonical": "Twin-Log Quantization",
        "aliases": [
          "TLQ"
        ],
        "category": "unique_technical",
        "rationale": "A novel quantization method introduced in the paper, relevant for discussions on quantization techniques.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Adaptive Rotation Scheme",
        "canonical": "Adaptive Rotation Scheme",
        "aliases": [
          "ARS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new approach to handle activation outliers, linking to optimization techniques.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.87
      },
      {
        "surface": "Image and Video Generation",
        "canonical": "Computer Vision",
        "aliases": [
          "Image Generation",
          "Video Generation"
        ],
        "category": "broad_technical",
        "rationale": "This connects to the broader field of computer vision, relevant for linking across visual generation topics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Gaussian-like distribution",
      "activation quantization",
      "resource-constrained scenarios"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Post-Training Quantization",
      "resolved_canonical": "Post-Training Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Twin-Log Quantization",
      "resolved_canonical": "Twin-Log Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Adaptive Rotation Scheme",
      "resolved_canonical": "Adaptive Rotation Scheme",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.87
      }
    },
    {
      "candidate_surface": "Image and Video Generation",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# LRQ-DiT: Log-Rotation Post-Training Quantization of Diffusion Transformers for Image and Video Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2508.03485.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2508.03485](https://arxiv.org/abs/2508.03485)

## 🔗 유사한 논문
- [[2025-09-23/PTQTP_ Post-Training Quantization to Trit-Planes for Large Language Models_20250923|PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models]] (85.7% similar)
- [[2025-09-17/BWCache_ Accelerating Video Diffusion Transformers through Block-Wise Caching_20250917|BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching]] (84.5% similar)
- [[2025-09-23/DiCo_ Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling_20250923|DiCo: Revitalizing ConvNets for Scalable and Efficient Diffusion Modeling]] (84.1% similar)
- [[2025-09-23/QVGen_ Pushing the Limit of Quantized Video Generative Models_20250923|QVGen: Pushing the Limit of Quantized Video Generative Models]] (83.9% similar)
- [[2025-09-23/AlignedGen_ Aligning Style Across Generated Images_20250923|AlignedGen: Aligning Style Across Generated Images]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/Post-Training Quantization|Post-Training Quantization]], [[keywords/Twin-Log Quantization|Twin-Log Quantization]], [[keywords/Adaptive Rotation Scheme|Adaptive Rotation Scheme]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.03485v2 Announce Type: replace 
Abstract: Diffusion Transformers (DiTs) have achieved impressive performance in text-to-image and text-to-video generation. However, their high computational cost and large parameter sizes pose significant challenges for usage in resource-constrained scenarios. Effective compression of models has become a crucial issue that urgently needs to be addressed. Post-training quantization (PTQ) is a promising solution to reduce memory usage and accelerate inference, but existing PTQ methods suffer from severe performance degradation under extreme low-bit settings. After experiments and analysis, we identify two key obstacles to low-bit PTQ for DiTs: (1) the weights of DiT models follow a Gaussian-like distribution with long tails, causing uniform quantization to poorly allocate intervals and leading to significant quantization errors. This issue has been observed in the linear layer weights of different DiT models, which deeply limits the performance. (2) two types of activation outliers in DiT models: (i) Mild Outliers with slightly elevated values, and (ii) Salient Outliers with large magnitudes concentrated in specific channels, which disrupt activation quantization. To address these issues, we propose LRQ-DiT, an efficient and accurate post-training quantization framework for image and video generation. First, we introduce Twin-Log Quantization (TLQ), a log-based method that allocates more quantization intervals to the intermediate dense regions, effectively achieving alignment with the weight distribution and reducing quantization errors. Second, we propose an Adaptive Rotation Scheme (ARS) that dynamically applies Hadamard or outlier-aware rotations based on activation fluctuation, effectively mitigating the impact of both types of outliers.Extensive experiments on various text-to-image and text-to-video DiT models demonstrate that LRQ-DiT preserves high generation quality.

## 📝 요약

Diffusion Transformers (DiTs)는 텍스트-이미지 및 텍스트-비디오 생성에서 뛰어난 성능을 보였으나, 높은 계산 비용과 큰 파라미터 크기로 인해 자원 제약 환경에서 사용이 어려운 문제가 있습니다. 이를 해결하기 위해 모델 압축이 중요해졌으며, 사후 양자화(PTQ)는 메모리 사용량을 줄이고 추론을 가속화하는 유망한 방법입니다. 그러나 기존 PTQ 방법은 극단적인 저비트 설정에서 성능 저하를 겪습니다. 연구에서는 DiT 모델의 가중치가 긴 꼬리를 가진 가우시안 분포를 따르고, 활성화 값에서 두 가지 유형의 이상치가 발생하여 양자화 오류를 초래하는 것을 확인했습니다. 이를 해결하기 위해 LRQ-DiT라는 효율적이고 정확한 사후 양자화 프레임워크를 제안합니다. Twin-Log Quantization(TLQ) 방법을 도입하여 가중치 분포에 맞춰 양자화 간격을 할당하고, Adaptive Rotation Scheme(ARS)을 통해 활성화 이상치의 영향을 완화합니다. 다양한 실험을 통해 LRQ-DiT가 높은 생성 품질을 유지함을 입증했습니다.

## 🎯 주요 포인트

- 1. Diffusion Transformers (DiTs)는 텍스트-이미지 및 텍스트-비디오 생성에서 뛰어난 성능을 보였으나, 높은 계산 비용과 큰 파라미터 크기로 인해 자원 제약이 있는 환경에서 사용이 어려움.
- 2. 기존의 사후 훈련 양자화(PTQ) 방법은 극단적인 저비트 설정에서 성능 저하를 겪음.
- 3. DiT 모델의 가중치가 긴 꼬리를 가진 가우시안 분포를 따라 균일 양자화가 간격을 잘못 할당하여 양자화 오류를 유발함.
- 4. DiT 모델의 활성화에서 두 가지 유형의 이상치가 발견됨: 약간 높은 값을 가진 Mild Outliers와 특정 채널에 집중된 큰 크기의 Salient Outliers.
- 5. 제안된 LRQ-DiT 프레임워크는 Twin-Log Quantization과 Adaptive Rotation Scheme을 통해 양자화 오류를 줄이고, 활성화 이상치의 영향을 완화하여 높은 생성 품질을 유지함.


---

*Generated on 2025-09-24 05:28:12*