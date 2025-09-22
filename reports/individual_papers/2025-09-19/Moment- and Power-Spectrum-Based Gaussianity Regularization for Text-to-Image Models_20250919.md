
# Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models

**Korean Title:** 텍스트-투-이미지 모델을 위한 모멘트 및 파워 스펙트럼 기반 가우시안성 정규화

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Moment Based Regularization

## 🔗 유사한 논문
- [[BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (78.9% similar)
- [[Iterative_Prompt_Refinement_for_Safer_Text-to-Image_Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (78.2% similar)
- [[Generative_AI_for_Misalignment-Resistant_Virtual_Staining_to_Accelerate_Histopathology_Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (77.4% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (77.1% similar)
- [[Superpose_Task-specific_Features_for_Model_Merging_20250919|Superpose Task-specific Features for Model Merging]] (77.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.07027v3 Announce Type: replace-cross 
Abstract: We propose a novel regularization loss that enforces standard Gaussianity, encouraging samples to align with a standard Gaussian distribution. This facilitates a range of downstream tasks involving optimization in the latent space of text-to-image models. We treat elements of a high-dimensional sample as one-dimensional standard Gaussian variables and define a composite loss that combines moment-based regularization in the spatial domain with power spectrum-based regularization in the spectral domain. Since the expected values of moments and power spectrum distributions are analytically known, the loss promotes conformity to these properties. To ensure permutation invariance, the losses are applied to randomly permuted inputs. Notably, existing Gaussianity-based regularizations fall within our unified framework: some correspond to moment losses of specific orders, while the previous covariance-matching loss is equivalent to our spectral loss but incurs higher time complexity due to its spatial-domain computation. We showcase the application of our regularization in generative modeling for test-time reward alignment with a text-to-image model, specifically to enhance aesthetics and text alignment. Our regularization outperforms previous Gaussianity regularization, effectively prevents reward hacking and accelerates convergence.

## 🔍 Abstract (한글 번역)

arXiv:2509.07027v3 발표 유형: 교체-교차  
초록: 우리는 표준 가우시안성을 강제하는 새로운 정규화 손실을 제안하며, 이는 샘플들이 표준 가우시안 분포와 일치하도록 장려합니다. 이는 텍스트-이미지 모델의 잠재 공간에서 최적화를 포함한 다양한 후속 작업을 용이하게 합니다. 우리는 고차원 샘플의 요소들을 일차원 표준 가우시안 변수로 취급하고, 공간 도메인에서의 모멘트 기반 정규화와 스펙트럼 도메인에서의 파워 스펙트럼 기반 정규화를 결합한 복합 손실을 정의합니다. 모멘트와 파워 스펙트럼 분포의 기대값이 분석적으로 알려져 있기 때문에, 이 손실은 이러한 속성에 대한 일치를 촉진합니다. 순열 불변성을 보장하기 위해, 손실은 무작위로 순열된 입력에 적용됩니다. 특히, 기존의 가우시안성 기반 정규화는 우리의 통합 프레임워크 내에 속하며, 일부는 특정 차수의 모멘트 손실에 해당하고, 이전의 공분산 매칭 손실은 우리의 스펙트럼 손실과 동일하지만 공간 도메인 계산으로 인해 더 높은 시간 복잡도를 초래합니다. 우리는 우리의 정규화를 텍스트-이미지 모델과의 테스트 시 보상 정렬을 위한 생성 모델링에 적용하여, 특히 미학적 향상과 텍스트 정렬을 강화하는 것을 보여줍니다. 우리의 정규화는 이전의 가우시안성 정규화를 능가하며, 보상 해킹을 효과적으로 방지하고 수렴을 가속화합니다.

## 📝 요약

이 논문은 표준 가우시안 분포에 맞추는 새로운 정규화 손실을 제안합니다. 이는 텍스트-이미지 모델의 잠재 공간에서 최적화를 용이하게 합니다. 고차원 샘플의 요소를 1차원 표준 가우시안 변수로 간주하고, 공간 도메인의 모멘트 기반 정규화와 스펙트럼 도메인의 파워 스펙트럼 기반 정규화를 결합한 복합 손실을 정의합니다. 이 손실은 모멘트와 파워 스펙트럼 분포의 기대값에 맞추도록 유도합니다. 기존의 가우시안 정규화는 이 통합 프레임워크에 포함되며, 제안된 방법은 텍스트-이미지 모델에서 미적 감각과 텍스트 정렬을 개선하는 데 효과적입니다. 제안된 정규화는 기존 방법보다 성능이 뛰어나며, 보상 해킹을 방지하고 수렴 속도를 높입니다.

## 🎯 주요 포인트

- 1. 표준 가우시안 분포와의 정렬을 촉진하는 새로운 정규화 손실을 제안합니다.

- 2. 공간 도메인에서의 모멘트 기반 정규화와 스펙트럼 도메인에서의 파워 스펙트럼 기반 정규화를 결합한 복합 손실을 정의합니다.

- 3. 기존의 가우시안 정규화 기법들은 우리의 통합 프레임워크 내에 포함되며, 특히 이전의 공분산 매칭 손실은 스펙트럼 손실과 동일하지만 더 높은 시간 복잡도를 가집니다.

- 4. 제안된 정규화는 텍스트-이미지 모델에서 미적 감각과 텍스트 정렬을 향상시키기 위한 테스트 시 보상 정렬에 효과적으로 적용됩니다.

- 5. 우리의 정규화는 기존의 가우시안 정규화보다 우수하며, 보상 해킹을 효과적으로 방지하고 수렴 속도를 가속화합니다.

---

*Generated on 2025-09-19 15:22:00*