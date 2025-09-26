<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:37:35.778034",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Kaplan-Meier Plot",
    "Individual Patient Data",
    "Multimodal Learning",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Kaplan-Meier Plot": 0.78,
    "Individual Patient Data": 0.77,
    "Multimodal Learning": 0.8,
    "Large Language Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Kaplan-Meier plots",
        "canonical": "Kaplan-Meier Plot",
        "aliases": [
          "KM plots"
        ],
        "category": "unique_technical",
        "rationale": "Kaplan-Meier plots are central to the paper's methodology and are a unique technical concept in survival analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "individual patient data",
        "canonical": "Individual Patient Data",
        "aliases": [
          "IPD"
        ],
        "category": "unique_technical",
        "rationale": "The reconstruction of individual patient data is the primary focus of the paper, offering unique insights into clinical research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "multimodal reasoning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal reasoning is a key component of the AI pipeline, linking to broader concepts in AI and machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "GPT-5",
        "canonical": "Large Language Model",
        "aliases": [
          "GPT-5"
        ],
        "category": "broad_technical",
        "rationale": "GPT-5 is a specific instance of large language models, relevant to the AI-powered aspects of the pipeline.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "automated pipeline",
      "clinical research",
      "evidence synthesis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Kaplan-Meier plots",
      "resolved_canonical": "Kaplan-Meier Plot",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "individual patient data",
      "resolved_canonical": "Individual Patient Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "multimodal reasoning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "GPT-5",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# KM-GPT: An Automated Pipeline for Reconstructing Individual Patient Data from Kaplan-Meier Plots

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18141.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18141](https://arxiv.org/abs/2509.18141)

## 🔗 유사한 논문
- [[2025-09-23/IPGPhormer_ Interpretable Pathology Graph-Transformer for Survival Analysis_20250923|IPGPhormer: Interpretable Pathology Graph-Transformer for Survival Analysis]] (84.2% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (81.6% similar)
- [[2025-09-22/From Data to Diagnosis_ A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction_20250922|From Data to Diagnosis: A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction]] (81.3% similar)
- [[2025-09-23/Interpretable Clinical Classification with Kolgomorov-Arnold Networks_20250923|Interpretable Clinical Classification with Kolgomorov-Arnold Networks]] (81.1% similar)
- [[2025-09-18/ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX: Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Kaplan-Meier Plot|Kaplan-Meier Plot]], [[keywords/Individual Patient Data|Individual Patient Data]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18141v1 Announce Type: cross 
Abstract: Reconstructing individual patient data (IPD) from Kaplan-Meier (KM) plots provides valuable insights for evidence synthesis in clinical research. However, existing approaches often rely on manual digitization, which is error-prone and lacks scalability. To address these limitations, we develop KM-GPT, the first fully automated, AI-powered pipeline for reconstructing IPD directly from KM plots with high accuracy, robustness, and reproducibility. KM-GPT integrates advanced image preprocessing, multi-modal reasoning powered by GPT-5, and iterative reconstruction algorithms to generate high-quality IPD without manual input or intervention. Its hybrid reasoning architecture automates the conversion of unstructured information into structured data flows and validates data extraction from complex KM plots. To improve accessibility, KM-GPT is equipped with a user-friendly web interface and an integrated AI assistant, enabling researchers to reconstruct IPD without requiring programming expertise. KM-GPT was rigorously evaluated on synthetic and real-world datasets, consistently demonstrating superior accuracy. To illustrate its utility, we applied KM-GPT to a meta-analysis of gastric cancer immunotherapy trials, reconstructing IPD to facilitate evidence synthesis and biomarker-based subgroup analyses. By automating traditionally manual processes and providing a scalable, web-based solution, KM-GPT transforms clinical research by leveraging reconstructed IPD to enable more informed downstream analyses, supporting evidence-based decision-making.

## 📝 요약

논문은 Kaplan-Meier(KM) 플롯에서 개별 환자 데이터를 자동으로 재구성하는 AI 기반 도구인 KM-GPT를 소개합니다. 기존 방법의 수작업 문제를 해결하기 위해 개발된 KM-GPT는 이미지 전처리, GPT-5 기반 다중 모달 추론, 반복적 재구성 알고리즘을 통합하여 높은 정확성과 재현성을 제공합니다. 사용이 간편한 웹 인터페이스와 AI 어시스턴트를 통해 프로그래밍 지식 없이도 연구자들이 데이터를 재구성할 수 있습니다. 위장암 면역 치료 메타 분석에 적용하여 데이터 재구성의 유용성을 입증했으며, 이는 임상 연구의 증거 기반 의사 결정을 지원합니다.

## 🎯 주요 포인트

- 1. KM-GPT는 Kaplan-Meier 플롯에서 개별 환자 데이터를 자동으로 재구성하는 최초의 AI 기반 파이프라인으로, 높은 정확성과 재현성을 제공합니다.
- 2. 이 시스템은 고급 이미지 전처리, GPT-5 기반의 다중 모달 추론, 반복적 재구성 알고리즘을 통합하여 수작업 없이 고품질의 데이터를 생성합니다.
- 3. 사용자 친화적인 웹 인터페이스와 AI 어시스턴트를 통해 프로그래밍 지식 없이도 연구자들이 데이터를 재구성할 수 있도록 지원합니다.
- 4. KM-GPT는 합성 및 실제 데이터셋에서 높은 정확성을 입증했으며, 위암 면역요법 시험의 메타 분석에 적용되어 증거 종합 및 바이오마커 기반 하위 그룹 분석을 지원했습니다.
- 5. 이 도구는 임상 연구에서 전통적으로 수작업이 필요한 과정을 자동화하고, 웹 기반 솔루션을 제공하여 증거 기반 의사결정을 지원합니다.


---

*Generated on 2025-09-24 13:37:35*