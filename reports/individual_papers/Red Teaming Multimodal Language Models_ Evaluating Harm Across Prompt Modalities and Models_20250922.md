# Red Teaming Multimodal Language Models: Evaluating Harm Across Prompt Modalities and Models

**Korean Title:** 다중 모드 언어 모델의 레드 팀 작업: 프롬프트 모달리티와 모델 전반에 걸친 해악 평가

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Multimodal Safety Benchmarks|Multimodal Safety Benchmarks]] [[keywords/specific/Adversarial Prompts|Adversarial Prompts]] [[keywords/broad/Multimodal Large Language Models|Multimodal Large Language Models]] [[keywords/unique/Claude Sonnet 3.5|Claude Sonnet 3.5]] [[categories/cs.CL|cs.CL]] [[2025-09-18/Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection_20250918|Is GPT-4o mini Blinded by its Own Safety Filters? Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection]] (86.1% similar) [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming: Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (84.5% similar) [[2025-09-19/Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multimodal Safety Benchmarks
**🔗 Specific Connectable**: Adversarial Prompts
**🔬 Broad Technical**: Multimodal Large Language Models
**⭐ Unique Technical**: Pixtral 12B
## 🔗 유사한 논문
- [[2025-09-18/Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection_20250918|Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection]] (86.1% similar)
- [[2025-09-22/Toxicity Red-Teaming_ Benchmarking LLM Safety in Singapore's Low-Resource Languages_20250922|Toxicity Red-Teaming Benchmarking LLM Safety in Singapore's Low-Resource Languages]] (84.5% similar)
- [[2025-09-19/Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (83.9% similar)
- [[2025-09-18/MUSE_ MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models_20250918|MUSE MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models]] (83.7% similar)
- [[2025-09-22/Exploring the Impact of Personality Traits on LLM Bias and Toxicity_20250922|Exploring the Impact of Personality Traits on LLM Bias and Toxicity]] (83.5% similar)


**ArXiv ID**: [2509.15478](https://arxiv.org/abs/2509.15478)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15478.pdf)


**ArXiv ID**: [2509.15478](https://arxiv.org/abs/2509.15478)
**Published**: 2025-09-22
**Category**: cs.CL
**PDF**: [Download](https://arxiv.org/pdf/2509.15478.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multimodal Safety
**🔗 Specific Connectable**: Safety Benchmarks
**⭐ Unique Technical**: Claude Sonnet 3.5
**🔬 Broad Technical**: Multimodal Large Language Models, Adversarial Conditions

## 🏷️ 추출된 키워드



`Multimodal Large Language Models` • 

`Adversarial Prompts` • 

`Claude Sonnet 3.5` • 

`Multimodal Safety Benchmarks`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15478v1 Announce Type: new 
Abstract: Multimodal large language models (MLLMs) are increasingly used in real world applications, yet their safety under adversarial conditions remains underexplored. This study evaluates the harmlessness of four leading MLLMs (GPT-4o, Claude Sonnet 3.5, Pixtral 12B, and Qwen VL Plus) when exposed to adversarial prompts across text-only and multimodal formats. A team of 26 red teamers generated 726 prompts targeting three harm categories: illegal activity, disinformation, and unethical behaviour. These prompts were submitted to each model, and 17 annotators rated 2,904 model outputs for harmfulness using a 5-point scale. Results show significant differences in vulnerability across models and modalities. Pixtral 12B exhibited the highest rate of harmful responses (~62%), while Claude Sonnet 3.5 was the most resistant (~10%). Contrary to expectations, text-only prompts were slightly more effective at bypassing safety mechanisms than multimodal ones. Statistical analysis confirmed that both model type and input modality were significant predictors of harmfulness. These findings underscore the urgent need for robust, multimodal safety benchmarks as MLLMs are deployed more widely.

## 🔍 Abstract (한글 번역)

arXiv:2509.15478v1 발표 유형: 신규  
초록: 다중 모달 대형 언어 모델(MLLMs)은 실제 응용에서 점점 더 많이 사용되고 있지만, 적대적 조건에서의 안전성은 아직 충분히 탐구되지 않았습니다. 본 연구는 텍스트 전용 및 다중 모달 형식의 적대적 프롬프트에 노출될 때 네 가지 주요 MLLM(GPT-4o, Claude Sonnet 3.5, Pixtral 12B, Qwen VL Plus)의 무해성을 평가합니다. 26명의 레드 팀원이 불법 활동, 허위 정보, 비윤리적 행동의 세 가지 해악 범주를 목표로 726개의 프롬프트를 생성했습니다. 이러한 프롬프트는 각 모델에 제출되었고, 17명의 주석자가 5점 척도를 사용하여 2,904개의 모델 출력을 유해성으로 평가했습니다. 결과는 모델과 모달리티 간의 취약성에 있어 유의미한 차이를 보여주었습니다. Pixtral 12B는 가장 높은 비율의 유해한 응답(~62%)을 보였고, Claude Sonnet 3.5는 가장 저항력이 있었습니다(~10%). 예상과 달리, 텍스트 전용 프롬프트가 다중 모달 프롬프트보다 안전 메커니즘을 우회하는 데 약간 더 효과적이었습니다. 통계 분석은 모델 유형과 입력 모달리티가 유해성의 중요한 예측 변수임을 확인했습니다. 이러한 발견은 MLLM이 더 널리 배포됨에 따라 강력한 다중 모달 안전 벤치마크의 긴급한 필요성을 강조합니다.

## 📝 요약

이 연구는 다중모달 대형 언어 모델(MLLM)의 안전성을 평가했습니다. GPT-4o, Claude Sonnet 3.5, Pixtral 12B, Qwen VL Plus 등 4개의 주요 MLLM을 대상으로, 불법 활동, 허위 정보, 비윤리적 행동을 유도하는 726개의 적대적 프롬프트를 사용하여 모델의 무해성을 테스트했습니다. 결과적으로 Pixtral 12B는 가장 높은 유해 반응률(약 62%)을 보였고, Claude Sonnet 3.5는 가장 저항력이 높았습니다(약 10%). 텍스트 전용 프롬프트가 다중모달 프롬프트보다 안전 메커니즘을 우회하는 데 더 효과적이었습니다. 이러한 결과는 MLLM의 안전성 기준 마련의 필요성을 강조합니다.

## 🎯 주요 포인트


- 1. 본 연구는 네 가지 주요 다중모달 대형 언어 모델(MLLMs)의 안전성을 평가하며, 특히 적대적 조건에서의 무해성을 조사합니다.

- 2. 26명의 레드 팀원이 생성한 726개의 프롬프트를 통해 불법 활동, 허위 정보, 비윤리적 행동의 세 가지 해악 범주를 대상으로 모델을 테스트했습니다.

- 3. Pixtral 12B 모델은 약 62%의 높은 해로운 응답률을 보였으며, Claude Sonnet 3.5 모델은 약 10%로 가장 저항력이 높았습니다.

- 4. 텍스트 전용 프롬프트가 다중모달 프롬프트보다 안전 메커니즘을 우회하는 데 더 효과적이었습니다.

- 5. 연구 결과는 MLLMs의 널리 보급됨에 따라 강력한 다중모달 안전 기준의 필요성을 강조합니다.


---

*Generated on 2025-09-22 16:21:54*