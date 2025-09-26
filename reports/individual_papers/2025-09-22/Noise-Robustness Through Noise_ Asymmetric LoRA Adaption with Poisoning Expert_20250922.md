---
keywords:
  - Low-Rank Adaptation
  - Poisoning Expert
  - Mixture-of-Experts
  - Noise Injection
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2505.23868
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:00:30.388911",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Rank Adaptation",
    "Poisoning Expert",
    "Mixture-of-Experts",
    "Noise Injection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-Rank Adaptation": 0.85,
    "Poisoning Expert": 0.78,
    "Mixture-of-Experts": 0.8,
    "Noise Injection": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LoRA",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "LoRA is a novel adaptation technique relevant to parameter-efficient tuning, which is central to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Poisoning Expert",
        "canonical": "Poisoning Expert",
        "aliases": [
          "LoPE"
        ],
        "category": "unique_technical",
        "rationale": "The concept of a 'Poisoning Expert' is unique to this paper's proposed method and crucial for understanding its noise-robustness strategy.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mixture-of-Experts",
        "canonical": "Mixture-of-Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "The Mixture-of-Experts architecture is a well-known concept that enhances model adaptability and is central to the proposed method.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Noise Injection",
        "canonical": "Noise Injection",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Noise Injection is a key technique used in the paper to improve model robustness, linking it to broader noise-handling strategies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "parameter-efficient",
      "fine-tuning",
      "downstream tasks",
      "noisy data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LoRA",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Poisoning Expert",
      "resolved_canonical": "Poisoning Expert",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mixture-of-Experts",
      "resolved_canonical": "Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Noise Injection",
      "resolved_canonical": "Noise Injection",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Noise-Robustness Through Noise: Asymmetric LoRA Adaption with Poisoning Expert

**Korean Title:** 소음에 대한 강인성: 오염 전문가를 활용한 비대칭 LoRA 적응

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23868.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2505.23868](https://arxiv.org/abs/2505.23868)

## 🔗 유사한 논문
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (85.2% similar)
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (82.7% similar)
- [[2025-09-22/A noise-corrected Langevin algorithm and sampling by half-denoising_20250922|A noise-corrected Langevin algorithm and sampling by half-denoising]] (80.7% similar)
- [[2025-09-22/Evaluating Robustness of LLMs in Question Answering on Multilingual Noisy OCR Data_20250922|Evaluating Robustness of LLMs in Question Answering on Multilingual Noisy OCR Data]] (80.2% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]], [[keywords/Noise Injection|Noise Injection]]
**⚡ Unique Technical**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]], [[keywords/Poisoning Expert|Poisoning Expert]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23868v4 Announce Type: replace-cross 
Abstract: Current parameter-efficient fine-tuning methods for adapting pre-trained language models to downstream tasks are susceptible to interference from noisy data. Conventional noise-handling approaches either rely on laborious data pre-processing or employ model architecture modifications prone to error accumulation. In contrast to existing noise-process paradigms, we propose a noise-robust adaptation method via asymmetric LoRA poisoning experts (LoPE), a novel framework that enhances model robustness to noise only with generated noisy data. Drawing inspiration from the mixture-of-experts architecture, LoPE strategically integrates a dedicated poisoning expert in an asymmetric LoRA configuration. Through a two-stage paradigm, LoPE performs noise injection on the poisoning expert during fine-tuning to enhance its noise discrimination and processing ability. During inference, we selectively mask the dedicated poisoning expert to leverage purified knowledge acquired by normal experts for noise-robust output. Extensive experiments demonstrate that LoPE achieves strong performance and robustness purely through the low-cost noise injection, which completely eliminates the requirement of data cleaning.

## 🔍 Abstract (한글 번역)

arXiv:2505.23868v4 발표 유형: 교체-크로스  
초록: 사전 학습된 언어 모델을 다운스트림 작업에 적응시키기 위한 현재의 매개변수 효율적인 미세 조정 방법은 잡음이 많은 데이터로 인한 간섭에 취약합니다. 기존의 잡음 처리 접근법은 번거로운 데이터 전처리에 의존하거나 오류 누적에 취약한 모델 아키텍처 수정을 사용합니다. 기존의 잡음 처리 패러다임과 달리, 우리는 생성된 잡음 데이터만으로 모델의 잡음에 대한 강건성을 향상시키는 비대칭 LoRA 중독 전문가(LoPE)를 통한 잡음 강건 적응 방법을 제안합니다. 전문가 혼합 아키텍처에서 영감을 받아, LoPE는 비대칭 LoRA 구성에서 전용 중독 전문가를 전략적으로 통합합니다. 두 단계 패러다임을 통해, LoPE는 미세 조정 중에 중독 전문가에 잡음 주입을 수행하여 잡음 판별 및 처리 능력을 향상시킵니다. 추론 시, 우리는 정규 전문가가 획득한 정제된 지식을 활용하여 잡음 강건 출력을 위해 전용 중독 전문가를 선택적으로 마스킹합니다. 광범위한 실험을 통해 LoPE가 데이터 정리의 필요성을 완전히 제거하면서도 저비용 잡음 주입만으로 강력한 성능과 강건성을 달성함을 입증합니다.

## 📝 요약

이 논문은 사전 학습된 언어 모델을 다운스트림 작업에 적응시키는 과정에서 발생하는 노이즈 문제를 해결하기 위한 새로운 방법론을 제안합니다. 기존의 노이즈 처리 방법은 데이터 전처리나 모델 구조 수정에 의존하여 오류가 누적될 수 있습니다. 이에 반해, 제안된 방법은 비대칭 LoRA 포이즈닝 전문가(LoPE)를 활용하여 노이즈에 강한 적응을 가능하게 합니다. LoPE는 전문가 혼합 구조에서 영감을 받아, 노이즈가 포함된 데이터를 생성하여 모델의 노이즈 처리 능력을 강화합니다. 실험 결과, LoPE는 데이터 정제 없이도 강력한 성능과 노이즈에 대한 견고성을 보여주었습니다.

## 🎯 주요 포인트

- 1. 기존의 파라미터 효율적 미세 조정 방법은 잡음 데이터의 간섭에 취약합니다.
- 2. LoPE는 비대칭 LoRA 구성을 통해 잡음에 강한 적응 방법을 제안합니다.
- 3. LoPE는 두 단계 패러다임을 통해 미세 조정 시 잡음 주입을 수행하여 잡음 처리 능력을 향상시킵니다.
- 4. 추론 시, LoPE는 정화된 지식을 활용하여 잡음에 강한 출력을 제공합니다.
- 5. 실험 결과, LoPE는 데이터 정리 없이도 강력한 성능과 견고성을 달성합니다.


---

*Generated on 2025-09-23 10:00:30*