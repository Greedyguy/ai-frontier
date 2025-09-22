# FOVAL: Calibration-Free and Subject-Invariant Fixation Depth Estimation Across Diverse Eye-Tracking Datasets

**Korean Title:** FOVAL: 다양한 시선 추적 데이터셋에서 보정이 필요 없고 피험자에 무관한 고정 깊이 추정

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Calibration-Free Fixation Depth Estimation

## 🔗 유사한 논문
- [[2025-09-19/ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (82.5% similar)
- [[2025-09-22/ORCA_ Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models_20250922|ORCA Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language Models]] (81.2% similar)
- [[2025-09-19/Depth AnyEvent_ A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation_20250919|Depth AnyEvent A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (81.1% similar)
- [[2025-09-18/Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (80.9% similar)
- [[2025-09-22/Saccadic Vision for Fine-Grained Visual Classification_20250922|Saccadic Vision for Fine-Grained Visual Classification]] (80.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2408.03591v2 Announce Type: replace-cross 
Abstract: Accurate fixation depth estimation is essential for applications in extended reality (XR), robotics, and human-computer interaction. However, current methods heavily depend on user-specific calibration, which limits their scalability and usability. We introduce FOVAL, a robust calibration-free approach that combines spatiotemporal sequence modelling via Long Short-Term Memory (LSTM) networks with subject-invariant feature engineering and normalisation. Compared to Transformers, Temporal Convolutional Networks (TCNs), and CNNs, FOVAL achieves superior performance, particularly in scenarios with limited and noisy gaze data. Evaluations across three benchmark datasets using Leave-One-Out Cross-Validation (LOOCV) and cross-dataset validation show a mean absolute error (MAE) of 9.1 cm and strong generalisation without calibration. We further analyse inter-subject variability and domain shifts, providing insight into model robustness and adaptation. FOVAL's scalability and accuracy make it highly suitable for real-world deployment.

## 🔍 Abstract (한글 번역)

arXiv:2408.03591v2 발표 유형: 교차 대체  
초록: 정확한 고정 깊이 추정은 확장 현실(XR), 로봇 공학, 인간-컴퓨터 상호작용 분야에서 필수적입니다. 그러나 현재의 방법들은 사용자별 보정에 크게 의존하여 확장성과 사용성을 제한합니다. 우리는 FOVAL을 소개합니다. 이는 Long Short-Term Memory (LSTM) 네트워크를 통한 시공간 시퀀스 모델링과 주체 불변 특징 공학 및 정규화를 결합한 견고한 보정 없는 접근 방식입니다. Transformer, Temporal Convolutional Networks (TCNs), CNNs와 비교하여, FOVAL은 특히 제한적이고 잡음이 많은 시선 데이터 시나리오에서 우수한 성능을 발휘합니다. Leave-One-Out Cross-Validation (LOOCV) 및 교차 데이터셋 검증을 사용한 세 가지 벤치마크 데이터셋 평가에서 평균 절대 오차(MAE) 9.1 cm와 보정 없는 강력한 일반화를 보여줍니다. 우리는 또한 주체 간 변동성과 도메인 변화를 분석하여 모델의 견고성과 적응에 대한 통찰력을 제공합니다. FOVAL의 확장성과 정확성은 실제 환경에서의 배포에 매우 적합합니다.

## 📝 요약

이 논문은 XR, 로봇공학, 인간-컴퓨터 상호작용에서 중요한 고정 깊이 추정을 위한 새로운 방법론인 FOVAL을 소개합니다. FOVAL은 사용자별 보정 없이 LSTM 네트워크를 활용한 시공간 시퀀스 모델링과 주제 불변적 특징 공학 및 정규화를 결합하여 기존 방법의 한계를 극복합니다. FOVAL은 제한적이고 잡음이 많은 시선 데이터 상황에서 뛰어난 성능을 보이며, 세 가지 벤치마크 데이터셋에서 Leave-One-Out 교차 검증과 교차 데이터셋 검증을 통해 평균 절대 오차 9.1 cm를 기록했습니다. 또한, 주제 간 변동성과 도메인 변화에 대한 분석을 통해 모델의 견고성과 적응력을 입증했습니다. FOVAL은 보정 없이도 높은 정확도와 확장성을 제공하여 실제 응용에 적합합니다.

## 🎯 주요 포인트

- 1. FOVAL은 사용자별 보정 없이도 정확한 고정 깊이 추정을 가능하게 하는 강력한 방법을 제안합니다.

- 2. LSTM 네트워크를 활용한 시공간 시퀀스 모델링과 주제 불변적 특징 엔지니어링 및 정규화를 결합하여 높은 성능을 달성합니다.

- 3. FOVAL은 제한적이고 잡음이 많은 시선 데이터 시나리오에서 특히 뛰어난 성능을 보이며, 기존의 Transformer, TCN, CNN보다 우수합니다.

- 4. 세 가지 벤치마크 데이터셋에서 LOOCV와 교차 데이터셋 검증을 통해 평균 절대 오차(MAE) 9.1 cm를 기록하며, 보정 없이도 강력한 일반화 능력을 보여줍니다.

- 5. FOVAL의 확장성과 정확성은 실제 환경에서의 활용에 매우 적합합니다.

---

*Generated on 2025-09-22 14:37:12*