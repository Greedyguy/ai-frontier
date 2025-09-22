# Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception

**Korean Title:** 인간과 유사한 적응적 시각을 모방하여 효율적이고 유연한 기계 시각 인식을 구현하기

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Vision

## 🔗 유사한 논문
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (82.4% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (82.1% similar)
- [[2025-09-19/Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (82.0% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (81.8% similar)
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (81.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15333v1 Announce Type: cross 
Abstract: Human vision is highly adaptive, efficiently sampling intricate environments by sequentially fixating on task-relevant regions. In contrast, prevailing machine vision models passively process entire scenes at once, resulting in excessive resource demands scaling with spatial-temporal input resolution and model size, yielding critical limitations impeding both future advancements and real-world application. Here we introduce AdaptiveNN, a general framework aiming to drive a paradigm shift from 'passive' to 'active, adaptive' vision models. AdaptiveNN formulates visual perception as a coarse-to-fine sequential decision-making process, progressively identifying and attending to regions pertinent to the task, incrementally combining information across fixations, and actively concluding observation when sufficient. We establish a theory integrating representation learning with self-rewarding reinforcement learning, enabling end-to-end training of the non-differentiable AdaptiveNN without additional supervision on fixation locations. We assess AdaptiveNN on 17 benchmarks spanning 9 tasks, including large-scale visual recognition, fine-grained discrimination, visual search, processing images from real driving and medical scenarios, language-driven embodied AI, and side-by-side comparisons with humans. AdaptiveNN achieves up to 28x inference cost reduction without sacrificing accuracy, flexibly adapts to varying task demands and resource budgets without retraining, and provides enhanced interpretability via its fixation patterns, demonstrating a promising avenue toward efficient, flexible, and interpretable computer vision. Furthermore, AdaptiveNN exhibits closely human-like perceptual behaviors in many cases, revealing its potential as a valuable tool for investigating visual cognition. Code is available at https://github.com/LeapLabTHU/AdaptiveNN.

## 🔍 Abstract (한글 번역)

arXiv:2509.15333v1 발표 유형: 교차  
초록: 인간의 시각은 매우 적응력이 뛰어나며, 복잡한 환경을 효율적으로 샘플링하여 순차적으로 과제와 관련된 영역에 주목합니다. 반면에, 기존의 기계 시각 모델은 전체 장면을 한 번에 수동적으로 처리하여, 공간-시간적 입력 해상도와 모델 크기에 따라 과도한 자원 요구를 초래하고, 이는 미래 발전과 실제 응용을 저해하는 중요한 한계를 초래합니다. 여기서 우리는 '수동적'에서 '능동적이고 적응적인' 시각 모델로의 패러다임 전환을 목표로 하는 일반적인 프레임워크인 AdaptiveNN을 소개합니다. AdaptiveNN은 시각적 인식을 거칠게부터 세밀하게 순차적인 의사결정 과정으로 공식화하여, 점차적으로 과제와 관련된 영역을 식별하고 주목하며, 고정점을 통해 정보를 점진적으로 결합하고, 충분할 때 능동적으로 관찰을 종료합니다. 우리는 표현 학습과 자기 보상 강화 학습을 통합하는 이론을 수립하여, 고정점 위치에 대한 추가 감독 없이 비분화 가능한 AdaptiveNN의 종단 간 학습을 가능하게 합니다. 우리는 대규모 시각 인식, 세밀한 차별, 시각적 검색, 실제 운전 및 의료 시나리오의 이미지 처리, 언어 기반의 구현된 AI, 인간과의 나란한 비교를 포함한 9개의 과제에 걸친 17개의 벤치마크에서 AdaptiveNN을 평가합니다. AdaptiveNN은 정확성을 희생하지 않고 최대 28배의 추론 비용 절감을 달성하며, 재훈련 없이 다양한 과제 요구와 자원 예산에 유연하게 적응하고, 고정 패턴을 통해 향상된 해석 가능성을 제공하여 효율적이고 유연하며 해석 가능한 컴퓨터 비전으로의 유망한 경로를 보여줍니다. 더욱이, AdaptiveNN은 많은 경우에서 인간과 유사한 지각 행동을 보여주어, 시각 인지를 조사하는 귀중한 도구로서의 잠재력을 드러냅니다. 코드는 https://github.com/LeapLabTHU/AdaptiveNN에서 사용할 수 있습니다.

## 📝 요약

AdaptiveNN은 인간의 시각적 인지 방식을 모방하여 '수동적'에서 '능동적, 적응적'인 비전 모델로의 전환을 목표로 하는 프레임워크입니다. 이 모델은 시각적 인식을 점진적인 의사 결정 과정으로 정의하여, 과제와 관련된 영역을 순차적으로 식별하고 주목하며, 충분한 정보가 수집되면 관찰을 종료합니다. 이를 위해 표현 학습과 자기 보상 강화 학습을 통합한 이론을 제시하여, 고정 위치에 대한 추가 감독 없이 비분화 가능한 AdaptiveNN의 종단 간 학습을 가능하게 합니다. 17개의 벤치마크에서 AdaptiveNN은 최대 28배의 추론 비용 절감을 이루면서도 정확성을 유지하며, 다양한 과제 요구와 자원 예산에 유연하게 적응합니다. 또한, 고정 패턴을 통해 해석 가능성을 높이며, 인간과 유사한 지각 행동을 보여 시각 인지 연구에 유용한 도구로서의 잠재력을 드러냅니다.

## 🎯 주요 포인트

- 1. AdaptiveNN은 '수동적'에서 '능동적, 적응적' 비전 모델로의 패러다임 전환을 목표로 하는 일반적인 프레임워크입니다.

- 2. AdaptiveNN은 시각적 인식을 점진적으로 중요한 영역을 식별하고 주목하는 순차적 의사결정 과정으로 공식화합니다.

- 3. AdaptiveNN은 17개의 벤치마크에서 최대 28배의 추론 비용 절감을 달성하면서도 정확도를 유지합니다.

- 4. AdaptiveNN은 다양한 작업 요구와 자원 예산에 유연하게 적응하며, 재훈련 없이도 적용 가능합니다.

- 5. AdaptiveNN은 인간과 유사한 지각 행동을 보여주며, 시각 인지 연구에 유용한 도구로서의 잠재력을 드러냅니다.

---

*Generated on 2025-09-22 13:53:35*