---
keywords:
  - Multimodal Learning
  - Group Activity Detection
  - Transformer
  - Multimodal Dual-Alignment Fusion
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16054
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:19:10.238755",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Group Activity Detection",
    "Transformer",
    "Multimodal Dual-Alignment Fusion"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.78,
    "Group Activity Detection": 0.77,
    "Transformer": 0.7,
    "Multimodal Dual-Alignment Fusion": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Model",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLM"
        ],
        "category": "specific_connectable",
        "rationale": "Connects with the trend of integrating multiple modalities in language models, enhancing cross-domain insights.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Group Activity Detection",
        "canonical": "Group Activity Detection",
        "aliases": [
          "GAD"
        ],
        "category": "unique_technical",
        "rationale": "A specialized task within computer vision, offering a unique link to activity recognition research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Transformer Networks",
        "canonical": "Transformer",
        "aliases": [
          "Transformer Networks"
        ],
        "category": "broad_technical",
        "rationale": "A foundational architecture in modern deep learning, facilitating connections across various applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multimodal Dual-Alignment Fusion",
        "canonical": "Multimodal Dual-Alignment Fusion",
        "aliases": [
          "MDAF"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel integration technique for aligning multimodal data, enhancing model performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "video sequences",
      "visual features"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Group Activity Detection",
      "resolved_canonical": "Group Activity Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Transformer Networks",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multimodal Dual-Alignment Fusion",
      "resolved_canonical": "Multimodal Dual-Alignment Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Language-Instructed Reasoning for Group Activity Detection via Multimodal Large Language Model

**Korean Title:** 언어 지시적 추론을 통한 그룹 활동 탐지: 다중 모달 대형 언어 모델을 활용하여

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16054.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16054](https://arxiv.org/abs/2509.16054)

## 🔗 유사한 논문
- [[2025-09-19/Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (83.1% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.9% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (82.2% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (81.4% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Group Activity Detection|Group Activity Detection]], [[keywords/Multimodal Dual-Alignment Fusion|Multimodal Dual-Alignment Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16054v1 Announce Type: new 
Abstract: Group activity detection (GAD) aims to simultaneously identify group members and categorize their collective activities within video sequences. Existing deep learning-based methods develop specialized architectures (e.g., transformer networks) to model the dynamics of individual roles and semantic dependencies between individuals and groups. However, they rely solely on implicit pattern recognition from visual features and struggle with contextual reasoning and explainability. In this work, we propose LIR-GAD, a novel framework of language-instructed reasoning for GAD via Multimodal Large Language Model (MLLM). Our approach expand the original vocabulary of MLLM by introducing an activity-level  token and multiple cluster-specific  tokens. We process video frames alongside two specially designed tokens and language instructions, which are then integrated into the MLLM. The pretrained commonsense knowledge embedded in the MLLM enables the  token and  tokens to effectively capture the semantic information of collective activities and learn distinct representational features of different groups, respectively. Also, we introduce a multi-label classification loss to further enhance the  token's ability to learn discriminative semantic representations. Then, we design a Multimodal Dual-Alignment Fusion (MDAF) module that integrates MLLM's hidden embeddings corresponding to the designed tokens with visual features, significantly enhancing the performance of GAD. Both quantitative and qualitative experiments demonstrate the superior performance of our proposed method in GAD taks.

## 🔍 Abstract (한글 번역)

arXiv:2509.16054v1 발표 유형: 신규  
초록: 그룹 활동 감지(GAD)는 비디오 시퀀스 내에서 그룹 구성원을 식별하고 그들의 집단 활동을 분류하는 것을 목표로 합니다. 기존의 딥러닝 기반 방법들은 개별 역할의 역학과 개인과 그룹 간의 의미적 의존성을 모델링하기 위해 특화된 아키텍처(예: 트랜스포머 네트워크)를 개발합니다. 그러나 이러한 방법들은 시각적 특징에서 암묵적인 패턴 인식에만 의존하며, 맥락적 추론과 설명 가능성에서 어려움을 겪습니다. 본 연구에서는 멀티모달 대형 언어 모델(MLLM)을 통한 GAD를 위한 언어 지시 추론의 새로운 프레임워크인 LIR-GAD를 제안합니다. 우리의 접근법은 활동 수준 토큰과 여러 클러스터 특정 토큰을 도입하여 MLLM의 원래 어휘를 확장합니다. 우리는 비디오 프레임을 두 개의 특별히 설계된 토큰과 언어 지시와 함께 처리하고, 이를 MLLM에 통합합니다. MLLM에 내장된 사전 학습된 상식 지식은 토큰과 토큰들이 집단 활동의 의미 정보를 효과적으로 포착하고, 각각 다른 그룹의 독특한 표현 특징을 학습할 수 있게 합니다. 또한, 우리는 토큰의 차별적인 의미 표현 학습 능력을 더욱 향상시키기 위해 다중 레이블 분류 손실을 도입합니다. 그런 다음, 설계된 토큰에 해당하는 MLLM의 숨겨진 임베딩을 시각적 특징과 통합하는 멀티모달 이중 정렬 융합(MDAF) 모듈을 설계하여 GAD의 성능을 크게 향상시킵니다. 정량적 및 정성적 실험 모두 우리의 제안된 방법이 GAD 작업에서 우수한 성능을 보임을 입증합니다.

## 📝 요약

이 논문에서는 비디오 시퀀스에서 그룹 활동을 감지하는 새로운 프레임워크인 LIR-GAD를 제안합니다. 기존의 딥러닝 기반 방법들이 시각적 특징에 의존하는 반면, LIR-GAD는 다중모달 대형 언어 모델(MLLM)을 활용하여 언어 지시를 통한 추론을 수행합니다. MLLM의 원래 어휘를 확장하여 활동 수준의 토큰과 여러 클러스터 특정 토큰을 도입하고, 비디오 프레임과 함께 이 토큰들을 처리하여 집단 활동의 의미 정보를 효과적으로 포착합니다. 또한, 다중 레이블 분류 손실을 도입하여 토큰의 판별적 의미 표현 학습 능력을 강화합니다. MLLM의 숨겨진 임베딩과 시각적 특징을 통합하는 다중모달 이중 정렬 융합(MDAF) 모듈을 설계하여 GAD의 성능을 크게 향상시켰습니다. 실험 결과, 제안된 방법이 그룹 활동 감지에서 뛰어난 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. LIR-GAD는 비디오 시퀀스 내에서 그룹 활동을 감지하기 위해 다중 모달 대형 언어 모델(MLLM)을 활용한 새로운 프레임워크입니다.
- 2. MLLM의 원래 어휘를 확장하여 활동 수준 토큰과 여러 클러스터별 토큰을 도입하여 집단 활동의 의미 정보를 효과적으로 포착합니다.
- 3. 다중 레이블 분류 손실을 도입하여 토큰의 차별적 의미 표현 학습 능력을 강화합니다.
- 4. MDAF 모듈은 설계된 토큰과 시각적 특징을 통합하여 GAD의 성능을 크게 향상시킵니다.
- 5. 정량적 및 정성적 실험 결과, 제안된 방법이 GAD 작업에서 우수한 성능을 보임을 입증합니다.


---

*Generated on 2025-09-23 12:19:10*