<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:22:14.348433",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Proton Dose Calculation",
    "Cone Beam Computed Tomography",
    "Adaptive Treatment Planning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Proton Dose Calculation": 0.72,
    "Cone Beam Computed Tomography": 0.8,
    "Adaptive Treatment Planning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "xLSTM neural networks",
        "canonical": "Neural Network",
        "aliases": [
          "xLSTM",
          "extended Long Short-Term Memory"
        ],
        "category": "broad_technical",
        "rationale": "This term represents a specific type of neural network architecture used in the study, linking it to broader neural network concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "proton dose calculation",
        "canonical": "Proton Dose Calculation",
        "aliases": [
          "proton therapy dose calculation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specialized process central to the study, offering unique insights into proton therapy planning.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "CBCT images",
        "canonical": "Cone Beam Computed Tomography",
        "aliases": [
          "CBCT"
        ],
        "category": "specific_connectable",
        "rationale": "CBCT is a specific imaging technique crucial for the study's methodology, linking it to imaging and medical physics domains.",
        "novelty_score": 0.6,
        "connectivity_score": 0.79,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "adaptive treatment scenarios",
        "canonical": "Adaptive Treatment Planning",
        "aliases": [
          "adaptive therapy"
        ],
        "category": "specific_connectable",
        "rationale": "Adaptive treatment is a key concept in modern radiotherapy, enhancing the study's relevance to evolving treatment protocols.",
        "novelty_score": 0.65,
        "connectivity_score": 0.77,
        "specificity_score": 0.78,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "dose calculation",
      "treatment planning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "xLSTM neural networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "proton dose calculation",
      "resolved_canonical": "Proton Dose Calculation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "CBCT images",
      "resolved_canonical": "Cone Beam Computed Tomography",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.79,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "adaptive treatment scenarios",
      "resolved_canonical": "Adaptive Treatment Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.77,
        "specificity": 0.78,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Neural Network-Driven Direct CBCT-Based Dose Calculation for Head-and-Neck Proton Treatment Planning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18378.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18378](https://arxiv.org/abs/2509.18378)

## 🔗 유사한 논문
- [[2025-09-24/Surrogate Modelling of Proton Dose with Monte Carlo Dropout Uncertainty Quantification_20250924|Surrogate Modelling of Proton Dose with Monte Carlo Dropout Uncertainty Quantification]] (84.5% similar)
- [[2025-09-23/Multi-needle Localization for Pelvic Seed Implant Brachytherapy based on Tip-handle Detection and Matching_20250923|Multi-needle Localization for Pelvic Seed Implant Brachytherapy based on Tip-handle Detection and Matching]] (82.6% similar)
- [[2025-09-24/Enhancing Video Object Segmentation in TrackRAD Using XMem Memory Network_20250924|Enhancing Video Object Segmentation in TrackRAD Using XMem Memory Network]] (82.2% similar)
- [[2025-09-24/CPT-4DMR_ Continuous sPatial-Temporal Representation for 4D-MRI Reconstruction_20250924|CPT-4DMR: Continuous sPatial-Temporal Representation for 4D-MRI Reconstruction]] (81.0% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Cone Beam Computed Tomography|Cone Beam Computed Tomography]], [[keywords/Adaptive Treatment Planning|Adaptive Treatment Planning]]
**⚡ Unique Technical**: [[keywords/Proton Dose Calculation|Proton Dose Calculation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18378v1 Announce Type: cross 
Abstract: Accurate dose calculation on cone beam computed tomography (CBCT) images is essential for modern proton treatment planning workflows, particularly when accounting for inter-fractional anatomical changes in adaptive treatment scenarios. Traditional CBCT-based dose calculation suffers from image quality limitations, requiring complex correction workflows. This study develops and validates a deep learning approach for direct proton dose calculation from CBCT images using extended Long Short-Term Memory (xLSTM) neural networks. A retrospective dataset of 40 head-and-neck cancer patients with paired planning CT and treatment CBCT images was used to train an xLSTM-based neural network (CBCT-NN). The architecture incorporates energy token encoding and beam's-eye-view sequence modelling to capture spatial dependencies in proton dose deposition patterns. Training utilized 82,500 paired beam configurations with Monte Carlo-generated ground truth doses. Validation was performed on 5 independent patients using gamma analysis, mean percentage dose error assessment, and dose-volume histogram comparison. The CBCT-NN achieved gamma pass rates of 95.1 $\pm$ 2.7% using 2mm/2% criteria. Mean percentage dose errors were 2.6 $\pm$ 1.4% in high-dose regions ($>$90% of max dose) and 5.9 $\pm$ 1.9% globally. Dose-volume histogram analysis showed excellent preservation of target coverage metrics (Clinical Target Volume V95% difference: -0.6 $\pm$ 1.1%) and organ-at-risk constraints (parotid mean dose difference: -0.5 $\pm$ 1.5%). Computation time is under 3 minutes without sacrificing Monte Carlo-level accuracy. This study demonstrates the proof-of-principle of direct CBCT-based proton dose calculation using xLSTM neural networks. The approach eliminates traditional correction workflows while achieving comparable accuracy and computational efficiency suitable for adaptive protocols.

## 📝 요약

이 연구는 콘빔 컴퓨터 단층촬영(CBCT) 이미지를 이용한 직접적인 양성자 선량 계산을 위해 확장된 Long Short-Term Memory(xLSTM) 신경망을 개발하고 검증했습니다. 40명의 두경부암 환자의 계획 CT와 치료 CBCT 이미지를 사용하여 xLSTM 기반의 신경망(CBCT-NN)을 훈련했습니다. 이 신경망은 에너지 토큰 인코딩과 빔의 시야 시퀀스 모델링을 통해 양성자 선량 분포 패턴의 공간적 의존성을 포착합니다. 검증 결과, 5명의 독립적인 환자에 대해 감마 분석을 통해 2mm/2% 기준으로 95.1%의 감마 통과율을 기록했습니다. 고선량 영역에서 평균 선량 오차는 2.6%였으며, 전체적으로는 5.9%였습니다. 또한, 목표 커버리지와 위험 장기 제약 조건을 잘 유지했습니다. 이 연구는 전통적인 보정 과정을 제거하면서도 적응형 프로토콜에 적합한 정확성과 계산 효율성을 달성했습니다.

## 🎯 주요 포인트

- 1. 이 연구는 xLSTM 신경망을 사용하여 CBCT 이미지에서 직접적인 양성자 선량 계산을 수행하는 딥러닝 접근법을 개발하고 검증했습니다.
- 2. 40명의 두경부암 환자의 계획 CT와 치료 CBCT 이미지 쌍을 사용하여 CBCT-NN을 훈련했습니다.
- 3. CBCT-NN은 2mm/2% 기준으로 95.1%의 감마 통과율을 달성했으며, 높은 선량 영역에서 평균 선량 오차는 2.6%였습니다.
- 4. 선량-부피 히스토그램 분석에서 목표 커버리지 및 위험 기관 제약 조건의 우수한 보존을 보여주었습니다.
- 5. 이 접근법은 전통적인 보정 워크플로우를 제거하면서 적응형 프로토콜에 적합한 정확성과 계산 효율성을 달성했습니다.


---

*Generated on 2025-09-24 16:22:14*