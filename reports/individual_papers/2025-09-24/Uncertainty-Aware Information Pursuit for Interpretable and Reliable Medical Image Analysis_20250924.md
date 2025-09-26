<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:31:19.917442",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Variational Information Pursuit",
    "Uncertainty-Aware Models",
    "Medical Imaging",
    "Concept-Based Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Variational Information Pursuit": 0.78,
    "Uncertainty-Aware Models": 0.77,
    "Medical Imaging": 0.72,
    "Concept-Based Models": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Variational Information Pursuit",
        "canonical": "Variational Information Pursuit",
        "aliases": [
          "V-IP"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific framework central to the paper's methodology, enhancing interpretability in medical imaging.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Uncertainty-Aware Models",
        "canonical": "Uncertainty-Aware Models",
        "aliases": [
          "EUAV-IP",
          "IUAV-IP"
        ],
        "category": "unique_technical",
        "rationale": "These models are novel contributions that integrate uncertainty into the decision-making process, crucial for reliable medical image analysis.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Medical Imaging",
        "canonical": "Medical Imaging",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental domain in the paper, connecting with various AI applications in healthcare.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Concept-Based Models",
        "canonical": "Concept-Based Models",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "These models are central to the interpretability aspect of the framework, allowing for human-understandable predictions.",
        "novelty_score": 0.68,
        "connectivity_score": 0.74,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "interpretability",
      "reliability",
      "AI systems"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Variational Information Pursuit",
      "resolved_canonical": "Variational Information Pursuit",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Uncertainty-Aware Models",
      "resolved_canonical": "Uncertainty-Aware Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Medical Imaging",
      "resolved_canonical": "Medical Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Concept-Based Models",
      "resolved_canonical": "Concept-Based Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.74,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Uncertainty-Aware Information Pursuit for Interpretable and Reliable Medical Image Analysis

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.16742.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2506.16742](https://arxiv.org/abs/2506.16742)

## 🔗 유사한 논문
- [[2025-09-24/Position Paper_ Integrating Explainability and Uncertainty Estimation in Medical AI_20250924|Position Paper: Integrating Explainability and Uncertainty Estimation in Medical AI]] (86.1% similar)
- [[2025-09-23/Towards a Transparent and Interpretable AI Model for Medical Image Classifications_20250923|Towards a Transparent and Interpretable AI Model for Medical Image Classifications]] (85.4% similar)
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (84.9% similar)
- [[2025-09-23/Uncertainty-Supervised Interpretable and Robust Evidential Segmentation_20250923|Uncertainty-Supervised Interpretable and Robust Evidential Segmentation]] (84.7% similar)
- [[2025-09-24/VIBE_ Annotation-Free Video-to-Text Information Bottleneck Evaluation for TL;DR_20250924|VIBE: Annotation-Free Video-to-Text Information Bottleneck Evaluation for TL;DR]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Medical Imaging|Medical Imaging]]
**🔗 Specific Connectable**: [[keywords/Concept-Based Models|Concept-Based Models]]
**⚡ Unique Technical**: [[keywords/Variational Information Pursuit|Variational Information Pursuit]], [[keywords/Uncertainty-Aware Models|Uncertainty-Aware Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.16742v2 Announce Type: replace 
Abstract: To be adopted in safety-critical domains like medical image analysis, AI systems must provide human-interpretable decisions. Variational Information Pursuit (V-IP) offers an interpretable-by-design framework by sequentially querying input images for human-understandable concepts, using their presence or absence to make predictions. However, existing V-IP methods overlook sample-specific uncertainty in concept predictions, which can arise from ambiguous features or model limitations, leading to suboptimal query selection and reduced robustness. In this paper, we propose an interpretable and uncertainty-aware framework for medical imaging that addresses these limitations by accounting for upstream uncertainties in concept-based, interpretable-by-design models. Specifically, we introduce two uncertainty-aware models, EUAV-IP and IUAV-IP, that integrate uncertainty estimates into the V-IP querying process to prioritize more reliable concepts per sample. EUAV-IP skips uncertain concepts via masking, while IUAV-IP incorporates uncertainty into query selection implicitly for more informed and clinically aligned decisions. Our approach allows models to make reliable decisions based on a subset of concepts tailored to each individual sample, without human intervention, while maintaining overall interpretability. We evaluate our methods on five medical imaging datasets across four modalities: dermoscopy, X-ray, ultrasound, and blood cell imaging. The proposed IUAV-IP model achieves state-of-the-art accuracy among interpretable-by-design approaches on four of the five datasets, and generates more concise explanations by selecting fewer yet more informative concepts. These advances enable more reliable and clinically meaningful outcomes, enhancing model trustworthiness and supporting safer AI deployment in healthcare.

## 📝 요약

이 논문은 의료 영상 분석에서 인간이 이해할 수 있는 AI 시스템을 개발하기 위한 방법론을 제안합니다. 기존의 V-IP 방법론은 개념 예측의 불확실성을 고려하지 않아 최적의 쿼리 선택이 어려웠습니다. 이를 개선하기 위해, 본 연구는 불확실성을 고려한 두 가지 모델, EUAV-IP와 IUAV-IP를 제안합니다. EUAV-IP는 불확실한 개념을 마스킹하여 생략하고, IUAV-IP는 불확실성을 쿼리 선택 과정에 통합하여 더 신뢰할 수 있는 결정을 내립니다. 이 방법론은 각 샘플에 맞춘 개념을 선택하여 인간의 개입 없이도 신뢰할 수 있는 결정을 내리며, 전반적인 해석 가능성을 유지합니다. 제안된 IUAV-IP 모델은 5개의 의료 영상 데이터셋 중 4개에서 최첨단 정확도를 달성하며, 더 적은 수의 정보성 높은 개념을 선택하여 간결한 설명을 제공합니다. 이러한 발전은 모델의 신뢰성을 높이고, 의료 분야에서 AI의 안전한 활용을 지원합니다.

## 🎯 주요 포인트

- 1. V-IP는 인간이 이해할 수 있는 개념을 순차적으로 질의하여 예측하는 해석 가능한 AI 프레임워크를 제공합니다.
- 2. 기존 V-IP 방법은 개념 예측에서 샘플별 불확실성을 간과하여 최적이 아닌 질의 선택과 강건성 감소를 초래합니다.
- 3. 본 논문에서는 의료 영상에서 불확실성을 고려한 해석 가능하고 불확실성 인지 프레임워크를 제안합니다.
- 4. EUAV-IP와 IUAV-IP 모델은 V-IP 질의 과정에 불확실성 추정을 통합하여 샘플별로 더 신뢰할 수 있는 개념을 우선시합니다.
- 5. IUAV-IP 모델은 다섯 개의 의료 영상 데이터셋 중 네 개에서 해석 가능한 접근 방식 중 최첨단 정확도를 달성하며, 더 적지만 정보가 풍부한 개념을 선택하여 간결한 설명을 생성합니다.


---

*Generated on 2025-09-24 16:31:19*