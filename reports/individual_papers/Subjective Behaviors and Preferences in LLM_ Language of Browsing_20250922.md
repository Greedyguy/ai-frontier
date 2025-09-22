# Subjective Behaviors and Preferences in LLM: Language of Browsing

**Korean Title:** 주관적 행동과 선호도에 관한 LLM: 브라우징 언어

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Language of Browsing

## 🔗 유사한 논문
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox A practical guide to getting the most out of human ratings]] (85.4% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (85.1% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony On Multilingual Data Allocation for Large Language Models Pretraining]] (84.9% similar)
- [[2025-09-18/Catch Me If You Can Not Yet_ LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors_20250918|Catch Me If You Can Not Yet LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors]] (84.9% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang A Systematic Comparison between Human and Machine-Generated Slang Usages]] (84.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15474v3 Announce Type: replace-cross 
Abstract: A Large Language Model (LLM) offers versatility across domains and tasks, purportedly benefiting users with a wide variety of behaviors and preferences. We question this perception about an LLM when users have inherently subjective behaviors and preferences, as seen in their ubiquitous and idiosyncratic browsing of websites or apps. The sequential behavior logs of pages, thus generated, form something akin to each user's self-constructed "language", albeit without the structure and grammar imbued in natural languages. We ask: (i) Can a small LM represent the "language of browsing" better than a large LM? (ii) Can an LM with a single set of parameters (or, single LM) adequately capture myriad users' heterogeneous, subjective behaviors and preferences? (iii) Can a single LM with high average performance, yield low variance in performance to make alignment good at user level? We introduce clusterwise LM training, HeTLM (Heterogeneity aware Training of Language Model), appropriate for subjective behaviors. We find that (i) a small LM trained using a page-level tokenizer outperforms large pretrained or finetuned LMs; (ii) HeTLM with heterogeneous cluster specific set of parameters outperforms a single LM of the same family, controlling for the number of parameters; and (iii) a higher mean and a lower variance in generation ensues, implying improved alignment.

## 🔍 Abstract (한글 번역)

arXiv:2508.15474v3 발표 유형: 교차 대체  
초록: 대형 언어 모델(LLM)은 다양한 분야와 작업에서 유연성을 제공하며, 다양한 행동과 선호도를 가진 사용자에게 이점을 제공한다고 주장됩니다. 우리는 사용자가 웹사이트나 앱을 독특하고 특이하게 탐색하는 것처럼 본질적으로 주관적인 행동과 선호도를 가질 때 LLM에 대한 이러한 인식에 의문을 제기합니다. 이로 인해 생성된 페이지의 순차적 행동 로그는 자연어에 내재된 구조와 문법 없이 각 사용자가 스스로 구성한 "언어"와 유사한 것을 형성합니다. 우리는 다음과 같은 질문을 던집니다: (i) 작은 언어 모델(LM)이 "탐색 언어"를 대형 언어 모델보다 더 잘 표현할 수 있는가? (ii) 단일 매개변수 세트(또는 단일 LM)를 가진 LM이 다양한 사용자의 이질적이고 주관적인 행동과 선호도를 적절히 포착할 수 있는가? (iii) 높은 평균 성능을 가진 단일 LM이 사용자 수준에서의 정렬을 좋게 하기 위해 성능의 분산을 낮게 유지할 수 있는가? 우리는 주관적인 행동에 적합한 클러스터별 LM 훈련, HeTLM(이질성 인식 언어 모델 훈련)을 소개합니다. 우리는 (i) 페이지 수준의 토크나이저를 사용하여 훈련된 작은 LM이 대형 사전 훈련 또는 미세 조정된 LM보다 뛰어나다는 것을 발견했습니다; (ii) 이질적인 클러스터별 매개변수 세트를 가진 HeTLM이 동일한 패밀리의 단일 LM을 매개변수 수를 제어하면서 능가한다는 것을 발견했습니다; 그리고 (iii) 생성에서 더 높은 평균과 더 낮은 분산이 발생하여 정렬이 개선됨을 의미합니다.

## 📝 요약

이 논문은 사용자들의 주관적인 행동과 선호도를 반영하는 대형 언어 모델(LLM)의 효용성을 재검토합니다. 연구는 웹사이트나 앱에서의 사용자 행동 로그가 각자의 "브라우징 언어"를 형성한다고 보고, 작은 언어 모델이 이를 더 잘 표현할 수 있는지를 탐구합니다. 제안된 HeTLM(이질성 인식 언어 모델 훈련)은 사용자 행동의 이질성을 고려하여 클러스터별로 훈련된 모델로, 단일 모델보다 성능이 우수함을 보였습니다. 또한, 평균 성능이 높고 성능 변동성이 낮아 사용자 수준에서의 정렬이 개선되었습니다.

## 🎯 주요 포인트

- 1. 사용자의 주관적인 행동과 선호도를 반영하는 "브라우징 언어"는 작은 언어 모델(LM)이 큰 언어 모델보다 더 잘 표현할 수 있다.

- 2. HeTLM(이질성 인식 언어 모델 훈련)은 사용자 간의 이질적인 행동을 반영하여 특정 클러스터별 매개변수를 사용함으로써 단일 언어 모델보다 성능이 우수하다.

- 3. 페이지 수준의 토크나이저를 사용하여 훈련된 작은 언어 모델은 대형 사전 훈련 또는 미세 조정된 언어 모델보다 성능이 뛰어나다.

- 4. 높은 평균 성능과 낮은 성능 분산을 통해 사용자 수준에서의 정렬이 개선된다.

---

*Generated on 2025-09-22 14:58:35*