---
keywords:
  - Two-Stage Phoneme-Centric Architecture
  - Code-Switching
  - Phoneme Adaptation
  - Vietnamese-English Speech Recognition
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.05983
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:26:12.929997",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Two-Stage Phoneme-Centric Architecture",
    "Code-Switching",
    "Phoneme Adaptation",
    "Vietnamese-English Speech Recognition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Two-Stage Phoneme-Centric Architecture": 0.78,
    "Code-Switching": 0.82,
    "Phoneme Adaptation": 0.77,
    "Vietnamese-English Speech Recognition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Two-Stage Phoneme-Centric model",
        "canonical": "Two-Stage Phoneme-Centric Architecture",
        "aliases": [
          "TSPC"
        ],
        "category": "unique_technical",
        "rationale": "This novel architecture is central to the paper's contribution and is specific to the Vietnamese-English code-switching context.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "code-switching",
        "canonical": "Code-Switching",
        "aliases": [
          "CS"
        ],
        "category": "specific_connectable",
        "rationale": "Code-switching is a critical aspect of the study and connects to broader linguistic and ASR research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "phoneme adaptation",
        "canonical": "Phoneme Adaptation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Phoneme adaptation is a key mechanism in the proposed model, relevant for ASR improvements.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Vietnamese-English speech recognition",
        "canonical": "Vietnamese-English Speech Recognition",
        "aliases": [
          "Vietnamese-English ASR"
        ],
        "category": "unique_technical",
        "rationale": "This is the specific application domain of the study, highlighting its unique focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "general Auto-Speech Recognition",
      "existing methods",
      "experimental results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Two-Stage Phoneme-Centric model",
      "resolved_canonical": "Two-Stage Phoneme-Centric Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "code-switching",
      "resolved_canonical": "Code-Switching",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "phoneme adaptation",
      "resolved_canonical": "Phoneme Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Vietnamese-English speech recognition",
      "resolved_canonical": "Vietnamese-English Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# TSPC: A Two-Stage Phoneme-Centric Architecture for code-switching Vietnamese-English Speech Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.05983.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.05983](https://arxiv.org/abs/2509.05983)

## 🔗 유사한 논문
- [[2025-09-23/Speech Recognition on TV Series with Video-guided Post-ASR Correction_20250923|Speech Recognition on TV Series with Video-guided Post-ASR Correction]] (80.5% similar)
- [[2025-09-23/MaskVCT_ Masked Voice Codec Transformer for Zero-Shot Voice Conversion With Increased Controllability via Multiple Guidances_20250923|MaskVCT: Masked Voice Codec Transformer for Zero-Shot Voice Conversion With Increased Controllability via Multiple Guidances]] (80.0% similar)
- [[2025-09-23/TMD-TTS_ A Unified Tibetan Multi-Dialect Text-to-Speech Synthesis for \"U-Tsang, Amdo and Kham Speech Dataset Generation_20250923|TMD-TTS: A Unified Tibetan Multi-Dialect Text-to-Speech Synthesis for \"U-Tsang, Amdo and Kham Speech Dataset Generation]] (79.8% similar)
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (79.0% similar)
- [[2025-09-22/Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning_20250922|Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Code-Switching|Code-Switching]], [[keywords/Phoneme Adaptation|Phoneme Adaptation]]
**⚡ Unique Technical**: [[keywords/Two-Stage Phoneme-Centric Architecture|Two-Stage Phoneme-Centric Architecture]], [[keywords/Vietnamese-English Speech Recognition|Vietnamese-English Speech Recognition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.05983v3 Announce Type: replace-cross 
Abstract: Code-switching (CS) presents a significant challenge for general Auto-Speech Recognition (ASR) systems. Existing methods often fail to capture the subtle phonological shifts inherent in CS scenarios. The challenge is particularly difficult for language pairs like Vietnamese and English, where both distinct phonological features and the ambiguity arising from similar sound recognition are present. In this paper, we propose a novel architecture for Vietnamese-English CS ASR, a Two-Stage Phoneme-Centric model (TSPC). The TSPC employs a phoneme-centric approach, built upon an extended Vietnamese phoneme set as an intermediate representation to facilitate mixed-lingual modeling. Experimental results demonstrate that TSPC consistently outperforms existing baselines, including PhoWhisper-base, in Vietnamese-English CS ASR, achieving a significantly lower word error rate of 19.9% with reduced training resources. Furthermore, the phonetic-based two-stage architecture enables phoneme adaptation and language conversion to enhance ASR performance in complex CS Vietnamese-English ASR scenarios

## 📝 요약

이 논문은 베트남어-영어 코드 스위칭(CS) 상황에서 자동 음성 인식(ASR)의 어려움을 해결하기 위해 새로운 이단계 음소 중심 모델(TSPC)을 제안합니다. TSPC는 확장된 베트남어 음소 집합을 중간 표현으로 사용하여 혼합 언어 모델링을 촉진합니다. 실험 결과, TSPC는 기존의 PhoWhisper-base 등과 비교하여 베트남어-영어 CS ASR에서 일관되게 더 낮은 단어 오류율(19.9%)을 기록하며 성능을 향상시켰습니다. 이 모델은 음소 적응과 언어 변환을 통해 복잡한 CS 시나리오에서 ASR 성능을 강화합니다.

## 🎯 주요 포인트

- 1. 코드 스위칭(CS)은 일반적인 자동 음성 인식(ASR) 시스템에 큰 도전 과제를 제시합니다.
- 2. 베트남어와 영어와 같은 언어 쌍의 CS 시나리오에서 미묘한 음운 변화를 포착하는 것이 기존 방법으로는 어렵습니다.
- 3. 본 논문에서는 베트남어-영어 CS ASR를 위한 새로운 아키텍처인 Two-Stage Phoneme-Centric 모델(TSPC)을 제안합니다.
- 4. TSPC는 확장된 베트남어 음소 세트를 중간 표현으로 사용하여 혼합 언어 모델링을 촉진합니다.
- 5. 실험 결과, TSPC는 기존의 PhoWhisper-base를 포함한 기준 모델들보다 우수한 성능을 보이며, 19.9%의 낮은 단어 오류율을 달성했습니다.


---

*Generated on 2025-09-24 01:26:12*