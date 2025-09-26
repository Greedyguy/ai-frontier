---
keywords:
  - Multimodal Learning
  - Adversarial Attacks
  - Ethical AI
  - AI Safety
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15478
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:29:19.503693",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Adversarial Attacks",
    "Ethical AI",
    "AI Safety"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Adversarial Attacks": 0.77,
    "Ethical AI": 0.78,
    "AI Safety": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal large language models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the growing field of integrating multiple data modalities in language models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "adversarial prompts",
        "canonical": "Adversarial Attacks",
        "aliases": [
          "adversarial inputs"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the challenges in model robustness against adversarial inputs.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.77
      },
      {
        "surface": "harm categories",
        "canonical": "Ethical AI",
        "aliases": [
          "AI ethics",
          "harm assessment"
        ],
        "category": "evolved_concepts",
        "rationale": "Relates to the ethical implications of AI outputs, a critical area of study.",
        "novelty_score": 0.72,
        "connectivity_score": 0.76,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "safety mechanisms",
        "canonical": "AI Safety",
        "aliases": [
          "safety protocols",
          "safety measures"
        ],
        "category": "broad_technical",
        "rationale": "Addresses the implementation of safety protocols in AI systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "model outputs",
      "statistical analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal large language models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "adversarial prompts",
      "resolved_canonical": "Adversarial Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "harm categories",
      "resolved_canonical": "Ethical AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.76,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "safety mechanisms",
      "resolved_canonical": "AI Safety",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Red Teaming Multimodal Language Models: Evaluating Harm Across Prompt Modalities and Models

**Korean Title:** 다중 모달 언어 모델의 레드 팀 작업: 프롬프트 모달리티와 모델 전반에 걸친 해악 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15478.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15478](https://arxiv.org/abs/2509.15478)

## 🔗 유사한 논문
- [[2025-09-18/Is GPT-4o mini Blinded by its Own Safety Filters? Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection_20250918|Is GPT-4o mini Blinded by its Own Safety Filters? Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection]] (86.1% similar)
- [[2025-09-22/From Judgment to Interference_ Early Stopping LLM Harmful Outputs via Streaming Content Monitoring_20250922|From Judgment to Interference: Early Stopping LLM Harmful Outputs via Streaming Content Monitoring]] (85.7% similar)
- [[2025-09-22/Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study_20250922|Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study]] (85.1% similar)
- [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (84.5% similar)
- [[2025-09-19/Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/AI Safety|AI Safety]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Adversarial Attacks|Adversarial Attacks]]
**🚀 Evolved Concepts**: [[keywords/Ethical AI|Ethical AI]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15478v1 Announce Type: new 
Abstract: Multimodal large language models (MLLMs) are increasingly used in real world applications, yet their safety under adversarial conditions remains underexplored. This study evaluates the harmlessness of four leading MLLMs (GPT-4o, Claude Sonnet 3.5, Pixtral 12B, and Qwen VL Plus) when exposed to adversarial prompts across text-only and multimodal formats. A team of 26 red teamers generated 726 prompts targeting three harm categories: illegal activity, disinformation, and unethical behaviour. These prompts were submitted to each model, and 17 annotators rated 2,904 model outputs for harmfulness using a 5-point scale. Results show significant differences in vulnerability across models and modalities. Pixtral 12B exhibited the highest rate of harmful responses (~62%), while Claude Sonnet 3.5 was the most resistant (~10%). Contrary to expectations, text-only prompts were slightly more effective at bypassing safety mechanisms than multimodal ones. Statistical analysis confirmed that both model type and input modality were significant predictors of harmfulness. These findings underscore the urgent need for robust, multimodal safety benchmarks as MLLMs are deployed more widely.

## 🔍 Abstract (한글 번역)

arXiv:2509.15478v1 발표 유형: 신규  
초록: 다중 모달 대형 언어 모델(MLLMs)은 실제 응용에서 점점 더 많이 사용되고 있지만, 적대적 조건에서의 안전성은 여전히 충분히 탐구되지 않았습니다. 본 연구는 텍스트 전용 및 다중 모달 형식에서 적대적 프롬프트에 노출될 때 네 가지 주요 MLLMs(GPT-4o, Claude Sonnet 3.5, Pixtral 12B, Qwen VL Plus)의 무해성을 평가합니다. 26명의 레드 팀원이 불법 활동, 허위 정보, 비윤리적 행동의 세 가지 해악 범주를 목표로 726개의 프롬프트를 생성했습니다. 이러한 프롬프트는 각 모델에 제출되었으며, 17명의 주석자가 5점 척도를 사용하여 2,904개의 모델 출력을 유해성 측면에서 평가했습니다. 결과는 모델 및 모달리티 간의 취약성에 있어 유의미한 차이를 보여줍니다. Pixtral 12B는 가장 높은 유해 응답 비율(~62%)을 보였으며, Claude Sonnet 3.5는 가장 저항력이 있었습니다(~10%). 예상과 달리, 텍스트 전용 프롬프트가 다중 모달 프롬프트보다 안전 메커니즘을 우회하는 데 약간 더 효과적이었습니다. 통계 분석을 통해 모델 유형과 입력 모달리티가 유해성의 중요한 예측 변수임이 확인되었습니다. 이러한 연구 결과는 MLLMs가 더 널리 배포됨에 따라 강력한 다중 모달 안전 벤치마크의 긴급한 필요성을 강조합니다.

## 📝 요약

이 연구는 네 가지 주요 다중모달 대형 언어 모델(MLLMs)의 안전성을 평가했습니다. 26명의 레드 팀이 불법 활동, 허위 정보, 비윤리적 행동을 포함한 세 가지 해악 범주를 목표로 726개의 공격적 프롬프트를 생성했습니다. 각 모델에 대해 2,904개의 출력물을 평가한 결과, Pixtral 12B가 가장 높은 해악 응답률(약 62%)을 보였고, Claude Sonnet 3.5가 가장 저항력이 높았습니다(약 10%). 텍스트 전용 프롬프트가 다중모달 프롬프트보다 안전 메커니즘을 우회하는 데 더 효과적이었습니다. 이 결과는 모델 유형과 입력 방식이 해악성에 중요한 영향을 미친다는 것을 보여주며, MLLMs의 안전성 기준 마련이 시급함을 강조합니다.

## 🎯 주요 포인트

- 1. 본 연구는 네 가지 주요 다중모달 대형 언어 모델(MLLMs)의 안전성을 평가하며, 특히 악의적인 프롬프트에 대한 모델의 반응을 조사했습니다.
- 2. 26명의 레드 팀원이 생성한 726개의 프롬프트를 통해 불법 활동, 허위 정보, 비윤리적 행동의 세 가지 해악 범주를 대상으로 모델의 반응을 평가했습니다.
- 3. Pixtral 12B 모델은 약 62%의 높은 해로운 반응률을 보였으며, Claude Sonnet 3.5 모델은 약 10%로 가장 저항력이 강했습니다.
- 4. 텍스트 전용 프롬프트가 다중모달 프롬프트보다 안전 메커니즘을 우회하는 데 더 효과적이라는 결과가 나왔습니다.
- 5. 연구 결과는 MLLMs의 광범위한 배포에 앞서 강력한 다중모달 안전 기준의 필요성을 강조합니다.


---

*Generated on 2025-09-23 11:29:19*