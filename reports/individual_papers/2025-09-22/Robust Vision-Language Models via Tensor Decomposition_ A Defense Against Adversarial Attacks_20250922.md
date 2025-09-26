---
keywords:
  - Vision-Language Model
  - Tensor Decomposition
  - Adversarial Attack
  - CLIP
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16163
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:30:08.274893",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Tensor Decomposition",
    "Adversarial Attack",
    "CLIP"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Tensor Decomposition": 0.78,
    "Adversarial Attack": 0.82,
    "CLIP": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision language models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus on multimodal understanding and adversarial defense.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Tensor decomposition",
        "canonical": "Tensor Decomposition",
        "aliases": [
          "Tensor Train",
          "TT"
        ],
        "category": "unique_technical",
        "rationale": "Tensor decomposition is the novel technique proposed for enhancing model robustness against adversarial attacks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adversarial attacks",
        "canonical": "Adversarial Attack",
        "aliases": [
          "Adversarial Noise"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding adversarial attacks is crucial for linking defense strategies in vision-language models.",
        "novelty_score": 0.48,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "CLIP",
        "canonical": "CLIP",
        "aliases": [
          "Contrastive Language–Image Pretraining"
        ],
        "category": "specific_connectable",
        "rationale": "CLIP is a key model used in experiments, relevant for linking multimodal model performance.",
        "novelty_score": 0.5,
        "connectivity_score": 0.77,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
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
      "candidate_surface": "Vision language models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Tensor decomposition",
      "resolved_canonical": "Tensor Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adversarial attacks",
      "resolved_canonical": "Adversarial Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "CLIP",
      "resolved_canonical": "CLIP",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.77,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks

**Korean Title:** 텐서 분해를 통한 강건한 비전-언어 모델: 적대적 공격에 대한 방어

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16163.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16163](https://arxiv.org/abs/2509.16163)

## 🔗 유사한 논문
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (87.4% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (85.2% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (84.6% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (84.4% similar)
- [[2025-09-22/CLIPTTA_ Robust Contrastive Vision-Language Test-Time Adaptation_20250922|CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Adversarial Attack|Adversarial Attack]], [[keywords/CLIP|CLIP]]
**⚡ Unique Technical**: [[keywords/Tensor Decomposition|Tensor Decomposition]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16163v1 Announce Type: cross 
Abstract: Vision language models (VLMs) excel in multimodal understanding but are prone to adversarial attacks. Existing defenses often demand costly retraining or significant architecture changes. We introduce a lightweight defense using tensor decomposition suitable for any pre-trained VLM, requiring no retraining. By decomposing and reconstructing vision encoder representations, it filters adversarial noise while preserving meaning. Experiments with CLIP on COCO and Flickr30K show improved robustness. On Flickr30K, it restores 12.3\% performance lost to attacks, raising Recall@1 accuracy from 7.5\% to 19.8\%. On COCO, it recovers 8.1\% performance, improving accuracy from 3.8\% to 11.9\%. Analysis shows Tensor Train decomposition with low rank (8-32) and low residual strength ($\alpha=0.1-0.2$) is optimal. This method is a practical, plug-and-play solution with minimal overhead for existing VLMs.

## 🔍 Abstract (한글 번역)

arXiv:2509.16163v1 발표 유형: 교차  
초록: 비전 언어 모델(VLMs)은 다중 모달 이해에서 뛰어나지만, 적대적 공격에 취약합니다. 기존의 방어 방법은 종종 비용이 많이 드는 재훈련이나 상당한 아키텍처 변경을 요구합니다. 우리는 사전 훈련된 VLM에 적합하며 재훈련이 필요 없는 텐서 분해를 사용한 경량 방어 기법을 소개합니다. 비전 인코더 표현을 분해하고 재구성함으로써, 의미를 보존하면서 적대적 노이즈를 필터링합니다. COCO와 Flickr30K에서 CLIP을 사용한 실험은 향상된 강인성을 보여줍니다. Flickr30K에서는 공격으로 인해 손실된 성능의 12.3%를 복구하여 Recall@1 정확도를 7.5%에서 19.8%로 향상시킵니다. COCO에서는 8.1%의 성능을 회복하여 정확도를 3.8%에서 11.9%로 개선합니다. 분석 결과, 낮은 랭크(8-32)와 낮은 잔여 강도($\alpha=0.1-0.2$)를 가진 텐서 트레인 분해가 최적임을 보여줍니다. 이 방법은 기존 VLM에 최소한의 오버헤드로 적용 가능한 실용적이고 플러그 앤 플레이 솔루션입니다.

## 📝 요약

이 논문은 비전 언어 모델(VLM)의 적대적 공격에 대한 경량 방어 기법을 제안합니다. 기존 방어법은 재훈련이나 아키텍처 변경이 필요하지만, 이 방법은 텐서 분해를 활용하여 사전 훈련된 VLM에 적용 가능하며 재훈련이 필요 없습니다. 비전 인코더 표현을 분해하고 재구성하여 적대적 노이즈를 걸러내면서 의미를 보존합니다. CLIP 모델을 COCO와 Flickr30K 데이터셋에서 실험한 결과, Flickr30K에서 Recall@1 정확도를 7.5%에서 19.8%로, COCO에서는 3.8%에서 11.9%로 향상시켰습니다. 분석 결과, 낮은 랭크(8-32)와 낮은 잔여 강도(α=0.1-0.2)의 텐서 트레인 분해가 최적임을 보였습니다. 이 방법은 기존 VLM에 최소한의 오버헤드로 적용 가능한 실용적인 솔루션입니다.

## 🎯 주요 포인트

- 1. 비전 언어 모델(VLM)은 멀티모달 이해에 뛰어나지만 적대적 공격에 취약하다.
- 2. 기존 방어 방법은 재훈련이나 아키텍처 변경이 필요하지만, 본 연구에서는 텐서 분해를 활용한 경량 방어 방법을 제안한다.
- 3. 제안된 방법은 사전 훈련된 VLM에 적용 가능하며, 재훈련 없이 적대적 노이즈를 필터링하면서 의미를 보존한다.
- 4. CLIP 모델을 COCO와 Flickr30K 데이터셋에 적용한 결과, Flickr30K에서는 성능을 12.3% 회복하고 COCO에서는 8.1% 회복했다.
- 5. 텐서 트레인 분해를 사용하여 낮은 랭크(8-32)와 낮은 잔여 강도($\alpha=0.1-0.2$)가 최적임을 확인했다.


---

*Generated on 2025-09-23 09:30:08*