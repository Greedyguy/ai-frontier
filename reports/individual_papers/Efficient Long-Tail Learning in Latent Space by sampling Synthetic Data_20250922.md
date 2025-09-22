# Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data

**Korean Title:** 잠재 공간에서 합성 데이터를 샘플링하여 효율적인 롱테일 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Synthetic Data Generation

## 🔗 유사한 논문
- [[2025-09-22/Latent Zoning Network_ A Unified Principle for Generative Modeling, Representation Learning, and Classification_20250922|Latent Zoning Network A Unified Principle for Generative Modeling, Representation Learning, and Classification]] (84.8% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (84.0% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (83.7% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.1% similar)
- [[2025-09-22/LiteLong_ Resource-Efficient Long-Context Data Synthesis for LLMs_20250922|LiteLong Resource-Efficient Long-Context Data Synthesis for LLMs]] (82.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15859v1 Announce Type: new 
Abstract: Imbalanced classification datasets pose significant challenges in machine learning, often leading to biased models that perform poorly on underrepresented classes. With the rise of foundation models, recent research has focused on the full, partial, and parameter-efficient fine-tuning of these models to deal with long-tail classification. Despite the impressive performance of these works on the benchmark datasets, they still fail to close the gap with the networks trained using the balanced datasets and still require substantial computational resources, even for relatively smaller datasets. Underscoring the importance of computational efficiency and simplicity, in this work we propose a novel framework that leverages the rich semantic latent space of Vision Foundation Models to generate synthetic data and train a simple linear classifier using a mixture of real and synthetic data for long-tail classification. The computational efficiency gain arises from the number of trainable parameters that are reduced to just the number of parameters in the linear model. Our method sets a new state-of-the-art for the CIFAR-100-LT benchmark and demonstrates strong performance on the Places-LT benchmark, highlighting the effectiveness and adaptability of our simple and effective approach.

## 🔍 Abstract (한글 번역)

arXiv:2509.15859v1 발표 유형: 신규  
초록: 불균형한 분류 데이터셋은 기계 학습에서 상당한 도전을 제기하며, 종종 과소 대표된 클래스에서 성능이 저조한 편향된 모델을 초래합니다. 기초 모델의 부상과 함께, 최근 연구는 이러한 모델의 전체, 부분, 그리고 매개변수 효율적인 미세 조정을 통해 롱테일 분류를 다루는 데 초점을 맞추고 있습니다. 이러한 연구들이 벤치마크 데이터셋에서 인상적인 성능을 보였음에도 불구하고, 여전히 균형 잡힌 데이터셋을 사용하여 훈련된 네트워크와의 격차를 해소하지 못하며, 비교적 작은 데이터셋에서도 상당한 계산 자원을 요구합니다. 계산 효율성과 단순성의 중요성을 강조하며, 본 연구에서는 Vision Foundation Models의 풍부한 의미론적 잠재 공간을 활용하여 합성 데이터를 생성하고, 실제 데이터와 합성 데이터를 혼합하여 간단한 선형 분류기를 훈련하는 새로운 프레임워크를 제안합니다. 계산 효율성의 향상은 선형 모델의 매개변수 수로 줄어든 훈련 가능한 매개변수의 수에서 비롯됩니다. 우리의 방법은 CIFAR-100-LT 벤치마크에서 새로운 최첨단 성과를 기록하고, Places-LT 벤치마크에서도 강력한 성능을 보여주며, 우리의 간단하고 효과적인 접근 방식의 효과성과 적응성을 강조합니다.

## 📝 요약

이 논문은 불균형한 분류 데이터셋에서 발생하는 문제를 해결하기 위해 새로운 프레임워크를 제안합니다. 기존의 기초 모델들은 여전히 균형 잡힌 데이터셋을 사용한 네트워크에 비해 성능이 떨어지고, 많은 계산 자원을 필요로 합니다. 본 연구에서는 Vision Foundation Models의 풍부한 의미론적 잠재 공간을 활용하여 합성 데이터를 생성하고, 실제 데이터와 합성 데이터를 혼합하여 간단한 선형 분류기를 훈련하는 방법을 제안합니다. 이 방법은 훈련 가능한 매개변수 수를 선형 모델의 매개변수 수로 줄여 계산 효율성을 높입니다. 제안된 방법은 CIFAR-100-LT 벤치마크에서 새로운 최고 성능을 기록했으며, Places-LT 벤치마크에서도 강력한 성능을 보여주었습니다.

## 🎯 주요 포인트

- 1. 불균형한 분류 데이터셋은 머신러닝에서 편향된 모델을 초래하여 소수 클래스에서 성능이 저하되는 문제를 야기한다.

- 2. 본 연구는 비전 기반 모델의 풍부한 의미론적 잠재 공간을 활용하여 합성 데이터를 생성하고, 실제 데이터와 합성 데이터를 혼합하여 간단한 선형 분류기를 훈련하는 새로운 프레임워크를 제안한다.

- 3. 제안된 방법은 CIFAR-100-LT 벤치마크에서 새로운 최고 성능을 기록하였으며, Places-LT 벤치마크에서도 강력한 성능을 보여준다.

- 4. 제안된 방법은 선형 모델의 매개변수 수로 훈련 가능한 매개변수를 줄여 계산 효율성을 크게 향상시킨다.

---

*Generated on 2025-09-22 15:26:28*