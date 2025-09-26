<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:26:41.159137",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-Omics",
    "Biology-Instructions",
    "ChatMultiOmics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multi-Omics": 0.8,
    "Biology-Instructions": 0.78,
    "ChatMultiOmics": 0.77
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
        "rationale": "Large Language Models are central to the study and connect well with existing research in AI and machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Omics",
        "canonical": "Multi-Omics",
        "aliases": [
          "multi-omics biology"
        ],
        "category": "unique_technical",
        "rationale": "Multi-Omics is a specialized field that bridges various biological data types, crucial for linking biological and computational studies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Biology-Instructions",
        "canonical": "Biology-Instructions",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Biology-Instructions is a novel dataset that provides a foundation for linking LLMs with biological sequence tasks.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "ChatMultiOmics",
        "canonical": "ChatMultiOmics",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ChatMultiOmics represents a new approach in training LLMs for biological understanding, enhancing connectivity with bioinformatics.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "instruction-tuning",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-Omics",
      "resolved_canonical": "Multi-Omics",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Biology-Instructions",
      "resolved_canonical": "Biology-Instructions",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ChatMultiOmics",
      "resolved_canonical": "ChatMultiOmics",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Biology-Instructions: A Dataset and Benchmark for Multi-Omics Sequence Understanding Capability of Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2412.19191.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2412.19191](https://arxiv.org/abs/2412.19191)

## 🔗 유사한 논문
- [[2025-09-18/xGen-MM (BLIP-3)_ A Family of Open Large Multimodal Models_20250918|xGen-MM (BLIP-3): A Family of Open Large Multimodal Models]] (82.1% similar)
- [[2025-09-23/MSCoRe_ A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents_20250923|MSCoRe: A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents]] (82.1% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (81.7% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (81.5% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Multi-Omics|Multi-Omics]], [[keywords/Biology-Instructions|Biology-Instructions]], [[keywords/ChatMultiOmics|ChatMultiOmics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.19191v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) have shown remarkable capabilities in general domains, but their application to multi-omics biology remains underexplored. To address this gap, we introduce Biology-Instructions, the first large-scale instruction-tuning dataset for multi-omics biological sequences, including DNA, RNA, proteins, and multi-molecules. This dataset bridges LLMs and complex biological sequence-related tasks, enhancing their versatility and reasoning while maintaining conversational fluency. We also highlight significant limitations of current state-of-the-art LLMs on multi-omics tasks without specialized training. To overcome this, we propose ChatMultiOmics, a strong baseline with a novel three-stage training pipeline, demonstrating superior biological understanding through Biology-Instructions. Both resources are publicly available, paving the way for better integration of LLMs in multi-omics analysis. The Biology-Instructions is publicly available at: https://github.com/hhnqqq/Biology-Instructions.

## 📝 요약

이 논문은 대형 언어 모델(LLMs)의 다중 오믹스 생물학 분야 적용을 탐구합니다. 이를 위해 DNA, RNA, 단백질 및 다중 분자를 포함한 생물학적 서열을 위한 최초의 대규모 지침 조정 데이터셋인 Biology-Instructions를 소개합니다. 이 데이터셋은 LLMs가 복잡한 생물학적 서열 관련 작업을 수행할 수 있도록 지원하며, 대화 유창성을 유지하면서 다재다능성과 추론 능력을 향상시킵니다. 또한, 현재 최첨단 LLMs가 다중 오믹스 작업에서 전문적인 훈련 없이 직면하는 한계를 강조합니다. 이를 극복하기 위해, Biology-Instructions를 활용한 새로운 3단계 훈련 파이프라인을 제안하여 ChatMultiOmics라는 강력한 기준 모델을 개발하였습니다. 이 모델은 생물학적 이해에 있어 우수한 성능을 보이며, 두 자원 모두 공개되어 LLMs의 다중 오믹스 분석 통합을 촉진합니다.

## 🎯 주요 포인트

- 1. Biology-Instructions는 다중 오믹스 생물학적 서열을 위한 최초의 대규모 지시 조정 데이터셋으로, LLM의 적용 범위를 확장합니다.
- 2. 현재 최첨단 LLM은 다중 오믹스 작업에서 전문적인 훈련 없이 상당한 한계를 보입니다.
- 3. ChatMultiOmics는 새로운 3단계 훈련 파이프라인을 통해 생물학적 이해도를 향상시킨 강력한 기준 모델입니다.
- 4. Biology-Instructions와 ChatMultiOmics는 모두 공개되어 있어 LLM의 다중 오믹스 분석 통합을 촉진합니다.


---

*Generated on 2025-09-24 14:26:41*