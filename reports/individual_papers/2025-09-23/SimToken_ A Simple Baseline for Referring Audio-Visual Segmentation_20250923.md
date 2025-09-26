---
keywords:
  - Referring Audio-Visual Segmentation
  - Multimodal Learning
  - Segment Anything Model
  - Vision-Language Model
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17537
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:55:01.732909",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Referring Audio-Visual Segmentation",
    "Multimodal Learning",
    "Segment Anything Model",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Referring Audio-Visual Segmentation": 0.8,
    "Multimodal Learning": 0.85,
    "Segment Anything Model": 0.78,
    "Vision-Language Model": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Referring Audio-Visual Segmentation",
        "canonical": "Referring Audio-Visual Segmentation",
        "aliases": [
          "Ref-AVS"
        ],
        "category": "unique_technical",
        "rationale": "This is the core task discussed in the paper, offering a unique intersection of audio, visual, and text modalities.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Large Language Model",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLM"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the trending concept of integrating multiple modalities in learning models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Segment Anything Model",
        "canonical": "Segment Anything Model",
        "aliases": [
          "SAM"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific model used in the paper, crucial for understanding the segmentation process.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Highlights the integration of visual and language data, a key aspect of the paper's methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "cross-modal reasoning",
      "fine-grained object localization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Referring Audio-Visual Segmentation",
      "resolved_canonical": "Referring Audio-Visual Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Large Language Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Segment Anything Model",
      "resolved_canonical": "Segment Anything Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SimToken: A Simple Baseline for Referring Audio-Visual Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17537.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17537](https://arxiv.org/abs/2509.17537)

## 🔗 유사한 논문
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (84.1% similar)
- [[2025-09-23/The 1st Solution for 7th LSVOS RVOS Track_ SaSaSa2VA_20250923|The 1st Solution for 7th LSVOS RVOS Track: SaSaSa2VA]] (83.0% similar)
- [[2025-09-23/BiPrompt-SAM_ Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts_20250923|BiPrompt-SAM: Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts]] (82.9% similar)
- [[2025-09-23/SAMSON_ 3rd Place Solution of LSVOS 2025 VOS Challenge_20250923|SAMSON: 3rd Place Solution of LSVOS 2025 VOS Challenge]] (82.3% similar)
- [[2025-09-23/SAM-DCE_ Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation_20250923|SAM-DCE: Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Referring Audio-Visual Segmentation|Referring Audio-Visual Segmentation]], [[keywords/Segment Anything Model|Segment Anything Model]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17537v1 Announce Type: new 
Abstract: Referring Audio-Visual Segmentation (Ref-AVS) aims to segment specific objects in videos based on natural language expressions involving audio, vision, and text information. This task poses significant challenges in cross-modal reasoning and fine-grained object localization. In this paper, we propose a simple framework, SimToken, that integrates a multimodal large language model (MLLM) with the Segment Anything Model (SAM). The MLLM is guided to generate a special semantic token representing the referred object. This compact token, enriched with contextual information from all modalities, acts as a prompt to guide SAM to segment objectsacross video frames. To further improve semantic learning, we introduce a novel target-consistent semantic alignment loss that aligns token embeddings from different expressions but referring to the same object. Experiments on the Ref-AVS benchmark demonstrate that our approach achieves superior performance compared to existing methods.Code will be available at https://github.com/DianJin-HFUT/SimToken

## 📝 요약

Ref-AVS는 자연어 표현을 기반으로 비디오에서 특정 객체를 분할하는 작업으로, 교차 모달 추론과 세밀한 객체 위치 지정에 어려움이 있습니다. 본 논문에서는 SimToken이라는 간단한 프레임워크를 제안합니다. 이는 다중 모달 대형 언어 모델(MLLM)과 Segment Anything Model(SAM)을 통합하여, MLLM이 참조 객체를 나타내는 특별한 의미 토큰을 생성하도록 합니다. 이 토큰은 모든 모달의 맥락 정보를 포함하여 SAM이 비디오 프레임 전반에 걸쳐 객체를 분할하도록 안내합니다. 또한, 동일 객체를 참조하는 표현의 토큰 임베딩을 정렬하는 새로운 목표 일관성 의미 정렬 손실을 도입하여 의미 학습을 개선합니다. Ref-AVS 벤치마크 실험 결과, 제안된 방법이 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. Ref-AVS는 오디오, 비전, 텍스트 정보를 포함한 자연어 표현을 기반으로 비디오에서 특정 객체를 세분화하는 작업이다.
- 2. SimToken은 다중 모달 대형 언어 모델(MLLM)과 Segment Anything Model(SAM)을 통합한 간단한 프레임워크를 제안한다.
- 3. MLLM은 참조 객체를 나타내는 특수한 의미 토큰을 생성하도록 유도되며, 이 토큰은 SAM이 비디오 프레임 전반에 걸쳐 객체를 세분화하도록 안내한다.
- 4. 새로운 대상 일관성 의미 정렬 손실을 도입하여 서로 다른 표현에서 동일한 객체를 참조하는 토큰 임베딩을 정렬하여 의미 학습을 개선한다.
- 5. Ref-AVS 벤치마크 실험에서 제안된 접근 방식이 기존 방법보다 우수한 성능을 달성한다.


---

*Generated on 2025-09-24 04:55:01*