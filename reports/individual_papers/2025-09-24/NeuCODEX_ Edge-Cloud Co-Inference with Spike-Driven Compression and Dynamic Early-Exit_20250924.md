<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:16:58.218490",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Edge-Cloud Co-Inference",
    "Spike-Driven Compression",
    "Dynamic Early-Exit"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Edge-Cloud Co-Inference": 0.8,
    "Spike-Driven Compression": 0.78,
    "Dynamic Early-Exit": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Spiking Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "SNN",
          "Spiking Networks"
        ],
        "category": "broad_technical",
        "rationale": "Links to existing neural network concepts, emphasizing energy-efficient variants.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Edge-Cloud Co-Inference",
        "canonical": "Edge-Cloud Co-Inference",
        "aliases": [
          "Edge-Cloud Inference",
          "Co-Inference"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach to distributed inference, enhancing connectivity between edge and cloud systems.",
        "novelty_score": 0.78,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Spike-Driven Compression",
        "canonical": "Spike-Driven Compression",
        "aliases": [
          "Spiking Compression"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel compression technique specific to spiking data, enhancing data efficiency.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dynamic Early-Exit",
        "canonical": "Dynamic Early-Exit",
        "aliases": [
          "Adaptive Early-Exit"
        ],
        "category": "unique_technical",
        "rationale": "Describes a mechanism for adaptive inference termination, useful in resource-constrained settings.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
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
      "candidate_surface": "Spiking Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Edge-Cloud Co-Inference",
      "resolved_canonical": "Edge-Cloud Co-Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Spike-Driven Compression",
      "resolved_canonical": "Spike-Driven Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dynamic Early-Exit",
      "resolved_canonical": "Dynamic Early-Exit",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# NeuCODEX: Edge-Cloud Co-Inference with Spike-Driven Compression and Dynamic Early-Exit

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19156.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19156](https://arxiv.org/abs/2509.19156)

## 🔗 유사한 논문
- [[2025-09-24/Otters_ An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding_20250924|Otters: An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding]] (83.9% similar)
- [[2025-09-19/eIQ Neutron_ Redefining Edge-AI Inference with Integrated NPU and Compiler Innovations_20250919|eIQ Neutron: Redefining Edge-AI Inference with Integrated NPU and Compiler Innovations]] (83.3% similar)
- [[2025-09-24/Intra-DP_ A High Performance Collaborative Inference System for Mobile Edge Computing_20250924|Intra-DP: A High Performance Collaborative Inference System for Mobile Edge Computing]] (83.1% similar)
- [[2025-09-24/HyperNAS_ Enhancing Architecture Representation for NAS Predictor via Hypernetwork_20250924|HyperNAS: Enhancing Architecture Representation for NAS Predictor via Hypernetwork]] (82.7% similar)
- [[2025-09-23/SINF_ Semantic Neural Network Inference with Semantic Subgraphs_20250923|SINF: Semantic Neural Network Inference with Semantic Subgraphs]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Edge-Cloud Co-Inference|Edge-Cloud Co-Inference]], [[keywords/Spike-Driven Compression|Spike-Driven Compression]], [[keywords/Dynamic Early-Exit|Dynamic Early-Exit]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19156v1 Announce Type: new 
Abstract: Spiking Neural Networks (SNNs) offer significant potential for enabling energy-efficient intelligence at the edge. However, performing full SNN inference at the edge can be challenging due to the latency and energy constraints arising from fixed and high timestep overheads. Edge-cloud co-inference systems present a promising solution, but their deployment is often hindered by high latency and feature transmission costs. To address these issues, we introduce NeuCODEX, a neuromorphic co-inference architecture that jointly optimizes both spatial and temporal redundancy. NeuCODEX incorporates a learned spike-driven compression module to reduce data transmission and employs a dynamic early-exit mechanism to adaptively terminate inference based on output confidence. We evaluated NeuCODEX on both static images (CIFAR10 and Caltech) and neuromorphic event streams (CIFAR10-DVS and N-Caltech). To demonstrate practicality, we prototyped NeuCODEX on ResNet-18 and VGG-16 backbones in a real edge-to-cloud testbed. Our proposed system reduces data transfer by up to 2048x and edge energy consumption by over 90%, while reducing end-to-end latency by up to 3x compared to edge-only inference, all with a negligible accuracy drop of less than 2%. In doing so, NeuCODEX enables practical, high-performance SNN deployment in resource-constrained environments.

## 📝 요약

Spiking Neural Networks(SNNs)는 에너지 효율적인 엣지 인텔리전스를 가능하게 하지만, 엣지에서의 완전한 SNN 추론은 시간 지연과 에너지 제약으로 어려움이 있습니다. 이를 해결하기 위해 NeuCODEX라는 신경형 공동 추론 아키텍처를 제안합니다. NeuCODEX는 공간적, 시간적 중복성을 최적화하며, 학습된 스파이크 기반 압축 모듈을 통해 데이터 전송을 줄이고, 출력 신뢰도에 따라 추론을 조기에 종료하는 동적 메커니즘을 사용합니다. ResNet-18과 VGG-16 백본을 사용한 실험에서 NeuCODEX는 데이터 전송을 최대 2048배, 엣지 에너지 소비를 90% 이상 줄이고, 엣지 전용 추론 대비 지연 시간을 3배까지 단축하면서도 정확도 저하는 2% 미만으로 유지했습니다. 이를 통해 NeuCODEX는 자원이 제한된 환경에서 실용적이고 고성능의 SNN 배포를 가능하게 합니다.

## 🎯 주요 포인트

- 1. NeuCODEX는 공간적 및 시간적 중복성을 최적화하여 에너지 효율적인 엣지-클라우드 공동 추론을 가능하게 하는 신경형 공동 추론 아키텍처입니다.
- 2. 학습된 스파이크 기반 압축 모듈을 통해 데이터 전송을 줄이고, 출력 신뢰도에 따라 적응적으로 추론을 종료하는 동적 조기 종료 메커니즘을 도입했습니다.
- 3. NeuCODEX는 ResNet-18 및 VGG-16 백본을 사용하여 실제 엣지-클라우드 테스트베드에서 프로토타입을 구현하여 실용성을 입증했습니다.
- 4. 제안된 시스템은 데이터 전송을 최대 2048배, 엣지 에너지 소비를 90% 이상 줄이고, 엣지 전용 추론 대비 종단 간 지연을 최대 3배 감소시킵니다.
- 5. NeuCODEX는 정확도 손실이 2% 미만인 상태에서 자원 제약 환경에서의 실용적이고 고성능의 SNN 배포를 가능하게 합니다.


---

*Generated on 2025-09-24 16:16:58*