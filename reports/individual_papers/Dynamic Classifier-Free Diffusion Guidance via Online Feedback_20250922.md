# Dynamic Classifier-Free Diffusion Guidance via Online Feedback

**Korean Title:** 온라인 피드백을 통한 동적 분류기 비자유 확산 안내

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic CFG Scheduling

## 🔗 유사한 논문
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (81.2% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (81.0% similar)
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (80.9% similar)
- [[2025-09-22/DiffusionNFT_ Online Diffusion Reinforcement with Forward Process_20250922|DiffusionNFT Online Diffusion Reinforcement with Forward Process]] (80.4% similar)
- [[2025-09-22/Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification_20250922|Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification]] (80.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16131v1 Announce Type: new 
Abstract: Classifier-free guidance (CFG) is a cornerstone of text-to-image diffusion models, yet its effectiveness is limited by the use of static guidance scales. This "one-size-fits-all" approach fails to adapt to the diverse requirements of different prompts; moreover, prior solutions like gradient-based correction or fixed heuristic schedules introduce additional complexities and fail to generalize. In this work, we challeng this static paradigm by introducing a framework for dynamic CFG scheduling. Our method leverages online feedback from a suite of general-purpose and specialized small-scale latent-space evaluations, such as CLIP for alignment, a discriminator for fidelity and a human preference reward model, to assess generation quality at each step of the reverse diffusion process. Based on this feedback, we perform a greedy search to select the optimal CFG scale for each timestep, creating a unique guidance schedule tailored to every prompt and sample. We demonstrate the effectiveness of our approach on both small-scale models and the state-of-the-art Imagen 3, showing significant improvements in text alignment, visual quality, text rendering and numerical reasoning. Notably, when compared against the default Imagen 3 baseline, our method achieves up to 53.8% human preference win-rate for overall preference, a figure that increases up to to 55.5% on prompts targeting specific capabilities like text rendering. Our work establishes that the optimal guidance schedule is inherently dynamic and prompt-dependent, and provides an efficient and generalizable framework to achieve it.

## 🔍 Abstract (한글 번역)

arXiv:2509.16131v1 발표 유형: 신규  
초록: 분류기 없는 안내(Classifier-free guidance, CFG)는 텍스트-이미지 확산 모델의 핵심 요소이지만, 정적 안내 척도의 사용으로 인해 그 효과가 제한됩니다. 이러한 "일률적인" 접근 방식은 다양한 프롬프트의 요구 사항에 적응하지 못하며, 이전의 해결책인 그래디언트 기반 수정이나 고정된 휴리스틱 일정은 추가적인 복잡성을 초래하고 일반화에 실패합니다. 본 연구에서는 동적 CFG 스케줄링을 위한 프레임워크를 도입하여 이 정적 패러다임에 도전합니다. 우리의 방법은 CLIP을 통한 정렬, 충실도를 위한 판별기, 인간 선호 보상 모델과 같은 일반 목적 및 특수 목적의 소규모 잠재 공간 평가의 온라인 피드백을 활용하여 역확산 과정의 각 단계에서 생성 품질을 평가합니다. 이 피드백을 바탕으로, 우리는 탐욕적 검색을 수행하여 각 시간 단계에 대한 최적의 CFG 척도를 선택하고, 각 프롬프트와 샘플에 맞춘 고유한 안내 일정을 작성합니다. 우리는 소규모 모델과 최첨단 Imagen 3 모두에서 우리의 접근 방식의 효과를 입증하며, 텍스트 정렬, 시각적 품질, 텍스트 렌더링 및 수치적 추론에서 상당한 개선을 보여줍니다. 특히, 기본 Imagen 3 기준선과 비교했을 때, 우리의 방법은 전체 선호도에서 최대 53.8%의 인간 선호 승률을 달성하며, 텍스트 렌더링과 같은 특정 기능을 목표로 하는 프롬프트에서는 최대 55.5%까지 증가합니다. 우리의 연구는 최적의 안내 일정이 본질적으로 동적이며 프롬프트에 의존함을 입증하고, 이를 달성하기 위한 효율적이고 일반화 가능한 프레임워크를 제공합니다.

## 📝 요약

이 논문은 텍스트-이미지 변환 모델에서 사용되는 정적 분류기 없는 가이던스(CFG)의 한계를 극복하기 위해 동적 CFG 스케줄링 프레임워크를 제안합니다. 기존의 정적 가이던스 스케일은 다양한 프롬프트 요구사항에 적합하지 않으며, 이를 해결하기 위한 이전 방법들은 복잡성을 증가시키고 일반화에 실패했습니다. 제안된 방법은 CLIP, 판별기, 인간 선호 보상 모델 등 다양한 평가 도구를 활용하여 각 역확산 단계에서 생성 품질을 평가하고, 최적의 CFG 스케일을 선택하는 탐색 과정을 통해 프롬프트와 샘플에 맞춘 고유한 가이던스 스케줄을 생성합니다. 이 방법은 텍스트 정렬, 시각적 품질, 텍스트 렌더링 및 수치적 추론에서 큰 개선을 보여주며, 특히 특정 기능을 목표로 하는 프롬프트에서 최대 55.5%의 인간 선호율을 기록했습니다. 연구는 최적의 가이던스 스케줄이 동적이고 프롬프트에 의존적임을 입증하며, 이를 효율적으로 달성할 수 있는 일반화 가능한 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. 텍스트-이미지 변환 모델에서 정적 가이드 스케일의 한계를 극복하기 위해 동적 CFG 스케줄링 프레임워크를 제안합니다.

- 2. 제안된 방법은 CLIP, 판별기, 인간 선호 보상 모델 등 다양한 평가 도구를 활용하여 생성 품질을 실시간으로 평가합니다.

- 3. 각 시간 단계마다 최적의 CFG 스케일을 선택하여 프롬프트와 샘플에 맞춘 고유한 가이드 스케줄을 생성합니다.

- 4. 제안된 방법은 텍스트 정렬, 시각적 품질, 텍스트 렌더링 및 수치적 추론에서 유의미한 개선을 보여줍니다.

- 5. 인간 선호도 평가에서 기본 모델 대비 최대 55.5%의 승률을 기록하며, 프롬프트에 따라 최적의 가이드 스케줄이 동적이고 프롬프트에 의존적임을 입증합니다.

---

*Generated on 2025-09-22 15:33:11*