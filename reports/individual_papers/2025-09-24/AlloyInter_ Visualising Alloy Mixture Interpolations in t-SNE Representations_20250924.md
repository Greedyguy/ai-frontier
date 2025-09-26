<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:17:59.839934",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Explainable AI",
    "Manifold Learning",
    "Interpolation Techniques",
    "Model Ensemble"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Explainable AI": 0.85,
    "Manifold Learning": 0.78,
    "Interpolation Techniques": 0.72,
    "Model Ensemble": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "eXplainable Artificial Intelligence",
        "canonical": "Explainable AI",
        "aliases": [
          "XAI",
          "Explainable Artificial Intelligence"
        ],
        "category": "broad_technical",
        "rationale": "Explainable AI is crucial for understanding and interpreting machine learning models, enhancing the system's robustness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "manifold learning",
        "canonical": "Manifold Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Manifold learning is a key technique in dimensionality reduction and visualization, relevant to the paper's focus on t-SNE representations.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "interpolation approach",
        "canonical": "Interpolation Techniques",
        "aliases": [
          "interpolation methods"
        ],
        "category": "unique_technical",
        "rationale": "Interpolation techniques are central to the proposed system, allowing exploration of mixture ratios and output parameters.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "learned model ensemble",
        "canonical": "Model Ensemble",
        "aliases": [
          "ensemble learning"
        ],
        "category": "specific_connectable",
        "rationale": "Model ensembles enhance predictive performance and are integral to the system's interpolation approach.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "SciVis Contest 2025",
      "input mixtures",
      "output parameters space"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "eXplainable Artificial Intelligence",
      "resolved_canonical": "Explainable AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "manifold learning",
      "resolved_canonical": "Manifold Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "interpolation approach",
      "resolved_canonical": "Interpolation Techniques",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "learned model ensemble",
      "resolved_canonical": "Model Ensemble",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# AlloyInter: Visualising Alloy Mixture Interpolations in t-SNE Representations

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19202.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19202](https://arxiv.org/abs/2509.19202)

## 🔗 유사한 논문
- [[2025-09-22/Combo_ Co-speech holistic 3D human motion generation and efficient customizable adaptation in harmony_20250922|Combo: Co-speech holistic 3D human motion generation and efficient customizable adaptation in harmony]] (77.4% similar)
- [[2025-09-24/Towards Causal Representation Learning with Observable Sources as Auxiliaries_20250924|Towards Causal Representation Learning with Observable Sources as Auxiliaries]] (76.9% similar)
- [[2025-09-24/YAC_ Bridging Natural Language and Interactive Visual Exploration with Generative AI for Biomedical Data Discovery_20250924|YAC: Bridging Natural Language and Interactive Visual Exploration with Generative AI for Biomedical Data Discovery]] (76.9% similar)
- [[2025-09-23/Alpha-GPT_ Human-AI Interactive Alpha Mining for Quantitative Investment_20250923|Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment]] (76.6% similar)
- [[2025-09-23/Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation_20250923|Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation]] (76.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Explainable AI|Explainable AI]]
**🔗 Specific Connectable**: [[keywords/Manifold Learning|Manifold Learning]], [[keywords/Model Ensemble|Model Ensemble]]
**⚡ Unique Technical**: [[keywords/Interpolation Techniques|Interpolation Techniques]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19202v1 Announce Type: cross 
Abstract: This entry description proposes AlloyInter, a novel system to enable joint exploration of input mixtures and output parameters space in the context of the SciVis Contest 2025. We propose an interpolation approach, guided by eXplainable Artificial Intelligence (XAI) based on a learned model ensemble that allows users to discover input mixture ratios by specifying output parameter goals that can be iteratively adjusted and improved towards a goal. We strengthen the capabilities of our system by building upon prior research within the robustness of XAI, as well as combining well-established techniques like manifold learning with interpolation approaches.

## 📝 요약

이 논문은 SciVis Contest 2025를 위한 새로운 시스템인 AlloyInter를 제안합니다. AlloyInter는 입력 혼합물과 출력 매개변수 공간을 공동으로 탐색할 수 있도록 설계되었습니다. 이 시스템은 설명 가능한 인공지능(XAI)을 기반으로 한 학습 모델 앙상블을 활용하여, 사용자가 원하는 출력 목표를 설정하고 이를 통해 입력 혼합 비율을 발견할 수 있도록 합니다. 또한, 기존의 XAI 연구와 매니폴드 학습 등의 기법을 결합하여 시스템의 강력한 기능을 강화하였습니다. 주요 기여는 사용자가 목표에 맞춰 출력 매개변수를 조정하고 개선할 수 있는 인터폴레이션 접근 방식을 제시한 것입니다.

## 🎯 주요 포인트

- 1. AlloyInter는 SciVis Contest 2025의 입력 혼합물과 출력 매개변수 공간을 공동으로 탐색할 수 있는 시스템입니다.
- 2. 사용자는 출력 매개변수 목표를 지정하여 입력 혼합 비율을 발견할 수 있으며, 이는 반복적으로 조정 및 개선될 수 있습니다.
- 3. 이 시스템은 설명 가능한 인공지능(XAI) 기반의 학습된 모델 앙상블을 활용하여 인터폴레이션 접근 방식을 제안합니다.
- 4. XAI의 견고성을 기반으로 하고, 매니폴드 학습과 같은 잘 확립된 기법을 인터폴레이션 접근 방식과 결합하여 시스템의 기능을 강화합니다.


---

*Generated on 2025-09-24 15:17:59*