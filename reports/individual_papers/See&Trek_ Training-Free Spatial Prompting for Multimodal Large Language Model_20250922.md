# See&Trek: Training-Free Spatial Prompting for Multimodal Large Language Model

**Korean Title:** See&Trek: 멀티모달 대형 언어 모델을 위한 훈련이 필요 없는 공간적 프롬프팅

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Training Free Prompting

## 🔗 유사한 논문
- [[2025-09-19/Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (83.0% similar)
- [[2025-09-22/SmolRGPT_ Efficient Spatial Reasoning for Warehouse Environments with 600M Parameters_20250922|SmolRGPT Efficient Spatial Reasoning for Warehouse Environments with 600M Parameters]] (82.7% similar)
- [[2025-09-17/ST-LINK_ Spatially-Aware Large Language Models for Spatio-Temporal Forecasting_20250917|ST-LINK Spatially-Aware Large Language Models for Spatio-Temporal Forecasting]] (82.6% similar)
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (82.1% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (81.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16087v1 Announce Type: cross 
Abstract: We introduce SEE&amp;TREK, the first training-free prompting framework tailored to enhance the spatial understanding of Multimodal Large Language Models (MLLMS) under vision-only constraints. While prior efforts have incorporated modalities like depth or point clouds to improve spatial reasoning, purely visualspatial understanding remains underexplored. SEE&amp;TREK addresses this gap by focusing on two core principles: increasing visual diversity and motion reconstruction. For visual diversity, we conduct Maximum Semantic Richness Sampling, which employs an off-the-shell perception model to extract semantically rich keyframes that capture scene structure. For motion reconstruction, we simulate visual trajectories and encode relative spatial positions into keyframes to preserve both spatial relations and temporal coherence. Our method is training&amp;GPU-free, requiring only a single forward pass, and can be seamlessly integrated into existing MLLM'S. Extensive experiments on the VSI-B ENCH and STI-B ENCH show that S EE &amp;T REK consistently boosts various MLLM S performance across diverse spatial reasoning tasks with the most +3.5% improvement, offering a promising path toward stronger spatial intelligence.

## 🔍 Abstract (한글 번역)

arXiv:2509.16087v1 발표 유형: 교차  
초록: 우리는 시각적 제약 조건 하에서 다중 모달 대형 언어 모델(Multimodal Large Language Models, MLLMs)의 공간 이해를 향상시키기 위해 설계된 최초의 훈련 불필요 프롬프트 프레임워크인 SEE&TREK을 소개합니다. 이전의 연구들은 깊이(depth)나 포인트 클라우드와 같은 모달리티를 포함하여 공간 추론을 개선하려고 했으나, 순수한 시각적 공간 이해는 여전히 충분히 탐구되지 않았습니다. SEE&TREK은 시각적 다양성 증가와 운동 재구성이라는 두 가지 핵심 원칙에 초점을 맞추어 이 격차를 해소합니다. 시각적 다양성을 위해, 우리는 장면 구조를 포착하는 의미적으로 풍부한 키프레임을 추출하기 위해 오프더쉘프 인식 모델을 사용하는 최대 의미 풍부성 샘플링을 수행합니다. 운동 재구성을 위해, 우리는 시각적 궤적을 시뮬레이션하고 상대적 공간 위치를 키프레임에 인코딩하여 공간적 관계와 시간적 일관성을 모두 유지합니다. 우리의 방법은 훈련 및 GPU가 필요 없으며, 단일 전방 패스만 요구되며 기존의 MLLM에 원활하게 통합될 수 있습니다. VSI-BENCH와 STI-BENCH에 대한 광범위한 실험 결과, SEE&TREK이 다양한 공간 추론 작업에서 여러 MLLM의 성능을 일관되게 향상시키며 최대 3.5%의 개선을 보여주어 강력한 공간 지능으로 가는 유망한 경로를 제공합니다.

## 📝 요약

SEE&TREK은 시각적 제약 하에서 다중모달 대형 언어 모델(MLLM)의 공간 이해를 향상시키기 위한 최초의 훈련 불필요 프롬프팅 프레임워크입니다. 기존 연구들이 깊이 정보나 포인트 클라우드를 활용한 공간 추론을 시도한 반면, 순수 시각적 공간 이해는 충분히 탐구되지 않았습니다. SEE&TREK은 시각적 다양성 증대와 운동 재구성이라는 두 가지 원칙에 중점을 둡니다. 시각적 다양성을 위해, 우리는 오프더셸 인식 모델을 사용하여 장면 구조를 포착하는 의미적으로 풍부한 키프레임을 추출합니다. 운동 재구성을 위해, 시각적 궤적을 시뮬레이션하고 상대적 공간 위치를 키프레임에 인코딩하여 공간 관계와 시간적 일관성을 유지합니다. 이 방법은 훈련 및 GPU가 필요 없으며, 기존 MLLM에 쉽게 통합될 수 있습니다. VSI-BENCH와 STI-BENCH에서의 광범위한 실험 결과, SEE&TREK은 다양한 공간 추론 작업에서 MLLM의 성능을 최대 3.5% 향상시킵니다.

## 🎯 주요 포인트

- 1. SEE&TREK은 시각적 제약 하에서 다중 모달 대형 언어 모델의 공간 이해를 향상시키기 위한 최초의 훈련 불필요 프롬팅 프레임워크입니다.

- 2. 이 프레임워크는 시각적 다양성 증가와 운동 재구성이라는 두 가지 핵심 원칙에 중점을 둡니다.

- 3. 시각적 다양성을 위해, 최대 의미적 풍부성 샘플링을 통해 장면 구조를 포착하는 의미적으로 풍부한 키프레임을 추출합니다.

- 4. 운동 재구성을 위해, 시각적 궤적을 시뮬레이션하고 키프레임에 상대적 공간 위치를 인코딩하여 공간 관계와 시간적 일관성을 유지합니다.

- 5. SEE&TREK은 훈련과 GPU가 필요 없으며, 다양한 공간 추론 작업에서 성능을 +3.5%까지 향상시킵니다.

---

*Generated on 2025-09-22 14:24:24*