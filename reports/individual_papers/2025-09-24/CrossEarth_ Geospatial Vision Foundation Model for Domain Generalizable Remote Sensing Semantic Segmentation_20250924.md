<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:26:21.424440",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Remote Sensing Domain Generalization",
    "Semantic Segmentation",
    "Cross-Domain Generalization",
    "Vision Foundation Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Remote Sensing Domain Generalization": 0.8,
    "Semantic Segmentation": 0.85,
    "Cross-Domain Generalization": 0.82,
    "Vision Foundation Model": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Remote Sensing Domain Generalization",
        "canonical": "Remote Sensing Domain Generalization",
        "aliases": [
          "RSDG"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and represents a novel research area in remote sensing.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Semantic Segmentation",
        "canonical": "Semantic Segmentation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Semantic segmentation is a key task in computer vision, relevant for linking with other segmentation models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cross-Domain Generalization",
        "canonical": "Cross-Domain Generalization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding model adaptability across different domains.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Vision Foundation Model",
        "canonical": "Vision Foundation Model",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Foundation models are a growing trend in AI, providing a basis for linking with other foundational AI models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
      "candidate_surface": "Remote Sensing Domain Generalization",
      "resolved_canonical": "Remote Sensing Domain Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Semantic Segmentation",
      "resolved_canonical": "Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cross-Domain Generalization",
      "resolved_canonical": "Cross-Domain Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Vision Foundation Model",
      "resolved_canonical": "Vision Foundation Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# CrossEarth: Geospatial Vision Foundation Model for Domain Generalizable Remote Sensing Semantic Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2410.22629.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2410.22629](https://arxiv.org/abs/2410.22629)

## 🔗 유사한 논문
- [[2025-09-23/Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training_20250923|Enhancing Semantic Segmentation with Continual Self-Supervised Pre-training]] (83.8% similar)
- [[2025-09-24/RS3DBench_ A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing_20250924|RS3DBench: A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing]] (83.4% similar)
- [[2025-09-23/Remote Sensing-Oriented World Model_20250923|Remote Sensing-Oriented World Model]] (83.4% similar)
- [[2025-09-23/EarthGPT-X_ A Spatial MLLM for Multi-level Multi-Source Remote Sensing Imagery Understanding with Visual Prompting_20250923|EarthGPT-X: A Spatial MLLM for Multi-level Multi-Source Remote Sensing Imagery Understanding with Visual Prompting]] (82.7% similar)
- [[2025-09-23/Prototype-Based Pseudo-Label Denoising for Source-Free Domain Adaptation in Remote Sensing Semantic Segmentation_20250923|Prototype-Based Pseudo-Label Denoising for Source-Free Domain Adaptation in Remote Sensing Semantic Segmentation]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic Segmentation|Semantic Segmentation]], [[keywords/Cross-Domain Generalization|Cross-Domain Generalization]]
**⚡ Unique Technical**: [[keywords/Remote Sensing Domain Generalization|Remote Sensing Domain Generalization]]
**🚀 Evolved Concepts**: [[keywords/Vision Foundation Model|Vision Foundation Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.22629v3 Announce Type: replace 
Abstract: The field of Remote Sensing Domain Generalization (RSDG) has emerged as a critical and valuable research frontier, focusing on developing models that generalize effectively across diverse scenarios. Despite the substantial domain gaps in RS images that are characterized by variabilities such as location, wavelength, and sensor type, research in this area remains underexplored: (1) Current cross-domain methods primarily focus on Domain Adaptation (DA), which adapts models to predefined domains rather than to unseen ones; (2) Few studies targeting the RSDG issue, especially for semantic segmentation tasks, where existing models are developed for specific unknown domains, struggling with issues of underfitting on other unknown scenarios; (3) Existing RS foundation models tend to prioritize in-domain performance over cross-domain generalization. To this end, we introduce the first vision foundation model for RSDG semantic segmentation, CrossEarth. CrossEarth demonstrates strong cross-domain generalization through a specially designed data-level Earth-Style Injection pipeline and a model-level Multi-Task Training pipeline. In addition, for the semantic segmentation task, we have curated an RSDG benchmark comprising 32 cross-domain settings across various regions, spectral bands, platforms, and climates, providing a comprehensive framework for testing the generalizability of future RSDG models. Extensive experiments on this benchmark demonstrate the superiority of CrossEarth over existing state-of-the-art methods.

## 📝 요약

원격 감지 도메인 일반화(RSDG)는 다양한 시나리오에서 효과적으로 일반화할 수 있는 모델 개발을 목표로 하는 중요한 연구 분야입니다. 현재의 연구는 주로 도메인 적응(DA)에 초점을 맞추고 있으며, 이는 미리 정의된 도메인에 모델을 적응시키는 데 중점을 둡니다. 그러나 이는 보지 못한 도메인에 대한 일반화에는 한계가 있습니다. 특히 의미론적 분할 작업에서 기존 모델은 특정 도메인에 맞춰져 있어 다른 도메인에서는 성능 저하가 발생합니다. 이러한 문제를 해결하기 위해, 우리는 RSDG 의미론적 분할을 위한 최초의 비전 기초 모델인 CrossEarth를 소개합니다. CrossEarth는 데이터 수준의 Earth-Style Injection 파이프라인과 모델 수준의 Multi-Task Training 파이프라인을 통해 강력한 도메인 일반화를 보여줍니다. 또한, 다양한 지역, 스펙트럼 대역, 플랫폼, 기후를 아우르는 32개의 교차 도메인 설정을 포함한 RSDG 벤치마크를 구축하여 미래의 RSDG 모델의 일반화 가능성을 테스트할 수 있는 포괄적인 프레임워크를 제공합니다. 이 벤치마크에 대한 광범위한 실험 결과, CrossEarth가 기존 최첨단 방법들보다 우수한 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. 원격 감지 도메인 일반화(RSDG)는 다양한 시나리오에서 효과적으로 일반화할 수 있는 모델 개발을 목표로 하는 중요한 연구 분야로 부상했습니다.
- 2. 기존의 교차 도메인 방법은 주로 사전 정의된 도메인에 적응하는 도메인 적응(DA)에 초점을 맞추고 있으며, 미지의 도메인에 대한 일반화는 부족합니다.
- 3. RSDG 문제를 다루는 연구는 특히 의미론적 분할 작업에서 부족하며, 기존 모델은 특정 미지의 도메인에 맞춰 개발되어 다른 미지의 시나리오에서는 부적합 문제가 발생합니다.
- 4. CrossEarth는 데이터 수준의 Earth-Style Injection 파이프라인과 모델 수준의 Multi-Task Training 파이프라인을 통해 강력한 교차 도메인 일반화를 보여줍니다.
- 5. 32개의 교차 도메인 설정을 포함하는 RSDG 벤치마크를 구축하여 미래의 RSDG 모델의 일반화 가능성을 테스트할 수 있는 포괄적인 프레임워크를 제공합니다.


---

*Generated on 2025-09-24 16:26:21*