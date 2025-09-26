---
keywords:
  - Referring Expression Segmentation
  - Adversarial Examples
  - Multimodal Learning
  - Vision-Language Model
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2506.16157
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:25:03.288843",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Referring Expression Segmentation",
    "Adversarial Examples",
    "Multimodal Learning",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Referring Expression Segmentation": 0.78,
    "Adversarial Examples": 0.8,
    "Multimodal Learning": 0.77,
    "Vision-Language Model": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Referring Expression Segmentation",
        "canonical": "Referring Expression Segmentation",
        "aliases": [
          "RES"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and represents a specific task in vision-language systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adversarial Examples",
        "canonical": "Adversarial Examples",
        "aliases": [
          "Adversarial Attacks"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial examples are crucial for understanding model vulnerabilities, linking to security in AI systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Structure",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal learning is essential for integrating vision and language, a key aspect of the discussed models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Vision-Language Systems",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Integration"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are central to the paper's theme, focusing on integrating visual and textual data.",
        "novelty_score": 0.48,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "object segmentation",
      "natural language descriptions",
      "privacy protection"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Referring Expression Segmentation",
      "resolved_canonical": "Referring Expression Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adversarial Examples",
      "resolved_canonical": "Adversarial Examples",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Structure",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Vision-Language Systems",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Proxy-Embedding as an Adversarial Teacher: An Embedding-Guided Bidirectional Attack for Referring Expression Segmentation Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.16157.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2506.16157](https://arxiv.org/abs/2506.16157)

## 🔗 유사한 논문
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (82.0% similar)
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (82.0% similar)
- [[2025-09-23/ADVEDM_Fine-grained Adversarial Attack against VLM-based Embodied Agents_20250923|ADVEDM:Fine-grained Adversarial Attack against VLM-based Embodied Agents]] (81.0% similar)
- [[2025-09-22/Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models_20250922|Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models]] (80.7% similar)
- [[2025-09-23/Beyond Prompting_ An Efficient Embedding Framework for Open-Domain Question Answering_20250923|Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Adversarial Examples|Adversarial Examples]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Referring Expression Segmentation|Referring Expression Segmentation]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.16157v2 Announce Type: replace 
Abstract: Referring Expression Segmentation (RES) enables precise object segmentation in images based on natural language descriptions, offering high flexibility and broad applicability in real-world vision tasks. Despite its impressive performance, the robustness of RES models against adversarial examples remains largely unexplored. While prior adversarial attack methods have explored adversarial robustness on conventional segmentation models, they perform poorly when directly applied to RES models, failing to expose vulnerabilities in its multimodal structure. In practical open-world scenarios, users typically issue multiple, diverse referring expressions to interact with the same image, highlighting the need for adversarial examples that generalize across varied textual inputs. Furthermore, from the perspective of privacy protection, ensuring that RES models do not segment sensitive content without explicit authorization is a crucial aspect of enhancing the robustness and security of multimodal vision-language systems. To address these challenges, we present PEAT, an Embedding-Guided Bidirectional Attack for RES models. Extensive experiments across multiple RES architectures and standard benchmarks show that PEAT consistently outperforms competitive baselines.

## 📝 요약

이 논문은 자연어 설명을 기반으로 이미지 내 객체를 정확하게 분할하는 기술인 지시 표현 분할(RES)의 취약점을 탐구합니다. 기존의 적대적 공격 방법은 RES 모델의 다중 모달 구조의 취약점을 충분히 드러내지 못했습니다. 본 연구에서는 다양한 텍스트 입력에 대해 일반화할 수 있는 적대적 예제를 제시할 필요성을 강조하며, 이를 해결하기 위해 PEAT라는 임베딩 기반 양방향 공격 방법을 제안합니다. 여러 RES 아키텍처와 표준 벤치마크에서 실험한 결과, PEAT는 경쟁 방법들보다 일관되게 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 자연어 설명을 기반으로 이미지에서 객체를 정확하게 분할하는 참조 표현 분할(RES)은 실제 비전 작업에서 높은 유연성과 넓은 적용성을 제공합니다.
- 2. 기존의 적대적 공격 방법은 RES 모델의 다중 모달 구조의 취약성을 드러내지 못하여, RES 모델에 직접 적용할 경우 성능이 저조합니다.
- 3. 다양한 텍스트 입력에 대해 일반화된 적대적 예제를 생성하는 것이 중요하며, 이는 실제 오픈월드 시나리오에서 사용자가 동일한 이미지에 대해 여러 참조 표현을 발행하는 경우에 필요합니다.
- 4. 프라이버시 보호 관점에서, RES 모델이 명시적 승인 없이 민감한 콘텐츠를 분할하지 않도록 보장하는 것이 다중 모달 비전-언어 시스템의 견고성과 보안을 강화하는 데 중요합니다.
- 5. PEAT는 RES 모델을 위한 임베딩 기반 양방향 공격 방법으로, 여러 RES 아키텍처와 표준 벤치마크에서 경쟁력 있는 기준선을 일관되게 능가하는 성능을 보입니다.


---

*Generated on 2025-09-24 05:25:03*