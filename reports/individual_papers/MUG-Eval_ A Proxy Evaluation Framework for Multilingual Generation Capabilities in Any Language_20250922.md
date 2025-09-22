# MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language

**Korean Title:** MUG-Eval: 모든 언어에서 다국어 생성 능력을 평가하기 위한 프록시 평가 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Proxy Evaluation Framework

## 🔗 유사한 논문
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench A Kickoff for Multilingual and Regionalized Agent Evaluation]] (86.4% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (84.7% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (84.7% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.6% similar)
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope A Dimensional Lens for Probing Cultural Understanding in LLMs]] (84.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.14395v2 Announce Type: replace-cross 
Abstract: Evaluating text generation capabilities of large language models (LLMs) is challenging, particularly for low-resource languages where methods for direct assessment are scarce. We propose MUG-Eval, a novel framework that evaluates LLMs' multilingual generation capabilities by transforming existing benchmarks into conversational tasks and measuring the LLMs' accuracies on those tasks. We specifically designed these conversational tasks to require effective communication in the target language. Then, we simply use task success rate as a proxy for successful conversation generation. Our approach offers two key advantages: it is independent of language-specific NLP tools or annotated datasets, which are limited for most languages, and it does not rely on LLMs-as-judges, whose evaluation quality degrades outside a few high-resource languages. We evaluate 8 LLMs across 30 languages spanning high, mid, and low-resource categories, and we find that MUG-Eval correlates strongly with established benchmarks ($r$ > 0.75) while enabling standardized comparisons across languages and models. Our framework provides a robust and resource-efficient solution for evaluating multilingual generation that can be extended to thousands of languages.

## 🔍 Abstract (한글 번역)

arXiv:2505.14395v2 발표 유형: 교차 교체  
초록: 대형 언어 모델(LLM)의 텍스트 생성 능력을 평가하는 것은 특히 직접 평가 방법이 드문 저자원 언어의 경우 어려운 과제입니다. 우리는 MUG-Eval이라는 새로운 프레임워크를 제안하여 기존의 벤치마크를 대화형 과제로 변환하고 이러한 과제에서 LLM의 정확도를 측정함으로써 LLM의 다국어 생성 능력을 평가합니다. 우리는 이러한 대화형 과제를 목표 언어에서 효과적인 의사소통을 요구하도록 특별히 설계했습니다. 그런 다음, 우리는 단순히 과제 성공률을 성공적인 대화 생성의 대리 지표로 사용합니다. 우리의 접근 방식은 두 가지 주요 이점을 제공합니다: 대부분의 언어에 제한적인 언어별 NLP 도구나 주석 데이터셋에 의존하지 않으며, 평가 품질이 몇몇 고자원 언어 외에서는 저하되는 LLM-판사에 의존하지 않습니다. 우리는 고자원, 중자원, 저자원 범주에 걸쳐 30개 언어에서 8개의 LLM을 평가하며, MUG-Eval이 확립된 벤치마크와 강한 상관관계($r$ > 0.75)를 가지면서도 언어와 모델 간의 표준화된 비교를 가능하게 한다는 것을 발견했습니다. 우리의 프레임워크는 수천 개의 언어로 확장할 수 있는 다국어 생성 평가를 위한 강력하고 자원 효율적인 솔루션을 제공합니다.

## 📝 요약

MUG-Eval은 대형 언어 모델(LLM)의 다국어 생성 능력을 평가하기 위한 새로운 프레임워크로, 기존 벤치마크를 대화형 과제로 변환하여 LLM의 정확도를 측정합니다. 이 방법은 언어별 NLP 도구나 주석 데이터셋에 의존하지 않으며, LLM을 평가자로 사용하는 경우보다 더 넓은 범위의 언어에서 효과적입니다. 30개의 다양한 자원 수준의 언어에서 8개의 LLM을 평가한 결과, MUG-Eval은 기존 벤치마크와 강한 상관관계($r$ > 0.75)를 보이며, 언어와 모델 간의 표준화된 비교를 가능하게 합니다. 이 프레임워크는 수천 개의 언어로 확장 가능한 강력하고 자원 효율적인 평가 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. MUG-Eval은 기존 벤치마크를 대화형 태스크로 변환하여 대형 언어 모델(LLM)의 다국어 생성 능력을 평가하는 새로운 프레임워크입니다.

- 2. 이 접근법은 대부분의 언어에 대해 제한된 언어별 NLP 도구나 주석 데이터셋에 의존하지 않으며, 평가 품질이 저하되는 LLMs-as-judges에 의존하지 않습니다.

- 3. MUG-Eval은 고자원, 중자원, 저자원 언어를 포함한 30개 언어에 걸쳐 8개의 LLM을 평가하며, 기존 벤치마크와 강한 상관관계($r$ > 0.75)를 보입니다.

- 4. 이 프레임워크는 다국어 생성 평가를 위한 강력하고 자원 효율적인 솔루션을 제공하며, 수천 개의 언어로 확장 가능합니다.

---

*Generated on 2025-09-22 14:49:04*