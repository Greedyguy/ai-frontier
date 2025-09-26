---
keywords:
  - Large Language Model
  - Stereotype Content Model
  - Gender Bias
  - Sexual and Gender Minorities
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2501.05926
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:51:13.739909",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Stereotype Content Model",
    "Gender Bias",
    "Sexual and Gender Minorities"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Stereotype Content Model": 0.7,
    "Gender Bias": 0.8,
    "Sexual and Gender Minorities": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the study and connects to existing research on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Stereotype Content Model",
        "canonical": "Stereotype Content Model",
        "aliases": [
          "SCM"
        ],
        "category": "unique_technical",
        "rationale": "This model is a key framework used in the study to analyze biases, providing a unique connection point.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Gender Bias",
        "canonical": "Gender Bias",
        "aliases": [
          "Sexual Bias"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding gender bias is crucial for linking to broader discussions on bias in AI systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Sexual and Gender Minorities",
        "canonical": "Sexual and Gender Minorities",
        "aliases": [
          "LGBTQ+"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on non-binary categories, offering a unique perspective on bias.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Stereotype Content Model",
      "resolved_canonical": "Stereotype Content Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Gender Bias",
      "resolved_canonical": "Gender Bias",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Sexual and Gender Minorities",
      "resolved_canonical": "Sexual and Gender Minorities",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# LLMs Reproduce Stereotypes of Sexual and Gender Minorities

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2501.05926.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2501.05926](https://arxiv.org/abs/2501.05926)

## 🔗 유사한 논문
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (88.8% similar)
- [[2025-09-25/Probing Gender Bias in Multilingual LLMs_ A Case Study of Stereotypes in Persian_20250925|Probing Gender Bias in Multilingual LLMs: A Case Study of Stereotypes in Persian]] (88.4% similar)
- [[2025-09-23/Justice in Judgment_ Unveiling (Hidden) Bias in LLM-assisted Peer Reviews_20250923|Justice in Judgment: Unveiling (Hidden) Bias in LLM-assisted Peer Reviews]] (87.5% similar)
- [[2025-09-23/EuroGEST_ Investigating gender stereotypes in multilingual language models_20250923|EuroGEST: Investigating gender stereotypes in multilingual language models]] (87.1% similar)
- [[2025-09-23/Auto-Search and Refinement_ An Automated Framework for Gender Bias Mitigation in Large Language Models_20250923|Auto-Search and Refinement: An Automated Framework for Gender Bias Mitigation in Large Language Models]] (86.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Gender Bias|Gender Bias]]
**⚡ Unique Technical**: [[keywords/Stereotype Content Model|Stereotype Content Model]], [[keywords/Sexual and Gender Minorities|Sexual and Gender Minorities]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.05926v3 Announce Type: replace 
Abstract: A large body of research has found substantial gender bias in NLP systems. Most of this research takes a binary, essentialist view of gender: limiting its variation to the categories _men_ and _women_, conflating gender with sex, and ignoring different sexual identities. But gender and sexuality exist on a spectrum, so in this paper we study the biases of large language models (LLMs) towards sexual and gender minorities beyond binary categories. Grounding our study in a widely used social psychology model -- the Stereotype Content Model -- we demonstrate that English-language survey questions about social perceptions elicit more negative stereotypes of sexual and gender minorities from both humans and LLMs. We then extend this framework to a more realistic use case: text generation. Our analysis shows that LLMs generate stereotyped representations of sexual and gender minorities in this setting, showing that they amplify representational harms in creative writing, a widely advertised use for LLMs.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)이 성소수자 및 젠더 소수자에 대해 갖는 편향을 연구합니다. 기존 연구는 주로 젠더를 남성과 여성으로 이분화하여 다루었으나, 본 연구는 성별과 성적 정체성이 스펙트럼 상에 있음을 강조합니다. 사회심리학의 고정관념 내용 모델을 기반으로, 성소수자에 대한 부정적 고정관념이 인간과 LLM 모두에서 나타남을 보여줍니다. 또한, 텍스트 생성이라는 현실적 사례를 통해 LLM이 성소수자에 대한 고정관념적 표현을 생성하여 창작 활동에서 표현적 해악을 증폭시킴을 분석합니다.

## 🎯 주요 포인트

- 1. 많은 연구에서 자연어 처리 시스템에 상당한 성별 편향이 존재함을 발견했으며, 대부분의 연구는 성별을 이분법적으로 바라보고 있다.
- 2. 성별과 성 정체성은 스펙트럼 상에 존재하므로, 이 논문에서는 이분법적 범주를 넘어 성적 및 성별 소수자에 대한 대형 언어 모델의 편향을 연구한다.
- 3. 연구는 사회 심리학 모델인 고정관념 내용 모델에 기반하여, 성적 및 성별 소수자에 대한 부정적 고정관념이 인간과 대형 언어 모델 모두에서 유발됨을 보여준다.
- 4. 텍스트 생성이라는 현실적인 사용 사례로 이 프레임워크를 확장하여, 대형 언어 모델이 성적 및 성별 소수자에 대한 고정관념적 표현을 생성함을 분석한다.
- 5. 대형 언어 모델은 창의적 글쓰기에서 표현적 해악을 증폭시킨다는 점을 보여준다.


---

*Generated on 2025-09-26 08:51:13*