<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:00:26.053733",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Codebook-based Adaptive Feature Compression",
    "Semantic Enhancement",
    "Vector Quantization",
    "Edge-Cloud Systems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Codebook-based Adaptive Feature Compression": 0.79,
    "Semantic Enhancement": 0.78,
    "Vector Quantization": 0.72,
    "Edge-Cloud Systems": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Codebook-based Adaptive Feature Compression",
        "canonical": "Codebook-based Adaptive Feature Compression",
        "aliases": [
          "CAFC"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach specific to the paper, enhancing connectivity in edge-cloud systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Semantic Enhancement",
        "canonical": "Semantic Enhancement",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Semantic enhancement is a unique technique in the paper that improves feature compression, offering a new linkage point.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vector Quantization",
        "canonical": "Vector Quantization",
        "aliases": [
          "VQ"
        ],
        "category": "broad_technical",
        "rationale": "Vector Quantization is a well-known technique that connects to various compression methods in machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Edge-Cloud Systems",
        "canonical": "Edge-Cloud Systems",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Edge-cloud systems are an evolving concept, crucial for understanding distributed computing frameworks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Codebook-based Adaptive Feature Compression",
      "resolved_canonical": "Codebook-based Adaptive Feature Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Semantic Enhancement",
      "resolved_canonical": "Semantic Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vector Quantization",
      "resolved_canonical": "Vector Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Edge-Cloud Systems",
      "resolved_canonical": "Edge-Cloud Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Codebook-Based Adaptive Feature Compression With Semantic Enhancement for Edge-Cloud Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18481.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18481](https://arxiv.org/abs/2509.18481)

## 🔗 유사한 논문
- [[2025-09-23/Single-step Diffusion for Image Compression at Ultra-Low Bitrates_20250923|Single-step Diffusion for Image Compression at Ultra-Low Bitrates]] (84.4% similar)
- [[2025-09-23/ISCS_ Parameter-Guided Channel Ordering and Grouping for Learned Image Compression_20250923|ISCS: Parameter-Guided Channel Ordering and Grouping for Learned Image Compression]] (82.4% similar)
- [[2025-09-23/Learning Attribute-Aware Hash Codes for Fine-Grained Image Retrieval via Query Optimization_20250923|Learning Attribute-Aware Hash Codes for Fine-Grained Image Retrieval via Query Optimization]] (81.9% similar)
- [[2025-09-22/MEC-Quant_ Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training_20250922|MEC-Quant: Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training]] (81.3% similar)
- [[2025-09-18/Generative Image Coding with Diffusion Prior_20250918|Generative Image Coding with Diffusion Prior]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Vector Quantization|Vector Quantization]]
**⚡ Unique Technical**: [[keywords/Codebook-based Adaptive Feature Compression|Codebook-based Adaptive Feature Compression]], [[keywords/Semantic Enhancement|Semantic Enhancement]]
**🚀 Evolved Concepts**: [[keywords/Edge-Cloud Systems|Edge-Cloud Systems]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18481v1 Announce Type: new 
Abstract: Coding images for machines with minimal bitrate and strong analysis performance is key to effective edge-cloud systems. Several approaches deploy an image codec and perform analysis on the reconstructed image. Other methods compress intermediate features using entropy models and subsequently perform analysis on the decoded features. Nevertheless, these methods both perform poorly under low-bitrate conditions, as they retain many redundant details or learn over-concentrated symbol distributions. In this paper, we propose a Codebook-based Adaptive Feature Compression framework with Semantic Enhancement, named CAFC-SE. It maps continuous visual features to discrete indices with a codebook at the edge via Vector Quantization (VQ) and selectively transmits them to the cloud. The VQ operation that projects feature vectors onto the nearest visual primitives enables us to preserve more informative visual patterns under low-bitrate conditions. Hence, CAFC-SE is less vulnerable to low-bitrate conditions. Extensive experiments demonstrate the superiority of our method in terms of rate and accuracy.

## 📝 요약

이 논문은 엣지-클라우드 시스템에서 최소 비트레이트로 이미지 코딩을 수행하면서도 강력한 분석 성능을 유지하는 방법을 제안합니다. 기존 방법들은 재구성된 이미지나 중간 특징을 압축하여 분석하지만, 낮은 비트레이트에서는 성능이 저하됩니다. 본 연구에서는 코드북 기반의 적응형 특징 압축 프레임워크인 CAFC-SE를 제안합니다. 이는 벡터 양자화(VQ)를 통해 연속적인 시각적 특징을 이산적인 인덱스로 매핑하고, 선택적으로 클라우드로 전송합니다. VQ는 특징 벡터를 가장 가까운 시각적 원시로 투영하여, 낮은 비트레이트에서도 정보가 풍부한 시각적 패턴을 보존할 수 있게 합니다. 실험 결과, CAFC-SE는 비트레이트와 정확도 면에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 저비트율 조건에서 강력한 분석 성능을 유지하는 이미지 코딩은 엣지-클라우드 시스템의 핵심입니다.
- 2. 기존 방법들은 재구성된 이미지 또는 디코딩된 중간 특징에서 분석을 수행하지만, 저비트율 조건에서는 성능이 저하됩니다.
- 3. CAFC-SE는 벡터 양자화를 통해 연속적인 시각적 특징을 이산적인 인덱스로 매핑하고, 선택적으로 클라우드로 전송합니다.
- 4. CAFC-SE는 저비트율 조건에서도 정보가 풍부한 시각적 패턴을 보존하여 성능 저하를 방지합니다.
- 5. 광범위한 실험을 통해 CAFC-SE의 비율과 정확도 측면에서의 우수성이 입증되었습니다.


---

*Generated on 2025-09-24 16:00:26*