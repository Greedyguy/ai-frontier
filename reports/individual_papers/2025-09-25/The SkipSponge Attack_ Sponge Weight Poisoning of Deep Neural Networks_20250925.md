---
keywords:
  - SkipSponge Attack
  - Neural Network
  - Generative Adversarial Networks
  - Autoencoder
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2402.06357
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:11:06.941161",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "SkipSponge Attack",
    "Neural Network",
    "Generative Adversarial Networks",
    "Autoencoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "SkipSponge Attack": 0.88,
    "Neural Network": 0.75,
    "Generative Adversarial Networks": 0.82,
    "Autoencoder": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "SkipSponge",
        "canonical": "SkipSponge Attack",
        "aliases": [
          "Sponge Weight Poisoning"
        ],
        "category": "unique_technical",
        "rationale": "SkipSponge represents a novel attack method specifically targeting neural network parameters, providing a unique perspective on model vulnerabilities.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Deep Neural Networks"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are central to the paper's focus on energy consumption and attack vectors, linking to broader discussions in Deep Learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "GANs",
        "canonical": "Generative Adversarial Networks",
        "aliases": [
          "GAN"
        ],
        "category": "specific_connectable",
        "rationale": "GANs are specifically mentioned as more susceptible to the SkipSponge attack, highlighting their relevance in adversarial contexts.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Autoencoders",
        "canonical": "Autoencoder",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Autoencoders are identified as a key model type affected by the SkipSponge attack, facilitating discussions on model robustness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "energy consumption",
      "computation time",
      "parameters",
      "training dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "SkipSponge",
      "resolved_canonical": "SkipSponge Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "GANs",
      "resolved_canonical": "Generative Adversarial Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Autoencoders",
      "resolved_canonical": "Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# The SkipSponge Attack: Sponge Weight Poisoning of Deep Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2402.06357.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2402.06357](https://arxiv.org/abs/2402.06357)

## 🔗 유사한 논문
- [[2025-09-24/Otters_ An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding_20250924|Otters: An Energy-Efficient SpikingTransformer via Optical Time-to-First-Spike Encoding]] (80.0% similar)
- [[2025-09-24/Backdoor Attack with Invisible Triggers Based on Model Architecture Modification_20250924|Backdoor Attack with Invisible Triggers Based on Model Architecture Modification]] (78.7% similar)
- [[2025-09-23/Train to Defend_ First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks_20250923|Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks]] (78.2% similar)
- [[2025-09-23/CSDformer_ A Conversion Method for Fully Spike-Driven Transformer_20250923|CSDformer: A Conversion Method for Fully Spike-Driven Transformer]] (78.2% similar)
- [[2025-09-25/Sample what you cant compress_20250925|Sample what you cant compress]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Generative Adversarial Networks|Generative Adversarial Networks]], [[keywords/Autoencoder|Autoencoder]]
**⚡ Unique Technical**: [[keywords/SkipSponge Attack|SkipSponge Attack]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2402.06357v5 Announce Type: replace-cross 
Abstract: Sponge attacks aim to increase the energy consumption and computation time of neural networks. In this work, we present a novel sponge attack called SkipSponge. SkipSponge is the first sponge attack that is performed directly on the parameters of a pretrained model using only a few data samples. Our experiments show that SkipSponge can successfully increase the energy consumption of image classification models, GANs, and autoencoders, requiring fewer samples than the state-of-the-art sponge attacks (Sponge Poisoning). We show that poisoning defenses are ineffective if not adjusted specifically for the defense against SkipSponge (i.e., they decrease target layer bias values) and that SkipSponge is more effective on the GANs and the autoencoders than Sponge Poisoning. Additionally, SkipSponge is stealthy as it does not require significant changes to the victim model's parameters. Our experiments indicate that SkipSponge can be performed even when an attacker has access to less than 1% of the entire training dataset and reaches up to 13% energy increase.

## 📝 요약

SkipSponge는 사전 학습된 모델의 파라미터에 직접 수행되는 새로운 유형의 스펀지 공격으로, 적은 데이터 샘플만으로도 이미지 분류 모델, GAN, 오토인코더의 에너지 소비를 증가시킬 수 있습니다. 기존의 스펀지 공격보다 적은 샘플로 효과를 발휘하며, 특히 GAN과 오토인코더에 더 효과적입니다. 또한, SkipSponge는 피해 모델의 파라미터에 큰 변화를 주지 않아 탐지가 어렵습니다. 실험 결과, 전체 훈련 데이터의 1% 미만을 사용해도 최대 13%의 에너지 증가를 유발할 수 있음을 보여줍니다. 기존의 방어 기법은 SkipSponge에 특화되지 않으면 효과가 없으며, 이는 방어 기법의 조정 필요성을 시사합니다.

## 🎯 주요 포인트

- 1. SkipSponge는 사전 학습된 모델의 파라미터에 직접 수행되는 최초의 스펀지 공격으로, 소수의 데이터 샘플만을 사용합니다.
- 2. SkipSponge는 이미지 분류 모델, GANs, 오토인코더의 에너지 소비를 성공적으로 증가시킬 수 있으며, 기존 스펀지 공격보다 적은 샘플을 필요로 합니다.
- 3. SkipSponge는 GANs와 오토인코더에서 기존의 스펀지 공격보다 더 효과적이며, 방어가 조정되지 않으면 방어가 비효과적입니다.
- 4. SkipSponge는 피해 모델의 파라미터에 큰 변화를 요구하지 않기 때문에 은밀하게 수행됩니다.
- 5. SkipSponge는 전체 훈련 데이터셋의 1% 미만에 접근할 수 있는 경우에도 수행 가능하며, 최대 13%의 에너지 증가를 달성합니다.


---

*Generated on 2025-09-25 17:11:06*