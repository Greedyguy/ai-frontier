---
keywords:
  - Large Language Model
  - Retrieval-Augmented Code Completion
  - Multi-path Code Retrieval
  - BestFit Reranking
  - Retrieval Augmented Generation
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2509.16112
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:36:22.496369",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval-Augmented Code Completion",
    "Multi-path Code Retrieval",
    "BestFit Reranking",
    "Retrieval Augmented Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.82,
    "Retrieval-Augmented Code Completion": 0.78,
    "Multi-path Code Retrieval": 0.75,
    "BestFit Reranking": 0.73,
    "Retrieval Augmented Generation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Code Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "Code LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion on code completion, providing a strong link to existing research in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.87,
        "specificity_score": 0.68,
        "link_intent_score": 0.82
      },
      {
        "surface": "Retrieval-Augmented Repository-Level Code Completion",
        "canonical": "Retrieval-Augmented Code Completion",
        "aliases": [
          "Repository-Level Code Completion"
        ],
        "category": "unique_technical",
        "rationale": "This concept is unique to the paper and represents a novel approach to code completion, enhancing its novelty and specificity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-path Code Retrieval",
        "canonical": "Multi-path Code Retrieval",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique addresses specific issues in code retrieval, offering a unique method that can be linked to improvements in code completion.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.79,
        "link_intent_score": 0.75
      },
      {
        "surface": "Preference-aligned BestFit Reranking",
        "canonical": "BestFit Reranking",
        "aliases": [
          "Preference-aligned Reranking"
        ],
        "category": "unique_technical",
        "rationale": "This reranking method is a novel contribution of the paper, enhancing the specificity and novelty of the retrieval process.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.77,
        "link_intent_score": 0.73
      },
      {
        "surface": "Retrieval Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept that connects well with the retrieval-augmented methods discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
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
      "candidate_surface": "Code Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.87,
        "specificity": 0.68,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Repository-Level Code Completion",
      "resolved_canonical": "Retrieval-Augmented Code Completion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-path Code Retrieval",
      "resolved_canonical": "Multi-path Code Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.79,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Preference-aligned BestFit Reranking",
      "resolved_canonical": "BestFit Reranking",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.77,
        "link_intent": 0.73
      }
    },
    {
      "candidate_surface": "Retrieval Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion

**Korean Title:** CodeRAG: 검색 증강 저장소 수준 코드 완성을 위한 관련 및 필수 지식 찾기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16112.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2509.16112](https://arxiv.org/abs/2509.16112)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (86.0% similar)
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (85.7% similar)
- [[2025-09-22/RPG_ A Repository Planning Graph for Unified and Scalable Codebase Generation_20250922|RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation]] (84.1% similar)
- [[2025-09-19/Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications: Design, Development, and Evaluation]] (84.1% similar)
- [[2025-09-18/KGCompass_ Knowledge Graph Enhanced Repository-Level Software Repair_20250918|KGCompass: Knowledge Graph Enhanced Repository-Level Software Repair]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Retrieval-Augmented Code Completion|Retrieval-Augmented Code Completion]], [[keywords/Multi-path Code Retrieval|Multi-path Code Retrieval]], [[keywords/BestFit Reranking|BestFit Reranking]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16112v1 Announce Type: new 
Abstract: Repository-level code completion automatically predicts the unfinished code based on the broader information from the repository. Recent strides in Code Large Language Models (code LLMs) have spurred the development of repository-level code completion methods, yielding promising results. Nevertheless, they suffer from issues such as inappropriate query construction, single-path code retrieval, and misalignment between code retriever and code LLM. To address these problems, we introduce CodeRAG, a framework tailored to identify relevant and necessary knowledge for retrieval-augmented repository-level code completion. Its core components include log probability guided query construction, multi-path code retrieval, and preference-aligned BestFit reranking. Extensive experiments on benchmarks ReccEval and CCEval demonstrate that CodeRAG significantly and consistently outperforms state-of-the-art methods. The implementation of CodeRAG is available at https://github.com/KDEGroup/CodeRAG.

## 🔍 Abstract (한글 번역)

arXiv:2509.16112v1 발표 유형: 신규  
초록: 저장소 수준의 코드 완성은 저장소의 광범위한 정보를 기반으로 미완성 코드를 자동으로 예측합니다. 최근 코드 대형 언어 모델(Code LLMs)의 발전은 저장소 수준의 코드 완성 방법 개발을 촉진하여 유망한 결과를 가져왔습니다. 그럼에도 불구하고, 부적절한 쿼리 구성, 단일 경로 코드 검색, 코드 검색기와 코드 LLM 간의 불일치와 같은 문제를 겪고 있습니다. 이러한 문제를 해결하기 위해, 우리는 검색 보강 저장소 수준 코드 완성을 위한 관련 및 필수 지식을 식별하도록 설계된 프레임워크인 CodeRAG를 소개합니다. CodeRAG의 핵심 구성 요소는 로그 확률 기반 쿼리 구성, 다중 경로 코드 검색, 그리고 선호도에 맞춘 BestFit 재정렬을 포함합니다. ReccEval과 CCEval 벤치마크에 대한 광범위한 실험은 CodeRAG가 최첨단 방법들을 상당히 그리고 일관되게 능가함을 보여줍니다. CodeRAG의 구현은 https://github.com/KDEGroup/CodeRAG에서 이용할 수 있습니다.

## 📝 요약

이 논문은 저장소 수준의 코드 자동 완성을 위한 새로운 프레임워크인 CodeRAG를 소개합니다. 기존의 코드 대형 언어 모델(Code LLMs)은 부적절한 쿼리 구성, 단일 경로 코드 검색, 코드 검색기와 코드 LLM 간의 불일치 문제를 가지고 있었습니다. CodeRAG는 로그 확률 기반 쿼리 구성, 다중 경로 코드 검색, 선호도 정렬 BestFit 재정렬을 통해 이러한 문제를 해결합니다. 실험 결과, CodeRAG는 ReccEval 및 CCEval 벤치마크에서 기존 최첨단 방법들을 뛰어넘는 성능을 보였습니다. CodeRAG의 구현은 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. CodeRAG는 저장소 수준의 코드 완성을 위한 검색 보강 프레임워크로, 관련 지식 식별에 중점을 둡니다.
- 2. CodeRAG는 로그 확률 기반 쿼리 생성, 다중 경로 코드 검색, 선호도 정렬 BestFit 재정렬을 핵심 구성 요소로 포함합니다.
- 3. ReccEval 및 CCEval 벤치마크 실험에서 CodeRAG는 최신 방법들을 능가하는 성능을 보여줍니다.
- 4. CodeRAG의 구현 코드는 https://github.com/KDEGroup/CodeRAG에서 확인할 수 있습니다.


---

*Generated on 2025-09-23 11:36:22*