---
keywords:
  - Large Language Model
  - Browsing Language
  - Heterogeneity aware Training of Language Model
  - Clusterwise Language Model Training
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2508.15474
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:08:19.758741",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Browsing Language",
    "Heterogeneity aware Training of Language Model",
    "Clusterwise Language Model Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Browsing Language": 0.78,
    "Heterogeneity aware Training of Language Model": 0.8,
    "Clusterwise Language Model Training": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, linking to established concepts in language modeling.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "language of browsing",
        "canonical": "Browsing Language",
        "aliases": [
          "user browsing language"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept of user-specific browsing patterns as a language.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "HeTLM",
        "canonical": "Heterogeneity aware Training of Language Model",
        "aliases": [
          "HeTLM"
        ],
        "category": "unique_technical",
        "rationale": "A new training method specific to the paper, enhancing model alignment with user behavior.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "clusterwise LM training",
        "canonical": "Clusterwise Language Model Training",
        "aliases": [
          "cluster-based LM training"
        ],
        "category": "specific_connectable",
        "rationale": "Relates to advanced training techniques, relevant for linking with clustering methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "subjective behaviors",
      "preferences",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "language of browsing",
      "resolved_canonical": "Browsing Language",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "HeTLM",
      "resolved_canonical": "Heterogeneity aware Training of Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "clusterwise LM training",
      "resolved_canonical": "Clusterwise Language Model Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Subjective Behaviors and Preferences in LLM: Language of Browsing

**Korean Title:** 주제적 행동과 선호도에 관한 LLM: 브라우징 언어

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.15474.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2508.15474](https://arxiv.org/abs/2508.15474)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (87.4% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (86.3% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (85.4% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (85.4% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Clusterwise Language Model Training|Clusterwise Language Model Training]]
**⚡ Unique Technical**: [[keywords/Browsing Language|Browsing Language]], [[keywords/Heterogeneity aware Training of Language Model|Heterogeneity aware Training of Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15474v3 Announce Type: replace-cross 
Abstract: A Large Language Model (LLM) offers versatility across domains and tasks, purportedly benefiting users with a wide variety of behaviors and preferences. We question this perception about an LLM when users have inherently subjective behaviors and preferences, as seen in their ubiquitous and idiosyncratic browsing of websites or apps. The sequential behavior logs of pages, thus generated, form something akin to each user's self-constructed "language", albeit without the structure and grammar imbued in natural languages. We ask: (i) Can a small LM represent the "language of browsing" better than a large LM? (ii) Can an LM with a single set of parameters (or, single LM) adequately capture myriad users' heterogeneous, subjective behaviors and preferences? (iii) Can a single LM with high average performance, yield low variance in performance to make alignment good at user level? We introduce clusterwise LM training, HeTLM (Heterogeneity aware Training of Language Model), appropriate for subjective behaviors. We find that (i) a small LM trained using a page-level tokenizer outperforms large pretrained or finetuned LMs; (ii) HeTLM with heterogeneous cluster specific set of parameters outperforms a single LM of the same family, controlling for the number of parameters; and (iii) a higher mean and a lower variance in generation ensues, implying improved alignment.

## 🔍 Abstract (한글 번역)

arXiv:2508.15474v3 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLM)은 다양한 분야와 작업에서 다재다능함을 제공하여, 다양한 행동과 선호도를 가진 사용자들에게 이점을 제공한다고 주장됩니다. 우리는 사용자가 웹사이트나 앱을 독특하고 특이하게 탐색하는 것처럼 본질적으로 주관적인 행동과 선호도를 가질 때, LLM에 대한 이러한 인식을 의문시합니다. 이렇게 생성된 페이지의 순차적 행동 로그는 자연어에 내재된 구조와 문법 없이 각 사용자가 스스로 구성한 "언어"와 유사한 것을 형성합니다. 우리는 다음과 같은 질문을 던집니다: (i) 작은 언어 모델이 "탐색의 언어"를 대형 언어 모델보다 더 잘 표현할 수 있는가? (ii) 단일 파라미터 집합(또는 단일 언어 모델)을 가진 언어 모델이 다양한 사용자의 이질적이고 주관적인 행동과 선호도를 적절히 포착할 수 있는가? (iii) 높은 평균 성능을 가진 단일 언어 모델이 사용자 수준에서의 정렬을 좋게 하기 위해 성능의 분산을 낮게 유지할 수 있는가? 우리는 주관적 행동에 적합한 클러스터별 언어 모델 훈련, HeTLM(이질성 인식 언어 모델 훈련)을 소개합니다. 우리는 (i) 페이지 수준의 토크나이저를 사용하여 훈련된 작은 언어 모델이 대형 사전 훈련 또는 미세 조정된 언어 모델을 능가한다는 것을 발견했습니다; (ii) 이질적인 클러스터 특정 파라미터 집합을 가진 HeTLM이 동일한 계열의 단일 언어 모델을 파라미터 수를 통제하면서 능가하며; (iii) 생성에서 더 높은 평균과 더 낮은 분산이 발생하여, 정렬이 개선됨을 의미합니다.

## 📝 요약

이 논문은 사용자들의 주관적인 행동과 선호도를 반영하는 대형 언어 모델(LLM)의 효용성을 의문시하며, 각 사용자의 웹사이트 및 앱 탐색 기록을 분석합니다. 연구에서는 (i) 작은 언어 모델(LM)이 대형 모델보다 탐색 "언어"를 더 잘 표현할 수 있는지, (ii) 단일 모델이 다양한 사용자 행동을 포괄할 수 있는지, (iii) 평균 성능이 높은 단일 모델이 사용자 수준에서 낮은 성능 변동성을 보이는지를 탐구합니다. 이를 위해 HeTLM(이질성 인식 언어 모델 훈련)을 제안하며, 작은 LM이 페이지 수준 토크나이저를 사용해 대형 모델을 능가하고, HeTLM이 이질적 클러스터별 매개변수를 통해 단일 모델보다 우수한 성능을 보임을 발견했습니다. 이는 평균 성능 향상과 변동성 감소로 이어져 사용자 맞춤화가 개선됨을 시사합니다.

## 🎯 주요 포인트

- 1. 작은 언어 모델(LM)이 페이지 수준의 토크나이저를 사용하여 훈련될 경우, 대형 사전 훈련 또는 미세 조정된 언어 모델보다 더 나은 성능을 발휘합니다.
- 2. HeTLM(이질성 인식 언어 모델 훈련)은 이질적인 클러스터별 매개변수 세트를 사용하여 동일한 계열의 단일 언어 모델보다 우수한 성능을 보입니다.
- 3. 평균 성능이 높고 생성의 분산이 낮아져 사용자 수준에서의 정렬이 개선됩니다.


---

*Generated on 2025-09-23 10:08:19*