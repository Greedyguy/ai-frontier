---
keywords:
  - Federated Learning
  - Voice Cloning
  - Low-Rank Adaptation
  - Collaborative Filtering
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16010
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:25:52.206125",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Voice Cloning",
    "Low-Rank Adaptation",
    "Collaborative Filtering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Voice Cloning": 0.78,
    "Low-Rank Adaptation": 0.72,
    "Collaborative Filtering": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is a key framework for privacy-preserving collaborative learning, crucial for linking with other distributed learning methods.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Voice Cloning",
        "canonical": "Voice Cloning",
        "aliases": [
          "Speech Synthesis"
        ],
        "category": "unique_technical",
        "rationale": "Voice Cloning is a specialized application of TTS, linking to personalized and expressive speech generation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "Low-Rank Adaptation is a novel mechanism for efficient model adaptation, important for linking to parameter-efficient learning methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Collaborative Filtering",
        "canonical": "Collaborative Filtering",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Collaborative Filtering is used for personalized model aggregation, connecting to recommendation systems and personalization techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Text-to-Speech",
      "Personalized Identity-Style Adaptation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Voice Cloning",
      "resolved_canonical": "Voice Cloning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Collaborative Filtering",
      "resolved_canonical": "Collaborative Filtering",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation

**Korean Title:** 연합 PISA: 개인화된 정체성-스타일 적응을 통한 연합 음성 복제

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16010.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16010](https://arxiv.org/abs/2509.16010)

## 🔗 유사한 논문
- [[2025-09-22/P2VA_ Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech_20250922|P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech]] (82.8% similar)
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (82.1% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (80.7% similar)
- [[2025-09-19/SpeechOp_ Inference-Time Task Composition for Generative Speech Processing_20250919|SpeechOp: Inference-Time Task Composition for Generative Speech Processing]] (80.5% similar)
- [[2025-09-22/LESS_ Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data_20250922|LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Collaborative Filtering|Collaborative Filtering]]
**⚡ Unique Technical**: [[keywords/Voice Cloning|Voice Cloning]], [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16010v1 Announce Type: cross 
Abstract: Voice cloning for Text-to-Speech (TTS) aims to generate expressive and personalized speech from text using limited data from a target speaker. Federated Learning (FL) offers a collaborative and privacy-preserving framework for this task, but existing approaches suffer from high communication costs and tend to suppress stylistic heterogeneity, resulting in insufficient personalization. To address these issues, we propose Fed-PISA, which stands for Federated Personalized Identity-Style Adaptation. To minimize communication costs, Fed-PISA introduces a disentangled Low-Rank Adaptation (LoRA) mechanism: the speaker's timbre is retained locally through a private ID-LoRA, while only a lightweight style-LoRA is transmitted to the server, thereby minimizing parameter exchange. To harness heterogeneity, our aggregation method, inspired by collaborative filtering, is introduced to create custom models for each client by learning from stylistically similar peers. Experiments show that Fed-PISA improves style expressivity, naturalness, and speaker similarity, outperforming standard federated baselines with minimal communication costs.

## 🔍 Abstract (한글 번역)

arXiv:2509.16010v1 발표 유형: 교차  
초록: 텍스트 음성 변환(TTS)을 위한 음성 클로닝은 대상 화자의 제한된 데이터를 사용하여 텍스트로부터 표현력 있고 개인화된 음성을 생성하는 것을 목표로 합니다. 연합 학습(FL)은 이 작업을 위한 협력적이고 프라이버시를 보호하는 프레임워크를 제공하지만, 기존 접근 방식은 높은 통신 비용이 발생하고 스타일의 이질성을 억제하는 경향이 있어 개인화가 충분하지 않습니다. 이러한 문제를 해결하기 위해 우리는 Fed-PISA, 즉 연합 개인화된 정체성-스타일 적응(Federated Personalized Identity-Style Adaptation)을 제안합니다. 통신 비용을 최소화하기 위해, Fed-PISA는 분리된 저순위 적응(LoRA) 메커니즘을 도입합니다: 화자의 음색은 개인 ID-LoRA를 통해 로컬에서 유지되며, 가벼운 스타일-LoRA만 서버로 전송되어 매개변수 교환을 최소화합니다. 이질성을 활용하기 위해, 협업 필터링에서 영감을 받은 우리의 집계 방법은 스타일적으로 유사한 동료로부터 학습하여 각 클라이언트에 맞춤형 모델을 생성합니다. 실험 결과, Fed-PISA는 스타일 표현력, 자연스러움, 화자 유사성을 향상시키며, 최소한의 통신 비용으로 표준 연합 기준선을 능가하는 것으로 나타났습니다.

## 📝 요약

이 논문은 제한된 데이터로 텍스트에서 개인화된 음성을 생성하는 음성 복제를 위한 연합 학습(Federated Learning, FL) 방법인 Fed-PISA를 제안합니다. 기존 FL 접근법의 높은 통신 비용과 스타일 다양성 억제 문제를 해결하기 위해, 저자들은 Low-Rank Adaptation(LoRA) 메커니즘을 도입하여 통신 비용을 줄였습니다. 이 방법에서는 개인의 음색을 로컬에서 유지하고, 가벼운 스타일-LoRA만 서버로 전송합니다. 또한, 협업 필터링에서 영감을 받은 집계 방법을 통해 스타일이 유사한 클라이언트 간 학습을 통해 맞춤형 모델을 생성합니다. 실험 결과, Fed-PISA는 스타일 표현력, 자연스러움, 화자 유사성을 향상시키며, 최소한의 통신 비용으로 기존 연합 학습 기반을 능가하는 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Fed-PISA는 제한된 데이터로 텍스트에서 개인화된 음성을 생성하는 음성 복제를 위한 연합 학습 프레임워크입니다.
- 2. Fed-PISA는 Low-Rank Adaptation (LoRA) 메커니즘을 사용하여 통신 비용을 최소화하고, 개인 ID-LoRA를 통해 로컬에서 화자의 음색을 유지합니다.
- 3. 스타일 이질성을 활용하기 위해 협업 필터링에서 영감을 받은 집계 방법을 도입하여 스타일이 유사한 피어로부터 학습하여 각 클라이언트에 맞춤형 모델을 생성합니다.
- 4. 실험 결과, Fed-PISA는 스타일 표현력, 자연스러움 및 화자 유사성을 개선하여 표준 연합 학습 기준을 능가합니다.


---

*Generated on 2025-09-23 09:25:52*