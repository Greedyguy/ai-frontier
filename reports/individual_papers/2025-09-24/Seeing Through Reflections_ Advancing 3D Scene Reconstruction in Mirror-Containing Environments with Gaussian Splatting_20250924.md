<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:13:42.372638",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Scene Reconstruction",
    "Neural Radiance Fields",
    "MirrorScene3D Dataset",
    "Reflective Gaussian Splatting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Scene Reconstruction": 0.72,
    "Neural Radiance Fields": 0.81,
    "MirrorScene3D Dataset": 0.79,
    "Reflective Gaussian Splatting": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Scene Reconstruction",
        "canonical": "3D Scene Reconstruction",
        "aliases": [
          "3D Reconstruction"
        ],
        "category": "broad_technical",
        "rationale": "3D Scene Reconstruction is a fundamental concept in computer vision, linking to various methods and datasets.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Neural Radiance Fields",
        "canonical": "Neural Radiance Fields",
        "aliases": [
          "NeRF"
        ],
        "category": "specific_connectable",
        "rationale": "Neural Radiance Fields are a key technique in novel view synthesis, connecting to advancements in rendering and scene understanding.",
        "novelty_score": 0.55,
        "connectivity_score": 0.84,
        "specificity_score": 0.78,
        "link_intent_score": 0.81
      },
      {
        "surface": "MirrorScene3D",
        "canonical": "MirrorScene3D Dataset",
        "aliases": [
          "MirrorScene3D"
        ],
        "category": "unique_technical",
        "rationale": "MirrorScene3D is a unique dataset specifically designed for evaluating 3D reconstruction in mirror-rich environments.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "ReflectiveGS",
        "canonical": "Reflective Gaussian Splatting",
        "aliases": [
          "ReflectiveGS"
        ],
        "category": "unique_technical",
        "rationale": "ReflectiveGS is a novel extension of 3D Gaussian Splatting, enhancing reconstruction quality by utilizing mirror reflections.",
        "novelty_score": 0.78,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Scene Reconstruction",
      "resolved_canonical": "3D Scene Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Neural Radiance Fields",
      "resolved_canonical": "Neural Radiance Fields",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.84,
        "specificity": 0.78,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "MirrorScene3D",
      "resolved_canonical": "MirrorScene3D Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "ReflectiveGS",
      "resolved_canonical": "Reflective Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Seeing Through Reflections: Advancing 3D Scene Reconstruction in Mirror-Containing Environments with Gaussian Splatting

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18956.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18956](https://arxiv.org/abs/2509.18956)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (85.6% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (84.6% similar)
- [[2025-09-23/Neural-MMGS_ Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction_20250923|Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction]] (84.0% similar)
- [[2025-09-23/MirrorSAM2_ Segment Mirror in Videos with Depth Perception_20250923|MirrorSAM2: Segment Mirror in Videos with Depth Perception]] (83.3% similar)
- [[2025-09-23/Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views_20250923|Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/3D Scene Reconstruction|3D Scene Reconstruction]]
**🔗 Specific Connectable**: [[keywords/Neural Radiance Fields|Neural Radiance Fields]]
**⚡ Unique Technical**: [[keywords/MirrorScene3D Dataset|MirrorScene3D Dataset]], [[keywords/Reflective Gaussian Splatting|Reflective Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18956v1 Announce Type: new 
Abstract: Mirror-containing environments pose unique challenges for 3D reconstruction and novel view synthesis (NVS), as reflective surfaces introduce view-dependent distortions and inconsistencies. While cutting-edge methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) excel in typical scenes, their performance deteriorates in the presence of mirrors. Existing solutions mainly focus on handling mirror surfaces through symmetry mapping but often overlook the rich information carried by mirror reflections. These reflections offer complementary perspectives that can fill in absent details and significantly enhance reconstruction quality. To advance 3D reconstruction in mirror-rich environments, we present MirrorScene3D, a comprehensive dataset featuring diverse indoor scenes, 1256 high-quality images, and annotated mirror masks, providing a benchmark for evaluating reconstruction methods in reflective settings. Building on this, we propose ReflectiveGS, an extension of 3D Gaussian Splatting that utilizes mirror reflections as complementary viewpoints rather than simple symmetry artifacts, enhancing scene geometry and recovering absent details. Experiments on MirrorScene3D show that ReflectiveGaussian outperforms existing methods in SSIM, PSNR, LPIPS, and training speed, setting a new benchmark for 3D reconstruction in mirror-rich environments.

## 📝 요약

이 논문은 거울이 포함된 환경에서 3D 재구성과 새로운 시점 합성(NVS)의 문제를 다룹니다. 기존 방법들은 거울 표면의 대칭 매핑에 주로 의존하지만, 거울 반사에 담긴 풍부한 정보를 간과합니다. 이를 해결하기 위해, 다양한 실내 장면과 1256개의 고품질 이미지, 주석이 달린 거울 마스크를 포함한 MirrorScene3D 데이터셋을 제시합니다. 또한, 3D Gaussian Splatting을 확장한 ReflectiveGS를 제안하여 거울 반사를 보조 시점으로 활용함으로써 장면의 기하학적 구조를 개선하고 누락된 세부 정보를 복원합니다. 실험 결과, ReflectiveGS는 SSIM, PSNR, LPIPS 및 학습 속도에서 기존 방법들을 능가하여 거울이 많은 환경에서의 3D 재구성에 새로운 기준을 제시합니다.

## 🎯 주요 포인트

- 1. 거울이 포함된 환경은 3D 재구성과 새로운 시점 합성(NVS)에 독특한 도전을 제기하며, 반사 표면이 시점 의존적인 왜곡과 불일치를 초래합니다.
- 2. MirrorScene3D는 다양한 실내 장면, 1256개의 고품질 이미지, 주석이 달린 거울 마스크를 포함한 포괄적인 데이터셋으로, 반사 환경에서 재구성 방법을 평가하기 위한 벤치마크를 제공합니다.
- 3. ReflectiveGS는 3D Gaussian Splatting의 확장으로, 거울 반사를 단순한 대칭 인공물이 아닌 보완적인 시점으로 활용하여 장면 기하학을 향상시키고 누락된 세부 정보를 복구합니다.
- 4. MirrorScene3D 실험에서 ReflectiveGaussian은 SSIM, PSNR, LPIPS, 학습 속도에서 기존 방법을 능가하며, 거울이 풍부한 환경에서 3D 재구성의 새로운 기준을 설정합니다.


---

*Generated on 2025-09-24 16:13:42*