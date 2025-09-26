<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:39:10.260232",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "LLM Fingerprinting",
    "LeaFBench",
    "Retrieval Augmented Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "LLM Fingerprinting": 0.78,
    "LeaFBench": 0.8,
    "Retrieval Augmented Generation": 0.77
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
        "rationale": "As a foundational concept in the paper, it connects to discussions on model training and intellectual property.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "LLM fingerprinting",
        "canonical": "LLM Fingerprinting",
        "aliases": [
          "fingerprinting",
          "model fingerprinting"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique central to the paper's theme of copyright auditing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "LeaFBench",
        "canonical": "LeaFBench",
        "aliases": [
          "LeaF Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "A newly introduced benchmark that is crucial for evaluating LLM fingerprinting methods.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Retrieval Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "A trending technique relevant to the parameter-independent mechanisms discussed in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "copyright infringement",
      "model theft",
      "system prompts"
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
      "candidate_surface": "LLM fingerprinting",
      "resolved_canonical": "LLM Fingerprinting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LeaFBench",
      "resolved_canonical": "LeaFBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Retrieval Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SoK: Large Language Model Copyright Auditing via Fingerprinting

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.19843.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2508.19843](https://arxiv.org/abs/2508.19843)

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.4% similar)
- [[2025-09-18/LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking: An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (85.3% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (85.1% similar)
- [[2025-09-23/Intrinsic Meets Extrinsic Fairness_ Assessing the Downstream Impact of Bias Mitigation in Large Language Models_20250923|Intrinsic Meets Extrinsic Fairness: Assessing the Downstream Impact of Bias Mitigation in Large Language Models]] (85.0% similar)
- [[2025-09-24/From Parameters to Performance_ A Data-Driven Study on LLM Structure and Development_20250924|From Parameters to Performance: A Data-Driven Study on LLM Structure and Development]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/LLM Fingerprinting|LLM Fingerprinting]], [[keywords/LeaFBench|LeaFBench]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.19843v2 Announce Type: replace-cross 
Abstract: The broad capabilities and substantial resources required to train Large Language Models (LLMs) make them valuable intellectual property, yet they remain vulnerable to copyright infringement, such as unauthorized use and model theft. LLM fingerprinting, a non-intrusive technique that extracts and compares the distinctive features from LLMs to identify infringements, offers a promising solution to copyright auditing. However, its reliability remains uncertain due to the prevalence of diverse model modifications and the lack of standardized evaluation. In this SoK, we present the first comprehensive study of LLM fingerprinting. We introduce a unified framework and formal taxonomy that categorizes existing methods into white-box and black-box approaches, providing a structured overview of the state of the art. We further propose LeaFBench, the first systematic benchmark for evaluating LLM fingerprinting under realistic deployment scenarios. Built upon mainstream foundation models and comprising 149 distinct model instances, LeaFBench integrates 13 representative post-development techniques, spanning both parameter-altering methods (e.g., fine-tuning, quantization) and parameter-independent mechanisms (e.g., system prompts, RAG). Extensive experiments on LeaFBench reveal the strengths and weaknesses of existing methods, thereby outlining future research directions and critical open problems in this emerging field. The code is available at https://github.com/shaoshuo-ss/LeaFBench.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 저작권 침해 문제를 해결하기 위한 LLM 핑거프린팅 기법을 종합적으로 연구한 최초의 사례를 제시합니다. 저자들은 기존 방법을 백박스와 블랙박스 접근법으로 분류하는 통일된 프레임워크와 분류 체계를 소개하고, 현실적인 배포 시나리오에서 LLM 핑거프린팅을 평가하기 위한 최초의 체계적인 벤치마크인 LeaFBench를 제안합니다. LeaFBench는 149개의 모델 인스턴스를 포함하며, 파라미터 변경 및 비변경 기법을 아우르는 13개의 대표적인 후처리 기술을 통합합니다. 실험 결과는 기존 방법의 장단점을 드러내며, 향후 연구 방향과 해결해야 할 문제를 제시합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 저작권 침해 문제를 해결하기 위한 비침습적 기법인 LLM 핑거프린팅의 중요성을 강조합니다.
- 2. LLM 핑거프린팅의 신뢰성 문제를 해결하기 위해 최초로 포괄적인 연구를 수행하고, 이를 위한 통합 프레임워크와 분류 체계를 제시합니다.
- 3. 현실적인 배포 시나리오에서 LLM 핑거프린팅을 평가하기 위한 최초의 체계적인 벤치마크인 LeaFBench를 제안합니다.
- 4. LeaFBench는 149개의 모델 인스턴스를 포함하고, 매개변수 변경 및 비매개변수 메커니즘을 아우르는 13개의 대표적인 후처리 기법을 통합합니다.
- 5. LeaFBench를 통한 광범위한 실험을 통해 기존 방법의 장단점을 밝혀내고, 이 분야의 미래 연구 방향과 중요한 미해결 문제를 제시합니다.


---

*Generated on 2025-09-24 14:39:10*