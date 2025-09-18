
# GBV-SQL: Guided Generation and SQL2Text Back-Translation Validation for Multi-Agent Text2SQL

**Korean Title:** GBV-SQL: 다중 에이전트 텍스트2SQL을 위한 안내 생성 및 SQL2Text 역 번역 유효성 검사

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[keywords/Text2sql|Text2sql]] [[keywords/Large Language Models|Large Language Models]] [[keywords/Guided Generation|Guided Generation]] [[keywords/Sql2text Backtranslation|Sql2text Backtranslation]] [[keywords/Multiagent Framework|Multiagent Framework]] [[keywords/Gold Errors|Gold Errors]] [[keywords/Benchmark Integrity|Benchmark Integrity]] [[keywords/Semantic Validation|Semantic Validation]] [[keywords/Dataset Curation|Dataset Curation]] [[keywords/Execution Accuracy|Execution Accuracy]] [[categories/cs.AI|cs.AI]]

**ArXiv ID**: [2509.12612](https://arxiv.org/abs/2509.12612)
**Published**: 2025-09-17
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.12612.pdf)


## 🏷️ 추출된 키워드



`Text2sql` • 

`Guided Generation` • 

`Sql2text Backtranslation` • 

`Multiagent Framework` • 

`Gold Errors` • 

`Benchmark` • 

`Semantic Validation` • 

`Dataset Curation` • 

`Execution Accuracy`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12612v1 Announce Type: new 
Abstract: While Large Language Models have significantly advanced Text2SQL generation, a critical semantic gap persists where syntactically valid queries often misinterpret user intent. To mitigate this challenge, we propose GBV-SQL, a novel multi-agent framework that introduces Guided Generation with SQL2Text Back-translation Validation. This mechanism uses a specialized agent to translate the generated SQL back into natural language, which verifies its logical alignment with the original question. Critically, our investigation reveals that current evaluation is undermined by a systemic issue: the poor quality of the benchmarks themselves. We introduce a formal typology for "Gold Errors", which are pervasive flaws in the ground-truth data, and demonstrate how they obscure true model performance. On the challenging BIRD benchmark, GBV-SQL achieves 63.23% execution accuracy, a 5.8% absolute improvement. After removing flawed examples, GBV-SQL achieves 96.5% (dev) and 97.6% (test) execution accuracy on the Spider benchmark. Our work offers both a robust framework for semantic validation and a critical perspective on benchmark integrity, highlighting the need for more rigorous dataset curation.

## 🔍 Abstract (한글 번역)

arXiv:2509.12612v1 발표 유형: 새로운
요약: 대규모 언어 모델은 Text2SQL 생성을 크게 발전시켰지만, 구문적으로 유효한 쿼리가 종종 사용자 의도를 잘못 해석하는 중요한 의미적 간극이 여전히 존재합니다. 이러한 도전에 대처하기 위해, 우리는 GBV-SQL이라는 새로운 멀티 에이전트 프레임워크를 제안합니다. 이 프레임워크는 SQL2Text 역 번역 검증을 통해 가이드된 생성을 도입합니다. 이 메커니즘은 생성된 SQL을 자연어로 다시 번역하는 특수 에이전트를 사용하여 원래 질문과의 논리적 일치를 확인합니다. 중요한 점은, 우리의 조사 결과 현재의 평가가 체계적인 문제로 인해 저하되고 있는 것을 보여줍니다: 벤치마크 자체의 품질이 낮습니다. 우리는 "골드 에러"에 대한 공식적인 유형론을 소개하며, 이는 원본 데이터의 만연한 결함이며, 이로써 진정한 모델 성능이 흐릿해지는 방식을 보여줍니다. 어려운 BIRD 벤치마크에서 GBV-SQL은 63.23%의 실행 정확도를 달성하며, 5.8%의 절대적인 개선을 이루었습니다. 결함이 있는 예제를 제거한 후, GBV-SQL은 Spider 벤치마크에서 96.5% (개발) 및 97.6% (테스트)의 실행 정확도를 달성합니다. 우리의 연구는 의미적 유효성을 갖는 견고한 프레임워크와 벤치마크 무결성에 대한 비판적인 시각을 제공하며, 보다 엄격한 데이터셋 선별의 필요성을 강조합니다.

## 📝 요약

최근 대형 언어 모델은 Text2SQL 생성을 크게 발전시켰지만, 문법적으로 유효한 쿼리가 종종 사용자 의도를 잘못 해석하는 중요한 의미론적 간극이 여전히 존재합니다. 이러한 도전을 극복하기 위해 우리는 GBV-SQL이라는 새로운 다중 에이전트 프레임워크를 제안합니다. 이 프레임워크는 SQL2Text

## 🎯 주요 포인트


- GBV-SQL은 새로운 멀티 에이전트 프레임워크로, SQL을 자연어로 다시 번역하여 논리적 일치를 확인함

- 현재 Text2SQL 모델 성능을 가릴 수 있는 시스템적 문제로 "Gold Errors"를 소개하고 이를 보완함

- BIRD 벤치마크에서 GBV-SQL은 63.23%의 실행 정확도를 달성하며, Spider 벤치마크에서 96.5% (dev) 및 97.6% (test)의 실행 정확도를 달성함

- 우리의 연구는 의미 검증을 위한 견고한 프레임워크를 제공


---

*Generated on 2025-09-18 11:10:21*