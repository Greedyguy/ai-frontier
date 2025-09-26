---
keywords:
  - Remote Sensing Change Caption
  - Vision-Language Model
  - Disaster Monitoring
  - Bi-temporal Understanding
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.01907
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:53:23.483855",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Remote Sensing Change Caption",
    "Vision-Language Model",
    "Disaster Monitoring",
    "Bi-temporal Understanding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Remote Sensing Change Caption": 0.8,
    "Vision-Language Model": 0.85,
    "Disaster Monitoring": 0.8,
    "Bi-temporal Understanding": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Remote Sensing Change Caption",
        "canonical": "Remote Sensing Change Caption",
        "aliases": [
          "RSCC"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel dataset specifically designed for bi-temporal disaster analysis, enhancing connectivity in remote sensing research.",
        "novelty_score": 0.9,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Connects to the growing field of integrating visual and textual data, crucial for interpreting remote sensing data.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Disaster Monitoring",
        "canonical": "Disaster Monitoring",
        "aliases": [
          "Disaster Surveillance"
        ],
        "category": "specific_connectable",
        "rationale": "Key application area for remote sensing, linking to broader disaster management and response strategies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Bi-temporal Understanding",
        "canonical": "Bi-temporal Understanding",
        "aliases": [
          "Temporal Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for analyzing changes over time in remote sensing, enhancing model training and evaluation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.8,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "disaster events",
      "temporal image pairs",
      "detailed textual annotations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Remote Sensing Change Caption",
      "resolved_canonical": "Remote Sensing Change Caption",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Disaster Monitoring",
      "resolved_canonical": "Disaster Monitoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Bi-temporal Understanding",
      "resolved_canonical": "Bi-temporal Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.8,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# RSCC: A Large-Scale Remote Sensing Change Caption Dataset for Disaster Events

**Korean Title:** RSCC: 재난 사건을 위한 대규모 원격 감지 변화 캡션 데이터셋

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.01907.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.01907](https://arxiv.org/abs/2509.01907)

## 🔗 유사한 논문
- [[2025-09-22/DC-Mamba_ Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection_20250922|DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection]] (84.3% similar)
- [[2025-09-22/SAR-TEXT_ A Large-Scale SAR Image-Text Dataset Built with SAR-Narrator and Progressive Transfer Learning_20250922|SAR-TEXT: A Large-Scale SAR Image-Text Dataset Built with SAR-Narrator and Progressive Transfer Learning]] (82.8% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (81.7% similar)
- [[2025-09-22/Semantic Change Detection of Roads and Bridges_ A Fine-grained Dataset and Multimodal Frequency-driven Detector_20250922|Semantic Change Detection of Roads and Bridges: A Fine-grained Dataset and Multimodal Frequency-driven Detector]] (81.4% similar)
- [[2025-09-22/FoBa_ A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection_20250922|FoBa: A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Disaster Monitoring|Disaster Monitoring]], [[keywords/Bi-temporal Understanding|Bi-temporal Understanding]]
**⚡ Unique Technical**: [[keywords/Remote Sensing Change Caption|Remote Sensing Change Caption]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01907v4 Announce Type: replace-cross 
Abstract: Remote sensing is critical for disaster monitoring, yet existing datasets lack temporal image pairs and detailed textual annotations. While single-snapshot imagery dominates current resources, it fails to capture dynamic disaster impacts over time. To address this gap, we introduce the Remote Sensing Change Caption (RSCC) dataset, a large-scale benchmark comprising 62,315 pre-/post-disaster image pairs (spanning earthquakes, floods, wildfires, and more) paired with rich, human-like change captions. By bridging the temporal and semantic divide in remote sensing data, RSCC enables robust training and evaluation of vision-language models for disaster-aware bi-temporal understanding. Our results highlight RSCC's ability to facilitate detailed disaster-related analysis, paving the way for more accurate, interpretable, and scalable vision-language applications in remote sensing. Code and dataset are available at https://github.com/Bili-Sakura/RSCC.

## 🔍 Abstract (한글 번역)

arXiv:2509.01907v4 발표 유형: 교차 교체  
초록: 원격 감지는 재해 모니터링에 필수적이지만, 기존 데이터셋은 시간적 이미지 쌍과 상세한 텍스트 주석이 부족합니다. 단일 스냅샷 이미지는 현재 자원을 지배하지만, 이는 시간이 지남에 따라 변화하는 재해 영향을 포착하지 못합니다. 이 격차를 해소하기 위해, 우리는 원격 감지 변화 캡션(RSCC) 데이터셋을 소개합니다. 이는 지진, 홍수, 산불 등을 포함한 62,315개의 재해 전후 이미지 쌍과 풍부하고 인간적인 변화 캡션을 포함하는 대규모 벤치마크입니다. 원격 감지 데이터의 시간적 및 의미적 간극을 연결함으로써, RSCC는 재해 인식 이중 시간 이해를 위한 비전-언어 모델의 강력한 훈련 및 평가를 가능하게 합니다. 우리의 결과는 RSCC가 상세한 재해 관련 분석을 촉진할 수 있는 능력을 강조하며, 원격 감지에서 더 정확하고 해석 가능하며 확장 가능한 비전-언어 응용 프로그램의 길을 열어줍니다. 코드와 데이터셋은 https://github.com/Bili-Sakura/RSCC에서 사용할 수 있습니다.

## 📝 요약

이 논문은 재난 모니터링을 위한 원격 감지 데이터셋의 한계를 극복하기 위해 RSCC 데이터셋을 소개합니다. RSCC는 62,315개의 재난 전후 이미지 쌍과 상세한 변화 설명을 포함하여, 시각-언어 모델의 재난 인식 능력을 향상시킵니다. 이를 통해 보다 정확하고 해석 가능한 원격 감지 응용 프로그램 개발을 촉진합니다.

## 🎯 주요 포인트

- 1. 기존 원격 감지 데이터셋은 시간적 이미지 쌍과 상세한 텍스트 주석이 부족하다.
- 2. RSCC 데이터셋은 62,315개의 재난 전후 이미지 쌍과 풍부한 변화 설명을 포함한 대규모 벤치마크이다.
- 3. RSCC는 원격 감지 데이터의 시간적 및 의미적 격차를 해소하여 재난 인식 이중 시간 이해를 위한 비전-언어 모델의 강력한 훈련 및 평가를 가능하게 한다.
- 4. RSCC는 재난 관련 분석을 용이하게 하여 원격 감지에서 더 정확하고 해석 가능하며 확장 가능한 비전-언어 응용 프로그램을 위한 길을 열어준다.
- 5. 코드와 데이터셋은 https://github.com/Bili-Sakura/RSCC에서 제공된다.


---

*Generated on 2025-09-23 11:53:23*