
# Evaluating the Effectiveness of Coverage-Guided Fuzzing for Testing Deep Learning Library APIs

**Korean Title:** 딥러닝 라이브러리 API 테스트를 위한 커버리지 기반 퍼징의 효과 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Feedback Driven Synthesis

## 🔗 유사한 논문
- [[Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (79.7% similar)
- [[CodeLSI Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (78.9% similar)
- [[Protocol-Aware Firmware Rehosting for Effective Fuzzing of Embedded Network Stacks_20250918|Protocol-Aware Firmware Rehosting for Effective Fuzzing of Embedded Network Stacks]] (77.3% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (77.0% similar)
- [[A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14626v1 Announce Type: new 
Abstract: Deep Learning (DL) libraries such as PyTorch provide the core components to build major AI-enabled applications. Finding bugs in these libraries is important and challenging. Prior approaches have tackled this by performing either API-level fuzzing or model-level fuzzing, but they do not use coverage guidance, which limits their effectiveness and efficiency. This raises an intriguing question: can coverage guided fuzzing (CGF), in particular frameworks like LibFuzzer, be effectively applied to DL libraries, and does it offer meaningful improvements in code coverage, bug detection, and scalability compared to prior methods?
  We present the first in-depth study to answer this question. A key challenge in applying CGF to DL libraries is the need to create a test harness for each API that can transform byte-level fuzzer inputs into valid API inputs. To address this, we propose FlashFuzz, a technique that leverages Large Language Models (LLMs) to automatically synthesize API-level harnesses by combining templates, helper functions, and API documentation. FlashFuzz uses a feedback driven strategy to iteratively synthesize and repair harnesses. With this approach, FlashFuzz synthesizes harnesses for 1,151 PyTorch and 662 TensorFlow APIs. Compared to state-of-the-art fuzzing methods (ACETest, PathFinder, and TitanFuzz), FlashFuzz achieves up to 101.13 to 212.88 percent higher coverage and 1.0x to 5.4x higher validity rate, while also delivering 1x to 1182x speedups in input generation. FlashFuzz has discovered 42 previously unknown bugs in PyTorch and TensorFlow, 8 of which are already fixed. Our study confirms that CGF can be effectively applied to DL libraries and provides a strong baseline for future testing approaches.

## 🔍 Abstract (한글 번역)

arXiv:2509.14626v1 발표 유형: 신규  
초록: PyTorch와 같은 딥러닝(DL) 라이브러리는 주요 AI 기반 애플리케이션을 구축하는 핵심 구성 요소를 제공합니다. 이러한 라이브러리에서 버그를 찾는 것은 중요하면서도 도전적인 과제입니다. 이전 접근 방식은 API 수준 퍼징 또는 모델 수준 퍼징을 수행하여 이 문제를 해결했지만, 커버리지 지침을 사용하지 않아 그 효과성과 효율성이 제한되었습니다. 이는 흥미로운 질문을 제기합니다: 커버리지 지침 퍼징(CGF), 특히 LibFuzzer와 같은 프레임워크가 DL 라이브러리에 효과적으로 적용될 수 있으며, 이전 방법에 비해 코드 커버리지, 버그 탐지 및 확장성에서 의미 있는 개선을 제공할 수 있을까요?  
우리는 이 질문에 답하기 위한 최초의 심층 연구를 제시합니다. DL 라이브러리에 CGF를 적용하는 주요 과제는 바이트 수준 퍼저 입력을 유효한 API 입력으로 변환할 수 있는 각 API에 대한 테스트 하네스를 생성해야 한다는 점입니다. 이를 해결하기 위해 우리는 FlashFuzz라는 기술을 제안합니다. 이는 대형 언어 모델(LLM)을 활용하여 템플릿, 도우미 함수 및 API 문서를 결합하여 API 수준 하네스를 자동으로 합성합니다. FlashFuzz는 피드백 기반 전략을 사용하여 하네스를 반복적으로 합성하고 수정합니다. 이 접근 방식으로 FlashFuzz는 1,151개의 PyTorch 및 662개의 TensorFlow API에 대한 하네스를 합성합니다. 최첨단 퍼징 방법(ACETest, PathFinder, TitanFuzz)과 비교했을 때, FlashFuzz는 최대 101.13%에서 212.88% 더 높은 커버리지와 1.0배에서 5.4배 더 높은 유효성 비율을 달성하며, 입력 생성에서 1배에서 1182배의 속도 향상을 제공합니다. FlashFuzz는 PyTorch와 TensorFlow에서 이전에 알려지지 않은 42개의 버그를 발견했으며, 이 중 8개는 이미 수정되었습니다. 우리의 연구는 CGF가 DL 라이브러리에 효과적으로 적용될 수 있음을 확인하고, 향후 테스트 접근 방식에 대한 강력한 기준을 제공합니다.

## 📝 요약

이 논문은 딥러닝 라이브러리의 버그 탐지를 위한 새로운 접근법인 FlashFuzz를 제안합니다. 기존의 API 및 모델 수준 퍼징 기법은 코드 커버리지와 효율성에 한계가 있었으나, FlashFuzz는 커버리지 유도 퍼징(CGF)을 활용하여 이를 개선합니다. FlashFuzz는 대형 언어 모델(LLM)을 사용해 API 수준의 테스트 하네스를 자동으로 생성하며, PyTorch와 TensorFlow의 총 1,813개 API에 대해 적용되었습니다. 이 방법은 기존 퍼징 기법보다 최대 212.88% 높은 커버리지와 5.4배 높은 유효성을 달성했으며, 42개의 새로운 버그를 발견했습니다. 이 연구는 CGF가 딥러닝 라이브러리에 효과적으로 적용될 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. 딥러닝 라이브러리에 대한 커버리지 기반 퍼징(CGF)의 효과적인 적용 가능성을 탐구한 최초의 심층 연구를 제시합니다.

- 2. FlashFuzz는 대형 언어 모델(LLM)을 활용하여 API 문서와 템플릿을 결합해 API 수준의 테스트 하네스를 자동으로 생성합니다.

- 3. FlashFuzz는 최신 퍼징 방법들에 비해 최대 212.88% 높은 커버리지와 최대 5.4배 높은 유효성 비율을 달성합니다.

- 4. FlashFuzz는 PyTorch와 TensorFlow에서 42개의 새로운 버그를 발견했으며, 그 중 8개는 이미 수정되었습니다.

- 5. 본 연구는 CGF가 딥러닝 라이브러리에 효과적으로 적용될 수 있음을 확인하고, 향후 테스트 접근법을 위한 강력한 기준점을 제공합니다.

---

*Generated on 2025-09-19 16:41:05*