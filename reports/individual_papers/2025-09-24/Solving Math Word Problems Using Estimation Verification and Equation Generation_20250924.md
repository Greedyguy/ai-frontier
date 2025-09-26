<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:26:38.187333",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Math Word Problems",
    "Equation Generation",
    "Estimation Verification",
    "Symbolic Equation Solver"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Math Word Problems": 0.78,
    "Equation Generation": 0.8,
    "Estimation Verification": 0.82,
    "Symbolic Equation Solver": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's methodology and connects to a wide range of research in AI and NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Math Word Problems",
        "canonical": "Math Word Problems",
        "aliases": [
          "MWPs"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific problem domain addressed by the paper, providing a unique context for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Equation Generation",
        "canonical": "Equation Generation",
        "aliases": [
          "Equation Creation"
        ],
        "category": "specific_connectable",
        "rationale": "This process is a key step in the proposed method, linking to mathematical reasoning and problem-solving.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      },
      {
        "surface": "Estimation Verification",
        "canonical": "Estimation Verification",
        "aliases": [
          "Verification by Estimation"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach is central to the paper's contribution and offers a unique linking opportunity.",
        "novelty_score": 0.82,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Symbolic Equation Solver",
        "canonical": "Symbolic Equation Solver",
        "aliases": [
          "Symbolic Solver"
        ],
        "category": "specific_connectable",
        "rationale": "This tool is integral to the method described, connecting to computational mathematics.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Math Word Problems",
      "resolved_canonical": "Math Word Problems",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Equation Generation",
      "resolved_canonical": "Equation Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Estimation Verification",
      "resolved_canonical": "Estimation Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Symbolic Equation Solver",
      "resolved_canonical": "Symbolic Equation Solver",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Solving Math Word Problems Using Estimation Verification and Equation Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18565.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18565](https://arxiv.org/abs/2509.18565)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (87.4% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (86.9% similar)
- [[2025-09-23/Step Guided Reasoning_ Improving Mathematical Reasoning using Guidance Generation and Step Reasoning_20250923|Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning]] (86.6% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (86.3% similar)
- [[2025-09-23/Investigating Bias_ A Multilingual Pipeline for Generating, Solving, and Evaluating Math Problems with LLMs_20250923|Investigating Bias: A Multilingual Pipeline for Generating, Solving, and Evaluating Math Problems with LLMs]] (86.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Equation Generation|Equation Generation]], [[keywords/Symbolic Equation Solver|Symbolic Equation Solver]]
**⚡ Unique Technical**: [[keywords/Math Word Problems|Math Word Problems]], [[keywords/Estimation Verification|Estimation Verification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18565v1 Announce Type: new 
Abstract: Large Language Models (LLMs) excel at various tasks, including problem-solving and question-answering. However, LLMs often find Math Word Problems (MWPs) challenging because solving them requires a range of reasoning and mathematical abilities with which LLMs seem to struggle. Recent efforts have helped LLMs solve more complex MWPs with improved prompts. This study proposes a novel method that initially prompts an LLM to create equations from a decomposition of the question, followed by using an external symbolic equation solver to produce an answer. To ensure the accuracy of the obtained answer, inspired by an established recommendation of math teachers, the LLM is instructed to solve the MWP a second time, but this time with the objective of estimating the correct answer instead of solving it exactly. The estimation is then compared to the generated answer to verify. If verification fails, an iterative rectification process is employed to ensure the correct answer is eventually found. This approach achieves new state-of-the-art results on datasets used by prior published research on numeric and algebraic MWPs, improving the previous best results by nearly two percent on average. In addition, the approach obtains satisfactory results on trigonometric MWPs, a task not previously attempted to the authors' best knowledge. This study also introduces two new datasets, SVAMPClean and Trig300, to further advance the testing of LLMs' reasoning abilities.

## 📝 요약

이 연구는 대형 언어 모델(LLM)이 수학적 문제 해결에 어려움을 겪는 문제를 해결하기 위해 새로운 방법을 제안합니다. 제안된 방법은 문제를 분해하여 방정식을 생성하고, 외부 기호 방정식 해결기를 사용해 답을 도출합니다. 이후, LLM이 추정치를 통해 답을 검증하고, 필요시 반복적인 수정 과정을 거쳐 정확한 답을 찾습니다. 이 접근법은 기존 연구 대비 평균 2% 향상된 성과를 보였으며, 삼각 함수 문제에서도 만족스러운 결과를 얻었습니다. 또한, 연구는 새로운 데이터셋 SVAMPClean과 Trig300을 소개하여 LLM의 추론 능력을 더욱 발전시키고자 합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 다양한 작업에서 뛰어나지만 수학적 사고와 추론이 필요한 수학 단어 문제(MWPs) 해결에는 어려움을 겪는다.
- 2. 본 연구는 질문을 분해하여 방정식을 생성하고 외부 기호 방정식 해결기를 사용하여 답을 도출하는 새로운 방법을 제안한다.
- 3. 정확성을 보장하기 위해 LLM이 추정치를 통해 답을 검증하는 과정을 포함하며, 실패 시 반복적인 수정 과정을 통해 정확한 답을 찾는다.
- 4. 이 접근법은 기존 연구보다 평균 2% 개선된 결과를 달성하며, 삼각함수 MWPs에서도 만족스러운 성과를 보인다.
- 5. 연구는 LLM의 추론 능력 테스트를 위해 새로운 데이터셋인 SVAMPClean과 Trig300을 도입한다.


---

*Generated on 2025-09-24 13:26:38*