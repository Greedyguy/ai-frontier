<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:48:08.957438",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Vision-Language Model",
    "Zero-Shot Learning",
    "Check Fraud Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Vision-Language Model": 0.84,
    "Zero-Shot Learning": 0.83,
    "Check Fraud Detection": 0.78
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
        "rationale": "Multimodal Learning is crucial for integrating vision and language, central to the paper's framework.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are pivotal for the zero-shot detection capability discussed in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.84
      },
      {
        "surface": "Zero-Shot Detection",
        "canonical": "Zero-Shot Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a key technique enabling the model's deployment without additional training.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.77,
        "link_intent_score": 0.83
      },
      {
        "surface": "Check Fraud Detection",
        "canonical": "Check Fraud Detection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a unique application focus of the paper, linking to financial security topics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "field detection",
      "object detection",
      "dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "Zero-Shot Detection",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.77,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Check Fraud Detection",
      "resolved_canonical": "Check Fraud Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Check Field Detection Agent (CFD-Agent) using Multimodal Large Language and Vision Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18405.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18405](https://arxiv.org/abs/2509.18405)

## 🔗 유사한 논문
- [[2025-09-22/VLA-Mark_ A cross modal watermark for large vision-language alignment model_20250922|VLA-Mark: A cross modal watermark for large vision-language alignment model]] (82.0% similar)
- [[2025-09-23/Quality Assessment of Tabular Data using Large Language Models and Code Generation_20250923|Quality Assessment of Tabular Data using Large Language Models and Code Generation]] (81.9% similar)
- [[2025-09-23/Advanced Financial Reasoning at Scale_ A Comprehensive Evaluation of Large Language Models on CFA Level III_20250923|Advanced Financial Reasoning at Scale: A Comprehensive Evaluation of Large Language Models on CFA Level III]] (81.6% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (81.4% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Check Fraud Detection|Check Fraud Detection]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18405v1 Announce Type: cross 
Abstract: Checks remain a foundational instrument in the financial ecosystem, facilitating substantial transaction volumes across institutions. However, their continued use also renders them a persistent target for fraud, underscoring the importance of robust check fraud detection mechanisms. At the core of such systems lies the accurate identification and localization of critical fields, such as the signature, magnetic ink character recognition (MICR) line, courtesy amount, legal amount, payee, and payer, which are essential for subsequent verification against reference checks belonging to the same customer. This field-level detection is traditionally dependent on object detection models trained on large, diverse, and meticulously labeled datasets, a resource that is scarce due to proprietary and privacy concerns. In this paper, we introduce a novel, training-free framework for automated check field detection, leveraging the power of a vision language model (VLM) in conjunction with a multimodal large language model (MLLM). Our approach enables zero-shot detection of check components, significantly lowering the barrier to deployment in real-world financial settings. Quantitative evaluation of our model on a hand-curated dataset of 110 checks spanning multiple formats and layouts demonstrates strong performance and generalization capability. Furthermore, this framework can serve as a bootstrap mechanism for generating high-quality labeled datasets, enabling the development of specialized real-time object detection models tailored to institutional needs.

## 📝 요약

이 논문은 금융 시스템에서 중요한 수단인 수표의 사기 방지를 위한 새로운 방법론을 제안합니다. 전통적으로 수표의 중요한 필드들을 정확히 식별하기 위해 대규모의 라벨링된 데이터셋을 사용하는 객체 탐지 모델이 필요하지만, 데이터 부족 문제를 해결하기 위해 훈련이 필요 없는 새로운 프레임워크를 도입했습니다. 이 프레임워크는 비전 언어 모델(VLM)과 다중 모달 대형 언어 모델(MLLM)을 활용하여 수표 구성 요소를 제로샷으로 탐지할 수 있습니다. 110개의 다양한 수표 형식을 포함한 데이터셋에서의 실험 결과, 이 방법론은 강력한 성능과 일반화 능력을 보여주었으며, 고품질의 라벨링 데이터셋 생성에도 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 금융 생태계에서 수표는 여전히 중요한 거래 수단이지만, 사기 위험이 있어 강력한 사기 탐지 메커니즘이 필요합니다.
- 2. 수표의 중요한 필드(서명, MICR 라인, 금액 등)를 정확히 식별하는 것이 사기 탐지 시스템의 핵심입니다.
- 3. 기존의 필드 탐지는 대규모로 라벨링된 데이터셋에 의존하지만, 이는 프라이버시 문제로 인해 부족합니다.
- 4. 본 논문은 비전 언어 모델(VLM)과 다중모달 대형 언어 모델(MLLM)을 활용한 새로운 훈련 불필요 자동 수표 필드 탐지 프레임워크를 제안합니다.
- 5. 제안된 방법은 수표 구성 요소의 제로샷 탐지를 가능하게 하여 실제 금융 환경에서의 적용 장벽을 낮춥니다.


---

*Generated on 2025-09-24 13:48:08*