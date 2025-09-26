---
keywords:
  - Large Language Model
  - Calibrating LLM Confidence by Probing Perturbed Representation Stability
  - Adversarial Perturbations
  - Expected Calibration Error
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2505.21772
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:47:10.552737",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
    "Adversarial Perturbations",
    "Expected Calibration Error"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Calibrating LLM Confidence by Probing Perturbed Representation Stability": 0.8,
    "Adversarial Perturbations": 0.78,
    "Expected Calibration Error": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving model confidence, linking to broader discussions on LLMs.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "CCPS",
        "canonical": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
        "aliases": [
          "CCPS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method specific to this research, providing a unique link for further exploration.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adversarial Perturbations",
        "canonical": "Adversarial Perturbations",
        "aliases": [
          "Adversarial Attacks"
        ],
        "category": "specific_connectable",
        "rationale": "Key technique used in the paper, relevant to discussions on model robustness and security.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Expected Calibration Error",
        "canonical": "Expected Calibration Error",
        "aliases": [
          "ECE"
        ],
        "category": "specific_connectable",
        "rationale": "A critical metric for evaluating model calibration, linking to performance assessment discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
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
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "CCPS",
      "resolved_canonical": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adversarial Perturbations",
      "resolved_canonical": "Adversarial Perturbations",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Expected Calibration Error",
      "resolved_canonical": "Expected Calibration Error",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Calibrating LLM Confidence by Probing Perturbed Representation Stability

**Korean Title:** LLM 신뢰도 보정: 변형된 표현의 안정성 탐색

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.21772.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2505.21772](https://arxiv.org/abs/2505.21772)

## 🔗 유사한 논문
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (87.1% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (86.3% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (86.3% similar)
- [[2025-09-18/Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies_20250918|Calibrating LLMs for Text-to-SQL Parsing by Leveraging Sub-clause Frequencies]] (86.2% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO: A Framework for Confidence-Aware Routing of Large Language Models]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Adversarial Perturbations|Adversarial Perturbations]], [[keywords/Expected Calibration Error|Expected Calibration Error]]
**⚡ Unique Technical**: [[keywords/Calibrating LLM Confidence by Probing Perturbed Representation Stability|Calibrating LLM Confidence by Probing Perturbed Representation Stability]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.21772v2 Announce Type: replace 
Abstract: Miscalibration in Large Language Models (LLMs) undermines their reliability, highlighting the need for accurate confidence estimation. We introduce CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability), a novel method analyzing internal representational stability in LLMs. CCPS applies targeted adversarial perturbations to final hidden states, extracts features reflecting the model's response to these perturbations, and uses a lightweight classifier to predict answer correctness. CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats. Our results show that CCPS significantly outperforms current approaches. Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points, all relative to the strongest prior method. CCPS delivers an efficient, broadly applicable, and more accurate solution for estimating LLM confidence, thereby improving their trustworthiness.

## 🔍 Abstract (한글 번역)

arXiv:2505.21772v2 발표 유형: 교체  
초록: 대형 언어 모델(LLM)의 잘못된 보정은 그 신뢰성을 저해하며, 정확한 신뢰도 추정의 필요성을 강조합니다. 우리는 LLM의 내부 표현 안정성을 분석하는 새로운 방법인 CCPS(Calibrating LLM Confidence by Probing Perturbed Representation Stability)를 소개합니다. CCPS는 최종 은닉 상태에 목표 지향적 적대적 변화를 적용하고, 이러한 변화에 대한 모델의 반응을 반영하는 특징을 추출하며, 경량의 분류기를 사용하여 답변의 정확성을 예측합니다. CCPS는 MMLU와 MMLU-Pro 벤치마크를 사용하여 Llama, Qwen, Mistral 아키텍처를 포함한 8B에서 32B 매개변수의 LLM에서 다지선다형 및 개방형 형식으로 평가되었습니다. 우리의 결과는 CCPS가 현재의 접근법을 현저히 능가함을 보여줍니다. 네 개의 LLM과 세 가지 MMLU 변형 전반에 걸쳐, CCPS는 예상 보정 오류를 약 55%, 브라이어 점수를 21% 감소시키고, 정확도를 5% 포인트, 정밀도-재현율 곡선 아래 면적을 4% 포인트, 수신자 조작 특성 곡선 아래 면적을 6% 포인트 증가시켰으며, 이는 가장 강력한 이전 방법에 비해 모두 상대적입니다. CCPS는 LLM 신뢰도 추정을 위한 효율적이고 광범위하게 적용 가능한 더 정확한 솔루션을 제공하여 그 신뢰성을 향상시킵니다.

## 📝 요약

대형 언어 모델(LLM)의 신뢰성을 높이기 위해 정확한 신뢰도 추정이 필요합니다. 이를 위해 우리는 CCPS(Calibrating LLM Confidence by Probing Perturbed Representation Stability)라는 새로운 방법을 제안합니다. CCPS는 LLM의 내부 표현 안정성을 분석하여 최종 숨겨진 상태에 적대적 교란을 가하고, 모델의 반응을 특징으로 추출하여 경량 분류기를 통해 정답을 예측합니다. 8B에서 32B 파라미터의 LLM을 대상으로 MMLU 및 MMLU-Pro 벤치마크를 사용하여 평가한 결과, CCPS는 기존 방법보다 뛰어난 성능을 보였습니다. CCPS는 기대 보정 오류를 약 55% 줄이고, Brier 점수를 21% 감소시키며, 정확도를 5%포인트, 정밀-재현 곡선 아래 면적을 4%포인트, 수신자 조작 특성 곡선 아래 면적을 6%포인트 증가시킵니다. 이는 LLM의 신뢰도를 향상시키는 효율적이고 적용 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. CCPS는 대형 언어 모델(LLM)의 내부 표현 안정성을 분석하여 신뢰도를 개선하는 새로운 방법입니다.
- 2. CCPS는 최종 숨겨진 상태에 대한 적대적 교란을 적용하고, 모델의 반응을 반영하는 특징을 추출하여 정답 예측을 수행합니다.
- 3. CCPS는 Llama, Qwen, Mistral 아키텍처를 포함한 8B에서 32B 파라미터의 LLM에서 테스트되었으며, MMLU 및 MMLU-Pro 벤치마크를 사용하여 성능을 평가했습니다.
- 4. CCPS는 기존 방법에 비해 예상 보정 오류를 약 55% 감소시키고, Brier 점수를 21% 줄이며, 정확도를 5% 포인트 증가시켰습니다.
- 5. CCPS는 LLM의 신뢰도를 높이는 효율적이고 폭넓게 적용 가능한 솔루션을 제공합니다.


---

*Generated on 2025-09-23 11:47:10*