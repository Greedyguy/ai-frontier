# Real, Fake, or Manipulated? Detecting Machine-Influenced Text

**Korean Title:** 진짜, 가짜, 혹은 조작된 것인가? 기계에 의해 영향을 받은 텍스트 감지

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Length-Robust Detection|Length-Robust Detection]] [[keywords/specific/Subcategory Guidance|Subcategory Guidance]] [[keywords/broad/Large Language Model|Large Language Model]] [[keywords/broad/Machine Generated Text|Machine Generated Text]] [[keywords/unique/HERO|HERO]] [[categories/cs.CL|cs.CL]] [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.8% similar) [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (85.3% similar) [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Subcategory Guidance
**🔬 Broad Technical**: Large Language Model, Machine Generated Text
**⭐ Unique Technical**: HERO
## 🔗 유사한 논문
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (86.8% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang A Systematic Comparison between Human and Machine-Generated Slang Usages]] (85.3% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM Language of Browsing]] (83.8% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (83.8% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text]] (83.6% similar)


**ArXiv ID**: [2509.15350](https://arxiv.org/abs/2509.15350)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15350.pdf)


**ArXiv ID**: [2509.15350](https://arxiv.org/abs/2509.15350)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15350.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Length-Robust Detection
**🔗 Specific Connectable**: Subcategory Guidance
**⭐ Unique Technical**: HERO
**🔬 Broad Technical**: Large Language Model, Machine Generated Text

## 🏷️ 추출된 키워드



`Large Language Model` • 

`Machine Generated Text` • 

`Subcategory Guidance` • 

`HERO` • 

`Length-Robust Detection`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15350v1 Announce Type: new 
Abstract: Large Language Model (LLMs) can be used to write or modify documents, presenting a challenge for understanding the intent behind their use. For example, benign uses may involve using LLM on a human-written document to improve its grammar or to translate it into another language. However, a document entirely produced by a LLM may be more likely to be used to spread misinformation than simple translation (\eg, from use by malicious actors or simply by hallucinating). Prior works in Machine Generated Text (MGT) detection mostly focus on simply identifying whether a document was human or machine written, ignoring these fine-grained uses. In this paper, we introduce a HiErarchical, length-RObust machine-influenced text detector (HERO), which learns to separate text samples of varying lengths from four primary types: human-written, machine-generated, machine-polished, and machine-translated. HERO accomplishes this by combining predictions from length-specialist models that have been trained with Subcategory Guidance. Specifically, for categories that are easily confused (\eg, different source languages), our Subcategory Guidance module encourages separation of the fine-grained categories, boosting performance. Extensive experiments across five LLMs and six domains demonstrate the benefits of our HERO, outperforming the state-of-the-art by 2.5-3 mAP on average.

## 🔍 Abstract (한글 번역)

arXiv:2509.15350v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)은 문서를 작성하거나 수정하는 데 사용될 수 있으며, 이는 그 사용 의도를 이해하는 데 어려움을 제기합니다. 예를 들어, LLM을 인간이 작성한 문서에 사용하여 문법을 개선하거나 다른 언어로 번역하는 것은 무해한 사용에 해당할 수 있습니다. 그러나 LLM에 의해 완전히 생성된 문서는 단순 번역보다 잘못된 정보를 퍼뜨리는 데 사용될 가능성이 더 높습니다(예: 악의적인 행위자에 의한 사용 또는 단순히 환각에 의한 경우). 기계 생성 텍스트(MGT) 탐지에 관한 이전 연구들은 대부분 문서가 인간에 의해 작성되었는지 기계에 의해 작성되었는지를 식별하는 데 중점을 두며, 이러한 세부적인 사용을 무시합니다. 본 논문에서는 HiErarchical, 길이-견고한 기계 영향 텍스트 탐지기(HERO)를 소개하며, 이는 인간 작성, 기계 생성, 기계 수정, 기계 번역의 네 가지 주요 유형에서 다양한 길이의 텍스트 샘플을 구분하도록 학습합니다. HERO는 하위 범주 지침과 함께 훈련된 길이 전문 모델의 예측을 결합하여 이를 달성합니다. 특히, 쉽게 혼동될 수 있는 범주들(예: 다른 원본 언어)에 대해, 우리의 하위 범주 지침 모듈은 세부 범주의 분리를 장려하여 성능을 향상시킵니다. 다섯 개의 LLM과 여섯 개의 도메인에 걸친 광범위한 실험은 HERO의 이점을 입증하며, 최첨단 기술을 평균 2.5-3 mAP 만큼 능가합니다.

## 📝 요약

이 논문은 문서 작성 및 수정에 사용되는 대형 언어 모델(LLM)의 의도를 이해하는 데 어려움이 있다는 문제를 다룹니다. LLM은 문법 개선이나 번역에 사용될 수 있지만, 완전히 LLM에 의해 생성된 문서는 잘못된 정보를 퍼뜨릴 가능성이 높습니다. 기존 연구는 주로 문서가 인간 또는 기계에 의해 작성되었는지를 식별하는 데 초점을 맞추었지만, 이 논문에서는 인간 작성, 기계 생성, 기계 수정, 기계 번역의 네 가지 주요 유형을 구분하는 HiErarchical, length-RObust 기계 영향 텍스트 탐지기(HERO)를 제안합니다. HERO는 길이별 전문가 모델의 예측을 결합하고, 세부 카테고리 구분을 통해 성능을 향상시킵니다. 다섯 개의 LLM과 여섯 개의 도메인에 걸친 실험에서 HERO는 최첨단 기술보다 평균 2.5-3 mAP 더 높은 성능을 보였습니다.

## 🎯 주요 포인트


- 1. 대형 언어 모델(LLM)은 문서 작성 및 수정에 사용될 수 있으며, 이는 사용 의도를 이해하는 데 어려움을 준다.

- 2. LLM을 사용한 문서가 오역이나 허위 정보를 퍼뜨리는 데 사용될 가능성이 높다.

- 3. 기존의 기계 생성 텍스트(MGT) 탐지 연구는 문서가 인간 작성인지 기계 생성인지 식별하는 데 중점을 두었으나, 세부적인 사용 용도를 간과했다.

- 4. 본 논문에서는 인간 작성, 기계 생성, 기계 수정, 기계 번역의 네 가지 주요 유형을 구분하는 HERO 탐지기를 소개한다.

- 5. HERO는 세부 카테고리 분리를 통해 성능을 향상시키며, 최신 기술 대비 평균 2.5-3 mAP 높은 성능을 보인다.


---

*Generated on 2025-09-22 16:20:08*