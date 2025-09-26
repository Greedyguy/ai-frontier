---
keywords:
  - Generative Quantum Eigensolver
  - Unitary Coupled Cluster with Singles and Doubles
  - SMILES Representation
  - Transfer Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19715
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:46:19.242998",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Quantum Eigensolver",
    "Unitary Coupled Cluster with Singles and Doubles",
    "SMILES Representation",
    "Transfer Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generative Quantum Eigensolver": 0.8,
    "Unitary Coupled Cluster with Singles and Doubles": 0.75,
    "SMILES Representation": 0.79,
    "Transfer Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Generative Quantum Eigensolver",
        "canonical": "Generative Quantum Eigensolver",
        "aliases": [
          "GQE"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel integration of generative models with quantum eigensolvers, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Unitary Coupled Cluster with Singles and Doubles",
        "canonical": "Unitary Coupled Cluster with Singles and Doubles",
        "aliases": [
          "UCCSD"
        ],
        "category": "unique_technical",
        "rationale": "A key quantum chemistry method discussed in the paper, relevant for constructing quantum operators.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "SMILES representation",
        "canonical": "SMILES Representation",
        "aliases": [
          "SMILES"
        ],
        "category": "specific_connectable",
        "rationale": "Links computational chemistry with quantum operator construction, bridging two domains.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Transfer Learning",
        "canonical": "Transfer Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental machine learning concept applied to quantum operator construction in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "quantum operators",
      "molecular systems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Generative Quantum Eigensolver",
      "resolved_canonical": "Generative Quantum Eigensolver",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Unitary Coupled Cluster with Singles and Doubles",
      "resolved_canonical": "Unitary Coupled Cluster with Singles and Doubles",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "SMILES representation",
      "resolved_canonical": "SMILES Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Transfer Learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SMILES-Inspired Transfer Learning for Quantum Operators in Generative Quantum Eigensolver

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19715.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19715](https://arxiv.org/abs/2509.19715)

## 🔗 유사한 논문
- [[2025-09-22/Quantum Generative Adversarial Autoencoders_ Learning latent representations for quantum data generation_20250922|Quantum Generative Adversarial Autoencoders: Learning latent representations for quantum data generation]] (83.8% similar)
- [[2025-09-17/Learning quantum many-body data locally_ A provably scalable framework_20250917|Learning quantum many-body data locally: A provably scalable framework]] (83.4% similar)
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (82.0% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (81.8% similar)
- [[2025-09-22/Training Variational Quantum Circuits Using Particle Swarm Optimization_20250922|Training Variational Quantum Circuits Using Particle Swarm Optimization]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transfer Learning|Transfer Learning]]
**🔗 Specific Connectable**: [[keywords/SMILES Representation|SMILES Representation]]
**⚡ Unique Technical**: [[keywords/Generative Quantum Eigensolver|Generative Quantum Eigensolver]], [[keywords/Unitary Coupled Cluster with Singles and Doubles|Unitary Coupled Cluster with Singles and Doubles]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19715v1 Announce Type: cross 
Abstract: Given the inherent limitations of traditional Variational Quantum Eigensolver(VQE) algorithms, the integration of deep generative models into hybrid quantum-classical frameworks, specifically the Generative Quantum Eigensolver(GQE), represents a promising innovative approach. However, taking the Unitary Coupled Cluster with Singles and Doubles(UCCSD) ansatz which is widely used in quantum chemistry as an example, different molecular systems require constructions of distinct quantum operators. Considering the similarity of different molecules, the construction of quantum operators utilizing the similarity can reduce the computational cost significantly. Inspired by the SMILES representation method in computational chemistry, we developed a text-based representation approach for UCCSD quantum operators by leveraging the inherent representational similarities between different molecular systems. This framework explores text pattern similarities in quantum operators and employs text similarity metrics to establish a transfer learning framework. Our approach with a naive baseline setting demonstrates knowledge transfer between different molecular systems for ground-state energy calculations within the GQE paradigm. This discovery offers significant benefits for hybrid quantum-classical computation of molecular ground-state energies, substantially reducing computational resource requirements.

## 📝 요약

전통적인 변분 양자 고유값 솔버(VQE) 알고리즘의 한계를 극복하기 위해, 하이브리드 양자-고전적 프레임워크에 딥 생성 모델을 통합한 생성 양자 고유값 솔버(GQE)가 제안되었습니다. 특히, 양자 화학에서 널리 사용되는 유니터리 결합 클러스터(UCCSD) 앤자츠를 예로 들면, 서로 다른 분자 시스템은 각기 다른 양자 연산자 구성이 필요합니다. 본 연구는 SMILES 표현법에서 영감을 받아, UCCSD 양자 연산자를 텍스트 기반으로 표현하여 분자 시스템 간의 유사성을 활용한 전이 학습 프레임워크를 개발하였습니다. 이 접근법은 분자 시스템 간의 지식 전이를 통해 GQE 패러다임 내에서 기저 상태 에너지 계산의 계산 자원 요구를 크게 줄일 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존 VQE 알고리즘의 한계를 극복하기 위해 GQE를 활용한 하이브리드 양자-고전적 프레임워크가 제안되었습니다.
- 2. UCCSD 앤자츠를 사용하는 경우, 서로 다른 분자 시스템에 대해 개별적인 양자 연산자 구성이 필요합니다.
- 3. 분자 간의 유사성을 활용하여 양자 연산자를 구성하면 계산 비용을 크게 줄일 수 있습니다.
- 4. SMILES 표현법에 영감을 받아 UCCSD 양자 연산자의 텍스트 기반 표현 방법을 개발하였습니다.
- 5. 제안된 방법은 GQE 패러다임 내에서 분자 시스템 간의 지식 전이를 통해 계산 자원 요구를 크게 줄입니다.


---

*Generated on 2025-09-25 15:46:19*