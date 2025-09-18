
# FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph

**Korean Title:** FSR-VLN: 계층적 다중 모달 씬 그래프를 활용한 시각-언어 내비게이션을 위한 빠른 및 느린 추론

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-modal Map Representation|Multi-modal Map Representation]] [[keywords/broad/Vision-Language Navigation|Vision-Language Navigation]] [[keywords/broad/Hierarchical Multi-modal Scene Graph|Hierarchical Multi-modal Scene Graph]] [[keywords/specific/Fast-to-Slow Navigation Reasoning|Fast-to-Slow Navigation Reasoning]] [[keywords/unique/FSR-VLN|FSR-VLN]] [[categories/cs.RO|cs.RO]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-modal map representation
**🔬 Broad Technical**: Vision-Language Navigation, Hierarchical Multi-modal Scene Graph
**🔗 Specific Connectable**: Fast-to-Slow Navigation Reasoning
**⭐ Unique Technical**: FSR-VLN

**ArXiv ID**: [2509.13733](https://arxiv.org/abs/2509.13733)
**Published**: 2025-09-18
**Category**: cs.RO
**PDF**: [Download](https://arxiv.org/pdf/2509.13733.pdf)


## 🏷️ 추출된 키워드



`Vision-Language Navigation` • 

`Hierarchical Multi-modal Scene Graph` • 

`Fast-to-Slow Navigation Reasoning` • 

`FSR-VLN` • 

`Multi-modal map representation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13733v1 Announce Type: new 
Abstract: Visual-Language Navigation (VLN) is a fundamental challenge in robotic systems, with broad applications for the deployment of embodied agents in real-world environments. Despite recent advances, existing approaches are limited in long-range spatial reasoning, often exhibiting low success rates and high inference latency, particularly in long-range navigation tasks. To address these limitations, we propose FSR-VLN, a vision-language navigation system that combines a Hierarchical Multi-modal Scene Graph (HMSG) with Fast-to-Slow Navigation Reasoning (FSR). The HMSG provides a multi-modal map representation supporting progressive retrieval, from coarse room-level localization to fine-grained goal view and object identification. Building on HMSG, FSR first performs fast matching to efficiently select candidate rooms, views, and objects, then applies VLM-driven refinement for final goal selection. We evaluated FSR-VLN across four comprehensive indoor datasets collected by humanoid robots, utilizing 87 instructions that encompass a diverse range of object categories. FSR-VLN achieves state-of-the-art (SOTA) performance in all datasets, measured by the retrieval success rate (RSR), while reducing the response time by 82% compared to VLM-based methods on tour videos by activating slow reasoning only when fast intuition fails. Furthermore, we integrate FSR-VLN with speech interaction, planning, and control modules on a Unitree-G1 humanoid robot, enabling natural language interaction and real-time navigation.

## 🔍 Abstract (한글 번역)

arXiv:2509.13733v1 발표 유형: 새로운
요약: 시각-언어 내비게이션(VLN)은 로봇 시스템에서의 기본적인 도전 과제로, 현실 세계 환경에서의 태체 에이전트 배치에 대한 다양한 응용 프로그램을 가지고 있습니다. 최근의 발전에도 불구하고, 기존의 방법론은 장거리 공간 추론에서 제한되어 있으며 종종 낮은 성공률과 높은 추론 대기 시간을 나타내며 특히 장거리 내비게이션 작업에서 그러한 한계가 드러납니다. 이러한 한계를 해결하기 위해, 우리는 HMSG(Hierarchical Multi-modal Scene Graph)와 FSR(Fast-to-Slow Navigation Reasoning)를 결합한 비전-언어 내비게이션 시스템인 FSR-VLN을 제안합니다. HMSG는 계층적 다중 모달 씬 그래프를 제공하여, 굵은 방 수준의 로컬라이제이션부터 세밀한 목표 시점 및 객체 식별까지 점진적 검색을 지원합니다. HMSG를 기반으로, FSR은 먼저 빠른 매칭을 수행하여 후보 방, 시점 및 객체를 효율적으로 선택한 후, 최종 목표 선택을 위해 VLM 기반 세밀화를 적용합니다. 우리는 인간형 로봇에 의해 수집된 네 가지 포괄적인 실내 데이터셋을 활용하여 87개의 명령을 포함한 다양한 객체 범주를 포함하는 FSR-VLN을 평가했습니다. FSR-VLN은 모든 데이터셋에서 검색 성공률(RSR)을 기준으로 최신 기술 성능을 달성하며, 빠른 직관이 실패할 때에만 느린 추론을 활성화하여 VLM 기반 방법에 비해 응답 시간을 82% 줄였습니다. 더 나아가, 우리는 FSR-VLN을 Unitree-G1 인간형 로봇에 음성 상호 작용, 계획 및 제어 모듈과 통합하여 자연어 상호 작용 및 실시간 내비게이션을 가능하게 했습니다.

## 📝 요약

로봇 시스템에서의 시각-언어 내비게이션(VLN)은 현실 세계 환경에서 탑재된 에이전트의 배치에 넓은 응용 가능성을 가진 기본적인 도전 과제이다. 기존 방법론은 장거리 공간 추론에 제한이 있어서 장거리 내비게이션 작업에서 낮은 성공률과 높은 추론 대기 시간을 보인다. 이러한 한계를 극복하기 위해 HMSG와 FSR을 결합한 FSR-VLN을 제안한다. HMSG는 다양한 공간 그래프 표현을 제공하며, FSR은 빠른 매칭을 통해 후보 공간을 효율적으로 선택한 후 VLM 기반 세부 목표 선택을 수행한다. FSR-VLN은 인간형 로봇에 의해 수집된 네 가지 종합 실내 데이터셋에서 SOTA 성능을 달성하고, 응답 시간을 82% 줄이면서 자연어 상호작용과 실시간 내비게이션을 가능하게 한다.

## 🎯 주요 포인트


- 시각-언어 내비게이션은 로봇 시스템에서의 기본적인 도전 과제이며, 실제 환경에서 탑재된 에이전트의 넓은 응용 가능성을 갖고 있다.

- FSR-VLN은 HMSG와 FSR을 결합한 시각-언어 내비게이션 시스템으로, 장거리 공간 추론에 제한이 있는 기존 방법을 극복한다.

- FSR-VLN은 모든 데이터셋에서 SOTA 성능을 달성하며, 응답 시간을 82% 줄이고 자연어 상호작용 및 실시간 내비게이션을 가능하게 한다.


---

*Generated on 2025-09-18 17:15:15*