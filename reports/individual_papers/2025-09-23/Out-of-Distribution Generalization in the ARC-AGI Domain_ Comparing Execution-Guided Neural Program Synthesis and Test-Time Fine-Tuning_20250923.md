---
keywords:
  - Neural Program Synthesis
  - Test-Time Fine-Tuning
  - Out-of-Distribution Generalization
  - ARC-AGI Domain
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2507.15877
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:29:49.523717",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Program Synthesis",
    "Test-Time Fine-Tuning",
    "Out-of-Distribution Generalization",
    "ARC-AGI Domain"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Program Synthesis": 0.78,
    "Test-Time Fine-Tuning": 0.77,
    "Out-of-Distribution Generalization": 0.81,
    "ARC-AGI Domain": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "neural program synthesis",
        "canonical": "Neural Program Synthesis",
        "aliases": [
          "program synthesis",
          "NPS"
        ],
        "category": "unique_technical",
        "rationale": "Neural program synthesis is a specialized technique relevant to the ARC-AGI domain, offering unique insights into compositional generalization.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "test-time fine-tuning",
        "canonical": "Test-Time Fine-Tuning",
        "aliases": [
          "TTFT"
        ],
        "category": "unique_technical",
        "rationale": "Test-time fine-tuning is a distinct approach that enhances model adaptability, crucial for out-of-distribution generalization.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "out-of-distribution generalization",
        "canonical": "Out-of-Distribution Generalization",
        "aliases": [
          "OOD generalization"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the ARC-AGI domain, facilitating connections with other generalization techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "ARC-AGI domain",
        "canonical": "ARC-AGI Domain",
        "aliases": [
          "ARC domain"
        ],
        "category": "unique_technical",
        "rationale": "The ARC-AGI domain is a specific context for studying generalization, providing a unique framework for related research.",
        "novelty_score": 0.72,
        "connectivity_score": 0.62,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "experiment",
      "success",
      "ability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "neural program synthesis",
      "resolved_canonical": "Neural Program Synthesis",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "test-time fine-tuning",
      "resolved_canonical": "Test-Time Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "out-of-distribution generalization",
      "resolved_canonical": "Out-of-Distribution Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "ARC-AGI domain",
      "resolved_canonical": "ARC-AGI Domain",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.62,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Out-of-Distribution Generalization in the ARC-AGI Domain: Comparing Execution-Guided Neural Program Synthesis and Test-Time Fine-Tuning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.15877.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2507.15877](https://arxiv.org/abs/2507.15877)

## 🔗 유사한 논문
- [[2025-09-23/Program Synthesis via Test-Time Transduction_20250923|Program Synthesis via Test-Time Transduction]] (81.4% similar)
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (79.9% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (79.6% similar)
- [[2025-09-17/Class-invariant Test-Time Augmentation for Domain Generalization_20250917|Class-invariant Test-Time Augmentation for Domain Generalization]] (79.6% similar)
- [[2025-09-23/Evaluating Multimodal Large Language Models with Daily Composite Tasks in Home Environments_20250923|Evaluating Multimodal Large Language Models with Daily Composite Tasks in Home Environments]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Out-of-Distribution Generalization|Out-of-Distribution Generalization]]
**⚡ Unique Technical**: [[keywords/Neural Program Synthesis|Neural Program Synthesis]], [[keywords/Test-Time Fine-Tuning|Test-Time Fine-Tuning]], [[keywords/ARC-AGI Domain|ARC-AGI Domain]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.15877v2 Announce Type: replace 
Abstract: We run a controlled compositional generalization experiment in the ARC-AGI domain: an open-world problem domain in which the ability to generalize out-of-distribution is, by design, an essential characteristic for success. We compare neural program synthesis and test-time fine-tuning approaches on this experiment. We find that execution-guided neural program synthesis outperforms all reference algorithms in its ability to compose novel solutions. Our empirical findings also suggest that the success of TTFT on ARC-AGI lies mainly in eliciting in-distribution knowledge that the LLM otherwise fails to rely on directly.

## 📝 요약

이 연구는 ARC-AGI 도메인에서의 조합적 일반화 실험을 통해 신경망 프로그램 합성과 테스트 시점 미세 조정(TTFT) 접근법을 비교합니다. 실험 결과, 실행 유도 신경망 프로그램 합성이 새로운 해결책을 구성하는 데 있어 다른 알고리즘보다 우수함을 발견했습니다. 또한, TTFT의 성공은 주로 대형 언어 모델(LLM)이 직접 활용하지 않는 분포 내 지식을 이끌어내는 데 있다는 것을 시사합니다.

## 🎯 주요 포인트

- 1. ARC-AGI 도메인에서의 실험은 분포 외 일반화 능력이 성공의 필수 요소임을 보여준다.
- 2. 실행 유도 신경 프로그램 합성이 새로운 솔루션을 구성하는 데 있어 모든 참조 알고리즘을 능가한다.
- 3. TTFT의 성공은 주로 LLM이 직접적으로 의존하지 않는 분포 내 지식을 이끌어내는 데 있다.


---

*Generated on 2025-09-24 00:29:49*