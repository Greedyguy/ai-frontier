<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:54:01.533041",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "AI-generated Text",
    "Temporal Discrepancy Tomography",
    "Continuous Wavelet Transform",
    "Non-stationarity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "AI-generated Text": 0.82,
    "Temporal Discrepancy Tomography": 0.85,
    "Continuous Wavelet Transform": 0.7,
    "Non-stationarity": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AI-generated text",
        "canonical": "AI-generated Text",
        "aliases": [
          "Machine-generated Text",
          "Synthetic Text"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on detection techniques and represents a distinct area of study.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Temporal Discrepancy Tomography",
        "canonical": "Temporal Discrepancy Tomography",
        "aliases": [
          "TDT"
        ],
        "category": "unique_technical",
        "rationale": "As a novel detection paradigm introduced in the paper, it is crucial for understanding the proposed methodology.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Continuous Wavelet Transform",
        "canonical": "Continuous Wavelet Transform",
        "aliases": [
          "CWT"
        ],
        "category": "broad_technical",
        "rationale": "This mathematical tool is essential for the signal processing approach discussed in the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "non-stationarity",
        "canonical": "Non-stationarity",
        "aliases": [
          "Nonstationary Behavior"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding non-stationarity is key to grasping the challenges in detecting AI-generated text.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AI-generated text",
      "resolved_canonical": "AI-generated Text",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Temporal Discrepancy Tomography",
      "resolved_canonical": "Temporal Discrepancy Tomography",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Continuous Wavelet Transform",
      "resolved_canonical": "Continuous Wavelet Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "non-stationarity",
      "resolved_canonical": "Non-stationarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# AI-Generated Text is Non-Stationary: Detection via Temporal Tomography

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2508.01754.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2508.01754](https://arxiv.org/abs/2508.01754)

## 🔗 유사한 논문
- [[2025-09-24/T-Detect_ Tail-Aware Statistical Normalization for Robust Detection of Adversarial Machine-Generated Text_20250924|T-Detect: Tail-Aware Statistical Normalization for Robust Detection of Adversarial Machine-Generated Text]] (90.1% similar)
- [[2025-09-24/Diversity Boosts AI-Generated Text Detection_20250924|Diversity Boosts AI-Generated Text Detection]] (87.5% similar)
- [[2025-09-22/DNA-DetectLLM_ Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm_20250922|DNA-DetectLLM: Unveiling AI-Generated Text via a DNA-Inspired Mutation-Repair Paradigm]] (86.5% similar)
- [[2025-09-23/Fine-Grained Detection of AI-Generated Text Using Sentence-Level Segmentation_20250923|Fine-Grained Detection of AI-Generated Text Using Sentence-Level Segmentation]] (86.1% similar)
- [[2025-09-24/Trace Is In Sentences_ Unbiased Lightweight ChatGPT-Generated Text Detector_20250924|Trace Is In Sentences: Unbiased Lightweight ChatGPT-Generated Text Detector]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Continuous Wavelet Transform|Continuous Wavelet Transform]]
**🔗 Specific Connectable**: [[keywords/Non-stationarity|Non-stationarity]]
**⚡ Unique Technical**: [[keywords/AI-generated Text|AI-generated Text]], [[keywords/Temporal Discrepancy Tomography|Temporal Discrepancy Tomography]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.01754v2 Announce Type: replace 
Abstract: The field of AI-generated text detection has evolved from supervised classification to zero-shot statistical analysis. However, current approaches share a fundamental limitation: they aggregate token-level measurements into scalar scores, discarding positional information about where anomalies occur. Our empirical analysis reveals that AI-generated text exhibits significant non-stationarity, statistical properties vary by 73.8\% more between text segments compared to human writing. This discovery explains why existing detectors fail against localized adversarial perturbations that exploit this overlooked characteristic. We introduce Temporal Discrepancy Tomography (TDT), a novel detection paradigm that preserves positional information by reformulating detection as a signal processing task. TDT treats token-level discrepancies as a time-series signal and applies Continuous Wavelet Transform to generate a two-dimensional time-scale representation, capturing both the location and linguistic scale of statistical anomalies. On the RAID benchmark, TDT achieves 0.855 AUROC (7.1\% improvement over the best baseline). More importantly, TDT demonstrates robust performance on adversarial tasks, with 14.1\% AUROC improvement on HART Level 2 paraphrasing attacks. Despite its sophisticated analysis, TDT maintains practical efficiency with only 13\% computational overhead. Our work establishes non-stationarity as a fundamental characteristic of AI-generated text and demonstrates that preserving temporal dynamics is essential for robust detection.

## 📝 요약

AI 생성 텍스트 탐지 분야는 감독 학습에서 제로샷 통계 분석으로 발전했지만, 현재의 방법들은 위치 정보를 버리고 토큰 수준의 측정을 스칼라 점수로 집계하는 한계를 가지고 있습니다. 연구 결과, AI 생성 텍스트는 비정상성을 보여 인간 작성 텍스트보다 73.8% 더 많은 통계적 변화를 보입니다. 이는 기존 탐지기가 국부적 적대적 교란에 취약한 이유를 설명합니다. 우리는 위치 정보를 보존하는 새로운 탐지 패러다임인 Temporal Discrepancy Tomography (TDT)를 소개합니다. TDT는 토큰 수준의 불일치를 시계열 신호로 처리하고 연속 웨이블릿 변환을 적용해 통계적 이상 현상의 위치와 언어적 규모를 포착합니다. RAID 벤치마크에서 TDT는 0.855 AUROC를 기록하며, 이는 기존 최고 성능보다 7.1% 개선된 수치입니다. 특히, HART Level 2 패러프레이징 공격에서 14.1% AUROC 개선을 보여줍니다. TDT는 13%의 계산 오버헤드로 실용성을 유지하면서도 강력한 성능을 입증합니다. 이 연구는 AI 생성 텍스트의 비정상성을 근본적 특성으로 규명하고, 시간적 역학 보존이 강력한 탐지에 필수적임을 보여줍니다.

## 🎯 주요 포인트

- 1. AI 생성 텍스트는 인간의 글쓰기와 비교하여 비정상성이 73.8% 더 크게 나타나며, 이는 기존 탐지기가 국부적 적대적 교란에 취약한 이유를 설명합니다.
- 2. Temporal Discrepancy Tomography (TDT)는 위치 정보를 보존하여 탐지를 신호 처리 작업으로 재구성하는 새로운 탐지 패러다임을 제안합니다.
- 3. TDT는 RAID 벤치마크에서 0.855 AUROC를 기록하며, 이는 기존 최고 기준선보다 7.1% 향상된 성능을 보여줍니다.
- 4. TDT는 HART Level 2 패러프레이징 공격에서 14.1% AUROC 향상을 보이며, 적대적 작업에서도 강력한 성능을 입증합니다.
- 5. TDT는 13%의 계산 오버헤드로 실용적인 효율성을 유지하면서 AI 생성 텍스트의 비정상성을 탐지하는 데 필수적인 시간적 동역학 보존의 중요성을 입증합니다.


---

*Generated on 2025-09-24 15:54:01*