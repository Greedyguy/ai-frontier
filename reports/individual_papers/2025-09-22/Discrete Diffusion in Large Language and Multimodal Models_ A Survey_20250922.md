---
keywords:
  - Discrete Diffusion Language Models
  - Discrete Diffusion Multimodal Language Models
  - Parallel Decoding
  - Vision-Language Model
  - Denoising-based Generation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2506.13759
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:04:21.259182",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Discrete Diffusion Language Models",
    "Discrete Diffusion Multimodal Language Models",
    "Parallel Decoding",
    "Vision-Language Model",
    "Denoising-based Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Discrete Diffusion Language Models": 0.78,
    "Discrete Diffusion Multimodal Language Models": 0.8,
    "Parallel Decoding": 0.77,
    "Vision-Language Model": 0.79,
    "Denoising-based Generation": 0.76
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Discrete Diffusion Language Models",
        "canonical": "Discrete Diffusion Language Models",
        "aliases": [
          "dLLMs"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel paradigm in language model design distinct from autoregressive models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Discrete Diffusion Multimodal Language Models",
        "canonical": "Discrete Diffusion Multimodal Language Models",
        "aliases": [
          "dMLLMs"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific application of discrete diffusion in multimodal contexts, offering new research directions.",
        "novelty_score": 0.78,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Parallel Decoding",
        "canonical": "Parallel Decoding",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key technique enabling faster inference in discrete diffusion models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Represents a significant application area for multimodal models, linking language and vision.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "Denoising-based Generation",
        "canonical": "Denoising-based Generation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the generation strategy of discrete diffusion models, differentiating them from traditional methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.76
      }
    ],
    "ban_list_suggestions": [
      "autoregressive",
      "inference speed"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Discrete Diffusion Language Models",
      "resolved_canonical": "Discrete Diffusion Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Discrete Diffusion Multimodal Language Models",
      "resolved_canonical": "Discrete Diffusion Multimodal Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Parallel Decoding",
      "resolved_canonical": "Parallel Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Denoising-based Generation",
      "resolved_canonical": "Denoising-based Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.76
      }
    }
  ]
}
-->

# Discrete Diffusion in Large Language and Multimodal Models: A Survey

**Korean Title:** 대형 언어 및 다중 모달 모델에서의 이산 확산: 조사

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.13759.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2506.13759](https://arxiv.org/abs/2506.13759)

## 🔗 유사한 논문
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (86.3% similar)
- [[2025-09-18/From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery]] (85.7% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (85.5% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (85.5% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Parallel Decoding|Parallel Decoding]], [[keywords/Denoising-based Generation|Denoising-based Generation]]
**⚡ Unique Technical**: [[keywords/Discrete Diffusion Language Models|Discrete Diffusion Language Models]], [[keywords/Discrete Diffusion Multimodal Language Models|Discrete Diffusion Multimodal Language Models]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.13759v5 Announce Type: replace-cross 
Abstract: In this work, we provide a systematic survey of Discrete Diffusion Language Models (dLLMs) and Discrete Diffusion Multimodal Language Models (dMLLMs). Unlike autoregressive (AR) models, dLLMs and dMLLMs adopt a multi-token, parallel decoding paradigm using full attention and a denoising-based generation strategy. This paradigm naturally enables parallel generation, fine-grained output control, and dynamic perception. These capabilities are previously difficult to achieve with AR models. A growing number of industrial-scale proprietary d(M)LLMs, as well as a large number of open-source academic d(M)LLMs, have demonstrated performance comparable to their autoregressive counterparts, while achieving up to 10$\times$ acceleration in inference speed. These developments position discrete diffusion models as a promising alternative to intelligence based on the traditional autoregressive approach. In this work, we present a comprehensive overview of the research in the dLLM and dMLLM domains. We trace the historical development of dLLMs and dMLLMs, formalize the underlying mathematical frameworks, list commonly-used modeling methods, and categorize representative models. We further analyze key techniques for training, inference, quantization. We also discuss the trustworthy issues and summarize emerging applications across language, vision-language, and biological domains and etc.. We conclude by discussing future directions for research and deployment. Relative papers are collected in https://github.com/LiQiiiii/Awesome-Discrete-Diffusion-LLM_MLLM

## 🔍 Abstract (한글 번역)

arXiv:2506.13759v5 발표 유형: 교차 교체  
초록: 본 연구에서는 이산 확산 언어 모델(dLLM)과 이산 확산 다중모달 언어 모델(dMLLM)에 대한 체계적인 조사를 제공합니다. 자기회귀(AR) 모델과 달리, dLLM과 dMLLM은 전체 주의(attention)와 잡음 제거 기반 생성 전략을 사용하는 다중 토큰, 병렬 디코딩 패러다임을 채택합니다. 이 패러다임은 자연스럽게 병렬 생성, 세밀한 출력 제어 및 동적 인식을 가능하게 합니다. 이러한 기능은 AR 모델로는 이전에 달성하기 어려웠습니다. 산업 규모의 독점 d(M)LLM뿐만 아니라 다수의 오픈 소스 학술 d(M)LLM이 자기회귀 모델과 비교할 만한 성능을 보여주었으며, 추론 속도에서 최대 10배의 가속을 달성했습니다. 이러한 발전은 전통적인 자기회귀 접근 방식에 기반한 인공지능에 대한 유망한 대안으로 이산 확산 모델을 자리매김하게 합니다. 본 연구에서는 dLLM과 dMLLM 분야의 연구에 대한 포괄적인 개요를 제시합니다. dLLM과 dMLLM의 역사적 발전을 추적하고, 기본 수학적 프레임워크를 공식화하며, 일반적으로 사용되는 모델링 방법을 나열하고, 대표 모델을 분류합니다. 또한, 훈련, 추론, 양자화에 대한 주요 기술을 분석합니다. 신뢰성 문제를 논의하고, 언어, 비전-언어, 생물학적 분야 등에서의 새로운 응용을 요약합니다. 연구 및 배포의 미래 방향에 대해 논의하며 결론을 내립니다. 관련 논문은 https://github.com/LiQiiiii/Awesome-Discrete-Diffusion-LLM_MLLM에 수집되어 있습니다.

## 📝 요약

이 논문은 이산 확산 언어 모델(dLLM)과 이산 확산 다중모달 언어 모델(dMLLM)에 대한 체계적인 조사를 제공합니다. 기존의 자기회귀 모델과 달리, dLLM과 dMLLM은 멀티 토큰, 병렬 디코딩 패러다임을 채택하여 병렬 생성, 세밀한 출력 제어, 동적 인식을 가능하게 합니다. 이러한 모델들은 자기회귀 모델에 비해 최대 10배 빠른 추론 속도를 보이며, 산업 규모의 독점 모델과 오픈 소스 학술 모델 모두에서 유사한 성능을 입증했습니다. 논문은 dLLM과 dMLLM의 역사적 발전, 수학적 프레임워크, 일반적인 모델링 방법, 대표 모델을 분류하고, 훈련, 추론, 양자화의 주요 기술을 분석합니다. 또한 신뢰성 문제와 언어, 비전-언어, 생물학적 분야의 응용을 논의하며, 향후 연구 방향을 제시합니다.

## 🎯 주요 포인트

- 1. 본 논문은 Discrete Diffusion Language Models (dLLMs)와 Discrete Diffusion Multimodal Language Models (dMLLMs)에 대한 체계적인 조사를 제공한다.
- 2. dLLMs와 dMLLMs는 다중 토큰, 병렬 디코딩 패러다임을 채택하여 병렬 생성, 세밀한 출력 제어, 동적 인식을 가능하게 한다.
- 3. d(M)LLMs는 기존의 autoregressive 모델과 비교하여 최대 10배의 추론 속도 가속을 달성하면서 성능을 입증하였다.
- 4. 논문은 dLLM과 dMLLM의 역사적 발전, 수학적 프레임워크, 일반적인 모델링 방법, 대표 모델을 포괄적으로 개관한다.
- 5. 연구는 언어, 비전-언어, 생물학적 분야 등에서의 새로운 응용을 요약하고, 신뢰성 문제와 미래 연구 방향을 논의한다.


---

*Generated on 2025-09-23 10:04:21*