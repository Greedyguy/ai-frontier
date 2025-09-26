---
keywords:
  - Whole Slide Imaging
  - Report-auxiliary Self-distillation
  - Large Language Model
  - Risk-aware Mix-up
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15608
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:02:51.036594",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Whole Slide Imaging",
    "Report-auxiliary Self-distillation",
    "Large Language Model",
    "Risk-aware Mix-up"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Whole Slide Imaging": 0.75,
    "Report-auxiliary Self-distillation": 0.7,
    "Large Language Model": 0.8,
    "Risk-aware Mix-up": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Whole Slide Images",
        "canonical": "Whole Slide Imaging",
        "aliases": [
          "WSI",
          "Whole Slide Image"
        ],
        "category": "unique_technical",
        "rationale": "Whole Slide Imaging is a critical component in cancer prognosis, offering a unique technical perspective for linking pathology and imaging data.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Report-auxiliary self-distillation",
        "canonical": "Report-auxiliary Self-distillation",
        "aliases": [
          "Rasa"
        ],
        "category": "unique_technical",
        "rationale": "This novel framework integrates pathology reports with WSI data, enhancing survival analysis, and offers a unique approach to data integration.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are pivotal in extracting meaningful information from pathology reports, linking NLP with medical imaging.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Risk-aware mix-up strategy",
        "canonical": "Risk-aware Mix-up",
        "aliases": [
          "Mix-up Strategy"
        ],
        "category": "unique_technical",
        "rationale": "This strategy enhances model training by increasing data diversity, offering a unique approach to model robustness.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "survival analysis",
      "pathology reports",
      "training data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Whole Slide Images",
      "resolved_canonical": "Whole Slide Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Report-auxiliary self-distillation",
      "resolved_canonical": "Report-auxiliary Self-distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Risk-aware mix-up strategy",
      "resolved_canonical": "Risk-aware Mix-up",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Enhancing WSI-Based Survival Analysis with Report-Auxiliary Self-Distillation

**Korean Title:** WSI 기반 생존 분석을 보고서 보조 자기 증류로 향상시키기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15608.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15608](https://arxiv.org/abs/2509.15608)

## 🔗 유사한 논문
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (81.5% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (79.1% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (78.9% similar)
- [[2025-09-18/Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (78.8% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Whole Slide Imaging|Whole Slide Imaging]], [[keywords/Report-auxiliary Self-distillation|Report-auxiliary Self-distillation]], [[keywords/Risk-aware Mix-up|Risk-aware Mix-up]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15608v1 Announce Type: new 
Abstract: Survival analysis based on Whole Slide Images (WSIs) is crucial for evaluating cancer prognosis, as they offer detailed microscopic information essential for predicting patient outcomes. However, traditional WSI-based survival analysis usually faces noisy features and limited data accessibility, hindering their ability to capture critical prognostic features effectively. Although pathology reports provide rich patient-specific information that could assist analysis, their potential to enhance WSI-based survival analysis remains largely unexplored. To this end, this paper proposes a novel Report-auxiliary self-distillation (Rasa) framework for WSI-based survival analysis. First, advanced large language models (LLMs) are utilized to extract fine-grained, WSI-relevant textual descriptions from original noisy pathology reports via a carefully designed task prompt. Next, a self-distillation-based pipeline is designed to filter out irrelevant or redundant WSI features for the student model under the guidance of the teacher model's textual knowledge. Finally, a risk-aware mix-up strategy is incorporated during the training of the student model to enhance both the quantity and diversity of the training data. Extensive experiments carried out on our collected data (CRC) and public data (TCGA-BRCA) demonstrate the superior effectiveness of Rasa against state-of-the-art methods. Our code is available at https://github.com/zhengwang9/Rasa.

## 🔍 Abstract (한글 번역)

arXiv:2509.15608v1 발표 유형: 신규  
초록: 전 슬라이드 이미지(WSI)를 기반으로 한 생존 분석은 암 예후 평가에 있어 매우 중요합니다. 이는 환자의 결과를 예측하는 데 필수적인 세부적인 현미경 정보를 제공하기 때문입니다. 그러나 전통적인 WSI 기반 생존 분석은 일반적으로 잡음이 많은 특징과 제한된 데이터 접근성으로 인해 중요한 예후 특징을 효과적으로 포착하는 데 어려움을 겪습니다. 병리 보고서는 분석에 도움이 될 수 있는 풍부한 환자별 정보를 제공하지만, WSI 기반 생존 분석을 향상시킬 수 있는 잠재력은 대부분 탐구되지 않은 상태로 남아 있습니다. 이를 위해 본 논문에서는 WSI 기반 생존 분석을 위한 새로운 보고서 보조 자기 증류(Rasa) 프레임워크를 제안합니다. 먼저, 고급 대형 언어 모델(LLM)을 활용하여 원래의 잡음이 많은 병리 보고서에서 세심하게 설계된 작업 프롬프트를 통해 세분화된 WSI 관련 텍스트 설명을 추출합니다. 다음으로, 교사 모델의 텍스트 지식을 바탕으로 학생 모델에 대해 관련이 없거나 중복된 WSI 특징을 걸러내기 위한 자기 증류 기반 파이프라인을 설계합니다. 마지막으로, 학생 모델의 훈련 과정에서 위험 인식 혼합 전략을 통합하여 훈련 데이터의 양과 다양성을 모두 향상시킵니다. 수집된 데이터(CRC)와 공개 데이터(TCGA-BRCA)에서 수행된 광범위한 실험은 최첨단 방법에 비해 Rasa의 뛰어난 효과를 입증합니다. 우리의 코드는 https://github.com/zhengwang9/Rasa에서 확인할 수 있습니다.

## 📝 요약

이 논문은 전체 슬라이드 이미지(WSI)를 기반으로 한 생존 분석의 정확성을 높이기 위해 새로운 보고서 보조 자기 증류(Rasa) 프레임워크를 제안합니다. 기존의 WSI 기반 분석은 잡음이 많은 특징과 제한된 데이터 접근성 문제를 겪고 있습니다. 이를 해결하기 위해, 이 연구는 대형 언어 모델(LLM)을 사용하여 병리 보고서에서 WSI와 관련된 세부 텍스트를 추출하고, 자기 증류 기반 파이프라인을 통해 불필요한 WSI 특징을 제거합니다. 또한, 학생 모델의 학습 시 리스크 인식 혼합 전략을 사용하여 데이터의 양과 다양성을 증가시킵니다. 실험 결과, 제안된 Rasa 프레임워크가 기존 방법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. WSI 기반 생존 분석은 암 예후 평가에 중요하지만, 전통적인 방법은 잡음 있는 특징과 제한된 데이터 접근성으로 인해 중요한 예후 특징을 효과적으로 포착하기 어렵다.
- 2. 본 논문은 WSI 기반 생존 분석을 개선하기 위해 보고서 보조 자기 증류(Rasa) 프레임워크를 제안한다.
- 3. 대형 언어 모델(LLM)을 활용하여 원래의 잡음 있는 병리 보고서에서 세밀한 WSI 관련 텍스트 설명을 추출한다.
- 4. 교사 모델의 텍스트 지식을 바탕으로 학생 모델의 불필요하거나 중복된 WSI 특징을 걸러내는 자기 증류 기반 파이프라인을 설계한다.
- 5. 학생 모델의 훈련 시 위험 인식 혼합 전략을 도입하여 훈련 데이터의 양과 다양성을 향상시킨다.


---

*Generated on 2025-09-23 12:02:51*