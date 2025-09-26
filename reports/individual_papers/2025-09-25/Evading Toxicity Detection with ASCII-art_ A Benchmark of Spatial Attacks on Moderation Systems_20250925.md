---
keywords:
  - Toxicity Detection
  - ASCII Art
  - Adversarial Attacks
  - Large Language Model
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2409.18708
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:16:52.816214",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Toxicity Detection",
    "ASCII Art",
    "Adversarial Attacks",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Toxicity Detection": 0.85,
    "ASCII Art": 0.8,
    "Adversarial Attacks": 0.9,
    "Large Language Model": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "toxicity detection",
        "canonical": "Toxicity Detection",
        "aliases": [
          "toxicity classifier",
          "harmful content detection"
        ],
        "category": "unique_technical",
        "rationale": "Toxicity detection is a specific application area that connects to moderation and NLP systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "ASCII art",
        "canonical": "ASCII Art",
        "aliases": [
          "text art",
          "character art"
        ],
        "category": "unique_technical",
        "rationale": "ASCII art represents a unique form of input that challenges standard text processing models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "adversarial attacks",
        "canonical": "Adversarial Attacks",
        "aliases": [
          "attack strategies",
          "adversarial methods"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial attacks are crucial for understanding vulnerabilities in AI systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.9
      },
      {
        "surface": "large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "language model"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are central to modern NLP and connect to a wide range of applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "moderation systems",
      "state-of-the-art",
      "robustness"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "toxicity detection",
      "resolved_canonical": "Toxicity Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ASCII art",
      "resolved_canonical": "ASCII Art",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "adversarial attacks",
      "resolved_canonical": "Adversarial Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# Evading Toxicity Detection with ASCII-art: A Benchmark of Spatial Attacks on Moderation Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.18708.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2409.18708](https://arxiv.org/abs/2409.18708)

## 🔗 유사한 논문
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (83.8% similar)
- [[2025-09-25/Semantic Representation Attack against Aligned Large Language Models_20250925|Semantic Representation Attack against Aligned Large Language Models]] (83.1% similar)
- [[2025-09-24/T-Detect_ Tail-Aware Statistical Normalization for Robust Detection of Adversarial Machine-Generated Text_20250924|T-Detect: Tail-Aware Statistical Normalization for Robust Detection of Adversarial Machine-Generated Text]] (82.6% similar)
- [[2025-09-24/Algorithms for Adversarially Robust Deep Learning_20250924|Algorithms for Adversarially Robust Deep Learning]] (82.3% similar)
- [[2025-09-24/Backdoor Attack with Invisible Triggers Based on Model Architecture Modification_20250924|Backdoor Attack with Invisible Triggers Based on Model Architecture Modification]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Adversarial Attacks|Adversarial Attacks]]
**⚡ Unique Technical**: [[keywords/Toxicity Detection|Toxicity Detection]], [[keywords/ASCII Art|ASCII Art]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.18708v5 Announce Type: replace-cross 
Abstract: We introduce a novel class of adversarial attacks on toxicity detection models that exploit language models' failure to interpret spatially structured text in the form of ASCII art. To evaluate the effectiveness of these attacks, we propose ToxASCII, a benchmark designed to assess the robustness of toxicity detection systems against visually obfuscated inputs. Our attacks achieve a perfect Attack Success Rate (ASR) across a diverse set of state-of-the-art large language models and dedicated moderation tools, revealing a significant vulnerability in current text-only moderation systems.

## 📝 요약

이 논문은 ASCII 아트를 활용하여 텍스트의 공간적 구조를 해석하지 못하는 언어 모델의 취약점을 이용한 새로운 유형의 적대적 공격을 소개합니다. 이러한 공격의 효과를 평가하기 위해 ToxASCII라는 벤치마크를 제안하여 시각적으로 난독화된 입력에 대한 독성 탐지 시스템의 견고성을 평가합니다. 이 공격은 다양한 최신 대형 언어 모델과 전용 모더레이션 도구에서 완벽한 공격 성공률을 달성하여 현재 텍스트 기반 모더레이션 시스템의 중요한 취약성을 드러냅니다.

## 🎯 주요 포인트

- 1. ASCII 아트를 활용한 새로운 유형의 적대적 공격이 독성 탐지 모델의 취약점을 노린다.
- 2. ToxASCII라는 벤치마크를 제안하여 시각적으로 난독화된 입력에 대한 독성 탐지 시스템의 강인성을 평가한다.
- 3. 제안된 공격은 다양한 최신 대형 언어 모델과 전용 중재 도구에 대해 완벽한 공격 성공률(ASR)을 달성한다.
- 4. 현재의 텍스트 전용 중재 시스템에 중요한 취약점이 있음을 드러낸다.


---

*Generated on 2025-09-25 16:16:52*