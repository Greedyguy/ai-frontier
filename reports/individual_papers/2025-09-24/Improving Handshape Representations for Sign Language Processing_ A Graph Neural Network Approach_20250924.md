<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:07:30.973958",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Handshape Recognition",
    "Self-supervised Learning",
    "Anatomically-informed Graph Structures"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Handshape Recognition": 0.77,
    "Self-supervised Learning": 0.8,
    "Anatomically-informed Graph Structures": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Network is central to the paper's methodology and connects well with existing literature on neural networks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Handshape Recognition",
        "canonical": "Handshape Recognition",
        "aliases": [
          "Handshape Identification"
        ],
        "category": "unique_technical",
        "rationale": "This term is unique to sign language processing and is crucial for the paper's focus on improving recognition accuracy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Contrastive Self-supervised Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive learning is a form of self-supervised learning used in the paper to improve model performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Anatomically-informed Graph Structures",
        "canonical": "Anatomically-informed Graph Structures",
        "aliases": [
          "Anatomical Graphs"
        ],
        "category": "unique_technical",
        "rationale": "This concept is specific to the paper's approach, enhancing the model's ability to distinguish subtle handshape variations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "temporal dynamics",
      "recognition accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Handshape Recognition",
      "resolved_canonical": "Handshape Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Anatomically-informed Graph Structures",
      "resolved_canonical": "Anatomically-informed Graph Structures",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Improving Handshape Representations for Sign Language Processing: A Graph Neural Network Approach

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18309.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18309](https://arxiv.org/abs/2509.18309)

## 🔗 유사한 논문
- [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (82.0% similar)
- [[2025-09-23/Cross-Corpus and Cross-domain Handwriting Assessment of NeuroDegenerative Diseases via Time-Series-to-Image Conversion_20250923|Cross-Corpus and Cross-domain Handwriting Assessment of NeuroDegenerative Diseases via Time-Series-to-Image Conversion]] (80.9% similar)
- [[2025-09-23/Emergent 3D Correspondence from Neural Shape Representation_20250923|Emergent 3D Correspondence from Neural Shape Representation]] (80.1% similar)
- [[2025-09-19/Object Recognition and Force Estimation with the GelSight Baby Fin Ray_20250919|Object Recognition and Force Estimation with the GelSight Baby Fin Ray]] (79.3% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Handshape Recognition|Handshape Recognition]], [[keywords/Anatomically-informed Graph Structures|Anatomically-informed Graph Structures]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18309v1 Announce Type: cross 
Abstract: Handshapes serve a fundamental phonological role in signed languages, with American Sign Language employing approximately 50 distinct shapes. However,computational approaches rarely model handshapes explicitly, limiting both recognition accuracy and linguistic analysis.We introduce a novel graph neural network that separates temporal dynamics from static handshape configurations. Our approach combines anatomically-informed graph structures with contrastive learning to address key challenges in handshape recognition, including subtle interclass distinctions and temporal variations. We establish the first benchmark for structured handshape recognition in signing sequences, achieving 46% accuracy across 37 handshape classes (with baseline methods achieving 25%).

## 📝 요약

이 논문은 수어에서 중요한 역할을 하는 손 모양 인식을 개선하기 위해 새로운 그래프 신경망을 제안합니다. 이 모델은 시간적 역학과 정적인 손 모양 구성을 분리하여 처리하며, 해부학적으로 정보를 반영한 그래프 구조와 대조 학습을 결합하여 손 모양 인식의 주요 문제인 미세한 클래스 간 차이와 시간적 변화를 해결합니다. 이를 통해 수어 시퀀스에서 구조화된 손 모양 인식에 대한 첫 번째 벤치마크를 설정하고, 37개의 손 모양 클래스에서 46%의 정확도를 달성했습니다(기존 방법은 25%의 정확도).

## 🎯 주요 포인트

- 1. 수어에서 손 모양은 중요한 음운론적 역할을 하며, 미국 수어는 약 50개의 서로 다른 손 모양을 사용한다.
- 2. 기존의 계산 접근법은 손 모양을 명시적으로 모델링하지 않아 인식 정확도와 언어학적 분석에 한계가 있다.
- 3. 본 연구는 시간적 역학과 정적 손 모양 구성을 분리하는 새로운 그래프 신경망을 소개한다.
- 4. 해부학적으로 정보가 풍부한 그래프 구조와 대조 학습을 결합하여 손 모양 인식의 주요 문제를 해결한다.
- 5. 서명 시퀀스에서 구조화된 손 모양 인식을 위한 첫 번째 벤치마크를 설정하여 37개의 손 모양 클래스에서 46%의 정확도를 달성했다.


---

*Generated on 2025-09-24 15:07:30*