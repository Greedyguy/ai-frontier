---
keywords:
  - Large Language Model
  - Medical Fact-checking
  - In-context Learning
  - Fine-tuning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17436
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:26:20.063150",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Medical Fact-checking",
    "In-context Learning",
    "Fine-tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Medical Fact-checking": 0.78,
    "In-context Learning": 0.74,
    "Fine-tuning": 0.77
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
        "rationale": "This term is central to the paper's focus on evaluating LLM-generated content, providing a strong link to existing discussions on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Medical Fact-checking",
        "canonical": "Medical Fact-checking",
        "aliases": [
          "Medical Verification",
          "Healthcare Fact-checking"
        ],
        "category": "unique_technical",
        "rationale": "This is a key concept introduced by the paper, focusing on the verification of medical information, which is crucial for linking to related datasets and methodologies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "In-context Learning",
        "canonical": "In-context Learning",
        "aliases": [
          "ICL"
        ],
        "category": "specific_connectable",
        "rationale": "This learning approach is significant for understanding how LLMs can be adapted to new tasks, facilitating connections to broader machine learning strategies.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.79,
        "link_intent_score": 0.74
      },
      {
        "surface": "Fine-tuning",
        "canonical": "Fine-tuning",
        "aliases": [
          "Model Fine-tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Fine-tuning is a critical process in adapting models to specific tasks, linking to discussions on model optimization and performance enhancement.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "experiments",
      "error analysis"
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
      "candidate_surface": "Medical Fact-checking",
      "resolved_canonical": "Medical Fact-checking",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "In-context Learning",
      "resolved_canonical": "In-context Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.79,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Fine-tuning",
      "resolved_canonical": "Fine-tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MedFact: A Large-scale Chinese Dataset for Evidence-based Medical Fact-checking of LLM Responses

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17436.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17436](https://arxiv.org/abs/2509.17436)

## 🔗 유사한 논문
- [[2025-09-19/MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1: Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (84.6% similar)
- [[2025-09-23/ReasonMed_ A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning_20250923|ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning]] (83.9% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (83.8% similar)
- [[2025-09-17/Combating Biomedical Misinformation through Multi-modal Claim Detection and Evidence-based Verification_20250917|Combating Biomedical Misinformation through Multi-modal Claim Detection and Evidence-based Verification]] (82.5% similar)
- [[2025-09-17/Combining Evidence and Reasoning for Biomedical Fact-Checking_20250917|Combining Evidence and Reasoning for Biomedical Fact-Checking]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/In-context Learning|In-context Learning]], [[keywords/Fine-tuning|Fine-tuning]]
**⚡ Unique Technical**: [[keywords/Medical Fact-checking|Medical Fact-checking]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17436v1 Announce Type: new 
Abstract: Medical fact-checking has become increasingly critical as more individuals seek medical information online. However, existing datasets predominantly focus on human-generated content, leaving the verification of content generated by large language models (LLMs) relatively unexplored. To address this gap, we introduce MedFact, the first evidence-based Chinese medical fact-checking dataset of LLM-generated medical content. It consists of 1,321 questions and 7,409 claims, mirroring the complexities of real-world medical scenarios. We conduct comprehensive experiments in both in-context learning (ICL) and fine-tuning settings, showcasing the capability and challenges of current LLMs on this task, accompanied by an in-depth error analysis to point out key directions for future research. Our dataset is publicly available at https://github.com/AshleyChenNLP/MedFact.

## 📝 요약

이 논문은 LLM(대형 언어 모델)이 생성한 의료 콘텐츠의 사실 검증을 위한 최초의 증거 기반 중국어 데이터셋인 MedFact를 소개합니다. 이 데이터셋은 1,321개의 질문과 7,409개의 주장을 포함하며, 실제 의료 시나리오의 복잡성을 반영합니다. 연구는 문맥 학습과 미세 조정 환경에서 LLM의 능력과 도전 과제를 실험하고, 심층 오류 분석을 통해 향후 연구 방향을 제시합니다. 데이터셋은 공개되어 있으며, 연구는 LLM 기반 의료 정보 검증의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. MedFact는 LLM이 생성한 의료 콘텐츠의 사실 검증을 위한 최초의 증거 기반 중국어 데이터셋입니다.
- 2. 데이터셋은 1,321개의 질문과 7,409개의 주장으로 구성되어 실제 의료 시나리오의 복잡성을 반영합니다.
- 3. 연구는 in-context learning(ICL)과 파인튜닝 설정에서 LLM의 능력과 도전 과제를 보여줍니다.
- 4. 심층 오류 분석을 통해 향후 연구의 주요 방향을 제시합니다.
- 5. MedFact 데이터셋은 공개적으로 이용 가능하며, GitHub에서 접근할 수 있습니다.


---

*Generated on 2025-09-24 03:26:20*