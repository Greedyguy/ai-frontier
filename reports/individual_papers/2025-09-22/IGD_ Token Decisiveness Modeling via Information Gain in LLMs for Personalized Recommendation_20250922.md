---
keywords:
  - Large Language Model
  - Information Gain
  - Token Decisiveness
  - Personalized Recommendation
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2506.13229
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:49:12.128226",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Information Gain",
    "Token Decisiveness",
    "Personalized Recommendation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Information Gain": 0.78,
    "Token Decisiveness": 0.74,
    "Personalized Recommendation": 0.79
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
        "rationale": "Large Language Models are central to the paper's methodology and connect well with existing research in language processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Information Gain",
        "canonical": "Information Gain",
        "aliases": [
          "IG"
        ],
        "category": "unique_technical",
        "rationale": "Information Gain is a unique concept introduced in the paper to quantify token decisiveness, offering a novel perspective.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Token Decisiveness",
        "canonical": "Token Decisiveness",
        "aliases": [
          "Decisiveness of Tokens"
        ],
        "category": "unique_technical",
        "rationale": "Token Decisiveness is a novel concept that underpins the paper's approach to improving recommendation accuracy.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.74
      },
      {
        "surface": "Personalized Recommendation",
        "canonical": "Personalized Recommendation",
        "aliases": [
          "Recommendation Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Personalized Recommendation is a key application area for the proposed method, linking it to broader research in recommendation systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Information Gain",
      "resolved_canonical": "Information Gain",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Token Decisiveness",
      "resolved_canonical": "Token Decisiveness",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Personalized Recommendation",
      "resolved_canonical": "Personalized Recommendation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation

**Korean Title:** IGD: 개인화 추천을 위한 대형 언어 모델(LLM)에서 정보 이득을 통한 토큰 결정성 모델링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.13229.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2506.13229](https://arxiv.org/abs/2506.13229)

## 🔗 유사한 논문
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (85.3% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (84.7% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (83.8% similar)
- [[2025-09-22/Benchmarking Debiasing Methods for LLM-based Parameter Estimates_20250922|Benchmarking Debiasing Methods for LLM-based Parameter Estimates]] (83.7% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Personalized Recommendation|Personalized Recommendation]]
**⚡ Unique Technical**: [[keywords/Information Gain|Information Gain]], [[keywords/Token Decisiveness|Token Decisiveness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.13229v2 Announce Type: replace 
Abstract: Large Language Models (LLMs) have shown strong potential for recommendation by framing item prediction as a token-by-token language generation task. However, existing methods treat all item tokens equally, simply pursuing likelihood maximization during both optimization and decoding. This overlooks crucial token-level differences in decisiveness-many tokens contribute little to item discrimination yet can dominate optimization or decoding. To quantify token decisiveness, we propose a novel perspective that models item generation as a decision process, measuring token decisiveness by the Information Gain (IG) each token provides in reducing uncertainty about the generated item. Our empirical analysis reveals that most tokens have low IG but often correspond to high logits, disproportionately influencing training loss and decoding, which may impair model performance. Building on these insights, we introduce an Information Gain-based Decisiveness-aware Token handling (IGD) strategy that integrates token decisiveness into both tuning and decoding. Specifically, IGD downweights low-IG tokens during tuning and rebalances decoding to emphasize tokens with high IG. In this way, IGD moves beyond pure likelihood maximization, effectively prioritizing high-decisiveness tokens. Extensive experiments on four benchmark datasets with two LLM backbones demonstrate that IGD consistently improves recommendation accuracy, achieving significant gains on widely used ranking metrics compared to strong baselines.

## 🔍 Abstract (한글 번역)

arXiv:2506.13229v2 발표 유형: 교체  
초록: 대형 언어 모델(LLMs)은 아이템 예측을 토큰별 언어 생성 작업으로 프레이밍하여 추천에 대한 강력한 잠재력을 보여주었습니다. 그러나 기존 방법들은 모든 아이템 토큰을 동일하게 취급하며, 최적화와 디코딩 과정에서 단순히 가능성 최대화를 추구합니다. 이는 결정력에서의 중요한 토큰 수준의 차이를 간과하는데, 많은 토큰이 아이템 구별에 거의 기여하지 않으면서도 최적화나 디코딩을 지배할 수 있습니다. 토큰 결정력을 정량화하기 위해, 우리는 아이템 생성을 의사 결정 과정으로 모델링하는 새로운 관점을 제안하며, 생성된 아이템에 대한 불확실성을 줄이는 데 각 토큰이 제공하는 정보 이득(IG)을 통해 토큰 결정력을 측정합니다. 우리의 실증 분석은 대부분의 토큰이 낮은 IG를 가지고 있지만 종종 높은 로짓에 해당하여, 훈련 손실과 디코딩에 불균형적으로 영향을 미쳐 모델 성능을 저하시킬 수 있음을 보여줍니다. 이러한 통찰을 바탕으로, 우리는 조정과 디코딩 모두에 토큰 결정력을 통합하는 정보 이득 기반 결정력 인식 토큰 처리(IGD) 전략을 소개합니다. 구체적으로, IGD는 조정 과정에서 낮은 IG 토큰의 가중치를 낮추고, 디코딩을 재조정하여 높은 IG 토큰을 강조합니다. 이렇게 함으로써, IGD는 순수한 가능성 최대화를 넘어, 높은 결정력의 토큰을 효과적으로 우선시합니다. 두 개의 LLM 백본을 사용한 네 개의 벤치마크 데이터셋에 대한 광범위한 실험은 IGD가 강력한 기준선과 비교하여 널리 사용되는 순위 메트릭에서 유의미한 향상을 달성하며, 추천 정확도를 지속적으로 향상시킴을 보여줍니다.

## 📝 요약

대형 언어 모델(LLMs)은 아이템 예측을 언어 생성 작업으로 프레이밍하여 추천 시스템에서 강력한 잠재력을 보입니다. 그러나 기존 방법들은 모든 아이템 토큰을 동일하게 취급하여 최적화와 디코딩 시 단순히 가능성 최대화를 추구합니다. 이는 결정력 있는 토큰의 차이를 간과하는데, 많은 토큰이 아이템 구별에 거의 기여하지 않으면서도 최적화나 디코딩에 과도한 영향을 미칠 수 있습니다. 이를 해결하기 위해, 우리는 정보 이득(IG)을 통해 각 토큰이 생성된 아이템의 불확실성을 줄이는 데 기여하는 정도를 측정하여 토큰 결정력을 평가하는 새로운 관점을 제안합니다. 우리의 실증 분석에 따르면 대부분의 토큰은 낮은 IG를 가지지만 높은 로짓과 연관되어 있어 모델 성능을 저하시킬 수 있습니다. 이러한 통찰을 바탕으로, 우리는 정보 이득 기반의 결정력 인식 토큰 처리(IGD) 전략을 도입하여 토큰 결정력을 튜닝과 디코딩에 통합합니다. IGD는 튜닝 시 낮은 IG 토큰의 가중치를 낮추고, 디코딩 시 높은 IG 토큰을 강조하여 순수한 가능성 최대화에서 벗어납니다. 네 가지 벤치마크 데이터셋과 두 가지 LLM 백본을 사용한 실험에서 IGD는 추천 정확도를 지속적으로 향상시켰으며, 강력한 기준선과 비교하여 널리 사용되는 순위 매트릭스에서 유의미한 성과를 달성했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 아이템 예측을 토큰 단위의 언어 생성 작업으로 프레이밍하여 추천 분야에서 강력한 잠재력을 보여주었다.
- 2. 기존 방법은 모든 아이템 토큰을 동일하게 취급하여 최적화 및 디코딩 시 단순히 가능성 최대화를 추구한다.
- 3. 우리는 정보 이득(IG)을 통해 각 토큰이 생성된 아이템의 불확실성을 줄이는 데 기여하는 정도를 측정하여 토큰 결정성을 정량화하는 새로운 관점을 제안한다.
- 4. 정보 이득 기반 결정성 인식 토큰 처리(IGD) 전략은 튜닝과 디코딩 모두에 토큰 결정성을 통합하여, 낮은 IG 토큰의 가중치를 줄이고 높은 IG 토큰을 강조한다.
- 5. IGD는 네 가지 벤치마크 데이터셋과 두 가지 LLM 백본에서 추천 정확도를 지속적으로 향상시켜 강력한 기준선과 비교하여 순위 매트릭스에서 유의미한 성과 향상을 달성했다.


---

*Generated on 2025-09-23 11:49:12*