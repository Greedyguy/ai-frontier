---
keywords:
  - WeStar Framework
  - Retrieval Augmented Generation
  - Parametric Retrieval Augmented Generation
  - Direct Preference Optimization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17788
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:09:54.389035",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "WeStar Framework",
    "Retrieval Augmented Generation",
    "Parametric Retrieval Augmented Generation",
    "Direct Preference Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "WeStar Framework": 0.78,
    "Retrieval Augmented Generation": 0.85,
    "Parametric Retrieval Augmented Generation": 0.8,
    "Direct Preference Optimization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "WeStar",
        "canonical": "WeStar Framework",
        "aliases": [
          "WeStar"
        ],
        "category": "unique_technical",
        "rationale": "WeStar is a novel framework specifically designed for scalable, stylized AI assistance, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "RAG",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept that enhances context-grounded generation, facilitating connections in AI research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Parametric RAG",
        "canonical": "Parametric Retrieval Augmented Generation",
        "aliases": [
          "PRAG"
        ],
        "category": "unique_technical",
        "rationale": "Parametric RAG is an extension of RAG that incorporates dynamic style adaptation, offering a unique approach to AI generation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Direct Preference Optimization",
        "canonical": "Direct Preference Optimization",
        "aliases": [
          "DPO"
        ],
        "category": "specific_connectable",
        "rationale": "Direct Preference Optimization is a method that optimizes parameters for style clusters, relevant for linking optimization techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Chain-of-thought prompting",
      "per-account fine-tuning",
      "long prompt-based methods"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "WeStar",
      "resolved_canonical": "WeStar Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "RAG",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Parametric RAG",
      "resolved_canonical": "Parametric Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Direct Preference Optimization",
      "resolved_canonical": "Direct Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# One Agent to Serve All: a Lite-Adaptive Stylized AI Assistant for Millions of Multi-Style Official Accounts

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17788.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17788](https://arxiv.org/abs/2509.17788)

## 🔗 유사한 논문
- [[2025-09-22/Fed-PISA_ Federated Voice Cloning via Personalized Identity-Style Adaptation_20250922|Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation]] (80.5% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (79.5% similar)
- [[2025-09-18/StyleSculptor_ Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance_20250918|StyleSculptor: Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance]] (79.3% similar)
- [[2025-09-23/The STAR-XAI Protocol_ An Interactive Framework for Inducing Second-Order Agency in AI Agents_20250923|The STAR-XAI Protocol: An Interactive Framework for Inducing Second-Order Agency in AI Agents]] (79.0% similar)
- [[2025-09-22/PILOT_ Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting_20250922|PILOT: Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting]] (78.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Direct Preference Optimization|Direct Preference Optimization]]
**⚡ Unique Technical**: [[keywords/WeStar Framework|WeStar Framework]], [[keywords/Parametric Retrieval Augmented Generation|Parametric Retrieval Augmented Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17788v1 Announce Type: cross 
Abstract: Conversational agents deployed in industrial-scale official account platforms must generate responses that are both contextually grounded and stylistically aligned-requirements that existing methods struggle to meet. Chain-of-thought (CoT) prompting induces significant latency due to multi-turn reasoning; per-account fine-tuning is computationally prohibitive; and long prompt-based methods degrade the model's ability to grasp injected context and style. In this paper, we propose WeStar, a lite-adaptive framework for stylized contextual question answering that scales to millions of official accounts. WeStar combines context-grounded generation via RAG with style-aware generation using Parametric RAG (PRAG), where LoRA modules are dynamically activated per style cluster. Our contributions are fourfold: (1) We introduce WeStar, a unified framework capable of serving large volumes of official accounts with minimal overhead. (2) We propose a multi-dimensional, cluster-based parameter sharing scheme that enables compact style representation while preserving stylistic diversity. (3) We develop a style-enhanced Direct Preference Optimization (SeDPO) method to optimize each style cluster's parameters for improved generation quality. (4) Experiments on a large-scale industrial dataset validate the effectiveness and efficiency of WeStar, underscoring its pracitical value in real-world deployment.

## 📝 요약

이 논문에서는 산업 규모의 공식 계정 플랫폼에서 대화형 에이전트가 문맥에 맞고 스타일에 부합하는 응답을 생성하도록 하는 WeStar라는 경량 적응형 프레임워크를 제안합니다. WeStar는 RAG를 통해 문맥 기반 생성과 PRAG를 통해 스타일 인식 생성을 결합하며, 스타일 클러스터별로 LoRA 모듈을 동적으로 활성화합니다. 주요 기여는 다음과 같습니다: (1) 대규모 공식 계정을 최소한의 오버헤드로 지원하는 통합 프레임워크 WeStar를 소개합니다. (2) 스타일 다양성을 유지하면서도 압축된 스타일 표현을 가능하게 하는 다차원 클러스터 기반 매개변수 공유 방식을 제안합니다. (3) 각 스타일 클러스터의 매개변수를 최적화하여 생성 품질을 향상시키는 스타일 강화 직접 선호 최적화(SeDPO) 방법을 개발합니다. (4) 대규모 산업 데이터셋 실험을 통해 WeStar의 효과성과 효율성을 검증하여 실제 적용에서의 실용적 가치를 강조합니다.

## 🎯 주요 포인트

- 1. WeStar는 공식 계정 플랫폼에서 대규모로 활용 가능한 경량 적응형 프레임워크로, 문맥에 기반한 응답 생성과 스타일 인식을 결합하여 높은 효율성을 제공합니다.
- 2. 스타일 클러스터별로 LoRA 모듈을 동적으로 활성화하여, 파라메트릭 RAG를 통해 스타일 다양성을 유지하면서도 컴팩트한 스타일 표현을 가능하게 합니다.
- 3. 스타일 클러스터의 매개변수를 최적화하기 위해 스타일 강화 직접 선호 최적화(SeDPO) 방법을 개발하여 생성 품질을 향상시킵니다.
- 4. 대규모 산업 데이터셋 실험을 통해 WeStar의 효과성과 효율성이 입증되어 실제 배포에서의 실용적 가치를 강조합니다.


---

*Generated on 2025-09-24 00:09:54*