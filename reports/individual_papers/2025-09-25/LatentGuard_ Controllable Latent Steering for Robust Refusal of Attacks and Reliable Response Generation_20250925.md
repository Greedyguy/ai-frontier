---
keywords:
  - Latent Steering
  - Large Language Model
  - Structured Variational Autoencoder
  - Safety Alignment
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19839
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:17:47.263749",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Latent Steering",
    "Large Language Model",
    "Structured Variational Autoencoder",
    "Safety Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Latent Steering": 0.78,
    "Large Language Model": 0.85,
    "Structured Variational Autoencoder": 0.77,
    "Safety Alignment": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Latent Steering",
        "canonical": "Latent Steering",
        "aliases": [
          "Latent Control",
          "Latent Manipulation"
        ],
        "category": "unique_technical",
        "rationale": "Latent Steering is a unique approach central to the paper's methodology, offering a novel way to control model behavior.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are the focus of the paper, providing a broad technical context for the discussed techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Structured Variational Autoencoder",
        "canonical": "Structured Variational Autoencoder",
        "aliases": [
          "Structured VAE"
        ],
        "category": "unique_technical",
        "rationale": "The use of a Structured Variational Autoencoder is a specific technical approach that underpins the paper's framework.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Safety Alignment",
        "canonical": "Safety Alignment",
        "aliases": [
          "Safety Control",
          "Safety Steering"
        ],
        "category": "specific_connectable",
        "rationale": "Safety Alignment is a key concept in ensuring the model's responses are safe and reliable, linking to broader safety discussions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "robust safety",
      "response generation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Latent Steering",
      "resolved_canonical": "Latent Steering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Structured Variational Autoencoder",
      "resolved_canonical": "Structured Variational Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Safety Alignment",
      "resolved_canonical": "Safety Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# LatentGuard: Controllable Latent Steering for Robust Refusal of Attacks and Reliable Response Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19839.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19839](https://arxiv.org/abs/2509.19839)

## 🔗 유사한 논문
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (89.0% similar)
- [[2025-09-23/Automating Steering for Safe Multimodal Large Language Models_20250923|Automating Steering for Safe Multimodal Large Language Models]] (88.3% similar)
- [[2025-09-23/AdaptiveGuard_ Towards Adaptive Runtime Safety for LLM-Powered Software_20250923|AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software]] (87.9% similar)
- [[2025-09-23/Reasoning-to-Defend_ Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking_20250923|Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking]] (87.1% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (85.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Safety Alignment|Safety Alignment]]
**⚡ Unique Technical**: [[keywords/Latent Steering|Latent Steering]], [[keywords/Structured Variational Autoencoder|Structured Variational Autoencoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19839v1 Announce Type: new 
Abstract: Achieving robust safety alignment in large language models (LLMs) while preserving their utility remains a fundamental challenge. Existing approaches often struggle to balance comprehensive safety with fine-grained controllability at the representation level. We introduce LATENTGUARD, a novel three-stage framework that combines behavioral alignment with supervised latent space control for interpretable and precise safety steering. Our approach begins by fine-tuning an LLM on rationalized datasets containing both reasoning-enhanced refusal responses to adversarial prompts and reasoning-enhanced normal responses to benign queries, establishing robust behavioral priors across both safety-critical and utility-preserving scenarios. We then train a structured variational autoencoder (VAE) on intermediate MLP activations, supervised by multi-label annotations including attack types, attack methods, and benign indicators. This supervision enables the VAE to learn disentangled latent representations that capture distinct adversarial characteristics while maintaining semantic interpretability. Through targeted manipulation of learned latent dimensions, LATENTGUARD achieves selective refusal behavior, effectively blocking harmful requests while preserving helpfulness for legitimate use cases. Experiments on Qwen3-8B demonstrate significant improvements in both safety controllability and response interpretability without compromising utility. Cross-architecture validation on Mistral-7B confirms the generalizability of our latent steering approach, showing consistent effectiveness across different model families. Our results suggest that structured representation-level intervention offers a promising pathway toward building safer yet practical LLM systems.

## 📝 요약

LATENTGUARD는 대형 언어 모델(LLM)의 안전성을 강화하면서도 유용성을 유지하는 새로운 3단계 프레임워크입니다. 이 방법은 행동 정렬과 감독된 잠재 공간 제어를 결합하여 해석 가능하고 정밀한 안전 제어를 제공합니다. 먼저, 적대적 프롬프트에 대한 거부 응답과 정상 쿼리에 대한 응답을 포함한 데이터셋으로 LLM을 미세 조정하여 안전성과 유용성을 모두 고려한 행동 기준을 설정합니다. 이후, 다중 레이블 주석으로 감독된 구조적 변분 오토인코더(VAE)를 사용해 잠재 표현을 학습하고, 이를 통해 해로운 요청을 차단하면서도 유용한 요청에 대한 도움을 제공할 수 있습니다. Qwen3-8B 실험에서 안전성과 응답 해석 가능성이 크게 향상되었으며, Mistral-7B에서도 일반화 가능성을 확인했습니다. 이 연구는 구조적 표현 수준의 개입이 안전하면서도 실용적인 LLM 시스템 구축에 기여할 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. LATENTGUARD는 행동 정렬과 감독된 잠재 공간 제어를 결합하여 해석 가능하고 정밀한 안전 조정을 제공하는 새로운 프레임워크입니다.
- 2. 이 접근법은 적대적 프롬프트에 대한 거부 응답과 정상적인 쿼리에 대한 응답을 포함한 데이터셋으로 LLM을 미세 조정하여 안전성과 유용성을 모두 보장하는 행동적 사전 지식을 확립합니다.
- 3. 구조화된 변분 오토인코더(VAE)를 사용하여 공격 유형, 공격 방법, 정상 지표 등의 다중 레이블 주석으로 감독된 중간 MLP 활성화에 대해 훈련합니다.
- 4. 학습된 잠재 차원의 목표 조작을 통해 LATENTGUARD는 유해한 요청을 차단하면서도 정당한 사용 사례에 대한 도움을 유지하는 선택적 거부 행동을 달성합니다.
- 5. Qwen3-8B와 Mistral-7B 모델에서의 실험은 안전성 제어 가능성과 응답 해석 가능성의 개선을 보여주며, 다양한 모델 계열에서도 일관된 효과를 입증합니다.


---

*Generated on 2025-09-25 15:17:47*