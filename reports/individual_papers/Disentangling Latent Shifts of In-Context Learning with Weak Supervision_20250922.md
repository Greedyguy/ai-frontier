# Disentangling Latent Shifts of In-Context Learning with Weak Supervision

**Korean Title:** 잠재적 변화의 맥락 내 학습을 약한 지도 학습으로 분리하기

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Pseudo-label Correction|Pseudo-label Correction]] [[keywords/specific/Few-shot Learning|Few-shot Learning]] [[keywords/specific/Weak Supervision|Weak Supervision]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/unique/Disentangled Latent Shifts|Disentangled Latent Shifts]] [[categories/cs.LG|cs.LG]] [[2025-09-22/KITE_ Kernelized and Information Theoretic Exemplars for In-Context Learning_20250922|KITE: Kernelized and Information Theoretic Exemplars for In-Context Learning]] (85.6% similar) [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL: Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (81.4% similar) [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release: Iterative LLM Unlearning with Self-generated Data]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Pseudo-label Correction
**🔗 Specific Connectable**: Few-shot Learning, Weak Supervision
**🔬 Broad Technical**: Large Language Models
**⭐ Unique Technical**: Disentangled Latent Shifts
## 🔗 유사한 논문
- [[2025-09-22/KITE_ Kernelized and Information Theoretic Exemplars for In-Context Learning_20250922|KITE Kernelized and Information Theoretic Exemplars for In-Context Learning]] (85.6% similar)
- [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (81.4% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (80.9% similar)
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting A Simple yet Effective Contrastive Strategy for Continual Learning]] (80.4% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (80.1% similar)


**ArXiv ID**: [2410.01508](https://arxiv.org/abs/2410.01508)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2410.01508.pdf)


**ArXiv ID**: [2410.01508](https://arxiv.org/abs/2410.01508)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2410.01508.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Weak-to-strong Generalization
**🔗 Specific Connectable**: Few-shot Learning, Weak Supervision
**⭐ Unique Technical**: Demonstration-induced Latent Shifts
**🔬 Broad Technical**: Large Language Models

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Few-shot Learning` • 

`Weak Supervision` • 

`Disentangled Latent Shifts` • 

`Pseudo-label Correction`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.01508v2 Announce Type: replace-cross 
Abstract: In-context learning (ICL) enables large language models to perform few-shot learning by conditioning on labeled examples in the prompt. Despite its flexibility, ICL suffers from instability -- especially as prompt length increases with more demonstrations. To address this, we treat ICL as a source of weak supervision and propose a parameter-efficient method that disentangles demonstration-induced latent shifts from those of the query. An ICL-based teacher generates pseudo-labels on unlabeled queries, while a student predicts them using only the query input, updating a lightweight adapter. This captures demonstration effects in a compact, reusable form, enabling efficient inference while remaining composable with new demonstrations. Although trained on noisy teacher outputs, the student often outperforms its teacher through pseudo-label correction and coverage expansion, consistent with the weak-to-strong generalization effect. Empirically, our method improves generalization, stability, and efficiency across both in-domain and out-of-domain tasks, surpassing standard ICL and prior disentanglement methods.

## 🔍 Abstract (한글 번역)

arXiv:2410.01508v2 발표 유형: 교차 교체  
초록: 맥락 내 학습(ICL)은 대형 언어 모델이 프롬프트에 레이블이 있는 예제를 조건으로 하여 소수 샷 학습을 수행할 수 있게 합니다. 그 유연성에도 불구하고, ICL은 불안정성 문제를 겪습니다. 특히, 더 많은 시연과 함께 프롬프트 길이가 증가할수록 그렇습니다. 이를 해결하기 위해, 우리는 ICL을 약한 감독의 원천으로 간주하고, 시연에 의해 유도된 잠재적 변화를 쿼리의 변화와 분리하는 매개변수 효율적인 방법을 제안합니다. ICL 기반의 교사는 레이블이 없는 쿼리에 대해 의사 레이블을 생성하고, 학생은 쿼리 입력만을 사용하여 이를 예측하며 가벼운 어댑터를 업데이트합니다. 이는 시연 효과를 간결하고 재사용 가능한 형태로 포착하여 새로운 시연과 결합 가능하면서도 효율적인 추론을 가능하게 합니다. 비록 교사의 출력이 노이즈가 있을 수 있지만, 학생은 종종 의사 레이블 수정 및 범위 확장을 통해 교사를 능가하며, 이는 약한 감독에서 강한 일반화 효과와 일치합니다. 경험적으로, 우리의 방법은 도메인 내 및 도메인 외 작업 모두에서 일반화, 안정성 및 효율성을 개선하여 표준 ICL 및 이전의 분리 방법을 능가합니다.

## 📝 요약

이 논문에서는 대형 언어 모델의 불안정성을 해결하기 위해 약한 감독으로서의 맥락 내 학습(ICL)을 활용하는 방법을 제안합니다. ICL은 프롬프트에 레이블이 있는 예시를 조건으로 하여 소수의 샘플로 학습을 수행하지만, 시연이 많아질수록 불안정해집니다. 이를 해결하기 위해, 저자들은 ICL을 약한 감독의 원천으로 보고, 시연에 의해 유도된 잠재적 변화를 쿼리의 변화와 분리하는 방법을 제안합니다. ICL 기반의 교사가 레이블이 없는 쿼리에 대해 가짜 레이블을 생성하고, 학생 모델은 경량 어댑터를 업데이트하여 쿼리 입력만으로 이를 예측합니다. 이 방법은 시연의 효과를 간결하고 재사용 가능한 형태로 캡처하여 효율적인 추론을 가능하게 합니다. 실험 결과, 제안된 방법은 일반화, 안정성, 효율성을 개선하며, 표준 ICL 및 기존의 분리 방법을 능가합니다.

## 🎯 주요 포인트


- 1. In-context learning(ICL)은 프롬프트 내 레이블이 있는 예시를 조건으로 사용하여 대형 언어 모델이 소수의 샷 학습을 수행할 수 있게 합니다.

- 2. ICL은 프롬프트 길이가 증가할수록 불안정성이 증가하는 문제를 겪습니다.

- 3. 제안된 방법은 ICL을 약한 감독의 원천으로 보고, 시연에 의해 유도된 잠재적 변화를 쿼리의 변화와 분리하여 처리합니다.

- 4. ICL 기반의 교사가 레이블이 없는 쿼리에 대해 의사 레이블을 생성하고, 학생은 쿼리 입력만을 사용하여 이를 예측하며 경량 어댑터를 업데이트합니다.

- 5. 제안된 방법은 표준 ICL과 이전의 분리 방법을 능가하며, 일반화, 안정성, 효율성을 향상시킵니다.


---

*Generated on 2025-09-22 16:07:40*