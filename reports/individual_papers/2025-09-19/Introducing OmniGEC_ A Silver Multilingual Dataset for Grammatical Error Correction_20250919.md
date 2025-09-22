
# Introducing OmniGEC: A Silver Multilingual Dataset for Grammatical Error Correction

**Korean Title:** 옴니GEC 소개: 문법 오류 수정을 위한 은색 다국어 데이터셋

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Silver Standard Dataset

## 🔗 유사한 논문
- [[COMI-LINGUA Expert Annotated Large-Scale Dataset for Multitask NLP in Hindi-English Code-Mixing]] (78.5% similar)
- [[Long-context Reference-based MT Quality Estimation]] (78.1% similar)
- [[Omni-CLST Error-aware Curriculum Learning with guided Selective chain-of-Thought for audio question answering]] (78.0% similar)
- [[Apertus Democratizing Open and Compliant LLMs for Global Language Environments]] (78.0% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (76.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14504v1 Announce Type: cross 
Abstract: In this paper, we introduce OmniGEC, a collection of multilingual silver-standard datasets for the task of Grammatical Error Correction (GEC), covering eleven languages: Czech, English, Estonian, German, Greek, Icelandic, Italian, Latvian, Slovene, Swedish, and Ukrainian. These datasets facilitate the development of multilingual GEC solutions and help bridge the data gap in adapting English GEC solutions to multilingual GEC. The texts in the datasets originate from three sources: Wikipedia edits for the eleven target languages, subreddits from Reddit in the eleven target languages, and the Ukrainian-only UberText 2.0 social media corpus. While Wikipedia edits were derived from human-made corrections, the Reddit and UberText 2.0 data were automatically corrected with the GPT-4o-mini model. The quality of the corrections in the datasets was evaluated both automatically and manually. Finally, we fine-tune two open-source large language models - Aya-Expanse (8B) and Gemma-3 (12B) - on the multilingual OmniGEC corpora and achieve state-of-the-art (SOTA) results for paragraph-level multilingual GEC. The dataset collection and the best-performing models are available on Hugging Face.

## 🔍 Abstract (한글 번역)

arXiv:2509.14504v1 발표 유형: 교차  
초록: 본 논문에서는 문법 오류 수정(GEC) 작업을 위한 다국어 은표준 데이터셋 모음인 OmniGEC를 소개합니다. 이 데이터셋은 체코어, 영어, 에스토니아어, 독일어, 그리스어, 아이슬란드어, 이탈리아어, 라트비아어, 슬로베니아어, 스웨덴어, 우크라이나어 등 11개 언어를 포함합니다. 이러한 데이터셋은 다국어 GEC 솔루션 개발을 촉진하고, 영어 GEC 솔루션을 다국어 GEC로 적응시키는 과정에서의 데이터 격차를 해소하는 데 도움을 줍니다. 데이터셋의 텍스트는 11개 대상 언어의 위키백과 편집, 11개 대상 언어의 Reddit 서브레딧, 우크라이나어 전용 UberText 2.0 소셜 미디어 코퍼스에서 비롯되었습니다. 위키백과 편집은 인간이 만든 수정에서 파생되었으며, Reddit 및 UberText 2.0 데이터는 GPT-4o-mini 모델을 사용하여 자동으로 수정되었습니다. 데이터셋의 수정 품질은 자동 및 수동으로 평가되었습니다. 마지막으로, 두 개의 오픈 소스 대형 언어 모델인 Aya-Expanse (8B)와 Gemma-3 (12B)를 다국어 OmniGEC 코퍼스에 맞추어 미세 조정하여 단락 수준의 다국어 GEC에서 최신(SOTA) 결과를 달성했습니다. 데이터셋 모음과 최고 성능의 모델은 Hugging Face에서 이용할 수 있습니다.

## 📝 요약

이 논문에서는 11개 언어에 대한 문법 오류 수정(GEC) 작업을 위한 다국어 은표준 데이터셋 모음인 OmniGEC를 소개합니다. 이 데이터셋은 체코어, 영어, 에스토니아어, 독일어, 그리스어, 아이슬란드어, 이탈리아어, 라트비아어, 슬로베니아어, 스웨덴어, 우크라이나어를 포함하며, 영어 GEC 솔루션을 다국어로 확장하는 데 도움을 줍니다. 데이터는 Wikipedia 편집, Reddit의 서브레딧, 우크라이나어 전용 UberText 2.0 소셜 미디어 코퍼스에서 수집되었습니다. Wikipedia 데이터는 인간이 수정한 것이며, 나머지는 GPT-4o-mini 모델로 자동 수정되었습니다. 데이터셋의 품질은 자동 및 수동으로 평가되었습니다. 또한, Aya-Expanse와 Gemma-3 모델을 OmniGEC 코퍼스에 맞춰 미세 조정하여 문단 수준의 다국어 GEC에서 최첨단 성과를 달성했습니다. 데이터셋과 모델은 Hugging Face에서 이용 가능합니다.

## 🎯 주요 포인트

- 1. OmniGEC는 11개 언어에 대한 다국어 문법 오류 수정(GEC)용 실버 표준 데이터셋을 제공합니다.

- 2. 데이터셋은 Wikipedia 편집, Reddit의 하위 레딧, 우크라이나어 전용 UberText 2.0 소셜 미디어 코퍼스에서 수집되었습니다.

- 3. Reddit 및 UberText 2.0 데이터는 GPT-4o-mini 모델을 사용하여 자동으로 수정되었습니다.

- 4. Aya-Expanse와 Gemma-3 모델을 OmniGEC 데이터셋으로 미세 조정하여 다국어 GEC에서 최첨단 성과를 달성했습니다.

- 5. 데이터셋과 최상의 성능을 보이는 모델은 Hugging Face에서 이용 가능합니다.

---

*Generated on 2025-09-19 14:56:05*