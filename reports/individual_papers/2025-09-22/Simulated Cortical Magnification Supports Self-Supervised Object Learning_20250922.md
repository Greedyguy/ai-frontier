---
keywords:
  - Self-supervised Learning
  - Cortical Magnification
  - Foveated Vision
  - Egocentric Videos
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15751
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:08:27.145205",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Cortical Magnification",
    "Foveated Vision",
    "Egocentric Videos"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Cortical Magnification": 0.7,
    "Foveated Vision": 0.72,
    "Egocentric Videos": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key concept in the paper and connects well with existing research on learning models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cortical Magnification",
        "canonical": "Cortical Magnification",
        "aliases": [
          "Cortical Scaling"
        ],
        "category": "unique_technical",
        "rationale": "A unique concept central to the paper's approach, offering a novel perspective on visual processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Foveated Vision",
        "canonical": "Foveated Vision",
        "aliases": [
          "Foveal Vision"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the paper's methodology and its impact on object representation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Egocentric Videos",
        "canonical": "Egocentric Videos",
        "aliases": [
          "First-person Videos"
        ],
        "category": "unique_technical",
        "rationale": "The use of egocentric videos is a distinctive aspect of the study, relevant for linking with human visual experience research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "visual experience",
      "object representations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cortical Magnification",
      "resolved_canonical": "Cortical Magnification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Foveated Vision",
      "resolved_canonical": "Foveated Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Egocentric Videos",
      "resolved_canonical": "Egocentric Videos",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Simulated Cortical Magnification Supports Self-Supervised Object Learning

**Korean Title:** 시뮬레이션된 피질 확대는 자가 지도 객체 학습을 지원합니다.

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15751.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15751](https://arxiv.org/abs/2509.15751)

## 🔗 유사한 논문
- [[2025-09-22/Modeling the Human Visual System_ Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms_20250922|Modeling the Human Visual System: Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms]] (84.1% similar)
- [[2025-09-22/Large Vision Models Can Solve Mental Rotation Problems_20250922|Large Vision Models Can Solve Mental Rotation Problems]] (83.7% similar)
- [[2025-09-19/Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (81.7% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (81.3% similar)
- [[2025-09-22/Saccadic Vision for Fine-Grained Visual Classification_20250922|Saccadic Vision for Fine-Grained Visual Classification]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Cortical Magnification|Cortical Magnification]], [[keywords/Foveated Vision|Foveated Vision]], [[keywords/Egocentric Videos|Egocentric Videos]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15751v1 Announce Type: new 
Abstract: Recent self-supervised learning models simulate the development of semantic object representations by training on visual experience similar to that of toddlers. However, these models ignore the foveated nature of human vision with high/low resolution in the center/periphery of the visual field. Here, we investigate the role of this varying resolution in the development of object representations. We leverage two datasets of egocentric videos that capture the visual experience of humans during interactions with objects. We apply models of human foveation and cortical magnification to modify these inputs, such that the visual content becomes less distinct towards the periphery. The resulting sequences are used to train two bio-inspired self-supervised learning models that implement a time-based learning objective. Our results show that modeling aspects of foveated vision improves the quality of the learned object representations in this setting. Our analysis suggests that this improvement comes from making objects appear bigger and inducing a better trade-off between central and peripheral visual information. Overall, this work takes a step towards making models of humans' learning of visual representations more realistic and performant.

## 🔍 Abstract (한글 번역)

arXiv:2509.15751v1 발표 유형: 신규  
초록: 최근의 자기 지도 학습 모델은 유아와 유사한 시각적 경험을 통해 의미론적 객체 표현의 개발을 시뮬레이션합니다. 그러나 이러한 모델은 인간 시각의 중심/주변 시야에서 고해상도/저해상도의 중심화된 특성을 무시합니다. 본 연구에서는 객체 표현의 개발에서 이러한 해상도 변화의 역할을 조사합니다. 우리는 객체와의 상호작용 중 인간의 시각적 경험을 포착한 두 개의 자아중심적 비디오 데이터셋을 활용합니다. 우리는 인간의 중심화 및 피질 확대 모델을 적용하여 이러한 입력을 수정하여 시각적 콘텐츠가 주변부로 갈수록 덜 명확해지도록 합니다. 결과적으로 생성된 시퀀스는 시간 기반 학습 목표를 구현하는 두 개의 생체 영감 자기 지도 학습 모델을 훈련하는 데 사용됩니다. 우리의 결과는 중심화된 시각의 측면을 모델링하는 것이 이 설정에서 학습된 객체 표현의 품질을 향상시킨다는 것을 보여줍니다. 우리의 분석은 이러한 개선이 객체를 더 크게 보이게 하고 중심 및 주변 시각 정보 간의 더 나은 균형을 유도함으로써 이루어진다고 제안합니다. 전반적으로, 이 연구는 인간의 시각적 표현 학습 모델을 보다 현실적이고 성능이 뛰어나게 만드는 방향으로 한 걸음 나아갑니다.

## 📝 요약

최근의 자가 지도 학습 모델은 유아의 시각적 경험을 모방하여 객체 표현을 학습하지만, 인간 시각의 중심부와 주변부의 해상도 차이를 무시합니다. 본 연구는 이러한 해상도 차이가 객체 표현 발달에 미치는 영향을 조사합니다. 인간의 물체 상호작용을 담은 두 가지 시점 비디오 데이터를 활용하여, 인간의 중심 시각과 피질 확대 모델을 적용해 주변부 시각 정보를 덜 명확하게 수정했습니다. 이를 통해 시간 기반 학습 목표를 구현한 생체 모방 자가 지도 학습 모델을 훈련했습니다. 결과적으로, 중심 시각 모델링이 객체 표현의 질을 향상시킴을 확인했으며, 이는 객체를 더 크게 보이게 하고 중심 및 주변 시각 정보 간의 균형을 개선한 데 기인합니다. 본 연구는 인간의 시각 표현 학습 모델을 더욱 현실적이고 성능 좋게 만드는 데 기여합니다.

## 🎯 주요 포인트

- 1. 최근의 자기 지도 학습 모델은 유아와 유사한 시각적 경험을 통해 의미 있는 객체 표현을 개발하지만, 인간 시각의 중심/주변부 해상도 차이를 무시한다.
- 2. 본 연구는 인간의 시각 경험을 포착한 두 가지 자아 중심 비디오 데이터셋을 활용하여 객체 표현 개발에서 해상도 변화의 역할을 조사한다.
- 3. 인간의 중심 시각과 대뇌 확대 모델을 적용하여 입력 데이터를 수정하고, 주변부로 갈수록 시각적 콘텐츠가 덜 명확해지도록 한다.
- 4. 이러한 수정된 시퀀스를 사용하여 시간 기반 학습 목표를 구현한 생체 영감을 받은 두 가지 자기 지도 학습 모델을 훈련한다.
- 5. 연구 결과, 중심 시각의 측면을 모델링하면 학습된 객체 표현의 품질이 향상되며, 이는 객체를 더 크게 보이게 하고 중심 및 주변부 정보 간의 균형을 개선하는 데 기인한다.


---

*Generated on 2025-09-23 12:08:27*