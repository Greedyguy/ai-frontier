---
keywords:
  - Implicit Hate Speech Detection
  - Attention Mechanism
  - Named Entity Recognition
  - Self-supervised Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2505.19528
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:59:51.164027",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Implicit Hate Speech Detection",
    "Attention Mechanism",
    "Named Entity Recognition",
    "Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Implicit Hate Speech Detection": 0.78,
    "Attention Mechanism": 0.85,
    "Named Entity Recognition": 0.8,
    "Self-supervised Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Implicit Hate Speech Detection",
        "canonical": "Implicit Hate Speech Detection",
        "aliases": [
          "Implicit Hate Detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task that connects to research on hate speech and its detection methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Attention-Based Relationships",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Patterns"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for understanding the relational dynamics in NLP tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Named Entity Recognition",
        "canonical": "Named Entity Recognition",
        "aliases": [
          "NER"
        ],
        "category": "broad_technical",
        "rationale": "NER is a foundational NLP task that supports the identification of explicit targets in text.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Contrastive Methods"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive learning is a popular self-supervised approach relevant to distinguishing between classes.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
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
      "candidate_surface": "Implicit Hate Speech Detection",
      "resolved_canonical": "Implicit Hate Speech Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Attention-Based Relationships",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Named Entity Recognition",
      "resolved_canonical": "Named Entity Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# AmpleHate: Amplifying the Attention for Versatile Implicit Hate Detection

**Korean Title:** AmpleHate: 다재다능한 암묵적 혐오 감지를 위한 주의 증폭

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.19528.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2505.19528](https://arxiv.org/abs/2505.19528)

## 🔗 유사한 논문
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (81.5% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (80.7% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (80.4% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (80.0% similar)
- [[2025-09-22/KatFishNet_ Detecting LLM-Generated Korean Text through Linguistic Feature Analysis_20250922|KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Named Entity Recognition|Named Entity Recognition]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Implicit Hate Speech Detection|Implicit Hate Speech Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19528v3 Announce Type: replace-cross 
Abstract: Implicit hate speech detection is challenging due to its subtlety and reliance on contextual interpretation rather than explicit offensive words. Current approaches rely on contrastive learning, which are shown to be effective on distinguishing hate and non-hate sentences. Humans, however, detect implicit hate speech by first identifying specific targets within the text and subsequently interpreting how these target relate to their surrounding context. Motivated by this reasoning process, we propose AmpleHate, a novel approach designed to mirror human inference for implicit hate detection. AmpleHate identifies explicit target using a pretrained Named Entity Recognition model and capture implicit target information via [CLS] tokens. It computes attention-based relationships between explicit, implicit targets and sentence context and then, directly injects these relational vectors into the final sentence representation. This amplifies the critical signals of target-context relations for determining implicit hate. Experiments demonstrate that AmpleHate achieves state-of-the-art performance, outperforming contrastive learning baselines by an average of 82.14% and achieve faster convergence. Qualitative analyses further reveal that attention patterns produced by AmpleHate closely align with human judgement, underscoring its interpretability and robustness. Our code is publicly available at: https://github.com/leeyejin1231/AmpleHate.

## 🔍 Abstract (한글 번역)

arXiv:2505.19528v3 발표 유형: 교체-교차  
초록: 암시적 혐오 발언 탐지는 그 미묘함과 명시적인 공격적 단어보다는 맥락적 해석에 의존하기 때문에 어려운 과제입니다. 현재의 접근법은 대조 학습에 의존하며, 이는 혐오 문장과 비혐오 문장을 구별하는 데 효과적임이 입증되었습니다. 그러나 인간은 먼저 텍스트 내 특정 대상을 식별하고, 그 후 이러한 대상이 주변 맥락과 어떻게 관련되는지를 해석함으로써 암시적 혐오 발언을 탐지합니다. 이러한 추론 과정을 바탕으로, 우리는 암시적 혐오 탐지를 위한 인간의 추론을 반영하도록 설계된 새로운 접근법인 AmpleHate를 제안합니다. AmpleHate는 사전 훈련된 개체명 인식 모델을 사용하여 명시적 대상을 식별하고, [CLS] 토큰을 통해 암시적 대상 정보를 캡처합니다. 그런 다음 명시적, 암시적 대상과 문장 맥락 간의 주의 기반 관계를 계산하고, 이러한 관계 벡터를 최종 문장 표현에 직접 주입합니다. 이는 암시적 혐오를 결정하기 위한 대상-맥락 관계의 중요한 신호를 증폭시킵니다. 실험 결과, AmpleHate는 대조 학습 기반을 평균 82.14% 초과하며, 더 빠른 수렴을 달성하여 최첨단 성능을 보여줍니다. 질적 분석은 또한 AmpleHate에 의해 생성된 주의 패턴이 인간의 판단과 밀접하게 일치함을 드러내어, 그 해석 가능성과 견고성을 강조합니다. 우리의 코드는 다음에서 공개적으로 이용 가능합니다: https://github.com/leeyejin1231/AmpleHate.

## 📝 요약

이 논문은 암묵적 혐오 발언 탐지의 어려움을 해결하기 위해 AmpleHate라는 새로운 접근법을 제안합니다. 기존의 대조 학습 방법은 혐오와 비혐오 문장을 구별하는 데 효과적이지만, AmpleHate는 인간의 추론 과정을 모방하여 명시적 및 암묵적 대상을 식별하고, 문맥과의 관계를 주의 기반으로 분석합니다. 이를 통해 문장의 최종 표현에 관계 벡터를 직접 주입하여 암묵적 혐오를 효과적으로 탐지합니다. 실험 결과, AmpleHate는 대조 학습 기반을 평균 82.14% 초과하며, 빠른 수렴 속도를 보입니다. 또한, 주의 패턴이 인간의 판단과 유사하여 해석 가능성과 견고성을 강조합니다.

## 🎯 주요 포인트

- 1. 암묵적 증오 발언 탐지는 명시적인 공격적 단어보다는 맥락적 해석에 의존하여 도전적이다.
- 2. AmpleHate는 명시적 타겟을 식별하고, 암묵적 타겟 정보를 [CLS] 토큰을 통해 포착하여 인간의 추론 방식을 모방한다.
- 3. AmpleHate는 명시적, 암묵적 타겟과 문장 맥락 간의 주의 기반 관계를 계산하여 최종 문장 표현에 직접 주입한다.
- 4. 실험 결과, AmpleHate는 기존의 대조 학습 기법을 평균 82.14% 상회하며, 더 빠른 수렴 속도를 보인다.
- 5. AmpleHate의 주의 패턴은 인간의 판단과 밀접하게 일치하여 해석 가능성과 견고성을 강조한다.


---

*Generated on 2025-09-23 09:59:51*