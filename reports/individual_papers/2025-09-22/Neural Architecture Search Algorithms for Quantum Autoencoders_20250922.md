---
keywords:
  - Neural Architecture Search
  - Quantum Autoencoder
  - Quantum Data Compression
  - Quantum Circuit
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15451
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:48:48.508704",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Architecture Search",
    "Quantum Autoencoder",
    "Quantum Data Compression",
    "Quantum Circuit"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Architecture Search": 0.85,
    "Quantum Autoencoder": 0.78,
    "Quantum Data Compression": 0.77,
    "Quantum Circuit": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Architecture Search",
        "canonical": "Neural Architecture Search",
        "aliases": [
          "NAS"
        ],
        "category": "broad_technical",
        "rationale": "Neural Architecture Search is a key method for automating model design, relevant across machine learning and quantum computing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Quantum Autoencoders",
        "canonical": "Quantum Autoencoder",
        "aliases": [
          "Quantum AE"
        ],
        "category": "unique_technical",
        "rationale": "Quantum Autoencoders are a specialized application of quantum circuits, crucial for quantum data compression tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Quantum Data Compression",
        "canonical": "Quantum Data Compression",
        "aliases": [
          "Quantum Compression"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task that demonstrates the application of quantum circuits, linking to broader quantum computing efforts.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Quantum Circuits",
        "canonical": "Quantum Circuit",
        "aliases": [
          "Quantum Circuit Design"
        ],
        "category": "specific_connectable",
        "rationale": "Quantum Circuits are foundational elements in quantum computing, crucial for linking various quantum algorithm designs.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "circuit design effort",
      "quantum task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Architecture Search",
      "resolved_canonical": "Neural Architecture Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Quantum Autoencoders",
      "resolved_canonical": "Quantum Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Quantum Data Compression",
      "resolved_canonical": "Quantum Data Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Quantum Circuits",
      "resolved_canonical": "Quantum Circuit",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Neural Architecture Search Algorithms for Quantum Autoencoders

**Korean Title:** 양자 오토인코더를 위한 신경망 구조 탐색 알고리즘

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15451.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15451](https://arxiv.org/abs/2509.15451)

## 🔗 유사한 논문
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (81.8% similar)
- [[2025-09-22/Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits_20250922|Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits]] (81.4% similar)
- [[2025-09-22/Impact of Single Rotations and Entanglement Topologies in Quantum Neural Networks_20250922|Impact of Single Rotations and Entanglement Topologies in Quantum Neural Networks]] (81.4% similar)
- [[2025-09-22/Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization_20250922|Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization]] (80.8% similar)
- [[2025-09-22/Quantum Generative Adversarial Autoencoders_ Learning latent representations for quantum data generation_20250922|Quantum Generative Adversarial Autoencoders: Learning latent representations for quantum data generation]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Architecture Search|Neural Architecture Search]]
**🔗 Specific Connectable**: [[keywords/Quantum Circuit|Quantum Circuit]]
**⚡ Unique Technical**: [[keywords/Quantum Autoencoder|Quantum Autoencoder]], [[keywords/Quantum Data Compression|Quantum Data Compression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15451v1 Announce Type: cross 
Abstract: The design of quantum circuits is currently driven by the specific objectives of the quantum algorithm in question. This approach thus relies on a significant manual effort by the quantum algorithm designer to design an appropriate circuit for the task. However this approach cannot scale to more complex quantum algorithms in the future without exponentially increasing the circuit design effort and introducing unwanted inductive biases. Motivated by this observation, we propose to automate the process of cicuit design by drawing inspiration from Neural Architecture Search (NAS). In this work, we propose two Quantum-NAS algorithms that aim to find efficient circuits given a particular quantum task. We choose quantum data compression as our driver quantum task and demonstrate the performance of our algorithms by finding efficient autoencoder designs that outperform baselines on three different tasks - quantum data denoising, classical data compression and pure quantum data compression. Our results indicate that quantum NAS algorithms can significantly alleviate the manual effort while delivering performant quantum circuits for any given task.

## 🔍 Abstract (한글 번역)

arXiv:2509.15451v1 발표 유형: 교차  
요약: 양자 회로 설계는 현재 문제의 양자 알고리즘의 특정 목표에 의해 주도되고 있습니다. 이러한 접근 방식은 양자 알고리즘 설계자가 해당 작업에 적합한 회로를 설계하기 위해 상당한 수작업을 필요로 합니다. 그러나 이러한 접근 방식은 미래의 더 복잡한 양자 알고리즘에 대해 회로 설계 노력을 기하급수적으로 증가시키고 원치 않는 귀납적 편향을 도입하지 않고는 확장될 수 없습니다. 이러한 관찰에 영감을 받아, 우리는 Neural Architecture Search (NAS)에서 영감을 얻어 회로 설계 과정을 자동화할 것을 제안합니다. 본 연구에서는 특정 양자 작업에 대해 효율적인 회로를 찾기 위한 두 가지 Quantum-NAS 알고리즘을 제안합니다. 우리는 양자 데이터 압축을 주된 양자 작업으로 선택하고, 세 가지 다른 작업 - 양자 데이터 노이즈 제거, 고전적 데이터 압축 및 순수 양자 데이터 압축 - 에서 기준을 능가하는 효율적인 오토인코더 설계를 찾아내는 우리의 알고리즘 성능을 입증합니다. 우리의 결과는 양자 NAS 알고리즘이 수작업 노력을 크게 줄이면서 주어진 작업에 대해 성능이 뛰어난 양자 회로를 제공할 수 있음을 나타냅니다.

## 📝 요약

이 논문에서는 양자 회로 설계의 자동화를 목표로 하는 두 가지 Quantum-NAS 알고리즘을 제안합니다. 기존의 양자 회로 설계는 수작업에 의존하여 복잡한 알고리즘에 비효율적이었으나, 제안된 알고리즘은 Neural Architecture Search(NAS)를 활용하여 이를 개선합니다. 연구에서는 양자 데이터 압축을 주요 과제로 삼아, 제안된 알고리즘이 양자 데이터 노이즈 제거, 고전 데이터 압축, 순수 양자 데이터 압축 등 세 가지 과제에서 기존 방법보다 우수한 성능을 보임을 입증했습니다. 이 결과는 Quantum-NAS 알고리즘이 수작업을 크게 줄이면서도 효율적인 양자 회로 설계를 가능하게 함을 시사합니다.

## 🎯 주요 포인트

- 1. 현재의 양자 회로 설계는 특정 양자 알고리즘의 목표에 의해 주도되며, 이는 설계자의 수작업에 크게 의존한다.
- 2. 복잡한 양자 알고리즘의 경우, 기존 방법은 회로 설계 노력을 기하급수적으로 증가시키고 원치 않는 편향을 도입할 수 있다.
- 3. Neural Architecture Search (NAS)에서 영감을 받아 양자 회로 설계 과정을 자동화하는 방법을 제안한다.
- 4. 제안된 두 가지 Quantum-NAS 알고리즘은 특정 양자 작업에 대해 효율적인 회로를 찾는 것을 목표로 한다.
- 5. 실험 결과, Quantum-NAS 알고리즘은 수작업을 크게 줄이면서도 주어진 작업에 대해 성능이 뛰어난 양자 회로를 제공할 수 있음을 보여준다.


---

*Generated on 2025-09-23 10:48:48*