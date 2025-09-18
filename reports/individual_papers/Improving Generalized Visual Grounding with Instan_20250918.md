
# Improving Generalized Visual Grounding with Instance-aware Joint Learning

**Korean Title:** 인스턴스 인식 공통 시각적 기반 개선을 위한 합동 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-granularity Predictions|Multi-granularity Predictions]] [[keywords/broad/Generalized Visual Grounding|Generalized Visual Grounding]] [[keywords/broad/Instance-aware Joint Learning|Instance-aware Joint Learning]] [[keywords/specific/Multi-task Learning|Multi-task Learning]] [[keywords/unique/InstanceVG|InstanceVG]] [[categories/cs.CV|cs.CV]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-granularity Predictions
**🔬 Broad Technical**: Generalized Visual Grounding, Instance-aware Joint Learning
**🔗 Specific Connectable**: Multi-task Learning
**⭐ Unique Technical**: InstanceVG

**ArXiv ID**: [2509.13747](https://arxiv.org/abs/2509.13747)
**Published**: 2025-09-18
**Category**: cs.CV
**PDF**: [Download](https://arxiv.org/pdf/2509.13747.pdf)


## 🏷️ 추출된 키워드



`Generalized Visual Grounding` • 

`Instance-aware Joint Learning` • 

`Multi-task Learning` • 

`InstanceVG` • 

`Multi-granularity Predictions`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13747v1 Announce Type: new 
Abstract: Generalized visual grounding tasks, including Generalized Referring Expression Comprehension (GREC) and Segmentation (GRES), extend the classical visual grounding paradigm by accommodating multi-target and non-target scenarios. Specifically, GREC focuses on accurately identifying all referential objects at the coarse bounding box level, while GRES aims for achieve fine-grained pixel-level perception. However, existing approaches typically treat these tasks independently, overlooking the benefits of jointly training GREC and GRES to ensure consistent multi-granularity predictions and streamline the overall process. Moreover, current methods often treat GRES as a semantic segmentation task, neglecting the crucial role of instance-aware capabilities and the necessity of ensuring consistent predictions between instance-level boxes and masks. To address these limitations, we propose InstanceVG, a multi-task generalized visual grounding framework equipped with instance-aware capabilities, which leverages instance queries to unify the joint and consistency predictions of instance-level boxes and masks. To the best of our knowledge, InstanceVG is the first framework to simultaneously tackle both GREC and GRES while incorporating instance-aware capabilities into generalized visual grounding. To instantiate the framework, we assign each instance query a prior reference point, which also serves as an additional basis for target matching. This design facilitates consistent predictions of points, boxes, and masks for the same instance. Extensive experiments obtained on ten datasets across four tasks demonstrate that InstanceVG achieves state-of-the-art performance, significantly surpassing the existing methods in various evaluation metrics. The code and model will be publicly available at https://github.com/Dmmm1997/InstanceVG.

## 🔍 Abstract (한글 번역)

arXiv:2509.13747v1 발표 유형: 새로운
요약: 일반화된 시각적 기반 작업인 일반화된 지시 표현 이해 (GREC) 및 세분화 (GRES)를 포함한 작업은 다중 대상 및 비대상 시나리오를 수용하여 고전적인 시각적 기반 패러다임을 확장합니다. 특히, GREC는 대략적인 경계 상자 수준에서 모든 지시 대상 객체를 정확하게 식별하는 데 초점을 맞추고, GRES는 세밀한 픽셀 수준 인식을 달성하기 위해 노력합니다. 그러나 기존 접근 방식은 일반적으로 이러한 작업을 독립적으로 처리하여 GREC 및 GRES를 함께 훈련하여 일관된 다중 단위 예측을 보장하고 전체 프로세스를 간소화하는 이점을 간과합니다. 또한 현재 방법은 종종 GRES를 의미 분할 작업으로 취급하여 인스턴스 인식 능력의 중요성과 인스턴스 수준 상자 및 마스크 사이의 일관된 예측을 보장해야 하는 필요성을 무시합니다. 이러한 한계를 해결하기 위해 우리는 인스턴스 인식 능력이 갖춰진 다중 작업 일반화된 시각적 기반 프레임워크 인 InstanceVG를 제안합니다. 이 프레임워크는 인스턴스 쿼리를 활용하여 인스턴스 수준 상자와 마스크의 공동 및 일관된 예측을 통합합니다. 우리의 지식으로는 InstanceVG가 일반화된 시각적 기반에 인스턴스 인식 능력을 통합하면서 GREC와 GRES를 동시에 다루는 첫 번째 프레임워크입니다. 이 프레임워크를 실체화하기 위해 각 인스턴스 쿼리에 사전 참조 지점을 할당하고 이는 대상 일치를 위한 추가 기준으로도 작용합니다. 이 설계는 동일한 인스턴스에 대한 점, 상자 및 마스크의 일관된 예측을 용이하게 합니다. 네 가지 작업을 통해 열 개의 데이터셋에서 수행된 광범위한 실험 결과는 InstanceVG가 다양한 평가 지표에서 기존 방법을 크게 능가하며 최첨단 성능을 달성한다는 것을 보여줍니다. 코드 및 모델은 https://github.com/Dmmm1997/InstanceVG에서 공개적으로 이용 가능합니다.

## 📝 요약

이 연구는 일반화된 시각적 그라운딩 작업을 다루고 있으며, 특히 일반화된 지시어 이해 및 세분화 작업을 다루고 있다. 기존 방법론은 이러한 작업들을 독립적으로 처리하여 일관성 있는 다중 단계 예측을 보장하지 못했지만, 본 연구에서는 InstanceVG라는 다중 작업 일반화된 시각적 그라운딩 프레임워크를 제안하였다. 이 프레임워크는 인스턴스 인식 능력을 갖추어 인스턴스 수준 상자와 마스크 간 일관된 예측을 보장한다. 실험 결과는 InstanceVG가 다양한 평가 지표에서 기존 방법을 크게 능가하는 최고 수준의 성능을 달성한다는 것을 보여준다.

## 🎯 주요 포인트


- 1. 일반화된 시각적 그라운딩 작업을 위한 InstanceVG 프레임워크가 GREC 및 GRES를 동시에 다루며 인스턴스 인식 능력을 통합하여 최적의 성능을 보임.

- 2. InstanceVG는 인스턴스 쿼리에 이전 참조점을 할당하여 일관된 예측을 용이하게 함.

- 3. InstanceVG는 GREC 및 GRES를 동시에 처리하고 인스턴스 인식 능력을 포함한 첫 번째 프레임워크임.


---

*Generated on 2025-09-18 17:00:07*