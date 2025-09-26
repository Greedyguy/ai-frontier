---
keywords:
  - Quantum Agnostic Boosting
  - Depth-3 Circuits
  - Quantum Agnostic Learning
  - Probably Approximately Correct Model
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.14461
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:41:05.620833",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantum Agnostic Boosting",
    "Depth-3 Circuits",
    "Quantum Agnostic Learning",
    "Probably Approximately Correct Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quantum Agnostic Boosting": 0.8,
    "Depth-3 Circuits": 0.75,
    "Quantum Agnostic Learning": 0.78,
    "Probably Approximately Correct Model": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "quantum agnostic boosting",
        "canonical": "Quantum Agnostic Boosting",
        "aliases": [
          "quantum boosting",
          "agnostic boosting"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, crucial for linking advancements in quantum learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "depth-3 circuits",
        "canonical": "Depth-3 Circuits",
        "aliases": [
          "3-layer circuits",
          "three-layer circuits"
        ],
        "category": "unique_technical",
        "rationale": "Depth-3 circuits are central to the paper's focus on circuit learning, providing a specific technical target.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "quantum agnostic learning",
        "canonical": "Quantum Agnostic Learning",
        "aliases": [
          "agnostic quantum learning"
        ],
        "category": "unique_technical",
        "rationale": "This concept is pivotal to the paper's exploration of learning models using quantum states.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "PAC model",
        "canonical": "Probably Approximately Correct Model",
        "aliases": [
          "PAC learning",
          "PAC framework"
        ],
        "category": "broad_technical",
        "rationale": "The PAC model is a foundational concept in learning theory, relevant for connecting to broader machine learning discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "function class",
      "decision trees",
      "DNF formulas"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "quantum agnostic boosting",
      "resolved_canonical": "Quantum Agnostic Boosting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "depth-3 circuits",
      "resolved_canonical": "Depth-3 Circuits",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "quantum agnostic learning",
      "resolved_canonical": "Quantum Agnostic Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "PAC model",
      "resolved_canonical": "Probably Approximately Correct Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Efficiently learning depth-3 circuits via quantum agnostic boosting

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14461.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.14461](https://arxiv.org/abs/2509.14461)

## 🔗 유사한 논문
- [[2025-09-17/Efficiently learning depth-3 circuits via quantum agnostic boosting_20250917|Efficiently learning depth-3 circuits via quantum agnostic boosting]] (96.6% similar)
- [[2025-09-22/Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits_20250922|Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits]] (82.4% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (80.2% similar)
- [[2025-09-22/Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization_20250922|Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization]] (79.6% similar)
- [[2025-09-24/Re-uploading quantum data_ A universal function approximator for quantum inputs_20250924|Re-uploading quantum data: A universal function approximator for quantum inputs]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Probably Approximately Correct Model|Probably Approximately Correct Model]]
**⚡ Unique Technical**: [[keywords/Quantum Agnostic Boosting|Quantum Agnostic Boosting]], [[keywords/Depth-3 Circuits|Depth-3 Circuits]], [[keywords/Quantum Agnostic Learning|Quantum Agnostic Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14461v2 Announce Type: replace-cross 
Abstract: We initiate the study of quantum agnostic learning of phase states with respect to a function class $\mathsf{C}\subseteq \{c:\{0,1\}^n\rightarrow \{0,1\}\}$: given copies of an unknown $n$-qubit state $|\psi\rangle$ which has fidelity $\textsf{opt}$ with a phase state $|\phi_c\rangle=\frac{1}{\sqrt{2^n}}\sum_{x\in \{0,1\}^n}(-1)^{c(x)}|x\rangle$ for some $c\in \mathsf{C}$, output $|\phi\rangle$ which has fidelity $|\langle \phi | \psi \rangle|^2 \geq \textsf{opt}-\varepsilon$. To this end, we give agnostic learning protocols for the following classes: (i) Size-$t$ decision trees which runs in time $\textsf{poly}(n,t,1/\varepsilon)$. This also implies $k$-juntas can be agnostically learned in time $\textsf{poly}(n,2^k,1/\varepsilon)$. (ii) $s$-term DNF formulas in time $\textsf{poly}(n,(s/\varepsilon)^{\log \log (s/\varepsilon) \cdot \log(1/\varepsilon)})$.
  Our main technical contribution is a quantum agnostic boosting protocol which converts a weak agnostic learner, which outputs a parity state $|\phi\rangle$ such that $|\langle \phi|\psi\rangle|^2\geq \textsf{opt}/\textsf{poly}(n)$, into a strong learner which outputs a superposition of parity states $|\phi'\rangle$ such that $|\langle \phi'|\psi\rangle|^2\geq \textsf{opt} - \varepsilon$.
  Using quantum agnostic boosting, we obtain a $n^{O(\log \log n \cdot \log(1/\varepsilon))}$-time algorithm for learning $\textsf{poly}(n)$-sized depth-$3$ circuits (consisting of $\textsf{AND}$, $\textsf{OR}$, $\textsf{NOT}$ gates) in the uniform $\textsf{PAC}$ model given quantum examples, which is near-polynomial time for constant $\varepsilon$. Classically, obtaining an algorithm with a similar complexity has been an open question in the $\textsf{PAC}$ model and our work answers this given quantum examples.

## 📝 요약

이 논문은 함수 클래스 $\mathsf{C}$에 대한 위상 상태의 양자 불가지 학습을 연구합니다. 주어진 $n$-큐빗 상태 $|\psi\rangle$가 위상 상태 $|\phi_c\rangle$와의 충실도가 $\textsf{opt}$일 때, 충실도가 $\textsf{opt}-\varepsilon$ 이상인 상태 $|\phi\rangle$를 출력하는 방법을 제안합니다. 주요 기여는 다음과 같습니다: (i) 크기-$t$ 결정 트리를 다루는 불가지 학습 프로토콜을 제시하여, $k$-juntas를 다항 시간 내에 학습할 수 있음을 보여줍니다. (ii) $s$-항 DNF 공식을 다항 시간 내에 학습할 수 있는 방법을 제안합니다. 핵심 기술적 기여는 약한 불가지 학습자를 강한 학습자로 변환하는 양자 불가지 부스팅 프로토콜입니다. 이를 통해 양자 예제를 사용하여 깊이-3 회로를 거의 다항 시간 내에 학습하는 알고리즘을 개발하였으며, 이는 고전적 PAC 모델에서 해결되지 않았던 문제를 해결합니다.

## 🎯 주요 포인트

- 1. 우리는 함수 클래스 $\mathsf{C}$에 대한 위상 상태의 양자 불가지 학습을 연구하여, 주어진 $n$-큐빗 상태 $|\psi\rangle$의 위상 상태 $|\phi_c\rangle$와의 충실도가 $\textsf{opt}$인 경우, 충실도가 $\textsf{opt}-\varepsilon$ 이상인 상태 $|\phi\rangle$를 출력하는 문제를 다룹니다.
- 2. 크기-$t$ 결정 트리에 대한 불가지 학습 프로토콜을 제시하며, 이는 $k$-juntas를 시간 $\textsf{poly}(n,2^k,1/\varepsilon)$에 불가지 학습할 수 있음을 의미합니다.
- 3. $s$-항 DNF 공식에 대해 시간 $\textsf{poly}(n,(s/\varepsilon)^{\log \log (s/\varepsilon) \cdot \log(1/\varepsilon)})$에 불가지 학습이 가능합니다.
- 4. 주요 기술적 기여는 약한 불가지 학습자를 강한 학습자로 변환하는 양자 불가지 부스팅 프로토콜로, 이는 충실도가 $\textsf{opt}/\textsf{poly}(n)$ 이상인 경우를 $\textsf{opt} - \varepsilon$ 이상으로 향상시킵니다.
- 5. 양자 예제를 사용하여 깊이-3 회로를 학습하는 $n^{O(\log \log n \cdot \log(1/\varepsilon))}$-시간 알고리즘을 얻었으며, 이는 고전적으로는 열린 문제였던 유사한 복잡도의 알고리즘을 양자 예제를 통해 해결합니다.


---

*Generated on 2025-09-26 08:41:05*