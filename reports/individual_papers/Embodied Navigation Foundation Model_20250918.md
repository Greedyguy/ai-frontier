
# Embodied Navigation Foundation Model

**Korean Title:** 구체화된 내비게이션 기반 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Cross-embodiment Navigation|Cross-embodiment Navigation]] [[keywords/broad/Vision-Language Models|Vision-Language Models]] [[keywords/broad/Embodied AI|Embodied AI]] [[keywords/specific/Multimodal Navigation|Multimodal Navigation]] [[keywords/unique/NavFoM|NavFoM]] [[categories/cs.RO|cs.RO]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-embodiment Navigation
**🔬 Broad Technical**: Vision-Language Models, Embodied AI
**🔗 Specific Connectable**: Multimodal Navigation
**⭐ Unique Technical**: NavFoM

**ArXiv ID**: [2509.12129](https://arxiv.org/abs/2509.12129)
**Published**: 2025-09-18
**Category**: cs.RO
**PDF**: [Download](https://arxiv.org/pdf/2509.12129.pdf)


## 🏷️ 추출된 키워드



`Vision-Language Models` • 

`Embodied AI` • 

`Multimodal Navigation` • 

`NavFoM` • 

`Cross-embodiment Navigation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12129v2 Announce Type: replace 
Abstract: Navigation is a fundamental capability in embodied AI, representing the intelligence required to perceive and interact within physical environments following language instructions. Despite significant progress in large Vision-Language Models (VLMs), which exhibit remarkable zero-shot performance on general vision-language tasks, their generalization ability in embodied navigation remains largely confined to narrow task settings and embodiment-specific architectures. In this work, we introduce a cross-embodiment and cross-task Navigation Foundation Model (NavFoM), trained on eight million navigation samples that encompass quadrupeds, drones, wheeled robots, and vehicles, and spanning diverse tasks such as vision-and-language navigation, object searching, target tracking, and autonomous driving. NavFoM employs a unified architecture that processes multimodal navigation inputs from varying camera configurations and navigation horizons. To accommodate diverse camera setups and temporal horizons, NavFoM incorporates identifier tokens that embed camera view information of embodiments and the temporal context of tasks. Furthermore, to meet the demands of real-world deployment, NavFoM controls all observation tokens using a dynamically adjusted sampling strategy under a limited token length budget. Extensive evaluations on public benchmarks demonstrate that our model achieves state-of-the-art or highly competitive performance across multiple navigation tasks and embodiments without requiring task-specific fine-tuning. Additional real-world experiments further confirm the strong generalization capability and practical applicability of our approach.

## 🔍 Abstract (한글 번역)

arXiv:2509.12129v2 발표 유형: 대체
요약: 내재된 AI에서의 탐색은 언어 지시를 따르며 물리적 환경 내에서 지각하고 상호 작용하는 데 필요한 지능을 나타냅니다. 대형 Vision-Language 모델(VLMs)에서 상당한 진전이 있었지만, 일반적인 비전-언어 작업에서 놀라운 제로샷 성능을 보이는 VLMs의 일반화 능력은 주로 좁은 작업 설정과 구체적인 구조에 한정되어 있습니다. 본 연구에서는 네 발, 드론, 바퀴 로봇 및 차량을 포함한 여덟 백만 개의 탐색 샘플에서 훈련된 교차 구현 및 교차 작업 네비게이션 기초 모델(NavFoM)을 소개합니다. 이 모델은 비전-언어 탐색, 물체 검색, 대상 추적 및 자율 주행과 같은 다양한 작업을 포괄하며, 다양한 카메라 구성과 탐색 지평을 처리하는 통합 아키텍처를 사용합니다. 다양한 카메라 설정과 시간적 지평을 수용하기 위해 NavFoM은 구현체의 카메라 보기 정보와 작업의 시간적 맥락을 포함하는 식별자 토큰을 통합합니다. 또한, 실제 세계 배치 요구를 충족시키기 위해 NavFoM은 제한된 토큰 길이 예산 하에서 모든 관측 토큰을 동적으로 조정된 샘플링 전략을 사용하여 제어합니다. 공개 벤치마크에서의 광범위한 평가 결과, 본 모델이 작업별 특정 세부 조정이 필요하지 않고 다양한 탐색 작업과 구현체에서 최첨단 또는 매우 경쟁력 있는 성능을 달성한다는 것을 보여줍니다. 추가적인 실제 세계 실험은 우리의 접근 방식의 강력한 일반화 능력과 실용적 적용 가능성을 확인합니다.

## 📝 요약

본 연구는 신체적 AI에서의 핵심 능력인 내비게이션에 초점을 맞추고 있습니다. 대규모 Vision-Language 모델(VLMs)의 발전에도 불구하고, 이러한 모델들의 내비게이션 일반화 능력은 좁은 과제 설정과 특정 구조에 제한되어 있습니다. 본 연구에서는 다양한 임무와 다양한 카메라 설정에서 학습된 크로스-임베디먼트 및 크로스-태스크 내비게이션 기반 모델(NavFoM)을 제안합니다. NavFoM은 다양한 카메라 구성과 내비게이션 시야에서의 다중 모달 내비게이션 입력을 처리하는 통합 아키텍처를 사용하며, 실제 배치 요구를 충족하기 위해 제한된 토큰 길이 예산 하에 모든 관측 토큰을 동적으로 조정된 샘플링 전략을 사용합니다. 공개 벤치마크에서의 폭넓은 평가 결과, 본 모델은 과제 특정 미세 조정이 필요 없이 다양한 내비게이션 작업과 임베디먼트에서 최첨단 또는 매우 경쟁력 있는 성능을 달성함을 보여줍니다. 추가적인 현실 세계 실험은 우리 방법의 강력한 일반화 능력과 실용적 적용 가능성을 확인합니다.

## 🎯 주요 포인트


- 1. 신경망 모델 NavFoM은 다양한 태스크와 태체에 대해 뛰어난 일반화 성능을 보여줌

- 2. NavFoM은 다양한 카메라 설정과 시간적 범위를 고려하여 통합 아키텍처를 사용함

- 3. 모델은 임베딩된 신원 정보 및 임무의 시간적 맥락을 고려하기 위해 식별자 토큰을 사용함.


---

*Generated on 2025-09-18 17:21:34*