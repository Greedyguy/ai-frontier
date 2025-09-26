---
keywords:
  - Large Language Model
  - Zeroth-Order Optimization
  - Multi-Perturbed LoRA
  - Inference Engine
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2409.15520
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:35:06.721176",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Zeroth-Order Optimization",
    "Multi-Perturbed LoRA",
    "Inference Engine"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Zeroth-Order Optimization": 0.78,
    "Multi-Perturbed LoRA": 0.82,
    "Inference Engine": 0.75
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
        "rationale": "Central to the paper's focus on fine-tuning and edge deployment, linking to broader discussions on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "zeroth-order optimization",
        "canonical": "Zeroth-Order Optimization",
        "aliases": [
          "ZO optimization"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel optimization method crucial for the proposed framework, enhancing technical specificity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-Perturbed LoRA",
        "canonical": "Multi-Perturbed LoRA",
        "aliases": [
          "MP-LoRA"
        ],
        "category": "unique_technical",
        "rationale": "A specific module innovation that is key to the framework's efficiency, offering a unique technical link.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "inference engines",
        "canonical": "Inference Engine",
        "aliases": [
          "ExecuTorch"
        ],
        "category": "specific_connectable",
        "rationale": "Inference engines are repurposed for fine-tuning, connecting to broader discussions on model deployment.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "zeroth-order optimization",
      "resolved_canonical": "Zeroth-Order Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-Perturbed LoRA",
      "resolved_canonical": "Multi-Perturbed LoRA",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "inference engines",
      "resolved_canonical": "Inference Engine",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2409.15520.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2409.15520](https://arxiv.org/abs/2409.15520)

## 🔗 유사한 논문
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (85.5% similar)
- [[2025-09-23/SparseDoctor_ Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models_20250923|SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models]] (84.0% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (83.9% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (83.8% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Inference Engine|Inference Engine]]
**⚡ Unique Technical**: [[keywords/Zeroth-Order Optimization|Zeroth-Order Optimization]], [[keywords/Multi-Perturbed LoRA|Multi-Perturbed LoRA]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.15520v3 Announce Type: replace 
Abstract: Large Language Models (LLMs) are currently pre-trained and fine-tuned on large cloud servers. The next frontier is LLM personalization, where a foundation model can be fine-tuned with user/task-specific data. Given the sensitive nature of such private data, it is desirable to fine-tune these models on edge devices to improve user trust. However, fine-tuning on resource-constrained edge devices presents significant challenges due to substantial memory and computational demands, as well as limited infrastructure support. We observe that inference engines (e.g., ExecuTorch) can be repurposed for fine-tuning by leveraging zeroth-order (ZO) optimization, which uses multiple forward passes to approximate gradients. While promising, direct application of ZO methods on edge devices is inefficient due to the high computational cost of multiple forward passes required for accurate gradient estimation, and their deployment has been largely unexplored in practice. We introduce MobiZO, a resource-efficient fine-tuning framework for LLMs specifically designed for edge devices. MobiZO combines three key innovations: (1) a parallelized randomized gradient estimator that employs both outer-loop and inner-loop parallelism to eliminate sequential forward passes, (2) a specialized Multi-Perturbed LoRA (MP-LoRA) module that enables efficient realization of both inner and outer loop parallelism, and (3) a seamless integration with ExecuTorch for on-device training, requiring no modifications to the runtime. Experiments demonstrate that MobiZO achieves substantial runtime speedups and memory savings while improving fine-tuning accuracy, paving the way for practical deployment of LLMs in real-time, on-device applications.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 개인화를 위한 새로운 접근법을 제안합니다. 기존에는 대형 서버에서 사전 훈련 및 미세 조정이 이루어졌으나, 사용자 신뢰를 높이기 위해 엣지 디바이스에서의 미세 조정이 필요합니다. 그러나 엣지 디바이스의 자원 한계로 인해 어려움이 있습니다. 이를 해결하기 위해 제안된 MobiZO는 자원 효율적인 미세 조정 프레임워크로, 엣지 디바이스에서의 실행을 위해 설계되었습니다. MobiZO는 병렬화된 무작위 기울기 추정기, Multi-Perturbed LoRA 모듈, 그리고 ExecuTorch와의 통합을 통해 자원 소모를 줄이고 정확성을 높입니다. 실험 결과, MobiZO는 실행 속도와 메모리 사용을 개선하며, 실시간 디바이스 상의 LLM 활용 가능성을 열었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 개인화는 사용자/작업별 데이터로 모델을 미세 조정하는 것으로, 민감한 데이터를 보호하기 위해 엣지 디바이스에서의 미세 조정이 필요합니다.
- 2. 엣지 디바이스에서의 미세 조정은 메모리와 계산 요구량이 크고 인프라 지원이 제한적이어서 도전 과제가 됩니다.
- 3. MobiZO는 엣지 디바이스에 특화된 자원 효율적인 LLM 미세 조정 프레임워크로, 병렬화된 무작위 그래디언트 추정기와 MP-LoRA 모듈을 활용하여 효율성을 높입니다.
- 4. MobiZO는 ExecuTorch와의 통합을 통해 엣지 디바이스에서의 실시간, 온디바이스 애플리케이션 배포를 가능하게 하며, 런타임 수정이 필요 없습니다.
- 5. 실험 결과, MobiZO는 실행 시간 단축과 메모리 절약을 달성하면서도 미세 조정 정확도를 향상시킵니다.


---

*Generated on 2025-09-24 02:35:06*