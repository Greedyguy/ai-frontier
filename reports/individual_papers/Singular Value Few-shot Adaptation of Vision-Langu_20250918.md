
# Singular Value Few-shot Adaptation of Vision-Language Models

**Korean Title:** 비전-언어 모델의 특이값 소수 샷 적응

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-modal Adaptation|Multi-modal Adaptation]] [[keywords/broad/Vision-Language Models|Vision-Language Models]] [[keywords/broad/Singular Value Decomposition|Singular Value Decomposition]] [[keywords/specific/Few-shot Learning|Few-shot Learning]] [[keywords/unique/CLIP-SVD|CLIP-SVD]] [[categories/cs.CL|cs.CL]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-modal Adaptation
**🔬 Broad Technical**: Vision-Language Models, Singular Value Decomposition
**🔗 Specific Connectable**: Few-shot Learning
**⭐ Unique Technical**: CLIP-SVD

**ArXiv ID**: [2509.03740](https://arxiv.org/abs/2509.03740)
**Published**: 2025-09-18
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.03740.pdf)


## 🏷️ 추출된 키워드



`Vision-Language Models` • 

`Singular Value Decomposition` • 

`Few-shot Learning` • 

`CLIP-SVD` • 

`Domain Adaptation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.03740v2 Announce Type: replace-cross 
Abstract: Vision-language models (VLMs) like CLIP have shown impressive zero-shot and few-shot learning capabilities across diverse applications. However, adapting these models to new fine-grained domains remains difficult due to reliance on prompt engineering and the high cost of full model fine-tuning. Existing adaptation approaches rely on augmented components, such as prompt tokens and adapter modules, which could limit adaptation quality, destabilize the model, and compromise the rich knowledge learned during pretraining. In this work, we present CLIP-SVD, a novel multi-modal and parameter-efficient adaptation technique that leverages Singular Value Decomposition (SVD) to modify the internal parameter space of CLIP without injecting additional modules. Specifically, we fine-tune only the singular values of the CLIP parameter matrices to rescale the basis vectors for domain adaptation while retaining the pretrained model. This design enables enhanced adaptation performance using only 0.04% of the model's total parameters and better preservation of its generalization ability. CLIP-SVD achieves state-of-the-art classification results on 11 natural and 10 biomedical datasets, outperforming previous methods in both accuracy and generalization under few-shot settings. Additionally, we leverage a natural language-based approach to analyze the effectiveness and dynamics of the CLIP adaptation to allow interpretability of CLIP-SVD. The code is publicly available at https://github.com/HealthX-Lab/CLIP-SVD.

## 🔍 Abstract (한글 번역)

arXiv:2509.03740v2 발표 유형: replace-cross
요약: CLIP와 같은 시각-언어 모델(VLMs)은 다양한 응용 분야에서 인상적인 제로샷 및 퓨샷 학습 능력을 보여주었습니다. 그러나 이러한 모델을 새로운 세부 도메인에 적응시키는 것은 프롬프트 엔지니어링에 의존하고 전체 모델 파인튜닝의 높은 비용 때문에 여전히 어려움이 남아 있습니다. 기존의 적응 접근 방식은 프롬프트 토큰 및 어댑터 모듈과 같은 보조 구성 요소에 의존하는데, 이는 적응 품질을 제한하고 모델을 불안정하게 만들며 사전 훈련 중에 학습한 풍부한 지식을 손상시킬 수 있습니다. 본 연구에서는 CLIP-SVD라는 새로운 멀티모달 및 파라미터 효율적인 적응 기술을 제시합니다. 이 기술은 Singular Value Decomposition (SVD)을 활용하여 CLIP의 내부 파라미터 공간을 수정하여 추가 모듈을 주입하지 않고도 도메인 적응을 위한 기저 벡터를 재조정합니다. 구체적으로, 우리는 CLIP 파라미터 행렬의 특이값만을 파인튜닝하여 사전 훈련된 모델을 유지한 채 도메인 적응을 위한 기저 벡터를 재조정합니다. 이 설계는 모델의 총 파라미터 중 0.04%만을 사용하여 향상된 적응 성능과 일반화 능력을 더 잘 보존할 수 있게 합니다. CLIP-SVD는 11개의 자연 및 10개의 생물의학 데이터셋에서 최신 분류 결과를 달성하며, 적은 샷 설정에서 정확도와 일반화 면에서 이전 방법을 능가합니다. 또한, 우리는 CLIP 적응의 효과와 역학을 분석하기 위해 자연어 기반 접근 방식을 활용하여 CLIP-SVD의 해석 가능성을 허용합니다. 코드는 https://github.com/HealthX-Lab/CLIP-SVD에서 공개적으로 제공됩니다.

## 📝 요약

이 연구는 CLIP-SVD라는 새로운 멀티모달 및 매개변수 효율적인 적응 기술을 제안한다. 이 기술은 CLIP의 내부 매개변수 공간을 수정하기 위해 특이값 분해(SVD)를 활용하며, 추가 모듈을 삽입하지 않고 도메인 적응을 위해 CLIP 매개변수 행렬의 특이값만을 미세조정한다. 이 설계는 모델의 총 매개변수의 0.04%만을 사용하여 향상된 적응 성능과 일반화 능력을 더 잘 보존할 수 있게 한다. CLIP-SVD는 11개의 자연 및 10개의 생물의학 데이터셋에서 최첨단의 분류 결과를 달성하며, 적은 샷 설정에서 정확도와 일반화 면에서 이전 방법을 능가한다. 또한 CLIP-SVD의 효과와 역학을 분석하기 위해 자연어 기반 접근법을 활용하여 CLIP의 적응을 해석할 수 있다.

## 🎯 주요 포인트


- 1. CLIP-SVD는 prompt engineering에 의존하지 않고 새로운 세부 도메인에 적응하는 혁신적인 멀티모달 및 매개변수 효율적인 적응 기술이다.

- 2. CLIP-SVD는 CLIP의 내부 매개변수 공간을 수정하기 위해 SVD를 활용하며 추가 모듈을 주입하지 않는다.

- 3. CLIP-SVD는 적은 수의 파라미터만 사용하여 모델의 일반화 능력을 더 잘 보존하면서 다양한 데이터셋에서 최고 수준의 분류 결과를 달성한다.


---

*Generated on 2025-09-18 16:58:10*