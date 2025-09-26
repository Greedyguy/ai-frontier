<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:57:40.362177",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Optoelectronic Synapse",
    "Time-to-First-Spike Encoding",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Optoelectronic Synapse": 0.78,
    "Time-to-First-Spike Encoding": 0.82,
    "Transformer": 0.88
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
        "rationale": "Links to the broader category of neural networks, which is foundational for understanding the paper's context.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Optoelectronic Synapse",
        "canonical": "Optoelectronic Synapse",
        "aliases": [
          "Optical Synapse",
          "Indium Oxide Synapse"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel hardware component crucial for the paper's proposed energy-efficient computation.",
        "novelty_score": 0.92,
        "connectivity_score": 0.67,
        "specificity_score": 0.91,
        "link_intent_score": 0.78
      },
      {
        "surface": "Time-to-First-Spike Encoding",
        "canonical": "Time-to-First-Spike Encoding",
        "aliases": [
          "TTFS Encoding"
        ],
        "category": "unique_technical",
        "rationale": "A specific encoding method central to the paper's energy efficiency claims.",
        "novelty_score": 0.85,
        "connectivity_score": 0.72,
        "specificity_score": 0.89,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Connects to a widely recognized architecture, facilitating integration with existing knowledge graphs.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "energy efficiency",
      "state-of-the-art",
      "hardware-software co-design"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Optoelectronic Synapse",
      "resolved_canonical": "Optoelectronic Synapse",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.67,
        "specificity": 0.91,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Time-to-First-Spike Encoding",
      "resolved_canonical": "Time-to-First-Spike Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.72,
        "specificity": 0.89,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# Otters: An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18968.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18968](https://arxiv.org/abs/2509.18968)

## 🔗 유사한 논문
- [[2025-09-23/CSDformer_ A Conversion Method for Fully Spike-Driven Transformer_20250923|CSDformer: A Conversion Method for Fully Spike-Driven Transformer]] (85.1% similar)
- [[2025-09-22/SPACE_ SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks_20250922|SPACE: SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks]] (84.5% similar)
- [[2025-09-23/Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics_20250923|Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics]] (83.8% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (82.4% similar)
- [[2025-09-22/Automating Versatile Time-Series Analysis with Tiny Transformers on Embedded FPGAs_20250922|Automating Versatile Time-Series Analysis with Tiny Transformers on Embedded FPGAs]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]], [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Optoelectronic Synapse|Optoelectronic Synapse]], [[keywords/Time-to-First-Spike Encoding|Time-to-First-Spike Encoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18968v1 Announce Type: new 
Abstract: Spiking neural networks (SNNs) promise high energy efficiency, particularly with time-to-first-spike (TTFS) encoding, which maximizes sparsity by emitting at most one spike per neuron. However, such energy advantage is often unrealized because inference requires evaluating a temporal decay function and subsequent multiplication with the synaptic weights. This paper challenges this costly approach by repurposing a physical hardware `bug', namely, the natural signal decay in optoelectronic devices, as the core computation of TTFS. We fabricated a custom indium oxide optoelectronic synapse, showing how its natural physical decay directly implements the required temporal function. By treating the device's analog output as the fused product of the synaptic weight and temporal decay, optoelectronic synaptic TTFS (named Otters) eliminates these expensive digital operations. To use the Otters paradigm in complex architectures like the transformer, which are challenging to train directly due to the sparsity issue, we introduce a novel quantized neural network-to-SNN conversion algorithm. This complete hardware-software co-design enables our model to achieve state-of-the-art accuracy across seven GLUE benchmark datasets and demonstrates a 1.77$\times$ improvement in energy efficiency over previous leading SNNs, based on a comprehensive analysis of compute, data movement, and memory access costs using energy measurements from a commercial 22nm process. Our work thus establishes a new paradigm for energy-efficient SNNs, translating fundamental device physics directly into powerful computational primitives. All codes and data are open source.

## 📝 요약

이 논문은 스파이킹 신경망(SNN)의 에너지 효율성을 높이기 위해 새로운 하드웨어-소프트웨어 공동 설계를 제안합니다. 기존의 SNN은 시간-첫-스파이크(TTFS) 인코딩을 통해 에너지를 절약하지만, 시간적 감쇠 함수와 시냅스 가중치의 곱셈이 필요해 실제로는 비효율적입니다. 저자들은 인듐 산화물 광전자 시냅스를 제작하여 자연적인 신호 감쇠를 TTFS의 핵심 연산으로 활용했습니다. 이를 통해 복잡한 신경망 구조에서도 효율적으로 사용할 수 있는 새로운 양자화 신경망-스파이킹 신경망 변환 알고리즘을 개발했습니다. 이 방법은 GLUE 벤치마크 데이터셋에서 최첨단 정확도를 달성했으며, 기존 SNN 대비 에너지 효율성을 1.77배 개선했습니다. 모든 코드와 데이터는 오픈 소스로 제공됩니다.

## 🎯 주요 포인트

- 1. 스파이킹 신경망(SNN)의 에너지 효율성을 높이기 위해 자연적인 신호 감쇠를 활용한 옵토전자 시냅스를 개발했습니다.
- 2. 옵토전자 시냅스의 자연적 물리적 감쇠를 통해 시간-첫-스파이크(TTFS) 인코딩의 핵심 연산을 구현하여 디지털 연산 비용을 절감했습니다.
- 3. 복잡한 아키텍처에서의 희소성 문제를 해결하기 위해 새로운 양자화 신경망-스파이킹 신경망 변환 알고리즘을 도입했습니다.
- 4. 제안된 하드웨어-소프트웨어 공동 설계를 통해 GLUE 벤치마크 데이터셋에서 최첨단 정확도를 달성하고, 이전 SNN 대비 에너지 효율성을 1.77배 개선했습니다.
- 5. 본 연구는 기초적인 장치 물리학을 강력한 계산 원리로 직접 변환하여 에너지 효율적인 SNN의 새로운 패러다임을 제시합니다.


---

*Generated on 2025-09-24 14:57:40*