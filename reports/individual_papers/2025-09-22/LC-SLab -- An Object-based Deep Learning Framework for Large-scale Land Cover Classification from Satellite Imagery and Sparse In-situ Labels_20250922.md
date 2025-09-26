---
keywords:
  - Deep Learning
  - Graph Neural Network
  - Object-based Classification
  - Semantic Segmentation
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15868
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:12:20.966618",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Graph Neural Network",
    "Object-based Classification",
    "Semantic Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Graph Neural Network": 0.78,
    "Object-based Classification": 0.7,
    "Semantic Segmentation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental technique used in the proposed framework, linking it to a wide range of related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are specifically mentioned for input-level aggregation, indicating a strong technical connection.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Object-based Classification",
        "canonical": "Object-based Classification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This approach is central to the paper's novelty in land cover classification, providing a unique technical angle.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Semantic Segmentation",
        "canonical": "Semantic Segmentation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Semantic Segmentation is a key process in the framework's output-level aggregation, linking to computer vision research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "large-scale",
      "performance",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Object-based Classification",
      "resolved_canonical": "Object-based Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Semantic Segmentation",
      "resolved_canonical": "Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# LC-SLab -- An Object-based Deep Learning Framework for Large-scale Land Cover Classification from Satellite Imagery and Sparse In-situ Labels

**Korean Title:** LC-SLab -- 위성 이미지와 희소한 현장 라벨을 활용한 대규모 토지 피복 분류를 위한 객체 기반 딥러닝 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15868.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15868](https://arxiv.org/abs/2509.15868)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (83.4% similar)
- [[2025-09-22/Latent Zoning Network_ A Unified Principle for Generative Modeling, Representation Learning, and Classification_20250922|Latent Zoning Network: A Unified Principle for Generative Modeling, Representation Learning, and Classification]] (81.3% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (80.6% similar)
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (80.5% similar)
- [[2025-09-18/Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Semantic Segmentation|Semantic Segmentation]]
**⚡ Unique Technical**: [[keywords/Object-based Classification|Object-based Classification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15868v1 Announce Type: new 
Abstract: Large-scale land cover maps generated using deep learning play a critical role across a wide range of Earth science applications. Open in-situ datasets from principled land cover surveys offer a scalable alternative to manual annotation for training such models. However, their sparse spatial coverage often leads to fragmented and noisy predictions when used with existing deep learning-based land cover mapping approaches. A promising direction to address this issue is object-based classification, which assigns labels to semantically coherent image regions rather than individual pixels, thereby imposing a minimum mapping unit. Despite this potential, object-based methods remain underexplored in deep learning-based land cover mapping pipelines, especially in the context of medium-resolution imagery and sparse supervision. To address this gap, we propose LC-SLab, the first deep learning framework for systematically exploring object-based deep learning methods for large-scale land cover classification under sparse supervision. LC-SLab supports both input-level aggregation via graph neural networks, and output-level aggregation by postprocessing results from established semantic segmentation models. Additionally, we incorporate features from a large pre-trained network to improve performance on small datasets. We evaluate the framework on annual Sentinel-2 composites with sparse LUCAS labels, focusing on the tradeoff between accuracy and fragmentation, as well as sensitivity to dataset size. Our results show that object-based methods can match or exceed the accuracy of common pixel-wise models while producing substantially more coherent maps. Input-level aggregation proves more robust on smaller datasets, whereas output-level aggregation performs best with more data. Several configurations of LC-SLab also outperform existing land cover products, highlighting the framework's practical utility.

## 🔍 Abstract (한글 번역)

arXiv:2509.15868v1 발표 유형: 신규  
초록: 심층 학습을 사용하여 생성된 대규모 토지 피복 지도는 다양한 지구 과학 응용 분야에서 중요한 역할을 합니다. 체계적인 토지 피복 조사를 통해 얻은 공개 현장 데이터 세트는 이러한 모델을 훈련하기 위한 수작업 주석의 확장 가능한 대안을 제공합니다. 그러나 공간적 범위가 드문 경우가 많아 기존의 심층 학습 기반 토지 피복 매핑 접근 방식과 함께 사용할 때 단편적이고 노이즈가 많은 예측을 초래할 수 있습니다. 이 문제를 해결하기 위한 유망한 방향은 개체 기반 분류로, 개별 픽셀이 아닌 의미론적으로 일관된 이미지 영역에 레이블을 할당하여 최소 매핑 단위를 부여하는 것입니다. 이러한 잠재력에도 불구하고 개체 기반 방법은 특히 중간 해상도 이미지와 희소 감독의 맥락에서 심층 학습 기반 토지 피복 매핑 파이프라인에서 충분히 탐구되지 않았습니다. 이러한 격차를 해결하기 위해 우리는 희소 감독 하에 대규모 토지 피복 분류를 위한 개체 기반 심층 학습 방법을 체계적으로 탐구하기 위한 최초의 심층 학습 프레임워크인 LC-SLab을 제안합니다. LC-SLab은 그래프 신경망을 통한 입력 수준 집계와 기존의 의미론적 분할 모델에서 나온 결과를 후처리하여 출력 수준 집계를 모두 지원합니다. 또한, 대규모 사전 학습 네트워크의 기능을 통합하여 작은 데이터 세트에서 성능을 향상시킵니다. 우리는 희소한 LUCAS 레이블이 있는 연간 Sentinel-2 합성물을 대상으로 정확도와 단편화 간의 균형, 데이터 세트 크기에 대한 민감성을 중점적으로 프레임워크를 평가합니다. 우리의 결과는 개체 기반 방법이 일반적인 픽셀 단위 모델의 정확도를 맞추거나 초과할 수 있으며 훨씬 더 일관된 지도를 생성할 수 있음을 보여줍니다. 입력 수준 집계는 더 작은 데이터 세트에서 더 견고한 반면, 출력 수준 집계는 더 많은 데이터에서 최고의 성능을 발휘합니다. LC-SLab의 여러 구성은 기존의 토지 피복 제품보다 뛰어난 성능을 발휘하여 프레임워크의 실용성을 강조합니다.

## 📝 요약

이 논문은 대규모 토지 피복 지도를 생성하는 데 있어 객체 기반 분류의 중요성을 강조합니다. 기존의 딥러닝 기반 방법은 희소한 공간 커버리지로 인해 단편적이고 노이즈가 많은 예측을 초래할 수 있습니다. 이를 해결하기 위해, 저자들은 LC-SLab이라는 프레임워크를 제안하여 객체 기반 딥러닝 방법을 체계적으로 탐구합니다. 이 프레임워크는 그래프 신경망을 통한 입력 수준의 집계와 기존 의미론적 분할 모델의 결과를 후처리하는 출력 수준의 집계를 지원합니다. 또한, 대규모 사전 학습된 네트워크의 특징을 활용하여 작은 데이터셋에서도 성능을 향상시킵니다. 실험 결과, 객체 기반 방법이 일반적인 픽셀 기반 모델의 정확도를 능가하거나 동등한 수준을 유지하면서도 더 일관된 지도를 생성할 수 있음을 보여줍니다. 입력 수준의 집계는 작은 데이터셋에서 더 강력하며, 출력 수준의 집계는 더 많은 데이터와 함께 최상의 성능을 발휘합니다. LC-SLab의 여러 구성은 기존의 토지 피복 제품을 능가하여 실용성을 입증합니다.

## 🎯 주요 포인트

- 1. 대규모 토지 피복 지도는 딥러닝을 통해 생성되며, 이는 지구 과학 응용 분야에서 중요한 역할을 한다.
- 2. 객체 기반 분류는 개별 픽셀이 아닌 의미적으로 일관된 이미지 영역에 레이블을 할당하여 단편화된 예측 문제를 해결할 수 있다.
- 3. LC-SLab은 희소한 감독 하에서 대규모 토지 피복 분류를 위한 객체 기반 딥러닝 방법을 체계적으로 탐구하는 최초의 프레임워크이다.
- 4. LC-SLab은 그래프 신경망을 통한 입력 수준 집계와 기존 의미론적 분할 모델의 결과를 후처리하는 출력 수준 집계를 지원한다.
- 5. 객체 기반 방법은 일반적인 픽셀 기반 모델과 비교하여 더 일관된 지도를 생성하며, LC-SLab의 여러 구성은 기존 토지 피복 제품보다 우수한 성능을 보인다.


---

*Generated on 2025-09-23 12:12:20*