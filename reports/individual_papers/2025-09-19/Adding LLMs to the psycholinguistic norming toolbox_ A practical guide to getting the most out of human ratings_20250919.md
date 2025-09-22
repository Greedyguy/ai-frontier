
# Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings

**Korean Title:** 심리언어학적 규준 도구에 LLM 추가하기: 인간 평가를 최대한 활용하기 위한 실용 가이드

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Augmented Human Norming

## 🔗 유사한 논문
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (86.5% similar)
- [[Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (85.7% similar)
- [[Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (84.7% similar)
- [[Do LLMs Align Human Values Regarding Social Biases_ Judging and Explaining Social Biases with LLMs_20250918|Do LLMs Align Human Values Regarding Social Biases Judging and Explaining Social Biases with LLMs]] (84.0% similar)
- [[A Comprehensive Survey on the Trustworthiness of Large Language Models in Healthcare]] (83.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14405v1 Announce Type: new 
Abstract: Word-level psycholinguistic norms lend empirical support to theories of language processing. However, obtaining such human-based measures is not always feasible or straightforward. One promising approach is to augment human norming datasets by using Large Language Models (LLMs) to predict these characteristics directly, a practice that is rapidly gaining popularity in psycholinguistics and cognitive science. However, the novelty of this approach (and the relative inscrutability of LLMs) necessitates the adoption of rigorous methodologies that guide researchers through this process, present the range of possible approaches, and clarify limitations that are not immediately apparent, but may, in some cases, render the use of LLMs impractical.
  In this work, we present a comprehensive methodology for estimating word characteristics with LLMs, enriched with practical advice and lessons learned from our own experience. Our approach covers both the direct use of base LLMs and the fine-tuning of models, an alternative that can yield substantial performance gains in certain scenarios. A major emphasis in the guide is the validation of LLM-generated data with human "gold standard" norms. We also present a software framework that implements our methodology and supports both commercial and open-weight models.
  We illustrate the proposed approach with a case study on estimating word familiarity in English. Using base models, we achieved a Spearman correlation of 0.8 with human ratings, which increased to 0.9 when employing fine-tuned models. This methodology, framework, and set of best practices aim to serve as a reference for future research on leveraging LLMs for psycholinguistic and lexical studies.

## 🔍 Abstract (한글 번역)

arXiv:2509.14405v1 발표 유형: 신규  
초록: 단어 수준의 심리언어학적 규범은 언어 처리 이론에 실증적 지원을 제공합니다. 그러나 이러한 인간 기반 측정을 얻는 것은 항상 가능하거나 간단하지 않습니다. 유망한 접근법 중 하나는 대형 언어 모델(LLMs)을 사용하여 이러한 특성을 직접 예측함으로써 인간 규범 데이터세트를 보강하는 것이며, 이는 심리언어학 및 인지과학 분야에서 빠르게 인기를 얻고 있습니다. 그러나 이 접근법의 참신함(및 LLM의 상대적 불투명성)은 연구자들이 이 과정을 안내하고 가능한 접근법의 범위를 제시하며 즉시 명확하지는 않지만 경우에 따라 LLM 사용을 비실용적으로 만들 수 있는 한계를 명확히 하는 엄격한 방법론의 채택을 필요로 합니다.  
이 연구에서는 실용적인 조언과 우리의 경험에서 얻은 교훈으로 풍부해진 LLM을 사용한 단어 특성 추정을 위한 포괄적인 방법론을 제시합니다. 우리의 접근법은 기본 LLM의 직접 사용과 특정 시나리오에서 상당한 성능 향상을 가져올 수 있는 모델의 미세 조정을 모두 다룹니다. 가이드에서 주요 강조점은 인간의 "골드 스탠다드" 규범으로 LLM 생성 데이터를 검증하는 것입니다. 또한 우리의 방법론을 구현하고 상업용 및 오픈 가중치 모델을 모두 지원하는 소프트웨어 프레임워크를 제시합니다.  
우리는 영어 단어 친숙도 추정에 대한 사례 연구를 통해 제안된 접근법을 설명합니다. 기본 모델을 사용하여 인간 평가와 0.8의 스피어만 상관관계를 달성했으며, 미세 조정된 모델을 사용할 때 0.9로 증가했습니다. 이 방법론, 프레임워크 및 모범 사례 세트는 심리언어학 및 어휘 연구를 위한 LLM 활용에 대한 향후 연구의 참고 자료로 활용되는 것을 목표로 합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용하여 단어 수준의 심리언어학적 특성을 예측하는 방법론을 제시합니다. 기존의 인간 기반 측정이 어려운 경우, LLM을 통해 이를 보완할 수 있습니다. 저자들은 LLM을 직접 사용하거나 모델을 미세 조정하여 성능을 향상시키는 방법을 설명하며, 인간의 "골드 스탠다드" 기준과의 검증을 강조합니다. 영어 단어 친숙도를 예측하는 사례 연구에서, 기본 모델로는 인간 평가와 0.8의 스피어만 상관관계를, 미세 조정 모델로는 0.9의 상관관계를 달성했습니다. 이 연구는 심리언어학 및 어휘 연구에서 LLM 활용을 위한 참고 자료로 활용될 수 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)을 활용하여 인간 기반의 심리언어학적 규범을 예측하는 방법이 점점 인기를 얻고 있다.

- 2. LLM을 활용한 단어 특성 추정 방법론을 제시하며, 직접적인 모델 사용과 모델 미세 조정의 두 가지 접근 방식을 다룬다.

- 3. LLM 생성 데이터의 유효성을 인간의 "골드 스탠다드" 규범과 비교하여 검증하는 것이 중요하다.

- 4. 제안된 방법론은 영어 단어 친숙도 추정 사례 연구에서 인간 평가와 0.8의 스피어만 상관을 달성했으며, 미세 조정 모델 사용 시 0.9로 증가했다.

- 5. 본 연구는 심리언어학 및 어휘 연구에서 LLM을 활용하는 미래 연구의 참고 자료로 활용될 수 있다.

---

*Generated on 2025-09-19 15:47:35*