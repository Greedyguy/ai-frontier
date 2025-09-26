<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:03:09.566746",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Geometric Visual Illusions",
    "Perceptual Inductive Biases",
    "Convolutional Neural Network",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Geometric Visual Illusions": 0.78,
    "Perceptual Inductive Biases": 0.77,
    "Convolutional Neural Network": 0.8,
    "Transformer": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "geometric visual illusions",
        "canonical": "Geometric Visual Illusions",
        "aliases": [
          "visual illusions",
          "geometric illusions"
        ],
        "category": "unique_technical",
        "rationale": "Integrating geometric visual illusions as perceptual biases is a novel approach in vision models, offering unique insights.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "perceptual inductive biases",
        "canonical": "Perceptual Inductive Biases",
        "aliases": [
          "inductive biases",
          "perceptual biases"
        ],
        "category": "unique_technical",
        "rationale": "Perceptual inductive biases are crucial for linking perceptual psychology with machine learning models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "CNN",
        "canonical": "Convolutional Neural Network",
        "aliases": [
          "CNN",
          "ConvNet"
        ],
        "category": "broad_technical",
        "rationale": "CNNs are a fundamental architecture in deep learning, relevant for understanding the integration of perceptual biases.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "transformer-based architectures",
        "canonical": "Transformer",
        "aliases": [
          "transformer architectures"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a key architecture in modern vision models, relevant for exploring perceptual biases.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "image classification",
      "structured insights",
      "training pipelines"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "geometric visual illusions",
      "resolved_canonical": "Geometric Visual Illusions",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "perceptual inductive biases",
      "resolved_canonical": "Perceptual Inductive Biases",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "CNN",
      "resolved_canonical": "Convolutional Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "transformer-based architectures",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15156.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.15156](https://arxiv.org/abs/2509.15156)

## 🔗 유사한 논문
- [[2025-09-22/Large Vision Models Can Solve Mental Rotation Problems_20250922|Large Vision Models Can Solve Mental Rotation Problems]] (82.2% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (82.0% similar)
- [[2025-09-22/Simulated Cortical Magnification Supports Self-Supervised Object Learning_20250922|Simulated Cortical Magnification Supports Self-Supervised Object Learning]] (81.7% similar)
- [[2025-09-22/Modeling the Human Visual System_ Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms_20250922|Modeling the Human Visual System: Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms]] (81.7% similar)
- [[2025-09-23/Look, Focus, Act_ Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers_20250923|Look, Focus, Act: Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Convolutional Neural Network|Convolutional Neural Network]], [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Geometric Visual Illusions|Geometric Visual Illusions]], [[keywords/Perceptual Inductive Biases|Perceptual Inductive Biases]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15156v1 Announce Type: cross 
Abstract: Contemporary deep learning models have achieved impressive performance in image classification by primarily leveraging statistical regularities within large datasets, but they rarely incorporate structured insights drawn directly from perceptual psychology. To explore the potential of perceptually motivated inductive biases, we propose integrating classic geometric visual illusions well-studied phenomena from human perception into standard image-classification training pipelines. Specifically, we introduce a synthetic, parametric geometric-illusion dataset and evaluate three multi-source learning strategies that combine illusion recognition tasks with ImageNet classification objectives. Our experiments reveal two key conceptual insights: (i) incorporating geometric illusions as auxiliary supervision systematically improves generalization, especially in visually challenging cases involving intricate contours and fine textures; and (ii) perceptually driven inductive biases, even when derived from synthetic stimuli traditionally considered unrelated to natural image recognition, can enhance the structural sensitivity of both CNN and transformer-based architectures. These results demonstrate a novel integration of perceptual science and machine learning and suggest new directions for embedding perceptual priors into vision model design.

## 📝 요약

현대의 딥러닝 모델은 대규모 데이터셋의 통계적 규칙성을 활용하여 이미지 분류에서 뛰어난 성능을 보이지만, 지각 심리학에서 직접 도출된 구조적 통찰을 거의 반영하지 않습니다. 본 연구는 지각적으로 동기화된 귀납적 편향의 잠재력을 탐구하기 위해, 인간 지각에서 잘 연구된 고전적 기하학적 시각 착각을 이미지 분류 훈련 과정에 통합하는 방법을 제안합니다. 이를 위해 합성된 매개변수적 기하학적 착각 데이터셋을 도입하고, 착각 인식 과제를 ImageNet 분류 목표와 결합하는 세 가지 다중 소스 학습 전략을 평가했습니다. 실험 결과, 기하학적 착각을 보조 감독으로 포함하면 일반화가 체계적으로 개선되며, 특히 복잡한 윤곽과 세밀한 질감을 포함한 시각적으로 어려운 사례에서 효과적임을 발견했습니다. 또한, 합성 자극에서 유래한 지각적 귀납적 편향이 자연 이미지 인식과 관련이 없다고 여겨지더라도, CNN 및 트랜스포머 기반 아키텍처의 구조적 민감성을 향상시킬 수 있음을 보여주었습니다. 이러한 결과는 지각 과학과 기계 학습의 새로운 통합을 증명하며, 시각 모델 설계에 지각적 우선순위를 내재화하는 새로운 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 현대의 딥러닝 모델은 주로 대규모 데이터셋의 통계적 규칙성을 활용하여 이미지 분류에서 뛰어난 성능을 보이지만, 지각 심리학에서 직접적으로 도출된 구조적 통찰을 거의 포함하지 않는다.
- 2. 우리는 인간 지각에서 잘 연구된 고전적인 기하학적 시각 착시를 이미지 분류 훈련 파이프라인에 통합하여 지각적으로 동기화된 귀납적 편향의 잠재력을 탐구한다.
- 3. 기하학적 착시를 보조 감독으로 포함하면 복잡한 윤곽과 섬세한 질감을 포함한 시각적으로 도전적인 사례에서 일반화가 체계적으로 개선된다.
- 4. 합성 자극에서 파생된 지각적으로 유도된 귀납적 편향은 자연 이미지 인식과 전통적으로 관련이 없다고 여겨지더라도 CNN 및 트랜스포머 기반 아키텍처의 구조적 민감성을 향상시킬 수 있다.
- 5. 이 연구는 지각 과학과 기계 학습의 새로운 통합을 보여주며, 시각 모델 설계에 지각적 우선순위를 내재화하는 새로운 방향을 제시한다.


---

*Generated on 2025-09-24 15:03:09*