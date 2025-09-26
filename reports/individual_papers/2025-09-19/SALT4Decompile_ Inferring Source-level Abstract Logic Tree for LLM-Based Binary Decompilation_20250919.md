---
keywords:
  - Large Language Models
  - Source-level Abstract Logic Tree
  - Obfuscation Techniques
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14646
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:26:31.617340",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Source-level Abstract Logic Tree",
    "Obfuscation Techniques"
  ],
  "rejected_keywords": [
    "Binary Decompilation"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Source-level Abstract Logic Tree": 0.75,
    "Obfuscation Techniques": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# SALT4Decompile: Inferring Source-level Abstract Logic Tree for LLM-Based Binary Decompilation

**Korean Title:** SALT4Decompile: LLM 기반 바이너리 디컴파일을 위한 소스 수준의 추상 논리 트리 추론

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Obfuscation Techniques|Obfuscation Techniques]]
**⚡ Unique Technical**: [[keywords/Source-level Abstract Logic Tree|Source-level Abstract Logic Tree]]

## 🔗 유사한 논문
- [[Do Code Semantics Help_ A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models_20250919|Do Code Semantics Help A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (80.8% similar)
- [[CodeLSI Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (79.3% similar)
- [[An LLM Agentic Approach for Legal-Critical Software A Case Study for Tax Prep Software]] (79.1% similar)
- [[MADAR Efficient Continual Learning for Malware Analysis with Distribution-Aware Replay]] (79.0% similar)
- [[BEACON Behavioral Malware Classification with Large Language Model Embeddings and Deep Learning]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14646v1 Announce Type: new 
Abstract: Decompilation is widely used in reverse engineering to recover high-level language code from binary executables. While recent approaches leveraging Large Language Models (LLMs) have shown promising progress, they typically treat assembly code as a linear sequence of instructions, overlooking arbitrary jump patterns and isolated data segments inherent to binary files. This limitation significantly hinders their ability to correctly infer source code semantics from assembly code. To address this limitation, we propose \saltm, a novel binary decompilation method that abstracts stable logical features shared between binary and source code. The core idea of \saltm is to abstract selected binary-level operations, such as specific jumps, into a high-level logic framework that better guides LLMs in semantic recovery. Given a binary function, \saltm constructs a Source-level Abstract Logic Tree (\salt) from assembly code to approximate the logic structure of high-level language. It then fine-tunes an LLM using the reconstructed \salt to generate decompiled code. Finally, the output is refined through error correction and symbol recovery to improve readability and correctness. We compare \saltm to three categories of baselines (general-purpose LLMs, commercial decompilers, and decompilation methods) using three well-known datasets (Decompile-Eval, MBPP, Exebench). Our experimental results demonstrate that \saltm is highly effective in recovering the logic of the source code, significantly outperforming state-of-the-art methods (e.g., 70.4\% TCP rate on Decompile-Eval with a 10.6\% improvement). The results further validate its robustness against four commonly used obfuscation techniques. Additionally, analyses of real-world software and a user study confirm that our decompiled output offers superior assistance to human analysts in comprehending binary functions.

## 🔍 Abstract (한글 번역)

arXiv:2509.14646v1 발표 유형: 신규  
초록: 디컴파일은 이진 실행 파일에서 고급 언어 코드를 복구하기 위해 역공학에서 널리 사용됩니다. 최근 대형 언어 모델(LLMs)을 활용한 접근 방식이 유망한 진전을 보였지만, 이들은 일반적으로 어셈블리 코드를 명령어의 선형 시퀀스로 취급하여 이진 파일에 내재된 임의의 점프 패턴과 고립된 데이터 세그먼트를 간과합니다. 이 제한은 어셈블리 코드에서 소스 코드 의미를 올바르게 추론하는 능력을 크게 저해합니다. 이 제한을 해결하기 위해, 우리는 \saltm라는 새로운 이진 디컴파일 방법을 제안합니다. 이는 이진 코드와 소스 코드 간에 공유되는 안정적인 논리적 특징을 추상화합니다. \saltm의 핵심 아이디어는 특정 점프와 같은 선택된 이진 수준의 작업을 고급 논리 프레임워크로 추상화하여 LLM이 의미 복구를 더 잘 안내하도록 하는 것입니다. 주어진 이진 함수에 대해, \saltm은 어셈블리 코드에서 소스 수준의 추상 논리 트리(\salt)를 구성하여 고급 언어의 논리 구조를 근사화합니다. 그런 다음 재구성된 \salt를 사용하여 LLM을 미세 조정하여 디컴파일된 코드를 생성합니다. 마지막으로, 출력은 오류 수정과 기호 복구를 통해 가독성과 정확성을 향상시킵니다. 우리는 세 가지 잘 알려진 데이터셋(Decompile-Eval, MBPP, Exebench)을 사용하여 세 가지 범주의 기준선(범용 LLM, 상업용 디컴파일러, 디컴파일 방법)과 \saltm을 비교합니다. 실험 결과는 \saltm이 소스 코드의 논리를 복구하는 데 매우 효과적이며, 최첨단 방법을 크게 능가함을 보여줍니다(예: Decompile-Eval에서 70.4% TCP 비율로 10.6% 향상). 결과는 또한 널리 사용되는 네 가지 난독화 기술에 대한 견고성을 추가로 검증합니다. 또한, 실제 소프트웨어 분석과 사용자 연구는 우리의 디컴파일된 출력이 이진 함수 이해에 있어 인간 분석가에게 우수한 지원을 제공함을 확인합니다.

## 📝 요약

이 논문은 이진 파일에서 고급 언어 코드를 복구하는 디컴파일링 방법을 제안합니다. 기존의 방법들은 어셈블리 코드를 선형적인 명령어 시퀀스로 처리하여 이진 파일의 점프 패턴과 데이터 세그먼트를 간과하는 한계가 있었습니다. 이를 해결하기 위해, \saltm은 이진 코드와 소스 코드 간의 안정적인 논리적 특징을 추상화하여 LLMs가 의미를 더 잘 복구할 수 있도록 돕습니다. \saltm은 어셈블리 코드에서 소스 수준의 추상 논리 트리를 구성하고, 이를 통해 LLM을 미세 조정하여 디컴파일된 코드를 생성합니다. 실험 결과, \saltm은 기존 방법들보다 높은 성능을 보였으며, 특히 Decompile-Eval 데이터셋에서 70.4%의 TCP 비율을 기록하며 10.6%의 성능 향상을 보였습니다. 또한, 실제 소프트웨어 분석 및 사용자 연구를 통해 \saltm의 디컴파일 결과가 이진 함수 이해에 큰 도움을 준다는 것을 확인했습니다.

## 🎯 주요 포인트

- 1. \saltm은 이진 파일과 소스 코드 간의 안정적인 논리적 특징을 추상화하여 고급 논리 프레임워크로 변환하는 새로운 바이너리 디컴파일 방법을 제안합니다.

- 2. \saltm은 어셈블리 코드에서 소스 수준의 추상 논리 트리(\salt)를 구성하여 고급 언어의 논리 구조를 근사하고, 이를 통해 LLM을 미세 조정하여 디컴파일된 코드를 생성합니다.

- 3. 실험 결과, \saltm은 Decompile-Eval 데이터셋에서 70.4%의 TCP 비율을 기록하며, 최첨단 방법들보다 10.6% 향상된 성능을 보였습니다.

- 4. \saltm은 네 가지 일반적인 난독화 기법에 대한 강력한 내성을 입증하였으며, 실제 소프트웨어 분석 및 사용자 연구에서 인간 분석가에게 뛰어난 지원을 제공합니다.

---

*Generated on 2025-09-19 16:41:33*