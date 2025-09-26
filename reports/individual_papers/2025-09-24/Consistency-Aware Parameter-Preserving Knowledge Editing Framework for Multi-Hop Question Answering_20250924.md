<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:41:12.570771",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Parameter-Preserving Knowledge Editing",
    "Knowledge Graph",
    "Multi-Hop Question Answering",
    "Consistency-Aware Parameter-Preserving Editing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Parameter-Preserving Knowledge Editing": 0.78,
    "Knowledge Graph": 0.82,
    "Multi-Hop Question Answering": 0.79,
    "Consistency-Aware Parameter-Preserving Editing": 0.81
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Parameter-Preserving Knowledge Editing",
        "canonical": "Parameter-Preserving Knowledge Editing",
        "aliases": [
          "PPKE"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach to updating models without retraining.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Knowledge Graphs",
        "canonical": "Knowledge Graph",
        "aliases": [
          "KG"
        ],
        "category": "specific_connectable",
        "rationale": "Knowledge Graphs are crucial for the framework described, enabling structured knowledge representation and retrieval.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-Hop Question Answering",
        "canonical": "Multi-Hop Question Answering",
        "aliases": [
          "MHQA"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on improving consistency in multi-hop reasoning tasks, making this a key concept.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.83,
        "link_intent_score": 0.79
      },
      {
        "surface": "Consistency-Aware Parameter-Preserving Editing",
        "canonical": "Consistency-Aware Parameter-Preserving Editing",
        "aliases": [
          "CAPE-KG"
        ],
        "category": "unique_technical",
        "rationale": "This is the proposed framework in the paper, emphasizing the novel aspect of consistency in knowledge editing.",
        "novelty_score": 0.8,
        "connectivity_score": 0.68,
        "specificity_score": 0.87,
        "link_intent_score": 0.81
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Parameter-Preserving Knowledge Editing",
      "resolved_canonical": "Parameter-Preserving Knowledge Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Knowledge Graphs",
      "resolved_canonical": "Knowledge Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-Hop Question Answering",
      "resolved_canonical": "Multi-Hop Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.83,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Consistency-Aware Parameter-Preserving Editing",
      "resolved_canonical": "Consistency-Aware Parameter-Preserving Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.68,
        "specificity": 0.87,
        "link_intent": 0.81
      }
    }
  ]
}
-->

# Consistency-Aware Parameter-Preserving Knowledge Editing Framework for Multi-Hop Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18655.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18655](https://arxiv.org/abs/2509.18655)

## 🔗 유사한 논문
- [[2025-09-24/CaKE_ Circuit-aware Editing Enables Generalizable Knowledge Learners_20250924|CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners]] (86.6% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (82.3% similar)
- [[2025-09-24/Pathways of Thoughts_ Multi-Directional Thinking for Long-form Personalized Question Answering_20250924|Pathways of Thoughts: Multi-Directional Thinking for Long-form Personalized Question Answering]] (81.0% similar)
- [[2025-09-23/EpiCache_ Episodic KV Cache Management for Long Conversational Question Answering_20250923|EpiCache: Episodic KV Cache Management for Long Conversational Question Answering]] (80.2% similar)
- [[2025-09-23/Large Language Models Meet Knowledge Graphs for Question Answering_ Synthesis and Opportunities_20250923|Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Knowledge Graph|Knowledge Graph]]
**⚡ Unique Technical**: [[keywords/Parameter-Preserving Knowledge Editing|Parameter-Preserving Knowledge Editing]], [[keywords/Multi-Hop Question Answering|Multi-Hop Question Answering]], [[keywords/Consistency-Aware Parameter-Preserving Editing|Consistency-Aware Parameter-Preserving Editing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18655v1 Announce Type: new 
Abstract: Parameter-Preserving Knowledge Editing (PPKE) enables updating models with new or corrected information without retraining or parameter adjustment. Recent PPKE approaches based on knowledge graphs (KG) to extend knowledge editing (KE) capabilities to multi-hop question answering (MHQA). However, these methods often lack consistency, leading to knowledge contamination, unstable updates, and retrieval behaviors that fail to reflect the intended edits. Such inconsistencies undermine the reliability of PPKE in multi- hop reasoning. We present CAPE-KG, Consistency-Aware Parameter-Preserving Editing with Knowledge Graphs, a novel consistency-aware framework for PPKE on MHQA. CAPE-KG ensures KG construction, update, and retrieval are always aligned with the requirements of the MHQA task, maintaining coherent reasoning over both unedited and edited knowledge. Extensive experiments on the MQuAKE benchmark show accuracy improvements in PPKE performance for MHQA, demonstrating the effectiveness of addressing consistency in PPKE.

## 📝 요약

CAPE-KG는 다중 단계 질문 응답(MHQA)에서 일관성을 유지하는 파라미터 보존 지식 편집(PPKE) 프레임워크를 제안합니다. 기존의 PPKE 방법은 일관성 부족으로 인해 지식 오염과 불안정한 업데이트를 초래하였으나, CAPE-KG는 지식 그래프(KG)를 활용하여 이러한 문제를 해결합니다. CAPE-KG는 KG의 구성, 업데이트, 검색이 MHQA의 요구사항에 맞게 일관되게 이루어지도록 하여, 편집된 지식과 편집되지 않은 지식 모두에 대해 일관된 추론을 유지합니다. MQuAKE 벤치마크 실험에서 CAPE-KG는 PPKE 성능을 향상시켜, 일관성 문제 해결의 효과성을 입증했습니다.

## 🎯 주요 포인트

- 1. PPKE는 재훈련이나 파라미터 조정 없이 모델을 새로운 정보로 업데이트할 수 있게 한다.
- 2. 기존의 PPKE 방법은 일관성이 부족하여 지식 오염 및 불안정한 업데이트 문제를 야기할 수 있다.
- 3. CAPE-KG는 일관성을 고려한 새로운 PPKE 프레임워크로, MHQA 작업의 요구사항에 맞춰 KG의 구축, 업데이트, 검색을 보장한다.
- 4. CAPE-KG는 수정된 지식과 수정되지 않은 지식 모두에 대해 일관된 추론을 유지한다.
- 5. MQuAKE 벤치마크 실험에서 CAPE-KG는 MHQA에 대한 PPKE 성능의 정확도를 향상시켰다.


---

*Generated on 2025-09-24 15:41:12*