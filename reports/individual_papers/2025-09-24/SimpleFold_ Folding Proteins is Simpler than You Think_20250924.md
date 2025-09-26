<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:52:42.333940",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Protein Folding",
    "Generative Flow-Matching",
    "Adaptive Layers"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Protein Folding": 0.8,
    "Generative Flow-Matching": 0.78,
    "Adaptive Layers": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer blocks",
        "canonical": "Transformer",
        "aliases": [
          "Transformer architecture"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in deep learning, relevant for linking to other models using similar structures.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Protein folding",
        "canonical": "Protein Folding",
        "aliases": [
          "Protein structure prediction"
        ],
        "category": "unique_technical",
        "rationale": "Protein folding is a specific domain application that connects to bioinformatics and computational biology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Generative flow-matching objective",
        "canonical": "Generative Flow-Matching",
        "aliases": [
          "Flow-matching objective"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel training objective that could link to other generative modeling techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adaptive layers",
        "canonical": "Adaptive Layers",
        "aliases": [
          "Adaptive neural layers"
        ],
        "category": "specific_connectable",
        "rationale": "Adaptive layers are a specific architectural feature that can link to discussions on model flexibility and efficiency.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "SimpleFold",
      "state-of-the-art baselines"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer blocks",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Protein folding",
      "resolved_canonical": "Protein Folding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Generative flow-matching objective",
      "resolved_canonical": "Generative Flow-Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adaptive layers",
      "resolved_canonical": "Adaptive Layers",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SimpleFold: Folding Proteins is Simpler than You Think

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18480.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18480](https://arxiv.org/abs/2509.18480)

## 🔗 유사한 논문
- [[2025-09-22/Monte Carlo Tree Diffusion with Multiple Experts for Protein Design_20250922|Monte Carlo Tree Diffusion with Multiple Experts for Protein Design]] (82.4% similar)
- [[2025-09-22/ProFusion_ 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images_20250922|ProFusion: 3D Reconstruction of Protein Complex Structures from Multi-view AFM Images]] (81.4% similar)
- [[2025-09-23/AI-based Methods for Simulating, Sampling, and Predicting Protein Ensembles_20250923|AI-based Methods for Simulating, Sampling, and Predicting Protein Ensembles]] (80.0% similar)
- [[2025-09-24/THFlow_ A Temporally Hierarchical Flow Matching Framework for 3D Peptide Design_20250924|THFlow: A Temporally Hierarchical Flow Matching Framework for 3D Peptide Design]] (79.6% similar)
- [[2025-09-23/A Closer Look at Model Collapse_ From a Generalization-to-Memorization Perspective_20250923|A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Adaptive Layers|Adaptive Layers]]
**⚡ Unique Technical**: [[keywords/Protein Folding|Protein Folding]], [[keywords/Generative Flow-Matching|Generative Flow-Matching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18480v1 Announce Type: new 
Abstract: Protein folding models have achieved groundbreaking results typically via a combination of integrating domain knowledge into the architectural blocks and training pipelines. Nonetheless, given the success of generative models across different but related problems, it is natural to question whether these architectural designs are a necessary condition to build performant models. In this paper, we introduce SimpleFold, the first flow-matching based protein folding model that solely uses general purpose transformer blocks. Protein folding models typically employ computationally expensive modules involving triangular updates, explicit pair representations or multiple training objectives curated for this specific domain. Instead, SimpleFold employs standard transformer blocks with adaptive layers and is trained via a generative flow-matching objective with an additional structural term. We scale SimpleFold to 3B parameters and train it on approximately 9M distilled protein structures together with experimental PDB data. On standard folding benchmarks, SimpleFold-3B achieves competitive performance compared to state-of-the-art baselines, in addition SimpleFold demonstrates strong performance in ensemble prediction which is typically difficult for models trained via deterministic reconstruction objectives. Due to its general-purpose architecture, SimpleFold shows efficiency in deployment and inference on consumer-level hardware. SimpleFold challenges the reliance on complex domain-specific architectures designs in protein folding, opening up an alternative design space for future progress.

## 📝 요약

이 논문에서는 SimpleFold라는 새로운 단백질 접힘 모델을 소개합니다. SimpleFold는 일반적인 트랜스포머 블록만을 사용하여, 복잡한 도메인 지식 없이도 뛰어난 성능을 발휘합니다. 기존 모델들이 삼각형 업데이트, 명시적 쌍 표현, 다중 학습 목표 등 복잡한 모듈을 사용하는 반면, SimpleFold는 적응형 레이어와 구조적 요소를 포함한 생성적 흐름-매칭 목표를 사용하여 학습됩니다. 3억 개의 파라미터로 확장된 SimpleFold는 약 900만 개의 단백질 구조와 실험적 PDB 데이터를 기반으로 훈련되었습니다. 표준 접힘 벤치마크에서 최첨단 모델과 경쟁력 있는 성능을 보이며, 특히 앙상블 예측에서 강력한 성능을 발휘합니다. SimpleFold는 복잡한 도메인-특정 아키텍처에 의존하지 않고, 일반적인 아키텍처로 소비자 수준의 하드웨어에서도 효율적인 배포와 추론이 가능합니다. 이를 통해 단백질 접힘 모델 설계에서 새로운 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. SimpleFold는 일반적인 트랜스포머 블록만을 사용하여 단백질 접힘 모델을 구현한 최초의 흐름 매칭 기반 모델입니다.
- 2. SimpleFold는 기존의 복잡한 도메인 특화 아키텍처 대신 적응형 레이어와 생성적 흐름 매칭 목표를 사용하여 훈련됩니다.
- 3. SimpleFold-3B는 약 9백만 개의 증류된 단백질 구조와 실험적 PDB 데이터를 통해 훈련되어, 표준 접힘 벤치마크에서 최첨단 기준과 경쟁력 있는 성능을 보입니다.
- 4. SimpleFold는 일반적인 아키텍처 덕분에 소비자 수준의 하드웨어에서도 효율적인 배포 및 추론이 가능합니다.
- 5. SimpleFold는 단백질 접힘에서 복잡한 도메인 특화 아키텍처에 대한 의존성을 도전하며, 미래 발전을 위한 대안적 설계 공간을 열어줍니다.


---

*Generated on 2025-09-24 14:52:42*