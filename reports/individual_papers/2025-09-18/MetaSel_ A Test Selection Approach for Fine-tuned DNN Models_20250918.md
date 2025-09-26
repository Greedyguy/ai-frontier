---
keywords:
  - Transfer Learning
  - Neural Networks
  - Covariate Shift
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2503.17534
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:19:38.233300",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transfer Learning",
    "Neural Networks",
    "Covariate Shift"
  ],
  "rejected_keywords": [
    "Test Selection"
  ],
  "similarity_scores": {
    "Transfer Learning": 0.78,
    "Neural Networks": 0.85,
    "Covariate Shift": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# MetaSel: A Test Selection Approach for Fine-tuned DNN Models

**Korean Title:** 메타셀: 세밀하게 조정된 DNN 모델을 위한 테스트 선택 접근 방식

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|Deep Neural Networks]]
**🔗 Specific Connectable**: [[keywords/Transfer Learning|Fine-tuning]]
**⚡ Unique Technical**: [[keywords/Covariate Shift|Covariate Shift]]

## 🔗 유사한 논문
- [[DiffGAN_A_Test_Generation_Approach_for_Differential_Testing_of_Deep_Neural_Networks_for_Image_Analysis_20250918|DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis]] (79.9% similar)
- [[Controllable Pareto Trade-off between Fairness and Accuracy]] (78.9% similar)
- [[Meta-Learning Linear Models for Molecular Property Prediction]] (78.5% similar)
- [[Effort-Optimized,_Accuracy-Driven_Labelling_and_Validation_of_Test_Inputs_for_DL_Systems_A_Mixed-Integer_Linear_Programming_Approach_20250918|Effort-Optimized, Accuracy-Driven Labelling and Validation of Test Inputs for DL Systems: A Mixed-Integer Linear Programming Approach]] (78.4% similar)
- [[DRDT3: Diffusion-Refined Decision Test-Time Training Model]] (78.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.17534v4 Announce Type: replace 
Abstract: Deep Neural Networks (DNNs) face challenges during deployment due to covariate shift, i.e., data distribution shifts between development and deployment contexts. Fine-tuning adapts pre-trained models to new contexts requiring smaller labeled sets. However, testing fine-tuned models under constrained labeling budgets remains a critical challenge. This paper introduces MetaSel, a new approach tailored for DNN models that have been fine-tuned to address covariate shift, to select tests from unlabeled inputs. MetaSel assumes that fine-tuned and pre-trained models share related data distributions and exhibit similar behaviors for many inputs. However, their behaviors diverge within the input subspace where fine-tuning alters decision boundaries, making those inputs more prone to misclassification. Unlike general approaches that rely solely on the DNN model and its input set, MetaSel leverages information from both the fine-tuned and pre-trained models and their behavioral differences to estimate misclassification probability for unlabeled test inputs, enabling more effective test selection. Our extensive empirical evaluation, comparing MetaSel against 11 state-of-the-art approaches and involving 68 fine-tuned models across weak, medium, and strong distribution shifts, demonstrates that MetaSel consistently delivers significant improvements in Test Relative Coverage (TRC) over existing baselines, particularly under highly constrained labeling budgets. MetaSel shows average TRC improvements of 28.46% to 56.18% over the most frequent second-best baselines while maintaining a high TRC median and low variability. Our results confirm MetaSel's practicality, robustness, and cost-effectiveness for test selection in the context of fine-tuned models.

## 🔍 Abstract (한글 번역)

arXiv:2503.17534v4 발표 유형: 대체
요약: 심층 신경망(DNNs)은 개발과 배포 환경 사이의 데이터 분포 변화로 인한 공변량 이동으로 인해 배포 중에 도전을 겪습니다. 파인튜닝은 새로운 맥락에 사전 훈련된 모델을 적응시키는 데 필요한 더 작은 라벨이 달린 세트를 요구합니다. 그러나 제한된 라벨링 예산 하에서 파인튜닝된 모델을 테스트하는 것은 여전히 중요한 도전 과제입니다. 본 논문은 공변량 이동을 해결하기 위해 파인튜닝된 DNN 모델에 맞춘 새로운 접근 방식인 MetaSel을 소개합니다. MetaSel은 파인튜닝된 모델과 사전 훈련된 모델이 관련된 데이터 분포를 공유하고 많은 입력에 대해 유사한 행동을 보여준다고 가정합니다. 그러나 파인튜닝이 결정 경계를 변경하는 입력 부분 공간에서 그들의 행동이 다르게 되어 해당 입력이 잘못 분류될 가능성이 높아집니다. DNN 모델과 입력 세트만을 의존하는 일반적인 접근 방식과 달리, MetaSel은 파인튜닝된 모델과 사전 훈련된 모델 및 그들의 행동적 차이로부터 라벨이 없는 테스트 입력에 대한 잘못 분류 확률을 추정하여 보다 효과적인 테스트 선택을 가능하게 합니다. 약, 중간, 강한 분포 변화를 가진 68개의 파인튜닝된 모델에 대해 MetaSel을 11가지 최첨단 접근 방식과 비교하는 방대한 경험적 평가는 MetaSel이 기존 기준선에 비해 특히 높은 제한된 라벨링 예산 하에서 테스트 상대적 커버리지(TRC)에서 상당한 개선을 지속적으로 제공함을 보여줍니다. MetaSel은 가장 빈도가 높은 두 번째 최고의 기준선에 대해 평균 TRC 개선률이 28.46%에서 56.18%를 보여주며 높은 TRC 중위값과 낮은 변동성을 유지합니다. 우리의 결과는 파인튜닝된 모델의 맥락에서의 테스트 선택에 대한 MetaSel의 실용성, 견고성 및 비용 효율성을 확인합니다.

## 📝 요약

본 연구는 covariate shift로 인해 배포 중에 발생하는 문제를 해결하기 위해 fine-tuning된 DNN 모델을 위한 새로운 접근 방식인 MetaSel을 소개한다. MetaSel은 fine-tuned 및 pre-trained 모델이 관련된 데이터 분포를 공유하고 많은 입력에 대해 유사한 행동을 보이지만, fine-tuning으로 인해 결정 경계가 변경되는 입력 부분 공간에서 그들의 행동이 다르다고 가정한다. MetaSel은 fine-tuned 및 pre-trained 모델 및 그들의 행동 차이로부터 정보를 활용하여 라벨이 지정되지 않은 테스트 입력에 대한 잘못된 분류 확률을 추정함으로써 더 효과적인 테스트 선택을 가능하게 한다. MetaSel은 다양한 실험 결과를 통해 기존 기준선 대비 Test Relative Coverage(TRC)에서 상당한 개선을 보여주며, 특히 라벨링 예산이 제한적인 경우에 더욱 효과적임을 입증하였다. 이러한 결과는 MetaSel이 fine-tuned 모델의 테스트 선택에 있어 실용성, 견고성 및 비용 효율성을 보여준다.

## 🎯 주요 포인트

- 1. MetaSel은 DNN 모델의 효율적인 테스트 선택을 위해 fine-tuned 및 pre-trained 모델의 정보를 활용한다.

- 2. MetaSel은 라벨링 예산이 제한된 상황에서도 높은 Test Relative Coverage(TCR) 향상을 제공한다.

- 3. MetaSel은 fine-tuned 모델의 특정 입력 하위 공간에서의 동작 차이를 이용하여 미분류 확률을 추정한다.

---

*Generated on 2025-09-18 16:47:15*