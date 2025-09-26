---
keywords:
  - Attention Mechanism
  - Stereo Matching
  - Global Regulation and Excitation
  - Iterative Algorithms
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15891
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:14:23.536845",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Stereo Matching",
    "Global Regulation and Excitation",
    "Iterative Algorithms"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.8,
    "Stereo Matching": 0.78,
    "Global Regulation and Excitation": 0.85,
    "Iterative Algorithms": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Attention Tuning",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are central to the proposed framework, linking it to existing work on attention-based models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Stereo Matching",
        "canonical": "Stereo Matching",
        "aliases": [
          "Stereo Vision",
          "3D Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "Stereo matching is a specific technique in computer vision, directly relevant to the paper's focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Global Regulation and Excitation",
        "canonical": "Global Regulation and Excitation",
        "aliases": [
          "GREAT Framework"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced by the authors, central to their contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Iterative Algorithms",
        "canonical": "Iterative Algorithms",
        "aliases": [
          "Iterative Methods"
        ],
        "category": "broad_technical",
        "rationale": "Iterative algorithms are a broad concept but are crucial for understanding the context of the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.5,
        "link_intent_score": 0.65
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
      "candidate_surface": "Attention Tuning",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Stereo Matching",
      "resolved_canonical": "Stereo Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Global Regulation and Excitation",
      "resolved_canonical": "Global Regulation and Excitation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Iterative Algorithms",
      "resolved_canonical": "Iterative Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.5,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Global Regulation and Excitation via Attention Tuning for Stereo Matching

**Korean Title:** 글로벌 조절 및 흥분: 스테레오 매칭을 위한 주의 조정 기술

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15891.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15891](https://arxiv.org/abs/2509.15891)

## 🔗 유사한 논문
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (80.8% similar)
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (80.6% similar)
- [[2025-09-22/See&Trek_ Training-Free Spatial Prompting for Multimodal Large Language Model_20250922|See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model]] (80.6% similar)
- [[2025-09-18/Improving Generalized Visual Grounding with Instance-aware Joint Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (80.3% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Iterative Algorithms|Iterative Algorithms]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Stereo Matching|Stereo Matching]], [[keywords/Global Regulation and Excitation|Global Regulation and Excitation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15891v1 Announce Type: new 
Abstract: Stereo matching achieves significant progress with iterative algorithms like RAFT-Stereo and IGEV-Stereo. However, these methods struggle in ill-posed regions with occlusions, textureless, or repetitive patterns, due to a lack of global context and geometric information for effective iterative refinement. To enable the existing iterative approaches to incorporate global context, we propose the Global Regulation and Excitation via Attention Tuning (GREAT) framework which encompasses three attention modules. Specifically, Spatial Attention (SA) captures the global context within the spatial dimension, Matching Attention (MA) extracts global context along epipolar lines, and Volume Attention (VA) works in conjunction with SA and MA to construct a more robust cost-volume excited by global context and geometric details. To verify the universality and effectiveness of this framework, we integrate it into several representative iterative stereo-matching methods and validate it through extensive experiments, collectively denoted as GREAT-Stereo. This framework demonstrates superior performance in challenging ill-posed regions. Applied to IGEV-Stereo, among all published methods, our GREAT-IGEV ranks first on the Scene Flow test set, KITTI 2015, and ETH3D leaderboards, and achieves second on the Middlebury benchmark. Code is available at https://github.com/JarvisLee0423/GREAT-Stereo.

## 🔍 Abstract (한글 번역)

arXiv:2509.15891v1 발표 유형: 신규  
초록: RAFT-Stereo 및 IGEV-Stereo와 같은 반복 알고리즘을 통해 스테레오 매칭은 상당한 발전을 이루었습니다. 그러나 이러한 방법들은 가려짐, 무纹리, 반복 패턴과 같은 불완전한 영역에서 효과적인 반복적 정제를 위한 전역적 맥락과 기하학적 정보의 부족으로 어려움을 겪습니다. 기존의 반복적 접근 방식이 전역적 맥락을 통합할 수 있도록 하기 위해, 우리는 주의 조정을 통한 전역 조절 및 흥분(GREAT) 프레임워크를 제안합니다. 이 프레임워크는 세 가지 주의 모듈을 포함합니다. 구체적으로, 공간 주의(SA)는 공간 차원 내의 전역 맥락을 포착하고, 매칭 주의(MA)는 에피폴라 라인에 따라 전역 맥락을 추출하며, 볼륨 주의(VA)는 SA 및 MA와 함께 작동하여 전역 맥락과 기하학적 세부 사항에 의해 흥분된 보다 강력한 비용 볼륨을 구축합니다. 이 프레임워크의 보편성과 효과성을 검증하기 위해, 우리는 이를 여러 대표적인 반복적 스테레오 매칭 방법에 통합하고 광범위한 실험을 통해 검증하였으며, 이를 GREAT-Stereo라고 통칭합니다. 이 프레임워크는 도전적인 불완전한 영역에서 우수한 성능을 보여줍니다. IGEV-Stereo에 적용했을 때, 모든 발표된 방법 중에서 우리의 GREAT-IGEV는 Scene Flow 테스트 세트, KITTI 2015 및 ETH3D 리더보드에서 1위를 차지하였고, Middlebury 벤치마크에서는 2위를 기록하였습니다. 코드는 https://github.com/JarvisLee0423/GREAT-Stereo에서 확인할 수 있습니다.

## 📝 요약

이 논문은 스테레오 매칭의 성능을 향상시키기 위해 글로벌 컨텍스트를 통합하는 GREAT(Great Regulation and Excitation via Attention Tuning) 프레임워크를 제안합니다. 이 프레임워크는 세 가지 주의(attention) 모듈로 구성되어 있으며, 공간 주의(SA)는 공간 차원에서, 매칭 주의(MA)는 에피폴라 라인에서, 볼륨 주의(VA)는 SA와 MA와 함께 작동하여 더 견고한 비용 볼륨을 구축합니다. 이 방법론은 여러 스테레오 매칭 방법에 통합되어 실험을 통해 검증되었으며, 특히 어려운 영역에서 뛰어난 성능을 보였습니다. GREAT-IGEV는 Scene Flow, KITTI 2015, ETH3D 등에서 최고 성능을 기록했으며, Middlebury 벤치마크에서는 2위를 차지했습니다.

## 🎯 주요 포인트

- 1. 기존의 반복적 스테레오 매칭 알고리즘은 폐색, 무纹理, 반복 패턴과 같은 난해한 영역에서 글로벌 컨텍스트와 기하학적 정보의 부족으로 어려움을 겪는다.
- 2. GREAT 프레임워크는 글로벌 컨텍스트를 통합하기 위해 세 가지 주의 모듈을 포함하며, 공간 주의(SA), 매칭 주의(MA), 볼륨 주의(VA)를 통해 보다 견고한 비용 볼륨을 구축한다.
- 3. GREAT 프레임워크는 다양한 반복적 스테레오 매칭 방법에 통합되어, 난해한 영역에서 우수한 성능을 입증한다.
- 4. GREAT-IGEV는 Scene Flow 테스트 세트, KITTI 2015, ETH3D 리더보드에서 1위를 차지하고, Middlebury 벤치마크에서는 2위를 기록한다.
- 5. 연구의 코드와 결과는 GitHub에서 제공된다.


---

*Generated on 2025-09-23 12:14:23*