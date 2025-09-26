<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:25:42.771897",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Model Kinship",
    "Top-k Greedy Merging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Model Kinship": 0.78,
    "Top-k Greedy Merging": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on model merging and evolution.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Model Kinship",
        "canonical": "Model Kinship",
        "aliases": [
          "Model Relatedness"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept for evaluating model similarity in the context of merging.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Top-k Greedy Merging",
        "canonical": "Top-k Greedy Merging",
        "aliases": [
          "Greedy Merging"
        ],
        "category": "unique_technical",
        "rationale": "Describes a specific strategy proposed in the paper for model merging.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "model evolution",
      "performance improvements",
      "benchmark performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Model Kinship",
      "resolved_canonical": "Model Kinship",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Top-k Greedy Merging",
      "resolved_canonical": "Top-k Greedy Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Exploring Model Kinship for Merging Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.12613.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2410.12613](https://arxiv.org/abs/2410.12613)

## 🔗 유사한 논문
- [[2025-09-24/OptMerge_ Unifying Multimodal LLM Capabilities and Modalities via Model Merging_20250924|OptMerge: Unifying Multimodal LLM Capabilities and Modalities via Model Merging]] (88.7% similar)
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (85.9% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (84.7% similar)
- [[2025-09-18/FroM_ Frobenius Norm-Based Data-Free Adaptive Model Merging_20250918|FroM: Frobenius Norm-Based Data-Free Adaptive Model Merging]] (84.6% similar)
- [[2025-09-23/Probabilistic Token Alignment for Large Language Model Fusion_20250923|Probabilistic Token Alignment for Large Language Model Fusion]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Model Kinship|Model Kinship]], [[keywords/Top-k Greedy Merging|Top-k Greedy Merging]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.12613v3 Announce Type: replace-cross 
Abstract: Model merging has emerged as a key technique for enhancing the capabilities and efficiency of Large Language Models (LLMs). The open-source community has driven model evolution by iteratively merging existing models, yet a principled understanding of the gains and underlying factors in model merging remains limited. In this work, we study model evolution through iterative merging, drawing an analogy to biological evolution, and introduce the concept of model kinship, the degree of similarity or relatedness between LLMs. Through comprehensive empirical analysis, we show that model kinship is closely linked to the performance improvements achieved by merging, providing a useful criterion for selecting candidate models. Building on this insight, we propose a new model merging strategy: Top-k Greedy Merging with Model Kinship, which can improve benchmark performance. Specifically, we discover that incorporating model kinship as a guiding criterion enables continuous merging while mitigating performance degradation caused by local optima, thereby facilitating more effective model evolution. Code is available at https://github.com/zjunlp/ModelKinship.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 성능과 효율성을 향상시키기 위한 모델 병합 기법을 연구합니다. 저자들은 모델 병합을 생물학적 진화에 비유하며, 모델 간 유사성을 나타내는 '모델 친족' 개념을 도입했습니다. 실증 분석을 통해 모델 친족이 병합에 따른 성능 향상과 밀접한 관련이 있음을 밝혀냈으며, 이를 바탕으로 '모델 친족을 고려한 Top-k 탐욕적 병합' 전략을 제안했습니다. 이 전략은 성능 저하를 방지하면서 모델 진화를 촉진할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 모델 병합은 대형 언어 모델(LLMs)의 성능과 효율성을 향상시키는 핵심 기술로 부상하고 있다.
- 2. 모델 친족도는 모델 병합을 통한 성능 향상과 밀접한 관련이 있으며, 후보 모델 선택의 유용한 기준이 된다.
- 3. 모델 친족도를 활용한 Top-k 탐욕적 병합 전략은 벤치마크 성능을 개선할 수 있다.
- 4. 모델 친족도를 기준으로 하면 지역 최적점으로 인한 성능 저하를 완화하면서 지속적인 모델 병합이 가능하다.


---

*Generated on 2025-09-24 14:25:42*