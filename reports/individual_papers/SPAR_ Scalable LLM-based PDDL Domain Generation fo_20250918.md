
# SPAR: Scalable LLM-based PDDL Domain Generation for Aerial Robotics

**Korean Title:** SPAR: 비행로봇을 위한 확장 가능한 LLM 기반 PDDL 도메인 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Natural Language Input|Natural Language Input]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/PDDL|PDDL]] [[keywords/specific/UAV Planning|UAV Planning]] [[keywords/unique/SPAR|SPAR]] [[categories/cs.RO|cs.RO]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Natural Language Input
**🔬 Broad Technical**: Large Language Models, PDDL
**🔗 Specific Connectable**: UAV Planning
**⭐ Unique Technical**: SPAR

**ArXiv ID**: [2509.13691](https://arxiv.org/abs/2509.13691)
**Published**: 2025-09-18
**Category**: cs.RO
**PDF**: [Download](https://arxiv.org/pdf/2509.13691.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Planning Domain Definition Language` • 

`UAV planning dataset` • 

`SPAR` • 

`Generative capabilities of LLMs`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13691v1 Announce Type: new 
Abstract: We investigate the problem of automatic domain generation for the Planning Domain Definition Language (PDDL) using Large Language Models (LLMs), with a particular focus on unmanned aerial vehicle (UAV) tasks. Although PDDL is a widely adopted standard in robotic planning, manually designing domains for diverse applications such as surveillance, delivery, and inspection is labor-intensive and error-prone, which hinders adoption and real-world deployment. To address these challenges, we propose SPAR, a framework that leverages the generative capabilities of LLMs to automatically produce valid, diverse, and semantically accurate PDDL domains from natural language input. To this end, we first introduce a systematically formulated and validated UAV planning dataset, consisting of ground-truth PDDL domains and associated problems, each paired with detailed domain and action descriptions. Building on this dataset, we design a prompting framework that generates high-quality PDDL domains from language input. The generated domains are evaluated through syntax validation, executability, feasibility, and interpretability. Overall, this work demonstrates that LLMs can substantially accelerate the creation of complex planning domains, providing a reproducible dataset and evaluation pipeline that enables application experts without prior experience to leverage it for practical tasks and advance future research in aerial robotics and automated planning.

## 🔍 Abstract (한글 번역)

arXiv:2509.13691v1 발표 유형: 새로운
요약: 우리는 대규모 언어 모델 (LLM)을 사용하여 계획 도메인 정의 언어 (PDDL)의 자동 도메인 생성 문제를 연구하였으며, 특히 무인 항공기 (UAV) 작업에 초점을 맞추었습니다. PDDL은 로봇 계획에서 널리 사용되는 표준이지만 감시, 배송 및 검사와 같은 다양한 응용 프로그램을 위해 도메인을 수동으로 설계하는 것은 노동 집약적이고 오류가 발생하기 쉬워 채택과 실제 세계 배치를 방해합니다. 이러한 도전에 대처하기 위해 우리는 SPAR이라는 프레임워크를 제안합니다. 이 프레임워크는 LLM의 생성 능력을 활용하여 자연어 입력에서 유효하고 다양하며 의미론적으로 정확한 PDDL 도메인을 자동으로 생성합니다. 이를 위해 먼저 체계적으로 고안되고 검증된 UAV 계획 데이터 세트를 소개합니다. 이 데이터 세트는 지면 진실 PDDL 도메인과 관련된 문제로 구성되어 있으며 각각 상세한 도메인 및 작업 설명과 함께 제공됩니다. 이 데이터 세트를 기반으로 언어 입력에서 고품질 PDDL 도메인을 생성하는 프롬프팅 프레임워크를 설계합니다. 생성된 도메인은 구문 유효성, 실행 가능성, 실현 가능성 및 해석 가능성을 통해 평가됩니다. 전반적으로, 이 작업은 LLM이 복잡한 계획 도메인의 생성을 크게 가속화할 수 있음을 보여주며, 이를 통해 응용 전문가들이 실용적인 작업에 활용하고 항공 로봇 및 자동화된 계획 분야의 미래 연구를 진전시킬 수 있는 재현 가능한 데이터 세트와 평가 파이프라인을 제공합니다.

## 📝 요약

이 연구는 대규모 언어 모델(Large Language Models, LLMs)을 활용하여 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)의 자동 도메인 생성 문제를 연구하였다. 특히 무인 항공기(UAV) 작업에 초점을 맞추었으며, 수색, 배송, 검사 등 다양한 응용 분야에 대한 도메인을 수동으로 설계하는 것은 노동 집약적이고 오류가 발생하기 쉬워 채택과 현실 세계 배치를 방해한다. 이러한 도전에 대응하기 위해 LLMs의 생성 능력을 활용하여 자연어 입력으로부터 유효하고 다양하며 의미론적으로 정확한 PDDL 도메인을 자동으로 생성하는 SPAR 프레임워크를 제안하였다. 이를 위해 우선 UAV 계획 데이터셋을 소개하고, 이를 기반으로 언어 입력으로부터 고품질의 PDDL 도메인을 생성하는 프롬프팅 프레임워크를 설계하였다. 생성된 도메인은 구문 유효성, 실행 가능성, 실현 가능성 및 해석 가능성을 통해 평가되었으며, 본 연구는 LLMs가 복잡한 계획 도메인의 생성을 크게 가속화할 수 있음을 보여주었다.

## 🎯 주요 포인트


- PDDL을 위한 자동 도메인 생성 문제를 LLMs를 사용하여 연구

- SPAR 프레임워크를 제안하여 LLMs의 생성 능력을 활용하여 자동으로 유효하고 다양하며 의미론적으로 정확한 PDDL 도메인 생성

- UAV 계획 데이터셋을 소개하고 이를 기반으로 높은 품질의 PDDL 도메인 생성

- LLMs가 복잡한 계획 도메인 생성을 가속화하고 응용 전문가들이 실제 작업에 활용할 수 있도록 함.


---

*Generated on 2025-09-18 17:14:46*