---
keywords:
  - Large Language Model
  - Multilingual Dialogue Evaluation
  - Open-Domain Dialogue
  - Meta-Evaluation Benchmark
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2505.22777
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:47:30.519637",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multilingual Dialogue Evaluation",
    "Open-Domain Dialogue",
    "Meta-Evaluation Benchmark"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multilingual Dialogue Evaluation": 0.78,
    "Open-Domain Dialogue": 0.8,
    "Meta-Evaluation Benchmark": 0.72
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
        "rationale": "Large Language Models are central to the paper's framework and evaluation process.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multilingual Dialogue Evaluation",
        "canonical": "Multilingual Dialogue Evaluation",
        "aliases": [
          "multilingual evaluation",
          "cross-lingual evaluation"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a new benchmark specifically focused on multilingual dialogue evaluation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Open-Domain Dialogue",
        "canonical": "Open-Domain Dialogue",
        "aliases": [
          "open-domain chat",
          "open dialogue"
        ],
        "category": "specific_connectable",
        "rationale": "Open-domain dialogue is a key focus of the evaluation framework introduced in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Meta-Evaluation Benchmark",
        "canonical": "Meta-Evaluation Benchmark",
        "aliases": [
          "evaluation benchmark",
          "meta-evaluation"
        ],
        "category": "unique_technical",
        "rationale": "The paper proposes a new meta-evaluation benchmark to improve dialogue evaluation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multilingual Dialogue Evaluation",
      "resolved_canonical": "Multilingual Dialogue Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Open-Domain Dialogue",
      "resolved_canonical": "Open-Domain Dialogue",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Meta-Evaluation Benchmark",
      "resolved_canonical": "Meta-Evaluation Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators

**Korean Title:** MEDAL: 다국어 오픈 도메인 대화 평가자로서 대형 언어 모델(LLM)을 벤치마킹하기 위한 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.22777.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2505.22777](https://arxiv.org/abs/2505.22777)

## 🔗 유사한 논문
- [[2025-09-22/MUG-Eval_ A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language_20250922|MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language]] (87.3% similar)
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation]] (86.3% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (85.6% similar)
- [[2025-09-19/Judging with Many Minds_ Do More Perspectives Mean Less Prejudice? On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge_20250919|Judging with Many Minds: Do More Perspectives Mean Less Prejudice? On Bias Amplifications and Resistance in Multi-Agent Based LLM-as-Judge]] (85.3% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (85.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Open-Domain Dialogue|Open-Domain Dialogue]]
**⚡ Unique Technical**: [[keywords/Multilingual Dialogue Evaluation|Multilingual Dialogue Evaluation]], [[keywords/Meta-Evaluation Benchmark|Meta-Evaluation Benchmark]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.22777v3 Announce Type: replace 
Abstract: Evaluating the quality of open-domain chatbots has become increasingly reliant on LLMs acting as automatic judges. However, existing meta-evaluation benchmarks are static, outdated, and lacking in multilingual coverage, limiting their ability to fully capture subtle weaknesses in evaluation. We introduce MEDAL, an automated multi-agent framework for curating more representative and diverse open-domain dialogue evaluation benchmarks. Our approach leverages several state-of-the-art LLMs to generate user-chatbot multilingual dialogues, conditioned on varied seed contexts. Then, a strong LLM (GPT-4.1) is used for a multidimensional analysis of the performance of the chatbots, uncovering noticeable cross-lingual performance differences. Guided by this large-scale evaluation, we curate a new meta-evaluation multilingual benchmark and human-annotate samples with nuanced quality judgments. This benchmark is then used to assess the ability of several reasoning and non-reasoning LLMs to act as evaluators of open-domain dialogues. Using MEDAL, we uncover that state-of-the-art judges fail to reliably detect nuanced issues such as lack of empathy, commonsense, or relevance.

## 🔍 Abstract (한글 번역)

arXiv:2505.22777v3 발표 유형: 교체  
초록: 오픈 도메인 챗봇의 품질 평가가 점점 더 자동 심판 역할을 하는 대형 언어 모델(LLM)에 의존하게 되었습니다. 그러나 기존의 메타 평가 벤치마크는 정적이고, 구식이며, 다국어 범위가 부족하여 평가에서 미세한 약점을 완전히 포착하는 데 한계가 있습니다. 우리는 보다 대표적이고 다양한 오픈 도메인 대화 평가 벤치마크를 큐레이팅하기 위한 자동화된 다중 에이전트 프레임워크인 MEDAL을 소개합니다. 우리의 접근 방식은 여러 최첨단 LLM을 활용하여 다양한 시드 컨텍스트에 기반한 사용자-챗봇 다국어 대화를 생성합니다. 그런 다음 강력한 LLM(GPT-4.1)을 사용하여 챗봇의 성능을 다차원적으로 분석하여 눈에 띄는 언어 간 성능 차이를 발견합니다. 이 대규모 평가를 통해 우리는 새로운 메타 평가 다국어 벤치마크를 큐레이팅하고, 미묘한 품질 판단으로 인간 주석을 추가합니다. 이 벤치마크는 여러 추론 및 비추론 LLM이 오픈 도메인 대화의 평가자로서의 능력을 평가하는 데 사용됩니다. MEDAL을 사용하여 우리는 최첨단 심판이 공감 부족, 상식 부족 또는 관련성 부족과 같은 미묘한 문제를 신뢰성 있게 감지하지 못한다는 것을 발견합니다.

## 📝 요약

이 논문은 오픈 도메인 챗봇의 평가에서 LLM(대형 언어 모델)의 자동 평가자 역할에 대한 한계를 지적하고, 이를 개선하기 위해 MEDAL이라는 자동화된 다중 에이전트 프레임워크를 제안합니다. MEDAL은 다양한 최첨단 LLM을 활용하여 다국어 사용자-챗봇 대화를 생성하고, 이를 통해 챗봇 성능의 다차원 분석을 수행합니다. 특히, GPT-4.1을 사용하여 언어 간 성능 차이를 발견하고, 이를 바탕으로 새로운 다국어 메타 평가 벤치마크를 구축합니다. 이 벤치마크는 여러 LLM의 평가자로서의 능력을 검증하는 데 사용되며, MEDAL을 통해 최신 평가자들이 공감 부족, 상식 결여, 관련성 부족 등의 미묘한 문제를 신뢰성 있게 감지하지 못한다는 점을 밝혀냅니다.

## 🎯 주요 포인트

- 1. 기존의 메타 평가 벤치마크는 정적이고 오래되었으며 다국어 지원이 부족하여 평가의 미묘한 약점을 완전히 포착하지 못한다.
- 2. MEDAL은 다양한 오픈 도메인 대화 평가 벤치마크를 생성하기 위한 자동화된 다중 에이전트 프레임워크이다.
- 3. 최신 LLM들을 활용하여 다국어 사용자-챗봇 대화를 생성하고, GPT-4.1을 사용해 챗봇의 성능을 다차원적으로 분석한다.
- 4. 대규모 평가를 통해 새로운 메타 평가 다국어 벤치마크를 만들고, 인간이 세심한 품질 판단으로 샘플을 주석한다.
- 5. MEDAL을 통해 최신 심판들이 공감 부족, 상식 부족, 관련성 부족과 같은 미묘한 문제를 신뢰성 있게 감지하지 못한다는 것을 발견한다.


---

*Generated on 2025-09-23 11:47:30*