<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:00:58.373929",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "BridgeSplat",
    "Non-Rigid Gaussian Splatting",
    "Deformable Surgical Navigation",
    "3D Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "BridgeSplat": 0.8,
    "Non-Rigid Gaussian Splatting": 0.75,
    "Deformable Surgical Navigation": 0.85,
    "3D Reconstruction": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "BridgeSplat",
        "canonical": "BridgeSplat",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "BridgeSplat is a novel method specific to this research, offering a unique approach to surgical navigation.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Non-Rigid Gaussian Splatting",
        "canonical": "Non-Rigid Gaussian Splatting",
        "aliases": [
          "Gaussian Splatting"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's methodology and provides a specific approach for deformable navigation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "Deformable Surgical Navigation",
        "canonical": "Deformable Surgical Navigation",
        "aliases": [
          "Surgical Navigation"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the application of the method in surgical settings.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "3D Reconstruction",
        "canonical": "3D Reconstruction",
        "aliases": [
          "3D Reconstruct"
        ],
        "category": "broad_technical",
        "rationale": "3D Reconstruction is a fundamental concept in computer vision, relevant to the paper's approach.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "BridgeSplat",
      "resolved_canonical": "BridgeSplat",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Non-Rigid Gaussian Splatting",
      "resolved_canonical": "Non-Rigid Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Deformable Surgical Navigation",
      "resolved_canonical": "Deformable Surgical Navigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "3D Reconstruction",
      "resolved_canonical": "3D Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# BridgeSplat: Bidirectionally Coupled CT and Non-Rigid Gaussian Splatting for Deformable Intraoperative Surgical Navigation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18501.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18501](https://arxiv.org/abs/2509.18501)

## 🔗 유사한 논문
- [[2025-09-23/Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views_20250923|Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views]] (84.9% similar)
- [[2025-09-23/DriveSplat_ Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians_20250923|DriveSplat: Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians]] (83.2% similar)
- [[2025-09-23/MedGS_ Gaussian Splatting for Multi-Modal 3D Medical Imaging_20250923|MedGS: Gaussian Splatting for Multi-Modal 3D Medical Imaging]] (81.8% similar)
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (81.4% similar)
- [[2025-09-23/SPFSplatV2_ Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views_20250923|SPFSplatV2: Efficient Self-Supervised Pose-Free 3D Gaussian Splatting from Sparse Views]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/3D Reconstruction|3D Reconstruction]]
**🔗 Specific Connectable**: [[keywords/Deformable Surgical Navigation|Deformable Surgical Navigation]]
**⚡ Unique Technical**: [[keywords/BridgeSplat|BridgeSplat]], [[keywords/Non-Rigid Gaussian Splatting|Non-Rigid Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18501v1 Announce Type: new 
Abstract: We introduce BridgeSplat, a novel approach for deformable surgical navigation that couples intraoperative 3D reconstruction with preoperative CT data to bridge the gap between surgical video and volumetric patient data. Our method rigs 3D Gaussians to a CT mesh, enabling joint optimization of Gaussian parameters and mesh deformation through photometric supervision. By parametrizing each Gaussian relative to its parent mesh triangle, we enforce alignment between Gaussians and mesh and obtain deformations that can be propagated back to update the CT. We demonstrate BridgeSplat's effectiveness on visceral pig surgeries and synthetic data of a human liver under simulation, showing sensible deformations of the preoperative CT on monocular RGB data. Code, data, and additional resources can be found at https://maxfehrentz.github.io/ct-informed-splatting/ .

## 📝 요약

BridgeSplat은 변형 가능한 외과 내비게이션을 위한 새로운 접근 방식으로, 수술 중 3D 재구성과 수술 전 CT 데이터를 결합하여 수술 비디오와 환자의 체적 데이터를 연결합니다. 이 방법은 3D 가우시안을 CT 메시에 연결하여 가우시안 매개변수와 메쉬 변형을 광학적 감독을 통해 공동 최적화합니다. 각 가우시안을 부모 메쉬 삼각형에 상대적으로 매개변수화하여 가우시안과 메쉬의 정렬을 보장하고, 변형을 CT에 반영할 수 있도록 합니다. 이 방법은 돼지 내장 수술과 인간 간의 시뮬레이션 데이터에서 효과적임을 입증하였습니다. 코드와 데이터는 온라인에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. BridgeSplat은 수술 비디오와 환자의 체적 데이터 간의 격차를 해소하기 위해 수술 중 3D 재구성과 수술 전 CT 데이터를 결합하는 새로운 접근 방식을 제안합니다.
- 2. 이 방법은 3D 가우시안을 CT 메시에 연결하여 가우시안 매개변수와 메쉬 변형을 광도 감독을 통해 공동 최적화합니다.
- 3. 각 가우시안을 부모 메쉬 삼각형에 상대적으로 매개변수화하여 가우시안과 메쉬 간의 정렬을 보장하고 변형을 CT 업데이트에 반영할 수 있습니다.
- 4. BridgeSplat의 효과는 내장 돼지 수술과 시뮬레이션된 인간 간의 합성 데이터에서 입증되었으며, 단안 RGB 데이터에서 수술 전 CT의 합리적인 변형을 보여줍니다.


---

*Generated on 2025-09-24 16:00:58*