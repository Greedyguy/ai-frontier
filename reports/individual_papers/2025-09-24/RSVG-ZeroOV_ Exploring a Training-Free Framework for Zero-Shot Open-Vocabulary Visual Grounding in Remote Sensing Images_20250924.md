<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:00:27.353797",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Zero-Shot Learning",
    "Diffusion Model",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Zero-Shot Learning": 0.8,
    "Diffusion Model": 0.75,
    "Attention Mechanism": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the framework and connect with multimodal learning concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a key aspect of the proposed framework, linking to broader machine learning strategies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Diffusion Model",
        "canonical": "Diffusion Model",
        "aliases": [
          "DM"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion Models are uniquely used in this framework for enhancing object structure information.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention Mechanisms are integral to the model's ability to focus on relevant image regions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.68,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "training-free",
      "framework",
      "segmentation masks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Diffusion Model",
      "resolved_canonical": "Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.68,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# RSVG-ZeroOV: Exploring a Training-Free Framework for Zero-Shot Open-Vocabulary Visual Grounding in Remote Sensing Images

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18711.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18711](https://arxiv.org/abs/2509.18711)

## 🔗 유사한 논문
- [[2025-09-22/Zero-Shot Visual Grounding in 3D Gaussians via View Retrieval_20250922|Zero-Shot Visual Grounding in 3D Gaussians via View Retrieval]] (86.4% similar)
- [[2025-09-24/VLN-Zero_ Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation_20250924|VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation]] (82.6% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (82.4% similar)
- [[2025-09-18/Improving Generalized Visual Grounding with Instance-aware Joint Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (82.3% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Diffusion Model|Diffusion Model]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18711v1 Announce Type: cross 
Abstract: Remote sensing visual grounding (RSVG) aims to localize objects in remote sensing images based on free-form natural language expressions. Existing approaches are typically constrained to closed-set vocabularies, limiting their applicability in open-world scenarios. While recent attempts to leverage generic foundation models for open-vocabulary RSVG, they overly rely on expensive high-quality datasets and time-consuming fine-tuning. To address these limitations, we propose \textbf{RSVG-ZeroOV}, a training-free framework that aims to explore the potential of frozen generic foundation models for zero-shot open-vocabulary RSVG. Specifically, RSVG-ZeroOV comprises three key stages: (i) Overview: We utilize a vision-language model (VLM) to obtain cross-attention\footnote[1]{In this paper, although decoder-only VLMs use self-attention over all tokens, we refer to the image-text interaction part as cross-attention to distinguish it from pure visual self-attention.}maps that capture semantic correlations between text queries and visual regions. (ii) Focus: By leveraging the fine-grained modeling priors of a diffusion model (DM), we fill in gaps in structural and shape information of objects, which are often overlooked by VLM. (iii) Evolve: A simple yet effective attention evolution module is introduced to suppress irrelevant activations, yielding purified segmentation masks over the referred objects. Without cumbersome task-specific training, RSVG-ZeroOV offers an efficient and scalable solution. Extensive experiments demonstrate that the proposed framework consistently outperforms existing weakly-supervised and zero-shot methods.

## 📝 요약

이 논문은 원격 감지 이미지에서 자연어 표현을 기반으로 객체를 찾는 작업인 원격 감지 시각적 그라운딩(RSVG)에 대한 연구입니다. 기존 방법들은 닫힌 집합 어휘에 제한되어 있어 개방형 세계 시나리오에 적용하기 어렵습니다. 이를 해결하기 위해, 이 논문에서는 고가의 데이터셋이나 시간 소모적인 미세 조정 없이도 동작하는 \textbf{RSVG-ZeroOV}라는 훈련이 필요 없는 프레임워크를 제안합니다. 이 프레임워크는 세 가지 주요 단계로 구성됩니다: (i) VLM을 사용하여 텍스트 쿼리와 시각적 영역 간의 의미적 상관관계를 포착하는 교차 주의 맵을 생성, (ii) 확산 모델을 활용하여 객체의 구조적 및 형태 정보를 보완, (iii) 불필요한 활성화를 억제하여 객체의 세분화 마스크를 개선하는 주의 진화 모듈 도입. 제안된 프레임워크는 기존의 약지도 및 제로샷 방법보다 우수한 성능을 보입니다.

## 🎯 주요 포인트

- 1. 원격 감지 시각적 그라운딩(RSVG)은 자연어 표현을 기반으로 원격 감지 이미지 내 객체를 위치 지정하는 것을 목표로 합니다.
- 2. 기존 방법들은 폐쇄형 어휘에 제한되어 있어 개방형 세계 시나리오에서의 적용이 제한적입니다.
- 3. RSVG-ZeroOV는 고가의 데이터셋과 시간 소모적인 미세 조정 없이 동결된 일반 기초 모델을 활용하여 제로샷 개방형 어휘 RSVG를 가능하게 합니다.
- 4. RSVG-ZeroOV는 비전-언어 모델(VLM)과 확산 모델(DM)을 활용하여 텍스트 쿼리와 시각적 영역 간의 의미적 상관관계를 포착하고, 객체의 구조 및 형태 정보를 보완합니다.
- 5. 제안된 프레임워크는 기존의 약지도 및 제로샷 방법을 일관되게 능가하며, 효율적이고 확장 가능한 솔루션을 제공합니다.


---

*Generated on 2025-09-24 14:00:27*