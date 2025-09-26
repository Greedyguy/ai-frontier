---
keywords:
  - Large Language Model
  - Gender Bias
  - Fairwords
  - Auto-Search and Refinement
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.11559
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:46:34.355629",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Gender Bias",
    "Fairwords",
    "Auto-Search and Refinement"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Gender Bias": 0.9,
    "Fairwords": 0.8,
    "Auto-Search and Refinement": 0.78
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
        "rationale": "A core technology discussed in the paper, crucial for understanding the context of gender bias mitigation.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "gender bias",
        "canonical": "Gender Bias",
        "aliases": [
          "sex bias"
        ],
        "category": "specific_connectable",
        "rationale": "Central issue addressed by the framework, linking to broader discussions on bias in AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Fairwords",
        "canonical": "Fairwords",
        "aliases": [
          "bias mitigation tokens"
        ],
        "category": "unique_technical",
        "rationale": "A novel concept introduced by the paper, essential for understanding the proposed solution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "auto-search and refinement",
        "canonical": "Auto-Search and Refinement",
        "aliases": [
          "adaptive search"
        ],
        "category": "unique_technical",
        "rationale": "Describes the innovative process used in the framework, highlighting its adaptive nature.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "task performance",
      "resource-intensive"
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
      "candidate_surface": "gender bias",
      "resolved_canonical": "Gender Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Fairwords",
      "resolved_canonical": "Fairwords",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "auto-search and refinement",
      "resolved_canonical": "Auto-Search and Refinement",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Auto-Search and Refinement: An Automated Framework for Gender Bias Mitigation in Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.11559.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.11559](https://arxiv.org/abs/2502.11559)

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.5% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (84.8% similar)
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (84.2% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.0% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Gender Bias|Gender Bias]]
**⚡ Unique Technical**: [[keywords/Fairwords|Fairwords]], [[keywords/Auto-Search and Refinement|Auto-Search and Refinement]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.11559v2 Announce Type: replace-cross 
Abstract: Pre-training large language models (LLMs) on vast text corpora enhances natural language processing capabilities but risks encoding social biases, particularly gender bias. While parameter-modification methods like fine-tuning mitigate bias, they are resource-intensive, unsuitable for closed-source models, and lack adaptability to evolving societal norms. Instruction-based approaches offer flexibility but often compromise task performance. To address these limitations, we propose $\textit{FaIRMaker}$, an automated and model-independent framework that employs an $\textbf{auto-search and refinement}$ paradigm to adaptively generate Fairwords, which act as instructions integrated into input queries to reduce gender bias and enhance response quality. Extensive experiments demonstrate that $\textit{FaIRMaker}$ automatically searches for and dynamically refines Fairwords, effectively mitigating gender bias while preserving task integrity and ensuring compatibility with both API-based and open-source LLMs.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 사전 학습이 자연어 처리 능력을 향상시키지만, 성별 편향과 같은 사회적 편향을 내포할 위험이 있음을 지적합니다. 기존의 매개변수 수정 방법은 자원 소모가 크고, 폐쇄형 모델에 적합하지 않으며, 사회적 규범 변화에 적응하기 어렵습니다. 이를 해결하기 위해, 저자들은 자동 검색 및 개선 패러다임을 활용하여 공정한 단어(Fairwords)를 생성하는 $\textit{FaIRMaker}$라는 자동화된 모델 독립적 프레임워크를 제안합니다. 이 프레임워크는 입력 쿼리에 통합된 지시문으로 작용하여 성별 편향을 줄이고 응답 품질을 향상시킵니다. 실험 결과, $\textit{FaIRMaker}$는 성별 편향을 효과적으로 완화하면서도 작업의 완전성을 유지하고, API 기반 및 오픈 소스 LLM과의 호환성을 보장함을 보여줍니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLMs)의 사전 학습은 자연어 처리 능력을 향상시키지만, 성 편견과 같은 사회적 편견을 내포할 위험이 있다.
- 2. 파라미터 수정 방법인 파인 튜닝은 편견을 줄일 수 있지만, 자원 소모가 크고 폐쇄형 모델에 적합하지 않으며 사회적 규범 변화에 대한 적응력이 부족하다.
- 3. $\textit{FaIRMaker}$는 자동 검색 및 정제 패러다임을 사용하여 Fairwords를 생성하고, 이를 입력 쿼리에 통합하여 성 편견을 줄이고 응답 품질을 향상시키는 자동화된 모델 독립적 프레임워크이다.
- 4. $\textit{FaIRMaker}$는 API 기반 및 오픈 소스 LLMs와의 호환성을 유지하면서 성 편견을 효과적으로 완화하고 작업 무결성을 보존한다.
- 5. 광범위한 실험을 통해 $\textit{FaIRMaker}$가 Fairwords를 자동으로 검색하고 동적으로 정제하여 성 편견을 줄이는 데 효과적임을 입증했다.


---

*Generated on 2025-09-24 00:46:34*