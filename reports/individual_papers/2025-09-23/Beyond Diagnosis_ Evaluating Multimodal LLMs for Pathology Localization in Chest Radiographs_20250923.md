---
keywords:
  - Multimodal Learning
  - Pathology Localization
  - Vision-Language Model
  - CheXlocalize Dataset
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.18015
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:17:31.233896",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Pathology Localization",
    "Vision-Language Model",
    "CheXlocalize Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.79,
    "Pathology Localization": 0.72,
    "Vision-Language Model": 0.81,
    "CheXlocalize Dataset": 0.69
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal LLMs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Large Language Models"
        ],
        "category": "specific_connectable",
        "rationale": "Connects advancements in language models with multimodal capabilities, relevant for linking to recent trends.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Pathology Localization",
        "canonical": "Pathology Localization",
        "aliases": [
          "Disease Localization",
          "Lesion Localization"
        ],
        "category": "unique_technical",
        "rationale": "A specific task in medical imaging that bridges clinical applications and AI models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.72
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents the integration of visual and textual data processing, crucial for understanding multimodal systems.",
        "novelty_score": 0.57,
        "connectivity_score": 0.84,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "CheXlocalize dataset",
        "canonical": "CheXlocalize Dataset",
        "aliases": [
          "CheXlocalize"
        ],
        "category": "unique_technical",
        "rationale": "A specific dataset used for evaluating pathology localization, linking data resources with research outcomes.",
        "novelty_score": 0.73,
        "connectivity_score": 0.62,
        "specificity_score": 0.85,
        "link_intent_score": 0.69
      }
    ],
    "ban_list_suggestions": [
      "diagnostic tasks",
      "clinical utility",
      "spatial understanding"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal LLMs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Pathology Localization",
      "resolved_canonical": "Pathology Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.57,
        "connectivity": 0.84,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "CheXlocalize dataset",
      "resolved_canonical": "CheXlocalize Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.73,
        "connectivity": 0.62,
        "specificity": 0.85,
        "link_intent": 0.69
      }
    }
  ]
}
-->

# Beyond Diagnosis: Evaluating Multimodal LLMs for Pathology Localization in Chest Radiographs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18015.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.18015](https://arxiv.org/abs/2509.18015)

## 🔗 유사한 논문
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (84.9% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (83.7% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (82.8% similar)
- [[2025-09-23/Evaluation of Causal Reasoning for Large Language Models in Contextualized Clinical Scenarios of Laboratory Test Interpretation_20250923|Evaluation of Causal Reasoning for Large Language Models in Contextualized Clinical Scenarios of Laboratory Test Interpretation]] (82.6% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence: Label Quality, Domain Shift, Bias and Evaluation Challenges]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Pathology Localization|Pathology Localization]], [[keywords/CheXlocalize Dataset|CheXlocalize Dataset]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18015v1 Announce Type: cross 
Abstract: Recent work has shown promising performance of frontier large language models (LLMs) and their multimodal counterparts in medical quizzes and diagnostic tasks, highlighting their potential for broad clinical utility given their accessible, general-purpose nature. However, beyond diagnosis, a fundamental aspect of medical image interpretation is the ability to localize pathological findings. Evaluating localization not only has clinical and educational relevance but also provides insight into a model's spatial understanding of anatomy and disease. Here, we systematically assess two general-purpose MLLMs (GPT-4 and GPT-5) and a domain-specific model (MedGemma) in their ability to localize pathologies on chest radiographs, using a prompting pipeline that overlays a spatial grid and elicits coordinate-based predictions. Averaged across nine pathologies in the CheXlocalize dataset, GPT-5 exhibited a localization accuracy of 49.7%, followed by GPT-4 (39.1%) and MedGemma (17.7%), all lower than a task-specific CNN baseline (59.9%) and a radiologist benchmark (80.1%). Despite modest performance, error analysis revealed that GPT-5's predictions were largely in anatomically plausible regions, just not always precisely localized. GPT-4 performed well on pathologies with fixed anatomical locations, but struggled with spatially variable findings and exhibited anatomically implausible predictions more frequently. MedGemma demonstrated the lowest performance on all pathologies, showing limited capacity to generalize to this novel task. Our findings highlight both the promise and limitations of current MLLMs in medical imaging and underscore the importance of integrating them with task-specific tools for reliable use.

## 📝 요약

최근 연구에서는 대형 언어 모델(LLM)과 그 멀티모달 버전이 의료 퀴즈와 진단 작업에서 뛰어난 성능을 보였으나, 병리학적 소견의 위치를 파악하는 능력은 여전히 도전 과제입니다. 본 연구는 일반 목적의 MLLM(GPT-4, GPT-5)과 도메인 특화 모델(MedGemma)이 흉부 X선에서 병리학적 소견을 얼마나 잘 위치화할 수 있는지를 평가했습니다. CheXlocalize 데이터셋을 기반으로 한 결과, GPT-5는 49.7%의 정확도를 보였고, GPT-4는 39.1%, MedGemma는 17.7%를 기록했습니다. 이는 특정 작업에 최적화된 CNN(59.9%)과 방사선 전문의(80.1%)의 정확도보다 낮았습니다. GPT-5는 해부학적으로 그럴듯한 영역에서 예측했으나 정확한 위치화는 부족했습니다. GPT-4는 고정된 해부학적 위치의 병리에서 잘 작동했으나, 가변적인 위치에서는 어려움을 겪었습니다. MedGemma는 모든 병리에서 가장 낮은 성능을 보였습니다. 연구 결과는 현재 MLLM의 가능성과 한계를 보여주며, 신뢰할 수 있는 사용을 위해 특정 작업에 맞춘 도구와의 통합이 중요함을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)과 그 멀티모달 버전은 의료 퀴즈 및 진단 작업에서 유망한 성과를 보였으나, 병리학적 소견의 위치를 파악하는 능력은 여전히 과제로 남아있다.
- 2. GPT-5는 흉부 X선 사진에서 병리학적 소견을 위치화하는 데 있어 49.7%의 정확도를 보였으며, 이는 GPT-4(39.1%)와 MedGemma(17.7%)보다 높았으나, 특정 과제에 특화된 CNN(59.9%)과 방사선 전문의 기준(80.1%)보다는 낮았다.
- 3. GPT-5는 해부학적으로 그럴듯한 영역에서 예측을 했으나, 항상 정확히 위치화하지는 못했다.
- 4. GPT-4는 고정된 해부학적 위치에 있는 병리학적 소견에서는 잘 수행했으나, 공간적으로 변동이 있는 소견에서는 어려움을 겪었다.
- 5. MedGemma는 모든 병리학적 소견에서 가장 낮은 성과를 보였으며, 새로운 과제에 대한 일반화 능력이 제한적이었다.


---

*Generated on 2025-09-24 00:17:31*