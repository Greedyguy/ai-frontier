---
keywords:
  - Transformer Architecture
  - Uncertainty Quantification
  - Data Quality Monitoring
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2501.19237
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:50:20.864051",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer Architecture",
    "Uncertainty Quantification",
    "Data Quality Monitoring"
  ],
  "rejected_keywords": [
    "Exponentially Weighted Moving Average"
  ],
  "similarity_scores": {
    "Transformer Architecture": 0.8,
    "Uncertainty Quantification": 0.78,
    "Data Quality Monitoring": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# DINAMO: Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments

**Korean Title:** DINAMO: 대규모 입자 물리 실험을 위한 동적이고 해석 가능한 이상 감시 시스템

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|transformer encoder]], [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**⚡ Unique Technical**: [[keywords/Data Quality Monitoring|Data Quality Monitoring]]

## 🔗 유사한 논문
- [[Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter_20250919|Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter]] (81.9% similar)
- [[RationAnomaly Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning]] (80.1% similar)
- [[AD-DINOv3 Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (79.1% similar)
- [[DREAM Domain-aware Reasoning for Efficient Autonomous Underwater Monitoring]] (78.7% similar)
- [[Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (78.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.19237v2 Announce Type: replace-cross 
Abstract: Ensuring reliable data collection in large-scale particle physics experiments demands Data Quality Monitoring (DQM) procedures to detect possible detector malfunctions and preserve data integrity. Traditionally, this resource-intensive task has been handled by human shifters who struggle with frequent changes in operational conditions. We present DINAMO: a novel, interpretable, robust, and scalable DQM framework designed to automate anomaly detection in time-dependent settings. Our approach constructs evolving histogram templates with built-in uncertainties, featuring both a statistical variant - extending the classical Exponentially Weighted Moving Average (EWMA) - and a machine learning (ML)-enhanced version that leverages a transformer encoder for improved adaptability. Experimental validations on synthetic datasets demonstrate the high accuracy, adaptability, and interpretability of these methods. The statistical variant is being commissioned in the LHCb experiment at the Large Hadron Collider, underscoring its real-world impact. The code used in this study is available at https://github.com/ArseniiGav/DINAMO.

## 🔍 Abstract (한글 번역)

arXiv:2501.19237v2 발표 유형: 교차 교체  
초록: 대규모 입자 물리 실험에서 신뢰할 수 있는 데이터 수집을 보장하기 위해서는 데이터 품질 모니터링(DQM) 절차가 필요하며, 이는 가능한 검출기 오작동을 감지하고 데이터 무결성을 유지하는 데 필수적입니다. 전통적으로 이 자원 집약적인 작업은 운영 조건의 빈번한 변화에 어려움을 겪는 인간 교대 근무자들이 처리해 왔습니다. 우리는 시간 의존적 환경에서 이상 탐지를 자동화하도록 설계된 새로운, 해석 가능하고, 견고하며 확장 가능한 DQM 프레임워크인 DINAMO를 소개합니다. 우리의 접근 방식은 내장된 불확실성을 가진 진화하는 히스토그램 템플릿을 구성하며, 고전적인 지수 가중 이동 평균(EWMA)을 확장한 통계적 변형과 적응성을 향상시키기 위해 트랜스포머 인코더를 활용한 기계 학습(ML) 강화 버전을 특징으로 합니다. 합성 데이터셋에 대한 실험적 검증은 이러한 방법들의 높은 정확성, 적응성 및 해석 가능성을 입증합니다. 통계적 변형은 대형 강입자 충돌기(LHC)의 LHCb 실험에서 실험적으로 사용되고 있으며, 이는 실질적인 영향을 강조합니다. 이 연구에서 사용된 코드는 https://github.com/ArseniiGav/DINAMO에서 확인할 수 있습니다.

## 📝 요약

이 논문은 대규모 입자 물리 실험에서 데이터 수집의 신뢰성을 보장하기 위한 데이터 품질 모니터링(DQM) 절차를 자동화하는 DINAMO라는 새로운 프레임워크를 제안합니다. DINAMO는 시간 의존적 환경에서 이상 탐지를 자동화하며, 전통적인 EWMA를 확장한 통계적 변형과 트랜스포머 인코더를 활용한 머신러닝 변형을 포함합니다. 실험 결과, 이 방법들이 높은 정확도와 적응성, 해석 가능성을 보임을 확인했습니다. 특히, 통계적 변형은 LHCb 실험에 적용되고 있으며, 연구에 사용된 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. DINAMO는 대규모 입자 물리 실험에서 데이터 품질 모니터링을 자동화하기 위한 새로운 프레임워크로, 시간 의존적 환경에서 이상 탐지를 수행합니다.

- 2. 이 프레임워크는 고전적인 EWMA를 확장한 통계적 변형과 트랜스포머 인코더를 활용한 머신러닝 기반 버전을 포함하여 진화하는 히스토그램 템플릿을 구성합니다.

- 3. 실험 결과, DINAMO는 높은 정확도, 적응성, 해석 가능성을 보여주었으며, 통계적 변형은 LHCb 실험에서 실제로 사용되고 있습니다.

- 4. 연구에 사용된 코드는 https://github.com/ArseniiGav/DINAMO에서 공개되어 있습니다.

---

*Generated on 2025-09-19 15:44:13*