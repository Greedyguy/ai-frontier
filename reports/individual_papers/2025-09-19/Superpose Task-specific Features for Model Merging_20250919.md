---
keywords:
  - Model Merging
  - Multi-Task Capabilities
  - Linear Representation Hypothesis
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2502.10698
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:22:40.249632",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Model Merging",
    "Multi-Task Capabilities",
    "Linear Representation Hypothesis"
  ],
  "rejected_keywords": [
    "Neural Networks",
    "Feature Vectors"
  ],
  "similarity_scores": {
    "Model Merging": 0.85,
    "Multi-Task Capabilities": 0.8,
    "Linear Representation Hypothesis": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Superpose Task-specific Features for Model Merging

**Korean Title:** 모델 병합을 위한 작업별 특징 중첩

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multi-Task Capabilities|Multi-Task Capabilities]]
**⚡ Unique Technical**: [[keywords/Model Merging|Model Merging]], [[keywords/Linear Representation Hypothesis|Linear Representation Hypothesis]]

## 🔗 유사한 논문
- [[FroM Frobenius Norm-Based Data-Free Adaptive Model Merging]] (84.2% similar)
- [[HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (81.9% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.6% similar)
- [[Masked_Feature_Modeling_Enhances_Adaptive_Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (80.3% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.10698v2 Announce Type: replace-cross 
Abstract: Model merging enables powerful capabilities in neural networks without requiring additional training. In this paper, we introduce a novel perspective on model merging by leveraging the fundamental mechanisms of neural network representation. Our approach is motivated by the linear representation hypothesis, which states that neural networks encode information through linear combinations of feature vectors. We propose a method that superposes task-specific features from individual models into a merged model. Our approach specifically targets linear transformation matrices, which are crucial for feature activation and extraction in deep networks. By formulating the merging process as a linear system, we can preserve task-specific features from individual models and create merged models that effectively maintain multi-task capabilities compared to existing methods. Extensive experiments across diverse benchmarks and models demonstrate that our method outperforms existing techniques. Code is available at https://github.com/LARS-research/STF.

## 🔍 Abstract (한글 번역)

arXiv:2502.10698v2 발표 유형: 교차 교체  
초록: 모델 병합은 추가적인 훈련 없이 신경망의 강력한 기능을 가능하게 합니다. 본 논문에서는 신경망 표현의 기본 메커니즘을 활용하여 모델 병합에 대한 새로운 관점을 소개합니다. 우리의 접근법은 신경망이 특징 벡터의 선형 결합을 통해 정보를 인코딩한다는 선형 표현 가설에 의해 동기 부여되었습니다. 우리는 개별 모델의 작업별 특징을 병합된 모델에 중첩시키는 방법을 제안합니다. 우리의 접근법은 특히 심층 네트워크에서 특징 활성화와 추출에 중요한 선형 변환 행렬을 대상으로 합니다. 병합 과정을 선형 시스템으로 공식화함으로써, 개별 모델의 작업별 특징을 보존하고 기존 방법과 비교하여 다중 작업 기능을 효과적으로 유지하는 병합 모델을 생성할 수 있습니다. 다양한 벤치마크와 모델에 대한 광범위한 실험을 통해 우리의 방법이 기존 기술을 능가함을 입증합니다. 코드는 https://github.com/LARS-research/STF에서 확인할 수 있습니다.

## 📝 요약

이 논문은 추가 학습 없이 신경망의 강력한 기능을 활용할 수 있는 모델 병합에 대한 새로운 관점을 제시합니다. 저자들은 신경망이 정보 인코딩을 선형 조합을 통해 수행한다는 가설을 바탕으로, 개별 모델의 작업별 특징을 병합 모델에 중첩하는 방법을 제안합니다. 특히, 특징 활성화와 추출에 중요한 선형 변환 행렬을 대상으로 하여 병합 과정을 선형 시스템으로 공식화함으로써, 개별 모델의 작업별 특징을 보존하면서도 다중 작업 기능을 유지하는 병합 모델을 생성합니다. 다양한 벤치마크와 모델을 대상으로 한 실험에서 제안된 방법이 기존 기술보다 우수한 성능을 보임을 입증했습니다. 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 본 논문은 추가적인 학습 없이 신경망의 강력한 기능을 가능하게 하는 모델 병합에 대한 새로운 관점을 제시합니다.

- 2. 모델 병합을 위해 선형 표현 가설을 활용하여 개별 모델의 작업별 특징을 병합 모델에 중첩하는 방법을 제안합니다.

- 3. 선형 변환 행렬을 대상으로 하여, 개별 모델의 작업별 특징을 보존하면서 다중 작업 기능을 효과적으로 유지하는 병합 모델을 생성합니다.

- 4. 다양한 벤치마크와 모델을 대상으로 한 실험에서 제안된 방법이 기존 기술보다 우수한 성능을 보임을 입증합니다.

- 5. 연구의 코드는 https://github.com/LARS-research/STF에서 제공됩니다.

---

*Generated on 2025-09-19 15:11:05*