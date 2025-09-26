<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:56:30.944755",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Radiology Report Generation",
    "Oracle-educated Reinforcement Learning",
    "Vision-Language Model",
    "FactScore-based Reward",
    "CheXpert Plus Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Radiology Report Generation": 0.8,
    "Oracle-educated Reinforcement Learning": 0.85,
    "Vision-Language Model": 0.82,
    "FactScore-based Reward": 0.78,
    "CheXpert Plus Dataset": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Radiology Report Generation",
        "canonical": "Radiology Report Generation",
        "aliases": [
          "RRG"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and represents a specific application of AI in healthcare.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Oracle-educated Reinforcement Learning",
        "canonical": "Oracle-educated Reinforcement Learning",
        "aliases": [
          "OraPO"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel approach introduced in the paper, crucial for understanding the methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "The use of a Vision-Language Model is a key component in the proposed method, linking to recent advancements.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "FactScore-based reward",
        "canonical": "FactScore-based Reward",
        "aliases": [
          "FactS"
        ],
        "category": "unique_technical",
        "rationale": "FactScore is a unique scoring mechanism introduced for evaluating the factual accuracy of generated reports.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "CheXpert Plus dataset",
        "canonical": "CheXpert Plus Dataset",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This dataset is critical for benchmarking the proposed method and connects to other works using the same dataset.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Radiology Report Generation",
      "resolved_canonical": "Radiology Report Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Oracle-educated Reinforcement Learning",
      "resolved_canonical": "Oracle-educated Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "FactScore-based reward",
      "resolved_canonical": "FactScore-based Reward",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CheXpert Plus dataset",
      "resolved_canonical": "CheXpert Plus Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# OraPO: Oracle-educated Reinforcement Learning for Data-efficient and Factual Radiology Report Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18600.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18600](https://arxiv.org/abs/2509.18600)

## 🔗 유사한 논문
- [[2025-09-19/MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1: Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (81.7% similar)
- [[2025-09-23/Medical AI Consensus_ A Multi-Agent Framework for Radiology Report Generation and Evaluation_20250923|Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation]] (81.4% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (81.3% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (80.1% similar)
- [[2025-09-23/GRPO-LEAD_ A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models_20250923|GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/CheXpert Plus Dataset|CheXpert Plus Dataset]]
**⚡ Unique Technical**: [[keywords/Radiology Report Generation|Radiology Report Generation]], [[keywords/Oracle-educated Reinforcement Learning|Oracle-educated Reinforcement Learning]], [[keywords/FactScore-based Reward|FactScore-based Reward]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18600v1 Announce Type: cross 
Abstract: Radiology report generation (RRG) aims to automatically produce clinically faithful reports from chest X-ray images. Prevailing work typically follows a scale-driven paradigm, by multi-stage training over large paired corpora and oversized backbones, making pipelines highly data- and compute-intensive. In this paper, we propose Oracle-educated GRPO {OraPO) with a FactScore-based reward (FactS) to tackle the RRG task under constrained budgets. OraPO enables single-stage, RL-only training by converting failed GRPO explorations on rare or difficult studies into direct preference supervision via a lightweight oracle step. FactS grounds learning in diagnostic evidence by extracting atomic clinical facts and checking entailment against ground-truth labels, yielding dense, interpretable sentence-level rewards. Together, OraPO and FactS create a compact and powerful framework that significantly improves learning efficiency on clinically challenging cases, setting the new SOTA performance on the CheXpert Plus dataset (0.341 in F1) with 2--3 orders of magnitude less training data using a small base VLM on modest hardware.

## 📝 요약

이 논문은 방사선 보고서 생성(RRG)을 위한 새로운 접근법인 OraPO를 제안합니다. OraPO는 제한된 자원 하에서 효율적인 학습을 위해 단일 단계의 강화 학습(RL)만을 사용하며, 실패한 탐색을 선호도 지도 학습으로 변환합니다. 또한, FactScore 기반 보상(FactS)을 통해 진단 증거에 기반한 학습을 지원하며, 임상적 사실을 추출하고 이를 참조 레이블과 비교하여 해석 가능한 문장 수준의 보상을 제공합니다. 이 방법론은 CheXpert Plus 데이터셋에서 새로운 최고 성능(F1 점수 0.341)을 기록하며, 기존 방법보다 훨씬 적은 데이터와 자원을 사용하여 임상적으로 어려운 사례에서 학습 효율성을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. Oracle-educated GRPO (OraPO)와 FactScore 기반 보상(FactS)을 통해 제한된 자원 하에서 방사선 보고서 생성(RRG) 작업을 수행합니다.
- 2. OraPO는 실패한 탐색을 선호도 감독으로 전환하여 단일 단계의 강화 학습만으로 훈련을 가능하게 합니다.
- 3. FactS는 진단 증거를 기반으로 학습을 진행하며, 임상적 사실을 추출하고 참조 라벨과의 함의 관계를 확인하여 해석 가능한 문장 수준의 보상을 제공합니다.
- 4. OraPO와 FactS는 CheXpert Plus 데이터셋에서 새로운 SOTA 성능을 달성하며, 적은 양의 훈련 데이터와 소형 VLM을 사용하여 학습 효율성을 크게 향상시킵니다.


---

*Generated on 2025-09-24 13:56:30*