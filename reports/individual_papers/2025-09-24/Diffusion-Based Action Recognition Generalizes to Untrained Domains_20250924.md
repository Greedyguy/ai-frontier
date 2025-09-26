<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:33:27.829751",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision Diffusion Model",
    "Transformer",
    "Action Recognition",
    "Generalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision Diffusion Model": 0.78,
    "Transformer": 0.85,
    "Action Recognition": 0.82,
    "Generalization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Diffusion Model",
        "canonical": "Vision Diffusion Model",
        "aliases": [
          "VDM"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach in action recognition, enhancing semantic feature extraction.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A key component in aggregating features, linking to existing transformer-based models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Action Recognition",
        "canonical": "Action Recognition",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the paper's theme, connecting to broader research in recognizing human and animal actions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Generalization",
        "canonical": "Generalization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Focuses on the model's ability to adapt across different domains, a key research challenge.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "model",
      "process",
      "features"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Diffusion Model",
      "resolved_canonical": "Vision Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Action Recognition",
      "resolved_canonical": "Action Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Generalization",
      "resolved_canonical": "Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Diffusion-Based Action Recognition Generalizes to Untrained Domains

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.08908.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.08908](https://arxiv.org/abs/2509.08908)

## 🔗 유사한 논문
- [[2025-09-23/KRAST_ Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models_20250923|KRAST: Knowledge-Augmented Robotic Action Recognition with Structured Text for Vision-Language Models]] (83.4% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (82.1% similar)
- [[2025-09-23/Look, Focus, Act_ Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers_20250923|Look, Focus, Act: Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers]] (82.0% similar)
- [[2025-09-23/DINOv3-Diffusion Policy_ Self-Supervised Large Visual Model for Visuomotor Diffusion Policy Learning_20250923|DINOv3-Diffusion Policy: Self-Supervised Large Visual Model for Visuomotor Diffusion Policy Learning]] (81.7% similar)
- [[2025-09-23/KungfuBot2_ Learning Versatile Motion Skills for Humanoid Whole-Body Control_20250923|KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Action Recognition|Action Recognition]], [[keywords/Generalization|Generalization]]
**⚡ Unique Technical**: [[keywords/Vision Diffusion Model|Vision Diffusion Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08908v3 Announce Type: replace 
Abstract: Humans can recognize the same actions despite large context and viewpoint variations, such as differences between species (walking in spiders vs. horses), viewpoints (egocentric vs. third-person), and contexts (real life vs movies). Current deep learning models struggle with such generalization. We propose using features generated by a Vision Diffusion Model (VDM), aggregated via a transformer, to achieve human-like action recognition across these challenging conditions. We find that generalization is enhanced by the use of a model conditioned on earlier timesteps of the diffusion process to highlight semantic information over pixel level details in the extracted features. We experimentally explore the generalization properties of our approach in classifying actions across animal species, across different viewing angles, and different recording contexts. Our model sets a new state-of-the-art across all three generalization benchmarks, bringing machine action recognition closer to human-like robustness. Project page: https://www.vision.caltech.edu/actiondiff. Code: https://github.com/frankyaoxiao/ActionDiff

## 📝 요약

이 논문은 인간이 다양한 맥락과 시점에서 동일한 행동을 인식할 수 있는 능력을 기계 학습 모델에 적용하고자 합니다. 이를 위해 Vision Diffusion Model(VDM)을 사용하여 생성된 특징을 트랜스포머로 집계하는 방법을 제안합니다. 이 모델은 확산 과정의 초기 단계에서 조건화된 모델을 사용하여 픽셀 수준의 세부사항보다 의미론적 정보를 강조함으로써 일반화 능력을 향상시킵니다. 동물 종, 시점, 녹화 맥락 등 다양한 조건에서 행동을 분류하는 실험을 통해 이 접근법의 일반화 특성을 탐구하였으며, 모든 일반화 벤치마크에서 최신 성능을 달성하여 기계의 행동 인식이 인간과 유사한 견고성에 한 걸음 더 다가섰습니다.

## 🎯 주요 포인트

- 1. 인간은 다양한 맥락과 관점의 변화를 초월하여 동일한 행동을 인식할 수 있는 반면, 현재의 딥러닝 모델은 이러한 일반화에 어려움을 겪고 있습니다.
- 2. Vision Diffusion Model(VDM)을 활용하여 추출된 특징을 트랜스포머로 집계하여 인간과 유사한 행동 인식을 달성하는 방법을 제안합니다.
- 3. 확산 과정의 초기 타임스텝에 조건화된 모델을 사용하여 픽셀 수준의 세부사항보다 의미론적 정보를 강조함으로써 일반화가 향상됨을 발견했습니다.
- 4. 제안된 모델은 동물 종, 시점, 녹화 맥락에 걸친 행동 분류에서 새로운 최첨단 성능을 기록하여 기계의 행동 인식이 인간과 유사한 견고성에 가까워졌습니다.


---

*Generated on 2025-09-24 16:33:27*