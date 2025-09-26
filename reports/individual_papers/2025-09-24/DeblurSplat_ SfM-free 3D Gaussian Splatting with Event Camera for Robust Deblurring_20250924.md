<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:11:36.287524",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Event Camera",
    "Structure-from-Motion",
    "Dense Stereo Module"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Event Camera": 0.8,
    "Structure-from-Motion": 0.72,
    "Dense Stereo Module": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3D-GS"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique specific to the paper, providing a unique contribution to 3D rendering and deblurring methods.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Event Camera",
        "canonical": "Event Camera",
        "aliases": [
          "Dynamic Vision Sensor"
        ],
        "category": "specific_connectable",
        "rationale": "Event cameras are increasingly used in computer vision for capturing dynamic scenes, offering strong connectivity with related research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Structure-from-Motion",
        "canonical": "Structure-from-Motion",
        "aliases": [
          "SfM"
        ],
        "category": "broad_technical",
        "rationale": "As a foundational technique in 3D reconstruction, it connects well with a broad range of computer vision research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Dense Stereo Module",
        "canonical": "Dense Stereo Module",
        "aliases": [
          "DUSt3R"
        ],
        "category": "unique_technical",
        "rationale": "This module is specific to the paper's method, providing a distinct point of discussion in stereo vision techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
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
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Event Camera",
      "resolved_canonical": "Event Camera",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Structure-from-Motion",
      "resolved_canonical": "Structure-from-Motion",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Dense Stereo Module",
      "resolved_canonical": "Dense Stereo Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# DeblurSplat: SfM-free 3D Gaussian Splatting with Event Camera for Robust Deblurring

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18898.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18898](https://arxiv.org/abs/2509.18898)

## 🔗 유사한 논문
- [[2025-09-22/Camera Splatting for Continuous View Optimization_20250922|Camera Splatting for Continuous View Optimization]] (85.4% similar)
- [[2025-09-23/DriveSplat_ Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians_20250923|DriveSplat: Decoupled Driving Scene Reconstruction with Geometry-enhanced Partitioned Neural Gaussians]] (85.3% similar)
- [[2025-09-24/Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction_20250924|Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction]] (84.5% similar)
- [[2025-09-23/From Restoration to Reconstruction_ Rethinking 3D Gaussian Splatting for Underwater Scenes_20250923|From Restoration to Reconstruction: Rethinking 3D Gaussian Splatting for Underwater Scenes]] (84.4% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Structure-from-Motion|Structure-from-Motion]]
**🔗 Specific Connectable**: [[keywords/Event Camera|Event Camera]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Dense Stereo Module|Dense Stereo Module]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18898v1 Announce Type: new 
Abstract: In this paper, we propose the first Structure-from-Motion (SfM)-free deblurring 3D Gaussian Splatting method via event camera, dubbed DeblurSplat. We address the motion-deblurring problem in two ways. First, we leverage the pretrained capability of the dense stereo module (DUSt3R) to directly obtain accurate initial point clouds from blurred images. Without calculating camera poses as an intermediate result, we avoid the cumulative errors transfer from inaccurate camera poses to the initial point clouds' positions. Second, we introduce the event stream into the deblur pipeline for its high sensitivity to dynamic change. By decoding the latent sharp images from the event stream and blurred images, we can provide a fine-grained supervision signal for scene reconstruction optimization. Extensive experiments across a range of scenes demonstrate that DeblurSplat not only excels in generating high-fidelity novel views but also achieves significant rendering efficiency compared to the SOTAs in deblur 3D-GS.

## 📝 요약

이 논문에서는 이벤트 카메라를 활용한 최초의 SfM(Structure-from-Motion) 비의존 3D 가우시안 스플래팅 디블러링 방법인 DeblurSplat을 제안합니다. 첫째, 사전 학습된 밀집 스테레오 모듈(DUSt3R)을 활용하여 흐릿한 이미지로부터 정확한 초기 포인트 클라우드를 직접 얻어내며, 카메라 자세를 계산하지 않아 누적 오류를 방지합니다. 둘째, 이벤트 스트림을 디블러 파이프라인에 도입하여 동적 변화에 민감한 이벤트 스트림과 흐릿한 이미지로부터 선명한 이미지를 복원함으로써 장면 재구성 최적화를 위한 세밀한 감독 신호를 제공합니다. 다양한 실험 결과, DeblurSplat은 고품질의 새로운 시각을 생성하고, 기존 방법들에 비해 뛰어난 렌더링 효율성을 달성함을 보여줍니다.

## 🎯 주요 포인트

- 1. DeblurSplat은 Structure-from-Motion(SfM) 없이 이벤트 카메라를 활용한 3D Gaussian Splatting 기반의 첫 번째 디블러링 방법을 제안합니다.
- 2. DUSt3R 모듈을 활용하여 흐릿한 이미지로부터 정확한 초기 포인트 클라우드를 직접 얻어내어 카메라 포즈 계산에 따른 누적 오류를 방지합니다.
- 3. 이벤트 스트림을 디블러 파이프라인에 도입하여 역동적인 변화에 대한 높은 감도를 활용하고, 이를 통해 장면 재구성 최적화를 위한 세밀한 감독 신호를 제공합니다.
- 4. 다양한 장면에서의 실험 결과, DeblurSplat은 높은 충실도의 새로운 뷰를 생성할 뿐만 아니라 기존 최첨단 기술(SOTAs) 대비 뛰어난 렌더링 효율성을 달성합니다.


---

*Generated on 2025-09-24 16:11:36*