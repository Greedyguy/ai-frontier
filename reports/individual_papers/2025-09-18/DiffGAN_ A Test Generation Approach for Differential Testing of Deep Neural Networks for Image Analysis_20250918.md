---
keywords:
  - Generative Models
  - Differential Testing
  - Neural Networks
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2410.19794
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:33:03.175218",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Generative Models",
    "Differential Testing",
    "Neural Networks"
  ],
  "rejected_keywords": [
    "Non-dominated Sorting Genetic Algorithm II"
  ],
  "similarity_scores": {
    "Generative Models": 0.78,
    "Differential Testing": 0.72,
    "Neural Networks": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis

**Korean Title:** DiffGAN: 이미지 분석을 위한 딥 뉴럴 네트워크의 차별적 테스트를 위한 테스트 생성 접근 방식

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Neural Networks|Deep Neural Networks]]
**🔗 Specific Connectable**: [[keywords/Generative Models|Generative Adversarial Network]]
**⚡ Unique Technical**: [[keywords/Differential Testing|Differential Testing]]

## 🔗 유사한 논문
- [[Evolution Meets Diffusion: Efficient Neural Architecture Generation]] (82.8% similar)
- [[MetaSel_A_Test_Selection_Approach_for_Fine-tuned_DNN_Models_20250918|MetaSel: A Test Selection Approach for Fine-tuned DNN Models]] (79.9% similar)
- [[DiffHash_Text-Guided_Targeted_Attack_via_Diffusion_Models_against_Deep_Hashing_Image_Retrieval_20250918|DiffHash: Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (79.5% similar)
- [[GROOD_GRadient-Aware_Out-of-Distribution_Detection_20250918|GROOD: GRadient-Aware Out-of-Distribution Detection]] (79.1% similar)
- [[Tabular Data Generation Models: An In-Depth Survey and Performance Benchmarks with Extensive Tuning]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.19794v4 Announce Type: replace-cross 
Abstract: Deep Neural Networks (DNNs) are increasingly deployed across applications. However, ensuring their reliability remains a challenge, and in many situations, alternative models with similar functionality and accuracy are available. Traditional accuracy-based evaluations often fail to capture behavioral differences between models, especially with limited test datasets, making it difficult to select or combine models effectively. Differential testing addresses this by generating test inputs that expose discrepancies in DNN model behavior. However, existing approaches face significant limitations: many rely on model internals or are constrained by available seed inputs. To address these challenges, we propose DiffGAN, a black-box test image generation approach for differential testing of DNN models. DiffGAN leverages a Generative Adversarial Network (GAN) and the Non-dominated Sorting Genetic Algorithm II to generate diverse and valid triggering inputs that reveal behavioral discrepancies between models. DiffGAN employs two custom fitness functions, focusing on diversity and divergence, to guide the exploration of the GAN input space and identify discrepancies between models' outputs. By strategically searching this space, DiffGAN generates inputs with specific features that trigger differences in model behavior. DiffGAN is black-box, making it applicable in more situations. We evaluate DiffGAN on eight DNN model pairs trained on widely used image datasets. Our results show DiffGAN significantly outperforms a SOTA baseline, generating four times more triggering inputs, with greater diversity and validity, within the same budget. Additionally, the generated inputs improve the accuracy of a machine learning-based model selection mechanism, which selects the best-performing model based on input characteristics and can serve as a smart output voting mechanism when using alternative models.

## 🔍 Abstract (한글 번역)

arXiv:2410.19794v4 공지 유형: replace-cross
요약: 심층 신경망(DNNs)은 다양한 응용 프로그램에서 점점 더 많이 사용되고 있습니다. 그러나 그들의 신뢰성을 보장하는 것은 여전히 어려운 과제이며, 많은 상황에서 유사한 기능과 정확도를 가진 대안 모델이 사용 가능합니다. 전통적인 정확도 기반 평가는 종종 모델 간의 행동 차이를 포착하지 못하며, 특히 제한된 테스트 데이터셋에서는 모델을 효과적으로 선택하거나 결합하기 어렵습니다. 차별적 테스트는 DNN 모델의 행동 차이를 드러내는 테스트 입력을 생성함으로써 이를 해결합니다. 그러나 기존 접근 방식은 중요한 제약 사항을 가지고 있습니다: 많은 것들이 모델 내부에 의존하거나 사용 가능한 초기 입력에 제한을 받습니다. 이러한 도전 과제를 해결하기 위해, 우리는 DNN 모델의 차별적 테스트를 위한 블랙박스 테스트 이미지 생성 접근법인 DiffGAN을 제안합니다. DiffGAN은 적합성이 없는 정렬 유전 알고리즘 II를 활용하여 모델 간의 행동 차이를 드러내는 다양하고 유효한 트리거 입력을 생성하는 생성적 적대 신경망(GAN)을 활용합니다. DiffGAN은 다양성과 발산에 초점을 맞춘 두 가지 사용자 정의 적합성 함수를 사용하여 GAN 입력 공간의 탐색을 안내하고 모델 출력 간의 차이를 식별합니다. 이 공간을 전략적으로 탐색함으로써 DiffGAN은 모델 행동에서 차이를 유발하는 특정 기능을 가진 입력을 생성합니다. DiffGAN은 블랙박스이므로 더 많은 상황에서 적용할 수 있습니다. 우리는 널리 사용되는 이미지 데이터셋에서 훈련된 여덟 개의 DNN 모델 쌍에 대해 DiffGAN을 평가했습니다. 결과는 DiffGAN이 SOTA 기준을 크게 능가하여 동일한 예산 내에서 더 많은 트리거 입력을 생성하며, 더 큰 다양성과 유효성을 보여줍니다. 또한 생성된 입력은 입력 특성을 기반으로 최상의 성능을 가진 모델을 선택하는 기계 학습 기반 모델 선택 메커니즘의 정확도를 향상시키며, 대안 모델을 사용할 때 스마트한 출력 투표 메커니즘으로 작동할 수 있습니다.

## 📝 요약

딥 뉴럴 네트워크(DNNs)의 신뢰성 확보는 여전히 어려운 문제이며, 다양한 상황에서 유사한 기능과 정확도를 갖는 대안 모델이 많이 존재한다. 기존의 정확도 중심 평가는 종종 모델 간의 행동 차이를 포착하지 못하며, 특히 제한된 테스트 데이터셋에서는 모델을 효과적으로 선택하거나 결합하기 어렵다. 본 연구에서는 DiffGAN이라는 DNN 모델 간의 차이를 드러내기 위한 블랙박스 테스트 이미지 생성 방법을 제안한다. DiffGAN은 GAN과 NSGA-II를 활용하여 다양하고 유효한 트리거 입력을 생성하여 모델 간의 행동 차이를 드러낸다. 실험 결과는 DiffGAN이 SOTA 기준을 크게 능가하며, 동일한 예산 내에서 더 많은 트리거 입력을 생성하고 더 큰 다양성과 유효성을 갖는 것을 보여준다. 또한, 생성된 입력은 입력 특성을 기반으로 최상의 모델을 선택하는 기계 학습 기반 모델 선택 메커니즘의 정확도를 향상시키며, 대안 모델을 사용할 때 스마트한 출력 투표 메커니즘으로 작용할 수 있다.

## 🎯 주요 포인트

- 1. DNN 모델 간의 행동 차이를 드러내는 유효한 입력을 생성하는 DiffGAN 제안

- 2. GAN과 NSGA-II를 활용하여 다양하고 유효한 트리거 입력 생성

- 3. 기존 방법들의 한계를 극복하며 SOTA 베이스라인을 크게 능가하는 성능을 보임

---

*Generated on 2025-09-18 16:49:17*