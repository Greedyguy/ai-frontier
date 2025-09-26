---
keywords:
  - Neural Network
  - Modular Learning Framework
  - Genetic Circuits
  - Modular Identifiability
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19601
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:37:22.589714",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Modular Learning Framework",
    "Genetic Circuits",
    "Modular Identifiability"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Modular Learning Framework": 0.78,
    "Genetic Circuits": 0.8,
    "Modular Identifiability": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "NNET"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the paper's framework and are a key concept in machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Modular Learning Framework",
        "canonical": "Modular Learning Framework",
        "aliases": [
          "Modular Framework"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach proposed in the paper, crucial for linking to modular system design.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Genetic Circuits",
        "canonical": "Genetic Circuits",
        "aliases": [
          "Synthetic Biological Circuits"
        ],
        "category": "specific_connectable",
        "rationale": "Genetic circuits are a specific application area for the proposed framework, offering strong domain-specific links.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Modular Identifiability",
        "canonical": "Modular Identifiability",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is introduced in the paper and is key to understanding the framework's theoretical foundations.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "input/output data",
      "compositional structure"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Network",
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
      "candidate_surface": "Modular Learning Framework",
      "resolved_canonical": "Modular Learning Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Genetic Circuits",
      "resolved_canonical": "Genetic Circuits",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Modular Identifiability",
      "resolved_canonical": "Modular Identifiability",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Modular Machine Learning with Applications to Genetic Circuit Composition

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19601.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19601](https://arxiv.org/abs/2509.19601)

## 🔗 유사한 논문
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (83.1% similar)
- [[2025-09-23/Information-Theoretic Bounds and Task-Centric Learning Complexity for Real-World Dynamic Nonlinear Systems_20250923|Information-Theoretic Bounds and Task-Centric Learning Complexity for Real-World Dynamic Nonlinear Systems]] (81.0% similar)
- [[2025-09-22/Modeling Transformers as complex networks to analyze learning dynamics_20250922|Modeling Transformers as complex networks to analyze learning dynamics]] (81.0% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (80.9% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Genetic Circuits|Genetic Circuits]]
**⚡ Unique Technical**: [[keywords/Modular Learning Framework|Modular Learning Framework]], [[keywords/Modular Identifiability|Modular Identifiability]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19601v1 Announce Type: new 
Abstract: In several applications, including in synthetic biology, one often has input/output data on a system composed of many modules, and although the modules' input/output functions and signals may be unknown, knowledge of the composition architecture can significantly reduce the amount of training data required to learn the system's input/output mapping. Learning the modules' input/output functions is also necessary for designing new systems from different composition architectures. Here, we propose a modular learning framework, which incorporates prior knowledge of the system's compositional structure to (a) identify the composing modules' input/output functions from the system's input/output data and (b) achieve this by using a reduced amount of data compared to what would be required without knowledge of the compositional structure. To achieve this, we introduce the notion of modular identifiability, which allows recovery of modules' input/output functions from a subset of the system's input/output data, and provide theoretical guarantees on a class of systems motivated by genetic circuits. We demonstrate the theory on computational studies showing that a neural network (NNET) that accounts for the compositional structure can learn the composing modules' input/output functions and predict the system's output on inputs outside of the training set distribution. By contrast, a neural network that is agnostic of the structure is unable to predict on inputs that fall outside of the training set distribution. By reducing the need for experimental data and allowing module identification, this framework offers the potential to ease the design of synthetic biological circuits and of multi-module systems more generally.

## 📝 요약

이 논문은 합성 생물학 등 여러 분야에서 모듈로 구성된 시스템의 입력/출력 데이터를 효과적으로 학습하기 위한 모듈러 학습 프레임워크를 제안합니다. 시스템의 구성 구조에 대한 사전 지식을 활용하여 모듈의 입력/출력 함수를 식별하고, 이를 통해 필요한 데이터 양을 줄일 수 있습니다. 저자들은 모듈러 식별 가능성 개념을 도입하여 시스템의 일부 입력/출력 데이터만으로도 모듈의 함수를 복원할 수 있음을 이론적으로 보장합니다. 실험 결과, 구성 구조를 고려한 신경망이 모듈의 입력/출력 함수를 학습하고 훈련 세트 분포 외부의 입력에 대해서도 시스템 출력을 예측할 수 있음을 보여주었습니다. 이 프레임워크는 실험 데이터의 필요성을 줄이고 모듈 식별을 가능하게 하여 합성 생물학적 회로 및 다중 모듈 시스템 설계를 용이하게 할 잠재력을 가집니다.

## 🎯 주요 포인트

- 1. 모듈의 구성 아키텍처에 대한 사전 지식을 활용하여 시스템의 입력/출력 데이터로부터 모듈의 입력/출력 기능을 식별하는 모듈 학습 프레임워크를 제안합니다.
- 2. 모듈 식별 가능성 개념을 도입하여 시스템의 일부 입력/출력 데이터만으로 모듈의 입력/출력 기능을 복구할 수 있도록 합니다.
- 3. 합성 생물학 및 유전자 회로와 같은 응용 분야에서 실험 데이터의 필요성을 줄이고 모듈 식별을 가능하게 하여 새로운 시스템 설계를 용이하게 합니다.
- 4. 구성 구조를 고려한 신경망(NNET)은 학습 세트 분포 외부의 입력에 대해 시스템 출력을 예측할 수 있지만, 구조를 고려하지 않은 신경망은 이를 예측할 수 없습니다.
- 5. 이론적 보장을 제공하여 다양한 시스템에서 모듈의 입력/출력 기능을 학습하고 예측하는 데 기여합니다.


---

*Generated on 2025-09-25 16:37:22*