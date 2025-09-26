---
keywords:
  - Large Language Model
  - Indoor Layout Generation
  - 3D-SynthPlace Dataset
  - Multi-Stage Preference Optimization
  - Scene Editing
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2506.07570
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:03:12.709292",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Indoor Layout Generation",
    "3D-SynthPlace Dataset",
    "Multi-Stage Preference Optimization",
    "Scene Editing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Indoor Layout Generation": 0.78,
    "3D-SynthPlace Dataset": 0.82,
    "Multi-Stage Preference Optimization": 0.8,
    "Scene Editing": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Links to existing work on language models and their applications in various domains.",
        "novelty_score": 0.35,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "indoor layout generation",
        "canonical": "Indoor Layout Generation",
        "aliases": [
          "scene layout generation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, connecting to design and AI applications.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D-SynthPlace",
        "canonical": "3D-SynthPlace Dataset",
        "aliases": [
          "3D SynthPlace"
        ],
        "category": "unique_technical",
        "rationale": "A new dataset introduced in the paper, crucial for replicating and extending the research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "multi-stage preference optimization",
        "canonical": "Multi-Stage Preference Optimization",
        "aliases": [
          "preference optimization"
        ],
        "category": "specific_connectable",
        "rationale": "A novel optimization technique that enhances layout generation quality.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "scene editing",
        "canonical": "Scene Editing",
        "aliases": [
          "interactive scene editing"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the interactive capabilities of the proposed system, linking to user interaction studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "automatic",
      "method",
      "experiment",
      "performance",
      "success rates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "indoor layout generation",
      "resolved_canonical": "Indoor Layout Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D-SynthPlace",
      "resolved_canonical": "3D-SynthPlace Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "multi-stage preference optimization",
      "resolved_canonical": "Multi-Stage Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "scene editing",
      "resolved_canonical": "Scene Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization

**Korean Title:** 옵티씬: 확장된 인간 정렬 데이터 합성과 다단계 선호 최적화를 통한 LLM 기반 실내 장면 배치 생성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.07570.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2506.07570](https://arxiv.org/abs/2506.07570)

## 🔗 유사한 논문
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN: Layout-guided 3D Indoor Scene Generation]] (90.2% similar)
- [[2025-09-22/Causal Reasoning Elicits Controllable 3D Scene Generation_20250922|Causal Reasoning Elicits Controllable 3D Scene Generation]] (81.8% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (80.9% similar)
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (80.0% similar)
- [[2025-09-22/SCENEFORGE_ Enhancing 3D-text alignment with Structured Scene Compositions_20250922|SCENEFORGE: Enhancing 3D-text alignment with Structured Scene Compositions]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multi-Stage Preference Optimization|Multi-Stage Preference Optimization]], [[keywords/Scene Editing|Scene Editing]]
**⚡ Unique Technical**: [[keywords/Indoor Layout Generation|Indoor Layout Generation]], [[keywords/3D-SynthPlace Dataset|3D-SynthPlace Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.07570v2 Announce Type: replace-cross 
Abstract: Automatic indoor layout generation has attracted increasing attention due to its potential in interior design, virtual environment construction, and embodied AI. Existing methods fall into two categories: prompt-driven approaches that leverage proprietary LLM services (e.g., GPT APIs) and learning-based methods trained on layout data upon diffusion-based models. Prompt-driven methods often suffer from spatial inconsistency and high computational costs, while learning-based methods are typically constrained by coarse relational graphs and limited datasets, restricting their generalization to diverse room categories. In this paper, we revisit LLM-based indoor layout generation and present 3D-SynthPlace, a large-scale dataset that combines synthetic layouts generated via a 'GPT synthesize, Human inspect' pipeline, upgraded from the 3D-Front dataset. 3D-SynthPlace contains nearly 17,000 scenes, covering four common room types -- bedroom, living room, kitchen, and bathroom -- enriched with diverse objects and high-level spatial annotations. We further introduce OptiScene, a strong open-source LLM optimized for indoor layout generation, fine-tuned based on our 3D-SynthPlace dataset through our two-stage training. For the warum-up stage I, we adopt supervised fine-tuning (SFT), which is taught to first generate high-level spatial descriptions then conditionally predict concrete object placements. For the reinforcing stage II, to better align the generated layouts with human design preferences, we apply multi-turn direct preference optimization (DPO), which significantly improving layout quality and generation success rates. Extensive experiments demonstrate that OptiScene outperforms traditional prompt-driven and learning-based baselines. Moreover, OptiScene shows promising potential in interactive tasks such as scene editing and robot navigation.

## 🔍 Abstract (한글 번역)

arXiv:2506.07570v2 발표 유형: 교차 교체  
초록: 자동 실내 레이아웃 생성은 인테리어 디자인, 가상 환경 구축 및 구현된 AI 분야에서의 잠재력 때문에 점점 더 많은 주목을 받고 있습니다. 기존 방법은 독점적인 LLM 서비스(예: GPT API)를 활용하는 프롬프트 기반 접근법과 확산 기반 모델에 대한 레이아웃 데이터를 학습한 학습 기반 방법으로 두 가지 범주로 나뉩니다. 프롬프트 기반 방법은 공간적 일관성 부족과 높은 계산 비용의 문제를 자주 겪으며, 학습 기반 방법은 일반적으로 거친 관계 그래프와 제한된 데이터셋에 의해 제약을 받아 다양한 방 종류에 대한 일반화가 제한됩니다. 이 논문에서는 LLM 기반 실내 레이아웃 생성을 재검토하고, 'GPT 합성, 인간 검사' 파이프라인을 통해 생성된 합성 레이아웃을 결합한 대규모 데이터셋인 3D-SynthPlace를 소개합니다. 이는 3D-Front 데이터셋에서 업그레이드된 것입니다. 3D-SynthPlace는 침실, 거실, 주방, 욕실의 네 가지 일반적인 방 유형을 포함하여 거의 17,000개의 장면을 포함하고 있으며, 다양한 객체와 고급 공간 주석으로 풍부하게 구성되어 있습니다. 우리는 또한 실내 레이아웃 생성을 위해 최적화된 강력한 오픈 소스 LLM인 OptiScene을 소개하며, 3D-SynthPlace 데이터셋을 기반으로 한 두 단계의 학습을 통해 미세 조정되었습니다. 준비 단계 I에서는 감독된 미세 조정(SFT)을 채택하여 먼저 고급 공간 설명을 생성한 다음 조건부로 구체적인 객체 배치를 예측하도록 교육합니다. 강화 단계 II에서는 생성된 레이아웃을 인간의 디자인 선호도와 더 잘 맞추기 위해 다중 턴 직접 선호 최적화(DPO)를 적용하여 레이아웃 품질과 생성 성공률을 크게 향상시킵니다. 광범위한 실험을 통해 OptiScene이 전통적인 프롬프트 기반 및 학습 기반 기준을 능가함을 입증합니다. 또한 OptiScene은 장면 편집 및 로봇 내비게이션과 같은 대화형 작업에서 유망한 잠재력을 보여줍니다.

## 📝 요약

이 논문은 실내 레이아웃 자동 생성에 관한 연구로, 기존 방법론의 한계를 극복하기 위해 3D-SynthPlace라는 대규모 데이터셋을 소개합니다. 이 데이터셋은 'GPT 생성, 인간 검사' 과정을 통해 생성된 합성 레이아웃을 포함하며, 침실, 거실, 주방, 욕실 등 다양한 방 유형을 다룹니다. 또한, 3D-SynthPlace를 기반으로 한 OptiScene이라는 강력한 오픈 소스 LLM을 제안합니다. OptiScene은 두 단계의 훈련 과정을 통해 개발되었으며, 높은 수준의 공간 설명을 생성하고 구체적인 객체 배치를 예측합니다. 실험 결과, OptiScene은 기존 방법들보다 우수한 성능을 보였으며, 장면 편집 및 로봇 내비게이션과 같은 상호작용 작업에서도 유망한 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 실내 레이아웃 자동 생성은 인테리어 디자인, 가상 환경 구축, 구현된 AI 분야에서 주목받고 있다.
- 2. 기존 방법은 GPT API와 같은 LLM 서비스를 활용하는 프롬프트 기반 접근법과 확산 기반 모델에 학습된 데이터 기반 방법으로 나뉜다.
- 3. 3D-SynthPlace는 'GPT 합성, 인간 검사' 파이프라인을 통해 생성된 약 17,000개의 장면을 포함한 대규모 합성 레이아웃 데이터셋이다.
- 4. OptiScene은 실내 레이아웃 생성을 위해 최적화된 오픈 소스 LLM으로, 3D-SynthPlace 데이터셋을 기반으로 한 두 단계의 훈련을 통해 개발되었다.
- 5. OptiScene은 전통적인 프롬프트 기반 및 학습 기반 방법보다 뛰어난 성능을 보이며, 장면 편집 및 로봇 내비게이션과 같은 상호작용 작업에서도 잠재력을 보여준다.


---

*Generated on 2025-09-23 10:03:12*