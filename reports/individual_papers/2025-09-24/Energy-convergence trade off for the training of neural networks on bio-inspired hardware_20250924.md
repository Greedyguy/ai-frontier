<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:03:42.187723",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Ferroelectric Synaptic Devices",
    "Symmetry Point Shifting",
    "Memristive Devices"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Ferroelectric Synaptic Devices": 0.8,
    "Symmetry Point Shifting": 0.78,
    "Memristive Devices": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "neural network training",
        "canonical": "Neural Network",
        "aliases": [
          "NN training",
          "neural training"
        ],
        "category": "broad_technical",
        "rationale": "Neural Network is a fundamental concept that connects with a wide range of AI and hardware topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "ferroelectric synaptic devices",
        "canonical": "Ferroelectric Synaptic Devices",
        "aliases": [
          "ferroelectric synapses",
          "synaptic devices"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific hardware technology that directly relates to the paper's focus on bio-inspired hardware.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "symmetry point shifting",
        "canonical": "Symmetry Point Shifting",
        "aliases": [
          "symmetry shift",
          "point shifting"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique introduced in the paper that addresses asymmetric updates in neural network training.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "memristive devices",
        "canonical": "Memristive Devices",
        "aliases": [
          "memristors",
          "memristive hardware"
        ],
        "category": "specific_connectable",
        "rationale": "Memristive devices are crucial for understanding the hardware acceleration of neural networks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "experiment",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "neural network training",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ferroelectric synaptic devices",
      "resolved_canonical": "Ferroelectric Synaptic Devices",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "symmetry point shifting",
      "resolved_canonical": "Symmetry Point Shifting",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "memristive devices",
      "resolved_canonical": "Memristive Devices",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Energy-convergence trade off for the training of neural networks on bio-inspired hardware

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18121.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18121](https://arxiv.org/abs/2509.18121)

## 🔗 유사한 논문
- [[2025-09-24/Otters_ An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding_20250924|Otters: An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding]] (85.0% similar)
- [[2025-09-22/Training thermodynamic computers by gradient descent_20250922|Training thermodynamic computers by gradient descent]] (83.5% similar)
- [[2025-09-22/Analog In-memory Training on General Non-ideal Resistive Elements_ The Impact of Response Functions_20250922|Analog In-memory Training on General Non-ideal Resistive Elements: The Impact of Response Functions]] (83.3% similar)
- [[2025-09-23/Elucidating the Design Space of FP4 training_20250923|Elucidating the Design Space of FP4 training]] (82.9% similar)
- [[2025-09-23/Joint Optimization of Memory Frequency, Computing Frequency, Transmission Power and Task Offloading for Energy-efficient DNN Inference_20250923|Joint Optimization of Memory Frequency, Computing Frequency, Transmission Power and Task Offloading for Energy-efficient DNN Inference]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Memristive Devices|Memristive Devices]]
**⚡ Unique Technical**: [[keywords/Ferroelectric Synaptic Devices|Ferroelectric Synaptic Devices]], [[keywords/Symmetry Point Shifting|Symmetry Point Shifting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18121v1 Announce Type: cross 
Abstract: The increasing deployment of wearable sensors and implantable devices is shifting AI processing demands to the extreme edge, necessitating ultra-low power for continuous operation. Inspired by the brain, emerging memristive devices promise to accelerate neural network training by eliminating costly data transfers between compute and memory. Though, balancing performance and energy efficiency remains a challenge. We investigate ferroelectric synaptic devices based on HfO2/ZrO2 superlattices and feed their experimentally measured weight updates into hardware-aware neural network simulations. Across pulse widths from 20 ns to 0.2 ms, shorter pulses lower per-update energy but require more training epochs while still reducing total energy without sacrificing accuracy. Classification accuracy using plain stochastic gradient descent (SGD) is diminished compared to mixed-precision SGD. We analyze the causes and propose a ``symmetry point shifting'' technique, addressing asymmetric updates and restoring accuracy. These results highlight a trade-off among accuracy, convergence speed, and energy use, showing that short-pulse programming with tailored training significantly enhances on-chip learning efficiency.

## 📝 요약

이 논문은 HfO2/ZrO2 초격자 기반의 강유전체 시냅스 소자를 활용하여 에너지 효율적인 신경망 학습을 연구합니다. 실험적으로 측정된 가중치 업데이트를 하드웨어 인식 신경망 시뮬레이션에 적용하여, 20 ns에서 0.2 ms의 펄스 폭을 사용한 경우 짧은 펄스가 에너지를 절약하면서도 정확도를 유지할 수 있음을 발견했습니다. 일반 확률적 경사 하강법(SGD)보다 혼합 정밀도 SGD가 더 높은 정확도를 보였으며, 비대칭 업데이트 문제를 해결하기 위해 '대칭점 이동' 기법을 제안했습니다. 이 연구는 정확도, 수렴 속도, 에너지 사용 간의 균형을 강조하며, 맞춤형 학습을 통한 칩 내 학습 효율성 향상을 보여줍니다.

## 🎯 주요 포인트

- 1. 웨어러블 센서와 이식형 장치의 증가로 AI 처리 수요가 극단적 엣지로 이동하며, 초저전력 연산이 필요해지고 있다.
- 2. HfO2/ZrO2 초격자 기반의 강유전체 시냅스 장치를 활용한 연구에서, 짧은 펄스가 에너지를 절약하면서도 정확도를 유지하는 데 효과적임을 발견했다.
- 3. 평범한 확률적 경사 하강법(SGD)보다 혼합 정밀도 SGD가 더 높은 분류 정확도를 제공한다.
- 4. 비대칭 업데이트 문제를 해결하고 정확도를 회복하기 위해 '대칭점 이동' 기법을 제안했다.
- 5. 짧은 펄스 프로그래밍과 맞춤형 훈련이 칩 내 학습 효율성을 크게 향상시킬 수 있음을 보여준다.


---

*Generated on 2025-09-24 15:03:42*