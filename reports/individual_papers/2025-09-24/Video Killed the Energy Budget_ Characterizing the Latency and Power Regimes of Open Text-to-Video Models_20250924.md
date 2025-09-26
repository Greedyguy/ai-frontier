<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:02:14.478577",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text-to-Video Generation",
    "Energy Consumption in AI Models",
    "Scaling Laws in AI",
    "Temporal Coherence in Video Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text-to-Video Generation": 0.82,
    "Energy Consumption in AI Models": 0.79,
    "Scaling Laws in AI": 0.77,
    "Temporal Coherence in Video Models": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "text-to-video generation",
        "canonical": "Text-to-Video Generation",
        "aliases": [
          "T2V generation",
          "text-to-video"
        ],
        "category": "unique_technical",
        "rationale": "This is a distinct and emerging field within generative AI, crucial for linking related research on video synthesis from text.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "energy consumption",
        "canonical": "Energy Consumption in AI Models",
        "aliases": [
          "energy demands",
          "power usage"
        ],
        "category": "evolved_concepts",
        "rationale": "Understanding energy consumption is vital for sustainable AI development, linking to broader discussions on AI's environmental impact.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "scaling laws",
        "canonical": "Scaling Laws in AI",
        "aliases": [
          "scaling principles",
          "scaling behaviors"
        ],
        "category": "specific_connectable",
        "rationale": "Scaling laws are fundamental for predicting model performance and resource requirements, connecting to optimization strategies in AI.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "temporal coherence",
        "canonical": "Temporal Coherence in Video Models",
        "aliases": [
          "time consistency",
          "temporal consistency"
        ],
        "category": "specific_connectable",
        "rationale": "Temporal coherence is critical for the quality of generated videos, linking to research on video stability and realism.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "compute-bound analytical model",
      "fine-grained experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "text-to-video generation",
      "resolved_canonical": "Text-to-Video Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "energy consumption",
      "resolved_canonical": "Energy Consumption in AI Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "scaling laws",
      "resolved_canonical": "Scaling Laws in AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "temporal coherence",
      "resolved_canonical": "Temporal Coherence in Video Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Video Killed the Energy Budget: Characterizing the Latency and Power Regimes of Open Text-to-Video Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19222.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19222](https://arxiv.org/abs/2509.19222)

## 🔗 유사한 논문
- [[2025-09-18/Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations_20250918|Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations]] (83.4% similar)
- [[2025-09-23/VidCLearn_ A Continual Learning Approach for Text-to-Video Generation_20250923|VidCLearn: A Continual Learning Approach for Text-to-Video Generation]] (83.0% similar)
- [[2025-09-24/Foresight_ Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation_20250924|Foresight: Adaptive Layer Reuse for Accelerated and High-Quality Text-to-Video Generation]] (81.6% similar)
- [[2025-09-22/AcT2I_ Evaluating and Improving Action Depiction in Text-to-Image Models_20250922|AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models]] (81.5% similar)
- [[2025-09-22/BBScoreV2_ Learning Time-Evolution and Latent Alignment from Stochastic Representation_20250922|BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Scaling Laws in AI|Scaling Laws in AI]], [[keywords/Temporal Coherence in Video Models|Temporal Coherence in Video Models]]
**⚡ Unique Technical**: [[keywords/Text-to-Video Generation|Text-to-Video Generation]]
**🚀 Evolved Concepts**: [[keywords/Energy Consumption in AI Models|Energy Consumption in AI Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19222v1 Announce Type: new 
Abstract: Recent advances in text-to-video (T2V) generation have enabled the creation of high-fidelity, temporally coherent clips from natural language prompts. Yet these systems come with significant computational costs, and their energy demands remain poorly understood. In this paper, we present a systematic study of the latency and energy consumption of state-of-the-art open-source T2V models. We first develop a compute-bound analytical model that predicts scaling laws with respect to spatial resolution, temporal length, and denoising steps. We then validate these predictions through fine-grained experiments on WAN2.1-T2V, showing quadratic growth with spatial and temporal dimensions, and linear scaling with the number of denoising steps. Finally, we extend our analysis to six diverse T2V models, comparing their runtime and energy profiles under default settings. Our results provide both a benchmark reference and practical insights for designing and deploying more sustainable generative video systems.

## 📝 요약

최근 텍스트-비디오(T2V) 생성 기술의 발전으로 자연어 프롬프트에서 고품질의 시간적으로 일관된 영상을 생성할 수 있게 되었습니다. 그러나 이러한 시스템은 높은 계산 비용이 들며, 에너지 소모에 대한 이해가 부족합니다. 본 논문에서는 최첨단 오픈소스 T2V 모델의 지연 시간과 에너지 소비를 체계적으로 연구했습니다. 공간 해상도, 시간 길이, 노이즈 제거 단계에 따른 스케일링 법칙을 예측하는 계산 중심의 분석 모델을 개발하고, WAN2.1-T2V 모델을 통해 이를 검증했습니다. 실험 결과, 공간 및 시간 차원에 따라 이차적으로 증가하고, 노이즈 제거 단계 수에 따라 선형적으로 증가함을 확인했습니다. 또한, 여섯 가지 다양한 T2V 모델의 실행 시간과 에너지 프로필을 비교 분석하여, 지속 가능한 생성 비디오 시스템 설계를 위한 벤치마크와 실용적 인사이트를 제공했습니다.

## 🎯 주요 포인트

- 1. 최신 텍스트-비디오 생성 기술은 자연어 프롬프트로부터 고품질의 시간적으로 일관된 클립을 생성할 수 있게 되었다.
- 2. 본 연구는 최첨단 오픈소스 텍스트-비디오 모델의 지연 시간과 에너지 소비를 체계적으로 분석하였다.
- 3. 공간 해상도, 시간적 길이, 노이즈 제거 단계에 따른 스케일링 법칙을 예측하는 계산 중심의 분석 모델을 개발하였다.
- 4. WAN2.1-T2V 모델을 통해 공간 및 시간적 차원에 대한 이차 성장과 노이즈 제거 단계 수에 대한 선형 스케일링을 실험적으로 검증하였다.
- 5. 여섯 가지 다양한 텍스트-비디오 모델의 실행 시간과 에너지 프로필을 비교하여 지속 가능한 생성 비디오 시스템 설계에 실용적인 통찰력을 제공하였다.


---

*Generated on 2025-09-24 15:02:14*