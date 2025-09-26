---
keywords:
  - AuditoryBench++
  - Auditory Imagination Reasoning
  - Multimodal Learning
  - Auditory Commonsense
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17641
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:04:12.696292",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "AuditoryBench++",
    "Auditory Imagination Reasoning",
    "Multimodal Learning",
    "Auditory Commonsense"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "AuditoryBench++": 0.78,
    "Auditory Imagination Reasoning": 0.77,
    "Multimodal Learning": 0.79,
    "Auditory Commonsense": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AuditoryBench++",
        "canonical": "AuditoryBench++",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "AuditoryBench++ is a unique benchmark specifically designed for evaluating auditory knowledge in text-only settings, making it a novel concept in the field.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "auditory imagination reasoning",
        "canonical": "Auditory Imagination Reasoning",
        "aliases": [
          "AIR-CoT"
        ],
        "category": "unique_technical",
        "rationale": "This method introduces a novel approach to integrate auditory information during inference, which is crucial for linking auditory concepts in language models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Multimodal LLMs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Large Language Models"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal LLMs are increasingly relevant for integrating auditory and textual data, providing strong connectivity with existing multimodal research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "auditory commonsense",
        "canonical": "Auditory Commonsense",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Auditory commonsense is a specific concept that highlights the intuitive understanding of auditory properties, which is underexplored in language models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "auditory properties",
      "auditory knowledge",
      "benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AuditoryBench++",
      "resolved_canonical": "AuditoryBench++",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "auditory imagination reasoning",
      "resolved_canonical": "Auditory Imagination Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Multimodal LLMs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "auditory commonsense",
      "resolved_canonical": "Auditory Commonsense",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# AuditoryBench++: Can Language Models Understand Auditory Knowledge without Hearing?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17641.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17641](https://arxiv.org/abs/2509.17641)

## 🔗 유사한 논문
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (86.4% similar)
- [[2025-09-22/SightSound-R1_ Cross-Modal Reasoning Distillation from Vision to Audio Language Models_20250922|SightSound-R1: Cross-Modal Reasoning Distillation from Vision to Audio Language Models]] (84.5% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (84.3% similar)
- [[2025-09-22/Benchmark of stylistic variation in LLM-generated texts_20250922|Benchmark of stylistic variation in LLM-generated texts]] (84.1% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/AuditoryBench++|AuditoryBench++]], [[keywords/Auditory Imagination Reasoning|Auditory Imagination Reasoning]], [[keywords/Auditory Commonsense|Auditory Commonsense]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17641v1 Announce Type: cross 
Abstract: Even without directly hearing sounds, humans can effortlessly reason about auditory properties, such as pitch, loudness, or sound-source associations, drawing on auditory commonsense. In contrast, language models often lack this capability, limiting their effectiveness in multimodal interactions. As an initial step to address this gap, we present AuditoryBench++, a comprehensive benchmark for evaluating auditory knowledge and reasoning in text-only settings. The benchmark encompasses tasks that range from basic auditory comparisons to contextually grounded reasoning, enabling fine-grained analysis of how models process and integrate auditory concepts. In addition, we introduce AIR-CoT, a novel auditory imagination reasoning method that generates and integrates auditory information during inference through span detection with special tokens and knowledge injection. Extensive experiments with recent LLMs and Multimodal LLMs demonstrate that AIR-CoT generally outperforms both the off-the-shelf models and those augmented with auditory knowledge. The project page is available at https://auditorybenchpp.github.io.

## 📝 요약

이 논문은 인간이 소리 없이도 청각적 특성을 추론할 수 있는 능력을 언어 모델이 갖추지 못한 문제를 해결하기 위해 AuditoryBench++라는 벤치마크를 제안합니다. 이 벤치마크는 텍스트 기반 환경에서 청각 지식과 추론 능력을 평가하며, 기본적인 청각 비교부터 맥락에 기반한 추론까지 다양한 과제를 포함합니다. 또한, AIR-CoT라는 새로운 청각 상상 추론 방법을 도입하여 특수 토큰과 지식 주입을 통해 추론 시 청각 정보를 생성하고 통합합니다. 실험 결과, AIR-CoT는 기존 모델과 청각 지식이 보강된 모델보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 인간은 직접 소리를 듣지 않고도 청각적 상식을 통해 음높이, 음량, 소리의 출처 등을 추론할 수 있지만, 언어 모델은 이러한 능력이 부족하다.
- 2. AuditoryBench++는 텍스트 기반 환경에서 청각적 지식과 추론을 평가하기 위한 포괄적인 벤치마크로, 기본적인 청각 비교부터 맥락적 추론까지 다양한 과제를 포함한다.
- 3. AIR-CoT는 추론 중에 특별한 토큰과 지식 주입을 통해 청각 정보를 생성하고 통합하는 새로운 청각 상상 추론 방법이다.
- 4. 최신 대규모 언어 모델(LLM) 및 다중 모달 LLM을 사용한 실험 결과, AIR-CoT가 기본 모델과 청각 지식이 추가된 모델보다 일반적으로 더 우수한 성능을 보였다.


---

*Generated on 2025-09-24 00:04:12*