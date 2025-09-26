---
keywords:
  - Large Language Model
  - Optical Character Recognition
  - Multilingual Question Answering Systems
  - OCR Noise
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2502.16781
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:41:20.927532",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Optical Character Recognition",
    "Multilingual Question Answering Systems",
    "OCR Noise"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Optical Character Recognition": 0.85,
    "Multilingual Question Answering Systems": 0.78,
    "OCR Noise": 0.82
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
        "rationale": "LLMs are central to the study, providing a basis for evaluating performance under noisy conditions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Optical Character Recognition",
        "canonical": "Optical Character Recognition",
        "aliases": [
          "OCR"
        ],
        "category": "unique_technical",
        "rationale": "OCR is a critical component affecting the QA systems' performance in the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multilingual QA Systems",
        "canonical": "Multilingual Question Answering Systems",
        "aliases": [
          "Multilingual QA"
        ],
        "category": "unique_technical",
        "rationale": "The focus on multilingual capabilities highlights the study's scope and challenges.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "OCR-induced noise",
        "canonical": "OCR Noise",
        "aliases": [
          "OCR errors",
          "OCR-induced errors"
        ],
        "category": "unique_technical",
        "rationale": "Understanding OCR noise is essential for improving QA system performance.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "question-answering",
      "dataset",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Optical Character Recognition",
      "resolved_canonical": "Optical Character Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multilingual QA Systems",
      "resolved_canonical": "Multilingual Question Answering Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "OCR-induced noise",
      "resolved_canonical": "OCR Noise",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Evaluating Robustness of LLMs in Question Answering on Multilingual Noisy OCR Data

**Korean Title:** 다국어 잡음이 있는 OCR 데이터에서 질문 응답에 대한 대형 언어 모델(LLM)의 견고성 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.16781.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2502.16781](https://arxiv.org/abs/2502.16781)

## 🔗 유사한 논문
- [[2025-09-22/Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering_20250922|Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering]] (83.5% similar)
- [[2025-09-22/PCSR_ Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning_20250922|PCSR: Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning]] (80.8% similar)
- [[2025-09-22/Noise-Robustness Through Noise_ Asymmetric LoRA Adaption with Poisoning Expert_20250922|Noise-Robustness Through Noise: Asymmetric LoRA Adaption with Poisoning Expert]] (80.2% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (80.0% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Optical Character Recognition|Optical Character Recognition]], [[keywords/Multilingual Question Answering Systems|Multilingual Question Answering Systems]], [[keywords/OCR Noise|OCR Noise]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.16781v3 Announce Type: replace 
Abstract: Optical Character Recognition (OCR) plays a crucial role in digitizing historical and multilingual documents, yet OCR errors - imperfect extraction of text, including character insertion, deletion, and substitution can significantly impact downstream tasks like question-answering (QA). In this work, we conduct a comprehensive analysis of how OCR-induced noise affects the performance of Multilingual QA Systems. To support this analysis, we introduce a multilingual QA dataset MultiOCR-QA, comprising 50K question-answer pairs across three languages, English, French, and German. The dataset is curated from OCR-ed historical documents, which include different levels and types of OCR noise. We then evaluate how different state-of-the-art Large Language Models (LLMs) perform under different error conditions, focusing on three major OCR error types. Our findings show that QA systems are highly prone to OCR-induced errors and perform poorly on noisy OCR text. By comparing model performance on clean versus noisy texts, we provide insights into the limitations of current approaches and emphasize the need for more noise-resilient QA systems in historical digitization contexts.

## 🔍 Abstract (한글 번역)

arXiv:2502.16781v3 발표 유형: 교체  
초록: 광학 문자 인식(OCR)은 역사적 및 다국어 문서를 디지털화하는 데 중요한 역할을 하지만, 문자 삽입, 삭제, 대체를 포함한 텍스트의 불완전한 추출과 같은 OCR 오류는 질문-응답(QA)과 같은 후속 작업에 상당한 영향을 미칠 수 있습니다. 본 연구에서는 OCR로 인한 노이즈가 다국어 QA 시스템의 성능에 어떻게 영향을 미치는지에 대한 종합적인 분석을 수행합니다. 이를 지원하기 위해 영어, 프랑스어, 독일어의 세 가지 언어에 걸쳐 50,000개의 질문-응답 쌍으로 구성된 다국어 QA 데이터셋 MultiOCR-QA를 소개합니다. 이 데이터셋은 다양한 수준과 유형의 OCR 노이즈를 포함하는 OCR 처리된 역사적 문서에서 큐레이션되었습니다. 그런 다음, 세 가지 주요 OCR 오류 유형에 중점을 두고, 다양한 최첨단 대형 언어 모델(LLM)이 서로 다른 오류 조건에서 어떻게 성능을 발휘하는지 평가합니다. 우리의 연구 결과는 QA 시스템이 OCR로 인한 오류에 매우 취약하며, 노이즈가 있는 OCR 텍스트에서 성능이 저조하다는 것을 보여줍니다. 깨끗한 텍스트와 노이즈가 있는 텍스트에서의 모델 성능을 비교함으로써, 현재 접근 방식의 한계를 통찰하고 역사적 디지털화 맥락에서 더 강력한 노이즈 저항성을 가진 QA 시스템의 필요성을 강조합니다.

## 📝 요약

이 논문은 Optical Character Recognition(OCR) 오류가 다국어 질문-응답(QA) 시스템에 미치는 영향을 분석합니다. 이를 위해 영어, 프랑스어, 독일어로 구성된 50,000개의 질문-응답 쌍을 포함한 다국어 QA 데이터셋인 MultiOCR-QA를 소개합니다. 이 데이터셋은 다양한 수준과 유형의 OCR 노이즈를 포함한 역사적 문서에서 수집되었습니다. 연구는 최신 대형 언어 모델(LLM)이 OCR 오류 조건에서 어떻게 성능을 발휘하는지를 평가하며, 세 가지 주요 OCR 오류 유형에 초점을 맞춥니다. 결과적으로 QA 시스템이 OCR로 인한 오류에 매우 취약하며, 노이즈가 있는 텍스트에서 성능이 저하됨을 발견했습니다. 이를 통해 현재 접근 방식의 한계를 밝히고, 역사적 디지털화에서 노이즈에 강한 QA 시스템의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. Optical Character Recognition (OCR) 오류는 다국어 문서의 디지털화 과정에서 질문-응답(QA) 시스템의 성능에 큰 영향을 미친다.
- 2. 본 연구에서는 OCR로 인한 노이즈가 다국어 QA 시스템의 성능에 미치는 영향을 종합적으로 분석하였다.
- 3. 연구를 위해 영어, 프랑스어, 독일어로 구성된 50,000개의 질문-응답 쌍을 포함하는 다국어 QA 데이터셋 MultiOCR-QA를 소개하였다.
- 4. 최신 대형 언어 모델(LLM)의 성능을 다양한 OCR 오류 조건 하에서 평가하였으며, QA 시스템이 OCR 오류에 매우 취약하다는 것을 발견하였다.
- 5. 깨끗한 텍스트와 노이즈가 있는 텍스트에서의 모델 성능 비교를 통해 현재 접근 방식의 한계를 파악하고, 역사적 디지털화 맥락에서 더 강력한 QA 시스템의 필요성을 강조하였다.


---

*Generated on 2025-09-23 11:41:20*