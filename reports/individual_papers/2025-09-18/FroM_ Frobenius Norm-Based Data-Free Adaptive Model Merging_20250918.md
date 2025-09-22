
# FroM: Frobenius Norm-Based Data-Free Adaptive Model Merging

**Korean Title:** 제목: 프로베니우스 노름을 기반으로 한 데이터 무료 적응형 모델 병합

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive merging

## 🔗 유사한 논문
- [[HAM_Hierarchical_Adapter_Merging_for_Scalable_Continual_Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (80.5% similar)
- [[MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (79.1% similar)
- [[Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (79.1% similar)
- [[THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (78.5% similar)
- [[Masked_Feature_Modeling_Enhances_Adaptive_Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (78.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.02478v2 Announce Type: replace 
Abstract: With the development of large language models, fine-tuning has emerged as an effective method to enhance performance in specific scenarios by injecting domain-specific knowledge. In this context, model merging techniques provide a solution for fusing knowledge from multiple fine-tuning models by combining their parameters. However, traditional methods often encounter task interference when merging full fine-tuning models, and this problem becomes even more evident in parameter-efficient fine-tuning scenarios. In this paper, we introduce an improvement to the RegMean method, which indirectly leverages the training data to approximate the outputs of the linear layers before and after merging. We propose an adaptive merging method called FroM, which directly measures the model parameters using the Frobenius norm, without any training data. By introducing an additional hyperparameter for control, FroM outperforms baseline methods across various fine-tuning scenarios, alleviating the task interference problem.

## 🔍 Abstract (한글 번역)

arXiv:2506.02478v2 발표 유형: 대체
요약: 대규모 언어 모델의 발전으로 인해, 파인 튜닝은 도메인 특정 지식을 주입하여 특정 시나리오에서 성능을 향상시키는 효과적인 방법으로 부상했습니다. 이 맥락에서, 모델 병합 기술은 여러 파인 튜닝 모델에서 지식을 결합하여 그들의 매개변수를 결합함으로써 해결책을 제공합니다. 그러나 전통적인 방법은 종종 전체 파인 튜닝 모델을 병합할 때 작업 간섭에 직면하며, 이 문제는 매개변수 효율적인 파인 튜닝 시나리오에서 더욱 뚜렷해집니다. 본 논문에서는 RegMean 방법을 개선하여 제안합니다. 이 방법은 훈련 데이터를 간접적으로 활용하여 병합 전후의 선형 레이어의 출력을 근사화합니다. 우리는 Frobenius norm을 사용하여 모델 매개변수를 직접 측정하는 적응형 병합 방법인 FroM을 제안합니다. 훈련 데이터 없이도. 제어를 위한 추가 하이퍼파라미터를 도입함으로써, FroM은 다양한 파인 튜닝 시나리오에서 기존 방법을 능가하며 작업 간섭 문제를 완화시킵니다.

## 📝 요약

최근 대형 언어 모델의 발전으로 도메인 특화 지식을 주입하여 특정 시나리오에서 성능을 향상시키는 데 효과적인 파인튜닝이 등장했다. 이 연구에서는 모델 병합 기술이 여러 파인튜닝 모델로부터 지식을 융합하는 해결책을 제공한다. 기존 방법은 전체 파인튜닝 모델을 병합할 때 작업 간섭 문제를 겪지만, 저효율 파라미터 파인튜닝 시나리오에서 이 문제가 더욱 두드러진다. 본 논문에서는 RegMean 방법을 개선한 FroM 방법을 소개한다. FroM은 훈련 데이터를 간접적으로 활용하여 모델 파라미터를 직접 측정하는 적응형 병합 방법으로, 추가적인 하이퍼파라미터를 도입하여 다양한 파인튜닝 시나리오에서 작업 간섭 문제를 완화시키며 기존 방법을 능가한다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델의 발전으로 세부 도메인 지식을 주입하여 성능을 향상시키는 효과적인 방법으로 세밀 조정이 부각되었다.

- 2. 모델 병합 기술은 여러 세밀 조정 모델의 지식을 결합하여 파라미터를 합치는 해결책을 제공한다.

- 3. FroM이라는 적응형 병합 방법은 훈련 데이터를 간접적으로 활용하여 선형 레이어의 출력을 근사화하며, 기존 방법보다 더 나은 성능을 보인다.

---

*Generated on 2025-09-18 16:54:42*