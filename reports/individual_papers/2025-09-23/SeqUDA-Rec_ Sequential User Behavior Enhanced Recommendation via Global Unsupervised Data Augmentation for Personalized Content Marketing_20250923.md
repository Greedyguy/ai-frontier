---
keywords:
  - Graph Neural Network
  - Self-supervised Learning
  - Transformer
  - Generative Adversarial Network
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17361
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:53:44.214893",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Self-supervised Learning",
    "Transformer",
    "Generative Adversarial Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Self-supervised Learning": 0.82,
    "Transformer": 0.8,
    "Generative Adversarial Network": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Global User-Item Interaction Graph",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GUIG"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is closely related to Graph Neural Networks, which are essential for modeling complex interactions in recommendation systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "graph contrastive learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "contrastive learning"
        ],
        "category": "specific_connectable",
        "rationale": "Graph contrastive learning is a form of self-supervised learning, enhancing the robustness of embeddings in recommendation systems.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transformer-based encoder",
        "canonical": "Transformer",
        "aliases": [
          "Transformer encoder"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational technology for sequence modeling in recommendation systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "GAN-based augmentation",
        "canonical": "Generative Adversarial Network",
        "aliases": [
          "GAN augmentation"
        ],
        "category": "unique_technical",
        "rationale": "GANs are used for generating synthetic data to improve training diversity, which is a novel application in this context.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "personalized content marketing",
      "recommendation systems",
      "user behavior sequences"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Global User-Item Interaction Graph",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "graph contrastive learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transformer-based encoder",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "GAN-based augmentation",
      "resolved_canonical": "Generative Adversarial Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# SeqUDA-Rec: Sequential User Behavior Enhanced Recommendation via Global Unsupervised Data Augmentation for Personalized Content Marketing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17361.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17361](https://arxiv.org/abs/2509.17361)

## 🔗 유사한 논문
- [[2025-09-19/Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems_20250919|Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems]] (81.7% similar)
- [[2025-09-19/JU-NLP at Touch\'e_ Covert Advertisement in Conversational AI-Generation and Detection Strategies_20250919|JU-NLP at Touch\'e: Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (80.7% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (80.4% similar)
- [[2025-09-23/Equip Pre-ranking with Target Attention by Residual Quantization_20250923|Equip Pre-ranking with Target Attention by Residual Quantization]] (80.2% similar)
- [[2025-09-23/AHA -- Predicting What Matters Next_ Online Highlight Detection Without Looking Ahead_20250923|AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Generative Adversarial Network|Generative Adversarial Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17361v1 Announce Type: cross 
Abstract: Personalized content marketing has become a crucial strategy for digital platforms, aiming to deliver tailored advertisements and recommendations that match user preferences. Traditional recommendation systems often suffer from two limitations: (1) reliance on limited supervised signals derived from explicit user feedback, and (2) vulnerability to noisy or unintentional interactions. To address these challenges, we propose SeqUDA-Rec, a novel deep learning framework that integrates user behavior sequences with global unsupervised data augmentation to enhance recommendation accuracy and robustness. Our approach first constructs a Global User-Item Interaction Graph (GUIG) from all user behavior sequences, capturing both local and global item associations. Then, a graph contrastive learning module is applied to generate robust embeddings, while a sequential Transformer-based encoder models users' evolving preferences. To further enhance diversity and counteract sparse supervised labels, we employ a GAN-based augmentation strategy, generating plausible interaction patterns and supplementing training data. Extensive experiments on two real-world marketing datasets (Amazon Ads and TikTok Ad Clicks) demonstrate that SeqUDA-Rec significantly outperforms state-of-the-art baselines such as SASRec, BERT4Rec, and GCL4SR. Our model achieves a 6.7% improvement in NDCG@10 and 11.3% improvement in HR@10, proving its effectiveness in personalized advertising and intelligent content recommendation.

## 📝 요약

개인화된 콘텐츠 마케팅을 위한 새로운 딥러닝 프레임워크인 SeqUDA-Rec을 제안합니다. 이 방법은 사용자 행동 시퀀스와 전역 비지도 데이터 증강을 통합하여 추천 정확성과 강건성을 향상시킵니다. 먼저, 모든 사용자 행동 시퀀스로부터 전역 사용자-아이템 상호작용 그래프(GUIG)를 구축하여 로컬 및 글로벌 아이템 연관성을 포착합니다. 그런 다음, 그래프 대조 학습 모듈을 통해 강건한 임베딩을 생성하고, 순차적 Transformer 기반 인코더로 사용자의 변화하는 선호도를 모델링합니다. 또한, GAN 기반 증강 전략을 사용하여 다양한 상호작용 패턴을 생성하고 훈련 데이터를 보완합니다. Amazon Ads와 TikTok Ad Clicks 데이터셋을 활용한 실험 결과, SeqUDA-Rec은 기존의 SASRec, BERT4Rec, GCL4SR 등 최신 기법보다 NDCG@10에서 6.7%, HR@10에서 11.3% 향상된 성능을 보였습니다. 이는 개인화된 광고 및 지능형 콘텐츠 추천에 있어 효과적임을 입증합니다.

## 🎯 주요 포인트

- 1. SeqUDA-Rec는 사용자 행동 시퀀스와 전역 비지도 데이터 증강을 통합하여 추천 정확성과 강건성을 향상시키는 새로운 딥러닝 프레임워크입니다.
- 2. Global User-Item Interaction Graph(GUIG)를 구축하여 지역 및 전역 항목 연관성을 포착하고, 그래프 대조 학습 모듈을 통해 강건한 임베딩을 생성합니다.
- 3. 사용자의 변화하는 선호도를 모델링하기 위해 순차적 Transformer 기반 인코더를 사용하며, GAN 기반 증강 전략을 통해 상호작용 패턴을 생성하고 훈련 데이터를 보완합니다.
- 4. 두 개의 실제 마케팅 데이터셋(Amazon Ads와 TikTok Ad Clicks)에서 SeqUDA-Rec는 기존 최첨단 모델들을 능가하며, NDCG@10에서 6.7%, HR@10에서 11.3%의 개선을 달성했습니다.
- 5. SeqUDA-Rec는 개인화된 광고와 지능형 콘텐츠 추천에서 효과적임을 입증했습니다.


---

*Generated on 2025-09-23 23:53:44*