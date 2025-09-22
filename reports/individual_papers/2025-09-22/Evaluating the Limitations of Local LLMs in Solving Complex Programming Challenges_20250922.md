# Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges

**Korean Title:** 복잡한 프로그래밍 문제 해결에서 지역 LLM의 한계 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: AI-driven Code Generation Evaluation

## 🔗 유사한 논문
- [[2025-09-19/Automating Modelica Module Generation Using Large Language Models_ A Case Study on Building Control Description Language_20250919|Automating Modelica Module Generation Using Large Language Models A Case Study on Building Control Description Language]] (84.4% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (83.6% similar)
- [[2025-09-18/An LLM Agentic Approach for Legal-Critical Software_ A Case Study for Tax Prep Software_20250918|An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (83.4% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (83.2% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO A Framework for Confidence-Aware Routing of Large Language Models]] (83.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15283v1 Announce Type: cross 
Abstract: This study examines the performance of today's open-source, locally hosted large-language models (LLMs) in handling complex competitive programming tasks with extended problem descriptions and contexts. Building on the original Framework for AI-driven Code Generation Evaluation (FACE), the authors retrofit the pipeline to work entirely offline through the Ollama runtime, collapsing FACE's sprawling per-problem directory tree into a handful of consolidated JSON files, and adding robust checkpointing so multi-day runs can resume after failures. The enhanced framework generates, submits, and records solutions for the full Kattis corpus of 3,589 problems across eight code-oriented models ranging from 6.7-9 billion parameters. The submission results show that the overall pass@1 accuracy is modest for the local models, with the best models performing at approximately half the acceptance rate of the proprietary models, Gemini 1.5 and ChatGPT-4. These findings expose a persistent gap between private, cost-controlled LLM deployments and state-of-the-art proprietary services, yet also highlight the rapid progress of open models and the practical benefits of an evaluation workflow that organizations can replicate on in-house hardware.

## 🔍 Abstract (한글 번역)

arXiv:2509.15283v1 발표 유형: 교차  
초록: 이 연구는 오늘날의 오픈 소스, 로컬 호스팅 대형 언어 모델(LLM)이 확장된 문제 설명과 맥락을 가진 복잡한 경쟁 프로그래밍 작업을 처리하는 성능을 조사합니다. AI 기반 코드 생성 평가를 위한 원래의 프레임워크(FACE)를 기반으로, 저자들은 Ollama 런타임을 통해 파이프라인을 완전히 오프라인으로 작동하도록 개조하고, FACE의 방대한 문제별 디렉토리 트리를 소수의 통합된 JSON 파일로 축소하며, 다일간의 실행이 실패 후에도 재개될 수 있도록 강력한 체크포인팅을 추가했습니다. 향상된 프레임워크는 6.7-9억 개의 매개변수를 갖춘 8개의 코드 지향 모델에 걸쳐 3,589개의 문제로 구성된 전체 Kattis 코퍼스에 대한 솔루션을 생성, 제출 및 기록합니다. 제출 결과는 로컬 모델의 전체 pass@1 정확도가 보통 수준임을 보여주며, 최고의 모델은 Gemini 1.5 및 ChatGPT-4와 같은 독점 모델의 수용률의 약 절반 수준으로 수행됩니다. 이러한 결과는 사설, 비용 통제된 LLM 배포와 최첨단 독점 서비스 간의 지속적인 격차를 드러내지만, 또한 오픈 모델의 빠른 발전과 조직이 자체 하드웨어에서 복제할 수 있는 평가 워크플로의 실질적인 이점을 강조합니다.

## 📝 요약

이 연구는 오늘날의 오픈 소스, 로컬 호스팅 대형 언어 모델(LLM)이 복잡한 경쟁 프로그래밍 과제를 처리하는 성능을 평가합니다. AI 기반 코드 생성 평가 프레임워크(FACE)를 기반으로, Ollama 런타임을 통해 오프라인에서 작동하도록 파이프라인을 개조하고, JSON 파일로 통합하여 효율성을 높였습니다. 6.7-9억 매개변수의 8개 코드 지향 모델을 사용하여 Kattis의 3,589개 문제에 대한 솔루션을 생성, 제출, 기록했습니다. 결과적으로 로컬 모델의 pass@1 정확도는 다소 낮으며, 최고의 모델도 Gemini 1.5와 ChatGPT-4의 절반 수준에 그쳤습니다. 이는 사설 모델과 최신 독점 서비스 간의 격차를 보여주지만, 오픈 모델의 빠른 발전과 자체 하드웨어에서 평가 워크플로우를 복제할 수 있는 실용적 이점을 강조합니다.

## 🎯 주요 포인트

- 1. 본 연구는 복잡한 경쟁 프로그래밍 과제를 처리하는 데 있어 오픈 소스, 로컬 호스팅 대형 언어 모델(LLMs)의 성능을 평가합니다.

- 2. 연구진은 FACE 프레임워크를 오프라인에서 완전히 작동하도록 개조하여 Ollama 런타임을 통해 문제별 디렉토리 구조를 통합된 JSON 파일로 축소하고, 견고한 체크포인트 기능을 추가했습니다.

- 3. 연구 결과, 로컬 모델의 전체 pass@1 정확도는 보통 수준이며, 최고 성능 모델도 Gemini 1.5 및 ChatGPT-4와 같은 독점 모델의 절반 정도의 수용률을 보였습니다.

- 4. 이러한 결과는 사설 LLM 배포와 최첨단 독점 서비스 간의 지속적인 격차를 드러내지만, 오픈 모델의 빠른 발전과 조직이 자체 하드웨어에서 복제할 수 있는 평가 워크플로의 실질적 이점을 강조합니다.

---

*Generated on 2025-09-22 13:52:55*