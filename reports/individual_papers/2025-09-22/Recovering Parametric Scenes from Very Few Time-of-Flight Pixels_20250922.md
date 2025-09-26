---
keywords:
  - 3D Parametric Scenes
  - Time-of-Flight Sensors
  - Differentiable Rendering
  - Analysis-by-Synthesis Framework
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16132
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:21:44.049349",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Parametric Scenes",
    "Time-of-Flight Sensors",
    "Differentiable Rendering",
    "Analysis-by-Synthesis Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Parametric Scenes": 0.78,
    "Time-of-Flight Sensors": 0.77,
    "Differentiable Rendering": 0.8,
    "Analysis-by-Synthesis Framework": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D parametric scenes",
        "canonical": "3D Parametric Scenes",
        "aliases": [
          "parametric 3D scenes"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on geometry recovery and is specific to the domain of 3D modeling.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "time-of-flight sensors",
        "canonical": "Time-of-Flight Sensors",
        "aliases": [
          "ToF sensors"
        ],
        "category": "unique_technical",
        "rationale": "Time-of-flight sensors are crucial to the methodology discussed, providing the sparse data for scene recovery.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "differentiable rendering",
        "canonical": "Differentiable Rendering",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Differentiable rendering is a key technique used in the paper's analysis-by-synthesis framework.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "analysis-by-synthesis framework",
        "canonical": "Analysis-by-Synthesis Framework",
        "aliases": [
          "analysis by synthesis"
        ],
        "category": "unique_technical",
        "rationale": "This framework is central to the paper's approach and is a specific method in computational imaging.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "geometry",
      "method",
      "experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D parametric scenes",
      "resolved_canonical": "3D Parametric Scenes",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "time-of-flight sensors",
      "resolved_canonical": "Time-of-Flight Sensors",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "differentiable rendering",
      "resolved_canonical": "Differentiable Rendering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "analysis-by-synthesis framework",
      "resolved_canonical": "Analysis-by-Synthesis Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Recovering Parametric Scenes from Very Few Time-of-Flight Pixels

**Korean Title:** 아주 적은 수의 비행 시간 픽셀로부터 파라메트릭 장면 복원하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16132.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16132](https://arxiv.org/abs/2509.16132)

## 🔗 유사한 논문
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (83.2% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (82.5% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (82.3% similar)
- [[2025-09-22/Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors_20250922|Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors]] (81.9% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Differentiable Rendering|Differentiable Rendering]]
**⚡ Unique Technical**: [[keywords/3D Parametric Scenes|3D Parametric Scenes]], [[keywords/Time-of-Flight Sensors|Time-of-Flight Sensors]], [[keywords/Analysis-by-Synthesis Framework|Analysis-by-Synthesis Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16132v1 Announce Type: new 
Abstract: We aim to recover the geometry of 3D parametric scenes using very few depth measurements from low-cost, commercially available time-of-flight sensors. These sensors offer very low spatial resolution (i.e., a single pixel), but image a wide field-of-view per pixel and capture detailed time-of-flight data in the form of time-resolved photon counts. This time-of-flight data encodes rich scene information and thus enables recovery of simple scenes from sparse measurements. We investigate the feasibility of using a distributed set of few measurements (e.g., as few as 15 pixels) to recover the geometry of simple parametric scenes with a strong prior, such as estimating the 6D pose of a known object. To achieve this, we design a method that utilizes both feed-forward prediction to infer scene parameters, and differentiable rendering within an analysis-by-synthesis framework to refine the scene parameter estimate. We develop hardware prototypes and demonstrate that our method effectively recovers object pose given an untextured 3D model in both simulations and controlled real-world captures, and show promising initial results for other parametric scenes. We additionally conduct experiments to explore the limits and capabilities of our imaging solution.

## 🔍 Abstract (한글 번역)

arXiv:2509.16132v1 발표 유형: 신규  
초록: 우리는 저비용의 상업적으로 이용 가능한 비행시간 센서를 사용하여 매우 적은 수의 깊이 측정을 통해 3D 매개변수 장면의 기하학을 복원하는 것을 목표로 합니다. 이러한 센서는 매우 낮은 공간 해상도(즉, 단일 픽셀)를 제공하지만, 픽셀당 넓은 시야를 이미지화하고 시간 분해된 광자 수 형태의 상세한 비행시간 데이터를 캡처합니다. 이 비행시간 데이터는 풍부한 장면 정보를 인코딩하며, 따라서 희소한 측정값으로부터 단순한 장면을 복원할 수 있게 합니다. 우리는 적은 수의 측정값(예: 15픽셀 정도)으로 분산된 세트를 사용하여 강력한 사전 지식을 가진 단순 매개변수 장면의 기하학을 복원하는 가능성을 조사합니다. 예를 들어, 알려진 객체의 6D 자세를 추정하는 것과 같은 작업입니다. 이를 달성하기 위해, 우리는 장면 매개변수를 추론하기 위한 피드포워드 예측과 분석-합성 프레임워크 내에서 장면 매개변수 추정치를 정제하기 위한 미분 가능한 렌더링을 모두 활용하는 방법을 설계합니다. 우리는 하드웨어 프로토타입을 개발하고, 시뮬레이션과 통제된 실제 촬영에서 텍스처가 없는 3D 모델이 주어졌을 때 우리의 방법이 객체 자세를 효과적으로 복원함을 입증하며, 다른 매개변수 장면에 대한 유망한 초기 결과를 보여줍니다. 추가로, 우리의 이미징 솔루션의 한계와 능력을 탐구하기 위한 실험을 수행합니다.

## 📝 요약

이 논문은 저비용 상용 비행시간(ToF) 센서를 사용하여 소수의 깊이 측정으로 3D 파라메트릭 장면의 기하학을 복원하는 방법을 제안합니다. 이 센서는 낮은 공간 해상도를 제공하지만, 픽셀당 넓은 시야각과 시간 분해된 광자 수를 캡처하여 장면 정보를 풍부하게 인코딩합니다. 연구에서는 소수의 측정값(예: 15픽셀)으로 강한 사전 정보를 가진 간단한 파라메트릭 장면의 기하학을 복원할 수 있는 가능성을 탐구합니다. 이를 위해 장면 매개변수를 추론하는 피드포워드 예측과 분석-합성 프레임워크 내에서의 미분 가능한 렌더링을 결합한 방법을 설계했습니다. 하드웨어 프로토타입을 개발하고, 시뮬레이션 및 실제 환경에서 텍스처 없는 3D 모델을 사용하여 객체의 자세를 효과적으로 복원하는 방법을 입증했습니다. 추가로, 다른 파라메트릭 장면에 대한 초기 결과도 제시하며, 이 이미지 솔루션의 한계와 가능성을 탐구하는 실험을 수행했습니다.

## 🎯 주요 포인트

- 1. 저비용 상용 비행시간 센서를 사용하여 3D 파라메트릭 장면의 기하학을 소수의 깊이 측정으로 복원하는 방법을 연구합니다.
- 2. 단일 픽셀의 매우 낮은 공간 해상도를 가진 센서가 넓은 시야와 시간 분해 광자 수 데이터를 제공하여 장면 정보를 인코딩합니다.
- 3. 소수의 측정값(예: 15픽셀)으로 간단한 파라메트릭 장면의 기하학을 복원하는 것이 가능함을 조사합니다.
- 4. 장면 매개변수를 추론하기 위한 피드포워드 예측과 분석-합성 프레임워크 내의 미분 가능 렌더링을 결합한 방법을 설계합니다.
- 5. 하드웨어 프로토타입을 개발하여 시뮬레이션과 실제 환경에서 텍스처가 없는 3D 모델의 객체 자세를 효과적으로 복원함을 입증합니다.


---

*Generated on 2025-09-23 12:21:44*