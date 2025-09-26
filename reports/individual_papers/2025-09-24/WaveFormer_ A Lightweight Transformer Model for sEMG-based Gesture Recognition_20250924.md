<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:30:46.932193",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Wavelet Transform",
    "sEMG Gesture Recognition",
    "INT8 Quantization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Wavelet Transform": 0.78,
    "sEMG Gesture Recognition": 0.8,
    "INT8 Quantization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in machine learning, relevant to the proposed WaveFormer model.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Wavelet Transform",
        "canonical": "Wavelet Transform",
        "aliases": [
          "WaveletConv",
          "Wavelet Decomposition"
        ],
        "category": "unique_technical",
        "rationale": "Wavelet Transform is a unique feature of the WaveFormer model, enhancing its gesture recognition capabilities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "sEMG Gesture Recognition",
        "canonical": "sEMG Gesture Recognition",
        "aliases": [
          "Surface Electromyographic Gesture Recognition"
        ],
        "category": "unique_technical",
        "rationale": "The focus on sEMG gesture recognition is central to the paper's contribution to human-machine interaction.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "INT8 Quantization",
        "canonical": "INT8 Quantization",
        "aliases": [
          "8-bit Quantization"
        ],
        "category": "specific_connectable",
        "rationale": "INT8 Quantization is a key technique for enabling real-time deployment on resource-constrained systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "gesture recognition",
      "classification accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Wavelet Transform",
      "resolved_canonical": "Wavelet Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "sEMG Gesture Recognition",
      "resolved_canonical": "sEMG Gesture Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "INT8 Quantization",
      "resolved_canonical": "INT8 Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# WaveFormer: A Lightweight Transformer Model for sEMG-based Gesture Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2506.11168.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2506.11168](https://arxiv.org/abs/2506.11168)

## 🔗 유사한 논문
- [[2025-09-23/Contextual Gesture_ Co-Speech Gesture Video Generation through Context-aware Gesture Representation_20250923|Contextual Gesture: Co-Speech Gesture Video Generation through Context-aware Gesture Representation]] (80.4% similar)
- [[2025-09-23/Search-Optimized Quantization in Biomedical Ontology Alignment_20250923|Search-Optimized Quantization in Biomedical Ontology Alignment]] (80.2% similar)
- [[2025-09-23/SISMA_ Semantic Face Image Synthesis with Mamba_20250923|SISMA: Semantic Face Image Synthesis with Mamba]] (80.0% similar)
- [[2025-09-24/PainFormer_ a Vision Foundation Model for Automatic Pain Assessment_20250924|PainFormer: a Vision Foundation Model for Automatic Pain Assessment]] (79.7% similar)
- [[2025-09-24/An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling_20250924|An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling]] (79.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/INT8 Quantization|INT8 Quantization]]
**⚡ Unique Technical**: [[keywords/Wavelet Transform|Wavelet Transform]], [[keywords/sEMG Gesture Recognition|sEMG Gesture Recognition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.11168v2 Announce Type: replace 
Abstract: Human-machine interaction, particularly in prosthetic and robotic control, has seen progress with gesture recognition via surface electromyographic (sEMG) signals.However, classifying similar gestures that produce nearly identical muscle signals remains a challenge, often reducing classification accuracy. Traditional deep learning models for sEMG gesture recognition are large and computationally expensive, limiting their deployment on resource-constrained embedded systems. In this work, we propose WaveFormer, a lightweight transformer-based architecture tailored for sEMG gesture recognition. Our model integrates time-domain and frequency-domain features through a novel learnable wavelet transform, enhancing feature extraction. In particular, the WaveletConv module, a multi-level wavelet decomposition layer with depthwise separable convolution, ensures both efficiency and compactness. With just 3.1 million parameters, WaveFormer achieves 95% classification accuracy on the EPN612 dataset, outperforming larger models. Furthermore, when profiled on a laptop equipped with an Intel CPU, INT8 quantization achieves real-time deployment with a 6.75 ms inference latency.

## 📝 요약

이 연구에서는 표면 근전도(sEMG) 신호를 통한 제스처 인식에서 발생하는 유사한 제스처 분류 문제를 해결하기 위해 WaveFormer라는 경량의 트랜스포머 기반 아키텍처를 제안합니다. WaveFormer는 시간 및 주파수 도메인 특징을 통합하여 특징 추출을 강화하며, 특히 WaveletConv 모듈을 통해 효율성과 컴팩트함을 보장합니다. 이 모델은 310만 개의 파라미터로 EPN612 데이터셋에서 95%의 분류 정확도를 달성하며, 더 큰 모델들을 능가합니다. 또한, INT8 양자화를 통해 인텔 CPU가 장착된 노트북에서 6.75ms의 추론 지연 시간으로 실시간 배포가 가능합니다.

## 🎯 주요 포인트

- 1. 유사한 근육 신호를 생성하는 제스처를 분류하는 것은 여전히 어려운 문제로, 이는 분류 정확도를 감소시킨다.
- 2. 기존의 sEMG 제스처 인식을 위한 딥러닝 모델은 크고 계산 비용이 높아, 자원이 제한된 임베디드 시스템에서의 활용이 제한적이다.
- 3. WaveFormer는 sEMG 제스처 인식을 위한 경량의 트랜스포머 기반 아키텍처로, 시간 및 주파수 도메인 특징을 통합하여 특징 추출을 향상시킨다.
- 4. WaveFormer는 310만 개의 파라미터로 EPN612 데이터셋에서 95%의 분류 정확도를 달성하며, 더 큰 모델들을 능가한다.
- 5. INT8 양자화는 인텔 CPU가 장착된 노트북에서 실시간 배포를 가능하게 하며, 6.75ms의 추론 지연 시간을 기록한다.


---

*Generated on 2025-09-24 16:30:46*