# mucAI at BAREC Shared Task 2025: Towards Uncertainty Aware Arabic Readability Assessment

**Korean Title:** mucAI at BAREC Shared Task 2025: 불확실성을 인지하는 아랍어 가독성 평가를 향하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Fine-grained Readability Classification

## 🔗 유사한 논문
- [[2025-09-17/Hala Technical Report_ Building Arabic-Centric Instruction & Translation Models at Scale_20250917|Hala Technical Report Building Arabic-Centric Instruction & Translation Models at Scale]] (82.3% similar)
- [[2025-09-17/Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications_20250917|Exploring Data and Parameter Efficient Strategies for Arabic Dialect Identifications]] (81.7% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (80.8% similar)
- [[2025-09-19/ReCoVeR the Target Language_ Language Steering without Sacrificing Task Performance_20250919|ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (80.6% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15485v1 Announce Type: cross 
Abstract: We present a simple, model-agnostic post-processing technique for fine-grained Arabic readability classification in the BAREC 2025 Shared Task (19 ordinal levels). Our method applies conformal prediction to generate prediction sets with coverage guarantees, then computes weighted averages using softmax-renormalized probabilities over the conformal sets. This uncertainty-aware decoding improves Quadratic Weighted Kappa (QWK) by reducing high-penalty misclassifications to nearer levels. Our approach shows consistent QWK improvements of 1-3 points across different base models. In the strict track, our submission achieves QWK scores of 84.9\%(test) and 85.7\% (blind test) for sentence level, and 73.3\% for document level. For Arabic educational assessment, this enables human reviewers to focus on a handful of plausible levels, combining statistical guarantees with practical usability.

## 🔍 Abstract (한글 번역)

arXiv:2509.15485v1 발표 유형: 교차  
초록: 우리는 BAREC 2025 공유 과제(19개의 서수 수준)에서 세밀한 아랍어 가독성 분류를 위한 간단하고 모델 비종속적인 후처리 기법을 제시합니다. 우리의 방법은 적합 예측을 적용하여 커버리지 보장을 갖춘 예측 집합을 생성한 후, 적합 집합에 대해 소프트맥스 재정규화된 확률을 사용하여 가중 평균을 계산합니다. 이러한 불확실성 인식 디코딩은 높은 페널티의 오분류를 더 가까운 수준으로 줄임으로써 이차 가중 카파(QWK)를 개선합니다. 우리의 접근법은 다양한 기본 모델에서 일관되게 1-3 포인트의 QWK 개선을 보여줍니다. 엄격한 트랙에서 우리의 제출물은 문장 수준에서 84.9\%(테스트)와 85.7\%(블라인드 테스트), 문서 수준에서 73.3\%의 QWK 점수를 달성합니다. 아랍어 교육 평가에 있어, 이는 통계적 보장과 실용적 사용성을 결합하여 인간 검토자가 몇 가지 가능한 수준에 집중할 수 있도록 합니다.

## 📝 요약

이 논문은 BAREC 2025 공유 과제에서 세밀한 아랍어 가독성 분류를 위한 모델 비종속적 후처리 기법을 제안합니다. 이 방법은 적합 예측을 적용하여 커버리지 보장을 제공하는 예측 세트를 생성하고, 소프트맥스 재정규화 확률을 사용해 가중 평균을 계산합니다. 이를 통해 높은 패널티의 오분류를 줄여 QWK(Quadratic Weighted Kappa)를 개선합니다. 다양한 기본 모델에서 QWK 점수가 1-3점 향상되었으며, 엄격한 트랙에서 문장 수준 QWK 84.9%(테스트), 85.7%(블라인드 테스트), 문서 수준 73.3%를 달성했습니다. 이는 아랍어 교육 평가에서 통계적 보장과 실용성을 결합하여 인간 검토자가 몇 가지 가능한 수준에 집중할 수 있도록 돕습니다.

## 🎯 주요 포인트

- 1. 본 연구는 BAREC 2025 Shared Task에서 세밀한 아랍어 가독성 분류를 위한 모델 비종속적 후처리 기법을 제안합니다.

- 2. 제안된 방법은 적합 예측을 적용하여 커버리지 보장이 있는 예측 집합을 생성하고, 소프트맥스 재정규화 확률을 사용하여 가중 평균을 계산합니다.

- 3. 불확실성 인지 디코딩을 통해 높은 페널티의 오분류를 줄여 QWK를 개선하며, 다양한 기본 모델에서 일관된 QWK 향상(1-3점)을 보입니다.

- 4. 엄격한 트랙에서 문장 수준 QWK 점수는 테스트에서 84.9%, 블라인드 테스트에서 85.7%, 문서 수준에서 73.3%를 기록했습니다.

- 5. 아랍어 교육 평가에서 통계적 보장과 실용성을 결합하여 인간 검토자가 몇 가지 유력한 수준에 집중할 수 있도록 지원합니다.

---

*Generated on 2025-09-22 13:59:18*