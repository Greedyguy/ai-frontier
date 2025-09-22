
# Is GPT-4o mini Blinded by its Own Safety Filters? Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection

**Korean Title:** GPT-4o mini는 자체 안전 필터에 의해 눈이 멀었는가? 혐오 발언 탐지에서의 멀티모달-유니모달 병목현상 노출

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unimodal Bottleneck

## 🔗 유사한 논문
- [[Multimodal Hate Detection Using Dual-Stream Graph Neural Networks]] (82.7% similar)
- [[Humor in Pixels Benchmarking Large Multimodal Models Understanding of Online Comics]] (81.4% similar)
- [[Language Models Identify Ambiguities and Exploit Loopholes]] (81.2% similar)
- [[Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary]] (80.9% similar)
- [[CyberLLMInstruct A Pseudo-malicious Dataset Revealing Safety-performance Trade-offs in Cyber Security LLM Fine-tuning]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13608v1 Announce Type: new 
Abstract: As Large Multimodal Models (LMMs) become integral to daily digital life, understanding their safety architectures is a critical problem for AI Alignment. This paper presents a systematic analysis of OpenAI's GPT-4o mini, a globally deployed model, on the difficult task of multimodal hate speech detection. Using the Hateful Memes Challenge dataset, we conduct a multi-phase investigation on 500 samples to probe the model's reasoning and failure modes. Our central finding is the experimental identification of a "Unimodal Bottleneck," an architectural flaw where the model's advanced multimodal reasoning is systematically preempted by context-blind safety filters. A quantitative validation of 144 content policy refusals reveals that these overrides are triggered in equal measure by unimodal visual 50% and textual 50% content. We further demonstrate that this safety system is brittle, blocking not only high-risk imagery but also benign, common meme formats, leading to predictable false positives. These findings expose a fundamental tension between capability and safety in state-of-the-art LMMs, highlighting the need for more integrated, context-aware alignment strategies to ensure AI systems can be deployed both safely and effectively.

## 🔍 Abstract (한글 번역)

arXiv:2509.13608v1 공고 유형: 신규
초록: 대규모 멀티모달 모델(LMMs)이 일상적인 디지털 생활의 핵심 요소가 되면서, 이들의 안전 아키텍처를 이해하는 것은 AI 정렬(AI Alignment)의 중요한 문제가 되었다. 본 논문은 전 세계적으로 배포된 모델인 OpenAI의 GPT-4o mini에 대해 멀티모달 혐오 발언 탐지라는 어려운 과제를 중심으로 체계적 분석을 제시한다. Hateful Memes Challenge 데이터셋을 사용하여 500개의 샘플에 대한 다단계 조사를 수행하여 모델의 추론 과정과 실패 모드를 탐구하였다. 우리의 핵심 발견은 "유니모달 병목(Unimodal Bottleneck)"의 실험적 식별로, 이는 모델의 고급 멀티모달 추론이 맥락을 고려하지 않는 안전 필터에 의해 체계적으로 선점되는 아키텍처 결함이다. 144개의 콘텐츠 정책 거부 사례에 대한 정량적 검증 결과, 이러한 우선적 개입이 유니모달 시각적 콘텐츠 50%와 텍스트 콘텐츠 50%에 의해 동등한 비율로 촉발됨을 확인하였다. 또한 이 안전 시스템이 취약하여 고위험 이미지뿐만 아니라 무해하고 일반적인 밈 형식도 차단함으로써 예측 가능한 거짓 양성(false positives)을 야기함을 실증하였다. 이러한 발견들은 최첨단 LMMs에서 역량과 안전성 간의 근본적인 긴장관계를 드러내며, AI 시스템이 안전하면서도 효과적으로 배포될 수 있도록 보다 통합적이고 맥락을 인식하는 정렬 전략의 필요성을 강조한다.

## 📝 요약

이 논문은 OpenAI의 GPT-4o mini 모델을 사용하여 다중 모드 혐오 발언 감지 문제를 분석합니다. 연구는 Hateful Memes Challenge 데이터셋을 활용하여 모델의 추론 및 실패 모드를 조사하였으며, 주요 발견은 "단일 모드 병목현상"이라는 구조적 결함을 실험적으로 확인한 것입니다. 이 결함은 모델의 고급 다중 모드 추론이 맥락을 고려하지 않는 안전 필터에 의해 방해받는 현상을 말합니다. 144개의 콘텐츠 정책 거부 사례를 분석한 결과, 시각적 콘텐츠와 텍스트 콘텐츠가 각각 50%씩 이 필터에 의해 차단된다는 것을 확인했습니다. 또한, 이 안전 시스템이 고위험 이미지만이 아니라 일반적인 밈 형식도 차단하여 예측 가능한 오탐을 발생시킨다는 점을 보여줍니다. 이러한 결과는 최신 다중 모드 모델에서 능력과 안전성 간의 근본적인 긴장을 드러내며, 보다 통합적이고 맥락을 고려한 정렬 전략의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 대규모 멀티모달 모델(LMM)의 안전성 구조 이해는 AI 정렬에서 중요한 문제로 부각되고 있다.

- 2. OpenAI의 GPT-4o mini 모델을 대상으로 멀티모달 혐오 발언 탐지 작업을 분석한 결과, "단일 모달 병목 현상"이라는 구조적 결함이 발견되었다.

- 3. 모델의 안전 필터가 맥락을 고려하지 않고 작동하여 고급 멀티모달 추론을 방해하는 것으로 나타났다.

- 4. 안전 시스템이 고위험 이미지만이 아니라 일반적인 밈 형식도 차단하여 오탐을 유발하는 취약성을 보였다.

- 5. LMM의 능력과 안전성 간의 근본적인 긴장을 드러내며, 맥락을 고려한 통합적인 정렬 전략의 필요성을 강조했다.

---

*Generated on 2025-09-19 11:14:23*