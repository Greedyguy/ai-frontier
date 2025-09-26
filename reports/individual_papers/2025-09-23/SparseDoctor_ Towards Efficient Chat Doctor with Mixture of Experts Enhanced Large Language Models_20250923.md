---
keywords:
  - Large Language Model
  - SparseDoctor
  - Contrastive Learning
  - Mixture of Experts
  - Low Rank Adaptation-Mixture of Experts
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.14269
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:31:32.467546",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "SparseDoctor",
    "Contrastive Learning",
    "Mixture of Experts",
    "Low Rank Adaptation-Mixture of Experts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "SparseDoctor": 0.7,
    "Contrastive Learning": 0.75,
    "Mixture of Experts": 0.7,
    "Low Rank Adaptation-Mixture of Experts": 0.65
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
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's focus on enhancing language models for medical applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      },
      {
        "surface": "SparseDoctor",
        "canonical": "SparseDoctor",
        "aliases": [
          "Sparse Doctor"
        ],
        "category": "unique_technical",
        "rationale": "A novel model introduced in the paper, representing a unique contribution to the field.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Contrastive Learning",
        "aliases": [
          "Contrastive"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for enhancing the model's performance and is a key component of the proposed architecture.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Mixture of Experts",
        "canonical": "Mixture of Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "A significant architectural element that enhances the model's efficiency and effectiveness.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "LoRA-MoE",
        "canonical": "Low Rank Adaptation-Mixture of Experts",
        "aliases": [
          "LoRA-MoE"
        ],
        "category": "unique_technical",
        "rationale": "A specific architecture proposed in the paper, combining low-rank adaptation with mixture of experts.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "training cost",
      "memory overflow"
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
        "specificity": 0.5,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "SparseDoctor",
      "resolved_canonical": "SparseDoctor",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Mixture of Experts",
      "resolved_canonical": "Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "LoRA-MoE",
      "resolved_canonical": "Low Rank Adaptation-Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14269.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.14269](https://arxiv.org/abs/2509.14269)

## 🔗 유사한 논문
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (87.5% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (86.9% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (86.9% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (85.3% similar)
- [[2025-09-18/Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes_20250918|Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Contrastive Learning|Contrastive Learning]], [[keywords/Mixture of Experts|Mixture of Experts]]
**⚡ Unique Technical**: [[keywords/SparseDoctor|SparseDoctor]], [[keywords/Low Rank Adaptation-Mixture of Experts|Low Rank Adaptation-Mixture of Experts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14269v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) have achieved great success in medical question answering and clinical decision-making, promoting the efficiency and popularization of the personalized virtual doctor in society. However, the traditional fine-tuning strategies on LLM require the updates of billions of parameters, substantially increasing the training cost, including the training time and utility cost. To enhance the efficiency and effectiveness of the current medical LLMs and explore the boundary of the representation capability of the LLMs on the medical domain, apart from the traditional fine-tuning strategies from the data perspective (i.e., supervised fine-tuning or reinforcement learning from human feedback), we instead craft a novel sparse medical LLM named SparseDoctor armed with contrastive learning enhanced LoRA-MoE (low rank adaptation-mixture of experts) architecture. To this end, the crafted automatic routing mechanism can scientifically allocate the computational resources among different LoRA experts supervised by the contrastive learning. Additionally, we also introduce a novel expert memory queue mechanism to further boost the efficiency of the overall framework and prevent the memory overflow during training. We conduct comprehensive evaluations on three typical medical benchmarks: CMB, CMExam, and CMMLU-Med. Experimental results demonstrate that the proposed LLM can consistently outperform the strong baselines such as the HuatuoGPT series.

## 📝 요약

이 논문은 의료 분야에서 대형 언어 모델(LLM)의 효율성과 효과성을 향상시키기 위해 SparseDoctor라는 새로운 희소 의료 LLM을 제안합니다. 전통적인 미세 조정 방식이 아닌, 대조 학습이 강화된 LoRA-MoE(저차원 적응-전문가 혼합) 아키텍처를 활용하여 모델을 설계했습니다. 이를 통해 자동 라우팅 메커니즘이 다양한 LoRA 전문가들 간의 계산 자원을 과학적으로 배분할 수 있도록 했습니다. 또한, 새로운 전문가 메모리 큐 메커니즘을 도입하여 훈련 중 메모리 오버플로를 방지하고 효율성을 높였습니다. CMB, CMExam, CMMLU-Med 등 세 가지 의료 벤치마크에서의 평가 결과, 제안된 모델이 기존 강력한 모델들보다 일관되게 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)은 의료 분야에서 질문 응답 및 임상 의사 결정에 큰 성공을 거두었으나, 전통적인 미세 조정 전략은 막대한 매개변수 업데이트로 인해 높은 훈련 비용을 초래한다.
- 2. SparseDoctor라는 새로운 희소 의료 LLM은 대조 학습이 강화된 LoRA-MoE 아키텍처를 통해 효율성과 효과성을 높이고자 한다.
- 3. 자동 라우팅 메커니즘은 대조 학습에 의해 감독되는 다양한 LoRA 전문가들 간의 계산 자원을 과학적으로 할당한다.
- 4. 새로운 전문가 메모리 큐 메커니즘을 도입하여 전체 프레임워크의 효율성을 높이고 훈련 중 메모리 오버플로를 방지한다.
- 5. 세 가지 의료 벤치마크(CMB, CMExam, CMMLU-Med)에서의 실험 결과, 제안된 LLM은 HuatuoGPT 시리즈와 같은 강력한 기준 모델을 일관되게 능가한다.


---

*Generated on 2025-09-24 01:31:32*