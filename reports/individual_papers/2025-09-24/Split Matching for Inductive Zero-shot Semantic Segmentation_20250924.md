<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:28:57.162406",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Vision-Language Model",
    "Split Matching",
    "Hungarian Algorithm",
    "Multi-scale Feature Enhancement"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.9,
    "Vision-Language Model": 0.85,
    "Split Matching": 0.8,
    "Hungarian Algorithm": 0.75,
    "Multi-scale Feature Enhancement": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-shot Semantic Segmentation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "ZSS"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot learning is a trending concept and directly related to the paper's focus on segmenting unseen categories.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language",
          "VL Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are central to the paper's methodology and are a rapidly evolving area of research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.85
      },
      {
        "surface": "Split Matching",
        "canonical": "Split Matching",
        "aliases": [
          "SM"
        ],
        "category": "unique_technical",
        "rationale": "Split Matching is a novel strategy introduced in the paper, crucial for understanding its contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Hungarian Matching",
        "canonical": "Hungarian Algorithm",
        "aliases": [
          "Hungarian Matching"
        ],
        "category": "specific_connectable",
        "rationale": "The Hungarian Algorithm is a foundational method in the paper's approach, relevant for linking to optimization techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Multi-scale Feature Enhancement",
        "canonical": "Multi-scale Feature Enhancement",
        "aliases": [
          "MFE"
        ],
        "category": "unique_technical",
        "rationale": "This module is a unique contribution of the paper, enhancing feature extraction across scales.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "query-based segmentation",
      "pseudo masks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-shot Semantic Segmentation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Split Matching",
      "resolved_canonical": "Split Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Hungarian Matching",
      "resolved_canonical": "Hungarian Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Multi-scale Feature Enhancement",
      "resolved_canonical": "Multi-scale Feature Enhancement",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Split Matching for Inductive Zero-shot Semantic Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.05023.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2505.05023](https://arxiv.org/abs/2505.05023)

## 🔗 유사한 논문
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut: Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (82.3% similar)
- [[2025-09-22/TISDiSS_ A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation_20250922|TISDiSS: A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation]] (81.1% similar)
- [[2025-09-23/Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge_20250923|Ambiguous Medical Image Segmentation Using Diffusion Schr\"{o}dinger Bridge]] (80.9% similar)
- [[2025-09-24/A Single Image Is All You Need_ Zero-Shot Anomaly Localization Without Training Data_20250924|A Single Image Is All You Need: Zero-Shot Anomaly Localization Without Training Data]] (80.9% similar)
- [[2025-09-24/No Labels Needed_ Zero-Shot Image Classification with Collaborative Self-Learning_20250924|No Labels Needed: Zero-Shot Image Classification with Collaborative Self-Learning]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Hungarian Algorithm|Hungarian Algorithm]]
**⚡ Unique Technical**: [[keywords/Split Matching|Split Matching]], [[keywords/Multi-scale Feature Enhancement|Multi-scale Feature Enhancement]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.05023v3 Announce Type: replace 
Abstract: Zero-shot Semantic Segmentation (ZSS) aims to segment categories that are not annotated during training. While fine-tuning vision-language models has achieved promising results, these models often overfit to seen categories due to the lack of supervision for unseen classes. As an alternative to fully supervised approaches, query-based segmentation has shown great latent in ZSS, as it enables object localization without relying on explicit labels. However, conventional Hungarian matching, a core component in query-based frameworks, needs full supervision and often misclassifies unseen categories as background in the setting of ZSS. To address this issue, we propose Split Matching (SM), a novel assignment strategy that decouples Hungarian matching into two components: one for seen classes in annotated regions and another for latent classes in unannotated regions (referred to as unseen candidates). Specifically, we partition the queries into seen and candidate groups, enabling each to be optimized independently according to its available supervision. To discover unseen candidates, we cluster CLIP dense features to generate pseudo masks and extract region-level embeddings using CLS tokens. Matching is then conducted separately for the two groups based on both class-level similarity and mask-level consistency. Additionally, we introduce a Multi-scale Feature Enhancement (MFE) module that refines decoder features through residual multi-scale aggregation, improving the model's ability to capture spatial details across resolutions. SM is the first to introduce decoupled Hungarian matching under the inductive ZSS setting, and achieves state-of-the-art performance on two standard benchmarks.

## 📝 요약

제로샷 의미론적 분할(ZSS)은 학습 중 주석되지 않은 카테고리를 분할하는 것을 목표로 합니다. 기존의 비전-언어 모델은 유망한 결과를 보였으나, 미지의 클래스에 대한 감독 부족으로 인해 학습된 카테고리에 과적합되는 문제가 있습니다. 이를 해결하기 위해, 우리는 헝가리안 매칭을 두 부분으로 분리한 새로운 할당 전략인 Split Matching(SM)을 제안합니다. 이는 주석된 영역의 학습된 클래스와 주석되지 않은 영역의 잠재 클래스(미지 후보)를 각각 독립적으로 최적화합니다. 또한, CLIP 밀집 특징을 클러스터링하여 가짜 마스크를 생성하고, CLS 토큰을 사용해 영역 수준의 임베딩을 추출합니다. 두 그룹에 대해 클래스 수준의 유사성과 마스크 수준의 일관성을 기반으로 매칭을 수행합니다. 추가로, 다중 스케일 특징 강화(MFE) 모듈을 도입하여 디코더 특징을 개선하고, 공간 세부 사항을 더 잘 포착할 수 있도록 합니다. SM은 유도적 ZSS 설정에서 분리된 헝가리안 매칭을 처음으로 도입하여, 두 가지 표준 벤치마크에서 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. Zero-shot Semantic Segmentation(ZSS)는 학습 중 주석되지 않은 카테고리를 분할하는 것을 목표로 합니다.
- 2. 기존의 헝가리안 매칭은 완전한 감독이 필요하며, ZSS 설정에서 보이지 않는 카테고리를 배경으로 잘못 분류하는 경향이 있습니다.
- 3. Split Matching(SM)은 헝가리안 매칭을 보이는 클래스와 잠재 클래스에 대해 각각 독립적으로 최적화할 수 있도록 분리하는 새로운 할당 전략입니다.
- 4. Multi-scale Feature Enhancement(MFE) 모듈은 잔여 다중 스케일 집계를 통해 디코더 기능을 개선하여 공간 세부 사항을 포착하는 모델의 능력을 향상시킵니다.
- 5. SM은 유도 ZSS 설정에서 분리된 헝가리안 매칭을 도입한 최초의 방법으로, 두 가지 표준 벤치마크에서 최첨단 성능을 달성합니다.


---

*Generated on 2025-09-24 16:28:57*