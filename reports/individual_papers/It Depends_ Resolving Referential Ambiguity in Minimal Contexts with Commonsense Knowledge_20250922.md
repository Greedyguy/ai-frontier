# It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge

**Korean Title:** 의존성: 상식 지식을 활용한 최소한의 문맥에서의 지시적 모호성 해결

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Direct Preference Optimization|Direct Preference Optimization]] [[keywords/specific/Multilingual Evaluation|Multilingual Evaluation]] [[keywords/broad/Commonsense Knowledge|Commonsense Knowledge]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/unique/DeepSeek v3|DeepSeek v3]] [[categories/cs.CL|cs.CL]] [[2025-09-17/Correct-Detect_ Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs_20250917|Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs]] (88.3% similar) [[2025-09-17/Do Large Language Models Understand Word Senses_20250917|Do Large Language Models Understand Word Senses?]] (87.5% similar) [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (87.4% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Direct Preference Optimization
**🔗 Specific Connectable**: Multilingual Evaluation
**🔬 Broad Technical**: Large Language Models, Commonsense Knowledge
**⭐ Unique Technical**: DeepSeek v3
## 🔗 유사한 논문
- [[2025-09-17/Correct-Detect_ Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs_20250917|Correct-Detect Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs]] (88.3% similar)
- [[2025-09-17/Do Large Language Models Understand Word Senses_20250917|Do Large Language Models Understand Word Senses]] (87.5% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM Language of Browsing]] (87.4% similar)
- [[2025-09-22/Do Retrieval Augmented Language Models Know When They Don't Know_20250922|Do Retrieval Augmented Language Models Know When They Don't Know]] (86.5% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (86.4% similar)


**ArXiv ID**: [2509.16107](https://arxiv.org/abs/2509.16107)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.16107.pdf)


**ArXiv ID**: [2509.16107](https://arxiv.org/abs/2509.16107)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.16107.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Direct Preference Optimization
**🔗 Specific Connectable**: Multilingual Evaluation
**⭐ Unique Technical**: DeepSeek v3
**🔬 Broad Technical**: Large Language Models, Commonsense Knowledge

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Commonsense Knowledge` • 

`Multilingual Evaluation` • 

`DeepSeek v3` • 

`Direct Preference Optimization`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16107v1 Announce Type: new 
Abstract: Ambiguous words or underspecified references require interlocutors to resolve them, often by relying on shared context and commonsense knowledge. Therefore, we systematically investigate whether Large Language Models (LLMs) can leverage commonsense to resolve referential ambiguity in multi-turn conversations and analyze their behavior when ambiguity persists. Further, we study how requests for simplified language affect this capacity. Using a novel multilingual evaluation dataset, we test DeepSeek v3, GPT-4o, Qwen3-32B, GPT-4o-mini, and Llama-3.1-8B via LLM-as-Judge and human annotations. Our findings indicate that current LLMs struggle to resolve ambiguity effectively: they tend to commit to a single interpretation or cover all possible references, rather than hedging or seeking clarification. This limitation becomes more pronounced under simplification prompts, which drastically reduce the use of commonsense reasoning and diverse response strategies. Fine-tuning Llama-3.1-8B with Direct Preference Optimization substantially improves ambiguity resolution across all request types. These results underscore the need for advanced fine-tuning to improve LLMs' handling of ambiguity and to ensure robust performance across diverse communication styles.

## 🔍 Abstract (한글 번역)

arXiv:2509.16107v1 발표 유형: 신규  
초록: 모호한 단어나 명시되지 않은 참조는 대화자들이 이를 해결해야 하며, 종종 공유된 맥락과 상식적 지식에 의존하게 됩니다. 따라서 우리는 대형 언어 모델(LLM)이 상식을 활용하여 다중 회전 대화에서 참조적 모호성을 해결할 수 있는지 체계적으로 조사하고, 모호성이 지속될 때 그들의 행동을 분석합니다. 또한, 간단한 언어 요청이 이 능력에 어떻게 영향을 미치는지 연구합니다. 새로운 다국어 평가 데이터셋을 사용하여, 우리는 DeepSeek v3, GPT-4o, Qwen3-32B, GPT-4o-mini, Llama-3.1-8B를 LLM-as-Judge 및 인간 주석을 통해 테스트합니다. 우리의 연구 결과는 현재의 LLM이 모호성을 효과적으로 해결하는 데 어려움을 겪고 있음을 나타냅니다: 그들은 단일 해석에 전념하거나 모든 가능한 참조를 포괄하는 경향이 있으며, 모호성을 피하거나 명확화를 추구하기보다는 그렇습니다. 이 제한은 간소화 요청 하에서 더욱 두드러지며, 이는 상식적 추론과 다양한 응답 전략의 사용을 크게 감소시킵니다. Llama-3.1-8B를 직접 선호 최적화로 미세 조정하면 모든 요청 유형에 걸쳐 모호성 해결이 크게 개선됩니다. 이러한 결과는 LLM의 모호성 처리 능력을 향상시키고 다양한 의사소통 스타일에서 강력한 성능을 보장하기 위한 고급 미세 조정의 필요성을 강조합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 다중 회차 대화에서 모호한 참조를 해결하는 능력을 연구합니다. 특히, 공통의 맥락과 상식적 지식을 활용해 참조 모호성을 해결할 수 있는지를 조사하며, 모호성이 지속될 때의 모델 행동을 분석합니다. 연구는 새로운 다국어 평가 데이터셋을 사용하여 DeepSeek v3, GPT-4o, Qwen3-32B, GPT-4o-mini, Llama-3.1-8B를 테스트하였으며, LLM-as-Judge와 인간 주석을 통해 평가했습니다. 결과적으로, 현재 LLM은 모호성을 효과적으로 해결하는 데 어려움을 겪으며, 단일 해석에 집착하거나 모든 가능한 참조를 포괄하는 경향이 있습니다. 특히, 단순화 요청 시 상식적 추론과 다양한 응답 전략 사용이 크게 감소합니다. Llama-3.1-8B의 세밀한 튜닝은 이러한 문제를 개선하여 모호성 해결 능력을 향상시켰습니다. 연구는 LLM의 모호성 처리 능력을 개선하기 위한 고급 튜닝의 필요성을 강조합니다.

## 🎯 주요 포인트


- 1. 대형 언어 모델(LLM)은 다중 회차 대화에서 참조적 모호성을 해결하는 데 어려움을 겪으며, 단일 해석에 집착하거나 모든 가능한 참조를 포괄하는 경향이 있다.

- 2. 단순화된 언어 요청은 상식적 추론과 다양한 응답 전략 사용을 크게 감소시켜 모호성 해결 능력을 저하시킨다.

- 3. Llama-3.1-8B 모델을 Direct Preference Optimization으로 미세 조정하면 모든 요청 유형에서 모호성 해결 능력이 크게 향상된다.

- 4. 연구 결과는 LLM의 모호성 처리 능력을 개선하고 다양한 의사소통 스타일에서의 강력한 성능을 보장하기 위해 고급 미세 조정이 필요함을 강조한다.


---

*Generated on 2025-09-22 16:29:23*