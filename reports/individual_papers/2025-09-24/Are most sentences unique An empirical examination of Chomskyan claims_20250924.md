<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:44:28.717708",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Linguistic Utterances",
    "Large Corpora",
    "Exact String Matches",
    "Genre Constraints"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Linguistic Utterances": 0.7,
    "Large Corpora": 0.8,
    "Exact String Matches": 0.78,
    "Genre Constraints": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "linguistic utterances",
        "canonical": "Linguistic Utterances",
        "aliases": [
          "spoken sentences",
          "verbal expressions"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's investigation and offers a unique perspective on language analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "large corpora",
        "canonical": "Large Corpora",
        "aliases": [
          "big datasets",
          "extensive corpora"
        ],
        "category": "broad_technical",
        "rationale": "The use of large corpora is essential for empirical analysis in linguistics and connects to data-driven research methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "exact string matches",
        "canonical": "Exact String Matches",
        "aliases": [
          "string matching",
          "exact matches"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the methodology used in the paper and links to computational linguistics techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "genre constraints",
        "canonical": "Genre Constraints",
        "aliases": [
          "genre limitations",
          "genre-specific constraints"
        ],
        "category": "unique_technical",
        "rationale": "Identifying how genre affects sentence uniqueness provides insights into linguistic variability.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "linguistic utterances",
      "resolved_canonical": "Linguistic Utterances",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "large corpora",
      "resolved_canonical": "Large Corpora",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "exact string matches",
      "resolved_canonical": "Exact String Matches",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "genre constraints",
      "resolved_canonical": "Genre Constraints",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Are most sentences unique? An empirical examination of Chomskyan claims

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19108.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19108](https://arxiv.org/abs/2509.19108)

## 🔗 유사한 논문
- [[2025-09-22/UPRPRC_ Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations_20250922|UPRPRC: Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations]] (78.2% similar)
- [[2025-09-24/False Friends Are Not Foes_ Investigating Vocabulary Overlap in Multilingual Language Models_20250924|False Friends Are Not Foes: Investigating Vocabulary Overlap in Multilingual Language Models]] (76.2% similar)
- [[2025-09-24/Trace Is In Sentences_ Unbiased Lightweight ChatGPT-Generated Text Detector_20250924|Trace Is In Sentences: Unbiased Lightweight ChatGPT-Generated Text Detector]] (75.9% similar)
- [[2025-09-23/Multilingual vs Crosslingual Retrieval of Fact-Checked Claims_ A Tale of Two Approaches_20250923|Multilingual vs Crosslingual Retrieval of Fact-Checked Claims: A Tale of Two Approaches]] (75.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Corpora|Large Corpora]]
**🔗 Specific Connectable**: [[keywords/Exact String Matches|Exact String Matches]]
**⚡ Unique Technical**: [[keywords/Linguistic Utterances|Linguistic Utterances]], [[keywords/Genre Constraints|Genre Constraints]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19108v1 Announce Type: new 
Abstract: A repeated claim in linguistics is that the majority of linguistic utterances are unique. For example, Pinker (1994: 10), summarizing an argument by Noam Chomsky, states that "virtually every sentence that a person utters or understands is a brand-new combination of words, appearing for the first time in the history of the universe." With the increased availability of large corpora, this is a claim that can be empirically investigated. The current paper addresses the question by using the NLTK Python library to parse corpora of different genres, providing counts of exact string matches in each. Results show that while completely unique sentences are often the majority of corpora, this is highly constrained by genre, and that duplicate sentences are not an insignificant part of any individual corpus.

## 📝 요약

이 논문은 대부분의 언어적 발화가 고유하다는 주장을 대규모 코퍼스를 통해 실증적으로 조사합니다. NLTK Python 라이브러리를 사용하여 다양한 장르의 코퍼스를 분석한 결과, 완전히 고유한 문장이 코퍼스의 대다수를 차지하지만, 이는 장르에 따라 크게 달라진다는 것을 발견했습니다. 또한, 중복된 문장도 각 코퍼스에서 무시할 수 없는 부분을 차지하고 있음을 밝혔습니다.

## 🎯 주요 포인트

- 1. 대부분의 언어적 발화는 고유하다는 주장이 반복적으로 제기되어 왔습니다.
- 2. 대규모 코퍼스의 이용 가능성이 증가하면서 이러한 주장을 실증적으로 조사할 수 있게 되었습니다.
- 3. 본 논문은 NLTK Python 라이브러리를 사용하여 다양한 장르의 코퍼스를 분석하고, 정확한 문자열 일치 횟수를 제공합니다.
- 4. 결과에 따르면, 완전히 고유한 문장이 코퍼스의 대다수를 차지하는 경우가 많지만, 이는 장르에 따라 크게 제한됩니다.
- 5. 중복 문장은 개별 코퍼스에서 무시할 수 없는 부분을 차지합니다.


---

*Generated on 2025-09-24 15:44:28*