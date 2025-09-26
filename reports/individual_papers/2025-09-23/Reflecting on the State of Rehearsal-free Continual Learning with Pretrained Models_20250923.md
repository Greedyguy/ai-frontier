---
keywords:
  - Continual Learning
  - Pretrained Models
  - Parameter-efficient Finetuning
  - Rehearsal-free Continual Learning
  - Elastic Weight Consolidation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2406.09384
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:33:06.061207",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Continual Learning",
    "Pretrained Models",
    "Parameter-efficient Finetuning",
    "Rehearsal-free Continual Learning",
    "Elastic Weight Consolidation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Continual Learning": 0.85,
    "Pretrained Models": 0.8,
    "Parameter-efficient Finetuning": 0.78,
    "Rehearsal-free Continual Learning": 0.77,
    "Elastic Weight Consolidation": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Continual Learning",
        "canonical": "Continual Learning",
        "aliases": [
          "CL"
        ],
        "category": "broad_technical",
        "rationale": "Continual Learning is a central theme of the paper and connects to various machine learning paradigms.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Pretrained Models",
        "canonical": "Pretrained Models",
        "aliases": [
          "Pretrained Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Pretrained Models are crucial for understanding the shift in continual learning methods discussed.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Parameter-efficient Finetuning",
        "canonical": "Parameter-efficient Finetuning",
        "aliases": [
          "PEFT"
        ],
        "category": "unique_technical",
        "rationale": "This technique is pivotal in the paper's analysis of continual learning approaches.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Rehearsal-free Continual Learning",
        "canonical": "Rehearsal-free Continual Learning",
        "aliases": [
          "RFCL"
        ],
        "category": "unique_technical",
        "rationale": "RFCL is a specific focus of the study, highlighting a novel approach in the field.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Elastic Weight Consolidation",
        "canonical": "Elastic Weight Consolidation",
        "aliases": [
          "EWC"
        ],
        "category": "specific_connectable",
        "rationale": "EWC is a standard technique in continual learning, providing a baseline for comparison.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "methodological choices",
      "benchmark scores"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Continual Learning",
      "resolved_canonical": "Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Pretrained Models",
      "resolved_canonical": "Pretrained Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Parameter-efficient Finetuning",
      "resolved_canonical": "Parameter-efficient Finetuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Rehearsal-free Continual Learning",
      "resolved_canonical": "Rehearsal-free Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Elastic Weight Consolidation",
      "resolved_canonical": "Elastic Weight Consolidation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Reflecting on the State of Rehearsal-free Continual Learning with Pretrained Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2406.09384.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2406.09384](https://arxiv.org/abs/2406.09384)

## 🔗 유사한 논문
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning]] (83.5% similar)
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (81.5% similar)
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (81.0% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (80.5% similar)
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Continual Learning|Continual Learning]]
**🔗 Specific Connectable**: [[keywords/Pretrained Models|Pretrained Models]], [[keywords/Elastic Weight Consolidation|Elastic Weight Consolidation]]
**⚡ Unique Technical**: [[keywords/Parameter-efficient Finetuning|Parameter-efficient Finetuning]], [[keywords/Rehearsal-free Continual Learning|Rehearsal-free Continual Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.09384v2 Announce Type: replace 
Abstract: With the advent and recent ubiquity of foundation models, continual learning (CL) has recently shifted from continual training from scratch to the continual adaptation of pretrained models, seeing particular success on rehearsal-free CL benchmarks (RFCL). To achieve this, most proposed methods adapt and restructure parameter-efficient finetuning techniques (PEFT) to suit the continual nature of the problem. Based most often on input-conditional query-mechanisms or regularizations on top of prompt- or adapter-based PEFT, these PEFT-style RFCL (P-RFCL) approaches report peak performances; often convincingly outperforming existing CL techniques. However, on the other end, critical studies have recently highlighted competitive results by training on just the first task or via simple non-parametric baselines. Consequently, questions arise about the relationship between methodological choices in P-RFCL and their reported high benchmark scores. In this work, we tackle these questions to better understand the true drivers behind strong P-RFCL performances, their placement w.r.t. recent first-task adaptation studies, and their relation to preceding CL standards such as EWC or SI. In particular, we show: (1) P-RFCL techniques relying on input-conditional query mechanisms work not because, but rather despite them by collapsing towards standard PEFT shortcut solutions. (2) Indeed, we show how most often, P-RFCL techniques can be matched by a simple and lightweight PEFT baseline. (3) Using this baseline, we identify the implicit bound on tunable parameters when deriving RFCL approaches from PEFT methods as a potential denominator behind P-RFCL efficacy. Finally, we (4) better disentangle continual versus first-task adaptation, and (5) motivate standard RFCL techniques s.a. EWC or SI in light of recent P-RFCL methods.

## 📝 요약

이 논문은 사전 학습된 모델의 지속적 적응을 중점으로 하는 지속 학습(CL) 분야에서의 최근 발전을 다룹니다. 특히, 리허설이 필요 없는 지속 학습(RFCL) 벤치마크에서 성공을 거둔 PEFT 스타일의 RFCL(P-RFCL) 접근법을 분석합니다. 주요 발견으로는, P-RFCL 기법이 입력 조건 쿼리 메커니즘에 의존하지만, 실제로는 표준 PEFT 해결책으로 수렴하여 효과를 발휘한다는 점을 제시합니다. 또한, 간단한 PEFT 기반이 P-RFCL 기법과 유사한 성능을 보일 수 있음을 보여주며, 조정 가능한 매개변수의 암묵적 경계가 P-RFCL의 효율성에 기여할 수 있음을 밝힙니다. 마지막으로, 지속적 적응과 첫 번째 과제 적응을 명확히 구분하고, EWC나 SI 같은 기존 RFCL 기법의 중요성을 재조명합니다.

## 🎯 주요 포인트

- 1. 최근의 연구는 사전 학습된 모델의 지속적 적응으로 초점을 전환하여 리허설 없는 지속적 학습(RFCL) 벤치마크에서 성공을 거두고 있습니다.
- 2. PEFT 스타일의 RFCL 접근법은 입력 조건 쿼리 메커니즘이나 프롬프트 기반 PEFT 위의 정규화를 활용하여 기존 지속적 학습 기법을 능가하는 성능을 보고합니다.
- 3. 연구는 P-RFCL 기법이 입력 조건 쿼리 메커니즘에 의존하지 않고도 표준 PEFT 해결책으로 수렴하여 작동함을 보여줍니다.
- 4. 간단하고 경량화된 PEFT 기준선이 대부분의 P-RFCL 기법과 성능을 맞출 수 있음을 증명합니다.
- 5. 연구는 지속적 학습과 첫 번째 과제 적응을 더 잘 구분하고, 최근 P-RFCL 방법에 비추어 EWC나 SI와 같은 표준 RFCL 기법의 필요성을 강조합니다.


---

*Generated on 2025-09-24 02:33:06*