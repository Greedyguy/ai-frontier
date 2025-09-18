
# Pareto-Grid-Guided Large Language Models for Fast and High-Quality Heuristics Design in Multi-Objective Combinatorial Optimization

**Korean Title:** 다중 목적 조합 최적화에서 빠르고 고품질 휴리스틱 디자인을 위한 파레토-그리드-가이드 대형 언어 모델 유지하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Heuristic Generation|Heuristic Generation]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Multi-objective Combinatorial Optimization|Multi-objective Combinatorial Optimization]] [[keywords/specific/Pareto Front Grid|Pareto Front Grid]] [[keywords/unique/MPaGE|MPaGE]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Heuristic Generation
**🔬 Broad Technical**: Large Language Models, Multi-objective Combinatorial Optimization
**🔗 Specific Connectable**: Pareto Front Grid
**⭐ Unique Technical**: MPaGE

**ArXiv ID**: [2507.20923](https://arxiv.org/abs/2507.20923)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2507.20923.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Multi-objective Combinatorial Optimization` • 

`Pareto Front Grid` • 

`MPaGE` • 

`Heuristic Generation`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.20923v2 Announce Type: replace-cross 
Abstract: Multi-objective combinatorial optimization problems (MOCOP) frequently arise in practical applications that require the simultaneous optimization of conflicting objectives. Although traditional evolutionary algorithms can be effective, they typically depend on domain knowledge and repeated parameter tuning, limiting flexibility when applied to unseen MOCOP instances. Recently, integration of Large Language Models (LLMs) into evolutionary computation has opened new avenues for automatic heuristic generation, using their advanced language understanding and code synthesis capabilities. Nevertheless, most existing approaches predominantly focus on single-objective tasks, often neglecting key considerations such as runtime efficiency and heuristic diversity in multi-objective settings. To bridge this gap, we introduce Multi-heuristics for MOCOP via Pareto-Grid-guided Evolution of LLMs (MPaGE), a novel enhancement of the Simple Evolutionary Multiobjective Optimization (SEMO) framework that leverages LLMs and Pareto Front Grid (PFG) technique. By partitioning the objective space into grids and retaining top-performing candidates to guide heuristic generation, MPaGE utilizes LLMs to prioritize heuristics with semantically distinct logical structures during variation, thus promoting diversity and mitigating redundancy within the population. Through extensive evaluations, MPaGE demonstrates superior performance over existing LLM-based frameworks, and achieves competitive results to traditional Multi-objective evolutionary algorithms (MOEAs), with significantly faster runtime. Our code is available at: https://github.com/langkhachhoha/MPaGE.

## 🔍 Abstract (한글 번역)

arXiv:2507.20923v2 발표 유형: replace-cross
초록: 다중 목적 조합 최적화 문제 (MOCOP)는 상충하는 목표를 동시에 최적화해야 하는 실제 응용 프로그램에서 자주 발생합니다. 전통적인 진화 알고리즘은 효과적일 수 있지만, 일반적으로 도메인 지식과 반복적인 매개변수 조정에 의존하기 때문에 보이지 않는 MOCOP 인스턴스에 적용할 때 유연성이 제한됩니다. 최근에는 대형 언어 모델 (LLM)을 진화 계산에 통합하여 고급 언어 이해 및 코드 합성 능력을 활용하여 자동 휴리스틱 생성을 위한 새로운 길을 열었습니다. 그러나 대부분의 기존 접근 방식은 주로 단일 목적 작업에 초점을 맞추고 있으며 종종 실행 시간 효율성 및 다양성과 같은 중요한 고려 사항을 무시합니다. 이 간극을 메우기 위해, 우리는 Pareto-Grid-지도 진화를 통한 MOCOP을 위한 다중 휴리스틱 (MPaGE)를 소개합니다. 이는 LLM 및 Pareto Front Grid (PFG) 기술을 활용한 Simple Evolutionary Multiobjective Optimization (SEMO) 프레임워크의 혁신적인 개선입니다. 목적 공간을 그리드로 분할하고 성능이 우수한 후보를 유지하여 휴리스틱 생성을 안내함으로써, MPaGE는 LLM을 활용하여 변이 중에 의미론적으로 다른 논리 구조를 가진 휴리스틱을 우선시하므로, 다양성을 촉진하고 모집단 내의 중복을 줄입니다. 광범위한 평가를 통해, MPaGE는 기존 LLM 기반 프레임워크보다 우수한 성능을 보여주며, 전통적인 다중 목적 진화 알고리즘 (MOEA)과 경쟁력 있는 결과를 달성하면서 실행 시간이 훨씬 빠릅니다. 우리의 코드는 다음에서 사용할 수 있습니다: https://github.com/langkhachhoha/MPaGE.

## 📝 요약

최근에는 대규모 언어 모델(Large Language Models, LLMs)을 진화 계산에 통합하여 자동 휴리스틱 생성을 가능케 하는 새로운 방법이 제안되었다. 그러나 기존 접근 방식은 주로 단일 목적 작업에 초점을 맞추어 왔고, 다목적 설정에서의 실행 효율성과 휴리스틱 다양성을 무시하는 경우가 많다. 본 논문에서는 Multi-heuristics for MOCOP via Pareto-Grid-guided Evolution of LLMs (MPaGE)를 소개한다. MPaGE는 LLMs와 Pareto Front Grid (PFG) 기술을 활용한 Simple Evolutionary Multiobjective Optimization (SEMO) 프레임워크의 혁신적인 개선이다. MPaGE는 목적 공간을 그리드로 분할하고 세미안테적으로 다른 논리 구조를 가진 휴리스틱을 우선적으로 선택하여 다양성을 촉진하고 인구 내의 중복을 줄이는 데 LLMs를 활용한다. MPaGE는 기존 LLM 기반 프레임워크보다 우수한 성능을 보이며, 전통적인 다목적 진화 알고리즘(MOEAs)과 경쟁력 있는 결과를 달성하면서 실행 시간도 크게 단축시킨다.

## 🎯 주요 포인트


- 1. 다중 목적 조합 최적화 문제(MOCOP)에 대한 새로운 해법 MPaGE 소개

- 2. Large Language Models (LLMs)와 Pareto Front Grid (PFG) 기술을 활용한 MPaGE의 우수한 성능

- 3. MPaGE는 다양성을 증진시키고 인구 내 중복을 완화시키는데 효과적

- 4. 기존 LLM 기반 프레임워크보다 우수한 성능을 보이며 빠른 실행 시간을 달성함.


---

*Generated on 2025-09-18 16:33:57*