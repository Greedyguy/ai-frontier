---
keywords:
  - Large Language Model
  - Multilingual Coreference Resolution
  - Few-Shot Learning
  - CorefUD Dataset
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17796
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:32:53.151906",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multilingual Coreference Resolution",
    "Few-Shot Learning",
    "CorefUD Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multilingual Coreference Resolution": 0.8,
    "Few-Shot Learning": 0.82,
    "CorefUD Dataset": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's theme, providing a direct link to advancements in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multilingual Coreference Resolution",
        "canonical": "Multilingual Coreference Resolution",
        "aliases": [
          "Coreference Resolution"
        ],
        "category": "unique_technical",
        "rationale": "This task is the focus of the shared task discussed, offering a unique technical challenge in NLP.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Few-Shot Adaptation",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot Adaptation"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is a trending approach that is relevant to the paper's exploration of LLM capabilities.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "CorefUD",
        "canonical": "CorefUD Dataset",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "CorefUD is a specific dataset used in the paper, crucial for understanding the multilingual aspect of the task.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "Shared Task",
      "Traditional Approaches",
      "Participants",
      "Systems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multilingual Coreference Resolution",
      "resolved_canonical": "Multilingual Coreference Resolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Few-Shot Adaptation",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "CorefUD",
      "resolved_canonical": "CorefUD Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Findings of the Fourth Shared Task on Multilingual Coreference Resolution: Can LLMs Dethrone Traditional Approaches?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17796.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17796](https://arxiv.org/abs/2509.17796)

## 🔗 유사한 논문
- [[2025-09-23/CorefInst_ Leveraging LLMs for Multilingual Coreference Resolution_20250923|CorefInst: Leveraging LLMs for Multilingual Coreference Resolution]] (89.3% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.7% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance]] (83.1% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (83.1% similar)
- [[2025-09-22/Harnessing Multiple Large Language Models_ A Survey on LLM Ensemble_20250922|Harnessing Multiple Large Language Models: A Survey on LLM Ensemble]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Multilingual Coreference Resolution|Multilingual Coreference Resolution]], [[keywords/CorefUD Dataset|CorefUD Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17796v1 Announce Type: new 
Abstract: The paper presents an overview of the fourth edition of the Shared Task on Multilingual Coreference Resolution, organized as part of the CODI-CRAC 2025 workshop. As in the previous editions, participants were challenged to develop systems that identify mentions and cluster them according to identity coreference.
  A key innovation of this year's task was the introduction of a dedicated Large Language Model (LLM) track, featuring a simplified plaintext format designed to be more suitable for LLMs than the original CoNLL-U representation.
  The task also expanded its coverage with three new datasets in two additional languages, using version 1.3 of CorefUD - a harmonized multilingual collection of 22 datasets in 17 languages.
  In total, nine systems participated, including four LLM-based approaches (two fine-tuned and two using few-shot adaptation). While traditional systems still kept the lead, LLMs showed clear potential, suggesting they may soon challenge established approaches in future editions.

## 📝 요약

이 논문은 CODI-CRAC 2025 워크숍의 다국어 코어퍼런스 해결 공유 과제의 네 번째 에디션을 개괄합니다. 이번 과제의 주요 기여는 대형 언어 모델(LLM) 트랙의 도입으로, LLM에 적합한 간소화된 형식이 특징입니다. 또한, CorefUD 1.3 버전을 사용하여 17개 언어의 22개 데이터셋을 포함하고, 두 개의 추가 언어로 세 개의 새로운 데이터셋을 확장했습니다. 총 9개의 시스템이 참여했으며, 이 중 4개는 LLM 기반 접근법을 사용했습니다. 전통적인 시스템이 여전히 우위를 점했지만, LLM의 잠재력이 확인되어 향후 에디션에서 기존 접근법에 도전할 가능성을 시사합니다.

## 🎯 주요 포인트

- 1. 이번 과제의 주요 혁신은 대형 언어 모델(LLM) 트랙의 도입으로, LLM에 적합한 단순화된 평문 형식을 특징으로 합니다.
- 2. 과제는 CorefUD 1.3 버전을 사용하여 두 개의 추가 언어로 세 개의 새로운 데이터셋을 확장했습니다.
- 3. 총 9개의 시스템이 참여했으며, 이 중 4개는 LLM 기반 접근 방식으로, 두 개는 미세 조정, 두 개는 소수 샷 적응을 사용했습니다.
- 4. 전통적인 시스템이 여전히 우위를 점하고 있지만, LLM은 명확한 잠재력을 보여주어 향후 판에서 기존 접근 방식을 도전할 가능성을 시사합니다.


---

*Generated on 2025-09-24 03:32:53*