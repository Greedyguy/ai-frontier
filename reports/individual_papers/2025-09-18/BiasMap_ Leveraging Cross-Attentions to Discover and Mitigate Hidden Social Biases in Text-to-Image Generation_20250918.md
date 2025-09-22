
# BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation

**Korean Title:** BiasMap: 교차 어텐션을 활용한 텍스트-이미지 생성에서의 숨겨진 사회적 편향 발견 및 완화

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Energy-Guided Diffusion Sampling

## 🔗 유사한 논문
- [[Iterative_Prompt_Refinement_for_Safer_Text-to-Image_Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (79.9% similar)
- [[DiffHash Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (78.8% similar)
- [[Is GPT-4o mini Blinded by its Own Safety Filters_ Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection_20250918|Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection]] (78.7% similar)
- [[DiffGAN A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis]] (78.4% similar)
- [[Locally_Explaining_Prediction_Behavior_via_Gradual_Interventions_and_Measuring_Property_Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (78.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13496v1 Announce Type: cross 
Abstract: Bias discovery is critical for black-box generative models, especiall text-to-image (TTI) models. Existing works predominantly focus on output-level demographic distributions, which do not necessarily guarantee concept representations to be disentangled post-mitigation. We propose BiasMap, a model-agnostic framework for uncovering latent concept-level representational biases in stable diffusion models. BiasMap leverages cross-attention attribution maps to reveal structural entanglements between demographics (e.g., gender, race) and semantics (e.g., professions), going deeper into representational bias during the image generation. Using attribution maps of these concepts, we quantify the spatial demographics-semantics concept entanglement via Intersection over Union (IoU), offering a lens into bias that remains hidden in existing fairness discovery approaches. In addition, we further utilize BiasMap for bias mitigation through energy-guided diffusion sampling that directly modifies latent noise space and minimizes the expected SoftIoU during the denoising process. Our findings show that existing fairness interventions may reduce the output distributional gap but often fail to disentangle concept-level coupling, whereas our mitigation method can mitigate concept entanglement in image generation while complementing distributional bias mitigation.

## 🔍 Abstract (한글 번역)

arXiv:2509.13496v1 공지 유형: cross
초록: 편향 발견은 블랙박스 생성 모델, 특히 텍스트-이미지(TTI) 모델에 있어 매우 중요하다. 기존 연구들은 주로 출력 수준의 인구통계학적 분포에 초점을 맞추고 있으나, 이는 편향 완화 후 개념 표현의 분리를 반드시 보장하지 않는다. 본 연구에서는 안정적 확산 모델에서 잠재적 개념 수준의 표현적 편향을 발견하기 위한 모델 비종속적 프레임워크인 BiasMap을 제안한다. BiasMap은 교차 어텐션 귀인 맵을 활용하여 인구통계학적 특성(예: 성별, 인종)과 의미론적 특성(예: 직업) 간의 구조적 얽힘을 드러내며, 이미지 생성 과정에서 표현적 편향을 더욱 깊이 있게 탐구한다. 이러한 개념들의 귀인 맵을 사용하여, 우리는 교집합 대 합집합(IoU)을 통해 공간적 인구통계학-의미론 개념 얽힘을 정량화하며, 기존 공정성 발견 접근법에서 숨겨져 있던 편향을 들여다볼 수 있는 렌즈를 제공한다. 또한, 우리는 잠재 노이즈 공간을 직접 수정하고 디노이징 과정에서 예상 SoftIoU를 최소화하는 에너지 유도 확산 샘플링을 통해 편향 완화에 BiasMap을 더욱 활용한다. 우리의 연구 결과는 기존의 공정성 개입이 출력 분포적 격차를 줄일 수는 있지만 종종 개념 수준의 결합을 분리하는 데 실패하는 반면, 우리의 완화 방법은 분포적 편향 완화를 보완하면서 이미지 생성에서 개념 얽힘을 완화할 수 있음을 보여준다.

## 📝 요약

BiasMap은 텍스트-이미지 변환 모델에서 잠재적인 개념 수준의 표현 편향을 발견하기 위한 모델 비종속적 프레임워크입니다. 이 연구는 교차 주의 기법을 활용하여 인구통계학적 요소(예: 성별, 인종)와 의미적 요소(예: 직업) 간의 구조적 얽힘을 드러냅니다. 이를 통해 기존의 공정성 발견 접근법에서 숨겨진 편향을 탐색할 수 있습니다. BiasMap은 교차 주의 기법을 사용하여 개념 간의 공간적 얽힘을 IoU로 정량화하며, 에너지 기반 확산 샘플링을 통해 편향 완화도 수행합니다. 연구 결과, 기존의 공정성 개입은 출력 분포 격차를 줄일 수 있지만 개념 수준의 얽힘을 해결하지 못하는 반면, BiasMap은 이미지 생성 시 개념 얽힘을 완화하면서 분포 편향 완화도 보완할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. BiasMap은 안정적인 확산 모델에서 잠재적인 개념 수준의 표현 편향을 발견하기 위한 모델 비종속적 프레임워크입니다.

- 2. BiasMap은 교차 주의 기여 맵을 활용하여 인구통계학적 요소와 의미론적 요소 간의 구조적 얽힘을 드러냅니다.

- 3. 개념의 기여 맵을 사용하여 공간적 인구통계-의미론적 개념 얽힘을 IoU를 통해 정량화합니다.

- 4. BiasMap은 에너지 유도 확산 샘플링을 통해 편향 완화를 수행하여 개념 얽힘을 줄입니다.

- 5. 기존의 공정성 개입은 출력 분포 격차를 줄일 수 있지만, 개념 수준의 결합을 해소하지 못하는 경우가 많습니다.

---

*Generated on 2025-09-19 11:26:59*