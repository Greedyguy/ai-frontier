# Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection

**Korean Title:** 일반화 가능한 오디오 딥페이크 탐지에서 저차원 어댑터 전문가의 혼합

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Janne Laakkonen|Janne Laakkonen]] [[authors/Ivan Kukanov|Ivan Kukanov]] [[authors/Ville Hautamäki|Ville Hautamäki]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Generalizable Audio Deepfake Detection

## 🔗 유사한 논문
- [[Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (84.5% similar)
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (83.0% similar)
- [[FURINA_ Free from Unmergeable Router via LINear Aggregation of mixed experts_20250919|FURINA Free from Unmergeable Router via LINear Aggregation of mixed experts]] (82.8% similar)
- [[Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting_20250918|Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting]] (82.3% similar)
- [[Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation_20250919|Mixture of Multicenter Experts in Multimodal AI for Debiased Radiotherapy Target Delineation]] (81.3% similar)

## 📋 저자 정보

**Authors:** Janne Laakkonen, Ivan Kukanov, Ville Hautamäki

## 📄 Abstract (원문)

Foundation models such as Wav2Vec2 excel at representation learning in speech
tasks, including audio deepfake detection. However, after being fine-tuned on a
fixed set of bonafide and spoofed audio clips, they often fail to generalize to
novel deepfake methods not represented in training. To address this, we propose
a mixture-of-LoRA-experts approach that integrates multiple low-rank adapters
(LoRA) into the model's attention layers. A routing mechanism selectively
activates specialized experts, enhancing adaptability to evolving deepfake
attacks. Experimental results show that our method outperforms standard
fine-tuning in both in-domain and out-of-domain scenarios, reducing equal error
rates relative to baseline models. Notably, our best MoE-LoRA model lowers the
average out-of-domain EER from 8.55\% to 6.08\%, demonstrating its
effectiveness in achieving generalizable audio deepfake detection.

## 🔍 Abstract (한글 번역)

기초 모델인 Wav2Vec2는 오디오 딥페이크 탐지를 포함한 음성 작업에서 표현 학습에 뛰어납니다. 그러나 고정된 본래 및 위조 오디오 클립 세트에 대해 미세 조정된 후에는 훈련에 포함되지 않은 새로운 딥페이크 방법에 일반화하는 데 종종 실패합니다. 이를 해결하기 위해, 우리는 모델의 주의 메커니즘에 여러 저순위 어댑터(LoRA)를 통합하는 LoRA 전문가 혼합 접근법을 제안합니다. 라우팅 메커니즘은 특화된 전문가를 선택적으로 활성화하여 진화하는 딥페이크 공격에 대한 적응성을 향상시킵니다. 실험 결과에 따르면, 우리 방법은 도메인 내 및 도메인 외 시나리오 모두에서 표준 미세 조정보다 뛰어나며, 기준 모델에 비해 동등 오류율을 감소시킵니다. 특히, 우리의 최상의 MoE-LoRA 모델은 도메인 외 평균 EER을 8.55%에서 6.08%로 낮추어 일반화 가능한 오디오 딥페이크 탐지에서의 효과성을 입증합니다.

## 📝 요약

이 논문은 음성 작업에서 뛰어난 성능을 보이는 Wav2Vec2와 같은 기초 모델의 일반화 문제를 해결하기 위해 제안된 방법론을 다룹니다. 기존 모델은 고정된 데이터로 미세 조정되면 새로운 딥페이크 방법에 대한 일반화가 어려운 문제를 가집니다. 이를 해결하기 위해, 저자들은 모델의 주의 메커니즘에 여러 저순위 어댑터(LoRA)를 통합한 전문가 혼합 접근법을 제안했습니다. 이 접근법은 라우팅 메커니즘을 통해 특정 전문가를 선택적으로 활성화하여 진화하는 딥페이크 공격에 대한 적응성을 높입니다. 실험 결과, 제안된 방법은 기존의 미세 조정 방식보다 도메인 내외 시나리오에서 더 나은 성능을 보였으며, 특히 평균 도메인 외 EER을 8.55%에서 6.08%로 낮추어 일반화된 오디오 딥페이크 탐지에서의 효과성을 입증했습니다.

## 🎯 주요 포인트

- 1. Wav2Vec2와 같은 파운데이션 모델은 오디오 딥페이크 탐지에서 뛰어난 성능을 보이지만, 새로운 딥페이크 방법에 일반화하는 데 어려움을 겪습니다.

- 2. 이를 해결하기 위해, 우리는 모델의 주의 메커니즘에 여러 저순위 어댑터(LoRA)를 통합하는 mixture-of-LoRA-experts 접근법을 제안합니다.

- 3. 라우팅 메커니즘을 통해 특화된 전문가를 선택적으로 활성화하여 진화하는 딥페이크 공격에 대한 적응성을 향상시킵니다.

- 4. 실험 결과, 제안된 방법은 표준 미세 조정보다 인도메인 및 아웃도메인 시나리오에서 더 나은 성능을 보이며, 평균 아웃도메인 EER을 8.55%에서 6.08%로 낮추었습니다.

- 5. MoE-LoRA 모델은 일반화 가능한 오디오 딥페이크 탐지에서 효과적임을 입증했습니다.

---

*Generated on 2025-09-20 09:27:28*