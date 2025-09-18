
# Crash Report Enhancement with Large Language Models: An Empirical Study

**Korean Title:** 대형 언어 모델을 활용한 충돌 보고서 향상: 경험적 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Vision-Language Pre-training|Vision-Language Pre-training]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Stack-trace context|Stack-trace context]] [[keywords/specific/CodeBLEU|CodeBLEU]] [[keywords/unique/Agentic-LLM|Agentic-LLM]] [[categories/cs.SE|cs.SE]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: User study
**🔬 Broad Technical**: Large Language Models, Stack-trace context
**🔗 Specific Connectable**: Iterative approach
**⭐ Unique Technical**: Agentic-LLM

**ArXiv ID**: [2509.13535](https://arxiv.org/abs/2509.13535)
**Published**: 2025-09-18
**Category**: cs.SE
**PDF**: [Download](https://arxiv.org/pdf/2509.13535.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`Fault Localization` • 

`Stack-trace Context` • 

`Agentic-LLM` • 

`Iterative Approach`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13535v1 Announce Type: new 
Abstract: Crash reports are central to software maintenance, yet many lack the diagnostic detail developers need to debug efficiently. We examine whether large language models can enhance crash reports by adding fault locations, root-cause explanations, and repair suggestions. We study two enhancement strategies: Direct-LLM, a single-shot approach that uses stack-trace context, and Agentic-LLM, an iterative approach that explores the repository for additional evidence. On a dataset of 492 real-world crash reports, LLM-enhanced reports improve Top-1 problem-localization accuracy from 10.6% (original reports) to 40.2-43.1%, and produce suggested fixes that closely resemble developer patches (CodeBLEU around 56-57%). Both our manual evaluations and LLM-as-a-judge assessment show that Agentic-LLM delivers stronger root-cause explanations and more actionable repair guidance. A user study with 16 participants further confirms that enhanced reports make crashes easier to understand and resolve, with the largest improvement in repair guidance. These results indicate that supplying LLMs with stack traces and repository code yields enhanced crash reports that are substantially more useful for debugging.

## 🔍 Abstract (한글 번역)

arXiv:2509.13535v1 발표 유형: 새로운
요약: 충돌 보고서는 소프트웨어 유지보수에 중요하지만, 많은 보고서들은 개발자가 효율적으로 디버깅하기 위해 필요한 진단 세부 정보가 부족합니다. 우리는 대형 언어 모델이 결함 위치, 원인 설명 및 수리 제안을 추가하여 충돌 보고서를 향상시킬 수 있는지 조사합니다. 우리는 두 가지 향상 전략을 연구합니다: 직접-LLM은 스택 추적 컨텍스트를 사용하는 단일 샷 접근 방식이며, 에이전틱-LLM은 리포지토리를 탐색하여 추가 증거를 찾아내는 반복적인 접근 방식입니다. 492개의 실제 세계 충돌 보고서 데이터 세트에서, LLM으로 향상된 보고서는 Top-1 문제 지역화 정확도를 10.6% (원본 보고서)에서 40.2-43.1%로 향상시키고, 개발자 패치와 유사한 제안된 수정 사항을 생성합니다 (CodeBLEU 약 56-57%). 우리의 수동 평가와 LLM을 판사로 사용한 평가 모두 에이전틱-LLM이 더 강력한 원인 설명과 더 구체적인 수리 지침을 제공한다는 것을 보여줍니다. 16명의 참가자를 대상으로 한 사용자 연구는 향상된 보고서가 충돌을 이해하고 해결하기 쉽게 만들며, 수리 지침에서 가장 큰 개선이 있음을 확인합니다. 이러한 결과는 스택 추적과 리포지토리 코드를 LLM에 제공하면 디버깅에 대해 상당히 유용한 향상된 충돌 보고서가 생성된다는 것을 나타냅니다.

## 📝 요약

이 연구는 대규모 언어 모델이 충돌 보고서를 향상시킬 수 있는지 조사한다. 스택 추적 컨텍스트를 활용하는 단일 샷 방식인 Direct-LLM과 저장소를 탐색하여 추가 증거를 찾는 반복적 방식인 Agentic-LLM 두 가지 전략을 연구한다. 492개의 실제 충돌 보고서 데이터셋을 기반으로, LLM으로 향상된 보고서는 문제 지역화 정확도를 10.6%에서 40.2-43.1%로 향상시키고, 개발자 패치와 유사한 제안 수정을 제공한다. 수동 평가 및 LLM을 판사로 사용한 평가 모두 Agentic-LLM이 더 강력한 원인 설명과 실행 가능한 수리 지침을 제공한다는 것을 보여준다. 16명의 참가자를 대상으로 한 사용자 연구는 향상된 보고서가 충돌을 이해하고 해결하기 쉽게 만들어주며, 가장 큰 개선은 수리 지침에서 나타난다는 것을 확인한다. 이러한 결과는 LLM에 스택 추적과 저장소 코드를 제공함으로써 디버깅에 매우 유용한 향상된 충돌 보고서를 제공할 수 있다는 것을 보여준다.

## 🎯 주요 포인트


- 대규모 언어 모델을 사용하여 충돌 보고서를 향상시킬 수 있음

- LLM으로 향상된 보고서는 문제 지역화 정확도를 크게 향상시킴

- Agentic-LLM은 더 강력한 원인 해석과 실행 가능한 수리 지침을 제공함


---

*Generated on 2025-09-18 17:22:18*