<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:01:28.149635",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-View Universal Manipulation Interface",
    "Imitation Learning",
    "Handheld Grippers",
    "Third-Person Perspective"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-View Universal Manipulation Interface": 0.89,
    "Imitation Learning": 0.78,
    "Handheld Grippers": 0.84,
    "Third-Person Perspective": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-View Universal Manipulation Interface",
        "canonical": "Multi-View Universal Manipulation Interface",
        "aliases": [
          "MV-UMI"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique framework introduced in the paper, central to the research and not found in existing vocabularies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.68,
        "specificity_score": 0.92,
        "link_intent_score": 0.89
      },
      {
        "surface": "imitation learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "behavior cloning"
        ],
        "category": "broad_technical",
        "rationale": "Imitation learning is a foundational concept in machine learning, relevant to the paper's focus on learning from demonstrations.",
        "novelty_score": 0.45,
        "connectivity_score": 0.87,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "handheld grippers",
        "canonical": "Handheld Grippers",
        "aliases": [
          "portable grippers"
        ],
        "category": "specific_connectable",
        "rationale": "Handheld grippers are a key component in the paper's methodology, enabling cross-embodiment learning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.84
      },
      {
        "surface": "third-person perspective",
        "canonical": "Third-Person Perspective",
        "aliases": [
          "external view"
        ],
        "category": "specific_connectable",
        "rationale": "The integration of a third-person perspective is crucial for overcoming limitations in data collection, as discussed in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "robot manipulation policies",
      "data collection",
      "scene understanding"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-View Universal Manipulation Interface",
      "resolved_canonical": "Multi-View Universal Manipulation Interface",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.68,
        "specificity": 0.92,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "imitation learning",
      "resolved_canonical": "Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.87,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "handheld grippers",
      "resolved_canonical": "Handheld Grippers",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "third-person perspective",
      "resolved_canonical": "Third-Person Perspective",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# MV-UMI: A Scalable Multi-View Interface for Cross-Embodiment Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18757.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18757](https://arxiv.org/abs/2509.18757)

## 🔗 유사한 논문
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (85.2% similar)
- [[2025-09-19/M4Diffuser_ Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation_20250919|M4Diffuser: Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation]] (84.9% similar)
- [[2025-09-23/KungfuBot2_ Learning Versatile Motion Skills for Humanoid Whole-Body Control_20250923|KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control]] (84.8% similar)
- [[2025-09-23/UniSkill_ Imitating Human Videos via Cross-Embodiment Skill Representations_20250923|UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations]] (84.4% similar)
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Imitation Learning|Imitation Learning]]
**🔗 Specific Connectable**: [[keywords/Handheld Grippers|Handheld Grippers]], [[keywords/Third-Person Perspective|Third-Person Perspective]]
**⚡ Unique Technical**: [[keywords/Multi-View Universal Manipulation Interface|Multi-View Universal Manipulation Interface]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18757v1 Announce Type: cross 
Abstract: Recent advances in imitation learning have shown great promise for developing robust robot manipulation policies from demonstrations. However, this promise is contingent on the availability of diverse, high-quality datasets, which are not only challenging and costly to collect but are often constrained to a specific robot embodiment. Portable handheld grippers have recently emerged as intuitive and scalable alternatives to traditional robotic teleoperation methods for data collection. However, their reliance solely on first-person view wrist-mounted cameras often creates limitations in capturing sufficient scene contexts. In this paper, we present MV-UMI (Multi-View Universal Manipulation Interface), a framework that integrates a third-person perspective with the egocentric camera to overcome this limitation. This integration mitigates domain shifts between human demonstration and robot deployment, preserving the cross-embodiment advantages of handheld data-collection devices. Our experimental results, including an ablation study, demonstrate that our MV-UMI framework improves performance in sub-tasks requiring broad scene understanding by approximately 47% across 3 tasks, confirming the effectiveness of our approach in expanding the range of feasible manipulation tasks that can be learned using handheld gripper systems, without compromising the cross-embodiment advantages inherent to such systems.

## 📝 요약

이 논문은 다양한 시점의 카메라를 활용한 로봇 조작 정책 개발을 제안합니다. 기존의 휴대용 그리퍼는 손목 카메라에 의존하여 장면을 충분히 포착하지 못하는 한계가 있습니다. 이를 해결하기 위해, 본 연구에서는 1인칭 시점과 3인칭 시점을 통합한 MV-UMI 프레임워크를 제안합니다. 이 방법은 인간 시연과 로봇 배치 간의 도메인 차이를 줄이고, 다양한 로봇 형태에 적용 가능한 데이터 수집의 장점을 유지합니다. 실험 결과, MV-UMI는 장면 이해가 필요한 작업에서 약 47%의 성능 향상을 보였습니다. 이는 휴대용 그리퍼 시스템을 활용한 조작 작업의 범위를 확장하는 데 효과적임을 입증합니다.

## 🎯 주요 포인트

- 1. 모방 학습의 발전은 시연을 통해 강력한 로봇 조작 정책을 개발하는 데 유망하지만, 이는 다양한 고품질 데이터셋의 가용성에 달려 있다.
- 2. 휴대용 그리퍼는 전통적인 로봇 원격 조작 방법에 대한 직관적이고 확장 가능한 대안으로 부상하고 있다.
- 3. MV-UMI 프레임워크는 1인칭 시점의 카메라와 3인칭 시점을 통합하여 장면 컨텍스트를 충분히 포착하는 데 있어 기존의 한계를 극복한다.
- 4. 실험 결과에 따르면 MV-UMI는 광범위한 장면 이해가 필요한 하위 작업에서 약 47%의 성능 향상을 보여준다.
- 5. MV-UMI는 휴대용 그리퍼 시스템의 교차 구현 이점을 유지하면서 학습 가능한 조작 작업의 범위를 확장하는 데 효과적이다.


---

*Generated on 2025-09-24 14:01:28*