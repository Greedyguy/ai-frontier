---
keywords:
  - Large Language Model
  - Jailbreak Attacks
  - Surrogate Classifier
  - Model Alignment
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2501.16534
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:43:31.559133",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Jailbreak Attacks",
    "Surrogate Classifier",
    "Model Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Jailbreak Attacks": 0.8,
    "Surrogate Classifier": 0.78,
    "Model Alignment": 0.82
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion, connecting to a broad range of related research.",
        "novelty_score": 0.3,
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
        "rationale": "A specific type of attack discussed in the paper, relevant for security-focused research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "surrogate classifier",
        "canonical": "Surrogate Classifier",
        "aliases": [
          "approximate classifier"
        ],
        "category": "unique_technical",
        "rationale": "Key concept introduced in the paper, important for understanding the methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "alignment",
        "canonical": "Model Alignment",
        "aliases": [
          "alignment"
        ],
        "category": "specific_connectable",
        "rationale": "Alignment is crucial for ensuring model safety, a central theme of the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "safety classifier",
      "attack success rate"
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
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "surrogate classifier",
      "resolved_canonical": "Surrogate Classifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "alignment",
      "resolved_canonical": "Model Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2501.16534.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2501.16534](https://arxiv.org/abs/2501.16534)

## 🔗 유사한 논문
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (90.1% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (89.1% similar)
- [[2025-09-23/AdaptiveGuard_ Towards Adaptive Runtime Safety for LLM-Powered Software_20250923|AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software]] (87.7% similar)
- [[2025-09-18/LLM Jailbreak Detection for (Almost) Free!_20250918|LLM Jailbreak Detection for (Almost) Free!]] (87.6% similar)
- [[2025-09-23/Large Language Models for Cyber Security_ A Systematic Literature Review_20250923|Large Language Models for Cyber Security: A Systematic Literature Review]] (86.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Model Alignment|Model Alignment]]
**⚡ Unique Technical**: [[keywords/Jailbreak Attacks|Jailbreak Attacks]], [[keywords/Surrogate Classifier|Surrogate Classifier]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.16534v2 Announce Type: replace-cross 
Abstract: Alignment in large language models (LLMs) is used to enforce guidelines such as safety. Yet, alignment fails in the face of jailbreak attacks that modify inputs to induce unsafe outputs. In this paper, we introduce and evaluate a new technique for jailbreak attacks. We observe that alignment embeds a safety classifier in the LLM responsible for deciding between refusal and compliance, and seek to extract an approximation of this classifier: a surrogate classifier. To this end, we build candidate classifiers from subsets of the LLM. We first evaluate the degree to which candidate classifiers approximate the LLM's safety classifier in benign and adversarial settings. Then, we attack the candidates and measure how well the resulting adversarial inputs transfer to the LLM. Our evaluation shows that the best candidates achieve accurate agreement (an F1 score above 80%) using as little as 20% of the model architecture. Further, we find that attacks mounted on the surrogate classifiers can be transferred to the LLM with high success. For example, a surrogate using only 50% of the Llama 2 model achieved an attack success rate (ASR) of 70% with half the memory footprint and runtime -- a substantial improvement over attacking the LLM directly, where we only observed a 22% ASR. These results show that extracting surrogate classifiers is an effective and efficient means for modeling (and therein addressing) the vulnerability of aligned models to jailbreaking attacks.

## 📝 요약

이 논문에서는 대형 언어 모델(LLM)의 정렬을 우회하는 새로운 탈옥 공격 기법을 소개하고 평가합니다. 연구진은 LLM 내에 내장된 안전 분류기를 근사하는 대리 분류기를 추출하여 공격을 수행합니다. 후보 분류기를 LLM의 일부로부터 구축하고, 이들이 안전 분류기를 얼마나 잘 근사하는지 평가한 후, 대리 분류기에 대한 공격을 통해 LLM에 전이되는지를 측정합니다. 결과적으로, 모델 구조의 20%만으로도 높은 정확도의 대리 분류기를 구축할 수 있었으며, Llama 2 모델의 50%를 사용한 대리 분류기는 70%의 공격 성공률을 기록했습니다. 이는 직접 LLM을 공격했을 때보다 훨씬 높은 성공률로, 대리 분류기를 활용한 공격이 효율적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 정렬은 안전성 등의 지침을 강제하기 위해 사용되지만, 정렬은 입력을 수정하여 안전하지 않은 출력을 유도하는 탈옥 공격에 취약하다.
- 2. 본 논문에서는 탈옥 공격을 위한 새로운 기법을 소개하고 평가하며, LLM의 안전 분류기를 근사화한 대리 분류기를 추출하는 방법을 제안한다.
- 3. 대리 분류기를 사용한 공격은 LLM에 높은 성공률로 전이될 수 있으며, Llama 2 모델의 50%만 사용한 대리 분류기는 70%의 공격 성공률을 달성했다.
- 4. 대리 분류기를 추출하는 것은 정렬된 모델의 탈옥 공격 취약성을 모델링하고 해결하는 효과적이고 효율적인 방법임을 보여준다.


---

*Generated on 2025-09-24 00:43:31*