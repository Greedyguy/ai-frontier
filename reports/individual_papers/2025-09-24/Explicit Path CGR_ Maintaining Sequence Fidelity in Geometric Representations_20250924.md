<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:50:51.106062",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Chaos Game Representation",
    "Biological Sequence Analysis",
    "Sequence Recovery",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Chaos Game Representation": 0.8,
    "Biological Sequence Analysis": 0.75,
    "Sequence Recovery": 0.7,
    "Deep Learning": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Chaos Game Representation",
        "canonical": "Chaos Game Representation",
        "aliases": [
          "CGR"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific method central to the paper's contribution, offering a unique approach to biological sequence analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "biological sequence analysis",
        "canonical": "Biological Sequence Analysis",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a key application area for the method, linking it to broader bioinformatics research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "sequence recovery",
        "canonical": "Sequence Recovery",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The ability to recover sequences is a unique feature of the proposed method, distinguishing it from traditional CGR.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "deep learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep learning is relevant due to the method's potential for generating feature-rich images suitable for such models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Chaos Game Representation",
      "resolved_canonical": "Chaos Game Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "biological sequence analysis",
      "resolved_canonical": "Biological Sequence Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "sequence recovery",
      "resolved_canonical": "Sequence Recovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "deep learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Explicit Path CGR: Maintaining Sequence Fidelity in Geometric Representations

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18408.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18408](https://arxiv.org/abs/2509.18408)

## 🔗 유사한 논문
- [[2025-09-23/RLGF_ Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation_20250923|RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation]] (78.7% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (78.5% similar)
- [[2025-09-23/Preconditioned Deformation Grids_20250923|Preconditioned Deformation Grids]] (78.3% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (78.2% similar)
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Biological Sequence Analysis|Biological Sequence Analysis]]
**⚡ Unique Technical**: [[keywords/Chaos Game Representation|Chaos Game Representation]], [[keywords/Sequence Recovery|Sequence Recovery]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18408v1 Announce Type: new 
Abstract: We present a novel information-preserving Chaos Game Representation (CGR) method, also called Reverse-CGR (R-CGR), for biological sequence analysis that addresses the fundamental limitation of traditional CGR approaches - the loss of sequence information during geometric mapping. Our method introduces complete sequence recovery through explicit path encoding combined with rational arithmetic precision control, enabling perfect sequence reconstruction from stored geometric traces. Unlike purely geometric approaches, our reversibility is achieved through comprehensive path storage that maintains both positional and character information at each step. We demonstrate the effectiveness of R-CGR on biological sequence classification tasks, achieving competitive performance compared to traditional sequence-based methods while providing interpretable geometric visualizations. The approach generates feature-rich images suitable for deep learning while maintaining complete sequence information through explicit encoding, opening new avenues for interpretable bioinformatics analysis where both accuracy and sequence recovery are essential.

## 📝 요약

이 논문은 생물학적 서열 분석을 위한 새로운 정보 보존 혼돈 게임 표현(CGR) 방법인 역-CGR(R-CGR)을 제안합니다. 기존 CGR 방법의 한계인 서열 정보 손실 문제를 해결하기 위해, 경로 인코딩과 유리수 산술 정밀도 제어를 통해 완전한 서열 복구를 가능하게 합니다. R-CGR은 위치와 문자 정보를 모두 유지하는 포괄적인 경로 저장을 통해 서열 복원성을 확보합니다. 생물학적 서열 분류 작업에서 R-CGR은 전통적인 서열 기반 방법과 비교해 경쟁력 있는 성능을 보이며, 해석 가능한 기하학적 시각화를 제공합니다. 이 접근법은 심층 학습에 적합한 특징이 풍부한 이미지를 생성하면서도 명시적 인코딩을 통해 완전한 서열 정보를 유지하여, 정확성과 서열 복구가 중요한 해석 가능한 생물정보학 분석의 새로운 가능성을 열어줍니다.

## 🎯 주요 포인트

- 1. 새로운 정보 보존 혼돈 게임 표현(CGR) 방법인 Reverse-CGR(R-CGR)을 제안하여 전통적인 CGR의 한계인 시퀀스 정보 손실 문제를 해결합니다.
- 2. R-CGR은 경로 저장을 통해 위치 및 문자 정보를 유지하여 완전한 시퀀스 복구를 가능하게 합니다.
- 3. 생물학적 시퀀스 분류 작업에서 R-CGR은 전통적인 시퀀스 기반 방법과 경쟁력 있는 성능을 보여주며 해석 가능한 기하학적 시각화를 제공합니다.
- 4. 이 방법은 심층 학습에 적합한 특징이 풍부한 이미지를 생성하면서 명시적 인코딩을 통해 완전한 시퀀스 정보를 유지합니다.
- 5. 정확성과 시퀀스 복구가 중요한 해석 가능한 생물정보학 분석의 새로운 가능성을 열어줍니다.


---

*Generated on 2025-09-24 14:50:51*