---
keywords:
  - Hyperdimensional Computing
  - Deep Learning
  - Medical Data Classification
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:26:15.494515",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hyperdimensional Computing",
    "Deep Learning",
    "Medical Data Classification"
  ],
  "rejected_keywords": [
    "Energy-Efficient Classification"
  ],
  "similarity_scores": {
    "Hyperdimensional Computing": 0.78,
    "Deep Learning": 0.85,
    "Medical Data Classification": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# HD3C: Efficient Medical Data Classification for Embedded Devices

**Korean Title:** HD3C: 임베디드 장치를 위한 효율적인 의료 데이터 분류

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Hyperdimensional Computing|Hyperdimensional Computing]], [[keywords/Medical Data Classification|Medical Data Classification]]

## 🔗 유사한 논문
- [[Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (80.5% similar)
- [[Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (79.8% similar)
- [[Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (79.5% similar)
- [[ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (78.6% similar)
- [[Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (78.3% similar)

## 📋 저자 정보

**Authors:** Jianglan Wei, Zhenyu Zhang, Pengcheng Wang, Mingjie Zeng, Zhigang Zeng

## 📄 Abstract (원문)

Energy-efficient medical data classification is essential for modern disease
screening, particularly in home and field healthcare where embedded devices are
prevalent. While deep learning models achieve state-of-the-art accuracy, their
substantial energy consumption and reliance on GPUs limit deployment on such
platforms. We present Hyperdimensional Computing with Class-Wise Clustering
(HD3C), a lightweight classification framework designed for low-power
environments. HD3C encodes data into high-dimensional hypervectors, aggregates
them into multiple cluster-specific prototypes, and performs classification
through similarity search in hyperspace. We evaluate HD3C across three medical
classification tasks; on heart sound classification, HD3C is $350\times$ more
energy-efficient than Bayesian ResNet with less than 1% accuracy difference.
Moreover, HD3C demonstrates exceptional robustness to noise, limited training
data, and hardware error, supported by both theoretical analysis and empirical
results, highlighting its potential for reliable deployment in real-world
settings. Code is available at https://github.com/jianglanwei/HD3C.

## 🔍 Abstract (한글 번역)

에너지 효율적인 의료 데이터 분류는 현대 질병 선별, 특히 임베디드 장치가 널리 사용되는 가정 및 현장 의료에서 필수적입니다. 딥러닝 모델은 최첨단 정확도를 달성하지만, 상당한 에너지 소비와 GPU 의존성 때문에 이러한 플랫폼에 배포하는 데 한계가 있습니다. 우리는 저전력 환경을 위해 설계된 경량 분류 프레임워크인 클래스별 클러스터링을 활용한 초차원 컴퓨팅(HD3C)을 제안합니다. HD3C는 데이터를 고차원 초벡터로 인코딩하고, 이를 여러 클러스터별 프로토타입으로 집계하며, 초공간에서의 유사성 검색을 통해 분류를 수행합니다. 우리는 세 가지 의료 분류 작업에서 HD3C를 평가하였으며, 심장 소리 분류에서 HD3C는 베이지안 ResNet보다 에너지 효율성이 350배 높고, 정확도 차이는 1% 미만입니다. 더욱이, HD3C는 소음, 제한된 훈련 데이터, 하드웨어 오류에 대한 뛰어난 강인성을 보여주며, 이론적 분석과 실험적 결과를 통해 실제 환경에서의 신뢰할 수 있는 배포 가능성을 강조합니다. 코드는 https://github.com/jianglanwei/HD3C에서 이용할 수 있습니다.

## 📝 요약

에너지 효율적인 의료 데이터 분류는 현대 질병 선별에 필수적입니다. 본 연구에서는 저전력 환경을 위한 경량 분류 프레임워크인 HD3C를 제안합니다. HD3C는 데이터를 고차원 하이퍼벡터로 인코딩하고, 여러 클러스터별 프로토타입으로 집계하여 유사성 검색을 통해 분류를 수행합니다. 심장 소리 분류에서 HD3C는 Bayesian ResNet보다 350배 더 에너지 효율적이며, 정확도 차이는 1% 미만입니다. 또한, HD3C는 소음, 제한된 훈련 데이터, 하드웨어 오류에 대한 뛰어난 강건성을 보여주며, 이론적 분석과 실험 결과로 그 신뢰성을 입증합니다.

## 🎯 주요 포인트

- 1. HD3C는 저전력 환경을 위해 설계된 경량 분류 프레임워크로, 고차원 하이퍼벡터를 사용하여 데이터를 인코딩하고, 클러스터별 프로토타입으로 집계하여 분류를 수행합니다.

- 2. HD3C는 심장 소리 분류 작업에서 Bayesian ResNet보다 350배 더 에너지 효율적이며, 정확도 차이는 1% 미만입니다.

- 3. HD3C는 소음, 제한된 훈련 데이터, 하드웨어 오류에 대한 뛰어난 강건성을 보여주며, 이론적 분석과 실험 결과로 그 신뢰성을 입증합니다.

- 4. HD3C의 코드는 https://github.com/jianglanwei/HD3C에서 제공됩니다.

---

*Generated on 2025-09-20 05:49:16*