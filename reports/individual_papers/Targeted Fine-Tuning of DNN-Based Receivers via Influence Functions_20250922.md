# Targeted Fine-Tuning of DNN-Based Receivers via Influence Functions

**Korean Title:** DNN 기반 수신기의 목표 지향적 미세 조정을 위한 영향 함수 활용

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Influence-Aligned Update Strategy

## 🔗 유사한 논문
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (82.5% similar)
- [[2025-09-22/Toward Efficient Influence Function_ Dropout as a Compression Tool_20250922|Toward Efficient Influence Function Dropout as a Compression Tool]] (80.8% similar)
- [[2025-09-22/The Alignment Bottleneck_20250922|The Alignment Bottleneck]] (78.0% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (77.3% similar)
- [[2025-09-18/Joint Power and Spectrum Orchestration for D2D Semantic Communication Underlying Energy-Efficient Cellular Networks_20250918|Joint Power and Spectrum Orchestration for D2D Semantic Communication Underlying Energy-Efficient Cellular Networks]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15950v1 Announce Type: new 
Abstract: We present the first use of influence functions for deep learning-based wireless receivers. Applied to DeepRx, a fully convolutional receiver, influence analysis reveals which training samples drive bit predictions, enabling targeted fine-tuning of poorly performing cases. We show that loss-relative influence with capacity-like binary cross-entropy loss and first-order updates on beneficial samples most consistently improves bit error rate toward genie-aided performance, outperforming random fine-tuning in single-target scenarios. Multi-target adaptation proved less effective, underscoring open challenges. Beyond experiments, we connect influence to self-influence corrections and propose a second-order, influence-aligned update strategy. Our results establish influence functions as both an interpretability tool and a basis for efficient receiver adaptation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15950v1 발표 유형: 신규  
초록: 우리는 딥러닝 기반 무선 수신기에 대한 영향 함수의 첫 번째 사용을 제시합니다. 완전 합성곱 수신기인 DeepRx에 적용된 영향 분석은 어떤 학습 샘플이 비트 예측을 주도하는지를 밝혀내어 성능이 저조한 사례에 대한 목표 지향적 미세 조정을 가능하게 합니다. 용량과 유사한 이진 교차 엔트로피 손실과 유익한 샘플에 대한 1차 업데이트를 사용한 손실 상대적 영향이 비트 오류율을 진에이 지원 성능으로 일관되게 개선하며, 단일 목표 시나리오에서 무작위 미세 조정을 능가함을 보여줍니다. 다중 목표 적응은 덜 효과적임이 드러나며, 이는 여전히 해결되지 않은 과제를 강조합니다. 실험을 넘어, 우리는 영향을 자기 영향 수정과 연결하고, 2차 영향 정렬 업데이트 전략을 제안합니다. 우리의 결과는 영향 함수를 해석 가능성 도구이자 효율적인 수신기 적응의 기반으로 확립합니다.

## 📝 요약

이 논문은 딥러닝 기반 무선 수신기에서 영향 함수(influence functions)를 처음으로 사용한 연구를 소개합니다. DeepRx라는 완전한 합성곱 수신기에 적용하여, 어떤 훈련 샘플이 비트 예측에 영향을 미치는지를 분석하고, 성능이 낮은 사례를 목표로 세밀하게 조정할 수 있도록 합니다. 용량과 유사한 이진 교차 엔트로피 손실과 유익한 샘플에 대한 1차 업데이트를 사용한 손실-상대적 영향 분석이 비트 오류율을 개선하는 데 가장 효과적임을 보여주며, 이는 단일 목표 시나리오에서 무작위 미세 조정보다 우수한 성능을 발휘합니다. 다중 목표 적응은 덜 효과적이었으며, 이는 해결해야 할 과제를 남깁니다. 실험 외에도, 자기-영향 수정과의 연결을 제안하고, 2차 영향 정렬 업데이트 전략을 제안합니다. 이 연구는 영향 함수를 해석 가능성 도구 및 효율적인 수신기 적응의 기반으로 확립합니다.

## 🎯 주요 포인트

- 1. 딥러닝 기반 무선 수신기에 영향 함수(influence functions)를 최초로 적용하여 DeepRx의 비트 예측에 영향을 미치는 훈련 샘플을 분석했습니다.

- 2. 손실-상대적 영향과 수용량-유사 이진 교차 엔트로피 손실을 사용한 첫 번째 업데이트가 비트 오류율을 개선하는 데 가장 효과적임을 보였습니다.

- 3. 단일 목표 시나리오에서 무작위 미세 조정보다 우수한 성능을 발휘했으며, 다중 목표 적응은 덜 효과적임을 확인했습니다.

- 4. 영향 함수를 해석 가능성 도구로 활용하고, 효율적인 수신기 적응을 위한 기반으로 제안했습니다.

- 5. 자기 영향(self-influence) 수정과의 연결을 통해 두 번째 차원의 영향 정렬 업데이트 전략을 제안했습니다.

---

*Generated on 2025-09-22 15:28:43*