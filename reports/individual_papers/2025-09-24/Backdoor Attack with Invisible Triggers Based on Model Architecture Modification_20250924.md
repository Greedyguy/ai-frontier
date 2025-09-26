<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:26:23.928288",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Backdoor Attack",
    "Invisible Triggers",
    "Model Architecture Modification",
    "Pre-trained Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Backdoor Attack": 0.8,
    "Invisible Triggers": 0.7,
    "Model Architecture Modification": 0.78,
    "Pre-trained Models": 0.6
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "backdoor attack",
        "canonical": "Backdoor Attack",
        "aliases": [
          "backdoor manipulation",
          "backdoor threat"
        ],
        "category": "unique_technical",
        "rationale": "Backdoor attacks are a specific type of security threat in machine learning, crucial for understanding vulnerabilities.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "invisible triggers",
        "canonical": "Invisible Triggers",
        "aliases": [
          "stealthy triggers",
          "hidden triggers"
        ],
        "category": "unique_technical",
        "rationale": "Invisible triggers represent a novel method for activating backdoors without detection, enhancing the stealthiness of attacks.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "model architecture modification",
        "canonical": "Model Architecture Modification",
        "aliases": [
          "architectural changes",
          "model structure alteration"
        ],
        "category": "specific_connectable",
        "rationale": "Modifying model architecture is a sophisticated technique for embedding backdoors, linking to broader discussions on model integrity.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "pre-trained models",
        "canonical": "Pre-trained Models",
        "aliases": [
          "pretrained networks",
          "pre-trained architectures"
        ],
        "category": "broad_technical",
        "rationale": "Pre-trained models are widely used in machine learning, making them a common target for backdoor attacks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.6
      }
    ],
    "ban_list_suggestions": [
      "traditional backdoor attacks",
      "manual visual inspection"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "backdoor attack",
      "resolved_canonical": "Backdoor Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "invisible triggers",
      "resolved_canonical": "Invisible Triggers",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "model architecture modification",
      "resolved_canonical": "Model Architecture Modification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "pre-trained models",
      "resolved_canonical": "Pre-trained Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.6
      }
    }
  ]
}
-->

# Backdoor Attack with Invisible Triggers Based on Model Architecture Modification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2412.16905.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2412.16905](https://arxiv.org/abs/2412.16905)

## 🔗 유사한 논문
- [[2025-09-23/Rethinking Backdoor Detection Evaluation for Language Models_20250923|Rethinking Backdoor Detection Evaluation for Language Models]] (90.0% similar)
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (88.6% similar)
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (88.3% similar)
- [[2025-09-23/Neural Antidote_ Class-Wise Prompt Tuning for Purifying Backdoors in CLIP_20250923|Neural Antidote: Class-Wise Prompt Tuning for Purifying Backdoors in CLIP]] (85.3% similar)
- [[2025-09-23/Jailbreak-Tuning_ Models Efficiently Learn Jailbreak Susceptibility_20250923|Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Pre-trained Models|Pre-trained Models]]
**🔗 Specific Connectable**: [[keywords/Model Architecture Modification|Model Architecture Modification]]
**⚡ Unique Technical**: [[keywords/Backdoor Attack|Backdoor Attack]], [[keywords/Invisible Triggers|Invisible Triggers]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.16905v3 Announce Type: replace-cross 
Abstract: Machine learning systems are vulnerable to backdoor attacks, where attackers manipulate model behavior through data tampering or architectural modifications. Traditional backdoor attacks involve injecting malicious samples with specific triggers into the training data, causing the model to produce targeted incorrect outputs in the presence of the corresponding triggers. More sophisticated attacks modify the model's architecture directly, embedding backdoors that are harder to detect as they evade traditional data-based detection methods. However, the drawback of the architectural modification based backdoor attacks is that the trigger must be visible in order to activate the backdoor. To further strengthen the invisibility of the backdoor attacks, a novel backdoor attack method is presented in the paper. To be more specific, this method embeds the backdoor within the model's architecture and has the capability to generate inconspicuous and stealthy triggers. The attack is implemented by modifying pre-trained models, which are then redistributed, thereby posing a potential threat to unsuspecting users. Comprehensive experiments conducted on standard computer vision benchmarks validate the effectiveness of this attack and highlight the stealthiness of its triggers, which remain undetectable through both manual visual inspection and advanced detection tools.

## 📝 요약

이 논문은 기계 학습 시스템의 백도어 공격에 대한 새로운 방법을 제안합니다. 전통적인 백도어 공격은 훈련 데이터에 특정 트리거가 포함된 악성 샘플을 주입하여 모델의 출력을 조작하는 방식입니다. 그러나 이 논문에서는 모델의 아키텍처를 직접 수정하여 백도어를 삽입하고, 눈에 띄지 않는 트리거를 생성할 수 있는 방법을 소개합니다. 이 방법은 사전 학습된 모델을 수정하여 배포함으로써, 사용자가 인지하지 못하는 사이에 위협을 가할 수 있습니다. 실험 결과, 이 공격은 기존의 탐지 도구로도 발견하기 어려운 높은 은폐성을 가지며, 컴퓨터 비전 벤치마크에서 그 효과가 입증되었습니다.

## 🎯 주요 포인트

- 1. 기계 학습 시스템은 데이터 조작이나 구조적 수정으로 인해 백도어 공격에 취약하다.
- 2. 전통적인 백도어 공격은 특정 트리거를 포함한 악성 샘플을 훈련 데이터에 주입하여 모델이 잘못된 출력을 생성하도록 한다.
- 3. 새로운 백도어 공격 방법은 모델의 구조에 백도어를 내장하고 눈에 띄지 않는 트리거를 생성할 수 있다.
- 4. 이 공격은 사전 훈련된 모델을 수정하여 구현되며, 의심하지 않는 사용자에게 잠재적 위협이 된다.
- 5. 실험 결과, 이 공격은 수동 시각 검사와 고급 탐지 도구를 통해도 탐지되지 않는 높은 은밀성을 가진다.


---

*Generated on 2025-09-24 14:26:23*