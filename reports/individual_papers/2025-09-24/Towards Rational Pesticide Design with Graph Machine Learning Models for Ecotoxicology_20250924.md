<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:54:31.197950",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Machine Learning",
    "Graph Neural Network",
    "ApisTox",
    "Pesticide Discovery"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Machine Learning": 0.78,
    "Graph Neural Network": 0.82,
    "ApisTox": 0.75,
    "Pesticide Discovery": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Machine Learning",
        "canonical": "Graph Machine Learning",
        "aliases": [
          "Graph ML"
        ],
        "category": "unique_technical",
        "rationale": "It represents a specialized application of machine learning techniques to graph data, crucial for linking advancements in ecotoxicology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "GNNs are pivotal in processing molecular graph data, providing strong links to existing neural network research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "ApisTox",
        "canonical": "ApisTox",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "As the largest dataset on pesticide toxicity to honey bees, it is a unique resource for ecotoxicology research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Pesticide Discovery",
        "canonical": "Pesticide Discovery",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specialized area of research that benefits from linking to broader chemical and ecological studies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "medicinal chemistry",
      "broad evaluation",
      "future work"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Machine Learning",
      "resolved_canonical": "Graph Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "ApisTox",
      "resolved_canonical": "ApisTox",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Pesticide Discovery",
      "resolved_canonical": "Pesticide Discovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Towards Rational Pesticide Design with Graph Machine Learning Models for Ecotoxicology

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18703.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18703](https://arxiv.org/abs/2509.18703)

## 🔗 유사한 논문
- [[2025-09-23/Test-Time Training Scaling Laws for Chemical Exploration in Drug Design_20250923|Test-Time Training Scaling Laws for Chemical Exploration in Drug Design]] (79.3% similar)
- [[2025-09-23/AgriDoctor_ A Multimodal Intelligent Assistant for Agriculture_20250923|AgriDoctor: A Multimodal Intelligent Assistant for Agriculture]] (78.8% similar)
- [[2025-09-24/A deep reinforcement learning platform for antibiotic discovery_20250924|A deep reinforcement learning platform for antibiotic discovery]] (78.7% similar)
- [[2025-09-24/TinyEcoWeedNet_ Edge Efficient Real-Time Aerial Agricultural Weed Detection_20250924|TinyEcoWeedNet: Edge Efficient Real-Time Aerial Agricultural Weed Detection]] (78.6% similar)
- [[2025-09-22/A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction_20250922|A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Graph Machine Learning|Graph Machine Learning]], [[keywords/ApisTox|ApisTox]], [[keywords/Pesticide Discovery|Pesticide Discovery]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18703v1 Announce Type: new 
Abstract: This research focuses on rational pesticide design, using graph machine learning to accelerate the development of safer, eco-friendly agrochemicals, inspired by in silico methods in drug discovery. With an emphasis on ecotoxicology, the initial contributions include the creation of ApisTox, the largest curated dataset on pesticide toxicity to honey bees. We conducted a broad evaluation of machine learning (ML) models for molecular graph classification, including molecular fingerprints, graph kernels, GNNs, and pretrained transformers. The results show that methods successful in medicinal chemistry often fail to generalize to agrochemicals, underscoring the need for domain-specific models and benchmarks. Future work will focus on developing a comprehensive benchmarking suite and designing ML models tailored to the unique challenges of pesticide discovery.

## 📝 요약

이 연구는 그래프 머신러닝을 활용하여 안전하고 친환경적인 농약 개발을 가속화하는 데 중점을 두고 있습니다. 주요 기여로는 꿀벌에 대한 농약 독성을 다룬 최대 규모의 데이터셋인 ApisTox의 구축이 있습니다. 다양한 분자 그래프 분류 머신러닝 모델을 평가한 결과, 의약 화학에서 성공적인 방법들이 농약 분야에서는 일반화되지 않는다는 점을 발견했습니다. 이는 분야별 모델과 벤치마크의 필요성을 강조합니다. 향후 연구는 농약 발견의 고유한 문제를 해결하기 위한 맞춤형 ML 모델 개발에 초점을 맞출 예정입니다.

## 🎯 주요 포인트

- 1. 이 연구는 그래프 머신러닝을 활용하여 안전하고 친환경적인 농약 개발을 가속화하는 데 중점을 두고 있습니다.
- 2. 연구의 초기 기여로 꿀벌에 대한 농약 독성을 다룬 최대 규모의 데이터셋인 ApisTox를 생성했습니다.
- 3. 분자 그래프 분류를 위한 다양한 머신러닝 모델을 평가한 결과, 의약 화학에서 성공적인 방법들이 농약에는 일반화되지 않는다는 것을 발견했습니다.
- 4. 농약 발견의 고유한 도전에 맞춘 머신러닝 모델과 벤치마크의 필요성을 강조하고 있습니다.
- 5. 향후 연구는 포괄적인 벤치마킹 도구 개발과 농약 발견에 특화된 머신러닝 모델 설계에 초점을 맞출 것입니다.


---

*Generated on 2025-09-24 14:54:31*