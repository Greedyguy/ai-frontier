# H-Alpha Anomalyzer: An Explainable Anomaly Detector for Solar H-Alpha Observations

**Korean Title:** H-알파 아노말라이저: 태양 H-알파 관측을 위한 설명 가능한 이상 탐지기

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Mahsa Khazaei|Mahsa Khazaei]] [[authors/Azim Ahmadzadeh|Azim Ahmadzadeh]] [[authors/Alexei Pevtsov|Alexei Pevtsov]] [[authors/Luca Bertello|Luca Bertello]] [[authors/Alexander Pevtsov|Alexander Pevtsov]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Explainable Anomaly Detection

## 🔗 유사한 논문
- [[AnoF-Diff_ One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use_20250918|AnoF-Diff One-Step Diffusion-Based Anomaly Detection for Forceful Tool Use]] (80.4% similar)
- [[RationAnomaly_ Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning_20250919|RationAnomaly Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning]] (80.1% similar)
- [[DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (79.2% similar)
- [[Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform_20250918|Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform]] (78.9% similar)
- [[Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter_20250919|Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter]] (78.5% similar)

## 📋 저자 정보

**Authors:** Mahsa Khazaei, Azim Ahmadzadeh, Alexei Pevtsov, Luca Bertello, Alexander Pevtsov

## 📄 Abstract (원문)

The plethora of space-borne and ground-based observatories has provided
astrophysicists with an unprecedented volume of data, which can only be
processed at scale using advanced computing algorithms. Consequently, ensuring
the quality of data fed into machine learning (ML) models is critical. The
H$\alpha$ observations from the GONG network represent one such data stream,
producing several observations per minute, 24/7, since 2010. In this study, we
introduce a lightweight (non-ML) anomaly-detection algorithm, called H-Alpha
Anomalyzer, designed to identify anomalous observations based on user-defined
criteria. Unlike many black-box algorithms, our approach highlights exactly
which regions triggered the anomaly flag and quantifies the corresponding
anomaly likelihood. For our comparative analysis, we also created and released
a dataset of 2,000 observations, equally divided between anomalous and
non-anomalous cases. Our results demonstrate that the proposed model not only
outperforms existing methods but also provides explainability, enabling
qualitative evaluation by domain experts.

## 🔍 Abstract (한글 번역)

우주 기반 및 지상 기반 관측소의 다양성은 천체물리학자들에게 전례 없는 양의 데이터를 제공하였으며, 이는 고급 컴퓨팅 알고리즘을 통해서만 대규모로 처리될 수 있습니다. 따라서 기계 학습(ML) 모델에 입력되는 데이터의 품질을 보장하는 것이 중요합니다. GONG 네트워크의 H$\alpha$ 관측은 이러한 데이터 스트림 중 하나로, 2010년부터 24시간 내내 매분 여러 관측을 생성하고 있습니다. 본 연구에서는 사용자 정의 기준에 따라 이상 관측을 식별하도록 설계된 경량의 (비-ML) 이상 탐지 알고리즘인 H-Alpha Anomalyzer를 소개합니다. 많은 블랙박스 알고리즘과 달리, 우리의 접근법은 이상 플래그를 트리거한 정확한 영역을 강조하고 해당 이상 가능성을 정량화합니다. 비교 분석을 위해, 우리는 2,000개의 관측 데이터셋을 생성하고 공개했으며, 이는 이상과 비이상 사례로 균등하게 나누어져 있습니다. 우리의 결과는 제안된 모델이 기존 방법보다 뛰어날 뿐만 아니라 설명 가능성을 제공하여 도메인 전문가들이 질적 평가를 할 수 있게 함을 보여줍니다.

## 📝 요약

이 연구는 GONG 네트워크의 Hα 관측 데이터를 대상으로 하는 경량의 비기계학습 이상 탐지 알고리즘인 H-Alpha Anomalyzer를 소개합니다. 이 알고리즘은 사용자 정의 기준에 따라 이상 관측을 식별하며, 기존의 블랙박스 알고리즘과 달리 이상을 유발한 특정 영역을 강조하고 이상 가능성을 정량화합니다. 2,000개의 관측 데이터셋을 통해 비교 분석한 결과, 제안된 모델은 기존 방법보다 뛰어난 성능을 보였으며, 설명 가능성을 제공하여 전문가의 정성적 평가를 가능하게 합니다.

## 🎯 주요 포인트

- 1. 천문학자들은 방대한 양의 데이터를 처리하기 위해 고급 컴퓨팅 알고리즘을 사용해야 합니다.

- 2. GONG 네트워크의 Hα 관측은 2010년부터 매일 매분 여러 관측 데이터를 생성합니다.

- 3. H-Alpha Anomalyzer는 사용자 정의 기준에 따라 이상 관측을 식별하는 경량의 비-ML 이상 탐지 알고리즘입니다.

- 4. 제안된 모델은 기존 방법보다 뛰어난 성능을 보이며, 설명 가능성을 제공하여 전문가들이 질적 평가를 할 수 있게 합니다.

- 5. 비교 분석을 위해 이상 및 비이상 사례로 균등하게 나뉜 2,000개의 관측 데이터셋을 생성 및 공개했습니다.

---

*Generated on 2025-09-20 05:55:14*