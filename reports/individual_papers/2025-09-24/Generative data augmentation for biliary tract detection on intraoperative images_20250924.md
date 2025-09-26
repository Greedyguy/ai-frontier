<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:15:16.133834",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Adversarial Network",
    "Deep Learning",
    "Yolo",
    "Biliary Tract Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Generative Adversarial Network": 0.88,
    "Deep Learning": 0.7,
    "Yolo": 0.82,
    "Biliary Tract Detection": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Generative Adversarial Network",
        "canonical": "Generative Adversarial Network",
        "aliases": [
          "GAN"
        ],
        "category": "specific_connectable",
        "rationale": "GANs are a key component in generating synthetic data, enhancing the dataset for better model training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is the foundational technology for the proposed localization approach.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Yolo detection algorithm",
        "canonical": "Yolo",
        "aliases": [
          "You Only Look Once"
        ],
        "category": "unique_technical",
        "rationale": "Yolo is a specific object detection algorithm crucial for the localization task in the study.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Biliary tract detection",
        "canonical": "Biliary Tract Detection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is the primary application focus of the paper, linking medical imaging with AI techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "Cholecystectomy",
      "laparoscopic approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Generative Adversarial Network",
      "resolved_canonical": "Generative Adversarial Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Yolo detection algorithm",
      "resolved_canonical": "Yolo",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Biliary tract detection",
      "resolved_canonical": "Biliary Tract Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Generative data augmentation for biliary tract detection on intraoperative images

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18958.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18958](https://arxiv.org/abs/2509.18958)

## 🔗 유사한 논문
- [[2025-09-23/X-GAN_ A Generative AI-Powered Unsupervised Model for Main Vessel Segmentation of Glaucoma Screening_20250923|X-GAN: A Generative AI-Powered Unsupervised Model for Main Vessel Segmentation of Glaucoma Screening]] (84.0% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (83.0% similar)
- [[2025-09-23/Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images_20250923|Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images]] (82.7% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (82.2% similar)
- [[2025-09-19/Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery_20250919|Affordance-Based Disambiguation of Surgical Instructions for Collaborative Robot-Assisted Surgery]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Generative Adversarial Network|Generative Adversarial Network]]
**⚡ Unique Technical**: [[keywords/Yolo|Yolo]], [[keywords/Biliary Tract Detection|Biliary Tract Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18958v1 Announce Type: cross 
Abstract: Cholecystectomy is one of the most frequently performed procedures in gastrointestinal surgery, and the laparoscopic approach is the gold standard for symptomatic cholecystolithiasis and acute cholecystitis. In addition to the advantages of a significantly faster recovery and better cosmetic results, the laparoscopic approach bears a higher risk of bile duct injury, which has a significant impact on quality of life and survival. To avoid bile duct injury, it is essential to improve the intraoperative visualization of the bile duct. This work aims to address this problem by leveraging a deep-learning approach for the localization of the biliary tract from white-light images acquired during the surgical procedures. To this end, the construction and annotation of an image database to train the Yolo detection algorithm has been employed. Besides classical data augmentation techniques, the paper proposes Generative Adversarial Network (GAN) for the generation of a synthetic portion of the training dataset. Experimental results have been discussed along with ethical considerations.

## 📝 요약

이 연구는 복강경 담낭절제술 중 담관 손상을 방지하기 위해 심층 학습을 활용하여 담관의 위치를 정확히 파악하는 방법을 제안합니다. 이를 위해 Yolo 탐지 알고리즘을 훈련시키기 위한 이미지 데이터베이스를 구축하고 주석을 달았습니다. 또한, 전통적인 데이터 증강 기법 외에도 GAN을 사용하여 합성 데이터를 생성했습니다. 실험 결과와 윤리적 고려 사항도 논의되었습니다. 이 방법은 수술 중 담관 시각화를 개선하여 환자의 삶의 질과 생존율에 긍정적인 영향을 미칠 수 있습니다.

## 🎯 주요 포인트

- 1. 복강경 담낭절제술은 빠른 회복과 미용적 장점이 있지만 담관 손상의 위험이 높습니다.
- 2. 담관 손상을 방지하기 위해 수술 중 담관의 시각화를 개선하는 것이 중요합니다.
- 3. 본 연구는 수술 중 획득한 백색광 이미지를 통해 담관을 위치 파악하기 위해 딥러닝 접근 방식을 활용합니다.
- 4. Yolo 탐지 알고리즘을 훈련하기 위한 이미지 데이터베이스의 구축과 주석 작업이 수행되었습니다.
- 5. 데이터 증강 기법 외에도 GAN을 활용하여 합성 훈련 데이터셋을 생성하는 방법을 제안합니다.


---

*Generated on 2025-09-24 15:15:16*