---
keywords:
  - Large Language Model
  - Model Pruning
  - Prefill-Decode Disaggregation
  - KV Cache Pruning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.04467
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:25:38.492154",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Model Pruning",
    "Prefill-Decode Disaggregation",
    "KV Cache Pruning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Model Pruning": 0.82,
    "Prefill-Decode Disaggregation": 0.79,
    "KV Cache Pruning": 0.77
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
        "rationale": "LLMs are central to the paper's focus on computational efficiency and pruning strategies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Model Pruning",
        "canonical": "Model Pruning",
        "aliases": [
          "Pruning"
        ],
        "category": "unique_technical",
        "rationale": "Model pruning is a key technique discussed for improving inference efficiency.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Prefill-Decode Disaggregation",
        "canonical": "Prefill-Decode Disaggregation",
        "aliases": [
          "PD Disaggregation"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced in the paper, crucial for understanding the proposed pruning method.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "KV Cache Pruning",
        "canonical": "KV Cache Pruning",
        "aliases": [
          "Key-Value Cache Pruning"
        ],
        "category": "unique_technical",
        "rationale": "KV Cache Pruning is a specific technique highlighted for its role in reducing communication costs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "inference",
      "performance",
      "method"
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
      "candidate_surface": "Model Pruning",
      "resolved_canonical": "Model Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Prefill-Decode Disaggregation",
      "resolved_canonical": "Prefill-Decode Disaggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "KV Cache Pruning",
      "resolved_canonical": "KV Cache Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.04467.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.04467](https://arxiv.org/abs/2509.04467)

## 🔗 유사한 논문
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (86.5% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (85.8% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (84.9% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.7% similar)
- [[2025-09-22/Backdoor Mitigation via Invertible Pruning Masks_20250922|Backdoor Mitigation via Invertible Pruning Masks]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Model Pruning|Model Pruning]], [[keywords/Prefill-Decode Disaggregation|Prefill-Decode Disaggregation]], [[keywords/KV Cache Pruning|KV Cache Pruning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.04467v2 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) demonstrate exceptional capabilities across various tasks, but their deployment is constrained by high computational and memory costs. Model pruning provides an effective means to alleviate these demands. However, existing methods often ignore the characteristics of prefill-decode (PD) disaggregation in practice. In this paper, we propose a novel pruning method for PD disaggregation inference, enabling more precise and efficient block and KV Cache pruning. Our approach constructs pruning and distillation sets to perform iterative block removal independently for the prefill and decode stages, obtaining better pruning solutions. Moreover, we introduce a token-aware cache pruning mechanism that retains all KV Cache in the prefill stage but selectively reuses entries for the first and last token sequences in selected layers during decode, reducing communication costs with minimal overhead. Extensive experiments demonstrate that our approach consistently achieves strong performance in both PD disaggregation and PD unified settings without disaggregation. Under the same (default) settings, our method achieves improved performance and faster inference, along with a 4.95$\times$ reduction in data transmission bandwidth consumption.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 높은 계산 및 메모리 비용 문제를 해결하기 위해 모델 가지치기 기법을 제안합니다. 기존 방법들이 프리필-디코드(PD) 분해의 특성을 간과하는 반면, 본 연구는 PD 분해 추론을 위한 새로운 가지치기 방법을 제시하여 블록 및 KV 캐시 가지치기를 보다 정밀하고 효율적으로 수행합니다. 프리필 및 디코드 단계에서 독립적으로 블록 제거를 수행하는 가지치기 및 증류 세트를 구성하여 더 나은 가지치기 솔루션을 얻습니다. 또한, 토큰 인식 캐시 가지치기 메커니즘을 도입하여 프리필 단계에서는 모든 KV 캐시를 유지하되, 디코드 단계에서는 선택된 레이어의 첫 번째 및 마지막 토큰 시퀀스에 대해 선택적으로 재사용하여 통신 비용을 줄입니다. 실험 결과, 제안된 방법은 PD 분해 및 비분해 환경 모두에서 강력한 성능을 일관되게 보여주며, 데이터 전송 대역폭 소비를 4.95배 줄이면서 성능과 추론 속도를 개선합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)의 높은 계산 및 메모리 비용 문제를 모델 가지치기를 통해 해결하고자 합니다.
- 2. 기존 방법들이 간과한 prefill-decode(PD) 분해의 특성을 고려한 새로운 가지치기 방법을 제안합니다.
- 3. 제안된 방법은 prefill 및 decode 단계에서 독립적으로 블록 제거를 수행하여 더 나은 가지치기 솔루션을 제공합니다.
- 4. 토큰 인식 캐시 가지치기 메커니즘을 도입하여 통신 비용을 줄이면서도 최소한의 오버헤드로 성능을 유지합니다.
- 5. 실험 결과, 제안된 방법은 PD 분해 및 비분해 설정 모두에서 강력한 성능을 일관되게 달성하며 데이터 전송 대역폭 소비를 4.95배 줄입니다.


---

*Generated on 2025-09-24 01:25:38*