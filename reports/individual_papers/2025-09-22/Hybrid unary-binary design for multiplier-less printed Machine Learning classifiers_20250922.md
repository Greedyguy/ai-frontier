---
keywords:
  - Machine Learning
  - Printed Electronics
  - Multiplier-less Execution
  - Architecture-aware Training
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15316
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:20:16.869909",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Printed Electronics",
    "Multiplier-less Execution",
    "Architecture-aware Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Printed Electronics": 0.7,
    "Multiplier-less Execution": 0.78,
    "Architecture-aware Training": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a fundamental concept that connects this work to a broad range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Printed Electronics",
        "canonical": "Printed Electronics",
        "aliases": [
          "PE"
        ],
        "category": "unique_technical",
        "rationale": "Printed Electronics is a unique aspect of this research, offering a novel approach to circuit design.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multiplier-less execution",
        "canonical": "Multiplier-less Execution",
        "aliases": [
          "Multiplier-free Execution"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's innovation, enabling efficient computation in ML classifiers.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Architecture-aware training",
        "canonical": "Architecture-aware Training",
        "aliases": [
          "Hardware-aware Training"
        ],
        "category": "unique_technical",
        "rationale": "This training method is tailored to the hardware design, enhancing efficiency and performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "circuit design",
      "classifier complexity"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Printed Electronics",
      "resolved_canonical": "Printed Electronics",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multiplier-less execution",
      "resolved_canonical": "Multiplier-less Execution",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Architecture-aware training",
      "resolved_canonical": "Architecture-aware Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Hybrid unary-binary design for multiplier-less printed Machine Learning classifiers

**Korean Title:** 하이브리드 단항-이항 설계: 곱셈기 없는 인쇄형 머신러닝 분류기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15316.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15316](https://arxiv.org/abs/2509.15316)

## 🔗 유사한 논문
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (83.3% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (81.7% similar)
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (80.7% similar)
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (80.0% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**⚡ Unique Technical**: [[keywords/Printed Electronics|Printed Electronics]], [[keywords/Multiplier-less Execution|Multiplier-less Execution]], [[keywords/Architecture-aware Training|Architecture-aware Training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15316v1 Announce Type: new 
Abstract: Printed Electronics (PE) provide a flexible, cost-efficient alternative to silicon for implementing machine learning (ML) circuits, but their large feature sizes limit classifier complexity. Leveraging PE's low fabrication and NRE costs, designers can tailor hardware to specific ML models, simplifying circuit design. This work explores alternative arithmetic and proposes a hybrid unary-binary architecture that removes costly encoders and enables efficient, multiplier-less execution of MLP classifiers. We also introduce architecture-aware training to further improve area and power efficiency. Evaluation on six datasets shows average reductions of 46% in area and 39% in power, with minimal accuracy loss, surpassing other state-of-the-art MLP designs.

## 🔍 Abstract (한글 번역)

arXiv:2509.15316v1 발표 유형: 신규  
초록: 인쇄 전자(Printed Electronics, PE)는 기계 학습(ML) 회로 구현을 위한 실리콘의 유연하고 비용 효율적인 대안을 제공하지만, 큰 특징 크기로 인해 분류기 복잡성이 제한됩니다. PE의 낮은 제조 및 비반복 비용을 활용하여 설계자는 특정 ML 모델에 하드웨어를 맞춤화할 수 있으며, 이를 통해 회로 설계가 단순화됩니다. 본 연구는 대체 산술을 탐구하고 비용이 많이 드는 인코더를 제거하고 MLP 분류기의 효율적이고 곱셈기 없는 실행을 가능하게 하는 하이브리드 유니어리-바이너리 아키텍처를 제안합니다. 또한 영역 및 전력 효율성을 더욱 향상시키기 위해 아키텍처 인식 훈련을 도입합니다. 여섯 개의 데이터셋에 대한 평가 결과, 평균적으로 영역은 46%, 전력은 39% 감소했으며, 정확도 손실은 최소화되어 다른 최첨단 MLP 설계를 능가했습니다.

## 📝 요약

이 논문은 인쇄 전자(PE)를 활용하여 기계 학습(ML) 회로를 구현하는 방법을 제안합니다. PE는 실리콘에 비해 유연하고 비용 효율적이지만, 큰 특징 크기 때문에 분류기 복잡성이 제한됩니다. 저자들은 PE의 낮은 제작 비용과 비반복 비용을 활용하여 특정 ML 모델에 맞춘 하드웨어 설계를 제안합니다. 이 연구에서는 고가의 인코더를 제거하고 곱셈기 없이 MLP 분류기를 효율적으로 실행할 수 있는 하이브리드 유니어리-바이너리 아키텍처를 제안합니다. 또한, 아키텍처 인식 훈련을 도입하여 면적과 전력 효율성을 향상시킵니다. 여섯 개의 데이터셋 평가 결과, 평균적으로 면적은 46%, 전력은 39% 감소하면서도 정확도 손실은 최소화하여, 기존 최첨단 MLP 설계를 능가하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 인쇄 전자 기술은 실리콘보다 유연하고 비용 효율적인 머신 러닝 회로 구현 대안이지만, 큰 특징 크기가 분류기 복잡성을 제한합니다.
- 2. 인쇄 전자의 낮은 제작 및 비반복 비용을 활용하여 특정 머신 러닝 모델에 맞춘 하드웨어 설계가 가능합니다.
- 3. 하이브리드 유니어리-바이너리 아키텍처를 제안하여 비용이 많이 드는 인코더를 제거하고 곱셈기 없는 MLP 분류기 실행을 가능하게 합니다.
- 4. 아키텍처 인식 훈련을 도입하여 면적과 전력 효율성을 더욱 향상시킵니다.
- 5. 여섯 개의 데이터셋 평가에서 평균 46%의 면적 감소와 39%의 전력 감소를 달성하며, 정확도 손실은 최소화되어 다른 최신 MLP 설계를 능가합니다.


---

*Generated on 2025-09-23 10:20:16*