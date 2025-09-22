
# LLM-I: LLMs are Naturally Interleaved Multimodal Creators

**Korean Title:** LLM-I: LLM은 자연스러운 인터리브드 멀티모달 생성자이다

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interleaved Multimodal Framework

## 🔗 유사한 논문
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (84.0% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (83.8% similar)
- [[xGen-MM (BLIP-3) A Family of Open Large Multimodal Models]] (83.2% similar)
- [[$Agent^2$ An Agent-Generates-Agent Framework for Reinforcement Learning Automation]] (82.4% similar)
- [[Auto-Slides An Interactive Multi-Agent System for Creating and Customizing Research Presentations]] (82.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13642v1 Announce Type: new 
Abstract: We propose LLM-Interleaved (LLM-I), a flexible and dynamic framework that reframes interleaved image-text generation as a tool-use problem. LLM-I is designed to overcome the "one-tool" bottleneck of current unified models, which are limited to synthetic imagery and struggle with tasks requiring factual grounding or programmatic precision. Our framework empowers a central LLM or MLLM agent to intelligently orchestrate a diverse toolkit of specialized visual tools, including online image search, diffusion-based generation, code execution, and image editing. The agent is trained to select and apply these tools proficiently via a Reinforcement Learning (RL) framework that features a hybrid reward system combining rule-based logic with judgments from LLM and MLLM evaluators. Trained on a diverse new dataset using four different model backbones, LLM-I demonstrates state-of-the-art performance, outperforming existing methods by a large margin across four benchmarks. We also introduce a novel test-time scaling strategy that provides further performance gains. Project Page: https://github.com/ByteDance-BandAI/LLM-I.

## 🔍 Abstract (한글 번역)

arXiv:2509.13642v1 발표 유형: 신규
초록: 본 연구에서는 인터리브드(interleaved) 이미지-텍스트 생성을 도구 사용 문제로 재정의하는 유연하고 동적인 프레임워크인 LLM-Interleaved (LLM-I)를 제안한다. LLM-I는 합성 이미지에 제한되고 사실적 근거나 프로그래매틱 정밀성을 요구하는 작업에서 어려움을 겪는 기존 통합 모델들의 "단일 도구" 병목 현상을 극복하도록 설계되었다. 본 프레임워크는 중앙 LLM 또는 MLLM 에이전트가 온라인 이미지 검색, 확산 기반 생성, 코드 실행, 이미지 편집을 포함한 다양한 전문화된 시각적 도구 툴킷을 지능적으로 조율할 수 있도록 한다. 에이전트는 규칙 기반 논리와 LLM 및 MLLM 평가자들의 판단을 결합한 하이브리드 보상 시스템을 특징으로 하는 강화학습(RL) 프레임워크를 통해 이러한 도구들을 능숙하게 선택하고 적용하도록 훈련된다. 네 가지 서로 다른 모델 백본을 사용한 다양한 새로운 데이터셋으로 훈련된 LLM-I는 최첨단 성능을 입증하며, 네 개의 벤치마크에서 기존 방법들을 큰 폭으로 능가한다. 또한 추가적인 성능 향상을 제공하는 새로운 테스트 시간 스케일링 전략도 도입한다. 프로젝트 페이지: https://github.com/ByteDance-BandAI/LLM-I.

## 📝 요약

LLM-Interleaved(LLM-I)는 이미지-텍스트 생성 작업을 도구 활용 문제로 재구성하는 유연하고 동적인 프레임워크입니다. 기존 모델의 "하나의 도구" 한계를 극복하고자 설계되었으며, 사실적 기반이나 프로그래밍적 정밀성이 요구되는 작업에서 우수한 성능을 발휘합니다. 중앙 LLM 또는 MLLM 에이전트가 온라인 이미지 검색, 확산 기반 생성, 코드 실행, 이미지 편집 등 다양한 시각 도구를 지능적으로 조율합니다. 강화 학습을 통해 이 도구들을 효과적으로 선택하고 적용하도록 훈련되었으며, 네 가지 모델 백본을 사용한 새로운 데이터셋으로 학습하여 네 가지 벤치마크에서 기존 방법을 크게 능가하는 성과를 보였습니다. 또한, 성능 향상을 위한 새로운 테스트 시간 확장 전략을 도입했습니다.

## 🎯 주요 포인트

- 1. LLM-Interleaved(LLM-I)는 이미지-텍스트 생성 작업을 도구 사용 문제로 재구성하는 유연하고 동적인 프레임워크입니다.

- 2. LLM-I는 하나의 도구에 의존하는 기존 모델의 한계를 극복하고, 사실적 근거나 프로그래밍적 정밀성이 필요한 작업을 수행할 수 있도록 설계되었습니다.

- 3. 중앙 LLM 또는 MLLM 에이전트가 온라인 이미지 검색, 확산 기반 생성, 코드 실행, 이미지 편집 등 다양한 시각 도구를 지능적으로 조율합니다.

- 4. 강화 학습(RL) 프레임워크를 통해 에이전트가 도구를 능숙하게 선택하고 적용하도록 훈련되었으며, 규칙 기반 논리와 LLM 및 MLLM 평가자의 판단을 결합한 하이브리드 보상 시스템을 특징으로 합니다.

- 5. LLM-I는 새로운 데이터셋과 네 가지 모델 백본을 사용하여 훈련되었으며, 네 가지 벤치마크에서 기존 방법을 크게 능가하는 최첨단 성능을 보여줍니다.

---

*Generated on 2025-09-19 11:15:51*