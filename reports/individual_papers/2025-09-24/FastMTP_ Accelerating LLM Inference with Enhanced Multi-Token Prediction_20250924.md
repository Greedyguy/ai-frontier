<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:46:32.921227",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-Token Prediction",
    "Speculative Decoding",
    "Dynamic Vocabulary Compression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multi-Token Prediction": 0.78,
    "Speculative Decoding": 0.72,
    "Dynamic Vocabulary Compression": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion on inference acceleration and are a key concept in modern NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Token Prediction",
        "canonical": "Multi-Token Prediction",
        "aliases": [
          "MTP"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces FastMTP, which is a novel method for enhancing multi-token prediction, a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Speculative Decoding",
        "canonical": "Speculative Decoding",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Speculative Decoding is a specific technique discussed in the paper that contributes to inference speedup, making it a unique technical concept.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Dynamic Vocabulary Compression",
        "canonical": "Dynamic Vocabulary Compression",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is crucial for reducing computational overhead and is a unique technical concept introduced in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-Token Prediction",
      "resolved_canonical": "Multi-Token Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Speculative Decoding",
      "resolved_canonical": "Speculative Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Dynamic Vocabulary Compression",
      "resolved_canonical": "Dynamic Vocabulary Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# FastMTP: Accelerating LLM Inference with Enhanced Multi-Token Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18362.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18362](https://arxiv.org/abs/2509.18362)

## 🔗 유사한 논문
- [[2025-09-23/L-MTP_ Leap Multi-Token Prediction Beyond Adjacent Context for Large Language Models_20250923|L-MTP: Leap Multi-Token Prediction Beyond Adjacent Context for Large Language Models]] (92.2% similar)
- [[2025-09-22/CARD_ A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference_20250922|CARD: A Cache-Assisted Parallel Speculative Decoding Framework via Query-and-Correct Paradigm for Accelerating LLM Inference]] (83.9% similar)
- [[2025-09-23/Spiffy_ Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding_20250923|Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding]] (83.7% similar)
- [[2025-09-24/Sparse Training Scheme for Multimodal LLM_20250924|Sparse Training Scheme for Multimodal LLM]] (83.5% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Multi-Token Prediction|Multi-Token Prediction]], [[keywords/Speculative Decoding|Speculative Decoding]], [[keywords/Dynamic Vocabulary Compression|Dynamic Vocabulary Compression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18362v1 Announce Type: cross 
Abstract: As large language models (LLMs) become increasingly powerful, the sequential nature of autoregressive generation creates a fundamental throughput bottleneck that limits the practical deployment. While Multi-Token Prediction (MTP) has demonstrated remarkable benefits for model training efficiency and performance, its inherent potential for inference acceleration remains largely unexplored. This paper introduces FastMTP, a simple yet effective method that improves multi-step draft quality by aligning MTP training with its inference pattern, significantly enhancing speculative decoding performance. Our approach fine-tunes a single MTP head with position-shared weights on self-distilled data, enabling it to capture dependencies among consecutive future tokens and maintain high acceptance rates across multiple recursive draft steps. By integrating language-aware dynamic vocabulary compression into the MTP head, we further reduce computational overhead in the drafting process. Experimental results across seven diverse benchmarks demonstrate that FastMTP achieves an average of 2.03x speedup compared to standard next token prediction with lossless output quality, outperforming vanilla MTP by 82%. FastMTP requires only lightweight training and seamlessly integrates with existing inference frameworks, offering a practical and rapidly deployable solution for accelerating LLM inference.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 추론 속도를 향상시키기 위한 FastMTP라는 방법을 제안합니다. FastMTP는 다중 토큰 예측(MTP) 훈련을 추론 패턴과 정렬시켜 추론 성능을 크게 개선합니다. 이 방법은 위치 공유 가중치를 가진 단일 MTP 헤드를 미세 조정하여 연속적인 미래 토큰 간의 의존성을 포착하고, 여러 단계의 초안 작성에서 높은 수용률을 유지합니다. 또한, 언어 인식 동적 어휘 압축을 통합하여 계산 부담을 줄입니다. 실험 결과, FastMTP는 표준 다음 토큰 예측보다 평균 2.03배 빠른 속도를 기록하며, 기존 MTP보다 82% 더 우수한 성능을 보였습니다. FastMTP는 경량 훈련만 필요하며 기존 추론 프레임워크에 쉽게 통합될 수 있어 실용적이고 빠르게 배포 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. FastMTP는 MTP 훈련을 추론 패턴과 정렬하여 다단계 초안 품질을 개선하고 추측 디코딩 성능을 크게 향상시킵니다.
- 2. FastMTP는 위치 공유 가중치를 가진 단일 MTP 헤드를 미세 조정하여 연속적인 미래 토큰 간의 종속성을 포착하고 여러 반복 초안 단계에서 높은 수용률을 유지합니다.
- 3. 언어 인식 동적 어휘 압축을 MTP 헤드에 통합하여 초안 작성 과정에서 계산 오버헤드를 줄입니다.
- 4. FastMTP는 표준 다음 토큰 예측에 비해 평균 2.03배의 속도 향상을 달성하며, 출력 품질의 손실 없이 바닐라 MTP보다 82% 더 우수한 성능을 보입니다.
- 5. FastMTP는 경량 훈련만 필요하며 기존 추론 프레임워크와 원활하게 통합되어 LLM 추론을 가속화하는 실용적이고 신속하게 배포 가능한 솔루션을 제공합니다.


---

*Generated on 2025-09-24 13:46:32*