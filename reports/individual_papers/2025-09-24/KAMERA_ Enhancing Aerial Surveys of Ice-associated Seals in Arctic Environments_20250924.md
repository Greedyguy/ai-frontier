<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:16:41.132301",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "KAMERA System",
    "Multi-Camera Synchronization",
    "Multi-Spectral Detection",
    "Aerial Surveys"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "KAMERA System": 0.8,
    "Multi-Camera Synchronization": 0.78,
    "Multi-Spectral Detection": 0.79,
    "Aerial Surveys": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "KAMERA",
        "canonical": "KAMERA System",
        "aliases": [
          "KAMERA"
        ],
        "category": "unique_technical",
        "rationale": "KAMERA is a unique system introduced in the paper, providing a novel approach to aerial surveys with significant improvements in processing time.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-camera synchronization",
        "canonical": "Multi-Camera Synchronization",
        "aliases": [
          "camera synchronization"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is crucial for the system's functionality and can connect to broader topics in computer vision and imaging technologies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-spectral detection",
        "canonical": "Multi-Spectral Detection",
        "aliases": [
          "spectral detection"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-spectral detection is a key feature of the system, relevant to fields like remote sensing and environmental monitoring.",
        "novelty_score": 0.68,
        "connectivity_score": 0.77,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "aerial surveys",
        "canonical": "Aerial Surveys",
        "aliases": [
          "aerial survey"
        ],
        "category": "broad_technical",
        "rationale": "Aerial surveys are a fundamental method in environmental monitoring and wildlife studies, providing a broad connection to related research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "real-time detection",
      "dataset processing time"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "KAMERA",
      "resolved_canonical": "KAMERA System",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-camera synchronization",
      "resolved_canonical": "Multi-Camera Synchronization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-spectral detection",
      "resolved_canonical": "Multi-Spectral Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.77,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "aerial surveys",
      "resolved_canonical": "Aerial Surveys",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# KAMERA: Enhancing Aerial Surveys of Ice-associated Seals in Arctic Environments

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19129.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19129](https://arxiv.org/abs/2509.19129)

## 🔗 유사한 논문
- [[2025-09-23/Subjective Camera 1.0_ Bridging Human Cognition and Visual Reconstruction through Sequence-Aware Sketch-Guided Diffusion_20250923|Subjective Camera 1.0: Bridging Human Cognition and Visual Reconstruction through Sequence-Aware Sketch-Guided Diffusion]] (80.2% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (79.7% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (79.4% similar)
- [[2025-09-23/RCTDistill_ Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion_20250923|RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion]] (79.1% similar)
- [[2025-09-23/CameraVDP_ Perceptual Display Assessment with Uncertainty Estimation via Camera and Visual Difference Prediction_20250923|CameraVDP: Perceptual Display Assessment with Uncertainty Estimation via Camera and Visual Difference Prediction]] (78.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Aerial Surveys|Aerial Surveys]]
**🔗 Specific Connectable**: [[keywords/Multi-Camera Synchronization|Multi-Camera Synchronization]], [[keywords/Multi-Spectral Detection|Multi-Spectral Detection]]
**⚡ Unique Technical**: [[keywords/KAMERA System|KAMERA System]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19129v1 Announce Type: new 
Abstract: We introduce KAMERA: a comprehensive system for multi-camera, multi-spectral synchronization and real-time detection of seals and polar bears. Utilized in aerial surveys for ice-associated seals in the Bering, Chukchi, and Beaufort seas around Alaska, KAMERA provides up to an 80% reduction in dataset processing time over previous methods. Our rigorous calibration and hardware synchronization enable using multiple spectra for object detection. All collected data are annotated with metadata so they can be easily referenced later. All imagery and animal detections from a survey are mapped onto a world plane for accurate surveyed area estimates and quick assessment of survey results. We hope KAMERA will inspire other mapping and detection efforts in the scientific community, with all software, models, and schematics fully open-sourced.

## 📝 요약

KAMERA는 알래스카 주변 해역에서 얼음과 관련된 물개와 북극곰을 실시간으로 탐지하기 위한 다중 카메라 및 다중 스펙트럼 동기화 시스템입니다. 기존 방법보다 데이터셋 처리 시간을 최대 80% 단축하며, 엄격한 보정과 하드웨어 동기화를 통해 여러 스펙트럼을 활용한 객체 탐지가 가능합니다. 수집된 모든 데이터는 메타데이터와 함께 주석 처리되어 이후 참조가 용이하며, 조사 결과는 정확한 면적 추정과 빠른 평가를 위해 세계 평면에 매핑됩니다. KAMERA는 모든 소프트웨어, 모델, 설계도를 오픈 소스로 제공하여 과학 공동체의 다른 매핑 및 탐지 노력에 영감을 주고자 합니다.

## 🎯 주요 포인트

- 1. KAMERA는 다중 카메라 및 다중 스펙트럼 동기화 시스템으로, 실시간으로 바다표범과 북극곰을 탐지합니다.
- 2. 이 시스템은 알래스카 주변의 빙하 관련 바다표범 항공 조사에서 데이터 처리 시간을 최대 80%까지 단축합니다.
- 3. 엄격한 보정과 하드웨어 동기화를 통해 여러 스펙트럼을 활용한 객체 탐지가 가능합니다.
- 4. 수집된 모든 데이터는 메타데이터로 주석 처리되어 나중에 쉽게 참조할 수 있습니다.
- 5. KAMERA는 모든 소프트웨어, 모델, 설계도가 오픈 소스로 제공되어 과학 커뮤니티의 다른 매핑 및 탐지 노력에 영감을 주기를 기대합니다.


---

*Generated on 2025-09-24 16:16:41*