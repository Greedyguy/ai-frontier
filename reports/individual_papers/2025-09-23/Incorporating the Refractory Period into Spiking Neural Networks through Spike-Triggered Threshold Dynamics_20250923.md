---
keywords:
  - Neural Network
  - Refractory Period
  - Leaky Integrate-and-Fire Model
  - Spike-Triggered Threshold Dynamics
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17769
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:02:41.697187",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Refractory Period",
    "Leaky Integrate-and-Fire Model",
    "Spike-Triggered Threshold Dynamics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "Refractory Period": 0.72,
    "Leaky Integrate-and-Fire Model": 0.75,
    "Spike-Triggered Threshold Dynamics": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Spiking Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "SNNs"
        ],
        "category": "broad_technical",
        "rationale": "Spiking Neural Networks are a specific type of Neural Network, linking to broader neural network concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Refractory Period",
        "canonical": "Refractory Period",
        "aliases": [
          "neuron refractory period"
        ],
        "category": "unique_technical",
        "rationale": "The refractory period is a unique biological mechanism not commonly included in neural network models, offering novel insights.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Leaky Integrate-and-Fire",
        "canonical": "Leaky Integrate-and-Fire Model",
        "aliases": [
          "LIF model"
        ],
        "category": "specific_connectable",
        "rationale": "The LIF model is a foundational concept in spiking neural networks, facilitating connections with other neural modeling techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Spike-Triggered Threshold Dynamics",
        "canonical": "Spike-Triggered Threshold Dynamics",
        "aliases": [
          "threshold dynamics"
        ],
        "category": "unique_technical",
        "rationale": "This concept introduces a novel mechanism for enhancing neuron model accuracy, offering unique technical insights.",
        "novelty_score": 0.82,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
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
      "candidate_surface": "Spiking Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Refractory Period",
      "resolved_canonical": "Refractory Period",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Leaky Integrate-and-Fire",
      "resolved_canonical": "Leaky Integrate-and-Fire Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Spike-Triggered Threshold Dynamics",
      "resolved_canonical": "Spike-Triggered Threshold Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17769.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17769](https://arxiv.org/abs/2509.17769)

## 🔗 유사한 논문
- [[2025-09-23/Dendritic Resonate-and-Fire Neuron for Effective and Efficient Long Sequence Modeling_20250923|Dendritic Resonate-and-Fire Neuron for Effective and Efficient Long Sequence Modeling]] (84.5% similar)
- [[2025-09-23/CSDformer_ A Conversion Method for Fully Spike-Driven Transformer_20250923|CSDformer: A Conversion Method for Fully Spike-Driven Transformer]] (81.9% similar)
- [[2025-09-23/Neurodynamics-Driven Coupled Neural P Systems for Multi-Focus Image Fusion_20250923|Neurodynamics-Driven Coupled Neural P Systems for Multi-Focus Image Fusion]] (81.8% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (81.6% similar)
- [[2025-09-23/Lipschitz-Based Robustness Certification for Recurrent Neural Networks via Convex Relaxation_20250923|Lipschitz-Based Robustness Certification for Recurrent Neural Networks via Convex Relaxation]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Leaky Integrate-and-Fire Model|Leaky Integrate-and-Fire Model]]
**⚡ Unique Technical**: [[keywords/Refractory Period|Refractory Period]], [[keywords/Spike-Triggered Threshold Dynamics|Spike-Triggered Threshold Dynamics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17769v1 Announce Type: new 
Abstract: As the third generation of neural networks, spiking neural networks (SNNs) have recently gained widespread attention for their biological plausibility, energy efficiency, and effectiveness in processing neuromorphic datasets. To better emulate biological neurons, various models such as Integrate-and-Fire (IF) and Leaky Integrate-and-Fire (LIF) have been widely adopted in SNNs. However, these neuron models overlook the refractory period, a fundamental characteristic of biological neurons. Research on excitable neurons reveal that after firing, neurons enter a refractory period during which they are temporarily unresponsive to subsequent stimuli. This mechanism is critical for preventing over-excitation and mitigating interference from aberrant signals. Therefore, we propose a simple yet effective method to incorporate the refractory period into spiking LIF neurons through spike-triggered threshold dynamics, termed RPLIF. Our method ensures that each spike accurately encodes neural information, effectively preventing neuron over-excitation under continuous inputs and interference from anomalous inputs. Incorporating the refractory period into LIF neurons is seamless and computationally efficient, enhancing robustness and efficiency while yielding better performance with negligible overhead. To the best of our knowledge, RPLIF achieves state-of-the-art performance on Cifar10-DVS(82.40%) and N-Caltech101(83.35%) with fewer timesteps and demonstrates superior performance on DVS128 Gesture(97.22%) at low latency.

## 📝 요약

이 논문은 생물학적 신경세포의 불응기를 반영한 스파이킹 신경망(SNN) 모델인 RPLIF를 제안합니다. 기존의 통합-발화(IF) 및 누설 통합-발화(LIF) 모델은 불응기를 고려하지 않아 과도한 흥분을 방지하는 데 한계가 있었습니다. RPLIF는 스파이크 유발 임계값 동역학을 통해 불응기를 통합하여 지속적인 입력과 비정상 입력에 대한 신경 과흥분을 효과적으로 방지합니다. 이 방법은 계산 효율성을 유지하면서도 성능을 향상시킵니다. RPLIF는 Cifar10-DVS(82.40%), N-Caltech101(83.35%)에서 최첨단 성능을 보였으며, DVS128 Gesture(97.22%)에서도 낮은 지연 시간으로 우수한 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. 스파이킹 신경망(SNNs)은 생물학적 타당성, 에너지 효율성, 신경형 데이터셋 처리 효과로 주목받고 있습니다.
- 2. 기존의 신경 모델들은 생물학적 뉴런의 기본 특성인 불응기를 간과하고 있습니다.
- 3. 제안된 RPLIF 방법은 스파이크-트리거 임계값 동역학을 통해 불응기를 통합하여 뉴런의 과도한 흥분을 방지합니다.
- 4. RPLIF는 Cifar10-DVS와 N-Caltech101에서 최첨단 성능을 기록하며, DVS128 Gesture에서 낮은 지연 시간으로 우수한 성능을 보입니다.
- 5. 불응기를 통합한 LIF 뉴런은 계산 효율성을 유지하면서 강력한 성능을 제공합니다.


---

*Generated on 2025-09-24 05:02:41*