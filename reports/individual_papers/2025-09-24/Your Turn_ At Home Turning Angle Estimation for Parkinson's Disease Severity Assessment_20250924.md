<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:24:25.898970",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Human Pose Estimation",
    "Turn-REMAP Dataset",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Human Pose Estimation": 0.78,
    "Turn-REMAP Dataset": 0.74,
    "Transformer": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental technique used in the paper's approach to quantify turning angles.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Human Pose Estimation",
        "canonical": "Human Pose Estimation",
        "aliases": [
          "Pose Estimation"
        ],
        "category": "unique_technical",
        "rationale": "Human Pose Estimation is central to the methodology for extracting 3D skeletons from videos.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Turn-REMAP",
        "canonical": "Turn-REMAP Dataset",
        "aliases": [
          "Turn-REMAP"
        ],
        "category": "unique_technical",
        "rationale": "Turn-REMAP is a specific dataset used in the study, crucial for understanding the context and results.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.74
      },
      {
        "surface": "Strided Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Strided Transformer"
        ],
        "category": "specific_connectable",
        "rationale": "Strided Transformer is a variant of Transformer models used for pose estimation in the study.",
        "novelty_score": 0.58,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "gait",
      "turning angles",
      "PD symptoms"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Human Pose Estimation",
      "resolved_canonical": "Human Pose Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Turn-REMAP",
      "resolved_canonical": "Turn-REMAP Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "Strided Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Your Turn: At Home Turning Angle Estimation for Parkinson's Disease Severity Assessment

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2408.08182.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2408.08182](https://arxiv.org/abs/2408.08182)

## 🔗 유사한 논문
- [[2025-09-23/MRN_ Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data_20250923|MRN: Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data]] (82.0% similar)
- [[2025-09-23/Selecting Optimal Camera Views for Gait Analysis_ A Multi-Metric Assessment of 2D Projections_20250923|Selecting Optimal Camera Views for Gait Analysis: A Multi-Metric Assessment of 2D Projections]] (81.3% similar)
- [[2025-09-23/Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models_20250923|Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models]] (80.9% similar)
- [[2025-09-23/Cross-Corpus and Cross-domain Handwriting Assessment of NeuroDegenerative Diseases via Time-Series-to-Image Conversion_20250923|Cross-Corpus and Cross-domain Handwriting Assessment of NeuroDegenerative Diseases via Time-Series-to-Image Conversion]] (80.5% similar)
- [[2025-09-23/DynSTG-Mamba_ Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition_20250923|DynSTG-Mamba: Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Human Pose Estimation|Human Pose Estimation]], [[keywords/Turn-REMAP Dataset|Turn-REMAP Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2408.08182v4 Announce Type: replace-cross 
Abstract: People with Parkinson's Disease (PD) often experience progressively worsening gait, including changes in how they turn around, as the disease progresses. Existing clinical rating tools are not capable of capturing hour-by-hour variations of PD symptoms, as they are confined to brief assessments within clinic settings. Measuring gait turning angles continuously and passively is a component step towards using gait characteristics as sensitive indicators of disease progression in PD. This paper presents a deep learning-based approach to automatically quantify turning angles by extracting 3D skeletons from videos and calculating the rotation of hip and knee joints. We utilise state-of-the-art human pose estimation models, Fastpose and Strided Transformer, on a total of 1386 turning video clips from 24 subjects (12 people with PD and 12 healthy control volunteers), trimmed from a PD dataset of unscripted free-living videos in a home-like setting (Turn-REMAP). We also curate a turning video dataset, Turn-H3.6M, from the public Human3.6M human pose benchmark with 3D ground truth, to further validate our method. Previous gait research has primarily taken place in clinics or laboratories evaluating scripted gait outcomes, but this work focuses on free-living home settings where complexities exist, such as baggy clothing and poor lighting. Due to difficulties in obtaining accurate ground truth data in a free-living setting, we quantise the angle into the nearest bin $45^\circ$ based on the manual labelling of expert clinicians. Our method achieves a turning calculation accuracy of 41.6%, a Mean Absolute Error (MAE) of 34.7{\deg}, and a weighted precision WPrec of 68.3% for Turn-REMAP. This is the first work to explore the use of single monocular camera data to quantify turns by PD patients in a home setting.

## 📝 요약

이 논문은 파킨슨병(PD) 환자의 질병 진행을 민감하게 감지하기 위해 보행 특성을 활용하는 방법을 제안합니다. 기존의 임상 평가 도구는 시간별 증상 변화를 포착하지 못하지만, 이 연구는 비디오에서 3D 골격을 추출하고 고관절과 무릎 관절의 회전을 계산하여 회전 각도를 자동으로 정량화하는 딥러닝 기반 접근법을 제시합니다. Fastpose와 Strided Transformer 모델을 사용하여 24명의 피험자(12명의 PD 환자와 12명의 건강한 대조군)의 1386개의 회전 비디오 클립을 분석했습니다. 이 연구는 자유로운 생활 환경에서의 비디오 데이터를 사용하여, 기존의 임상 또는 실험실 환경에서의 연구와 차별화됩니다. 결과적으로, 제안된 방법은 Turn-REMAP 데이터셋에서 41.6%의 회전 계산 정확도와 34.7도의 평균 절대 오차(MAE), 68.3%의 가중 정밀도(WPrec)를 달성했습니다. 이는 가정 환경에서 단일 모노큘러 카메라 데이터를 사용하여 PD 환자의 회전을 정량화한 최초의 연구입니다.

## 🎯 주요 포인트

- 1. 파킨슨병 환자의 보행 변화, 특히 회전 동작을 자동으로 정량화하기 위해 딥러닝 기반 접근법을 제안합니다.
- 2. Fastpose와 Strided Transformer 모델을 활용하여 3D 스켈레톤을 추출하고, 엉덩이와 무릎 관절의 회전을 계산합니다.
- 3. Turn-REMAP 데이터셋을 사용하여 가정 환경에서 파킨슨병 환자의 회전을 단안 카메라로 측정하는 방법을 최초로 탐구합니다.
- 4. 자유로운 생활 환경에서의 회전 각도 측정을 위해 전문가의 수동 라벨링을 기반으로 각도를 $45^\circ$로 양자화합니다.
- 5. Turn-REMAP에서 회전 계산 정확도 41.6%, 평균 절대 오차 34.7도, 가중 정밀도 68.3%를 달성했습니다.


---

*Generated on 2025-09-24 14:24:25*