---
keywords:
  - Synthetic Bootstrapped Pretraining
  - Large Language Model
  - Inter-document Correlations
  - Bayesian Interpretation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15248
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:48:34.835179",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Synthetic Bootstrapped Pretraining",
    "Large Language Model",
    "Inter-document Correlations",
    "Bayesian Interpretation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Synthetic Bootstrapped Pretraining": 0.8,
    "Large Language Model": 0.85,
    "Inter-document Correlations": 0.78,
    "Bayesian Interpretation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Synthetic Bootstrapped Pretraining",
        "canonical": "Synthetic Bootstrapped Pretraining",
        "aliases": [
          "SBP"
        ],
        "category": "unique_technical",
        "rationale": "This is the core innovation of the paper, offering a novel approach to language model pretraining.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "language model",
        "canonical": "Large Language Model",
        "aliases": [
          "LM"
        ],
        "category": "broad_technical",
        "rationale": "Language models are central to the paper's methodology and connect to various related works in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "inter-document correlations",
        "canonical": "Inter-document Correlations",
        "aliases": [
          "document relations"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding inter-document correlations is key to the proposed method's improvement over traditional pretraining.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bayesian interpretation",
        "canonical": "Bayesian Interpretation",
        "aliases": [
          "Bayesian perspective"
        ],
        "category": "specific_connectable",
        "rationale": "The Bayesian interpretation provides a theoretical framework that could link to other probabilistic models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "pretraining setup",
      "performance improvement"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Synthetic Bootstrapped Pretraining",
      "resolved_canonical": "Synthetic Bootstrapped Pretraining",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "language model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "inter-document correlations",
      "resolved_canonical": "Inter-document Correlations",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bayesian interpretation",
      "resolved_canonical": "Bayesian Interpretation",
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

# Synthetic bootstrapped pretraining

**Korean Title:** 합성 부트스트랩 사전훈련

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15248.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15248](https://arxiv.org/abs/2509.15248)

## 🔗 유사한 논문
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.6% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (79.6% similar)
- [[2025-09-22/Bayesian Concept Bottleneck Models with LLM Priors_20250922|Bayesian Concept Bottleneck Models with LLM Priors]] (78.5% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (78.5% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery: Reinforced Distillation of Large Language Model Agents]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Inter-document Correlations|Inter-document Correlations]], [[keywords/Bayesian Interpretation|Bayesian Interpretation]]
**⚡ Unique Technical**: [[keywords/Synthetic Bootstrapped Pretraining|Synthetic Bootstrapped Pretraining]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15248v1 Announce Type: cross 
Abstract: We introduce Synthetic Bootstrapped Pretraining (SBP), a language model (LM) pretraining procedure that first learns a model of relations between documents from the pretraining dataset and then leverages it to synthesize a vast new corpus for joint training. While the standard pretraining teaches LMs to learn causal correlations among tokens within a single document, it is not designed to efficiently model the rich, learnable inter-document correlations that can potentially lead to better performance. We validate SBP by designing a compute-matched pretraining setup and pretrain a 3B-parameter model on up to 1T tokens from scratch. We find SBP consistently improves upon a strong repetition baseline and delivers a significant fraction of performance improvement attainable by an oracle upper bound with access to 20x more unique data. Qualitative analysis reveals that the synthesized documents go beyond mere paraphrases -- SBP first abstracts a core concept from the seed material and then crafts a new narration on top of it. Besides strong empirical performance, SBP admits a natural Bayesian interpretation: the synthesizer implicitly learns to abstract the latent concepts shared between related documents.

## 🔍 Abstract (한글 번역)

arXiv:2509.15248v1 발표 유형: 교차  
초록: 우리는 문서 간 관계를 학습하고 이를 활용하여 공동 학습을 위한 방대한 새로운 코퍼스를 합성하는 언어 모델(LM) 사전 학습 절차인 Synthetic Bootstrapped Pretraining (SBP)을 소개합니다. 표준 사전 학습은 단일 문서 내에서 토큰 간의 인과 관계를 학습하도록 LMs를 교육하지만, 이는 더 나은 성능으로 이어질 수 있는 풍부하고 학습 가능한 문서 간 상관 관계를 효율적으로 모델링하도록 설계되지 않았습니다. 우리는 계산이 일치하는 사전 학습 설정을 설계하고 1조 개의 토큰에서 3B-매개변수 모델을 처음부터 사전 학습하여 SBP를 검증합니다. SBP는 강력한 반복 기준선을 지속적으로 개선하고, 20배 더 많은 고유 데이터를 이용할 수 있는 오라클 상한선에 의해 달성 가능한 성능 향상의 상당 부분을 제공합니다. 질적 분석 결과 합성된 문서가 단순한 패러프레이즈를 넘어서는 것을 보여줍니다. SBP는 처음에 시드 자료에서 핵심 개념을 추상화한 다음 그 위에 새로운 서술을 작성합니다. 강력한 경험적 성능 외에도 SBP는 자연스러운 베이지안 해석을 허용합니다: 합성기는 관련 문서 간에 공유되는 잠재 개념을 추상화하는 법을 암묵적으로 학습합니다.

## 📝 요약

Synthetic Bootstrapped Pretraining (SBP)는 문서 간 관계를 학습하여 새로운 대규모 코퍼스를 생성하고 이를 통해 언어 모델을 공동 학습하는 방법론입니다. 기존의 사전 학습은 단일 문서 내의 인과적 상관관계에 중점을 두지만, SBP는 문서 간의 풍부한 상관관계를 효율적으로 모델링하여 성능을 향상시킵니다. SBP는 3B-파라미터 모델을 1조 토큰으로 사전 학습하여 성능 개선을 확인했으며, 이는 20배 더 많은 데이터에 접근할 수 있는 이상적인 상한선의 성능 개선의 상당 부분을 달성합니다. SBP는 문서의 핵심 개념을 추상화하고 새로운 서술을 창작하며, 베이지안 해석을 통해 관련 문서 간의 잠재 개념을 추상화하는 학습을 수행합니다.

## 🎯 주요 포인트

- 1. Synthetic Bootstrapped Pretraining (SBP)는 문서 간 관계를 학습하여 새로운 대규모 코퍼스를 합성하고 이를 공동 학습에 활용하는 언어 모델 사전 학습 절차입니다.
- 2. SBP는 단일 문서 내 토큰 간 인과적 상관관계를 학습하는 기존 사전 학습과 달리, 문서 간의 풍부한 상관관계를 효율적으로 모델링하여 성능을 향상시킵니다.
- 3. 3B-파라미터 모델을 최대 1조 개의 토큰으로 사전 학습한 결과, SBP는 강력한 반복 기반 모델을 능가하고, 20배 더 많은 고유 데이터를 사용할 수 있는 이상적인 상한선의 상당 부분을 달성했습니다.
- 4. SBP는 단순한 패러프레이즈를 넘어 핵심 개념을 추상화하고 새로운 서술을 구성하는 능력을 보여줍니다.
- 5. SBP는 관련 문서 간에 공유되는 잠재 개념을 추상화하는 학습을 통해 자연스러운 베이지안 해석을 제공합니다.


---

*Generated on 2025-09-23 08:48:34*