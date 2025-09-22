# Beyond Pixels: Enhancing LIME with Hierarchical Features and Segmentation Foundation Models

**Korean Title:** 픽셀을 넘어: 계층적 특징 및 세분화 기초 모델을 통한 LIME 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hierarchical Segmentation

## 🔗 유사한 논문
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.0% similar)
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (81.2% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (80.8% similar)
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (80.6% similar)
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth Explainability Assessment in Monocular Depth Estimation]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2403.07733v5 Announce Type: replace-cross 
Abstract: LIME (Local Interpretable Model-agnostic Explanations) is a popular XAI framework for unraveling decision-making processes in vision machine-learning models. The technique utilizes image segmentation methods to identify fixed regions for calculating feature importance scores as explanations. Therefore, poor segmentation can weaken the explanation and reduce the importance of segments, ultimately affecting the overall clarity of interpretation. To address these challenges, we introduce the DSEG-LIME (Data-Driven Segmentation LIME) framework, featuring: i) a data-driven segmentation for human-recognized feature generation by foundation model integration, and ii) a user-steered granularity in the hierarchical segmentation procedure through composition. Our findings demonstrate that DSEG outperforms on several XAI metrics on pre-trained ImageNet models and improves the alignment of explanations with human-recognized concepts. The code is available under: https://github. com/patrick-knab/DSEG-LIME

## 🔍 Abstract (한글 번역)

arXiv:2403.07733v5 발표 유형: 교차 교체  
초록: LIME(Local Interpretable Model-agnostic Explanations)는 비전 머신러닝 모델의 의사결정 과정을 해석하는 데 널리 사용되는 XAI 프레임워크입니다. 이 기법은 이미지 분할 방법을 활용하여 설명으로서 특징 중요도 점수를 계산하기 위한 고정 영역을 식별합니다. 따라서, 부적절한 분할은 설명을 약화시키고 세그먼트의 중요성을 감소시켜 궁극적으로 해석의 전반적인 명확성에 영향을 미칠 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 DSEG-LIME(Data-Driven Segmentation LIME) 프레임워크를 소개합니다. 이 프레임워크는: i) 기초 모델 통합을 통한 인간이 인식할 수 있는 특징 생성을 위한 데이터 기반 분할, ii) 구성에 의한 계층적 분할 절차에서 사용자가 조정할 수 있는 세분성을 특징으로 합니다. 우리의 연구 결과는 DSEG가 사전 훈련된 ImageNet 모델에서 여러 XAI 지표에서 우수한 성능을 보이며, 설명이 인간이 인식하는 개념과의 정렬을 개선함을 보여줍니다. 코드는 다음에서 사용할 수 있습니다: https://github.com/patrick-knab/DSEG-LIME

## 📝 요약

이 논문은 LIME의 한계를 극복하기 위해 DSEG-LIME이라는 새로운 프레임워크를 제안합니다. DSEG-LIME은 데이터 기반 세분화를 통해 인간이 인식할 수 있는 특징을 생성하고, 사용자가 세분화의 세밀도를 조정할 수 있도록 합니다. 이를 통해 기존 LIME의 설명력을 향상시키고, 인간이 인식하는 개념과의 일치를 개선합니다. 연구 결과, DSEG-LIME은 사전 학습된 ImageNet 모델에서 여러 XAI 지표에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. LIME은 비전 머신러닝 모델의 의사결정 과정을 설명하기 위한 인기 있는 XAI 프레임워크입니다.

- 2. 기존 LIME의 이미지 분할 방식은 설명의 명확성을 저해할 수 있는 문제점이 있습니다.

- 3. DSEG-LIME은 데이터 기반 분할과 사용자 주도적 계층적 분할을 통해 이러한 문제를 해결합니다.

- 4. DSEG-LIME은 사전 학습된 ImageNet 모델에서 여러 XAI 지표에서 우수한 성능을 보이며, 인간이 인식하는 개념과의 정렬을 개선합니다.

- 5. DSEG-LIME의 코드는 https://github.com/patrick-knab/DSEG-LIME에서 이용 가능합니다.

---

*Generated on 2025-09-22 14:35:20*