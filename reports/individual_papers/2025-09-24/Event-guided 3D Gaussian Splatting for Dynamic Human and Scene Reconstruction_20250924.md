<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:02:26.161174",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Event Camera",
    "Human-Scene Reconstruction",
    "Event-Guided Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Event Camera": 0.82,
    "Human-Scene Reconstruction": 0.75,
    "Event-Guided Loss": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "Gaussian Splatting"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's method and offers a unique approach to human-scene reconstruction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Event Camera",
        "canonical": "Event Camera",
        "aliases": [
          "Dynamic Vision Sensor"
        ],
        "category": "specific_connectable",
        "rationale": "Event cameras are crucial for handling fast motion and reducing blur, linking to dynamic vision research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Human-Scene Reconstruction",
        "canonical": "Human-Scene Reconstruction",
        "aliases": [
          "Dynamic Human Reconstruction"
        ],
        "category": "broad_technical",
        "rationale": "This is the core application area of the paper, relevant to computer vision and 3D modeling fields.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Event-Guided Loss",
        "canonical": "Event-Guided Loss",
        "aliases": [
          "Event-Based Loss"
        ],
        "category": "unique_technical",
        "rationale": "The event-guided loss is a novel contribution that enhances reconstruction fidelity, especially in dynamic scenes.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "monocular videos",
      "motion blur",
      "PSNR/SSIM",
      "LPIPS"
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
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Event Camera",
      "resolved_canonical": "Event Camera",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Human-Scene Reconstruction",
      "resolved_canonical": "Human-Scene Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Event-Guided Loss",
      "resolved_canonical": "Event-Guided Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18566.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18566](https://arxiv.org/abs/2509.18566)

## 🔗 유사한 논문
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (86.6% similar)
- [[2025-09-23/ProDyG_ Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos_20250923|ProDyG: Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos]] (86.3% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.8% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (84.6% similar)
- [[2025-09-23/Uni3C_ Unifying Precisely 3D-Enhanced Camera and Human Motion Controls for Video Generation_20250923|Uni3C: Unifying Precisely 3D-Enhanced Camera and Human Motion Controls for Video Generation]] (84.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Human-Scene Reconstruction|Human-Scene Reconstruction]]
**🔗 Specific Connectable**: [[keywords/Event Camera|Event Camera]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Event-Guided Loss|Event-Guided Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18566v1 Announce Type: new 
Abstract: Reconstructing dynamic humans together with static scenes from monocular videos remains difficult, especially under fast motion, where RGB frames suffer from motion blur. Event cameras exhibit distinct advantages, e.g., microsecond temporal resolution, making them a superior sensing choice for dynamic human reconstruction. Accordingly, we present a novel event-guided human-scene reconstruction framework that jointly models human and scene from a single monocular event camera via 3D Gaussian Splatting. Specifically, a unified set of 3D Gaussians carries a learnable semantic attribute; only Gaussians classified as human undergo deformation for animation, while scene Gaussians stay static. To combat blur, we propose an event-guided loss that matches simulated brightness changes between consecutive renderings with the event stream, improving local fidelity in fast-moving regions. Our approach removes the need for external human masks and simplifies managing separate Gaussian sets. On two benchmark datasets, ZJU-MoCap-Blur and MMHPSD-Blur, it delivers state-of-the-art human-scene reconstruction, with notable gains over strong baselines in PSNR/SSIM and reduced LPIPS, especially for high-speed subjects.

## 📝 요약

이 논문은 단안 비디오에서 역동적인 인간과 정적 장면을 재구성하는 문제를 다룹니다. 특히 빠른 움직임으로 인해 발생하는 모션 블러 문제를 해결하기 위해, 마이크로초 단위의 시간 해상도를 제공하는 이벤트 카메라를 활용한 새로운 프레임워크를 제안합니다. 이 프레임워크는 3D Gaussian Splatting을 통해 인간과 장면을 모델링하며, 인간으로 분류된 가우시안만 변형되어 애니메이션을 구현합니다. 모션 블러를 줄이기 위해 이벤트 유도 손실을 도입하여, 연속 렌더링 간의 밝기 변화를 이벤트 스트림과 일치시킵니다. 이 방법은 외부 인간 마스크가 필요 없으며, 별도의 가우시안 세트를 관리하는 복잡성을 줄입니다. 제안된 방법은 ZJU-MoCap-Blur 및 MMHPSD-Blur 데이터셋에서 최첨단 성능을 보이며, 특히 고속 움직임에서 PSNR/SSIM 및 LPIPS에서 강력한 기준선보다 뛰어난 성능을 보입니다.

## 🎯 주요 포인트

- 1. 단안 비디오에서 역동적인 인간과 정적 장면을 재구성하는 것은 특히 빠른 움직임에서 어려움을 겪지만, 이벤트 카메라는 마이크로초 단위의 시간 해상도를 제공하여 이를 극복할 수 있습니다.
- 2. 제안된 프레임워크는 단일 단안 이벤트 카메라를 통해 3D 가우시안 스플래팅을 사용하여 인간과 장면을 공동으로 모델링합니다.
- 3. 이벤트 유도 손실을 통해 연속 렌더링 간의 밝기 변화를 이벤트 스트림과 일치시켜 빠르게 움직이는 영역의 지역적 충실도를 개선합니다.
- 4. 외부 인간 마스크가 필요하지 않으며, 별도의 가우시안 세트를 관리하는 복잡성을 줄입니다.
- 5. ZJU-MoCap-Blur 및 MMHPSD-Blur 벤치마크 데이터셋에서 PSNR/SSIM 및 LPIPS에서 강력한 기준선 대비 뛰어난 성능을 보여줍니다.


---

*Generated on 2025-09-24 16:02:26*