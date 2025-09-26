---
keywords:
  - Pickle-based Models
  - Hugging Face Model Hub
  - Model Scanners
  - Malware
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2508.15987
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:22:50.915683",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Pickle-based Models",
    "Hugging Face Model Hub",
    "Model Scanners",
    "Malware"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Pickle-based Models": 0.78,
    "Hugging Face Model Hub": 0.85,
    "Model Scanners": 0.8,
    "Malware": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Pickle-based Machine Learning Models",
        "canonical": "Pickle-based Models",
        "aliases": [
          "Pickle Models",
          "Pickle ML Models"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on secure deserialization and is unique to the context of model security.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hugging Face Model Hub",
        "canonical": "Hugging Face Model Hub",
        "aliases": [
          "HF Model Hub",
          "Hugging Face Hub"
        ],
        "category": "specific_connectable",
        "rationale": "The Hugging Face Model Hub is a key platform for model exchange, making it relevant for linking to discussions on model repositories.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Model Scanners",
        "canonical": "Model Scanners",
        "aliases": [
          "Model Security Scanners"
        ],
        "category": "unique_technical",
        "rationale": "Model scanners are crucial for detecting malicious models, directly relating to the paper's security theme.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Malware",
        "canonical": "Malware",
        "aliases": [
          "Malicious Software"
        ],
        "category": "broad_technical",
        "rationale": "Malware is a fundamental concept in cybersecurity, relevant to the paper's focus on model threats.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
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
      "candidate_surface": "Pickle-based Machine Learning Models",
      "resolved_canonical": "Pickle-based Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hugging Face Model Hub",
      "resolved_canonical": "Hugging Face Model Hub",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Model Scanners",
      "resolved_canonical": "Model Scanners",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Malware",
      "resolved_canonical": "Malware",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# PickleBall: Secure Deserialization of Pickle-based Machine Learning Models (Extended Report)

**Korean Title:** 피클볼: 피클 기반 머신러닝 모델의 안전한 역직렬화 (확장 보고서)

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2508.15987.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2508.15987](https://arxiv.org/abs/2508.15987)

## 🔗 유사한 논문
- [[2025-09-22/When Secure Isn't_ Assessing the Security of Machine Learning Model Sharing_20250922|When Secure Isn't: Assessing the Security of Machine Learning Model Sharing]] (82.7% similar)
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (82.0% similar)
- [[2025-09-22/Red Teaming Multimodal Language Models_ Evaluating Harm Across Prompt Modalities and Models_20250922|Red Teaming Multimodal Language Models: Evaluating Harm Across Prompt Modalities and Models]] (79.9% similar)
- [[2025-09-19/Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (79.3% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Malware|Malware]]
**🔗 Specific Connectable**: [[keywords/Hugging Face Model Hub|Hugging Face Model Hub]]
**⚡ Unique Technical**: [[keywords/Pickle-based Models|Pickle-based Models]], [[keywords/Model Scanners|Model Scanners]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15987v2 Announce Type: replace-cross 
Abstract: Machine learning model repositories such as the Hugging Face Model Hub facilitate model exchanges. However, bad actors can deliver malware through compromised models. Existing defenses such as safer model formats, restrictive (but inflexible) loading policies, and model scanners have shortcomings: 44.9% of popular models on Hugging Face still use the insecure pickle format, 15% of these cannot be loaded by restrictive loading policies, and model scanners have both false positives and false negatives. Pickle remains the de facto standard for model exchange, and the ML community lacks a tool that offers transparent safe loading.
  We present PickleBall to help machine learning engineers load pickle-based models safely. PickleBall statically analyzes the source code of a given machine learning library and computes a custom policy that specifies a safe load-time behavior for benign models. PickleBall then dynamically enforces the policy during load time as a drop-in replacement for the pickle module. PickleBall generates policies that correctly load 79.8% of benign pickle-based models in our dataset, while rejecting all (100%) malicious examples in our dataset. In comparison, evaluated model scanners fail to identify known malicious models, and the state-of-art loader loads 22% fewer benign models than PickleBall. PickleBall removes the threat of arbitrary function invocation from malicious pickle-based models, raising the bar for attackers to depend on code reuse techniques.

## 🔍 Abstract (한글 번역)

arXiv:2508.15987v2 발표 유형: 교차 교체  
초록: Hugging Face Model Hub과 같은 머신 러닝 모델 저장소는 모델 교환을 용이하게 합니다. 그러나 악의적인 행위자는 손상된 모델을 통해 악성 소프트웨어를 전달할 수 있습니다. 안전한 모델 형식, 제한적(그러나 유연하지 않은) 로딩 정책, 모델 스캐너와 같은 기존 방어책에는 단점이 있습니다. Hugging Face의 인기 있는 모델 중 44.9%가 여전히 안전하지 않은 pickle 형식을 사용하고 있으며, 이 중 15%는 제한적인 로딩 정책으로 로드할 수 없으며, 모델 스캐너는 오탐지와 미탐지가 모두 존재합니다. Pickle은 여전히 모델 교환의 사실상 표준이며, ML 커뮤니티는 투명하고 안전한 로딩을 제공하는 도구가 부족합니다.

우리는 머신 러닝 엔지니어들이 pickle 기반 모델을 안전하게 로드할 수 있도록 돕기 위해 PickleBall을 제안합니다. PickleBall은 주어진 머신 러닝 라이브러리의 소스 코드를 정적으로 분석하고, 정상적인 모델에 대한 안전한 로드 타임 동작을 명시하는 맞춤형 정책을 계산합니다. 그런 다음 PickleBall은 pickle 모듈의 대체물로서 로드 시간 동안 정책을 동적으로 시행합니다. PickleBall은 우리의 데이터셋에서 79.8%의 정상적인 pickle 기반 모델을 올바르게 로드하는 정책을 생성하며, 데이터셋의 모든(100%) 악성 예제를 거부합니다. 비교해보면, 평가된 모델 스캐너는 알려진 악성 모델을 식별하지 못하고, 최신 로더는 PickleBall보다 22% 적은 정상 모델을 로드합니다. PickleBall은 악성 pickle 기반 모델의 임의 함수 호출 위협을 제거하여 공격자가 코드 재사용 기술에 의존해야 하는 장벽을 높입니다.

## 📝 요약

이 논문은 머신러닝 모델 저장소에서 악성 소프트웨어의 위험을 줄이기 위한 도구인 PickleBall을 소개합니다. 기존의 방어책은 불완전하며, 특히 Hugging Face의 인기 모델 중 44.9%가 취약한 pickle 포맷을 사용합니다. PickleBall은 머신러닝 라이브러리의 소스 코드를 정적으로 분석하여 안전한 로딩 정책을 생성하고, 이를 로딩 시 동적으로 적용합니다. 실험 결과, PickleBall은 79.8%의 정상 모델을 올바르게 로드하고, 모든 악성 모델을 차단했습니다. 이는 기존 스캐너와 로더보다 뛰어난 성능을 보여줍니다.

## 🎯 주요 포인트

- 1. 머신러닝 모델 저장소에서 악성코드가 포함된 모델이 유통될 수 있는 위험이 존재합니다.
- 2. 기존의 방어책은 불완전하며, 특히 Hugging Face의 인기 모델 중 44.9%가 여전히 안전하지 않은 pickle 포맷을 사용하고 있습니다.
- 3. PickleBall은 머신러닝 엔지니어가 pickle 기반 모델을 안전하게 로드할 수 있도록 돕는 도구로, 악성 모델을 100% 차단하면서도 79.8%의 정상 모델을 올바르게 로드합니다.
- 4. PickleBall은 로드 시간 동안 안전한 동작을 보장하는 정책을 동적으로 적용하여 악성 코드의 임의 함수 호출 위협을 제거합니다.
- 5. PickleBall은 기존의 모델 스캐너보다 더 높은 정확도로 악성 모델을 식별하며, 최신 로더보다 더 많은 정상 모델을 로드할 수 있습니다.


---

*Generated on 2025-09-23 11:22:50*