
# Disproving the Feasibility of Learned Confidence Calibration Under Binary Supervision: An Information-Theoretic Impossibility

**Korean Title:** 이진 감독 하에서 학습된 신뢰도 보정의 실행 가능성을 반증하기: 정보 이론적 불가능성

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Multi-agent Learning

## 🔗 유사한 논문
- [[Post-Hoc_Split-Point_Self-Consistency_Verification_for_Efficient,_Unified_Quantification_of_Aleatoric_and_Epistemic_Uncertainty_in_Deep_Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (80.7% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (78.3% similar)
- [[Accuracy Paradox in Large Language Models Regulating Hallucination Risks in Generative AI]] (78.2% similar)
- [[Leveraging_Geometric_Visual_Illusions_as_Perceptual_Inductive_Biases_for_Vision_Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (77.7% similar)
- [[From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (77.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14386v1 Announce Type: new 
Abstract: We prove a fundamental impossibility theorem: neural networks cannot simultaneously learn well-calibrated confidence estimates with meaningful diversity when trained using binary correct/incorrect supervision. Through rigorous mathematical analysis and comprehensive empirical evaluation spanning negative reward training, symmetric loss functions, and post-hoc calibration methods, we demonstrate this is an information-theoretic constraint, not a methodological failure. Our experiments reveal universal failure patterns: negative rewards produce extreme underconfidence (ECE greater than 0.8) while destroying confidence diversity (std less than 0.05), symmetric losses fail to escape binary signal averaging, and post-hoc methods achieve calibration (ECE less than 0.02) only by compressing the confidence distribution. We formalize this as an underspecified mapping problem where binary signals cannot distinguish between different confidence levels for correct predictions: a 60 percent confident correct answer receives identical supervision to a 90 percent confident one. Crucially, our real-world validation shows 100 percent failure rate for all training methods across MNIST, Fashion-MNIST, and CIFAR-10, while post-hoc calibration's 33 percent success rate paradoxically confirms our theorem by achieving calibration through transformation rather than learning. This impossibility directly explains neural network hallucinations and establishes why post-hoc calibration is mathematically necessary, not merely convenient. We propose novel supervision paradigms using ensemble disagreement and adaptive multi-agent learning that could overcome these fundamental limitations without requiring human confidence annotations.

## 🔍 Abstract (한글 번역)

arXiv:2509.14386v1 발표 유형: 신규  
초록: 우리는 근본적인 불가능성 정리를 증명합니다. 신경망은 이진 정/오답 감독을 사용하여 훈련할 때 의미 있는 다양성을 가진 잘 조정된 신뢰도 추정치를 동시에 학습할 수 없습니다. 엄격한 수학적 분석과 부정적 보상 훈련, 대칭 손실 함수, 사후 보정 방법을 아우르는 포괄적인 실험 평가를 통해, 이는 방법론적 실패가 아닌 정보 이론적 제약임을 증명합니다. 우리의 실험은 보편적인 실패 패턴을 드러냅니다: 부정적 보상은 극단적인 과소 신뢰도(ECE가 0.8 이상)를 초래하며 신뢰도의 다양성을 파괴합니다(표준편차가 0.05 미만). 대칭 손실은 이진 신호 평균화를 벗어나지 못하며, 사후 방법은 신뢰도 분포를 압축하여 보정(ECE가 0.02 미만)을 달성합니다. 우리는 이를 올바른 예측에 대한 다양한 신뢰 수준을 구별할 수 없는 이진 신호의 불충분한 매핑 문제로 형식화합니다: 60% 확신의 정답과 90% 확신의 정답은 동일한 감독을 받습니다. 중요한 것은, 우리의 실제 검증에서 MNIST, Fashion-MNIST, CIFAR-10에 대한 모든 훈련 방법의 100% 실패율을 보여주며, 사후 보정의 33% 성공률은 학습이 아닌 변환을 통한 보정을 달성함으로써 역설적으로 우리의 정리를 확인합니다. 이 불가능성은 신경망 환각을 직접적으로 설명하며, 사후 보정이 수학적으로 필요함을 확립합니다. 우리는 인간의 신뢰도 주석을 요구하지 않고 이러한 근본적인 한계를 극복할 수 있는 앙상블 불일치와 적응형 다중 에이전트 학습을 사용하는 새로운 감독 패러다임을 제안합니다.

## 📝 요약

이 논문은 신경망이 이진 정오 피드백을 사용하여 학습할 때, 잘 조정된 신뢰도 추정과 의미 있는 다양성을 동시에 학습할 수 없다는 불가능성 정리를 증명합니다. 수학적 분석과 실험을 통해 이는 방법론적 실패가 아닌 정보 이론적 제약임을 보여줍니다. 실험 결과, 부정적 보상은 극단적인 과소 신뢰를 초래하고, 대칭 손실 함수는 이진 신호 평균화를 벗어나지 못하며, 사후 보정 방법은 신뢰도 분포를 압축하여 보정만을 달성합니다. MNIST, Fashion-MNIST, CIFAR-10 데이터셋에서 모든 학습 방법이 실패했으며, 사후 보정의 33% 성공률은 학습이 아닌 변환을 통해 보정이 이루어짐을 보여줍니다. 이는 신경망의 환각 현상을 설명하며, 사후 보정의 수학적 필요성을 입증합니다. 새로운 감독 패러다임으로 앙상블 불일치와 적응형 다중 에이전트 학습을 제안하여 이러한 한계를 극복할 수 있음을 제안합니다.

## 🎯 주요 포인트

- 1. 신경망은 이진 정답/오답 감독 하에 학습할 때, 잘 조정된 신뢰도 추정과 의미 있는 다양성을 동시에 학습할 수 없다.

- 2. 부정적 보상은 극단적인 과소신뢰를 유발하며, 신뢰도 다양성을 파괴한다.

- 3. 대칭 손실 함수는 이진 신호 평균화를 벗어나지 못한다.

- 4. 사후 보정 방법은 신뢰도 분포를 압축함으로써만 보정을 달성할 수 있다.

- 5. 새로운 감독 패러다임으로 앙상블 불일치와 적응형 다중 에이전트 학습을 제안한다.

---

*Generated on 2025-09-19 15:23:46*