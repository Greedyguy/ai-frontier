<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:34:12.381484",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Neural Unsigned Distance Functions",
    "Bone Surface Reconstruction",
    "Local Tangent Plane Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.8,
    "Neural Unsigned Distance Functions": 0.78,
    "Bone Surface Reconstruction": 0.77,
    "Local Tangent Plane Optimization": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised framework",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised model",
          "self-supervised approach"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing work on self-supervised learning, which is crucial for understanding the methodology.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Neural unsigned distance functions",
        "canonical": "Neural Unsigned Distance Functions",
        "aliases": [
          "neural UDFs",
          "unsigned distance functions"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach specific to this paper, enhancing the understanding of the proposed method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bone surface reconstruction",
        "canonical": "Bone Surface Reconstruction",
        "aliases": [
          "bone reconstruction",
          "surface reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, linking to broader orthopedic and imaging research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Local tangent plane optimization",
        "canonical": "Local Tangent Plane Optimization",
        "aliases": [
          "tangent plane optimization",
          "local plane optimization"
        ],
        "category": "unique_technical",
        "rationale": "Highlights a specific technique used to improve reconstruction quality, relevant for technical discussions.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised framework",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Neural unsigned distance functions",
      "resolved_canonical": "Neural Unsigned Distance Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bone surface reconstruction",
      "resolved_canonical": "Bone Surface Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Local tangent plane optimization",
      "resolved_canonical": "Local Tangent Plane Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# UltraBoneUDF: Self-supervised Bone Surface Reconstruction from Ultrasound Based on Neural Unsigned Distance Functions

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2505.17912.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2505.17912](https://arxiv.org/abs/2505.17912)

## 🔗 유사한 논문
- [[2025-09-23/High Resolution UDF Meshing via Iterative Networks_20250923|High Resolution UDF Meshing via Iterative Networks]] (85.5% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (80.4% similar)
- [[2025-09-22/Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss_20250922|Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss]] (80.2% similar)
- [[2025-09-23/GeoSVR_ Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction_20250923|GeoSVR: Taming Sparse Voxels for Geometrically Accurate Surface Reconstruction]] (79.5% similar)
- [[2025-09-24/Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning_20250924|Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Neural Unsigned Distance Functions|Neural Unsigned Distance Functions]], [[keywords/Bone Surface Reconstruction|Bone Surface Reconstruction]], [[keywords/Local Tangent Plane Optimization|Local Tangent Plane Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.17912v3 Announce Type: replace-cross 
Abstract: Bone surface reconstruction is an essential component of computer-assisted orthopedic surgery (CAOS), forming the foundation for preoperative planning and intraoperative guidance. Compared to traditional imaging modalities such as CT and MRI, ultrasound provides a radiation-free, and cost-effective alternative. While ultrasound offers new opportunities in CAOS, technical shortcomings continue to hinder its translation into surgery. In particular, due to the inherent limitations of ultrasound imaging, B-mode ultrasound typically capture only partial bone surfaces, posing major challenges for surface reconstruction. Existing reconstruction methods struggle with such incomplete data, leading to increased reconstruction errors and artifacts. Effective techniques for accurately reconstructing open bone surfaces from real-world 3D ultrasound volumes remain lacking. We propose UltraBoneUDF, a self-supervised framework specifically designed for reconstructing open bone surfaces from ultrasound data using neural unsigned distance functions (UDFs). In addition, we present a novel loss function based on local tangent plane optimization that substantially improves surface reconstruction quality. UltraBoneUDF and competing models are benchmarked on three open-source datasets and further evaluated through ablation studies. Results: Qualitative results highlight the limitations of the state-of-the-art methods for open bone surface reconstruction and demonstrate the effectiveness of UltraBoneUDF. Quantitatively, UltraBoneUDF significantly outperforms competing methods across all evaluated datasets for both open and closed bone surface reconstruction in terms of mean Chamfer distance error: 0.96 mm on the UltraBones100k dataset (28.9% improvement compared to the state-of-the-art), 0.21 mm on the OpenBoneCT dataset (40.0% improvement), and 0.18 mm on the ClosedBoneCT dataset (63.3% improvement).

## 📝 요약

초음파를 활용한 뼈 표면 재구성은 방사선 노출이 없고 비용 효율적인 대안이지만, 기존 방법들은 불완전한 데이터로 인해 오류가 발생합니다. 본 논문에서는 초음파 데이터를 이용해 뼈 표면을 재구성하는 UltraBoneUDF라는 자가 지도 학습 프레임워크를 제안합니다. 특히, 지역 접선 평면 최적화를 기반으로 한 새로운 손실 함수를 도입하여 재구성 품질을 크게 향상시켰습니다. UltraBoneUDF는 세 가지 공개 데이터셋에서 기존 방법들보다 평균 챔퍼 거리 오류 측면에서 28.9%에서 63.3%까지 개선된 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 본 연구는 초음파 데이터를 활용한 개방형 골 표면 재구성을 위해 신경 비서명 거리 함수(UDF)를 사용하는 자가 지도 학습 프레임워크인 UltraBoneUDF를 제안합니다.
- 2. UltraBoneUDF는 국소 접선 평면 최적화에 기반한 새로운 손실 함수를 도입하여 표면 재구성 품질을 크게 향상시킵니다.
- 3. UltraBoneUDF는 세 가지 오픈 소스 데이터셋에서 기존 방법들과 비교 평가되었으며, 모든 데이터셋에서 평균 챔퍼 거리 오류 측면에서 경쟁 방법들보다 우수한 성능을 보였습니다.
- 4. 정량적 결과에서 UltraBoneUDF는 UltraBones100k, OpenBoneCT, ClosedBoneCT 데이터셋에서 각각 28.9%, 40.0%, 63.3%의 개선을 보여주었습니다.
- 5. 정성적 결과는 최신 방법들이 개방형 골 표면 재구성에서 가지는 한계를 강조하며, UltraBoneUDF의 효과성을 입증합니다.


---

*Generated on 2025-09-24 16:34:12*