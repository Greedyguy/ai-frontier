---
keywords:
  - Neural Network
  - Audio Tagging
  - Edge Computing
  - ONNX
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.14049
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:15:03.163706",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Audio Tagging",
    "Edge Computing",
    "ONNX"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Audio Tagging": 0.78,
    "Edge Computing": 0.8,
    "ONNX": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNN",
          "ConvNet"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are a fundamental concept in deep learning, and CNNs are a specific type widely used in audio and image processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Audio Tagging",
        "canonical": "Audio Tagging",
        "aliases": [
          "Sound Classification"
        ],
        "category": "unique_technical",
        "rationale": "Audio Tagging is a specific application of neural networks, providing a unique link to audio processing tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Resource-Constrained Devices",
        "canonical": "Edge Computing",
        "aliases": [
          "IoT Devices",
          "Low-Power Devices"
        ],
        "category": "specific_connectable",
        "rationale": "Edge Computing is increasingly relevant for deploying models on devices with limited resources, enhancing connectivity with IoT applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Open Neural Network Exchange",
        "canonical": "ONNX",
        "aliases": [
          "ONNX Format"
        ],
        "category": "unique_technical",
        "rationale": "ONNX is a key format for model interoperability across different platforms, crucial for deployment strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "computational efficiency",
      "thermal management",
      "performance stability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Audio Tagging",
      "resolved_canonical": "Audio Tagging",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Resource-Constrained Devices",
      "resolved_canonical": "Edge Computing",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Open Neural Network Exchange",
      "resolved_canonical": "ONNX",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Comprehensive Evaluation of CNN-Based Audio Tagging Models on Resource-Constrained Devices

**Korean Title:** 자원 제약 장치에서 CNN 기반 오디오 태깅 모델의 종합 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14049.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.14049](https://arxiv.org/abs/2509.14049)

## 🔗 유사한 논문
- [[2025-09-17/Comprehensive Evaluation of CNN-Based Audio Tagging Models on Resource-Constrained Devices_20250917|Comprehensive Evaluation of CNN-Based Audio Tagging Models on Resource-Constrained Devices]] (99.2% similar)
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (79.0% similar)
- [[2025-09-17/RFM-Editing_ Rectified Flow Matching for Text-guided Audio Editing_20250917|RFM-Editing: Rectified Flow Matching for Text-guided Audio Editing]] (78.9% similar)
- [[2025-09-22/Modeling the Human Visual System_ Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms_20250922|Modeling the Human Visual System: Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms]] (78.9% similar)
- [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL: Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Edge Computing|Edge Computing]]
**⚡ Unique Technical**: [[keywords/Audio Tagging|Audio Tagging]], [[keywords/ONNX|ONNX]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14049v2 Announce Type: replace-cross 
Abstract: Convolutional Neural Networks (CNNs) have demonstrated exceptional performance in audio tagging tasks. However, deploying these models on resource-constrained devices like the Raspberry Pi poses challenges related to computational efficiency and thermal management. In this paper, a comprehensive evaluation of multiple convolutional neural network (CNN) architectures for audio tagging on the Raspberry Pi is conducted, encompassing all 1D and 2D models from the Pretrained Audio Neural Networks (PANNs) framework, a ConvNeXt-based model adapted for audio classification, as well as MobileNetV3 architectures. In addition, two PANNs-derived networks, CNN9 and CNN13, recently proposed, are also evaluated. To enhance deployment efficiency and portability across diverse hardware platforms, all models are converted to the Open Neural Network Exchange (ONNX) format. Unlike previous works that focus on a single model, our analysis encompasses a broader range of architectures and involves continuous 24-hour inference sessions to assess performance stability. Our experiments reveal that, with appropriate model selection and optimization, it is possible to maintain consistent inference latency and manage thermal behavior effectively over extended periods. These findings provide valuable insights for deploying audio tagging models in real-world edge computing scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.14049v2 발표 유형: 교차 교체  
초록: 합성곱 신경망(CNN)은 오디오 태깅 작업에서 뛰어난 성능을 입증했습니다. 그러나 Raspberry Pi와 같은 자원이 제한된 장치에 이러한 모델을 배포하는 것은 계산 효율성과 열 관리와 관련된 문제를 제기합니다. 본 논문에서는 Raspberry Pi에서 오디오 태깅을 위한 여러 합성곱 신경망(CNN) 아키텍처를 포괄적으로 평가하며, 여기에는 사전 학습된 오디오 신경망(PANNs) 프레임워크의 모든 1D 및 2D 모델, 오디오 분류를 위해 적응된 ConvNeXt 기반 모델, 그리고 MobileNetV3 아키텍처가 포함됩니다. 또한, 최근 제안된 두 개의 PANNs 파생 네트워크인 CNN9 및 CNN13도 평가됩니다. 다양한 하드웨어 플랫폼에서의 배포 효율성과 이동성을 향상시키기 위해 모든 모델은 Open Neural Network Exchange (ONNX) 형식으로 변환됩니다. 단일 모델에 초점을 맞춘 이전 연구와 달리, 본 분석은 보다 광범위한 아키텍처를 포괄하며 성능 안정성을 평가하기 위해 24시간 연속 추론 세션을 포함합니다. 실험 결과, 적절한 모델 선택과 최적화를 통해 장기간에 걸쳐 일관된 추론 지연 시간을 유지하고 열 거동을 효과적으로 관리할 수 있음을 보여줍니다. 이러한 발견은 실제 엣지 컴퓨팅 시나리오에서 오디오 태깅 모델을 배포하는 데 있어 귀중한 통찰력을 제공합니다.

## 📝 요약

이 논문은 Raspberry Pi와 같은 자원이 제한된 장치에서 오디오 태깅을 위한 여러 CNN 아키텍처의 성능을 평가합니다. PANNs 프레임워크의 1D 및 2D 모델, ConvNeXt 기반 모델, MobileNetV3 아키텍처, 그리고 최근 제안된 CNN9 및 CNN13 네트워크를 포함합니다. 모든 모델은 ONNX 형식으로 변환되어 다양한 하드웨어 플랫폼에서의 효율성과 이식성을 높였습니다. 24시간 연속 추론 세션을 통해 성능 안정성을 평가한 결과, 적절한 모델 선택과 최적화를 통해 일관된 추론 지연 시간과 열 관리를 유지할 수 있음을 발견했습니다. 이는 실제 엣지 컴퓨팅 환경에서 오디오 태깅 모델 배포에 유용한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. Raspberry Pi와 같은 자원 제한 장치에서 CNN 기반 오디오 태깅 모델의 효율적인 배포를 위한 다양한 아키텍처 평가가 이루어졌습니다.
- 2. PANNs 프레임워크의 1D 및 2D 모델, ConvNeXt 기반 모델, MobileNetV3 아키텍처가 평가되었습니다.
- 3. 모든 모델은 다양한 하드웨어 플랫폼에서의 효율성과 이식성을 높이기 위해 ONNX 형식으로 변환되었습니다.
- 4. 24시간 연속 추론 세션을 통해 성능 안정성을 평가하며, 적절한 모델 선택과 최적화를 통해 일관된 추론 지연과 열 관리가 가능함을 발견했습니다.
- 5. 연구 결과는 실제 엣지 컴퓨팅 시나리오에서 오디오 태깅 모델을 배포하는 데 유용한 통찰력을 제공합니다.


---

*Generated on 2025-09-23 10:15:03*