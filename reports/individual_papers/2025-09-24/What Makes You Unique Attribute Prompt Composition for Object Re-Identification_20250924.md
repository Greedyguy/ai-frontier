<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:07:00.941125",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Object Re-Identification",
    "Attribute Prompt Composition",
    "Fast-Slow Training Strategy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Object Re-Identification": 0.78,
    "Attribute Prompt Composition": 0.8,
    "Fast-Slow Training Strategy": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are crucial for linking multimodal learning approaches and are trending in recent research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Object Re-Identification",
        "canonical": "Object Re-Identification",
        "aliases": [
          "Object ReID",
          "ReID"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task in computer vision that is central to the paper's contribution.",
        "novelty_score": 0.67,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Attribute Prompt Composition",
        "canonical": "Attribute Prompt Composition",
        "aliases": [
          "APC"
        ],
        "category": "unique_technical",
        "rationale": "A novel framework introduced in the paper, essential for understanding its unique contribution.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Fast-Slow Training Strategy",
        "canonical": "Fast-Slow Training Strategy",
        "aliases": [
          "FSTS"
        ],
        "category": "unique_technical",
        "rationale": "A novel training strategy proposed in the paper, highlighting its methodological innovation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
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
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Object Re-Identification",
      "resolved_canonical": "Object Re-Identification",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Attribute Prompt Composition",
      "resolved_canonical": "Attribute Prompt Composition",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Fast-Slow Training Strategy",
      "resolved_canonical": "Fast-Slow Training Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# What Makes You Unique? Attribute Prompt Composition for Object Re-Identification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18715.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18715](https://arxiv.org/abs/2509.18715)

## 🔗 유사한 논문
- [[2025-09-23/Towards Anytime Retrieval_ A Benchmark for Anytime Person Re-Identification_20250923|Towards Anytime Retrieval: A Benchmark for Anytime Person Re-Identification]] (83.7% similar)
- [[2025-09-23/ComposeMe_ Attribute-Specific Image Prompts for Controllable Human Image Generation_20250923|ComposeMe: Attribute-Specific Image Prompts for Controllable Human Image Generation]] (82.3% similar)
- [[2025-09-23/Re-Align_ Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization_20250923|Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization]] (81.6% similar)
- [[2025-09-23/Purely Semantic Indexing for LLM-based Generative Recommendation and Retrieval_20250923|Purely Semantic Indexing for LLM-based Generative Recommendation and Retrieval]] (80.8% similar)
- [[2025-09-24/Prompt Optimization Meets Subspace Representation Learning for Few-shot Out-of-Distribution Detection_20250924|Prompt Optimization Meets Subspace Representation Learning for Few-shot Out-of-Distribution Detection]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Object Re-Identification|Object Re-Identification]], [[keywords/Attribute Prompt Composition|Attribute Prompt Composition]], [[keywords/Fast-Slow Training Strategy|Fast-Slow Training Strategy]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18715v1 Announce Type: new 
Abstract: Object Re-IDentification (ReID) aims to recognize individuals across non-overlapping camera views. While recent advances have achieved remarkable progress, most existing models are constrained to either single-domain or cross-domain scenarios, limiting their real-world applicability. Single-domain models tend to overfit to domain-specific features, whereas cross-domain models often rely on diverse normalization strategies that may inadvertently suppress identity-specific discriminative cues. To address these limitations, we propose an Attribute Prompt Composition (APC) framework, which exploits textual semantics to jointly enhance discrimination and generalization. Specifically, we design an Attribute Prompt Generator (APG) consisting of a Semantic Attribute Dictionary (SAD) and a Prompt Composition Module (PCM). SAD is an over-complete attribute dictionary to provide rich semantic descriptions, while PCM adaptively composes relevant attributes from SAD to generate discriminative attribute-aware features. In addition, motivated by the strong generalization ability of Vision-Language Models (VLM), we propose a Fast-Slow Training Strategy (FSTS) to balance ReID-specific discrimination and generalizable representation learning. Specifically, FSTS adopts a Fast Update Stream (FUS) to rapidly acquire ReID-specific discriminative knowledge and a Slow Update Stream (SUS) to retain the generalizable knowledge inherited from the pre-trained VLM. Through a mutual interaction, the framework effectively focuses on ReID-relevant features while mitigating overfitting. Extensive experiments on both conventional and Domain Generalized (DG) ReID datasets demonstrate that our framework surpasses state-of-the-art methods, exhibiting superior performances in terms of both discrimination and generalization. The source code is available at https://github.com/AWangYQ/APC.

## 📝 요약

이 논문은 객체 재식별(Object Re-ID) 문제를 해결하기 위해 Attribute Prompt Composition (APC) 프레임워크를 제안합니다. 기존 모델들은 단일 도메인 또는 교차 도메인 시나리오에 제한되어 실제 적용에 한계가 있었습니다. 이를 해결하기 위해, 텍스트 의미론을 활용하여 식별력과 일반화 능력을 동시에 강화하는 방법을 제안합니다. APC는 Semantic Attribute Dictionary (SAD)와 Prompt Composition Module (PCM)으로 구성된 Attribute Prompt Generator (APG)를 사용하여 풍부한 의미적 설명을 제공하고, 이를 통해 차별화된 속성 인식 특징을 생성합니다. 또한, Vision-Language Models (VLM)의 강력한 일반화 능력을 활용하여 Fast-Slow Training Strategy (FSTS)를 도입, 빠른 업데이트 스트림(FUS)과 느린 업데이트 스트림(SUS)을 통해 재식별 특화 지식과 일반화 지식을 균형 있게 학습합니다. 실험 결과, 제안된 프레임워크는 기존 방법들보다 뛰어난 식별력과 일반화 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 객체 재식별(Object ReID)은 비중첩 카메라 뷰에서 개인을 인식하는 것을 목표로 하며, 기존 모델들은 단일 도메인 또는 교차 도메인 시나리오에 제한되어 실세계 적용에 한계가 있다.
- 2. Attribute Prompt Composition (APC) 프레임워크는 텍스트 의미론을 활용하여 식별력과 일반화 능력을 동시에 향상시키며, Semantic Attribute Dictionary (SAD)와 Prompt Composition Module (PCM)으로 구성된 Attribute Prompt Generator (APG)를 제안한다.
- 3. Vision-Language Models (VLM)의 강력한 일반화 능력에 영감을 받아, Fast-Slow Training Strategy (FSTS)를 통해 ReID-specific 식별력과 일반화 표현 학습을 균형 있게 유지한다.
- 4. 제안된 프레임워크는 ReID 관련 특징에 집중하면서 과적합을 완화하며, 기존 및 도메인 일반화 ReID 데이터셋에서 최첨단 방법들을 능가하는 성능을 보여준다.
- 5. 연구의 소스 코드는 https://github.com/AWangYQ/APC에서 제공된다.


---

*Generated on 2025-09-24 16:07:00*