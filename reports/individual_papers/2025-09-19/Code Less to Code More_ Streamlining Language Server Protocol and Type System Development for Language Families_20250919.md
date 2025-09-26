---
keywords:
  - Language Server Protocol
  - Typelang
  - Modular Language Server Generation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15150
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:52:50.415945",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Language Server Protocol",
    "Typelang",
    "Modular Language Server Generation"
  ],
  "rejected_keywords": [
    "Variant-Oriented Programming"
  ],
  "similarity_scores": {
    "Language Server Protocol": 0.85,
    "Typelang": 0.78,
    "Modular Language Server Generation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Code Less to Code More: Streamlining Language Server Protocol and Type System Development for Language Families

**Korean Title:** 코드를 덜 작성하여 더 많이 작성하기: 언어 계열을 위한 언어 서버 프로토콜 및 타입 시스템 개발의 간소화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Language Server Protocol|language server protocol]]
**⚡ Unique Technical**: [[keywords/Typelang|Typelang]]
**🚀 Evolved Concepts**: [[keywords/Modular Language Server Generation|modular language server generation]]

## 🔗 유사한 논문
- [[An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (77.8% similar)
- [[Automating Modelica Module Generation Using Large Language Models A Case Study on Building Control Description Language]] (77.7% similar)
- [[Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (77.5% similar)
- [[Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System_20250918|Semantic Alignment-Enhanced Code Translation via an LLM-Based Multi-Agent System]] (77.3% similar)
- [[ReCoVeR the Target Language Language Steering without Sacrificing Task Performance]] (77.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15150v1 Announce Type: new 
Abstract: Developing editing support for $L$ languages in $E$ editors is complex and time-consuming. Some languages do not provide dedicated editors, while others offer a single native editor. The $\textit{language server protocol}$ (LSP) reduces the language-editor combinations $L \times E$ to $L + E$, where a single language server communicates with editors via LSP plugins. However, overlapping implementations of linguistic components remain an issue. Existing language workbenches struggle with modularity, reusability, and leveraging type systems for language server generation. In this work, we propose: (i) Typelang, a family of domain-specific languages for modular, composable, and reusable type system implementation, (ii) a modular language server generation process, producing servers for languages built in a modular workbench, (iii) the variant-oriented programming paradigm and a cross-artifact coordination layer to manage interdependent software variants, and (iv) an LSP plugin generator, reducing $E$ to $1$ by automating plugin creation for multiple editors. To simplify editing support for language families, each language artifact integrates its own Typelang variant, used to generate language servers. This reduces combinations to $T \times 1$, where $T = L$ represents the number of type systems. Further reuse of language artifacts across languages lowers this to $N \times 1$, where $N << T$, representing unique type systems. We implement Typelang in Neverlang, generating language servers for each artifact and LSP plugins for three editors. Empirical evaluation shows a 93.48% reduction in characters needed for type system implementation and 100% automation of LSP plugin generation, significantly lowering effort for editing support in language families, especially when artifacts are reused.

## 🔍 Abstract (한글 번역)

arXiv:2509.15150v1 발표 유형: 신규  
요약: $L$개의 언어에 대해 $E$개의 편집기에서 편집 지원을 개발하는 것은 복잡하고 시간이 많이 소요됩니다. 일부 언어는 전용 편집기를 제공하지 않으며, 다른 언어는 단일 네이티브 편집기만 제공합니다. $\textit{언어 서버 프로토콜}$ (LSP)은 언어-편집기 조합 $L \times E$를 $L + E$로 줄여주며, 단일 언어 서버가 LSP 플러그인을 통해 편집기와 통신합니다. 그러나 언어 구성 요소의 중복 구현은 여전히 문제로 남아 있습니다. 기존의 언어 작업대는 모듈성, 재사용성, 언어 서버 생성에 대한 타입 시스템 활용에 어려움을 겪고 있습니다. 본 연구에서는 다음을 제안합니다: (i) 모듈화되고 조합 가능하며 재사용 가능한 타입 시스템 구현을 위한 도메인 특화 언어 집합인 Typelang, (ii) 모듈화된 언어 작업대에서 구축된 언어에 대한 서버를 생성하는 모듈화된 언어 서버 생성 프로세스, (iii) 상호 의존적인 소프트웨어 변종을 관리하기 위한 변종 지향 프로그래밍 패러다임과 교차 아티팩트 조정 계층, (iv) 여러 편집기에 대한 플러그인 생성을 자동화하여 $E$를 $1$로 줄이는 LSP 플러그인 생성기. 언어 계열에 대한 편집 지원을 단순화하기 위해 각 언어 아티팩트는 자체 Typelang 변종을 통합하여 언어 서버를 생성하는 데 사용됩니다. 이는 조합을 $T \times 1$로 줄이며, 여기서 $T = L$은 타입 시스템의 수를 나타냅니다. 언어 간 아티팩트의 추가 재사용은 이를 $N \times 1$로 줄이며, 여기서 $N << T$는 고유한 타입 시스템을 나타냅니다. 우리는 Neverlang에서 Typelang을 구현하여 각 아티팩트에 대한 언어 서버와 세 개의 편집기에 대한 LSP 플러그인을 생성합니다. 실증 평가 결과, 타입 시스템 구현에 필요한 문자 수가 93.48% 감소하고 LSP 플러그인 생성이 100% 자동화되어, 특히 아티팩트가 재사용될 때 언어 계열의 편집 지원에 대한 노력이 크게 줄어듭니다.

## 📝 요약

이 논문은 다수의 언어와 편집기 조합을 지원하는 데 필요한 복잡성을 줄이기 위해 Typelang이라는 도메인 특화 언어 집합을 제안합니다. Typelang은 모듈화, 재사용성, 그리고 타입 시스템 구현을 강조하며, 모듈화된 언어 서버 생성 과정을 통해 다양한 언어를 지원합니다. 또한, 여러 편집기에 대한 플러그인 생성을 자동화하여 편집기 수를 하나로 줄입니다. 실험 결과, 타입 시스템 구현에 필요한 문자 수를 93.48% 줄이고, LSP 플러그인 생성을 100% 자동화하여 언어 지원 노력을 크게 감소시켰습니다.

## 🎯 주요 포인트

- 1. Typelang은 모듈성, 조합성, 재사용성을 갖춘 타입 시스템 구현을 위한 도메인 특화 언어 패밀리입니다.

- 2. 모듈형 언어 서버 생성 프로세스를 통해 모듈형 워크벤치에서 구축된 언어에 대한 서버를 생성합니다.

- 3. 변형 지향 프로그래밍 패러다임과 교차 아티팩트 조정 레이어를 통해 상호 의존적인 소프트웨어 변형을 관리합니다.

- 4. LSP 플러그인 생성기를 통해 여러 편집기에 대한 플러그인 생성을 자동화하여 $E$를 1로 줄입니다.

- 5. Typelang을 Neverlang에 구현하여 각 아티팩트에 대한 언어 서버와 세 가지 편집기에 대한 LSP 플러그인을 생성하며, 타입 시스템 구현에 필요한 문자 수를 93.48% 줄이고 LSP 플러그인 생성을 100% 자동화합니다.

---

*Generated on 2025-09-19 16:43:09*