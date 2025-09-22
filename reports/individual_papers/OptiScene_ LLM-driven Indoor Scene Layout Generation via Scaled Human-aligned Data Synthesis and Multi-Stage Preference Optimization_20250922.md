# OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization

**Korean Title:** OptiScene: 확장된 인간 정렬 데이터 합성과 다단계 선호 최적화를 통한 LLM 기반 실내 장면 레이아웃 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Supervised Fine-tuning, Direct Preference Optimization

## 🔗 유사한 논문
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN Layout-guided 3D Indoor Scene Generation]] (90.2% similar)
- [[2025-09-22/Causal Reasoning Elicits Controllable 3D Scene Generation_20250922|Causal Reasoning Elicits Controllable 3D Scene Generation]] (81.8% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos Structured Prompts Meet Simulation Data]] (80.9% similar)
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (80.0% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.07570v2 Announce Type: replace-cross 
Abstract: Automatic indoor layout generation has attracted increasing attention due to its potential in interior design, virtual environment construction, and embodied AI. Existing methods fall into two categories: prompt-driven approaches that leverage proprietary LLM services (e.g., GPT APIs) and learning-based methods trained on layout data upon diffusion-based models. Prompt-driven methods often suffer from spatial inconsistency and high computational costs, while learning-based methods are typically constrained by coarse relational graphs and limited datasets, restricting their generalization to diverse room categories. In this paper, we revisit LLM-based indoor layout generation and present 3D-SynthPlace, a large-scale dataset that combines synthetic layouts generated via a 'GPT synthesize, Human inspect' pipeline, upgraded from the 3D-Front dataset. 3D-SynthPlace contains nearly 17,000 scenes, covering four common room types -- bedroom, living room, kitchen, and bathroom -- enriched with diverse objects and high-level spatial annotations. We further introduce OptiScene, a strong open-source LLM optimized for indoor layout generation, fine-tuned based on our 3D-SynthPlace dataset through our two-stage training. For the warum-up stage I, we adopt supervised fine-tuning (SFT), which is taught to first generate high-level spatial descriptions then conditionally predict concrete object placements. For the reinforcing stage II, to better align the generated layouts with human design preferences, we apply multi-turn direct preference optimization (DPO), which significantly improving layout quality and generation success rates. Extensive experiments demonstrate that OptiScene outperforms traditional prompt-driven and learning-based baselines. Moreover, OptiScene shows promising potential in interactive tasks such as scene editing and robot navigation.

## 🔍 Abstract (한글 번역)

arXiv:2506.07570v2 발표 유형: 교차 교체  
초록: 자동 실내 레이아웃 생성은 인테리어 디자인, 가상 환경 구축 및 구현된 AI 분야에서의 잠재력으로 인해 점점 더 많은 주목을 받고 있습니다. 기존 방법은 두 가지 범주로 나뉩니다: 독점적인 LLM 서비스를 활용하는 프롬프트 기반 접근법(예: GPT API)과 확산 기반 모델을 통해 레이아웃 데이터를 학습한 학습 기반 방법. 프롬프트 기반 방법은 종종 공간적 불일치와 높은 계산 비용의 문제를 겪는 반면, 학습 기반 방법은 일반적으로 거친 관계 그래프와 제한된 데이터셋에 의해 제약을 받아 다양한 방 종류에 대한 일반화가 제한됩니다. 본 논문에서는 LLM 기반 실내 레이아웃 생성을 재검토하고, 'GPT 합성, 인간 검사' 파이프라인을 통해 생성된 합성 레이아웃을 결합한 대규모 데이터셋인 3D-SynthPlace를 소개합니다. 이는 3D-Front 데이터셋에서 업그레이드된 것입니다. 3D-SynthPlace는 침실, 거실, 주방, 욕실 등 네 가지 일반적인 방 유형을 포함하여 거의 17,000개의 장면을 포함하고 있으며, 다양한 객체와 고수준의 공간 주석으로 풍부하게 구성되어 있습니다. 우리는 또한 실내 레이아웃 생성을 위해 최적화된 강력한 오픈 소스 LLM인 OptiScene을 소개하며, 3D-SynthPlace 데이터셋을 기반으로 한 2단계 훈련을 통해 미세 조정되었습니다. 초기 단계 I에서는 감독된 미세 조정(SFT)을 채택하여 먼저 고수준의 공간 설명을 생성한 후 조건부로 구체적인 객체 배치를 예측하도록 학습합니다. 강화 단계 II에서는 생성된 레이아웃을 인간의 디자인 선호도에 더 잘 맞추기 위해 다중 회차 직접 선호 최적화(DPO)를 적용하여 레이아웃 품질과 생성 성공률을 크게 향상시킵니다. 광범위한 실험을 통해 OptiScene이 전통적인 프롬프트 기반 및 학습 기반 기준을 능가함을 입증합니다. 또한, OptiScene은 장면 편집 및 로봇 내비게이션과 같은 상호작용 작업에서 유망한 잠재력을 보여줍니다.

## 📝 요약

이 논문은 실내 레이아웃 자동 생성에 관한 연구로, 기존 방법론의 한계를 극복하기 위해 3D-SynthPlace라는 대규모 데이터셋을 소개합니다. 이 데이터셋은 'GPT 생성, 인간 검사' 파이프라인을 통해 생성된 17,000여 개의 장면을 포함하며, 침실, 거실, 주방, 욕실 등 다양한 방 유형을 다룹니다. 또한, OptiScene이라는 강력한 오픈 소스 LLM을 제안하여, 3D-SynthPlace 데이터셋을 기반으로 두 단계의 훈련을 통해 실내 레이아웃 생성에 최적화했습니다. 첫 번째 단계에서는 감독된 미세 조정을 통해 공간 설명과 객체 배치를 생성하고, 두 번째 단계에서는 다중 회차 직접 선호 최적화를 통해 인간의 디자인 선호도에 맞춘 레이아웃을 생성합니다. 실험 결과, OptiScene은 기존 방법들보다 우수한 성능을 보였으며, 장면 편집 및 로봇 내비게이션과 같은 상호작용 작업에서도 유망한 가능성을 보여줍니다.

## 🎯 주요 포인트

- 1. 자동 실내 레이아웃 생성은 인테리어 디자인, 가상 환경 구축, 구현된 AI 분야에서 주목받고 있다.

- 2. 기존 방법은 LLM 서비스 기반의 프롬프트 주도 접근법과 확산 기반 모델로 훈련된 학습 기반 방법으로 나뉜다.

- 3. 3D-SynthPlace는 'GPT 생성, 인간 검사' 파이프라인을 통해 생성된 17,000개의 장면을 포함한 대규모 합성 레이아웃 데이터셋이다.

- 4. OptiScene은 3D-SynthPlace 데이터셋을 기반으로 실내 레이아웃 생성을 최적화한 강력한 오픈소스 LLM이다.

- 5. OptiScene은 장면 편집 및 로봇 내비게이션과 같은 상호작용 작업에서 유망한 잠재력을 보여준다.

---

*Generated on 2025-09-22 14:54:45*