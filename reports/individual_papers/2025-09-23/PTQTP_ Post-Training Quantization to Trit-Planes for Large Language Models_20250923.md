---
keywords:
  - Post-Training Quantization
  - Large Language Model
  - Ternary-weight Quantization
  - Quantization-aware Training
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16989
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:40:02.818293",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Post-Training Quantization",
    "Large Language Model",
    "Ternary-weight Quantization",
    "Quantization-aware Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Post-Training Quantization": 0.78,
    "Large Language Model": 0.85,
    "Ternary-weight Quantization": 0.82,
    "Quantization-aware Training": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Post-Training Quantization",
        "canonical": "Post-Training Quantization",
        "aliases": [
          "PTQ"
        ],
        "category": "unique_technical",
        "rationale": "Post-Training Quantization is a specific technique relevant to optimizing model deployment, enhancing connectivity with quantization methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus and connect broadly to the field of NLP and AI.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Ternary-weight PTQ",
        "canonical": "Ternary-weight Quantization",
        "aliases": [
          "Ternary PTQ",
          "Trit-Planes Quantization"
        ],
        "category": "unique_technical",
        "rationale": "Ternary-weight PTQ is a novel approach in the paper, offering a unique method for model optimization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Quantization-aware Training",
        "canonical": "Quantization-aware Training",
        "aliases": [
          "QAT"
        ],
        "category": "specific_connectable",
        "rationale": "Quantization-aware Training is a related concept that enhances understanding of model optimization techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
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
      "candidate_surface": "Post-Training Quantization",
      "resolved_canonical": "Post-Training Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Ternary-weight PTQ",
      "resolved_canonical": "Ternary-weight Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Quantization-aware Training",
      "resolved_canonical": "Quantization-aware Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PTQTP: Post-Training Quantization to Trit-Planes for Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16989.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16989](https://arxiv.org/abs/2509.16989)

## 🔗 유사한 논문
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (89.0% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (84.7% similar)
- [[2025-09-22/MEC-Quant_ Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training_20250922|MEC-Quant: Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training]] (83.4% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (83.4% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Quantization-aware Training|Quantization-aware Training]]
**⚡ Unique Technical**: [[keywords/Post-Training Quantization|Post-Training Quantization]], [[keywords/Ternary-weight Quantization|Ternary-weight Quantization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16989v1 Announce Type: cross 
Abstract: Post-training quantization (PTQ) of large language models (LLMs) to extremely low bit-widths remains challenging due to the fundamental trade-off between computational efficiency and model expressiveness. While existing ultra-low-bit PTQ methods rely on binary approximations or complex compensation mechanisms, they suffer from either limited representational capacity or computational overhead that undermines their efficiency gains. We introduce PTQ to Trit-Planes (PTQTP), the first ternary-weight PTQ framework that decomposes weight matrices into structured ternary {-1, 0, 1} trit-planes using 2x1.58-bit representation. PTQTP achieves multiplication-free inference, identical to 1-bit quantization, while maintaining superior expressiveness through its novel structured decomposition. Our approach provides: (1) a theoretically grounded progressive approximation algorithm ensuring global weight consistency; (2) model-agnostic deployment across diverse modern LLMs without architectural modifications; and (3) uniform ternary operations that eliminate the need for mixed-precision or compensation schemes. Comprehensive experiments across LLaMA3.x and Qwen3 model families (0.6B-70B parameters) demonstrate that PTQTP significantly outperforms existing low-bit PTQ methods, achieving 82.4% mathematical reasoning retention versus 0% for competing approaches. PTQTP approaches and sometimes surpasses 1.58-bit quantization-aware training performance while requiring only single-hour quantization compared to 10-14 GPU days for training-based methods. These results establish PTQTP as a practical solution for efficient LLM deployment in resource-constrained environments.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 극저비트 후처리 양자화(PTQ) 문제를 해결하기 위해 PTQTP라는 새로운 3진 가중치 PTQ 프레임워크를 제안합니다. PTQTP는 가중치 행렬을 구조화된 3진 {-1, 0, 1} 형태로 분해하여 2x1.58비트로 표현하며, 곱셈이 필요 없는 추론을 가능하게 합니다. 주요 기여는 다음과 같습니다: (1) 전역 가중치 일관성을 보장하는 점진적 근사 알고리즘, (2) 다양한 LLM에 아키텍처 수정 없이 적용 가능한 모델 비종속적 배포, (3) 혼합 정밀도나 보상 체계가 필요 없는 균일한 3진 연산. 실험 결과, PTQTP는 기존 저비트 PTQ 방법보다 우수한 성능을 보이며, 수학적 추론 유지율 82.4%를 달성합니다. 또한, 1.58비트 양자화 인식 훈련 성능에 근접하거나 이를 초과하면서도, 단 1시간의 양자화 시간만 소요됩니다. 이는 자원 제약 환경에서 LLM의 효율적 배포를 위한 실용적 솔루션으로 자리잡습니다.

## 🎯 주요 포인트

- 1. PTQTP는 가중치 행렬을 구조화된 삼진 {-1, 0, 1} 트릿-플레인으로 분해하여 곱셈 없는 추론을 가능하게 합니다.
- 2. PTQTP는 다양한 현대 대형 언어 모델(LLM)에 아키텍처 수정 없이 적용할 수 있는 모델-비종속적 배포를 제공합니다.
- 3. PTQTP는 혼합 정밀도나 보상 체계가 필요 없는 균일한 삼진 연산을 통해 기존 저비트 PTQ 방법을 능가하는 성능을 보여줍니다.
- 4. PTQTP는 수학적 추론 유지율에서 기존 방법의 0%에 비해 82.4%를 달성하며, 1.58비트 양자화 인식 훈련 성능에 근접하거나 이를 초과하는 성과를 보입니다.
- 5. PTQTP는 단시간(몇 시간) 양자화로도 기존 훈련 기반 방법의 10-14 GPU일 소요를 대체할 수 있는 실용적인 솔루션입니다.


---

*Generated on 2025-09-23 23:40:02*