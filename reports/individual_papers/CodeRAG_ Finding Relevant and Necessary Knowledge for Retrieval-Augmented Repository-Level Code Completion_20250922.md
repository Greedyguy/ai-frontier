# CodeRAG: Finding Relevant and Necessary Knowledge for Retrieval-Augmented Repository-Level Code Completion

**Korean Title:** CodeRAG: 검색 증강형 저장소 수준 코드 완성을 위한 관련 및 필수 지식 찾기

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Retrieval-Augmented Code Completion|Retrieval-Augmented Code Completion]] [[keywords/specific/Multi-path Code Retrieval|Multi-path Code Retrieval]] [[keywords/broad/Code Large Language Models|Code Large Language Models]] [[keywords/unique/CodeRAG|CodeRAG]] [[categories/cs.CL|cs.CL]] [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (86.0% similar) [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (85.7% similar) [[2025-09-22/RPG_ A Repository Planning Graph for Unified and Scalable Codebase Generation_20250922|RPG: A Repository Planning Graph for Unified and Scalable Codebase Generation]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Retrieval-Augmented Code Completion
**🔗 Specific Connectable**: Multi-path Code Retrieval
**🔬 Broad Technical**: Code Large Language Models
**⭐ Unique Technical**: CodeRAG
## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (86.0% similar)
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (85.7% similar)
- [[2025-09-22/RPG_ A Repository Planning Graph for Unified and Scalable Codebase Generation_20250922|RPG A Repository Planning Graph for Unified and Scalable Codebase Generation]] (84.1% similar)
- [[2025-09-19/Engineering RAG Systems for Real-World Applications_ Design, Development, and Evaluation_20250919|Engineering RAG Systems for Real-World Applications Design, Development, and Evaluation]] (84.1% similar)
- [[2025-09-18/KGCompass_ Knowledge Graph Enhanced Repository-Level Software Repair_20250918|KGCompass Knowledge Graph Enhanced Repository-Level Software Repair]] (83.2% similar)


**ArXiv ID**: [2509.16112](https://arxiv.org/abs/2509.16112)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.16112.pdf)


**ArXiv ID**: [2509.16112](https://arxiv.org/abs/2509.16112)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.16112.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Retrieval-augmented Repository-level Code Completion
**🔗 Specific Connectable**: Multi-path Code Retrieval
**⭐ Unique Technical**: CodeRAG
**🔬 Broad Technical**: Code Large Language Models

## 🏷️ 추출된 키워드



`Code Large Language Models` • 

`Multi-path Code Retrieval` • 

`CodeRAG` • 

`Retrieval-Augmented Repository-Level Code Completion`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16112v1 Announce Type: new 
Abstract: Repository-level code completion automatically predicts the unfinished code based on the broader information from the repository. Recent strides in Code Large Language Models (code LLMs) have spurred the development of repository-level code completion methods, yielding promising results. Nevertheless, they suffer from issues such as inappropriate query construction, single-path code retrieval, and misalignment between code retriever and code LLM. To address these problems, we introduce CodeRAG, a framework tailored to identify relevant and necessary knowledge for retrieval-augmented repository-level code completion. Its core components include log probability guided query construction, multi-path code retrieval, and preference-aligned BestFit reranking. Extensive experiments on benchmarks ReccEval and CCEval demonstrate that CodeRAG significantly and consistently outperforms state-of-the-art methods. The implementation of CodeRAG is available at https://github.com/KDEGroup/CodeRAG.

## 🔍 Abstract (한글 번역)

arXiv:2509.16112v1 발표 유형: 신규  
초록: 리포지토리 수준의 코드 완성은 리포지토리로부터의 광범위한 정보를 기반으로 미완성 코드를 자동으로 예측합니다. 최근 코드 대형 언어 모델(Code Large Language Models, code LLMs)의 발전은 리포지토리 수준의 코드 완성 방법의 개발을 촉진하여 유망한 결과를 도출했습니다. 그럼에도 불구하고, 부적절한 쿼리 구성, 단일 경로 코드 검색, 코드 검색기와 코드 LLM 간의 불일치와 같은 문제를 겪고 있습니다. 이러한 문제를 해결하기 위해, 우리는 검색 증강 리포지토리 수준 코드 완성을 위한 관련되고 필요한 지식을 식별하는 데 특화된 프레임워크인 CodeRAG를 소개합니다. 그 핵심 구성 요소는 로그 확률 기반 쿼리 구성, 다중 경로 코드 검색, 선호도 정렬 BestFit 재정렬을 포함합니다. ReccEval 및 CCEval 벤치마크에 대한 광범위한 실험은 CodeRAG가 최첨단 방법들을 상당히 그리고 일관되게 능가함을 보여줍니다. CodeRAG의 구현은 https://github.com/KDEGroup/CodeRAG에서 이용할 수 있습니다.

## 📝 요약

이 논문은 저장소 수준의 코드 자동 완성 문제를 해결하기 위해 CodeRAG라는 새로운 프레임워크를 제안합니다. 기존 방법들이 부적절한 쿼리 생성, 단일 경로 코드 검색, 코드 검색기와 코드 LLM 간의 불일치 문제를 겪는 반면, CodeRAG는 로그 확률 기반 쿼리 생성, 다중 경로 코드 검색, 선호도 정렬 BestFit 재정렬을 통해 이를 개선합니다. ReccEval과 CCEval 벤치마크 실험에서 CodeRAG는 최신 방법들보다 뛰어난 성능을 보였습니다. CodeRAG의 구현은 GitHub에서 제공됩니다.

## 🎯 주요 포인트


- 1. 저장소 수준의 코드 완성은 저장소의 광범위한 정보를 기반으로 미완성 코드를 자동으로 예측합니다.

- 2. 기존 코드 LLMs의 발전은 저장소 수준 코드 완성 방법의 개발을 촉진했지만, 부적절한 쿼리 구성 등 몇 가지 문제점이 존재합니다.

- 3. CodeRAG는 검색 증강 저장소 수준 코드 완성을 위한 프레임워크로, 로그 확률 기반 쿼리 구성, 다중 경로 코드 검색, 및 선호도 정렬 BestFit 재정렬을 포함합니다.

- 4. CodeRAG는 ReccEval 및 CCEval 벤치마크에서 최첨단 방법들보다 성능이 뛰어남을 입증했습니다.

- 5. CodeRAG의 구현은 https://github.com/KDEGroup/CodeRAG에서 확인할 수 있습니다.


---

*Generated on 2025-09-22 16:29:44*