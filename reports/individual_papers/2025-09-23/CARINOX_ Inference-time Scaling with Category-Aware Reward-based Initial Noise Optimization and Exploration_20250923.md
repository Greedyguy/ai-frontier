---
keywords:
  - Text-to-Image Diffusion Models
  - Compositional Alignment
  - Stable Diffusion
  - Reward Functions
  - CARINOX
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17458
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:51:55.108838",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text-to-Image Diffusion Models",
    "Compositional Alignment",
    "Stable Diffusion",
    "Reward Functions",
    "CARINOX"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text-to-Image Diffusion Models": 0.78,
    "Compositional Alignment": 0.77,
    "Stable Diffusion": 0.8,
    "Reward Functions": 0.7,
    "CARINOX": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Text-to-image diffusion models",
        "canonical": "Text-to-Image Diffusion Models",
        "aliases": [
          "T2I Diffusion Models"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's focus on improving image generation from text, offering a unique technical insight.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Compositional alignment",
        "canonical": "Compositional Alignment",
        "aliases": [
          "Compositionality"
        ],
        "category": "unique_technical",
        "rationale": "The paper addresses challenges in achieving this alignment, making it a key technical focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Stable Diffusion",
        "canonical": "Stable Diffusion",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A well-known model in the field, providing strong connectivity with related works.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reward functions",
        "canonical": "Reward Functions",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Central to the optimization approach discussed, linking to broader machine learning techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Category-Aware Reward-based Initial Noise Optimization and Exploration",
        "canonical": "CARINOX",
        "aliases": [
          "Category-Aware Optimization"
        ],
        "category": "unique_technical",
        "rationale": "A novel framework introduced by the authors, central to the paper's contributions.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
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
      "candidate_surface": "Text-to-image diffusion models",
      "resolved_canonical": "Text-to-Image Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Compositional alignment",
      "resolved_canonical": "Compositional Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Stable Diffusion",
      "resolved_canonical": "Stable Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reward functions",
      "resolved_canonical": "Reward Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Category-Aware Reward-based Initial Noise Optimization and Exploration",
      "resolved_canonical": "CARINOX",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# CARINOX: Inference-time Scaling with Category-Aware Reward-based Initial Noise Optimization and Exploration

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17458.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17458](https://arxiv.org/abs/2509.17458)

## 🔗 유사한 논문
- [[2025-09-22/PCSR_ Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning_20250922|PCSR: Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning]] (84.2% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (82.1% similar)
- [[2025-09-22/OSPO_ Object-centric Self-improving Preference Optimization for Text-to-Image Generation_20250922|OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation]] (81.9% similar)
- [[2025-09-22/Dynamic Classifier-Free Diffusion Guidance via Online Feedback_20250922|Dynamic Classifier-Free Diffusion Guidance via Online Feedback]] (81.9% similar)
- [[2025-09-23/Penalizing Boundary Activation for Object Completeness in Diffusion Models_20250923|Penalizing Boundary Activation for Object Completeness in Diffusion Models]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reward Functions|Reward Functions]]
**🔗 Specific Connectable**: [[keywords/Stable Diffusion|Stable Diffusion]]
**⚡ Unique Technical**: [[keywords/Text-to-Image Diffusion Models|Text-to-Image Diffusion Models]], [[keywords/Compositional Alignment|Compositional Alignment]], [[keywords/CARINOX|CARINOX]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17458v1 Announce Type: new 
Abstract: Text-to-image diffusion models, such as Stable Diffusion, can produce high-quality and diverse images but often fail to achieve compositional alignment, particularly when prompts describe complex object relationships, attributes, or spatial arrangements. Recent inference-time approaches address this by optimizing or exploring the initial noise under the guidance of reward functions that score text-image alignment without requiring model fine-tuning. While promising, each strategy has intrinsic limitations when used alone: optimization can stall due to poor initialization or unfavorable search trajectories, whereas exploration may require a prohibitively large number of samples to locate a satisfactory output. Our analysis further shows that neither single reward metrics nor ad-hoc combinations reliably capture all aspects of compositionality, leading to weak or inconsistent guidance. To overcome these challenges, we present Category-Aware Reward-based Initial Noise Optimization and Exploration (CARINOX), a unified framework that combines noise optimization and exploration with a principled reward selection procedure grounded in correlation with human judgments. Evaluations on two complementary benchmarks covering diverse compositional challenges show that CARINOX raises average alignment scores by +16% on T2I-CompBench++ and +11% on the HRS benchmark, consistently outperforming state-of-the-art optimization and exploration-based methods across all major categories, while preserving image quality and diversity. The project page is available at https://amirkasaei.com/carinox/{this URL}.

## 📝 요약

이 논문은 텍스트-이미지 변환 확산 모델의 조합적 정렬 문제를 해결하기 위해 CARINOX라는 새로운 프레임워크를 제안합니다. 기존 방법들은 초기화 문제나 많은 샘플 요구 등 한계가 있었으나, CARINOX는 인간 판단과의 상관관계를 고려한 보상 선택 절차를 통해 초기 노이즈 최적화와 탐색을 결합합니다. 두 가지 벤치마크에서 CARINOX는 평균 정렬 점수를 각각 16%와 11% 향상시켰으며, 이미지 품질과 다양성을 유지하면서도 기존 방법들을 능가하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 텍스트-이미지 변환 확산 모델은 복잡한 객체 관계나 속성, 공간 배열을 설명하는 프롬프트에서 구성적 정렬을 잘 이루지 못하는 문제가 있다.
- 2. 기존의 추론 시간 접근법은 모델의 미세 조정 없이 텍스트-이미지 정렬을 점수화하는 보상 함수를 통해 초기 노이즈를 최적화하거나 탐색하여 이 문제를 해결하려 한다.
- 3. 단일 보상 메트릭이나 임시 조합으로는 구성적 요소를 완벽히 포착하지 못해 일관성 없는 지침을 제공한다.
- 4. CARINOX는 노이즈 최적화와 탐색을 결합하고, 인간 판단과의 상관관계를 기반으로 한 보상 선택 절차를 통해 이 문제를 해결하는 통합 프레임워크이다.
- 5. CARINOX는 다양한 구성적 도전을 다루는 두 가지 벤치마크에서 평균 정렬 점수를 각각 16%, 11% 향상시키며, 이미지 품질과 다양성을 유지하면서 최신 최적화 및 탐색 기반 방법을 능가한다.


---

*Generated on 2025-09-24 04:51:55*