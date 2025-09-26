<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:39:36.741679",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Well-Logs Foundation Model",
    "Self-supervised Learning",
    "Few-Shot Learning",
    "Porosity Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Well-Logs Foundation Model": 0.78,
    "Self-supervised Learning": 0.82,
    "Few-Shot Learning": 0.8,
    "Porosity Estimation": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Well-Logs Foundation Model",
        "canonical": "Well-Logs Foundation Model",
        "aliases": [
          "WLFM"
        ],
        "category": "unique_technical",
        "rationale": "This model is a novel approach specific to geological interpretation, offering new connections in geological AI research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Self-supervised pretraining",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing self-supervised learning techniques, enhancing connections with similar methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Few-shot fine-tuning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "few-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the growing body of work on few-shot learning, relevant for model adaptation.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Porosity estimation",
        "canonical": "Porosity Estimation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific application in geological interpretation, linking to subsurface characterization studies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Well-Logs Foundation Model",
      "resolved_canonical": "Well-Logs Foundation Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Self-supervised pretraining",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Few-shot fine-tuning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Porosity estimation",
      "resolved_canonical": "Porosity Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# WLFM: A Well-Logs Foundation Model for Multi-Task and Cross-Well Geological Interpretation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18152.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18152](https://arxiv.org/abs/2509.18152)

## 🔗 유사한 논문
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.4% similar)
- [[2025-09-22/Foundation Models as World Models_ A Foundational Study in Text-Based GridWorlds_20250922|Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds]] (81.4% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (80.0% similar)
- [[2025-09-23/WISE_ Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification_20250923|WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification]] (79.8% similar)
- [[2025-09-23/LoFT_ Parameter-Efficient Fine-Tuning for Long-tailed Semi-Supervised Learning in Open-World Scenarios_20250923|LoFT: Parameter-Efficient Fine-Tuning for Long-tailed Semi-Supervised Learning in Open-World Scenarios]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Well-Logs Foundation Model|Well-Logs Foundation Model]], [[keywords/Porosity Estimation|Porosity Estimation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18152v1 Announce Type: cross 
Abstract: Well-log interpretation is fundamental for subsurface characterization but remains challenged by heterogeneous tool responses, noisy signals, and limited labels. We propose WLFM, a foundation model pretrained on multi-curve logs from 1200 wells, comprising three stages: tokenization of log patches into geological tokens, self-supervised pretraining with masked-token modeling and stratigraphy-aware contrastive learning, and multi-task adaptation with few-shot fine-tuning. WLFM consistently outperforms state-of-the-art baselines, achieving 0.0041 MSE in porosity estimation and 74.13\% accuracy in lithology classification, while WLFM-Finetune further improves to 0.0038 MSE and 78.10\% accuracy. Beyond predictive accuracy, WLFM exhibits emergent layer-awareness, learns a reusable geological vocabulary, and reconstructs masked curves with reasonable fidelity, though systematic offsets are observed in shallow and ultra-deep intervals. Although boundary detection is not explicitly evaluated here, clustering analyses suggest strong potential for future extension. These results establish WLFM as a scalable, interpretable, and transferable backbone for geological AI, with implications for multi-modal integration of logs, seismic, and textual data.

## 📝 요약

이 논문에서는 지하층 해석을 위한 새로운 모델인 WLFM을 제안합니다. WLFM은 1200개의 유정에서 수집한 다중 곡선 로그 데이터를 기반으로 사전 학습된 모델로, 세 가지 단계로 구성됩니다: 로그 패치를 지질학적 토큰으로 변환하는 토큰화, 마스크된 토큰 모델링과 층서학 인식 대조 학습을 통한 자기 지도 사전 학습, 그리고 소수의 샘플로 미세 조정하는 다중 작업 적응. WLFM은 기존의 최첨단 모델을 능가하며, 공극률 추정에서 0.0041 MSE, 암석 분류에서 74.13%의 정확도를 기록했습니다. WLFM-Finetune는 이를 더욱 개선하여 각각 0.0038 MSE와 78.10%의 정확도를 달성했습니다. 또한, WLFM은 지질학적 어휘를 학습하고, 마스크된 곡선을 합리적으로 재구성할 수 있는 능력을 보여주었습니다. 이 연구는 WLFM이 지질학적 AI의 확장 가능하고 해석 가능한 기반이 될 수 있음을 시사하며, 로그, 지진, 텍스트 데이터의 다중 모달 통합에 대한 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. WLFM은 1200개의 유정에서 수집한 다중 곡선 로그를 기반으로 사전 학습된 모델로, 지질 토큰으로 로그 패치를 토큰화하고, 마스크된 토큰 모델링과 층서학 인식 대조 학습을 통해 자가 지도 학습을 수행합니다.
- 2. WLFM은 최첨단 기준 모델들을 능가하며, 공극률 추정에서 0.0041 MSE, 암석 분류에서 74.13%의 정확도를 달성하며, WLFM-Finetune은 각각 0.0038 MSE와 78.10%의 정확도로 성능을 더욱 향상시킵니다.
- 3. WLFM은 예측 정확도 외에도 층 인식 능력, 재사용 가능한 지질학적 어휘 학습, 그리고 마스크된 곡선의 합리적인 복원을 보여주지만, 얕은 및 초심층 구간에서는 체계적인 오프셋이 관찰됩니다.
- 4. 경계 감지는 명시적으로 평가되지 않았지만, 클러스터링 분석은 향후 확장의 강력한 잠재력을 시사합니다.
- 5. WLFM은 지질학적 AI의 확장 가능하고 해석 가능하며 전이 가능한 백본으로, 로그, 지진, 텍스트 데이터의 다중 모달 통합에 대한 함의를 제공합니다.


---

*Generated on 2025-09-24 13:39:36*