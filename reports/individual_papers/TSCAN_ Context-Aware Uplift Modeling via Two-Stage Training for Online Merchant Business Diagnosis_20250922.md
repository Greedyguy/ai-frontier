# TSCAN: Context-Aware Uplift Modeling via Two-Stage Training for Online Merchant Business Diagnosis

**Korean Title:** TSCAN: 온라인 상거래 비즈니스 진단을 위한 두 단계 훈련 기반의 문맥 인식 업리프트 모델링

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Context-Aware Uplift|Context-Aware Uplift]] [[keywords/specific/Attention Mechanism|Attention Mechanism]] [[keywords/specific/Propensity Score Modeling|Propensity Score Modeling]] [[keywords/broad/Uplift Modeling|Uplift Modeling]] [[keywords/unique/TSCAN|TSCAN]] [[categories/cs.LG|cs.LG]] [[2025-09-22/No Black Box Anymore_ Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism_20250922|No Black Box Anymore: Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism]] (81.2% similar) [[2025-09-22/CIDER_ A Causal Cure for Brand-Obsessed Text-to-Image Models_20250922|CIDER: A Causal Cure for Brand-Obsessed Text-to-Image Models]] (80.3% similar) [[2025-09-22/Two Is Better Than One_ Aligned Representation Pairs for Anomaly Detection_20250922|Two Is Better Than One: Aligned Representation Pairs for Anomaly Detection]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Context-Aware Uplift Modeling
**🔗 Specific Connectable**: Attention Mechanism, Propensity Score Modeling
**🔬 Broad Technical**: Uplift Modeling
**⭐ Unique Technical**: TSCAN
## 🔗 유사한 논문
- [[2025-09-22/No Black Box Anymore_ Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism_20250922|No Black Box Anymore Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism]] (81.2% similar)
- [[2025-09-22/CIDER_ A Causal Cure for Brand-Obsessed Text-to-Image Models_20250922|CIDER A Causal Cure for Brand-Obsessed Text-to-Image Models]] (80.3% similar)
- [[2025-09-22/Two Is Better Than One_ Aligned Representation Pairs for Anomaly Detection_20250922|Two Is Better Than One Aligned Representation Pairs for Anomaly Detection]] (79.9% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (78.8% similar)
- [[2025-09-17/Compute as Teacher_ Turning Inference Compute Into Reference-Free Supervision_20250917|Compute as Teacher Turning Inference Compute Into Reference-Free Supervision]] (78.3% similar)


**ArXiv ID**: [2504.18881](https://arxiv.org/abs/2504.18881)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2504.18881.pdf)


**ArXiv ID**: [2504.18881](https://arxiv.org/abs/2504.18881)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2504.18881.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Context-Aware Uplift Modeling
**🔗 Specific Connectable**: Attention Mechanism, Propensity Score Modeling
**⭐ Unique Technical**: TSCAN
**🔬 Broad Technical**: Uplift Modeling

## 🏷️ 추출된 키워드



`Uplift Modeling` • 

`Attention Mechanism` • 

`Propensity Score Modeling` • 

`TSCAN` • 

`Context-Aware Uplift Modeling`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.18881v2 Announce Type: replace 
Abstract: A primary challenge in ITE estimation is sample selection bias. Traditional approaches utilize treatment regularization techniques such as the Integral Probability Metrics (IPM), re-weighting, and propensity score modeling to mitigate this bias. However, these regularizations may introduce undesirable information loss and limit the performance of the model. Furthermore, treatment effects vary across different external contexts, and the existing methods are insufficient in fully interacting with and utilizing these contextual features. To address these issues, we propose a Context-Aware uplift model based on the Two-Stage training approach (TSCAN), comprising CAN-U and CAN-D sub-models. In the first stage, we train an uplift model, called CAN-U, which includes the treatment regularizations of IPM and propensity score prediction, to generate a complete dataset with counterfactual uplift labels. In the second stage, we train a model named CAN-D, which utilizes an isotonic output layer to directly model uplift effects, thereby eliminating the reliance on the regularization components. CAN-D adaptively corrects the errors estimated by CAN-U through reinforcing the factual samples, while avoiding the negative impacts associated with the aforementioned regularizations. Additionally, we introduce a Context-Aware Attention Layer throughout the two-stage process to manage the interactions between treatment, merchant, and contextual features, thereby modeling the varying treatment effect in different contexts. We conduct extensive experiments on two real-world datasets to validate the effectiveness of TSCAN. Ultimately, the deployment of our model for real-world merchant diagnosis on one of China's largest online food ordering platforms validates its practical utility and impact.

## 🔍 Abstract (한글 번역)

arXiv:2504.18881v2 발표 유형: 교체  
초록: ITE(Individual Treatment Effect) 추정에서 주요 도전 과제는 샘플 선택 편향입니다. 전통적인 접근법은 이 편향을 완화하기 위해 적분 확률 지표(IPM), 재가중치, 성향 점수 모델링과 같은 치료 정규화 기법을 활용합니다. 그러나 이러한 정규화는 바람직하지 않은 정보 손실을 초래하고 모델의 성능을 제한할 수 있습니다. 게다가, 치료 효과는 다양한 외부 맥락에 따라 다르며, 기존 방법들은 이러한 맥락적 특징을 충분히 상호작용하고 활용하는 데에 부족합니다. 이러한 문제를 해결하기 위해, 우리는 CAN-U와 CAN-D 하위 모델로 구성된 이단계 훈련 접근법(TSCAN)에 기반한 맥락 인식 상승 모델을 제안합니다. 첫 번째 단계에서는 IPM과 성향 점수 예측의 치료 정규화를 포함하는 상승 모델 CAN-U를 훈련하여 반사실적 상승 레이블이 포함된 완전한 데이터셋을 생성합니다. 두 번째 단계에서는 CAN-D라는 모델을 훈련하여, 정규화 구성 요소에 대한 의존성을 제거하면서 상승 효과를 직접 모델링하기 위해 등위 출력 계층을 활용합니다. CAN-D는 사실 샘플을 강화하여 CAN-U가 추정한 오류를 적응적으로 수정하며, 앞서 언급한 정규화와 관련된 부정적인 영향을 피합니다. 또한, 우리는 치료, 상인, 맥락적 특징 간의 상호작용을 관리하여 다양한 맥락에서의 치료 효과를 모델링하기 위해 이단계 과정 전반에 걸쳐 맥락 인식 주의 계층을 도입합니다. 우리는 TSCAN의 효과성을 검증하기 위해 두 개의 실제 데이터셋에서 광범위한 실험을 수행합니다. 궁극적으로, 중국 최대의 온라인 음식 주문 플랫폼 중 하나에서 실제 상인 진단을 위한 모델 배포는 그 실용성과 영향을 검증합니다.

## 📝 요약

이 논문은 ITE(Individual Treatment Effect) 추정에서 발생하는 표본 선택 편향 문제를 해결하기 위해 TSCAN이라는 새로운 모델을 제안합니다. TSCAN은 두 단계로 구성되며, 첫 번째 단계에서는 CAN-U 모델을 통해 IPM 및 성향 점수 예측을 활용하여 반사실적 상승 효과 레이블을 생성합니다. 두 번째 단계에서는 CAN-D 모델이 등간 출력층을 사용하여 직접 상승 효과를 모델링하며, 기존의 정규화 요소에 대한 의존성을 제거합니다. 또한, 문맥 인식 주의 레이어를 도입하여 다양한 외부 문맥에서의 치료 효과를 효과적으로 모델링합니다. 두 개의 실제 데이터셋을 통해 TSCAN의 효과를 검증하였으며, 중국의 대형 온라인 음식 주문 플랫폼에서의 실제 적용을 통해 실용성을 입증했습니다.

## 🎯 주요 포인트


- 1. ITE 추정에서 샘플 선택 편향 문제를 해결하기 위해 TSCAN이라는 컨텍스트 인식 향상 모델을 제안합니다.

- 2. TSCAN은 두 단계로 구성되며, 첫 번째 단계에서는 CAN-U 모델을 통해 반사실적 향상 레이블을 생성합니다.

- 3. 두 번째 단계에서는 CAN-D 모델을 통해 정규화 구성 요소에 의존하지 않고 향상 효과를 직접 모델링합니다.

- 4. 컨텍스트 인식 주의 레이어를 도입하여 다양한 외부 컨텍스트에서의 치료 효과를 모델링합니다.

- 5. 실제 데이터셋을 활용한 실험을 통해 TSCAN의 효과성을 검증하였으며, 중국의 대형 온라인 음식 주문 플랫폼에서의 실용성을 입증했습니다.


---

*Generated on 2025-09-22 15:57:58*