---
keywords:
  - Large Language Model
  - Political Bias
  - Fact-Checking
  - X-phemisms
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.15335
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:26:22.497283",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Political Bias",
    "Fact-Checking",
    "X-phemisms"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Political Bias": 0.7,
    "Fact-Checking": 0.8,
    "X-phemisms": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, linking to broader discussions on AI and bias.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "political bias",
        "canonical": "Political Bias",
        "aliases": [
          "political leaning"
        ],
        "category": "unique_technical",
        "rationale": "Key concept in assessing the objectivity of AI models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "fact-checking",
        "canonical": "Fact-Checking",
        "aliases": [
          "verification"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant to discussions on AI's role in information verification.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "euphemisms or dysphemisms",
        "canonical": "X-phemisms",
        "aliases": [
          "euphemisms",
          "dysphemisms"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for assessing bias in language models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "objective assessment",
      "minimal pairs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "political bias",
      "resolved_canonical": "Political Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "fact-checking",
      "resolved_canonical": "Fact-Checking",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "euphemisms or dysphemisms",
      "resolved_canonical": "X-phemisms",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# PolBiX: Detecting LLMs' Political Bias in Fact-Checking through X-phemisms

**Korean Title:** PolBiX: X-피미즘을 통한 사실 확인에서 대형 언어 모델(LLM)의 정치적 편향 탐지

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15335.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.15335](https://arxiv.org/abs/2509.15335)

## 🔗 유사한 논문
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.6% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (84.5% similar)
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (83.8% similar)
- [[2025-09-19/Large Language Model probabilities cannot distinguish between possible and impossible language_20250919|Large Language Model probabilities cannot distinguish between possible and impossible language]] (83.4% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Fact-Checking|Fact-Checking]]
**⚡ Unique Technical**: [[keywords/Political Bias|Political Bias]], [[keywords/X-phemisms|X-phemisms]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15335v1 Announce Type: new 
Abstract: Large Language Models are increasingly used in applications requiring objective assessment, which could be compromised by political bias. Many studies found preferences for left-leaning positions in LLMs, but downstream effects on tasks like fact-checking remain underexplored. In this study, we systematically investigate political bias through exchanging words with euphemisms or dysphemisms in German claims. We construct minimal pairs of factually equivalent claims that differ in political connotation, to assess the consistency of LLMs in classifying them as true or false. We evaluate six LLMs and find that, more than political leaning, the presence of judgmental words significantly influences truthfulness assessment. While a few models show tendencies of political bias, this is not mitigated by explicitly calling for objectivism in prompts.

## 🔍 Abstract (한글 번역)

arXiv:2509.15335v1 발표 유형: 신규  
초록: 대형 언어 모델(LLM)은 점점 더 객관적인 평가가 요구되는 응용 프로그램에서 사용되고 있으며, 이는 정치적 편향에 의해 손상될 수 있습니다. 많은 연구에서 LLM이 좌파 성향을 선호한다는 것을 발견했지만, 사실 확인과 같은 작업에 대한 하위 효과는 충분히 탐구되지 않았습니다. 본 연구에서는 독일어 주장에서 완곡어법이나 경멸어법으로 단어를 교환하여 정치적 편향을 체계적으로 조사합니다. 정치적 함축이 다른 사실상 동등한 주장의 최소 쌍을 구성하여, LLM이 이를 진실 또는 거짓으로 분류하는 일관성을 평가합니다. 여섯 개의 LLM을 평가한 결과, 정치적 성향보다 판단적인 단어의 존재가 진실성 평가에 더 큰 영향을 미친다는 것을 발견했습니다. 일부 모델은 정치적 편향의 경향을 보이지만, 이는 프롬프트에서 객관성을 명시적으로 요구한다고 해서 완화되지 않습니다.

## 📝 요약

이 연구는 대형 언어 모델(LLM)의 정치적 편향이 사실 확인 작업에 미치는 영향을 조사합니다. 독일어 주장에서 완곡어법이나 경멸어를 교환하여 정치적 편향을 체계적으로 분석하고, 사실적으로 동등하지만 정치적 함의가 다른 최소 쌍의 주장을 구성하여 LLM의 일관성을 평가합니다. 여섯 개의 LLM을 평가한 결과, 정치적 성향보다 판단적 단어의 존재가 진실성 평가에 더 큰 영향을 미치는 것으로 나타났습니다. 일부 모델은 정치적 편향을 보였으나, 객관성을 강조하는 프롬프트로 이를 완화할 수는 없었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 정치적 편향으로 인해 객관적 평가가 필요한 응용 프로그램에서 문제가 발생할 수 있다.
- 2. 연구에서는 독일어 주장에서 완곡어법이나 경멸어를 교환하여 정치적 편향을 체계적으로 조사하였다.
- 3. 사실적으로 동등하지만 정치적 함의가 다른 최소 쌍의 주장을 구성하여 LLM의 일관성을 평가하였다.
- 4. 여섯 개의 LLM을 평가한 결과, 정치적 성향보다 판단적인 단어의 존재가 진실성 평가에 더 큰 영향을 미친다는 것을 발견하였다.
- 5. 일부 모델은 정치적 편향의 경향을 보였으나, 프롬프트에서 객관성을 명시적으로 요구해도 이러한 편향은 완화되지 않았다.


---

*Generated on 2025-09-23 11:26:22*