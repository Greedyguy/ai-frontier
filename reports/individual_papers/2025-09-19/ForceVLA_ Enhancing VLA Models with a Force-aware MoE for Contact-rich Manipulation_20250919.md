
# ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation

**Korean Title:** ForceVLA: 접촉이 많은 조작을 위한 힘 인식 MoE로 VLA 모델 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language-Action Models

## 🔗 유사한 논문
- [[CLAW A Vision-Language-Action Framework for Weight-Aware Robotic Grasping]] (86.0% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (85.4% similar)
- [[GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (85.3% similar)
- [[Manipulation Facing Threats Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (83.6% similar)
- [[V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (83.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22159v3 Announce Type: replace-cross 
Abstract: Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## 🔍 Abstract (한글 번역)

arXiv:2505.22159v3 발표 유형: 교체-교차  
초록: 비전-언어-행동(VLA) 모델은 사전 학습된 시각 및 언어 표현을 활용하여 범용 로봇 조작을 발전시켰습니다. 그러나 이러한 모델은 특히 시각적 가림이나 동적 불확실성 하에서 힘을 포함한 세밀한 제어가 필요한 접촉이 많은 작업에서 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 VLA 시스템 내에서 외부 힘 감지를 일급 모달리티로 취급하는 새로운 종단 간 조작 프레임워크인 ForceVLA를 제안합니다. ForceVLA는 FVLMoE라는 힘 인식 전문가 혼합(Mixture-of-Experts) 융합 모듈을 도입하여, 행동 디코딩 중에 사전 학습된 시각-언어 임베딩을 실시간 6축 힘 피드백과 동적으로 통합합니다. 이는 모달리티별 전문가 간의 문맥 인식 라우팅을 가능하게 하여 로봇이 미세한 접촉 역학에 적응할 수 있는 능력을 향상시킵니다. 우리는 또한 다섯 가지 접촉이 많은 조작 작업에 걸쳐 동기화된 시각, 고유 수용, 힘-토크 신호로 구성된 새로운 데이터셋 \textbf{ForceVLA-Data}를 소개합니다. ForceVLA는 강력한 pi_0 기반 기준선 대비 평균 작업 성공률을 23.2% 향상시켰으며, 플러그 삽입과 같은 작업에서 최대 80%의 성공률을 달성했습니다. 우리의 접근 방식은 섬세한 조작을 위한 다중 모달 통합의 중요성을 강조하며 물리적으로 지능적인 로봇 제어의 새로운 기준을 설정합니다. 코드와 데이터는 https://sites.google.com/view/forcevla2025에서 공개될 예정입니다.

## 📝 요약

Vision-Language-Action(VLA) 모델은 일반적인 로봇 조작에서 발전을 이루었지만, 시각적 가림이나 동적 불확실성 하에서의 정밀한 힘 제어가 필요한 접촉 중심 작업에서는 한계가 있습니다. 이를 해결하기 위해 ForceVLA라는 새로운 프레임워크를 제안합니다. ForceVLA는 외부 힘 감지를 VLA 시스템의 주요 모달리티로 취급하며, FVLMoE라는 힘 인식 전문가 혼합 모듈을 통해 사전 학습된 시각-언어 임베딩과 실시간 6축 힘 피드백을 통합합니다. 이를 통해 로봇은 미세한 접촉 역학에 적응할 수 있습니다. 또한, 다섯 가지 접촉 중심 작업에서의 동기화된 시각, 고유감각, 힘-토크 신호를 포함하는 ForceVLA-Data라는 새로운 데이터셋을 소개합니다. ForceVLA는 기존의 강력한 기준선 대비 평균 작업 성공률을 23.2% 향상시켰으며, 플러그 삽입과 같은 작업에서 최대 80%의 성공률을 달성했습니다. 이 접근법은 다중 모달 통합의 중요성을 강조하며, 물리적으로 지능적인 로봇 제어의 새로운 기준을 제시합니다. 코드와 데이터는 https://sites.google.com/view/forcevla2025에서 공개될 예정입니다.

## 🎯 주요 포인트

- 1. ForceVLA는 외부 힘 감지를 VLA 시스템의 주요 모달리티로 취급하여 세밀한 제어가 필요한 접촉이 많은 작업을 개선합니다.

- 2. FVLMoE는 사전 학습된 시각-언어 임베딩과 실시간 6축 힘 피드백을 통합하여 로봇의 적응성을 향상시킵니다.

- 3. ForceVLA-Data는 시각, 고유감각, 힘-토크 신호를 동기화한 새로운 데이터셋으로, 5가지 접촉이 많은 조작 작업을 포함합니다.

- 4. ForceVLA는 강력한 pi_0 기반의 기준선 대비 평균 작업 성공률을 23.2% 향상시킵니다.

- 5. 이 접근 방식은 다중 모달 통합의 중요성을 강조하며, 물리적으로 지능적인 로봇 제어의 새로운 기준을 설정합니다.

---

*Generated on 2025-09-19 16:21:11*