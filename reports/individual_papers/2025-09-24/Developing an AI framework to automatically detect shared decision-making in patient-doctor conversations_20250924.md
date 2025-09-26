<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:49:08.872687",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Artificial Intelligence",
    "Deep Learning",
    "Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Artificial Intelligence": 0.0,
    "Deep Learning": 0.0,
    "Language Model": 0.0
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Artificial Intelligence",
      "resolved_canonical": "Artificial Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.0,
        "connectivity": 0.0,
        "specificity": 0.0,
        "link_intent": 0.0
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.0,
        "connectivity": 0.0,
        "specificity": 0.0,
        "link_intent": 0.0
      }
    },
    {
      "candidate_surface": "Language Model",
      "resolved_canonical": "Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.0,
        "connectivity": 0.0,
        "specificity": 0.0,
        "link_intent": 0.0
      }
    }
  ]
}
-->

# Developing an AI framework to automatically detect shared decision-making in patient-doctor conversations

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18439.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18439](https://arxiv.org/abs/2509.18439)

## 🔗 유사한 논문
- [[2025-09-23/Longitudinal and Multimodal Recording System to Capture Real-World Patient-Clinician Conversations for AI and Encounter Research_ Protocol_20250923|Longitudinal and Multimodal Recording System to Capture Real-World Patient-Clinician Conversations for AI and Encounter Research: Protocol]] (83.5% similar)
- [[2025-09-23/"What's Up, Doc?"_ Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets_20250923|"What's Up, Doc?": Analyzing How Users Seek Health Information in Large-Scale Conversational AI Datasets]] (81.7% similar)
- [[2025-09-19/Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery_20250919|Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery]] (81.2% similar)
- [[2025-09-23/Enhancing Clinical Decision-Making_ Integrating Multi-Agent Systems with Ethical AI Governance_20250923|Enhancing Clinical Decision-Making: Integrating Multi-Agent Systems with Ethical AI Governance]] (81.1% similar)
- [[2025-09-17/Deploying UDM Series in Real-Life Stuttered Speech Applications_ A Clinical Evaluation Framework_20250917|Deploying UDM Series in Real-Life Stuttered Speech Applications: A Clinical Evaluation Framework]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Artificial Intelligence|Artificial Intelligence]], [[keywords/Deep Learning|Deep Learning]], [[keywords/Language Model|Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18439v1 Announce Type: cross 
Abstract: Shared decision-making (SDM) is necessary to achieve patient-centred care. Currently no methodology exists to automatically measure SDM at scale. This study aimed to develop an automated approach to measure SDM by using language modelling and the conversational alignment (CA) score. A total of 157 video-recorded patient-doctor conversations from a randomized multi-centre trial evaluating SDM decision aids for anticoagulation in atrial fibrillations were transcribed and segmented into 42,559 sentences. Context-response pairs and negative sampling were employed to train deep learning (DL) models and fine-tuned BERT models via the next sentence prediction (NSP) task. Each top-performing model was used to calculate four types of CA scores. A random-effects analysis by clinician, adjusting for age, sex, race, and trial arm, assessed the association between CA scores and SDM outcomes: the Decisional Conflict Scale (DCS) and the Observing Patient Involvement in Decision-Making 12 (OPTION12) scores. p-values were corrected for multiple comparisons with the Benjamini-Hochberg method. Among 157 patients (34% female, mean age 70 SD 10.8), clinicians on average spoke more words than patients (1911 vs 773). The DL model without the stylebook strategy achieved a recall@1 of 0.227, while the fine-tuned BERTbase (110M) achieved the highest recall@1 with 0.640. The AbsMax (18.36 SE7.74 p=0.025) and Max CA (21.02 SE7.63 p=0.012) scores generated with the DL without stylebook were associated with OPTION12. The Max CA score generated with the fine-tuned BERTbase (110M) was associated with the DCS score (-27.61 SE12.63 p=0.037). BERT model sizes did not have an impact the association between CA scores and SDM. This study introduces an automated, scalable methodology to measure SDM in patient-doctor conversations through explainable CA scores, with potential to evaluate SDM strategies at scale.

## 📝 요약

이 연구는 환자 중심의 치료를 위해 필요한 공동 의사결정(SDM)을 자동으로 측정할 수 있는 방법론을 개발했습니다. 심방세동 환자의 항응고제 선택을 위한 SDM 도구를 평가하는 다기관 무작위 시험에서 수집한 157개의 환자-의사 대화 영상을 분석했습니다. 대화는 42,559개의 문장으로 전사 및 세분화되었으며, 심층 학습(DL) 모델과 BERT 모델을 활용해 대화 정렬(CA) 점수를 계산했습니다. 연구 결과, BERT 모델을 활용한 Max CA 점수가 의사결정 갈등 척도(DCS)와 연관이 있었으며, DL 모델의 AbsMax와 Max CA 점수는 OPTION12 점수와 연관이 있었습니다. 이 연구는 설명 가능한 CA 점수를 통해 SDM을 자동으로 측정할 수 있는 확장 가능한 방법론을 제시하며, 대규모 SDM 전략 평가에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 환자 중심 치료를 달성하기 위해 필요한 공유 의사결정(SDM)을 자동으로 측정할 수 있는 방법론을 개발하는 것을 목표로 하였습니다.
- 2. 심방세동 항응고제 SDM 의사결정 도구를 평가하는 다기관 무작위 시험에서 157명의 환자-의사 대화를 분석하여 42,559개의 문장으로 전사 및 세분화하였습니다.
- 3. 딥러닝(DL) 모델과 BERT 모델을 활용하여 대화 정렬(CA) 점수를 계산하고, CA 점수와 SDM 결과 간의 연관성을 평가하였습니다.
- 4. DL 모델과 BERT 모델을 사용하여 생성된 CA 점수는 OPTION12 및 DCS 점수와 유의미한 연관성을 보였습니다.
- 5. 본 연구는 환자-의사 대화에서 SDM을 측정할 수 있는 자동화되고 확장 가능한 방법론을 제시하였으며, 대규모 SDM 전략 평가에 잠재력을 가지고 있습니다.


---

*Generated on 2025-09-24 13:49:08*