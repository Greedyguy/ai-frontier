<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:59:21.083932",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Chart Understanding",
    "CHART NOISe Dataset",
    "Reverse Inconsistency",
    "Occlusion Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Chart Understanding": 0.8,
    "CHART NOISe Dataset": 0.78,
    "Reverse Inconsistency": 0.72,
    "Occlusion Detection": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision language models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision Language Model"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus on chart understanding and are a trending concept.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "chart understanding",
        "canonical": "Chart Understanding",
        "aliases": [
          "chart analysis",
          "chart interpretation"
        ],
        "category": "unique_technical",
        "rationale": "Chart Understanding is a specific application area that connects to broader concepts in data visualization and interpretation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "CHART NOISe",
        "canonical": "CHART NOISe Dataset",
        "aliases": [
          "Chart Hallucinations, Answers, and Reasoning Testing on Noisy and Occluded Input Selections"
        ],
        "category": "unique_technical",
        "rationale": "The CHART NOISe Dataset is a novel contribution that offers a new testbed for evaluating VLMs, enhancing the paper's impact.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "reverse inconsistency",
        "canonical": "Reverse Inconsistency",
        "aliases": [
          "prompt reverse inconsistency"
        ],
        "category": "unique_technical",
        "rationale": "Reverse Inconsistency is a novel concept introduced in the paper, highlighting a specific vulnerability in VLMs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "occlusion detection",
        "canonical": "Occlusion Detection",
        "aliases": [
          "occlusion identification"
        ],
        "category": "specific_connectable",
        "rationale": "Occlusion Detection is a key mitigation strategy discussed, linking to broader themes in computer vision.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "corruption",
      "hallucinations",
      "performance drops"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision language models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "chart understanding",
      "resolved_canonical": "Chart Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "CHART NOISe",
      "resolved_canonical": "CHART NOISe Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "reverse inconsistency",
      "resolved_canonical": "Reverse Inconsistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "occlusion detection",
      "resolved_canonical": "Occlusion Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Losing the Plot: How VLM responses degrade on imperfect charts

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18425.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18425](https://arxiv.org/abs/2509.18425)

## 🔗 유사한 논문
- [[2025-09-23/ChartHal_ A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding_20250923|ChartHal: A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding]] (90.2% similar)
- [[2025-09-23/Unmasking Deceptive Visuals_ Benchmarking Multimodal Large Language Models on Misleading Chart Question Answering_20250923|Unmasking Deceptive Visuals: Benchmarking Multimodal Large Language Models on Misleading Chart Question Answering]] (87.9% similar)
- [[2025-09-19/METAL_ A Multi-Agent Framework for Chart Generation with Test-Time Scaling_20250919|METAL: A Multi-Agent Framework for Chart Generation with Test-Time Scaling]] (83.6% similar)
- [[2025-09-23/Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models_20250923|Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models]] (83.1% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Occlusion Detection|Occlusion Detection]]
**⚡ Unique Technical**: [[keywords/Chart Understanding|Chart Understanding]], [[keywords/CHART NOISe Dataset|CHART NOISe Dataset]], [[keywords/Reverse Inconsistency|Reverse Inconsistency]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18425v1 Announce Type: new 
Abstract: Vision language models (VLMs) show strong results on chart understanding, yet existing benchmarks assume clean figures and fact based queries. Real world charts often contain distortions and demand reasoning beyond simple matching. We evaluate ChatGPT 4o, Claude Sonnet 4, and Gemini 2.5 Pro, finding sharp performance drops under corruption or occlusion, with hallucinations such as value fabrication, trend misinterpretation, and entity confusion becoming more frequent. Models remain overconfident in degraded settings, generating plausible but unsupported explanations.
  To address this gap, we introduce CHART NOISe(Chart Hallucinations, Answers, and Reasoning Testing on Noisy and Occluded Input Selections), a dataset combining chart corruptions, occlusions, and exam style multiple choice questions inspired by Korea's CSAT English section. A key innovation is prompt reverse inconsistency, where models contradict themselves when asked to confirm versus deny the same statement. Our contributions are threefold: (1) benchmarking state of the art VLMs, exposing systematic vulnerabilities in chart reasoning; (2) releasing CHART NOISe, the first dataset unifying corruption, occlusion, and reverse inconsistency; and (3) proposing baseline mitigation strategies such as quality filtering and occlusion detection. Together, these efforts establish a rigorous testbed for advancing robustness and reliability in chart understanding.

## 📝 요약

이 논문은 시각 언어 모델(VLMs)이 차트 이해에서 강력한 성능을 보이지만, 실제 차트의 왜곡과 복잡한 추론 요구에 취약하다는 점을 지적합니다. 연구는 ChatGPT 4o, Claude Sonnet 4, Gemini 2.5 Pro 모델을 평가하여, 차트가 손상되거나 가려질 경우 성능이 급격히 저하되고, 값 조작, 추세 오해, 개체 혼동 등의 오류가 증가함을 발견했습니다. 이를 해결하기 위해, 차트 왜곡과 가림, 한국 수능 영어 섹션을 본뜬 문제를 포함한 CHART NOISe 데이터셋을 소개합니다. 주요 기여는 (1) 최신 VLMs의 체계적 취약점 노출, (2) CHART NOISe 데이터셋 공개, (3) 품질 필터링 및 가림 탐지와 같은 완화 전략 제안입니다. 이 연구는 차트 이해의 견고성과 신뢰성을 향상시키기 위한 엄격한 테스트 환경을 제공합니다.

## 🎯 주요 포인트

- 1. 기존의 비전 언어 모델(VLM)은 깨끗한 차트와 사실 기반 쿼리에 대해서는 강력한 성능을 보이지만, 왜곡된 차트나 복잡한 추론이 필요한 상황에서는 성능이 급격히 저하됩니다.
- 2. CHART NOISe라는 새로운 데이터셋을 도입하여 차트의 왜곡, 가림, 그리고 한국 수능 영어 섹션에서 영감을 받은 시험 스타일의 다지선다형 질문을 결합했습니다.
- 3. 모델들이 동일한 명제를 확인하거나 부정할 때 스스로 모순되는 '프롬프트 역불일치'라는 개념을 도입하여 모델의 취약점을 드러냈습니다.
- 4. CHART NOISe는 차트 이해의 강건성과 신뢰성을 향상시키기 위한 엄격한 테스트베드를 제공하며, 품질 필터링 및 가림 탐지와 같은 기본 완화 전략을 제안합니다.
- 5. 연구는 최신 VLM의 체계적인 취약성을 드러내고, 차트 이해에서의 강건성과 신뢰성을 향상시키기 위한 기초를 마련합니다.


---

*Generated on 2025-09-24 15:59:21*