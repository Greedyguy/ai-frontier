
# Evaluating Supervised Learning Models for Fraud Detection: A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data

**Korean Title:** 사기 탐지를 위한 지도 학습 모델 평가: 불균형 거래 데이터에서의 고전 및 심층 아키텍처 비교 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Imbalanced Data Handling

## 🔗 유사한 논문
- [[Adversarial_Distilled_Retrieval-Augmented_Guarding_Model_for_Online_Malicious_Intent_Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (81.1% similar)
- [[CyberLLMInstruct A Pseudo-malicious Dataset Revealing Safety-performance Trade-offs in Cyber Security LLM Fine-tuning]] (78.8% similar)
- [[GRADA Graph-based Reranking against Adversarial Documents Attack]] (78.6% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (78.5% similar)
- [[TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (78.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22521v2 Announce Type: replace-cross 
Abstract: Fraud detection remains a critical task in high-stakes domains such as finance and e-commerce, where undetected fraudulent transactions can lead to significant economic losses. In this study, we systematically compare the performance of four supervised learning models - Logistic Regression, Random Forest, Light Gradient Boosting Machine (LightGBM), and a Gated Recurrent Unit (GRU) network - on a large-scale, highly imbalanced online transaction dataset. While ensemble methods such as Random Forest and LightGBM demonstrated superior performance in both overall and class-specific metrics, Logistic Regression offered a reliable and interpretable baseline. The GRU model showed strong recall for the minority fraud class, though at the cost of precision, highlighting a trade-off relevant for real-world deployment. Our evaluation emphasizes not only weighted averages but also per-class precision, recall, and F1-scores, providing a nuanced view of each model's effectiveness in detecting rare but consequential fraudulent activity. The findings underscore the importance of choosing models based on the specific risk tolerance and operational needs of fraud detection systems.

## 🔍 Abstract (한글 번역)

arXiv:2505.22521v2 발표 유형: 교차 대체  
초록: 사기 탐지는 금융 및 전자 상거래와 같은 고위험 분야에서 중요한 과제로 남아 있으며, 탐지되지 않은 사기 거래는 상당한 경제적 손실을 초래할 수 있습니다. 본 연구에서는 대규모의, 심하게 불균형한 온라인 거래 데이터셋에서 네 가지 지도 학습 모델 - 로지스틱 회귀, 랜덤 포레스트, 라이트 그래디언트 부스팅 머신(LightGBM), 게이트 순환 유닛(GRU) 네트워크 - 의 성능을 체계적으로 비교합니다. 랜덤 포레스트와 LightGBM과 같은 앙상블 방법은 전체 및 클래스별 지표에서 우수한 성능을 보였으나, 로지스틱 회귀는 신뢰할 수 있고 해석 가능한 기준선을 제공했습니다. GRU 모델은 소수의 사기 클래스에 대해 강력한 재현율을 보였으나, 정밀도의 대가를 치렀으며, 이는 실제 배포에 관련된 절충점을 강조합니다. 우리의 평가는 가중 평균뿐만 아니라 클래스별 정밀도, 재현율, F1 점수도 강조하여 드문지만 중요한 사기 활동을 탐지하는 각 모델의 효과에 대한 세밀한 관점을 제공합니다. 이 연구 결과는 사기 탐지 시스템의 특정 위험 허용 범위와 운영 요구 사항에 따라 모델을 선택하는 것이 중요함을 강조합니다.

## 📝 요약

이 연구는 금융 및 전자상거래 분야에서 중요한 과제인 사기 탐지를 위해 네 가지 지도 학습 모델(Logistic Regression, Random Forest, LightGBM, GRU 네트워크)의 성능을 대규모 불균형 온라인 거래 데이터셋에서 비교했습니다. Random Forest와 LightGBM은 전반적 및 클래스별 성능에서 우수했으며, Logistic Regression은 해석 가능한 기준선을 제공했습니다. GRU 모델은 소수의 사기 클래스에서 높은 재현율을 보였으나 정밀도가 낮아지는 트레이드오프가 있었습니다. 연구는 모델 선택 시 사기 탐지 시스템의 위험 허용도와 운영 요구에 맞춘 결정을 강조합니다.

## 🎯 주요 포인트

- 1. 금융 및 전자 상거래 분야에서 사기 탐지는 경제적 손실을 방지하기 위해 중요한 과제입니다.

- 2. 연구에서는 대규모 불균형 온라인 거래 데이터셋을 대상으로 네 가지 지도 학습 모델의 성능을 비교했습니다.

- 3. 랜덤 포레스트와 LightGBM은 전반적 및 클래스별 성능에서 우수한 결과를 보였습니다.

- 4. GRU 모델은 소수 사기 클래스에서 높은 재현율을 보였으나 정밀도에서는 손해를 보았습니다.

- 5. 모델 선택은 사기 탐지 시스템의 특정 위험 허용 범위와 운영 요구에 따라 달라져야 합니다.

---

*Generated on 2025-09-19 15:16:01*