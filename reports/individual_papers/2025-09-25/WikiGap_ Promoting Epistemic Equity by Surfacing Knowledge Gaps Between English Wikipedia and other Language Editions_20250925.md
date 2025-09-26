---
keywords:
  - Epistemic Equity
  - Knowledge Gaps
  - Interlanguage Link
  - Multilingual Information-Gap Discovery
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2505.24195
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:58:49.044141",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Epistemic Equity",
    "Knowledge Gaps",
    "Interlanguage Link",
    "Multilingual Information-Gap Discovery"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Epistemic Equity": 0.78,
    "Knowledge Gaps": 0.77,
    "Interlanguage Link": 0.8,
    "Multilingual Information-Gap Discovery": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Epistemic Equity",
        "canonical": "Epistemic Equity",
        "aliases": [
          "Knowledge Equity"
        ],
        "category": "unique_technical",
        "rationale": "Addresses the distribution of knowledge across languages, enhancing the understanding of Wikipedia's role in global knowledge access.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Knowledge Gaps",
        "canonical": "Knowledge Gaps",
        "aliases": [
          "Information Gaps"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the disparities in content coverage between different language editions, crucial for understanding Wikipedia's limitations.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      },
      {
        "surface": "Interlanguage Link",
        "canonical": "Interlanguage Link",
        "aliases": [
          "ILL",
          "Language Link"
        ],
        "category": "specific_connectable",
        "rationale": "Key feature of Wikipedia that facilitates navigation between language editions, relevant for discussions on multilingual access.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multilingual Information-Gap Discovery",
        "canonical": "Multilingual Information-Gap Discovery",
        "aliases": [
          "Information-Gap Discovery"
        ],
        "category": "unique_technical",
        "rationale": "A novel method for identifying content disparities across languages, central to the paper's proposed solution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "method",
      "system",
      "study",
      "participants",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Epistemic Equity",
      "resolved_canonical": "Epistemic Equity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Knowledge Gaps",
      "resolved_canonical": "Knowledge Gaps",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Interlanguage Link",
      "resolved_canonical": "Interlanguage Link",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multilingual Information-Gap Discovery",
      "resolved_canonical": "Multilingual Information-Gap Discovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# WikiGap: Promoting Epistemic Equity by Surfacing Knowledge Gaps Between English Wikipedia and other Language Editions

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.24195.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2505.24195](https://arxiv.org/abs/2505.24195)

## 🔗 유사한 논문
- [[2025-09-23/WikiBigEdit_ Understanding the Limits of Lifelong Knowledge Editing in LLMs_20250923|WikiBigEdit: Understanding the Limits of Lifelong Knowledge Editing in LLMs]] (82.3% similar)
- [[2025-09-24/Anecdoctoring_ Automated Red-Teaming Across Language and Place_20250924|Anecdoctoring: Automated Red-Teaming Across Language and Place]] (78.4% similar)
- [[2025-09-23/Multilingual vs Crosslingual Retrieval of Fact-Checked Claims_ A Tale of Two Approaches_20250923|Multilingual vs Crosslingual Retrieval of Fact-Checked Claims: A Tale of Two Approaches]] (77.4% similar)
- [[2025-09-25/Enhancing RAG Efficiency with Adaptive Context Compression_20250925|Enhancing RAG Efficiency with Adaptive Context Compression]] (77.4% similar)
- [[2025-09-23/MAKIEval_ A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs_20250923|MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs]] (77.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Interlanguage Link|Interlanguage Link]]
**⚡ Unique Technical**: [[keywords/Epistemic Equity|Epistemic Equity]], [[keywords/Knowledge Gaps|Knowledge Gaps]], [[keywords/Multilingual Information-Gap Discovery|Multilingual Information-Gap Discovery]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.24195v3 Announce Type: replace-cross 
Abstract: With more than 11 times as many pageviews as the next largest edition, English Wikipedia dominates global knowledge access relative to other language editions. Readers are prone to assuming English Wikipedia as a superset of all language editions, leading many to prefer it even when their primary language is not English. Other language editions, however, comprise complementary facts rooted in their respective cultures and media environments, which are marginalized in English Wikipedia. While Wikipedia's user interface enables switching between language editions through its Interlanguage Link (ILL) system, it does not reveal to readers that other language editions contain valuable, complementary information. We present WikiGap, a system that surfaces complementary facts sourced from other Wikipedias within the English Wikipedia interface. Specifically, by combining a recent multilingual information-gap discovery method with a user-centered design, WikiGap enables access to complementary information from French, Russian, and Chinese Wikipedia. In a mixed-methods study (n=21), WikiGap significantly improved fact-finding accuracy, reduced task time, and received a 32-point higher usability score relative to Wikipedia's current ILL-based navigation system. Participants reported increased awareness of the availability of complementary information in non-English editions and reconsidered the completeness of English Wikipedia. WikiGap thus paves the way for improved epistemic equity across language editions.

## 📝 요약

영어 위키백과는 다른 언어판에 비해 압도적인 페이지뷰를 기록하며 글로벌 지식 접근을 주도하고 있지만, 각 언어판은 해당 문화와 미디어 환경에 뿌리를 둔 보완적인 정보를 포함하고 있습니다. WikiGap은 이러한 보완적 사실을 영어 위키백과 인터페이스에 통합하여 제공하는 시스템으로, 최근의 다국어 정보 격차 발견 방법과 사용자 중심 디자인을 결합하여 프랑스어, 러시아어, 중국어 위키백과의 정보를 활용합니다. 혼합 방법 연구(n=21)에서 WikiGap은 사실 탐색 정확도를 향상시키고 작업 시간을 단축했으며, 현재의 인터링크 기반 탐색 시스템보다 32점 높은 사용성 점수를 받았습니다. 참가자들은 비영어판의 보완적 정보에 대한 인식이 증가하고 영어 위키백과의 완전성을 재고하게 되었다고 보고했습니다. WikiGap은 언어판 간의 인식적 형평성을 개선하는 길을 열었습니다.

## 🎯 주요 포인트

- 1. 영어 위키백과는 다른 언어판에 비해 11배 이상의 페이지뷰를 기록하며 글로벌 지식 접근을 지배하고 있다.
- 2. 영어 위키백과는 모든 언어판의 상위 집합으로 오인되기 쉬워, 비영어권 사용자들도 영어판을 선호하는 경향이 있다.
- 3. WikiGap 시스템은 영어 위키백과 인터페이스 내에서 다른 언어판의 보완적 사실을 제공하여 정보 접근성을 높인다.
- 4. 혼합 방법 연구에서 WikiGap은 사실 찾기 정확성을 향상시키고, 작업 시간을 단축하며, 사용성 점수를 32점 높였다.
- 5. WikiGap은 비영어판의 보완적 정보에 대한 인식을 높이고 영어 위키백과의 완전성을 재고하게 한다.


---

*Generated on 2025-09-26 08:58:49*