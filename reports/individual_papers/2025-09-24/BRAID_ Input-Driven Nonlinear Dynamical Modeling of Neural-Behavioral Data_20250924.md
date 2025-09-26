<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:58:07.404956",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "BRAID Framework",
    "Neural Dynamics",
    "Input-Driven Neural Networks",
    "Motor Cortical Activity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "BRAID Framework": 0.85,
    "Neural Dynamics": 0.7,
    "Input-Driven Neural Networks": 0.78,
    "Motor Cortical Activity": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "BRAID",
        "canonical": "BRAID Framework",
        "aliases": [
          "BRAID Model"
        ],
        "category": "unique_technical",
        "rationale": "BRAID is a novel framework specifically introduced in this paper, making it a unique technical term.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "neural dynamics",
        "canonical": "Neural Dynamics",
        "aliases": [
          "neural activity dynamics"
        ],
        "category": "broad_technical",
        "rationale": "Neural dynamics is a fundamental concept in neuroscience and links to various related studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "input-driven recurrent neural networks",
        "canonical": "Input-Driven Neural Networks",
        "aliases": [
          "input-driven RNNs"
        ],
        "category": "specific_connectable",
        "rationale": "This concept connects to the broader field of neural networks with a specific focus on input-driven models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "motor cortical activity",
        "canonical": "Motor Cortical Activity",
        "aliases": [
          "motor cortex activity"
        ],
        "category": "specific_connectable",
        "rationale": "Motor cortical activity is a specific area of study within neuroscience, linking to research on motor control and behavior.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "behavior",
      "model",
      "neural-behavioral data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "BRAID",
      "resolved_canonical": "BRAID Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "neural dynamics",
      "resolved_canonical": "Neural Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "input-driven recurrent neural networks",
      "resolved_canonical": "Input-Driven Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "motor cortical activity",
      "resolved_canonical": "Motor Cortical Activity",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# BRAID: Input-Driven Nonlinear Dynamical Modeling of Neural-Behavioral Data

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18627.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18627](https://arxiv.org/abs/2509.18627)

## 🔗 유사한 논문
- [[2025-09-24/Dynamical Modeling of Behaviorally Relevant Spatiotemporal Patterns in Neural Imaging Data_20250924|Dynamical Modeling of Behaviorally Relevant Spatiotemporal Patterns in Neural Imaging Data]] (85.2% similar)
- [[2025-09-23/Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks_20250923|Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks]] (80.9% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding_20250919|UMind: A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding]] (80.8% similar)
- [[2025-09-23/DynSTG-Mamba_ Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition_20250923|DynSTG-Mamba: Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition]] (80.8% similar)
- [[2025-09-19/ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Dynamics|Neural Dynamics]]
**🔗 Specific Connectable**: [[keywords/Input-Driven Neural Networks|Input-Driven Neural Networks]], [[keywords/Motor Cortical Activity|Motor Cortical Activity]]
**⚡ Unique Technical**: [[keywords/BRAID Framework|BRAID Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18627v1 Announce Type: cross 
Abstract: Neural populations exhibit complex recurrent structures that drive behavior, while continuously receiving and integrating external inputs from sensory stimuli, upstream regions, and neurostimulation. However, neural populations are often modeled as autonomous dynamical systems, with little consideration given to the influence of external inputs that shape the population activity and behavioral outcomes. Here, we introduce BRAID, a deep learning framework that models nonlinear neural dynamics underlying behavior while explicitly incorporating any measured external inputs. Our method disentangles intrinsic recurrent neural population dynamics from the effects of inputs by including a forecasting objective within input-driven recurrent neural networks. BRAID further prioritizes the learning of intrinsic dynamics that are related to a behavior of interest by using a multi-stage optimization scheme. We validate BRAID with nonlinear simulations, showing that it can accurately learn the intrinsic dynamics shared between neural and behavioral modalities. We then apply BRAID to motor cortical activity recorded during a motor task and demonstrate that our method more accurately fits the neural-behavioral data by incorporating measured sensory stimuli into the model and improves the forecasting of neural-behavioral data compared with various baseline methods, whether input-driven or not.

## 📝 요약

이 논문은 외부 입력을 명시적으로 통합하여 행동을 유도하는 비선형 신경 동역학을 모델링하는 딥러닝 프레임워크인 BRAID를 소개합니다. BRAID는 입력에 의해 구동되는 순환 신경망 내에서 예측 목표를 포함하여 내재적 순환 신경 집단 동역학과 입력의 영향을 분리합니다. 다단계 최적화 방식을 통해 관심 있는 행동과 관련된 내재적 동역학 학습을 우선시합니다. 비선형 시뮬레이션을 통해 BRAID의 유효성을 검증하고, 운동 과제 중 기록된 운동 피질 활동에 적용하여 감각 자극을 모델에 통합함으로써 기존 방법보다 신경-행동 데이터의 예측 정확성을 향상시킵니다.

## 🎯 주요 포인트

- 1. BRAID는 외부 입력을 명시적으로 통합하여 행동을 기반으로 한 비선형 신경 역학을 모델링하는 딥러닝 프레임워크입니다.
- 2. 이 방법은 입력에 의해 영향을 받는 신경 집단의 내재적 순환 동역학을 분리하여 예측 목표를 포함합니다.
- 3. BRAID는 여러 단계의 최적화 방식을 사용하여 관심 있는 행동과 관련된 내재적 동역학 학습을 우선시합니다.
- 4. 비선형 시뮬레이션을 통해 BRAID가 신경 및 행동 양식 간에 공유되는 내재적 동역학을 정확하게 학습할 수 있음을 검증했습니다.
- 5. BRAID는 운동 과제 중 기록된 운동 피질 활동에 적용되어 측정된 감각 자극을 모델에 통합함으로써 신경-행동 데이터를 더 정확하게 예측합니다.


---

*Generated on 2025-09-24 13:58:07*