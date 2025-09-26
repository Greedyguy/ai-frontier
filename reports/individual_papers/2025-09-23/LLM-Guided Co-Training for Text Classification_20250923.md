---
keywords:
  - Large Language Model
  - Weighted Co-Training
  - Self-supervised Learning
  - Encoder-Only Networks
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16516
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:39:03.248739",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Weighted Co-Training",
    "Self-supervised Learning",
    "Encoder-Only Networks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Weighted Co-Training": 0.78,
    "Self-supervised Learning": 0.82,
    "Encoder-Only Networks": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the proposed method and connect broadly with existing NLP and ML research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Weighted Co-Training",
        "canonical": "Weighted Co-Training",
        "aliases": [
          "Co-Training",
          "Weighted Co-Training"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach is the core contribution of the paper, offering a new method for semi-supervised learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Semi-Supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL",
          "Semi-Supervised Learning"
        ],
        "category": "specific_connectable",
        "rationale": "The paper advances SSL techniques, which are pivotal in modern ML frameworks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Encoder-Only Networks",
        "canonical": "Encoder-Only Networks",
        "aliases": [
          "Encoder Networks"
        ],
        "category": "unique_technical",
        "rationale": "These networks are integral to the paper's methodology, distinguishing it from other architectures.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
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
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Weighted Co-Training",
      "resolved_canonical": "Weighted Co-Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Semi-Supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Encoder-Only Networks",
      "resolved_canonical": "Encoder-Only Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# LLM-Guided Co-Training for Text Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16516.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16516](https://arxiv.org/abs/2509.16516)

## 🔗 유사한 논문
- [[2025-09-23/Federated Learning with Ad-hoc Adapter Insertions_ The Case of Soft-Embeddings for Training Classifier-as-Retriever_20250923|Federated Learning with Ad-hoc Adapter Insertions: The Case of Soft-Embeddings for Training Classifier-as-Retriever]] (85.2% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.8% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (84.5% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.3% similar)
- [[2025-09-22/SENTRA_ Selected-Next-Token Transformer for LLM Text Detection_20250922|SENTRA: Selected-Next-Token Transformer for LLM Text Detection]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Weighted Co-Training|Weighted Co-Training]], [[keywords/Encoder-Only Networks|Encoder-Only Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16516v1 Announce Type: new 
Abstract: In this paper, we introduce a novel weighted co-training approach that is guided by Large Language Models (LLMs). Namely, in our co-training approach, we use LLM labels on unlabeled data as target labels and co-train two encoder-only based networks that train each other over multiple iterations: first, all samples are forwarded through each network and historical estimates of each network's confidence in the LLM label are recorded; second, a dynamic importance weight is derived for each sample according to each network's belief in the quality of the LLM label for that sample; finally, the two networks exchange importance weights with each other -- each network back-propagates all samples weighted with the importance weights coming from its peer network and updates its own parameters. By strategically utilizing LLM-generated guidance, our approach significantly outperforms conventional SSL methods, particularly in settings with abundant unlabeled data. Empirical results show that it achieves state-of-the-art performance on 4 out of 5 benchmark datasets and ranks first among 14 compared methods according to the Friedman test. Our results highlight a new direction in semi-supervised learning -- where LLMs serve as knowledge amplifiers, enabling backbone co-training models to achieve state-of-the-art performance efficiently.

## 📝 요약

이 논문에서는 대형 언어 모델(LLM)이 안내하는 새로운 가중치 공동 학습 방법을 제안합니다. 이 방법에서는 LLM이 생성한 라벨을 목표 라벨로 사용하여 두 개의 인코더 기반 네트워크가 서로 학습합니다. 각 네트워크는 LLM 라벨에 대한 신뢰도를 기록하고, 샘플의 중요도를 동적으로 계산하여 서로 교환합니다. 이 방식은 특히 많은 미라벨 데이터가 있는 환경에서 기존의 반지도 학습(SSL) 방법보다 뛰어난 성능을 보입니다. 실험 결과, 5개의 벤치마크 데이터셋 중 4개에서 최첨단 성능을 달성했으며, 14개의 비교 방법 중 프리드먼 테스트에서 1위를 기록했습니다. 이 연구는 LLM을 지식 증폭기로 활용하여 공동 학습 모델의 효율적인 성능 향상을 가능하게 하는 새로운 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 본 논문은 대형 언어 모델(LLM)이 안내하는 새로운 가중치 공동 학습 접근법을 소개합니다.
- 2. LLM 레이블을 목표 레이블로 사용하여 두 개의 인코더 기반 네트워크가 상호 학습하는 방식을 제안합니다.
- 3. 네트워크 간 중요도 가중치를 교환하여 각 네트워크가 상대 네트워크의 가중치로 모든 샘플을 역전파합니다.
- 4. 제안된 방법은 특히 많은 비라벨 데이터 환경에서 기존의 반지도 학습 방법을 능가합니다.
- 5. 5개의 벤치마크 데이터셋 중 4개에서 최첨단 성능을 달성하고, 14개의 비교 방법 중 프리드먼 테스트에서 1위를 차지했습니다.


---

*Generated on 2025-09-24 01:39:03*