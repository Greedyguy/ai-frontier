---
keywords:
  - Large Language Model
  - Jailbreak Attacks
  - Out-of-Distribution Detection
  - Continual Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16861
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:36:21.359532",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Jailbreak Attacks",
    "Out-of-Distribution Detection",
    "Continual Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Jailbreak Attacks": 0.78,
    "Out-of-Distribution Detection": 0.82,
    "Continual Learning": 0.8
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
        "rationale": "Large Language Models are central to the paper's focus on adaptive guardrails, linking to broader discussions in AI safety.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "jailbreak attacks",
        "canonical": "Jailbreak Attacks",
        "aliases": [
          "jailbreaking"
        ],
        "category": "unique_technical",
        "rationale": "Jailbreak attacks are a specific threat addressed by the proposed AdaptiveGuard, highlighting a unique area of security concern.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "out-of-distribution inputs",
        "canonical": "Out-of-Distribution Detection",
        "aliases": [
          "OOD inputs"
        ],
        "category": "specific_connectable",
        "rationale": "Out-of-distribution detection is crucial for AdaptiveGuard's adaptive capabilities, connecting to broader machine learning challenges.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "continual learning framework",
        "canonical": "Continual Learning",
        "aliases": [
          "continuous learning"
        ],
        "category": "specific_connectable",
        "rationale": "Continual learning is key to AdaptiveGuard's ability to adapt to new threats, linking to ongoing research in adaptive systems.",
        "novelty_score": 0.7,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Guardrails",
      "AdaptiveGuard"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
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
      "candidate_surface": "out-of-distribution inputs",
      "resolved_canonical": "Out-of-Distribution Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "continual learning framework",
      "resolved_canonical": "Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16861.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16861](https://arxiv.org/abs/2509.16861)

## 🔗 유사한 논문
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (88.0% similar)
- [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (86.8% similar)
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (85.6% similar)
- [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (85.0% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Out-of-Distribution Detection|Out-of-Distribution Detection]], [[keywords/Continual Learning|Continual Learning]]
**⚡ Unique Technical**: [[keywords/Jailbreak Attacks|Jailbreak Attacks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16861v1 Announce Type: cross 
Abstract: Guardrails are critical for the safe deployment of Large Language Models (LLMs)-powered software. Unlike traditional rule-based systems with limited, predefined input-output spaces that inherently constrain unsafe behavior, LLMs enable open-ended, intelligent interactions--opening the door to jailbreak attacks through user inputs. Guardrails serve as a protective layer, filtering unsafe prompts before they reach the LLM. However, prior research shows that jailbreak attacks can still succeed over 70% of the time, even against advanced models like GPT-4o. While guardrails such as LlamaGuard report up to 95% accuracy, our preliminary analysis shows their performance can drop sharply--to as low as 12%--when confronted with unseen attacks. This highlights a growing software engineering challenge: how to build a post-deployment guardrail that adapts dynamically to emerging threats? To address this, we propose AdaptiveGuard, an adaptive guardrail that detects novel jailbreak attacks as out-of-distribution (OOD) inputs and learns to defend against them through a continual learning framework. Through empirical evaluation, AdaptiveGuard achieves 96% OOD detection accuracy, adapts to new attacks in just two update steps, and retains over 85% F1-score on in-distribution data post-adaptation, outperforming other baselines. These results demonstrate that AdaptiveGuard is a guardrail capable of evolving in response to emerging jailbreak strategies post deployment. We release our AdaptiveGuard and studied datasets at https://github.com/awsm-research/AdaptiveGuard to support further research.

## 📝 요약

이 논문은 대형 언어 모델(LLM) 기반 소프트웨어의 안전한 배포를 위한 보호 장치의 중요성을 다룹니다. 기존의 규칙 기반 시스템과 달리 LLM은 개방형 상호작용을 가능하게 하여 사용자 입력을 통한 보안 침해 가능성을 높입니다. 기존 보호 장치들은 새로운 공격에 취약하며, 성능이 급격히 저하될 수 있습니다. 이를 해결하기 위해 제안된 AdaptiveGuard는 새로운 공격을 비정상 입력으로 감지하고 지속적인 학습을 통해 방어하는 적응형 보호 장치입니다. 실험 결과, AdaptiveGuard는 96%의 비정상 입력 감지 정확도를 보이며, 두 번의 업데이트로 새로운 공격에 적응하고, 기존 데이터에 대해 85% 이상의 F1-score를 유지합니다. 이러한 결과는 AdaptiveGuard가 배포 후에도 진화하는 보안 위협에 대응할 수 있음을 보여줍니다. 연구팀은 AdaptiveGuard와 관련 데이터셋을 공개하여 추가 연구를 지원합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 안전한 배포를 위해 가드레일이 중요하며, 이는 사용자 입력을 통한 탈옥 공격을 방지하는 보호층 역할을 한다.
- 2. 기존의 가드레일 시스템은 새로운 공격에 직면했을 때 성능이 급격히 떨어질 수 있으며, 이는 소프트웨어 엔지니어링의 새로운 도전 과제이다.
- 3. AdaptiveGuard는 새로운 탈옥 공격을 비분포 입력으로 감지하고, 지속적인 학습을 통해 방어하는 적응형 가드레일로 제안되었다.
- 4. AdaptiveGuard는 96%의 비분포 감지 정확도를 달성하고, 두 번의 업데이트로 새로운 공격에 적응하며, 적응 후에도 85% 이상의 F1-score를 유지한다.
- 5. 연구 결과 AdaptiveGuard는 배포 후에도 새로운 탈옥 전략에 대응할 수 있는 진화 가능한 가드레일임을 보여준다.


---

*Generated on 2025-09-23 23:36:21*