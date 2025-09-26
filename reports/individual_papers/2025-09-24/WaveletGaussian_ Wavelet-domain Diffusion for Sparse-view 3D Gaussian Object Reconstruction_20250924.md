<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:15:03.733428",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "WaveletGaussian",
    "Diffusion Models",
    "Sparse-view 3D Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "WaveletGaussian": 0.82,
    "Diffusion Models": 0.7,
    "Sparse-view 3D Reconstruction": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper's contribution, offering a unique approach to object reconstruction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "WaveletGaussian",
        "canonical": "WaveletGaussian",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents the novel framework introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A key concept in the paper, linking to broader discussions in machine learning and image processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Sparse-view 3D Reconstruction",
        "canonical": "Sparse-view 3D Reconstruction",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This is a specific problem domain addressed by the paper, connecting to similar research in 3D reconstruction.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
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
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "WaveletGaussian",
      "resolved_canonical": "WaveletGaussian",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Sparse-view 3D Reconstruction",
      "resolved_canonical": "Sparse-view 3D Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19073.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19073](https://arxiv.org/abs/2509.19073)

## 🔗 유사한 논문
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (86.8% similar)
- [[2025-09-23/Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning_20250923|Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning]] (86.1% similar)
- [[2025-09-23/AD-GS_ Alternating Densification for Sparse-Input 3D Gaussian Splatting_20250923|AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting]] (86.1% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (85.9% similar)
- [[2025-09-23/Neural-MMGS_ Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction_20250923|Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction]] (85.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Sparse-view 3D Reconstruction|Sparse-view 3D Reconstruction]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/WaveletGaussian|WaveletGaussian]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19073v1 Announce Type: new 
Abstract: 3D Gaussian Splatting (3DGS) has become a powerful representation for image-based object reconstruction, yet its performance drops sharply in sparse-view settings. Prior works address this limitation by employing diffusion models to repair corrupted renders, subsequently using them as pseudo ground truths for later optimization. While effective, such approaches incur heavy computation from the diffusion fine-tuning and repair steps. We present WaveletGaussian, a framework for more efficient sparse-view 3D Gaussian object reconstruction. Our key idea is to shift diffusion into the wavelet domain: diffusion is applied only to the low-resolution LL subband, while high-frequency subbands are refined with a lightweight network. We further propose an efficient online random masking strategy to curate training pairs for diffusion fine-tuning, replacing the commonly used, but inefficient, leave-one-out strategy. Experiments across two benchmark datasets, Mip-NeRF 360 and OmniObject3D, show WaveletGaussian achieves competitive rendering quality while substantially reducing training time.

## 📝 요약

WaveletGaussian은 3D Gaussian Splatting(3DGS)의 성능 저하 문제를 해결하기 위해 제안된 프레임워크로, 특히 sparse-view 환경에서 효율적인 객체 재구성을 목표로 합니다. 기존 방법들은 디퓨전 모델을 사용하여 손상된 렌더링을 복구하지만, 이는 높은 계산 비용을 초래합니다. WaveletGaussian은 디퓨전을 웨이블릿 도메인으로 이동시켜 저해상도 LL 서브밴드에만 적용하고, 고주파 서브밴드는 경량 네트워크로 보완합니다. 또한, 효율적인 온라인 랜덤 마스킹 전략을 도입하여 디퓨전 미세 조정을 위한 훈련 데이터를 생성합니다. Mip-NeRF 360과 OmniObject3D 데이터셋 실험 결과, WaveletGaussian은 경쟁력 있는 렌더링 품질을 유지하면서 훈련 시간을 크게 단축시켰습니다.

## 🎯 주요 포인트

- 1. 3D Gaussian Splatting은 이미지 기반 객체 재구성에 강력하지만, 희소 뷰 설정에서는 성능이 급격히 저하됩니다.
- 2. 기존 연구들은 확산 모델을 사용하여 손상된 렌더를 복구하고 이를 최적화의 가상 기준으로 사용하지만, 이는 높은 계산 비용을 초래합니다.
- 3. WaveletGaussian은 희소 뷰 3D Gaussian 객체 재구성을 더 효율적으로 수행하기 위해 확산을 웨이블릿 도메인으로 전환하는 프레임워크입니다.
- 4. WaveletGaussian은 저해상도 LL 서브밴드에만 확산을 적용하고, 고주파 서브밴드는 경량 네트워크로 정제합니다.
- 5. 실험 결과, WaveletGaussian은 Mip-NeRF 360 및 OmniObject3D 데이터셋에서 경쟁력 있는 렌더링 품질을 유지하면서도 훈련 시간을 크게 단축합니다.


---

*Generated on 2025-09-24 16:15:03*