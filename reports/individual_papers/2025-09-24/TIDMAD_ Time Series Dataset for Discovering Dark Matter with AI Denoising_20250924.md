<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:21:13.998830",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dark Matter",
    "ABRACADABRA Experiment",
    "Time Series Dataset",
    "AI Denoising"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dark Matter": 0.85,
    "ABRACADABRA Experiment": 0.8,
    "Time Series Dataset": 0.78,
    "AI Denoising": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dark Matter",
        "canonical": "Dark Matter",
        "aliases": [
          "DM"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus and a key concept in physics, linking to a wide range of scientific discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "ABRACADABRA experiment",
        "canonical": "ABRACADABRA Experiment",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific to the study and central to the dataset discussed, offering a unique link to experimental physics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Time Series Dataset",
        "canonical": "Time Series Dataset",
        "aliases": [
          "TIDMAD"
        ],
        "category": "broad_technical",
        "rationale": "Key data type in the study, relevant to data processing and AI applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "AI Denoising",
        "canonical": "AI Denoising",
        "aliases": [
          "Artificial Intelligence Denoising"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the use of AI in processing data, connecting to machine learning and signal processing fields.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "ultra-long",
      "samples per second",
      "community-standard"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dark Matter",
      "resolved_canonical": "Dark Matter",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ABRACADABRA experiment",
      "resolved_canonical": "ABRACADABRA Experiment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Time Series Dataset",
      "resolved_canonical": "Time Series Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "AI Denoising",
      "resolved_canonical": "AI Denoising",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# TIDMAD: Time Series Dataset for Discovering Dark Matter with AI Denoising

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2406.04378.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2406.04378](https://arxiv.org/abs/2406.04378)

## 🔗 유사한 논문
- [[2025-09-19/DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO: Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (79.9% similar)
- [[2025-09-18/Shedding Light on Dark Matter at the LHC with Machine Learning_20250918|Shedding Light on Dark Matter at the LHC with Machine Learning]] (77.6% similar)
- [[2025-09-22/Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems_20250922|Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems]] (76.3% similar)
- [[2025-09-17/H-Alpha Anomalyzer_ An Explainable Anomaly Detector for Solar H-Alpha Observations_20250917|H-Alpha Anomalyzer: An Explainable Anomaly Detector for Solar H-Alpha Observations]] (75.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Time Series Dataset|Time Series Dataset]]
**🔗 Specific Connectable**: [[keywords/AI Denoising|AI Denoising]]
**⚡ Unique Technical**: [[keywords/Dark Matter|Dark Matter]], [[keywords/ABRACADABRA Experiment|ABRACADABRA Experiment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.04378v2 Announce Type: replace 
Abstract: Dark matter makes up approximately 85% of total matter in our universe, yet it has never been directly observed in any laboratory on Earth. The origin of dark matter is one of the most important questions in contemporary physics, and a convincing detection of dark matter would be a Nobel-Prize-level breakthrough in fundamental science. The ABRACADABRA experiment was specifically designed to search for dark matter. Although it has not yet made a discovery, ABRACADABRA has produced several dark matter search results widely endorsed by the physics community. The experiment generates ultra-long time-series data at a rate of 10 million samples per second, where the dark matter signal would manifest itself as a sinusoidal oscillation mode within the ultra-long time series. In this paper, we present the TIDMAD -- a comprehensive data release from the ABRACADABRA experiment including three key components: an ultra-long time series dataset divided into training, validation, and science subsets; a carefully-designed denoising score for direct model benchmarking; and a complete analysis framework which produces a community-standard dark matter search result suitable for publication as a physics paper. This data release enables core AI algorithms to extract the signal and produce real physics results thereby advancing fundamental science. The data downloading and associated analysis scripts are available at https://github.com/jessicafry/TIDMAD

## 📝 요약

ABRACADABRA 실험은 암흑 물질 탐색을 위해 설계되었으며, 아직 발견에는 이르지 못했지만 물리학계에서 널리 인정받는 결과를 제시했습니다. 이 실험은 초당 1,000만 개의 샘플을 생성하는 초장기 시계열 데이터를 통해 암흑 물질 신호를 탐색합니다. 논문에서는 ABRACADABRA 실험의 데이터 릴리스인 TIDMAD를 소개하며, 이는 훈련, 검증, 과학 데이터 세트로 나뉜 초장기 시계열 데이터, 모델 벤치마킹을 위한 잡음 제거 점수, 물리학 논문으로 출판 가능한 분석 프레임워크를 포함합니다. 이 데이터 릴리스는 AI 알고리즘이 신호를 추출하고 실제 물리학 결과를 도출할 수 있도록 지원하여 기초 과학 발전에 기여합니다. 데이터와 분석 스크립트는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 암흑 물질은 우주의 총 물질의 약 85%를 차지하지만, 아직 지구의 실험실에서 직접 관측된 적은 없다.
- 2. ABRACADABRA 실험은 암흑 물질을 탐색하기 위해 특별히 설계된 실험으로, 아직 발견에 이르지는 못했지만 물리학 커뮤니티에서 널리 인정받는 결과를 도출했다.
- 3. TIDMAD는 ABRACADABRA 실험의 포괄적인 데이터 공개로, 훈련, 검증, 과학 하위 집합으로 나뉜 초장기 시계열 데이터셋을 포함한다.
- 4. 이 데이터 공개는 AI 알고리즘이 신호를 추출하고 실제 물리학 결과를 생성할 수 있게 하여 기초 과학을 발전시킨다.
- 5. 데이터 다운로드 및 관련 분석 스크립트는 https://github.com/jessicafry/TIDMAD에서 제공된다.


---

*Generated on 2025-09-24 15:21:13*