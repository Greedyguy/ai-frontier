<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:14:25.607283",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Adverse Weather Conditions",
    "Convolutional Neural Network",
    "Scene Correspondence Priors"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.8,
    "Adverse Weather Conditions": 0.78,
    "Convolutional Neural Network": 0.7,
    "Scene Correspondence Priors": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised stereo matching",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-supervised stereo",
          "Stereo self-supervision"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the broader concept of self-supervised learning, which is central to the paper's methodology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adverse weather conditions",
        "canonical": "Adverse Weather Conditions",
        "aliases": [
          "Weather degradation",
          "Weather effects"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique challenge addressed by the paper, crucial for understanding the context of the proposed solution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "CNN-based feature extractor",
        "canonical": "Convolutional Neural Network",
        "aliases": [
          "CNN feature extraction"
        ],
        "category": "broad_technical",
        "rationale": "CNNs are fundamental to the feature extraction process discussed in the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Scene correspondence priors",
        "canonical": "Scene Correspondence Priors",
        "aliases": [
          "Scene priors",
          "Correspondence priors"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to improve stereo matching under adverse conditions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
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
      "candidate_surface": "Self-supervised stereo matching",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adverse weather conditions",
      "resolved_canonical": "Adverse Weather Conditions",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CNN-based feature extractor",
      "resolved_canonical": "Convolutional Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Scene correspondence priors",
      "resolved_canonical": "Scene Correspondence Priors",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# RoSe: Robust Self-supervised Stereo Matching under Adverse Weather Conditions

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19165.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19165](https://arxiv.org/abs/2509.19165)

## 🔗 유사한 논문
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (82.2% similar)
- [[2025-09-23/StereoAdapter_ Adapting Stereo Depth Estimation to Underwater Scenes_20250923|StereoAdapter: Adapting Stereo Depth Estimation to Underwater Scenes]] (81.6% similar)
- [[2025-09-18/NDLPNet_ A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset_20250918|NDLPNet: A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset]] (81.0% similar)
- [[2025-09-23/BaseBoostDepth_ Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation_20250923|BaseBoostDepth: Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation]] (81.0% similar)
- [[2025-09-22/RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes_20250922|RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Convolutional Neural Network|Convolutional Neural Network]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Adverse Weather Conditions|Adverse Weather Conditions]], [[keywords/Scene Correspondence Priors|Scene Correspondence Priors]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19165v1 Announce Type: cross 
Abstract: Recent self-supervised stereo matching methods have made significant progress, but their performance significantly degrades under adverse weather conditions such as night, rain, and fog. We identify two primary weaknesses contributing to this performance degradation. First, adverse weather introduces noise and reduces visibility, making CNN-based feature extractors struggle with degraded regions like reflective and textureless areas. Second, these degraded regions can disrupt accurate pixel correspondences, leading to ineffective supervision based on the photometric consistency assumption. To address these challenges, we propose injecting robust priors derived from the visual foundation model into the CNN-based feature extractor to improve feature representation under adverse weather conditions. We then introduce scene correspondence priors to construct robust supervisory signals rather than relying solely on the photometric consistency assumption. Specifically, we create synthetic stereo datasets with realistic weather degradations. These datasets feature clear and adverse image pairs that maintain the same semantic context and disparity, preserving the scene correspondence property. With this knowledge, we propose a robust self-supervised training paradigm, consisting of two key steps: robust self-supervised scene correspondence learning and adverse weather distillation. Both steps aim to align underlying scene results from clean and adverse image pairs, thus improving model disparity estimation under adverse weather effects. Extensive experiments demonstrate the effectiveness and versatility of our proposed solution, which outperforms existing state-of-the-art self-supervised methods. Codes are available at \textcolor{blue}{https://github.com/cocowy1/RoSe-Robust-Self-supervised-Stereo-Matching-under-Adverse-Weather-Conditions}.

## 📝 요약

최근의 자가 지도 학습 기반 스테레오 매칭 방법은 악천후 조건에서 성능이 크게 저하됩니다. 이는 CNN 기반 특징 추출기가 반사 및 무질감 영역에서 어려움을 겪고, 이러한 영역이 정확한 픽셀 대응을 방해하기 때문입니다. 이를 해결하기 위해, 우리는 시각적 기초 모델에서 유래한 강력한 사전 지식을 CNN 기반 특징 추출기에 주입하여 특징 표현을 개선하고, 장면 대응 사전 지식을 도입하여 강력한 지도 신호를 구축합니다. 우리는 현실적인 날씨 악화가 포함된 합성 스테레오 데이터셋을 생성하여 동일한 의미적 맥락과 불일치를 유지하는 깨끗한 이미지와 악천후 이미지를 제공합니다. 이를 통해 강력한 자가 지도 학습 패러다임을 제안하며, 이는 두 가지 주요 단계로 구성됩니다: 강력한 자가 지도 장면 대응 학습과 악천후 증류. 제안된 방법은 기존 최첨단 자가 지도 방법을 능가하는 성능을 보입니다.

## 🎯 주요 포인트

- 1. 최근 자기 지도 학습 기반 스테레오 매칭 방법은 악천후 조건에서 성능이 크게 저하됩니다.
- 2. 악천후는 노이즈를 유발하고 가시성을 감소시켜 CNN 기반 특징 추출기가 반사 및 무纹리 영역에서 어려움을 겪습니다.
- 3. 우리는 시각적 기초 모델에서 파생된 강력한 사전 지식을 CNN 기반 특징 추출기에 주입하여 악천후 조건에서의 특징 표현을 개선합니다.
- 4. 장면 대응 사전 지식을 도입하여 광도 일관성 가정에만 의존하지 않고 강력한 감독 신호를 구축합니다.
- 5. 제안된 방법은 기존 최첨단 자기 지도 학습 방법을 능가하며, 코드가 공개되어 있습니다.


---

*Generated on 2025-09-24 14:14:25*