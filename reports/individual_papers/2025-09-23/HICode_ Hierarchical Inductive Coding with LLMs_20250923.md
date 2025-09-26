---
keywords:
  - Large Language Model
  - Hierarchical Clustering
  - Inductive Coding
  - Opioid Crisis
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17946
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:13:58.651070",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Hierarchical Clustering",
    "Inductive Coding",
    "Opioid Crisis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Hierarchical Clustering": 0.78,
    "Inductive Coding": 0.74,
    "Opioid Crisis": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLMs",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's proposed method and connect to broader research in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hierarchical Clustering",
        "canonical": "Hierarchical Clustering",
        "aliases": [
          "Hierarchical Cluster Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Hierarchical Clustering is a key component of HICode, relevant for linking to methods in data analysis.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Inductive Coding",
        "canonical": "Inductive Coding",
        "aliases": [
          "Inductive Code Generation"
        ],
        "category": "unique_technical",
        "rationale": "Inductive Coding is a novel approach in the paper, crucial for understanding the methodology.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.87,
        "link_intent_score": 0.74
      },
      {
        "surface": "Opioid Crisis",
        "canonical": "Opioid Crisis",
        "aliases": [
          "Opioid Epidemic"
        ],
        "category": "evolved_concepts",
        "rationale": "The Opioid Crisis is a significant case study in the paper, linking to socio-economic and health research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "manual labeling",
      "topic modeling",
      "litigation documents"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLMs",
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
      "candidate_surface": "Hierarchical Clustering",
      "resolved_canonical": "Hierarchical Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Inductive Coding",
      "resolved_canonical": "Inductive Coding",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.87,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Opioid Crisis",
      "resolved_canonical": "Opioid Crisis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# HICode: Hierarchical Inductive Coding with LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17946.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17946](https://arxiv.org/abs/2509.17946)

## 🔗 유사한 논문
- [[2025-09-23/Pico_ A Modular Framework for Hypothesis-Driven Small Language Model Research_20250923|Pico: A Modular Framework for Hypothesis-Driven Small Language Model Research]] (78.9% similar)
- [[2025-09-22/MedCOD_ Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework_20250922|MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework]] (78.8% similar)
- [[2025-09-22/AmpleHate_ Amplifying the Attention for Versatile Implicit Hate Detection_20250922|AmpleHate: Amplifying the Attention for Versatile Implicit Hate Detection]] (78.6% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI: Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (78.3% similar)
- [[2025-09-22/Efficient Extractive Text Summarization for Online News Articles Using Machine Learning_20250922|Efficient Extractive Text Summarization for Online News Articles Using Machine Learning]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Hierarchical Clustering|Hierarchical Clustering]]
**⚡ Unique Technical**: [[keywords/Inductive Coding|Inductive Coding]]
**🚀 Evolved Concepts**: [[keywords/Opioid Crisis|Opioid Crisis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17946v1 Announce Type: cross 
Abstract: Despite numerous applications for fine-grained corpus analysis, researchers continue to rely on manual labeling, which does not scale, or statistical tools like topic modeling, which are difficult to control. We propose that LLMs have the potential to scale the nuanced analyses that researchers typically conduct manually to large text corpora. To this effect, inspired by qualitative research methods, we develop HICode, a two-part pipeline that first inductively generates labels directly from analysis data and then hierarchically clusters them to surface emergent themes. We validate this approach across three diverse datasets by measuring alignment with human-constructed themes and demonstrating its robustness through automated and human evaluations. Finally, we conduct a case study of litigation documents related to the ongoing opioid crisis in the U.S., revealing aggressive marketing strategies employed by pharmaceutical companies and demonstrating HICode's potential for facilitating nuanced analyses in large-scale data.

## 📝 요약

이 논문은 세밀한 코퍼스 분석을 위한 새로운 방법론인 HICode를 제안합니다. 기존의 수작업 라벨링이나 주제 모델링의 한계를 극복하기 위해, HICode는 대규모 텍스트 코퍼스에서 연구자들이 수작업으로 수행하던 세밀한 분석을 확장할 수 있는 가능성을 제시합니다. 이 방법론은 먼저 데이터에서 라벨을 유도적으로 생성하고, 이를 계층적으로 클러스터링하여 새로운 주제를 도출합니다. 세 가지 다양한 데이터셋에서 인간이 구성한 주제와의 일치도를 측정하고, 자동 및 인간 평가를 통해 방법의 견고성을 입증했습니다. 또한, 미국의 오피오이드 위기와 관련된 소송 문서 사례 연구를 통해 제약회사의 공격적인 마케팅 전략을 밝혀내고, HICode가 대규모 데이터의 세밀한 분석을 촉진할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 연구자들이 수작업으로 수행하던 세밀한 분석을 대규모 텍스트 코퍼스로 확장할 수 있는 잠재력을 LLMs가 가지고 있음을 제안합니다.
- 2. HICode는 분석 데이터에서 직접 레이블을 생성하고 이를 계층적으로 클러스터링하여 새로운 주제를 도출하는 두 부분으로 구성된 파이프라인입니다.
- 3. 세 가지 다양한 데이터셋에서 HICode의 유효성을 검증하였으며, 인간이 구성한 주제와의 정렬을 측정하고 자동 및 인간 평가를 통해 견고성을 입증했습니다.
- 4. 미국의 지속적인 오피오이드 위기와 관련된 소송 문서에 대한 사례 연구를 통해 제약 회사의 공격적인 마케팅 전략을 밝혀냈습니다.
- 5. HICode는 대규모 데이터에서 세밀한 분석을 용이하게 할 수 있는 잠재력을 보여줍니다.


---

*Generated on 2025-09-24 00:13:58*