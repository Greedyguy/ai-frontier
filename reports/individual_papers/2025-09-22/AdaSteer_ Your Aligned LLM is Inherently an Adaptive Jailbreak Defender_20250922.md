---
keywords:
  - Large Language Model
  - Jailbreak Attacks
  - Activation Steering
  - Adaptive Coefficients
  - Rejection Law
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2504.09466
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:52:09.563605",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Jailbreak Attacks",
    "Activation Steering",
    "Adaptive Coefficients",
    "Rejection Law"
  ],
  "rejected_keywords": [
    "Harmfulness Law"
  ],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Jailbreak Attacks": 0.78,
    "Activation Steering": 0.72,
    "Adaptive Coefficients": 0.71,
    "Rejection Law": 0.7,
    "Harmfulness Law": 0.69
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
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on jailbreak defense, providing a strong link to existing research on language model safety.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "jailbreak attacks",
        "canonical": "Jailbreak Attacks",
        "aliases": [
          "jailbreaking",
          "model exploitation"
        ],
        "category": "unique_technical",
        "rationale": "Jailbreak attacks are a specific threat addressed by the proposed method, crucial for understanding model vulnerabilities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "activation steering",
        "canonical": "Activation Steering",
        "aliases": [
          "steering coefficients",
          "model steering"
        ],
        "category": "unique_technical",
        "rationale": "Activation steering is a core technique discussed, offering a novel approach to model defense without retraining.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.72
      },
      {
        "surface": "adaptive coefficients",
        "canonical": "Adaptive Coefficients",
        "aliases": [
          "dynamic coefficients",
          "variable coefficients"
        ],
        "category": "unique_technical",
        "rationale": "Adaptive coefficients are pivotal in the proposed method, enabling dynamic model adjustments to enhance security.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.71
      },
      {
        "surface": "Rejection Law",
        "canonical": "Rejection Law",
        "aliases": [
          "R-Law",
          "rejection principle"
        ],
        "category": "unique_technical",
        "rationale": "Rejection Law is a novel concept introduced to differentiate between adversarial and benign inputs, crucial for the method's effectiveness.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Harmfulness Law",
        "canonical": "Harmfulness Law",
        "aliases": [
          "H-Law",
          "harmfulness principle"
        ],
        "category": "unique_technical",
        "rationale": "Harmfulness Law is essential for understanding how the method distinguishes between harmful and benign inputs.",
        "novelty_score": 0.78,
        "connectivity_score": 0.58,
        "specificity_score": 0.82,
        "link_intent_score": 0.69
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
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "jailbreak attacks",
      "resolved_canonical": "Jailbreak Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "activation steering",
      "resolved_canonical": "Activation Steering",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "adaptive coefficients",
      "resolved_canonical": "Adaptive Coefficients",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.71
      }
    },
    {
      "candidate_surface": "Rejection Law",
      "resolved_canonical": "Rejection Law",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Harmfulness Law",
      "resolved_canonical": "Harmfulness Law",
      "decision": "skipped_threshold",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.58,
        "specificity": 0.82,
        "link_intent": 0.69
      }
    }
  ]
}
-->

# AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender

**Korean Title:** AdaSteer: 귀하의 정렬된 LLM은 본질적으로 적응형 탈옥 방어자입니다.

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2504.09466.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2504.09466](https://arxiv.org/abs/2504.09466)

## 🔗 유사한 논문
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (86.8% similar)
- [[2025-09-22/Beyond Linear Steering_ Unified Multi-Attribute Control for Language Models_20250922|Beyond Linear Steering: Unified Multi-Attribute Control for Language Models]] (86.4% similar)
- [[2025-09-18/LLM Jailbreak Detection for (Almost) Free!_20250918|LLM Jailbreak Detection for (Almost) Free!]] (85.7% similar)
- [[2025-09-22/From Judgment to Interference_ Early Stopping LLM Harmful Outputs via Streaming Content Monitoring_20250922|From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring]] (84.8% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Jailbreak Attacks|Jailbreak Attacks]], [[keywords/Activation Steering|Activation Steering]], [[keywords/Adaptive Coefficients|Adaptive Coefficients]], [[keywords/Rejection Law|Rejection Law]], [[keywords/Harmfulness Law|Harmfulness Law]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.09466v2 Announce Type: replace-cross 
Abstract: Despite extensive efforts in safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks. Activation steering offers a training-free defense method but relies on fixed steering coefficients, resulting in suboptimal protection and increased false rejections of benign inputs. To address this, we propose AdaSteer, an adaptive activation steering method that dynamically adjusts model behavior based on input characteristics. We identify two key properties: Rejection Law (R-Law), which shows that stronger steering is needed for jailbreak inputs opposing the rejection direction, and Harmfulness Law (H-Law), which differentiates adversarial and benign inputs. AdaSteer steers input representations along both the Rejection Direction (RD) and Harmfulness Direction (HD), with adaptive coefficients learned via logistic regression, ensuring robust jailbreak defense while preserving benign input handling. Experiments on LLaMA-3.1, Gemma-2, and Qwen2.5 show that AdaSteer outperforms baseline methods across multiple jailbreak attacks with minimal impact on utility. Our results highlight the potential of interpretable model internals for real-time, flexible safety enforcement in LLMs.

## 🔍 Abstract (한글 번역)

arXiv:2504.09466v2 발표 유형: 교체-크로스  
초록: 안전 정렬에 대한 광범위한 노력에도 불구하고, 대형 언어 모델(LLMs)은 여전히 탈옥 공격에 취약합니다. 활성화 조정은 훈련이 필요 없는 방어 방법을 제공하지만, 고정된 조정 계수에 의존하여 최적이 아닌 보호와 무해한 입력에 대한 거짓 거부를 증가시킵니다. 이를 해결하기 위해, 우리는 입력 특성에 따라 모델의 동작을 동적으로 조정하는 적응형 활성화 조정 방법인 AdaSteer를 제안합니다. 우리는 두 가지 주요 속성을 식별합니다: 거부 법칙(R-Law)은 거부 방향에 반대하는 탈옥 입력에 대해 더 강한 조정이 필요함을 보여주고, 유해성 법칙(H-Law)은 적대적 입력과 무해한 입력을 구별합니다. AdaSteer는 적응형 계수가 로지스틱 회귀를 통해 학습되어, 거부 방향(RD)과 유해성 방향(HD) 모두에서 입력 표현을 조정하여 무해한 입력 처리를 유지하면서도 강력한 탈옥 방어를 보장합니다. LLaMA-3.1, Gemma-2 및 Qwen2.5에 대한 실험에서 AdaSteer는 유용성에 미치는 영향을 최소화하면서 여러 탈옥 공격에서 기준 방법보다 우수한 성능을 보였습니다. 우리의 결과는 LLM에서 실시간, 유연한 안전 강화를 위한 해석 가능한 모델 내부의 잠재력을 강조합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 보안 취약점을 해결하기 위해 AdaSteer라는 적응형 활성화 조정 방법을 제안합니다. 기존의 고정된 조정 계수 방식은 최적의 보호를 제공하지 못하고, 정상 입력의 오탐률을 높이는 문제가 있었습니다. AdaSteer는 입력 특성에 따라 모델의 동작을 동적으로 조정하여 이러한 문제를 해결합니다. 두 가지 주요 속성인 거부 법칙(R-Law)과 유해성 법칙(H-Law)을 통해 적대적 입력과 정상 입력을 구분하고, 입력 표현을 조정합니다. 실험 결과, AdaSteer는 다양한 탈옥 공격에서 기존 방법보다 우수한 성능을 보이며, 정상 입력 처리에는 최소한의 영향을 미칩니다. 이 연구는 LLM의 실시간 안전성 강화를 위한 해석 가능한 모델 내부 구조의 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. AdaSteer는 입력 특성에 따라 모델의 행동을 동적으로 조정하는 적응형 활성화 조정 방법을 제안합니다.
- 2. R-Law와 H-Law를 통해 공격적 입력과 정상 입력을 구분하고, 적응형 계수를 사용하여 모델의 안전성을 강화합니다.
- 3. AdaSteer는 LLaMA-3.1, Gemma-2, Qwen2.5 모델에서 다양한 공격에 대해 기존 방법보다 우수한 성능을 보였습니다.
- 4. 이 연구는 해석 가능한 모델 내부 구조를 활용하여 실시간으로 유연한 안전성 강화를 가능하게 합니다.
- 5. AdaSteer는 고정된 조정 계수의 한계를 극복하여 정상 입력의 거부를 최소화하면서도 강력한 방어를 제공합니다.


---

*Generated on 2025-09-23 11:52:09*