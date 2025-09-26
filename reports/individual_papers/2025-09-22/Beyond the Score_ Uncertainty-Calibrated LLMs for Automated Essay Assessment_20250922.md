---
keywords:
  - Automated Essay Scoring
  - Conformal Prediction
  - Large Language Model
  - Uncertainty-aware Accuracy
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15926
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:54:31.024643",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Automated Essay Scoring",
    "Conformal Prediction",
    "Large Language Model",
    "Uncertainty-aware Accuracy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Automated Essay Scoring": 0.8,
    "Conformal Prediction": 0.78,
    "Large Language Model": 0.85,
    "Uncertainty-aware Accuracy": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Automated Essay Scoring",
        "canonical": "Automated Essay Scoring",
        "aliases": [
          "AES"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and provides a specific application area for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Conformal Prediction",
        "canonical": "Conformal Prediction",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is a novel aspect of the paper's methodology, enhancing the linking of uncertainty measures.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a foundational technology in the paper, relevant for connecting to broader NLP research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Uncertainty-aware Accuracy",
        "canonical": "Uncertainty-aware Accuracy",
        "aliases": [
          "UAcc"
        ],
        "category": "unique_technical",
        "rationale": "This metric is a unique contribution of the paper, useful for linking to performance evaluation discussions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "score",
      "model",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Automated Essay Scoring",
      "resolved_canonical": "Automated Essay Scoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Conformal Prediction",
      "resolved_canonical": "Conformal Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Uncertainty-aware Accuracy",
      "resolved_canonical": "Uncertainty-aware Accuracy",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Beyond the Score: Uncertainty-Calibrated LLMs for Automated Essay Assessment

**Korean Title:** 점수를 넘어서: 자동화된 에세이 평가를 위한 불확실성 보정 대형 언어 모델(LLM)

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15926.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15926](https://arxiv.org/abs/2509.15926)

## 🔗 유사한 논문
- [[2025-09-19/LLM Agents at the Roundtable_ A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring_20250919|LLM Agents at the Roundtable: A Multi-Perspective and Dialectical Reasoning Framework for Essay Scoring]] (85.3% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (84.0% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment]] (83.4% similar)
- [[2025-09-22/Fine-Tuning Large Multimodal Models for Automatic Pronunciation Assessment_20250922|Fine-Tuning Large Multimodal Models for Automatic Pronunciation Assessment]] (82.5% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Automated Essay Scoring|Automated Essay Scoring]], [[keywords/Conformal Prediction|Conformal Prediction]], [[keywords/Uncertainty-aware Accuracy|Uncertainty-aware Accuracy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15926v1 Announce Type: cross 
Abstract: Automated Essay Scoring (AES) systems now reach near human agreement on some public benchmarks, yet real-world adoption, especially in high-stakes examinations, remains limited. A principal obstacle is that most models output a single score without any accompanying measure of confidence or explanation. We address this gap with conformal prediction, a distribution-free wrapper that equips any classifier with set-valued outputs and formal coverage guarantees. Two open-source large language models (Llama-3 8B and Qwen-2.5 3B) are fine-tuned on three diverse corpora (ASAP, TOEFL11, Cambridge-FCE) and calibrated at a 90 percent risk level. Reliability is assessed with UAcc, an uncertainty-aware accuracy that rewards models for being both correct and concise. To our knowledge, this is the first work to combine conformal prediction and UAcc for essay scoring. The calibrated models consistently meet the coverage target while keeping prediction sets compact, indicating that open-source, mid-sized LLMs can already support teacher-in-the-loop AES; we discuss scaling and broader user studies as future work.

## 🔍 Abstract (한글 번역)

arXiv:2509.15926v1 발표 유형: 교차  
초록: 자동 에세이 채점(AES) 시스템은 이제 일부 공공 벤치마크에서 인간과 유사한 수준의 일치를 보이고 있지만, 실제 세계에서의 채택, 특히 중요한 시험에서의 채택은 여전히 제한적입니다. 주요 장애물 중 하나는 대부분의 모델이 신뢰도나 설명 없이 단일 점수만을 출력한다는 점입니다. 우리는 이 격차를 보완하기 위해 분포에 의존하지 않는 래퍼인 적합 예측을 사용하여 모든 분류기에 집합 값 출력과 공식적인 커버리지 보장을 제공합니다. 두 개의 오픈 소스 대형 언어 모델(Llama-3 8B 및 Qwen-2.5 3B)은 세 가지 다양한 코퍼스(ASAP, TOEFL11, Cambridge-FCE)에서 미세 조정되고 90% 위험 수준에서 보정됩니다. 신뢰성은 모델이 정확하고 간결할 때 보상하는 불확실성 인식 정확도(UAcc)로 평가됩니다. 우리의 지식에 따르면, 적합 예측과 UAcc를 에세이 채점에 결합한 것은 이번이 처음입니다. 보정된 모델은 일관되게 커버리지 목표를 충족하면서도 예측 집합을 간결하게 유지하여, 오픈 소스 중간 크기 LLM이 이미 교사 참여 AES를 지원할 수 있음을 나타냅니다. 우리는 확장 및 더 넓은 사용자 연구를 향후 작업으로 논의합니다.

## 📝 요약

이 논문은 자동 에세이 채점 시스템(AES)의 실제 적용을 방해하는 문제를 해결하기 위해, 예측 결과에 대한 신뢰도와 설명을 제공하지 않는 기존 모델의 한계를 극복하고자 합니다. 이를 위해, 저자들은 분포에 구애받지 않는 적합 예측(conformal prediction) 기법을 사용하여 모델에 집합값 출력과 공식적 커버리지 보장을 추가했습니다. Llama-3 8B와 Qwen-2.5 3B라는 두 개의 대형 언어 모델을 다양한 코퍼스(ASAP, TOEFL11, Cambridge-FCE)로 미세 조정하고 90% 위험 수준에서 보정했습니다. 신뢰성은 불확실성 인식 정확도(UAcc)로 평가되며, 이는 모델이 정확하고 간결할 때 보상을 줍니다. 이 연구는 적합 예측과 UAcc를 에세이 채점에 결합한 최초의 사례로, 보정된 모델들이 목표 커버리지를 일관되게 충족하면서 예측 집합을 작게 유지함을 보여줍니다. 이는 중형 오픈소스 LLM이 이미 교사와 함께하는 AES를 지원할 수 있음을 시사하며, 향후 확장 및 사용자 연구를 논의합니다.

## 🎯 주요 포인트

- 1. 자동 에세이 채점 시스템(AES)은 일부 공개 벤치마크에서 인간 수준의 일치를 달성했으나, 실제 고위험 시험에서의 채택은 제한적이다.
- 2. 대부분의 모델은 단일 점수만 출력하며, 신뢰도나 설명을 제공하지 않는 것이 주요 장애물이다.
- 3. 본 연구는 적합 예측(conformal prediction)을 통해 모든 분류기에 집합 값 출력과 형식적 커버리지 보장을 제공하여 이 문제를 해결한다.
- 4. 두 개의 오픈 소스 대형 언어 모델(Llama-3 8B, Qwen-2.5 3B)을 다양한 코퍼스에 맞춰 미세 조정하고 90% 위험 수준에서 보정하였다.
- 5. 본 연구는 적합 예측과 불확실성 인식 정확도(UAcc)를 에세이 채점에 결합한 최초의 연구로, 중간 크기의 오픈 소스 LLM이 이미 교사 참여 AES를 지원할 수 있음을 시사한다.


---

*Generated on 2025-09-23 10:54:31*