# Do Large Language Models Understand Word Senses?

**Korean Title:** 대형 언어 모델은 단어의 의미를 이해하는가?

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Domenico Meconi|Domenico Meconi]] [[authors/Simone Stirpe|Simone Stirpe]] [[authors/Federico Martelli|Federico Martelli]] [[authors/Leonardo Lavalle|Leonardo Lavalle]] [[authors/Roberto Navigli|Roberto Navigli]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Instruction-tuned LLMs

## 🔗 유사한 논문
- [[Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (85.0% similar)
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (84.7% similar)
- [[Correct-Detect_ Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs_20250917|Correct-Detect Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs]] (84.1% similar)
- [[From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy A Survey on Large Language Models in Scientific Discovery]] (83.9% similar)
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (83.8% similar)

## 📋 저자 정보

**Authors:** Domenico Meconi, Simone Stirpe, Federico Martelli, Leonardo Lavalle, Roberto Navigli

## 📄 Abstract (원문)

Understanding the meaning of words in context is a fundamental capability for
Large Language Models (LLMs). Despite extensive evaluation efforts, the extent
to which LLMs show evidence that they truly grasp word senses remains
underexplored. In this paper, we address this gap by evaluating both i) the
Word Sense Disambiguation (WSD) capabilities of instruction-tuned LLMs,
comparing their performance to state-of-the-art systems specifically designed
for the task, and ii) the ability of two top-performing open- and closed-source
LLMs to understand word senses in three generative settings: definition
generation, free-form explanation, and example generation. Notably, we find
that, in the WSD task, leading models such as GPT-4o and DeepSeek-V3 achieve
performance on par with specialized WSD systems, while also demonstrating
greater robustness across domains and levels of difficulty. In the generation
tasks, results reveal that LLMs can explain the meaning of words in context up
to 98\% accuracy, with the highest performance observed in the free-form
explanation task, which best aligns with their generative capabilities.

## 🔍 Abstract (한글 번역)

단어의 의미를 문맥에서 이해하는 것은 대형 언어 모델(LLM)의 기본적인 능력입니다. 광범위한 평가 노력에도 불구하고, LLM이 실제로 단어의 의미를 진정으로 이해하고 있다는 증거를 어느 정도 보여주는지는 아직 충분히 탐구되지 않았습니다. 이 논문에서는 i) 지시 조정된 LLM의 단어 의미 중의성 해소(WSD) 능력을 평가하여, 이 작업을 위해 특별히 설계된 최첨단 시스템과의 성능을 비교하고, ii) 정의 생성, 자유 형식 설명, 예제 생성의 세 가지 생성 설정에서 두 개의 최고 성능을 보이는 오픈 소스 및 클로즈드 소스 LLM이 단어의 의미를 이해하는 능력을 평가함으로써 이 격차를 해결합니다. 주목할 만한 점은, WSD 작업에서 GPT-4o 및 DeepSeek-V3와 같은 선도적인 모델이 전문화된 WSD 시스템과 동등한 성능을 달성하면서도, 도메인 및 난이도 수준에 걸쳐 더 큰 견고성을 보여준다는 것입니다. 생성 작업에서는 LLM이 문맥에서 단어의 의미를 최대 98% 정확도로 설명할 수 있으며, 이들의 생성 능력과 가장 잘 맞는 자유 형식 설명 작업에서 가장 높은 성능이 관찰되었습니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 문맥 내 단어 의미 이해 능력을 평가합니다. 연구는 두 가지 측면에서 진행되었습니다. 첫째, 명령 조정된 LLM의 단어 의미 중의성 해소(WSD) 능력을 평가하여, 이들이 해당 작업에 특화된 최첨단 시스템과 비교했을 때 유사한 성능을 보임을 확인했습니다. 특히, GPT-4o와 DeepSeek-V3 모델은 다양한 도메인과 난이도에서 높은 견고성을 나타냈습니다. 둘째, 두 개의 LLM이 정의 생성, 자유 형식 설명, 예시 생성의 세 가지 생성 설정에서 단어 의미를 이해하는 능력을 평가했습니다. 결과적으로, 자유 형식 설명 작업에서 최고 성능을 보이며, 문맥 내 단어 의미를 최대 98%의 정확도로 설명할 수 있음을 발견했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 문맥에서 단어의 의미를 이해하는 능력이 중요하다.

- 2. LLM의 단어 의미 구별(WSD) 능력은 전문 시스템과 비슷한 수준의 성능을 보인다.

- 3. GPT-4o와 DeepSeek-V3는 다양한 도메인과 난이도에서 뛰어난 견고성을 보인다.

- 4. LLM은 단어의 의미를 설명하는 생성 작업에서 최대 98%의 정확도를 달성한다.

- 5. 자유 형식 설명 작업에서 LLM의 생성 능력이 가장 잘 발휘된다.

---

*Generated on 2025-09-20 09:25:13*