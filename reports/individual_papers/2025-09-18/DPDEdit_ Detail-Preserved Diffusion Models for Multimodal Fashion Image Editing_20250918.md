
# DPDEdit: Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing

**Korean Title:** DPDEdit: 다중 모달 패션 이미지 편집을 위한 세부사항 보존 확산 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multimodal Fashion Image Editing

## 🔗 유사한 논문
- [[EdiVal-Agent An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing]] (80.6% similar)
- [[DiffHash Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (79.2% similar)
- [[FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (79.0% similar)
- [[Locally_Explaining_Prediction_Behavior_via_Gradual_Interventions_and_Measuring_Property_Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (78.8% similar)
- [[CraftMesh High-Fidelity Generative Mesh Manipulation via Poisson Seamless Fusion]] (78.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.01086v3 Announce Type: replace-cross 
Abstract: Fashion image editing is a crucial tool for designers to convey their creative ideas by visualizing design concepts interactively. Current fashion image editing techniques, though advanced with multimodal prompts and powerful diffusion models, often struggle to accurately identify editing regions and preserve the desired garment texture detail. To address these challenges, we introduce a new multimodal fashion image editing architecture based on latent diffusion models, called Detail-Preserved Diffusion Models (DPDEdit). DPDEdit guides the fashion image generation of diffusion models by integrating text prompts, region masks, human pose images, and garment texture images. To precisely locate the editing region, we first introduce Grounded-SAM to predict the editing region based on the user's textual description, and then combine it with other conditions to perform local editing. To transfer the detail of the given garment texture into the target fashion image, we propose a texture injection and refinement mechanism. Specifically, this mechanism employs a decoupled cross-attention layer to integrate textual descriptions and texture images, and incorporates an auxiliary U-Net to preserve the high-frequency details of generated garment texture. Additionally, we extend the VITON-HD dataset using a multimodal large language model to generate paired samples with texture images and textual descriptions. Extensive experiments show that our DPDEdit outperforms state-of-the-art methods in terms of image fidelity and coherence with the given multimodal inputs.

## 🔍 Abstract (한글 번역)

arXiv:2409.01086v3 공지 유형: replace-cross
초록: 패션 이미지 편집은 디자이너가 디자인 컨셉을 상호작용적으로 시각화하여 창의적 아이디어를 전달하는 데 중요한 도구이다. 현재의 패션 이미지 편집 기법들은 멀티모달 프롬프트와 강력한 확산 모델을 사용하여 발전되었음에도 불구하고, 편집 영역을 정확히 식별하고 원하는 의복 텍스처 세부사항을 보존하는 데 어려움을 겪는 경우가 많다. 이러한 과제들을 해결하기 위해, 우리는 잠재 확산 모델을 기반으로 한 새로운 멀티모달 패션 이미지 편집 아키텍처인 Detail-Preserved Diffusion Models (DPDEdit)을 제안한다. DPDEdit은 텍스트 프롬프트, 영역 마스크, 인간 포즈 이미지, 그리고 의복 텍스처 이미지를 통합하여 확산 모델의 패션 이미지 생성을 가이드한다. 편집 영역을 정확히 위치시키기 위해, 우리는 먼저 사용자의 텍스트 설명을 바탕으로 편집 영역을 예측하는 Grounded-SAM을 도입하고, 이를 다른 조건들과 결합하여 국소 편집을 수행한다. 주어진 의복 텍스처의 세부사항을 목표 패션 이미지로 전이하기 위해, 우리는 텍스처 주입 및 정제 메커니즘을 제안한다. 구체적으로, 이 메커니즘은 텍스트 설명과 텍스처 이미지를 통합하기 위해 분리된 교차 주의 계층을 사용하고, 생성된 의복 텍스처의 고주파 세부사항을 보존하기 위해 보조 U-Net을 통합한다. 또한, 우리는 멀티모달 대형 언어 모델을 사용하여 텍스처 이미지와 텍스트 설명이 쌍을 이루는 샘플을 생성함으로써 VITON-HD 데이터셋을 확장하였다. 광범위한 실험을 통해 우리의 DPDEdit이 주어진 멀티모달 입력과의 이미지 충실도 및 일관성 측면에서 최신 기법들을 능가함을 보여준다.

## 📝 요약

이 논문은 패션 이미지 편집의 정확성을 높이기 위해 새로운 멀티모달 패션 이미지 편집 아키텍처인 DPDEdit를 제안합니다. 기존 기술들이 편집 영역 식별과 의류 질감 세부사항 보존에서 어려움을 겪는 문제를 해결하고자, DPDEdit는 잠재 확산 모델을 기반으로 텍스트 프롬프트, 영역 마스크, 인체 포즈 이미지, 의류 질감 이미지를 통합하여 패션 이미지 생성을 안내합니다. 사용자의 텍스트 설명을 기반으로 편집 영역을 예측하는 Grounded-SAM을 도입하고, 텍스처 주입 및 정제 메커니즘을 통해 의류 질감을 목표 이미지에 정확히 전달합니다. 또한, VITON-HD 데이터셋을 확장하여 텍스처 이미지와 텍스트 설명이 포함된 샘플을 생성합니다. 실험 결과, DPDEdit는 이미지 충실도와 멀티모달 입력과의 일관성 측면에서 기존 방법들보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. DPDEdit는 잠재 확산 모델을 기반으로 한 새로운 다중 모달 패션 이미지 편집 아키텍처로, 텍스트 프롬프트, 영역 마스크, 인간 포즈 이미지, 의류 텍스처 이미지를 통합하여 패션 이미지 생성을 안내합니다.

- 2. Grounded-SAM을 도입하여 사용자의 텍스트 설명에 기반한 편집 영역을 예측하고, 이를 다른 조건과 결합하여 지역 편집을 수행합니다.

- 3. 주어진 의류 텍스처의 세부 사항을 목표 패션 이미지로 전송하기 위해 텍스처 주입 및 정제 메커니즘을 제안하며, 이는 텍스트 설명과 텍스처 이미지를 통합하는 분리된 교차 주의 레이어를 사용합니다.

- 4. VITON-HD 데이터셋을 확장하여 텍스처 이미지 및 텍스트 설명과 함께 페어링된 샘플을 생성하는 다중 모달 대형 언어 모델을 사용합니다.

- 5. DPDEdit는 이미지 충실도와 주어진 다중 모달 입력과의 일관성 측면에서 최첨단 방법들보다 우수한 성능을 보입니다.

---

*Generated on 2025-09-19 10:58:54*