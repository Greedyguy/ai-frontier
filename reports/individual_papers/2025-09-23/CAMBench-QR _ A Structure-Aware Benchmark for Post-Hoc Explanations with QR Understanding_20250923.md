---
keywords:
  - CAMBench-QR
  - QR Code
  - LayerCAM
  - Zero-Shot Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16745
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:32:37.714216",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "CAMBench-QR",
    "QR Code",
    "LayerCAM",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "CAMBench-QR": 0.8,
    "QR Code": 0.78,
    "LayerCAM": 0.77,
    "Zero-Shot Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CAMBench-QR",
        "canonical": "CAMBench-QR",
        "aliases": [
          "CAMBench",
          "QR Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel benchmark specifically for evaluating structure-aware visual explanations.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "QR codes",
        "canonical": "QR Code",
        "aliases": [
          "Quick Response Code"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the benchmark's structure-aware evaluation, linking to existing QR code studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "LayerCAM",
        "canonical": "LayerCAM",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A representative CAM method evaluated in the benchmark, relevant for visual explanation studies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Zero-Shot",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Describes a practical regime under which the benchmark is evaluated, relevant for transfer learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "visual explanations",
      "structure-aware",
      "benchmark"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CAMBench-QR",
      "resolved_canonical": "CAMBench-QR",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "QR codes",
      "resolved_canonical": "QR Code",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LayerCAM",
      "resolved_canonical": "LayerCAM",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Zero-Shot",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# CAMBench-QR : A Structure-Aware Benchmark for Post-Hoc Explanations with QR Understanding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16745.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16745](https://arxiv.org/abs/2509.16745)

## 🔗 유사한 논문
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (79.3% similar)
- [[2025-09-23/ProtoVQA_ An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering_20250923|ProtoVQA: An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering]] (79.1% similar)
- [[2025-09-22/CLEAR_ A Clinically-Grounded Tabular Framework for Radiology Report Evaluation_20250922|CLEAR: A Clinically-Grounded Tabular Framework for Radiology Report Evaluation]] (78.8% similar)
- [[2025-09-22/EyePCR_ A Comprehensive Benchmark for Fine-Grained Perception, Knowledge Comprehension and Clinical Reasoning in Ophthalmic Surgery_20250922|EyePCR: A Comprehensive Benchmark for Fine-Grained Perception, Knowledge Comprehension and Clinical Reasoning in Ophthalmic Surgery]] (78.7% similar)
- [[2025-09-22/MEC-Quant_ Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training_20250922|MEC-Quant: Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training]] (78.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/QR Code|QR Code]], [[keywords/LayerCAM|LayerCAM]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/CAMBench-QR|CAMBench-QR]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16745v1 Announce Type: cross 
Abstract: Visual explanations are often plausible but not structurally faithful. We introduce CAMBench-QR, a structure-aware benchmark that leverages the canonical geometry of QR codes (finder patterns, timing lines, module grid) to test whether CAM methods place saliency on requisite substructures while avoiding background. CAMBench-QR synthesizes QR/non-QR data with exact masks and controlled distortions, and reports structure-aware metrics (Finder/Timing Mass Ratios, Background Leakage, coverage AUCs, Distance-to-Structure) alongside causal occlusion, insertion/deletion faithfulness, robustness, and latency. We benchmark representative, efficient CAMs (LayerCAM, EigenGrad-CAM, XGrad-CAM) under two practical regimes of zero-shot and last-block fine-tuning. The benchmark, metrics, and training recipes provide a simple, reproducible yardstick for structure-aware evaluation of visual explanations. Hence we propose that CAMBENCH-QR can be used as a litmus test of whether visual explanations are truly structure-aware.

## 📝 요약

CAMBench-QR은 QR 코드의 구조적 요소를 활용하여 시각적 설명의 구조적 충실성을 평가하는 벤치마크입니다. 이 벤치마크는 QR 코드의 패턴과 그리드를 이용해 CAM 방법이 필요한 하위 구조에 주목하는지 평가합니다. CAMBench-QR은 정확한 마스크와 제어된 왜곡을 통해 QR/비QR 데이터를 합성하고, 구조 인식 지표와 인과적 폐색, 삽입/삭제 충실성, 강건성, 지연 시간을 보고합니다. LayerCAM, EigenGrad-CAM, XGrad-CAM 등의 CAM을 무샷과 마지막 블록 미세 조정 환경에서 평가하여 시각적 설명의 구조 인식 평가를 위한 기준을 제공합니다. CAMBench-QR은 시각적 설명의 구조 인식 여부를 평가하는 리트머스 시험지로 제안됩니다.

## 🎯 주요 포인트

- 1. CAMBench-QR는 QR 코드의 구조적 요소를 활용하여 시각적 설명의 구조적 충실성을 평가하는 벤치마크입니다.
- 2. 이 벤치마크는 QR/비QR 데이터를 정확한 마스크와 제어된 왜곡으로 합성하여 구조 인식 메트릭을 제공합니다.
- 3. 대표적인 CAM 방법들(LayerCAM, EigenGrad-CAM, XGrad-CAM)을 다양한 실용적 조건에서 벤치마크합니다.
- 4. CAMBench-QR은 시각적 설명의 구조 인식 평가를 위한 간단하고 재현 가능한 기준을 제공합니다.
- 5. CAMBench-QR은 시각적 설명이 구조를 인식하는지를 평가하는 시금석으로 사용될 수 있습니다.


---

*Generated on 2025-09-23 23:32:37*