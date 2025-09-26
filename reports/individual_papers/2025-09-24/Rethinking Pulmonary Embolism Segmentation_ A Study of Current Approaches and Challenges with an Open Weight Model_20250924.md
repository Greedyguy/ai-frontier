<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:57:26.777098",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Pulmonary Embolism Segmentation",
    "3D U-Net",
    "Transformer",
    "ResNet",
    "Dice Score"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Pulmonary Embolism Segmentation": 0.8,
    "3D U-Net": 0.78,
    "Transformer": 0.75,
    "ResNet": 0.72,
    "Dice Score": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Pulmonary Embolism Segmentation",
        "canonical": "Pulmonary Embolism Segmentation",
        "aliases": [
          "PE Segmentation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the study, this term is specific to the medical imaging domain and connects related research on embolism detection.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "3D U-Net",
        "canonical": "3D U-Net",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A widely used architecture in medical image segmentation, facilitating connections with other studies using similar models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Links to the broader field of Transformer models, relevant in comparing CNN and Transformer-based architectures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "ResNet encoder",
        "canonical": "ResNet",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A key component in many neural networks, connecting to studies focusing on encoder architectures.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Dice score",
        "canonical": "Dice Score",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific metric for evaluating segmentation accuracy, relevant to performance assessment in medical imaging.",
        "novelty_score": 0.65,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "classification-based pretraining",
      "large PE datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Pulmonary Embolism Segmentation",
      "resolved_canonical": "Pulmonary Embolism Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "3D U-Net",
      "resolved_canonical": "3D U-Net",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "ResNet encoder",
      "resolved_canonical": "ResNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Dice score",
      "resolved_canonical": "Dice Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Rethinking Pulmonary Embolism Segmentation: A Study of Current Approaches and Challenges with an Open Weight Model

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18308.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18308](https://arxiv.org/abs/2509.18308)

## 🔗 유사한 논문
- [[2025-09-24/PolypSeg-GradCAM_ Towards Explainable Computer-Aided Gastrointestinal Disease Detection Using U-Net Based Segmentation and Grad-CAM Visualization on the Kvasir Dataset_20250924|PolypSeg-GradCAM: Towards Explainable Computer-Aided Gastrointestinal Disease Detection Using U-Net Based Segmentation and Grad-CAM Visualization on the Kvasir Dataset]] (83.6% similar)
- [[2025-09-23/A Semantic Segmentation Algorithm for Pleural Effusion Based on DBIF-AUNet_20250923|A Semantic Segmentation Algorithm for Pleural Effusion Based on DBIF-AUNet]] (83.3% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (83.1% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (82.5% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/3D U-Net|3D U-Net]], [[keywords/ResNet|ResNet]]
**⚡ Unique Technical**: [[keywords/Pulmonary Embolism Segmentation|Pulmonary Embolism Segmentation]], [[keywords/Dice Score|Dice Score]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18308v1 Announce Type: new 
Abstract: In this study, we curated a densely annotated in-house dataset comprising 490 CTPA scans. Using this dataset, we systematically evaluated nine widely used segmentation architectures from both the CNN and Vision Transformer (ViT) families, initialized with either pretrained or random weights, under a unified testing framework as a performance audit. Our study leads to several important observations: (1) 3D U-Net with a ResNet encoder remains a highly effective architecture for PE segmentation; (2) 3D models are particularly well-suited to this task given the morphological characteristics of emboli; (3) CNN-based models generally yield superior performance compared to their ViT-based counterparts in PE segmentation; (4) classification-based pretraining, even on large PE datasets, can adversely impact segmentation performance compared to training from scratch, suggesting that PE classification and segmentation may rely on different sets of discriminative features; (5) different model architectures show a highly consistent pattern of segmentation performance when trained on the same data; and (6) while central and large emboli can be segmented with satisfactory accuracy, distal emboli remain challenging due to both task complexity and the scarcity of high-quality datasets. Besides these findings, our best-performing model achieves a mean Dice score of 0.7131 for segmentation. It detects 181 emboli with 49 false positives and 28 false negatives from 60 in-house testing scans. Its generalizability is further validated on public datasets.

## 📝 요약

이 연구에서는 490개의 CTPA 스캔으로 구성된 데이터셋을 활용하여, CNN과 Vision Transformer(ViT) 기반의 9가지 세분화 아키텍처를 평가했습니다. 주요 발견 사항은 다음과 같습니다: (1) ResNet 인코더를 사용하는 3D U-Net이 폐색전증(PE) 세분화에 효과적입니다. (2) 3D 모델은 색전의 형태적 특성상 이 작업에 적합합니다. (3) CNN 기반 모델이 ViT 기반 모델보다 우수한 성능을 보입니다. (4) 대규모 PE 데이터셋에서의 분류 기반 사전 학습은 세분화 성능에 부정적 영향을 미칠 수 있습니다. (5) 동일한 데이터로 훈련된 모델 아키텍처는 일관된 성능 패턴을 보입니다. (6) 중심부 및 큰 색전은 정확하게 세분화되지만, 말초 색전은 데이터 부족과 작업 복잡성으로 인해 어려움이 있습니다. 최적의 모델은 평균 Dice 점수 0.7131을 기록하며, 60개의 테스트 스캔에서 181개의 색전을 탐지하고 49개의 오탐지 및 28개의 미탐지를 보였습니다. 이 모델의 일반화 가능성은 공개 데이터셋에서도 검증되었습니다.

## 🎯 주요 포인트

- 1. 3D U-Net와 ResNet 인코더를 결합한 모델은 폐색전증(PE) 세분화에 매우 효과적이다.
- 2. 3D 모델은 색전의 형태적 특성 때문에 PE 세분화 작업에 특히 적합하다.
- 3. CNN 기반 모델은 ViT 기반 모델보다 PE 세분화에서 일반적으로 우수한 성능을 보인다.
- 4. 대규모 PE 데이터셋에서의 분류 기반 사전 학습은 세분화 성능에 부정적인 영향을 미칠 수 있다.
- 5. 중심부 및 대형 색전은 만족스러운 정확도로 세분화할 수 있지만, 원위부 색전은 여전히 어려운 과제이다.


---

*Generated on 2025-09-24 15:57:26*