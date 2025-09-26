---
keywords:
  - Large Language Model
  - Combinatorial Optimization
  - Reinforcement Learning
  - Supervised Fine-Tuning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16865
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:53:01.030976",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Combinatorial Optimization",
    "Reinforcement Learning",
    "Supervised Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Combinatorial Optimization": 0.8,
    "Reinforcement Learning": 0.78,
    "Supervised Fine-Tuning": 0.75
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
        "rationale": "Central to the paper's approach, linking to existing knowledge on LLMs.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Combinatorial Optimization",
        "canonical": "Combinatorial Optimization",
        "aliases": [
          "CO"
        ],
        "category": "unique_technical",
        "rationale": "The paper's focus is on solving combinatorial optimization problems, a distinct technical area.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "specific_connectable",
        "rationale": "Used in the paper's methodology, connecting to reinforcement learning techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Supervised Fine-Tuning",
        "canonical": "Supervised Fine-Tuning",
        "aliases": [
          "SFT"
        ],
        "category": "unique_technical",
        "rationale": "A specific training strategy discussed in the paper, relevant for linking training methodologies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "evaluation",
      "solution"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Combinatorial Optimization",
      "resolved_canonical": "Combinatorial Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Supervised Fine-Tuning",
      "resolved_canonical": "Supervised Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Large Language Models as End-to-end Combinatorial Optimization Solvers

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16865.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16865](https://arxiv.org/abs/2509.16865)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (87.5% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (85.8% similar)
- [[2025-09-22/Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges_20250922|Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges]] (85.4% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (85.1% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI: Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Combinatorial Optimization|Combinatorial Optimization]], [[keywords/Supervised Fine-Tuning|Supervised Fine-Tuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16865v1 Announce Type: new 
Abstract: Combinatorial optimization (CO) problems, central to decision-making scenarios like logistics and manufacturing, are traditionally solved using problem-specific algorithms requiring significant domain expertise. While large language models (LLMs) have shown promise in automating CO problem solving, existing approaches rely on intermediate steps such as code generation or solver invocation, limiting their generality and accessibility. This paper introduces a novel framework that empowers LLMs to serve as end-to-end CO solvers by directly mapping natural language problem descriptions to solutions. We propose a two-stage training strategy: supervised fine-tuning (SFT) imparts LLMs with solution generation patterns from domain-specific solvers, while a feasibility-and-optimality-aware reinforcement learning (FOARL) process explicitly mitigates constraint violations and refines solution quality. Evaluation across seven NP-hard CO problems shows that our method achieves a high feasibility rate and reduces the average optimality gap to 1.03-8.20% by tuning a 7B-parameter LLM, surpassing both general-purpose LLMs (e.g., GPT-4o), reasoning models (e.g., DeepSeek-R1), and domain-specific heuristics. Our method establishes a unified language-based pipeline for CO without extensive code execution or manual architectural adjustments for different problems, offering a general and language-driven alternative to traditional solver design while maintaining relative feasibility guarantees.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)을 활용하여 조합 최적화(CO) 문제를 자동으로 해결하는 새로운 프레임워크를 제안합니다. 기존 방법들은 코드 생성이나 솔버 호출 등의 중간 단계를 필요로 했지만, 이 연구는 자연어 문제 설명을 직접 솔루션으로 변환하는 방식을 도입했습니다. 두 단계의 훈련 전략을 사용하여, 첫째로 지도 학습(SFT)을 통해 LLM이 도메인별 솔버의 솔루션 생성 패턴을 학습하고, 둘째로 제약 조건 위반을 줄이고 솔루션 품질을 향상시키는 강화 학습(FOARL)을 적용했습니다. 7개의 NP-hard CO 문제에 대한 평가 결과, 제안된 방법은 높은 실행 가능성을 보이며 최적성 격차를 1.03-8.20%로 줄였습니다. 이는 기존의 일반 목적 LLM이나 도메인 특화 휴리스틱을 능가하는 성과로, 다양한 문제에 대한 통합된 언어 기반 파이프라인을 제공합니다.

## 🎯 주요 포인트

- 1. 본 논문은 자연어 문제 설명을 직접 솔루션으로 매핑하여 LLM을 종단 간 조합 최적화 문제 해결사로 활용하는 새로운 프레임워크를 소개합니다.
- 2. 제안된 두 단계의 훈련 전략은 감독된 미세 조정(SFT)과 제약 위반을 완화하고 솔루션 품질을 개선하는 타당성 및 최적성 인식 강화 학습(FOARL) 과정을 포함합니다.
- 3. 7개의 NP-난이도 조합 최적화 문제에 대한 평가에서 제안된 방법은 높은 타당성 비율을 달성하고 평균 최적성 격차를 1.03-8.20%로 줄였습니다.
- 4. 본 방법은 일반 목적 LLM, 추론 모델 및 도메인 특화 휴리스틱을 능가하며, 다양한 문제에 대해 코드 실행이나 수동적인 구조 조정 없이 통합된 언어 기반 파이프라인을 제공합니다.
- 5. 전통적인 해결사 설계에 대한 일반적이고 언어 중심의 대안을 제시하면서 상대적 타당성 보장을 유지합니다.


---

*Generated on 2025-09-23 22:53:01*